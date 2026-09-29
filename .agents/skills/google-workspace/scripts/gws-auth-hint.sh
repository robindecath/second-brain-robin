#!/usr/bin/env bash
#
# gws-auth-hint.sh — diagnose why gws cannot reach Google, and print the exact
# fix. Sourced by the other scripts; also runnable on its own as a check:
#
#   scripts/gws-auth-hint.sh
#
# Exit codes when run directly: 0 ready · 2 not installed / not signed in

# Kept in sync with GWS_LOGIN_SCOPES in
# src/copilot-extensions/decathlon-ai-augmented-sdlc/src/constants.ts, so the
# manual login grants exactly what the platform expects.
GWS_LOGIN_SCOPES="openid,email,profile,https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/documents,https://www.googleapis.com/auth/presentations,https://www.googleapis.com/auth/gmail.modify,https://www.googleapis.com/auth/gmail.settings.basic,https://www.googleapis.com/auth/calendar,https://www.googleapis.com/auth/tasks,https://www.googleapis.com/auth/contacts,https://www.googleapis.com/auth/contacts.other.readonly,https://www.googleapis.com/auth/directory.readonly,https://www.googleapis.com/auth/chat.spaces,https://www.googleapis.com/auth/chat.messages,https://www.googleapis.com/auth/chat.messages.reactions,https://www.googleapis.com/auth/chat.memberships,https://www.googleapis.com/auth/forms.body,https://www.googleapis.com/auth/forms.responses.readonly,https://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonly"

gws_config_dir() {
    if [ -d "${HOME}/.config/gws" ]; then
        echo "${HOME}/.config/gws"
    elif [ -d "${HOME}/Library/Application Support/gws" ]; then
        echo "${HOME}/Library/Application Support/gws"
    else
        echo "${HOME}/.config/gws"
    fi
}

# Print the remediation for whatever is actually wrong. Always to stderr, so it
# never pollutes a script's parsable stdout.
gws_auth_hint() {
    local dir; dir="$(gws_config_dir)"

    if ! command -v gws >/dev/null 2>&1; then
        {
            echo "  → gws is not installed. Run:"
            echo
            echo "     npm install -g @googleworkspace/cli"
            echo
            echo "     then sign in with the command below."
        } >&2
        gws_login_hint
        return 0
    fi

    # Signed in already? Then auth is not the problem — say so instead of
    # sending the user through a pointless login.
    if gws auth status 2>/dev/null \
        | grep -q '"token_valid"[[:space:]]*:[[:space:]]*true'; then
        {
            echo "  → You ARE signed in, so this is not an auth problem:"
            echo "     check the ID/URL, and that the item is shared with your"
            echo "     Decathlon account (open it in a browser to confirm)."
            echo "     If only one service returns 403, your token predates a"
            echo "     scope — re-consent by running:"
        } >&2
        gws_login_hint
        return 0
    fi

    if [ ! -f "${dir}/client_secret.json" ]; then
        {
            echo "  → No OAuth client at ${dir}/client_secret.json —"
            echo "     re-run the AI Augmented SDLC platform installer to write it,"
            echo "     then sign in with the command below."
        } >&2
    fi

    echo "  → You are not signed in." >&2
    gws_login_hint
}

# The login instructions. `gws auth login` prints a consent URL and then blocks
# on its localhost redirect listener — it does NOT open a browser itself, so the
# user has to open the printed URL by hand.
gws_login_hint() {
    {
        echo
        echo "     Run this in your terminal:"
        echo
        echo "     gws auth login --scopes ${GWS_LOGIN_SCOPES}"
        echo
        echo "     It prints a https://accounts.google.com/… URL and waits."
        echo "     Open that URL in your browser, sign in with your Decathlon"
        echo "     account and approve the permissions — the command completes"
        echo "     on its own once you do."
        echo
        echo "     Keep the --scopes list as-is: a bare 'gws auth login' grants"
        echo "     a narrower set that fails later."
    } >&2
}

# Direct invocation → act as a standalone readiness check.
case "${0##*/}" in
    gws-auth-hint.sh)
        if ! command -v gws >/dev/null 2>&1; then
            echo "gws: not installed" >&2; gws_auth_hint; exit 2
        fi
        STATUS=$(gws auth status 2>/dev/null)
        if printf '%s' "${STATUS}" | grep -q '"token_valid"[[:space:]]*:[[:space:]]*true'; then
            USER_EMAIL=$(printf '%s' "${STATUS}" \
                | sed -n 's/.*"user"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
            echo "gws: ready${USER_EMAIL:+ (${USER_EMAIL})}"
            exit 0
        fi
        echo "gws: not signed in" >&2
        gws_auth_hint
        exit 2
        ;;
esac
