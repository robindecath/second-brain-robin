---
name: protos-data-and-api-access
description: >
  Wires up authenticated Decathlon API access and optional persistent JSON
  storage for a Protos prototype during development — before it's ever
  deployed. Activate when the user asks to "set up protos data storage",
  "add API access to my prototype", "configure store.yaml", "let my prototype
  call Decathlon APIs", or similar dev-time requests for a repo that targets
  Decathlon's Protos platform. Scaffolds/updates a root-level store.yaml
  (declaring objects and readers/writers/admin roles via FedID subject IDs
  or support-group IDs), inserts a relative-fetch snippet for the /api/*
  proxy, and flags code that violates Protos' authentication and data
  boundaries. Complements the deploy-to-protos skill, which handles the
  actual CI/publish flow.
license: MIT
metadata:
  audience: developers
  domain: platform-engineering
  api: rest
  mcp_required: false
---

# Protos Data & API Access Skill

Sets up the two platform-owned integration points a Protos prototype is
allowed to use — the `/api/*` Decathlon API proxy and the `/data/*` persistent
JSON store — during development, before the prototype is ever published.

This is a **dev-time** skill. For creating/updating the CI workflow, triggering
a deployment, and following it to completion, use the sibling
**`deploy-to-protos`** skill instead. Use this skill first if the prototype
needs Decathlon API calls or persisted data; use `deploy-to-protos` once the
code is ready to ship.

---

## Platform Ground Rules (do not violate)

Protos owns three route prefixes. **Never** create application pages, static
files, or route handlers under these prefixes, and never add your own
authentication:

| Route | Purpose | What the prototype must do |
|---|---|---|
| `/api/*` | Authenticated proxy to `https://api.decathlon.net/*` | Call it with **relative fetches only** (`fetch("/api/...")`) |
| `/data/*` | Persistent JSON records declared in `store.yaml` | Use the CRUD contract below; declare objects in `store.yaml` |
| `/admin/*` | Platform data administration UI | Browser-only; link to it, don't rebuild it |

- **Never** call `https://api.decathlon.net` directly from the browser.
- **Never** add `Authorization` headers, bearer tokens, OAuth/FedID
  configuration, session or token storage, or refresh logic — Protos injects
  the signed-in user's token server-side.
- **Never** put personal or critical data anywhere in the prototype — no
  names, emails, employee/customer identifiers, payment/health data,
  credentials, or sensitive sample content. This applies to app code,
  persisted `/data` records, `store.yaml` itself, and CI publication
  provenance.
- **Never invent identities.** Only use FedID subject IDs or support-group IDs
  the user or their team actually provides.

---

## Step 1 — Decide what's needed

Ask (or infer from the user's request) which of these apply:
- Does the prototype need to call a Decathlon API? → Step 2
- Does the prototype need to persist records across sessions/users? → Step 3

Either, both, or neither may apply — skip steps that aren't needed.

---

## Step 2 — Wire up `/api/*` access

1. Scan the prototype's existing client code for violations before adding
   anything: direct calls to `api.decathlon.net`, any `Authorization` header,
   or OAuth/FedID setup. Flag and explain why each must be removed — Protos
   already handles auth server-side.
2. Insert/show a relative-fetch snippet matching the target endpoint, e.g.:
   ```ts
   const response = await fetch("/api/referential/flavor");

   if (!response.ok) {
     throw new Error(`Unable to load flavors (${response.status}).`);
   }

   const flavors = await response.json();
   ```
3. Handle non-OK responses in the UI — never fabricate fallback data when a
   call fails.

---

## Step 3 — Wire up `/data/*` persistence

1. Check for a root-level `store.yaml`. If missing, create one; if present,
   update it additively (don't clobber existing objects/roles without asking).
2. Ask the user (via `ask_user`) for the **object name(s)** to declare (e.g.
   `FlavorNotes` — alphanumeric, case-insensitive; exposed at the lowercase
   path, e.g. `/data/flavornotes`).
3. For **each** of the three roles — `readers`, `writers`, `admin` — ask the
   user how to grant it (readers grant reads, writers grant data changes,
   admin grants both data access and `/admin` access):
   - Specific **FedID subject IDs** (`users: [...]`) and/or
     **support-group IDs** (`support_groups: [...]`) the user/team provides.
   - `users: ["*"]` — an authenticated-only shorthand (literal value, not a
     glob) granting that one role to **every signed-in internal Protos
     user**. Usable independently per role. Explain this tradeoff clearly
     before applying it (fine for early internal testing, not a substitute
     for real access control before wider rollout).
   - Leave empty — grants **no one** access to that role. This is valid but
     means the feature is unusable until real IDs are added; say so
     explicitly rather than leaving it silently broken.
4. Write/update `store.yaml`:
   ```yaml
   data:
     readers:
       users: []
       support_groups: []
     writers:
       users: []
       support_groups: []
     admin:
       users: []
       support_groups: []
   objects:
     - FlavorNotes
   ```
5. Show the CRUD contract so the user knows how to call it from the client:

   | Operation | Request | Notes |
   |---|---|---|
   | List records | `GET /data/{object}` | ID-keyed map of JSON values |
   | Create a record | `POST /data/{object}/{id}` | 409 if the ID is already used |
   | Read a record | `GET /data/{object}/{id}` | 404 if missing |
   | Update a record | `PUT /data/{object}/{id}` | Full replace; 404 if missing |
   | Delete a record | `DELETE /data/{object}/{id}` | 404 if missing |

   Collection-level mutation methods (e.g. `POST /data/{object}`) are not
   supported and return `405`.

6. Provide a minimal client example against the declared object, e.g. for
   `flavornotes`:
   ```ts
   await fetch("/data/flavornotes/vanilla", {
     method: "POST",
     headers: { "Content-Type": "application/json" },
     body: JSON.stringify({ flavorId: "vanilla", comment: "Balanced.", note: 5 }),
   });
   ```
7. Before writing any example/sample data into the repo, re-check it against
   the boundaries above — no real names, emails, or identifiers, even as
   sample content.

---

## Step 4 — Hand off to deployment

Once API/data wiring is in place and boundary checks pass, tell the user the
prototype is ready to publish and point them at the **`deploy-to-protos`**
skill to create/update the CI workflow, trigger the deployment, and follow it
to completion.

---

## Edge Cases

| Situation | Handling |
|---|---|
| `store.yaml` already exists | Update additively; confirm with the user before changing existing roles/objects |
| User has no FedID/support-group IDs yet | Leave the role empty, explain it grants no access, don't invent IDs |
| Prototype needs broad internal access quickly | Offer `users: ["*"]` per-role, explain it's authenticated-only, not unrestricted |
| Existing code calls `api.decathlon.net` directly | Flag it, explain why, replace with a relative `/api/*` call |
| Existing code sets `Authorization` headers | Flag and remove — Protos supplies the token server-side |
| Sample/test data looks like real personal data | Ask the user to replace it before writing to the repo |

## Hard Rules

1. **Never** call `api.decathlon.net` directly or add auth headers/tokens — always use the relative `/api/*` proxy.
2. **Never invent** FedID subject IDs or support-group IDs — only use ones the user/team provides.
3. **Never** put personal or critical data in app code, `/data` records, `store.yaml`, or sample content.
4. **Never** silently overwrite an existing `store.yaml`'s objects/roles — confirm changes with the user.
5. **Always** explain the tradeoffs of `users: ["*"]` before applying it.
6. **Defer deployment/CI concerns to the `deploy-to-protos` skill** — this skill only wires up dev-time API/data access.
