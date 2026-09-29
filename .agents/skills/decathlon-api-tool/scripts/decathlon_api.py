#!/usr/bin/env python3
"""
Decathlon API client with OAuth2 PKCE authentication.

Executes authenticated HTTP requests against Decathlon API endpoints.
Obtains tokens via browser-based PKCE flow (or env var) — never exposes
the token to the caller. Shares token storage with the Copilot CLI extension
(~/.config/decathlon-cli/tokens.json).

Usage:
    python3 decathlon_api.py --url https://api.decathlon.net/v1/products
    python3 decathlon_api.py --method GET --url "https://..." --param "key=val" "key2=val2"
    python3 decathlon_api.py --method POST --url "https://..." --data '{"key": "val"}'
    python3 decathlon_api.py --client-id C0fb07148f... --url "https://api.decathlon.net/deliverymetrics/..."

    python3 decathlon_api.py login [--client-id CLIENT_ID]
    python3 decathlon_api.py logout [--client-id CLIENT_ID]

Client ID resolution order (first match wins):
    1. --client-id CLI argument
    2. DECATHLON_CLIENT_ID environment variable
    3. Built-in default client ID

Stdlib only — works on macOS, Linux, and Windows without pip install.
"""

import argparse
import base64
import hashlib
import http.server
import json
import os
import pathlib
import secrets
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from collections.abc import Callable
from typing import Any


# ─── Constants ─────────────────────────────────────────────────────────────────

ALLOWED_APEX_DOMAINS = [
    "decathlon.net",
    "decathlon.com",
    "decathlon.io",
    "dktapp.cloud",
    "subsidia.org",
    "dkt.cloud",
]

AUTHORIZATION_ENDPOINT = "https://idpdecathlon.oxylane.com/as/authorization.oauth2"
TOKEN_ENDPOINT = "https://idpdecathlon.oxylane.com/as/token.oauth2"
REVOCATION_ENDPOINT = "https://idpdecathlon.oxylane.com/as/revoke_token.oauth2"

DEFAULT_CLIENT_ID = "C74d77aa9f495d86eb6480494a5cd4a705ec6f346"
DEFAULT_SCOPES = ["email", "openid", "profile"]
REDIRECT_PORT = 9786
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/oauth/redirect"
REDIRECT_PATH = "/oauth/redirect"
REFRESH_SKEW_SECONDS = 60
REQUEST_TIMEOUT = 30
MAX_RESPONSE_BYTES = 10 * 1024 * 1024


# ─── Domain validation ─────────────────────────────────────────────────────────

def validate_origin(url: str) -> str | None:
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != "https":
            return f'Insecure URL rejected: only HTTPS endpoints are allowed (got "{parsed.scheme}").'
        hostname = parsed.hostname.lower() if parsed.hostname else ""
        allowed = any(
            hostname == apex or hostname.endswith(f".{apex}")
            for apex in ALLOWED_APEX_DOMAINS
        )
        if not allowed:
            return (
                f'Hostname "{parsed.hostname}" is not in the Decathlon API allowlist. '
                f"Allowed domains: {', '.join(f'*.{d}' for d in ALLOWED_APEX_DOMAINS)}."
            )
    except Exception:
        return f'Invalid URL: "{url}".'
    return None


# ─── Token storage ─────────────────────────────────────────────────────────────

def _get_tokens_path() -> pathlib.Path:
    if sys.platform == "win32":
        base = pathlib.Path(os.environ.get("APPDATA", "~/AppData/Roaming"))
    else:
        base = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", "~/.config"))
    return base.expanduser() / "decathlon-cli" / "tokens.json"


def _load_session() -> dict[str, Any] | None:
    path = _get_tokens_path()
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _save_session(session: dict[str, Any]) -> None:
    path = _get_tokens_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(session, indent=2))
    path.chmod(0o600)


def _clear_session() -> None:
    path = _get_tokens_path()
    try:
        path.unlink()
    except FileNotFoundError:
        pass


# ─── PKCE helpers ──────────────────────────────────────────────────────────────

def _to_base64_url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _generate_pkce() -> tuple[str, str]:
    verifier = _to_base64_url(secrets.token_bytes(32))
    challenge = _to_base64_url(hashlib.sha256(verifier.encode()).digest())
    return verifier, challenge


