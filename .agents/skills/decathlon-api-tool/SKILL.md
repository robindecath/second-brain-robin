---
name: decathlon-api-tool
description: >
  Instructions for making authenticated HTTP requests to Decathlon API
  endpoints. Works in VS Code (via callDecathlonApi LM tool) and in any CLI
  agent (via the bundled Python script with OAuth2 PKCE flow).
  Supports GET, POST, PUT, DELETE with automatic token management.
  Examples: "get products from the Decathlon API", "create a new product",
  "update inventory", "delete an item".
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  owner: Decathlon Digital Platform
  version: "1.0.0"
  last-updated: "2026-07-15"
  audience: all
  domain: platform-engineering
  api: http
  mcp_required: false
---

# Decathlon API Tool

Provides instructions for making authenticated HTTP requests to Decathlon API endpoints. Authentication is handled by the bundled Python script (OAuth2 PKCE flow or pre-acquired token). Never use `http_request` directly — it lacks the bearer token and will fail with 401.

---

## Allowed domains

The bearer token is only sent to these domains (and any subdomain depth thereof):

`*.decathlon.net`, `*.decathlon.com`, `*.decathlon.io`, `*.dktapp.cloud`, `*.subsidia.org`, `*.dkt.cloud`

Only HTTPS is accepted (HTTP URLs are rejected).

---

## CLI Execution (Required for CLI Agents)

This is the method you MUST use when the `callDecathlonApi` VS Code LM tool is NOT available in your environment.

### Step 1 — Locate the script path

Call `read_skill` on this skill to load these instructions. Your system prompt contains an `<available_skills>` block. Find the `decathlon-api-tool` entry and read its `<location>` tag:

```
<skill>
  <name>decathlon-api-tool</name>
  <location>file:///path/to/decathlon-api-tool/SKILL.md</location>
</skill>
```

Strip `file://` (keep the leading `/`) then remove the trailing `/SKILL.md`:
→ `<skill-dir>` = `/path/to/decathlon-api-tool`

### Step 2 — Execute via shell

Use the `shell` tool to run the Python script. It handles authentication, domain validation, and HTTP execution.

**Command syntax:**
```bash
python3 <skill-dir>/scripts/decathlon_api.py --url <url> [options]
```

**Options:**
| Option | Description |
|--------|-------------|
| `--method GET\|POST\|PUT\|DELETE` | HTTP method (default: GET) |
| `--url <url>` | Absolute HTTPS URL (required) |
| `--data '<json>'` | JSON body for POST/PUT/DELETE |
| `--param "key=val"` | Repeatable query param for GET |

**Examples:**

```bash
# GET with query params
python3 <skill-dir>/scripts/decathlon_api.py \
  --method GET \
  --url "https://api.decathlon.net/v1/products" \
  --param "limit=10" \
  --param "offset=0"

# POST with JSON body
python3 <skill-dir>/scripts/decathlon_api.py \
  --method POST \
  --url "https://api.decathlon.net/v1/products" \
  --data '{"name": "Bike", "price": 499.99}'

# PUT
python3 <skill-dir>/scripts/decathlon_api.py \
  --method PUT \
  --url "https://api.decathlon.net/v1/products/123" \
  --data '{"price": 449.99}'

# DELETE
python3 <skill-dir>/scripts/decathlon_api.py \
  --method DELETE \
  --url "https://api.decathlon.net/v1/products/123"
```

### Step 3 — Response handling

1. **Exit code 0** — response body (raw JSON) written to stdout. Use it to answer the user.
2. **Non-zero exit** — an error occurred. Read stderr and stdout for the error details.
3. **HTTP errors** — the response body (from the API) is still written to stdout. Check the status code from the error message.
4. **Large responses** are capped at 10 MB; requests time out after 30 seconds.

---

## Environment Variables

The Python script reads these from the process environment (the shell inherits them automatically):

- `DECATHLON_TOKEN` — pre-acquired bearer token (skip OAuth flow, for CI/offline)
- `DECATHLON_MOCK_RESPONSE` — canned response for offline testing (the script writes this to stdout and exits immediately)
- `DECATHLON_CLIENT_ID` — custom OAuth2 client ID (uses default if unset)

---

## Hard Rules

1. **Never use `http_request`** — this tool does not have the bearer token and will always fail with 401. You MUST use the `shell` tool to run the Python script.
2. **Never use `get_env`** — the Python script reads env vars from its process environment automatically. Do NOT read them yourself.
3. **Always call `read_skill decathlon-api-tool` first** — resolve `<skill-dir>` from the `<location>` tag in `<available_skills>`. Never guess the path.
4. **Never fabricate data** — if the script exits non-zero or returns an error, report it to the user. Do not make up fake API responses.
5. **Retry on failure** — if the script exits non-zero, retry ONCE. If the second attempt also fails, report the error and stop.
6. **Always respond in English** — never use any other language.
