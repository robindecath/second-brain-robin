#!/usr/bin/env bash
#
# gws-fetch.sh — download a Google Workspace file as the cheapest text
# representation and report only a summary.
#
# Why: `gws docs documents get` / `gws slides presentations get` return the full
# structural JSON of a document (15 MB+ on a 47-slide deck). Exporting through
# Drive returns plain text or Markdown instead — typically 100–600x smaller.
#
# The content is written to a file and NEVER printed, so nothing enters the
# agent context until it is deliberately read (grep / view a line range).
#
# Usage:
#   gws-fetch.sh <url-or-id> [-o <path>] [--mime <mime>] [--print]
#
# Options:
#   -o, --out <path>   Output file (default: $TMPDIR/gws-fetch/<id>.<ext>)
#       --mime <mime>  Force an export MIME type instead of the default
#       --print        Also print the content to stdout (use only for small files)
#   -h, --help         Show this help
#
# Exit codes: 0 ok · 1 usage · 2 gws missing/not authenticated · 3 API failure

set -uo pipefail

# Shared auth diagnostics: prints the exact `gws auth login` command on failure.
# shellcheck source=gws-auth-hint.sh
. "$(cd "$(dirname "$0")" && pwd)/gws-auth-hint.sh"

usage() { sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'; }

SOURCE=""
OUT=""
FORCE_MIME=""
PRINT=0

while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help)  usage; exit 0 ;;
        -o|--out)   OUT="${2:-}"; shift 2 ;;
        --mime)     FORCE_MIME="${2:-}"; shift 2 ;;
        --print)    PRINT=1; shift ;;
        -*)         echo "error: unknown option $1" >&2; usage >&2; exit 1 ;;
        *)          if [ -z "${SOURCE}" ]; then SOURCE="$1"; else
                        echo "error: unexpected argument $1" >&2; exit 1
                    fi; shift ;;
    esac
done

[ -n "${SOURCE}" ] || { echo "error: missing <url-or-id>" >&2; usage >&2; exit 1; }

command -v gws >/dev/null 2>&1 || { echo "error: gws is not available." >&2; gws_auth_hint; exit 2; }