# ─── Local callback server ─────────────────────────────────────────────────────

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    expected_state: str = ""
    result: dict[str, Any] = {}

    def log_message(self, fmt: str, *args: Any) -> None:
        pass

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path != REDIRECT_PATH:
            self._respond(404, "Not Found")
            return

        error = params.get("error", [None])[0]
        if error:
            desc = params.get("error_description", [error])[0]
            self._respond_html(400, "Authentication failed", f"<p>Error: {self._escape(desc)}</p>")
            type(self).result = {"error": f"OAuth error: {desc}"}
            return

        returned_state = params.get("state", [None])[0]
        if returned_state != self.expected_state:
            self._respond_html(400, "Authentication failed", "<p>Invalid state parameter.</p>")
            type(self).result = {"error": "Invalid state in OAuth callback"}
            return

        code = params.get("code", [None])[0]
        if not code:
            self._respond_html(400, "Authentication failed", "<p>No authorization code received.</p>")
            type(self).result = {"error": "No authorization code in OAuth callback"}
            return

        self._respond_html(200, "Authenticated!", "<p>You can close this tab.</p>")
        type(self).result = {"code": code}

    def _respond(self, status: int, body: str) -> None:
        encoded = body.encode()
        self.send_response(status)
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(encoded)

    def _respond_html(self, status: int, title: str, body: str) -> None:
        html = (
            f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{self._escape(title)}</title>'
            "<style>body{font-family:system-ui,sans-serif;max-width:480px;margin:80px auto;"
            "text-align:center;color:#333;}h1{color:#0070f3;}</style></head>"
            f"<body><h1>{self._escape(title)}</h1>{body}</body></html>"
        ).encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(html)

    def _escape(self, s: str) -> str:
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _start_callback_server(expected_state: str) -> dict[str, Any]:
    handler = CallbackHandler
    handler.expected_state = expected_state
    handler.result = {}

    server = http.server.HTTPServer(("127.0.0.1", REDIRECT_PORT), handler)
    server.timeout = 300

    server.handle_request()
    server.server_close()
    return handler.result


# ─── Token exchange & refresh ──────────────────────────────────────────────────

def _do_token_request(body: dict[str, str]) -> dict[str, Any]:
    data = urllib.parse.urlencode(body).encode()
    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"},
    )
    ctx = ssl.create_default_context(cafile=_find_ca_bundle())
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Token request failed ({e.code}): {text}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Token request failed: {e.reason}")


def _exchange_code(code: str, verifier: str, scopes: list[str], client_id: str) -> dict[str, Any]:
    return _do_token_request({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": client_id,
        "code_verifier": verifier,
        "scope": " ".join(sorted(scopes)),
    })


def _refresh_token(refresh_token: str, scopes: list[str], client_id: str) -> dict[str, Any]:
    return _do_token_request({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "scope": " ".join(sorted(scopes)),
    })


def _revoke_token(token: str, token_type_hint: str, client_id: str) -> None:
    data = urllib.parse.urlencode({
        "token": token,
        "token_type_hint": token_type_hint,
        "client_id": client_id,
    }).encode()
    req = urllib.request.Request(
        REVOCATION_ENDPOINT,
        data=data,
        method="POST",
    )
    ctx = ssl.create_default_context(cafile=_find_ca_bundle())
    try:
        urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx)
    except Exception:
        pass


def _build_session(tokens: dict[str, Any], scopes: list[str]) -> dict[str, Any]:
    expires_at = None
    if "expires_in" in tokens:
        expires_at = int(tokens["expires_in"]) * 1000 + _now_ms()
    return {
        "id": secrets.token_hex(16),
        "accessToken": tokens["access_token"],
        "refreshToken": tokens.get("refresh_token"),
        "expiresAt": expires_at,
        "scopes": sorted(scopes),
    }


def _now_ms() -> int:
    import time
    return int(time.time() * 1000)


# ─── Public token acquisition ──────────────────────────────────────────────────

def get_access_token(client_id: str = DEFAULT_CLIENT_ID) -> str:
    session = _load_session()

    if session:
        session["clientId"] = client_id
        _save_session(session)

        expires_at = session.get("expiresAt", 0)
        if expires_at and _now_ms() < expires_at - 300_000:
            return session["accessToken"]

        refresh_token = session.get("refreshToken")
        if refresh_token:
            try:
                scopes = session.get("scopes", DEFAULT_SCOPES)
                tokens = _refresh_token(refresh_token, scopes, client_id)
                access_token = tokens["access_token"]
                new_refresh = tokens.get("refresh_token", refresh_token)
                session.update({
                    "accessToken": access_token,
                    "refreshToken": new_refresh,
                    "expiresAt": (int(tokens["expires_in"]) * 1000 + _now_ms()) if "expires_in" in tokens else session.get("expiresAt"),
                    "clientId": client_id,
                })
                _save_session(session)
                return access_token
            except Exception:
                pass

    return _full_oauth_flow(client_id)


