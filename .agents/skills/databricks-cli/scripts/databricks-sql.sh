#!/usr/bin/env bash
# Submit SQL or resume polling an existing statement. Never resubmit on timeout.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/databricks-auth-hint.sh"

if [[ "${1:-}" == "--resume" ]]; then
    PROFILE="${2:?Usage: databricks-sql.sh --resume <profile> <statement_id>}"
    STATEMENT_ID="${3:?statement_id is required}"
    if [[ ! "${STATEMENT_ID}" =~ ^[a-zA-Z0-9_-]+$ ]]; then
        echo "Invalid statement_id: expected letters, digits, underscores or hyphens." >&2
        exit 1
    fi
    RESUME=true
else
    PROFILE="${1:?Usage: databricks-sql.sh <profile> <warehouse_id> <statement> [catalog] [schema]}"
    WAREHOUSE_ID="${2:?warehouse_id is required}"
    STATEMENT="${3:?SQL statement is required}"
    RESUME=false
fi

if ! command -v node >/dev/null 2>&1; then
    echo "Node.js is required to encode/decode Databricks JSON. Enable your installed Node.js runtime or rerun the platform installer without --skip-node." >&2
    exit 1
fi

if ! databricks_resolve_cli || ! databricks_is_signed_in "${PROFILE}"; then
    databricks_auth_hint "${PROFILE}"
    exit 2
fi

if [[ "${RESUME}" == "true" ]]; then
    RESPONSE="$(databricks_cli api get "/api/2.0/sql/statements/${STATEMENT_ID}" -p "${PROFILE}" -o json)"
else
    BODY="$(node "${SCRIPT_DIR}/databricks-json.mjs" request "${WAREHOUSE_ID}" "${STATEMENT}" "${4:-}" "${5:-}")"
    RESPONSE="$(databricks_cli api post /api/2.0/sql/statements -p "${PROFILE}" -o json --json "${BODY}")"
fi

STATUS="$(printf '%s' "${RESPONSE}" | node "${SCRIPT_DIR}/databricks-json.mjs" status)"
read -r STATEMENT_ID STATE <<< "${STATUS}"

ATTEMPT=0
while [[ "${STATE}" == "PENDING" || "${STATE}" == "RUNNING" ]] && (( ATTEMPT < 30 )); do
    sleep 4
    RESPONSE="$(databricks_cli api get "/api/2.0/sql/statements/${STATEMENT_ID}" -p "${PROFILE}" -o json)"
    STATUS="$(printf '%s' "${RESPONSE}" | node "${SCRIPT_DIR}/databricks-json.mjs" status)"
    read -r STATEMENT_ID STATE <<< "${STATUS}"
    ATTEMPT=$((ATTEMPT + 1))
done

if [[ "${STATE}" == "PENDING" || "${STATE}" == "RUNNING" ]]; then
    echo "Stopped waiting; statement ${STATEMENT_ID} is still ${STATE}. It has NOT been canceled. Do not resubmit it." >&2
    printf 'Resume checking: bash %q --resume %q %q\n' "${SCRIPT_DIR}/databricks-sql.sh" "${PROFILE}" "${STATEMENT_ID}" >&2
    printf '%s\n' "${RESPONSE}"
    exit 4
fi

if [[ "${STATE}" != "SUCCEEDED" ]]; then
    echo "Statement ${STATEMENT_ID} ended in state '${STATE}'." >&2
    printf '%s\n' "${RESPONSE}"
    exit 1
fi

printf '%s' "${RESPONSE}" | node "${SCRIPT_DIR}/databricks-json.mjs" result