# ── Resolve the file ID and its kind from a URL, or accept a raw ID ──────────
ID=""
KIND=""
case "${SOURCE}" in
    *docs.google.com/document/d/*)     KIND="document";     ID="${SOURCE#*document/d/}" ;;
    *docs.google.com/spreadsheets/d/*) KIND="spreadsheet";  ID="${SOURCE#*spreadsheets/d/}" ;;
    *docs.google.com/presentation/d/*) KIND="presentation"; ID="${SOURCE#*presentation/d/}" ;;
    *drive.google.com/file/d/*)        ID="${SOURCE#*file/d/}" ;;
    *drive.google.com/open*id=*)       ID="${SOURCE#*id=}" ;;
    http*)  echo "error: unrecognized Google URL: ${SOURCE}" >&2; exit 1 ;;
    *)      ID="${SOURCE}" ;;
esac
ID="${ID%%/*}"; ID="${ID%%\?*}"; ID="${ID%%#*}"

[ -n "${ID}" ] || { echo "error: could not extract a file ID from: ${SOURCE}" >&2; exit 1; }

# ── Look up name + mimeType (cheap: a field mask, not the whole file) ────────
META=$(gws drive files get --params "{\"fileId\":\"${ID}\",\"fields\":\"name,mimeType,modifiedTime\",\"supportsAllDrives\":true}" 2>/dev/null)
if [ -z "${META}" ] || ! printf '%s' "${META}" | grep -q '"mimeType"'; then
    echo "error: could not read file ${ID}." >&2
    echo "  Either you are not signed in, or the file is not shared with your" >&2
    echo "  Decathlon account." >&2
    gws_auth_hint
    exit 3
fi

jsonval() { printf '%s' "$1" | sed -n "s/.*\"$2\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p" | head -1; }

NAME=$(jsonval "${META}" name)
MIME=$(jsonval "${META}" mimeType)
MODIFIED=$(jsonval "${META}" modifiedTime)

case "${MIME}" in
    application/vnd.google-apps.document)     KIND="document" ;;
    application/vnd.google-apps.spreadsheet)  KIND="spreadsheet" ;;
    application/vnd.google-apps.presentation) KIND="presentation" ;;
    application/vnd.google-apps.*)            KIND="${MIME##*.}" ;;
    *)                                        KIND="binary" ;;
esac

# ── Pick the cheapest text export for this kind ─────────────────────────────
# Supported export formats (Drive API):
#   document     → text/markdown (best), text/plain, text/html, application/pdf
#   presentation → text/plain, application/pdf   (no markdown)
#   spreadsheet  → text/csv (FIRST SHEET ONLY), text/tab-separated-values
EXPORT_MIME="${FORCE_MIME}"
EXT="txt"
if [ -z "${EXPORT_MIME}" ]; then
    case "${KIND}" in
        document)     EXPORT_MIME="text/markdown"; EXT="md" ;;
        presentation) EXPORT_MIME="text/plain";    EXT="txt" ;;
        spreadsheet)  EXPORT_MIME="text/csv";      EXT="csv" ;;
        binary)       EXPORT_MIME="";              EXT="bin" ;;
        *)            EXPORT_MIME="text/plain";    EXT="txt" ;;
    esac
else
    case "${EXPORT_MIME}" in
        text/markdown|text/x-markdown) EXT="md" ;;
        text/csv)                      EXT="csv" ;;
        text/html)                     EXT="html" ;;
        application/pdf)               EXT="pdf" ;;
        *)                             EXT="txt" ;;
    esac
fi

if [ -z "${OUT}" ]; then
    OUT_DIR="${TMPDIR:-/tmp}"; OUT_DIR="${OUT_DIR%/}/gws-fetch"
    mkdir -p "${OUT_DIR}"
    OUT="${OUT_DIR}/${ID}.${EXT}"
else
    mkdir -p "$(dirname "${OUT}")" 2>/dev/null || true
fi

# ── Export (Google-native) or download (binary) ──────────────────────────────
# gws refuses --output paths outside its working directory, so run it from the
# destination directory and pass a bare filename.
OUT_ABS="$(cd "$(dirname "${OUT}")" && pwd)/$(basename "${OUT}")"
OUT_DIRNAME="$(dirname "${OUT_ABS}")"
OUT_BASENAME="$(basename "${OUT_ABS}")"
OUT="${OUT_ABS}"

if [ -n "${EXPORT_MIME}" ]; then
    RESULT=$(cd "${OUT_DIRNAME}" && gws drive files export \
        --params "{\"fileId\":\"${ID}\",\"mimeType\":\"${EXPORT_MIME}\"}" \
        -o "${OUT_BASENAME}" 2>&1)
else
    RESULT=$(cd "${OUT_DIRNAME}" && gws drive files get \
        --params "{\"fileId\":\"${ID}\",\"alt\":\"media\",\"supportsAllDrives\":true}" \
        -o "${OUT_BASENAME}" 2>&1)
fi

if [ ! -s "${OUT}" ]; then
    echo "error: export failed for ${ID} (${KIND} → ${EXPORT_MIME:-raw})" >&2
    printf '%s\n' "${RESULT}" | tail -5 >&2
    echo "  Note: Drive export is capped at 10 MB. For very large files, read the" >&2
    echo "  document through its API with a 'fields' mask instead." >&2
    exit 3
fi

BYTES=$(wc -c < "${OUT}" | tr -d ' ')
LINES=$(wc -l < "${OUT}" | tr -d ' ')
WORDS=$(wc -w < "${OUT}" | tr -d ' ')

cat <<EOF
title:    ${NAME}
kind:     ${KIND}
modified: ${MODIFIED}
exported: ${EXPORT_MIME:-raw bytes}
path:     ${OUT}
size:     ${BYTES} bytes · ${LINES} lines · ${WORDS} words (~$((WORDS * 4 / 3)) tokens)
EOF

if [ "${KIND}" = "spreadsheet" ] && [ -z "${FORCE_MIME}" ]; then
    echo "note:     CSV export covers the FIRST sheet only. For another tab use:"
    echo "          gws sheets spreadsheets values get --format csv \\"
    echo "            --params '{\"spreadsheetId\":\"${ID}\",\"range\":\"TabName!A1:Z500\"}'"
fi

if [ "${PRINT}" -eq 1 ]; then
    echo "---"
    cat "${OUT}"
fi