def _full_oauth_flow(client_id: str) -> str:
    verifier, challenge = _generate_pkce()
    state = secrets.token_hex(16)
    scopes = DEFAULT_SCOPES

    params = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "scope": " ".join(sorted(scopes)),
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    })
    auth_url = f"{AUTHORIZATION_ENDPOINT}?{params}"

    print("Decathlon authentication required. Opening browser...", file=sys.stderr)
    print(f"If the browser did not open, visit: {auth_url}", file=sys.stderr)

    webbrowser.open(auth_url)
    result = _start_callback_server(state)

    if "error" in result:
        raise RuntimeError(result["error"])

    tokens = _exchange_code(result["code"], verifier, scopes, client_id)
    new_session = _build_session(tokens, scopes)
    new_session["clientId"] = client_id
    _save_session(new_session)

    print("Authentication successful. Token stored locally.", file=sys.stderr)

    return new_session["accessToken"]


def _resolve_client_id(arg_value: str | None = None) -> str:
    """Resolve client ID: CLI arg > DECATHLON_CLIENT_ID env var > built-in default."""
    return arg_value or os.environ.get("DECATHLON_CLIENT_ID", DEFAULT_CLIENT_ID)


def _parse_client_id_from_argv(argv: list[str]) -> str:
    """Scan a raw argv list for --client-id VALUE and return the resolved client ID."""
    for i, arg in enumerate(argv):
        if arg == "--client-id" and i + 1 < len(argv):
            return argv[i + 1]
    return _resolve_client_id()


def logout(client_id: str = DEFAULT_CLIENT_ID) -> None:
    session = _load_session()
    if not session:
        return

    _clear_session()

    if session.get("refreshToken"):
        _revoke_token(session["refreshToken"], "refresh_token", client_id)
    _revoke_token(session["accessToken"], "access_token", client_id)


# ─── CA bundle discovery ───────────────────────────────────────────────────────

def _find_ca_bundle() -> str | None:
    paths = [
        os.environ.get("SSL_CERT_FILE"),
        os.environ.get("REQUESTS_CA_BUNDLE"),
        "/etc/ssl/cert.pem",
        "/etc/ssl/certs/ca-certificates.crt",
        "/etc/pki/tls/certs/ca-bundle.crt",
        "/usr/local/etc/openssl/cert.pem",
        "/usr/local/etc/ca-certificates/cert.pem",
    ]
    for p in paths:
        if p and os.path.isfile(p):
            return p
    return None


# ─── HTTP execution ────────────────────────────────────────────────────────────

