#!/usr/bin/env bash
#
# gws-slide-text.sh — read the text of ONE Google Slides slide, or an outline
# of the whole deck.
#
# Why: the Drive plain-text export of a presentation contains NO slide
# delimiters, so it cannot answer "what is on slide 6?". And the full
# presentations.get payload is multi-MB. This fetches a single page with a
# text-only field mask (~4 KB) and prints just its text (~1 KB).
#
# Usage:
#   gws-slide-text.sh <url-or-id> <slide-number|objectId>
#   gws-slide-text.sh <url-or-id> --outline
#
# Options:
#       --outline      One line per slide: number, objectId, first text line
#   -h, --help         Show this help
#
# Exit codes: 0 ok · 1 usage · 2 gws missing/not authenticated · 3 API failure

set -uo pipefail

# Shared auth diagnostics: prints the exact `gws auth login` command on failure.
# shellcheck source=gws-auth-hint.sh
. "$(cd "$(dirname "$0")" && pwd)/gws-auth-hint.sh"

usage() { sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; }

SOURCE=""; TARGET=""; OUTLINE=0

while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help) usage; exit 0 ;;
        --outline) OUTLINE=1; shift ;;
        -*)        echo "error: unknown option $1" >&2; usage >&2; exit 1 ;;
        *)         if   [ -z "${SOURCE}" ]; then SOURCE="$1"
                   elif [ -z "${TARGET}" ]; then TARGET="$1"
                   else echo "error: unexpected argument $1" >&2; exit 1; fi; shift ;;
    esac
done

[ -n "${SOURCE}" ] || { echo "error: missing <url-or-id>" >&2; usage >&2; exit 1; }
[ "${OUTLINE}" -eq 1 ] || [ -n "${TARGET}" ] || {
    echo "error: missing <slide-number|objectId> (or --outline)" >&2; exit 1; }

command -v gws >/dev/null 2>&1 || { echo "error: gws is not available." >&2; gws_auth_hint; exit 2; }

case "${SOURCE}" in
    *presentation/d/*) ID="${SOURCE#*presentation/d/}" ;;
    http*) echo "error: not a Google Slides URL: ${SOURCE}" >&2; exit 1 ;;
    *)     ID="${SOURCE}" ;;
esac
ID="${ID%%/*}"; ID="${ID%%\?*}"; ID="${ID%%#*}"

# Turn the JSON "content" strings of one page into readable text.
# Slides splits a single paragraph into several styled text runs, sometimes
# mid-word, so the runs are concatenated first and only then split on the
# escaped newlines they carry.
page_text() {
    awk '
        match($0, /"content"[ \t]*:[ \t]*"/) {
            s = substr($0, RSTART + RLENGTH); sub(/"[ \t]*,?[ \t]*$/, "", s)
            buf = buf s
        }
        END {
            gsub(/\\n/, "\n", buf); gsub(/\\t/, " ", buf)
            gsub(/\\"/, "\"", buf); gsub(/\\\\/, "\\", buf)
            print buf
        }
    ' | sed 's/[[:space:]]*$//' | grep -v '^$'
}

fetch_page() {
    gws slides presentations pages get --params \
        "{\"presentationId\":\"${ID}\",\"pageObjectId\":\"$1\",\"fields\":\"pageElements(shape(text(textElements(textRun(content)))))\"}" \
        2>/dev/null
}

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

TITLE=$(printf '%s' "${IDS_JSON}" | sed -n 's/.*"title"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
OBJECT_IDS=$(printf '%s' "${IDS_JSON}" \
    | sed -n 's/.*"objectId"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | grep .)
TOTAL=$(printf '%s\n' "${OBJECT_IDS}" | grep -c . || true)

if [ "${OUTLINE}" -eq 1 ]; then
    # One request for the whole deck. The field mask puts "objectId" at slide
    # level only, so it reliably marks each slide boundary for the awk pass.
    OUTLINE_JSON=$(gws slides presentations get --params \
        "{\"presentationId\":\"${ID}\",\"fields\":\"slides(objectId,pageElements(shape(text(textElements(textRun(content))))))\"}" \
        2>/dev/null)
    [ -n "${OUTLINE_JSON}" ] || {
        echo "error: could not read presentation ${ID}." >&2; exit 3; }

    echo "title:  ${TITLE:-?} (${TOTAL} slides)"
    printf '%s\n' "${OUTLINE_JSON}" | awk '
        function clean(t) {
            gsub(/[ \t]+/, " ", t); gsub(/^ | $/, "", t); return substr(t, 1, 70)
        }
        function emit(i, id, f, a) {
            if (f == "") { f = clean(a); if (f == "") f = "(no text)" }
            printf "%3d  %-20s %s\n", i, id, f
        }
        match($0, /"objectId"[ \t]*:[ \t]*"[^"]*"/) {
            if (oid != "") emit(++n, oid, first, acc)
            s = substr($0, RSTART, RLENGTH); sub(/.*: *"/, "", s); sub(/"$/, "", s)
            oid = s; first = ""; acc = ""; next
        }
        first == "" && match($0, /"content"[ \t]*:[ \t]*"/) {
            s = substr($0, RSTART + RLENGTH); sub(/"[ \t]*,?[ \t]*$/, "", s)
            gsub(/\\n/, " ", s)
            # Slides splits one title into several styled text runs, sometimes
            # mid-word, so concatenate raw — the \n-turned-space separates shapes.
            acc = acc s
            if (length(acc) >= 70) first = clean(acc)
        }
        END { if (oid != "") emit(++n, oid, first, acc) }
    '
    exit 0
fi

# A numeric target is a 1-based slide index; anything else is a raw objectId.
if printf '%s' "${TARGET}" | grep -qE '^[0-9]+$'; then
    if [ "${TARGET}" -lt 1 ] || [ "${TARGET}" -gt "${TOTAL}" ]; then
        echo "error: slide ${TARGET} out of range (presentation has ${TOTAL} slides)." >&2
        exit 1
    fi
    OBJECT_ID=$(printf '%s\n' "${OBJECT_IDS}" | sed -n "${TARGET}p")
    POSITION="${TARGET} of ${TOTAL}"
else
    OBJECT_ID="${TARGET}"
    # Resolve the objectId back to its position so the label stays useful.
    POSITION=$(printf '%s\n' "${OBJECT_IDS}" | grep -n "^${OBJECT_ID}$" | cut -d: -f1)
    [ -n "${POSITION}" ] || {
        echo "error: no slide with objectId '${OBJECT_ID}' in this presentation (run --outline)." >&2
        exit 1
    }
    POSITION="${POSITION} of ${TOTAL}"
fi

PAGE_JSON=$(fetch_page "${OBJECT_ID}")
[ -n "${PAGE_JSON}" ] || {
    echo "error: could not read slide ${TARGET} (objectId ${OBJECT_ID})." >&2; exit 3; }

TEXT=$(printf '%s' "${PAGE_JSON}" | page_text)

echo "slide:  ${POSITION} (objectId ${OBJECT_ID}) — ${TITLE:-?}"
echo "---"
if [ -n "${TEXT}" ]; then
    printf '%s\n' "${TEXT}"
else
    echo "(no text on this slide — it is probably a diagram or an image;"
    echo " render it with gws-slide-png.sh and look at it)"
fi
