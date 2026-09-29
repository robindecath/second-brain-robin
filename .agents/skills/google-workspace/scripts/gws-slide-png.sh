#!/usr/bin/env bash
#
# gws-slide-png.sh — export one Google Slides slide as a PNG image.
#
# Why: a slide's meaning often lives in shapes, arrows and diagrams that carry
# no text at all. Text extraction alone loses it. This renders the slide so it
# can be looked at directly.
#
# Usage:
#   gws-slide-png.sh <url-or-id> <slide-number|objectId> [-o <path>] [--size SMALL|MEDIUM|LARGE]
#
# Options:
#   -o, --out <path>    Output PNG (default: $TMPDIR/gws-fetch/<id>-slide-NN.png)
#       --size <size>   SMALL (200px) · MEDIUM (800px) · LARGE (1600px, default)
#       --list          List every slide number → objectId, then exit
#   -h, --help          Show this help
#
# Exit codes: 0 ok · 1 usage · 2 gws missing/not authenticated · 3 API failure

set -uo pipefail

# Shared auth diagnostics: prints the exact `gws auth login` command on failure.
# shellcheck source=gws-auth-hint.sh
. "$(cd "$(dirname "$0")" && pwd)/gws-auth-hint.sh"

usage() { sed -n '2,19p' "$0" | sed 's/^# \{0,1\}//'; }

SOURCE=""; TARGET=""; OUT=""; SIZE="LARGE"; LIST=0

while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help) usage; exit 0 ;;
        -o|--out)  OUT="${2:-}"; shift 2 ;;
        --size)    SIZE="${2:-LARGE}"; shift 2 ;;
        --list)    LIST=1; shift ;;
        -*)        echo "error: unknown option $1" >&2; usage >&2; exit 1 ;;
        *)         if   [ -z "${SOURCE}" ]; then SOURCE="$1"
                   elif [ -z "${TARGET}" ]; then TARGET="$1"
                   else echo "error: unexpected argument $1" >&2; exit 1; fi; shift ;;
    esac
done

[ -n "${SOURCE}" ] || { echo "error: missing <url-or-id>" >&2; usage >&2; exit 1; }
[ "${LIST}" -eq 1 ] || [ -n "${TARGET}" ] || { echo "error: missing <slide-number|objectId>" >&2; exit 1; }

command -v gws >/dev/null 2>&1 || { echo "error: gws is not available." >&2; gws_auth_hint; exit 2; }

case "${SOURCE}" in
    *presentation/d/*) ID="${SOURCE#*presentation/d/}" ;;
    http*) echo "error: not a Google Slides URL: ${SOURCE}" >&2; exit 1 ;;
    *)     ID="${SOURCE}" ;;
esac
ID="${ID%%/*}"; ID="${ID%%\?*}"; ID="${ID%%#*}"

# Field mask keeps this at ~2 KB instead of the multi-MB full presentation.
IDS_JSON=$(gws slides presentations get \
    --params "{\"presentationId\":\"${ID}\",\"fields\":\"title,slides.objectId\"}" 2>/dev/null)

if [ -z "${IDS_JSON}" ] || ! printf '%s' "${IDS_JSON}" | grep -q objectId; then
    echo "error: could not read presentation ${ID}." >&2
    echo "  Either you are not signed in, or the deck is not shared with your" >&2
    echo "  Decathlon account." >&2
    gws_auth_hint
    exit 3
fi

OBJECT_IDS=$(printf '%s' "${IDS_JSON}" \
    | sed -n 's/.*"objectId"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
TOTAL=$(printf '%s\n' "${OBJECT_IDS}" | grep -c . || true)

if [ "${LIST}" -eq 1 ]; then
    printf '%s\n' "${OBJECT_IDS}" | grep . | nl -ba -w3 -s'  '
    echo "(${TOTAL} slides)"
    exit 0
fi

# A numeric target is a 1-based slide index; anything else is a raw objectId.
if printf '%s' "${TARGET}" | grep -qE '^[0-9]+$'; then
    if [ "${TARGET}" -lt 1 ] || [ "${TARGET}" -gt "${TOTAL}" ]; then
        echo "error: slide ${TARGET} out of range (presentation has ${TOTAL} slides)." >&2
        exit 1
    fi
    OBJECT_ID=$(printf '%s\n' "${OBJECT_IDS}" | grep . | sed -n "${TARGET}p")
    LABEL=$(printf '%02d' "${TARGET}")
else
    OBJECT_ID="${TARGET}"
    LABEL="${TARGET}"
fi

if [ -z "${OUT}" ]; then
    OUT_DIR="${TMPDIR:-/tmp}"; OUT_DIR="${OUT_DIR%/}/gws-fetch"
    mkdir -p "${OUT_DIR}"
    OUT="${OUT_DIR}/${ID}-slide-${LABEL}.png"
else
    mkdir -p "$(dirname "${OUT}")" 2>/dev/null || true
fi

THUMB=$(gws slides presentations pages getThumbnail --params \
    "{\"presentationId\":\"${ID}\",\"pageObjectId\":\"${OBJECT_ID}\",\"thumbnailProperties.thumbnailSize\":\"${SIZE}\"}" 2>/dev/null)

CONTENT_URL=$(printf '%s' "${THUMB}" | sed -n 's/.*"contentUrl"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
[ -n "${CONTENT_URL}" ] || {
    echo "error: no thumbnail returned for slide ${TARGET} (objectId ${OBJECT_ID})." >&2
    exit 3
}

# contentUrl is a short-lived, pre-signed Google URL — no auth header needed.
curl -sfL "${CONTENT_URL}" -o "${OUT}" || {
    echo "error: could not download the rendered slide." >&2
    exit 3
}
[ -s "${OUT}" ] || { echo "error: downloaded image is empty." >&2; exit 3; }

W=$(printf '%s' "${THUMB}" | sed -n 's/.*"width"[[:space:]]*:[[:space:]]*\([0-9]*\).*/\1/p' | head -1)
H=$(printf '%s' "${THUMB}" | sed -n 's/.*"height"[[:space:]]*:[[:space:]]*\([0-9]*\).*/\1/p' | head -1)

cat <<EOF
slide:    ${TARGET} of ${TOTAL} (objectId ${OBJECT_ID})
path:     ${OUT}
size:     ${W:-?}x${H:-?} px · $(wc -c < "${OUT}" | tr -d ' ') bytes
EOF