def execute_request(
    method: str,
    url: str,
    token: str,
    data: str | None = None,
    params: list[str] | None = None,
) -> None:
    origin_error = validate_origin(url)
    if origin_error:
        print(json.dumps({"error": origin_error, "code": "ORIGIN_ERROR"}))
        sys.exit(1)

    target_url = url

    # Build query params for GET, body for others
    body_bytes = None
    if method == "GET":
        if data:
            print(json.dumps({"error": "--data is not supported with GET method", "code": "INVALID_USAGE"}))
            sys.exit(1)
        if params:
            qs_parts = []
            for p in params:
                if "=" in p:
                    key, val = p.split("=", 1)
                    qs_parts.append(f"{urllib.parse.quote(key)}={urllib.parse.quote(val)}")
            if qs_parts:
                separator = "&" if "?" in target_url else "?"
                target_url = f"{target_url}{separator}{'&'.join(qs_parts)}"
    else:
        if params:
            print(json.dumps({"error": "--param is only supported with GET method", "code": "INVALID_USAGE"}))
            sys.exit(1)
        if data:
            body_bytes = data.encode("utf-8")

    ctx = ssl.create_default_context(cafile=_find_ca_bundle())

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if body_bytes is not None:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        target_url,
        data=body_bytes,
        headers=headers,
        method=method,
    )

    # Track whether this is a retry after refresh
    retried = False

    while True:
        req.headers["Authorization"] = f"Bearer {token}"
        try:
            resp = urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx)
            body = resp.read().decode("utf-8")

            content_length = resp.headers.get("Content-Length")
            if content_length and int(content_length) > MAX_RESPONSE_BYTES:
                print(json.dumps({
                    "error": f"Response too large: content-length {content_length} exceeds {MAX_RESPONSE_BYTES}-byte limit",
                    "code": "RESPONSE_TOO_LARGE",
                }))
                sys.exit(1)

            if len(body) > MAX_RESPONSE_BYTES:
                print(json.dumps({
                    "error": f"Response truncated: {len(body)} bytes exceeds {MAX_RESPONSE_BYTES}-byte limit",
                    "code": "RESPONSE_TRUNCATED",
                }))
                sys.exit(1)

            sys.stdout.write(body)
            return

        except urllib.error.HTTPError as e:
            status = e.code
            body_text = e.read().decode("utf-8", errors="replace")

            if status == 401 and not retried:
                # Token expired — try to refresh
                session = _load_session()
                if session and session.get("refreshToken"):
                    client_id = session.get("clientId", DEFAULT_CLIENT_ID)
                    try:
                        tokens = _refresh_token(
                            session["refreshToken"],
                            session.get("scopes", DEFAULT_SCOPES),
                            client_id,
                        )
                        token = tokens["access_token"]
                        new_refresh = tokens.get("refresh_token", session["refreshToken"])
                        session.update({
                            "accessToken": token,
                            "refreshToken": new_refresh,
                            "expiresAt": (int(tokens["expires_in"]) * 1000 + _now_ms()) if "expires_in" in tokens else session.get("expiresAt"),
                            "clientId": client_id,
                        })
                        _save_session(session)
                        print("Token refreshed.", file=sys.stderr)
                        retried = True
                        continue
                    except Exception:
                        pass

                # Refresh failed or no refresh token — try full OAuth2
                try:
                    print("Token expired and refresh failed. Starting full authentication...", file=sys.stderr)
                    token = _full_oauth_flow(
                        session.get("clientId", DEFAULT_CLIENT_ID) if session else DEFAULT_CLIENT_ID,
                    )
                    retried = True
                    continue
                except Exception:
                    pass

            sys.stdout.write(body_text)
            sys.exit(1)

        except urllib.error.URLError as e:
            reason = str(e.reason)
            hint = ""
            if "CERTIFICATE_VERIFY_FAILED" in reason:
                hint = " Set SSL_CERT_FILE to your CA bundle path."
            print(json.dumps({"error": f"Connection failed: {reason}.{hint}", "code": "CONNECTION_ERROR"}))
            sys.exit(1)


# ─── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Execute authenticated HTTP requests against Decathlon APIs"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Absolute HTTPS URL of the Decathlon API endpoint",
    )
    parser.add_argument(
        "--method",
        default="GET",
        choices=["GET", "POST", "PUT", "DELETE"],
        help="HTTP method (default: GET)",
    )
    parser.add_argument(
        "--data",
        help='JSON body for POST/PUT/DELETE requests, e.g. \'{"key": "value"}\'',
    )
    parser.add_argument(
        "--param",
        action="append",
        help='Query parameter for GET requests, e.g. "key=value" (repeatable)',
    )
    parser.add_argument(
        "--client-id",
        default=None,
        dest="client_id",
        help=(
            "OAuth2 client ID override. "
            "Overrides the DECATHLON_CLIENT_ID env var and the built-in default. "
            "Use this when an API requires a different registered client "
            "(e.g. api.decathlon.net/deliverymetrics uses a different APIM client)."
        ),
    )

    args = parser.parse_args()

    # ─── Execution mode ────────────────────────────────────────────────────────────
    # Priority:
    #   1. DECATHLON_MOCK_RESPONSE  → return canned response, skip all I/O
    #   2. DECATHLON_TOKEN           → use as bearer token, skip OAuth flow
    #   3. Neither set               → run PKCE OAuth2 flow

    mock_response = os.environ.get("DECATHLON_MOCK_RESPONSE")
    if mock_response is not None:
        sys.stdout.write(mock_response)
        return

    decathlon_token = os.environ.get("DECATHLON_TOKEN")
    if decathlon_token:
        token = decathlon_token
    else:
        client_id = _resolve_client_id(args.client_id)
        token = get_access_token(client_id)

    execute_request(args.method, args.url, token, args.data, args.param)


# ─── Login / Logout helpers (for standalone use) ───────────────────────────────

def _cmd_login() -> None:
    client_id = _parse_client_id_from_argv(sys.argv[2:])
    token = get_access_token(client_id)
    print(f"Login successful. Token acquired (starts with: {token[:10]}...).", file=sys.stderr)


def _cmd_logout() -> None:
    client_id = _parse_client_id_from_argv(sys.argv[2:])
    logout(client_id)
    print("Logged out. Tokens revoked.", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "login":
            _cmd_login()
        elif sys.argv[1] == "logout":
            _cmd_logout()
        else:
            main()
    else:
        main()
