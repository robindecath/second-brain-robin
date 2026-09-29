#!/usr/bin/env bash
# Readiness checks never start the interactive OAuth browser login.
DEFAULT_PROFILE="dkt-expl"

databricks_config_file() {
    printf '%s\n' "${DATABRICKS_CONFIG_FILE:-${HOME}/.databrickscfg}"
}

databricks_resolve_cli() {
    DATABRICKS_CLI="$(command -v databricks 2>/dev/null)" && return 0
    local candidate
    for candidate in "${HOME}/homebrew/bin/databricks" "${HOME}/.local/bin/databricks" \
        "${LOCALAPPDATA:-${HOME}/AppData/Local}/Programs/databricks-cli/databricks.exe"; do
        if [ -x "${candidate}" ]; then
            DATABRICKS_CLI="${candidate}"
            return 0
        fi
    done
    return 1
}

databricks_cli() {
    if [ -z "${DATABRICKS_CLI:-}" ] && ! databricks_resolve_cli; then
        echo "Databricks CLI not found on PATH or in the platform install locations." >&2
        return 127
    fi
    "${DATABRICKS_CLI}" "$@"
}

databricks_is_signed_in() {
    # Preserve CLI errors: network/permission failures are not necessarily expired login.
    databricks_cli current-user me -p "$1" -o json >/dev/null
}

databricks_auth_hint() {
    local profile="${1:-${DEFAULT_PROFILE}}"
    local cfg; cfg="$(databricks_config_file)"
    if ! databricks_resolve_cli; then
        echo "Databricks CLI not found on PATH or in the platform install locations." >&2
        echo "Rerun the platform installer or install manually: https://docs.databricks.com/dev-tools/cli/install.html" >&2
        return 0
    fi

    if [ ! -f "${cfg}" ]; then
        echo "No Databricks config at ${cfg}. Create the selected profile using the login command below." >&2
    elif ! awk -v profile="${profile}" '
        { sub(/\r$/, ""); sub(/^[ \t]+/, ""); sub(/[ \t]+$/, "") }
        $0 == "[" profile "]" { found=1 }
        END { exit !found }
    ' "${cfg}"; then
        echo "Profile '${profile}' is missing in ${cfg}. Existing configs are preserved by the installer." >&2
        echo "Available profiles:" >&2
        if ! databricks_cli auth profiles >&2; then
            echo "Unable to list profiles; inspect your local config without sharing its contents." >&2
        fi
    else
        echo "Cannot reach the workspace for '${profile}'. Check the CLI error above for network, permission, or authentication problems." >&2
        echo "If authentication has expired, sign in again using the command below." >&2
    fi
    databricks_login_hint "${profile}"
}

databricks_login_hint() {
    local profile="${1:-${DEFAULT_PROFILE}}" host=""
    case "${profile}" in
        dkt-expl) host="https://decathlon-dataplatform-exploration.cloud.databricks.com" ;;
        dkt-indus) host="https://decathlon-dataplatform-indus.cloud.databricks.com" ;;
    esac
    {
        echo "Run this in your terminal (opens a browser; never run it headlessly):"
        printf '  '
        if [ -n "${DATABRICKS_CONFIG_FILE:-}" ]; then
            printf 'DATABRICKS_CONFIG_FILE=%q ' "${DATABRICKS_CONFIG_FILE}"
        fi
        printf '%q auth login -p %q' "${DATABRICKS_CLI:-databricks}" "${profile}"
        if [ -n "${host}" ]; then printf ' --host %q' "${host}"; fi
        printf '\n'
        if [ -z "${host}" ]; then
            echo "For a new custom profile, also pass --host with your confirmed workspace URL."
        fi
        echo "Sign in with your Decathlon account. Renew login when required by your organization's session policy."
    } >&2
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    PROFILE="${1:-${DEFAULT_PROFILE}}"
    if databricks_resolve_cli && databricks_is_signed_in "${PROFILE}"; then
        echo "databricks: ready (profile ${PROFILE})"
        exit 0
    fi
    databricks_auth_hint "${PROFILE}"
    exit 2
fi
