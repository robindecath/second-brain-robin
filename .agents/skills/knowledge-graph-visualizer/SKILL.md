---
name: knowledge-graph-visualizer
description: >
  Generates an interactive network graph of Decathlon's digital asset topology
  by combining the AppReferential Knowledge Graph, DeliveryMetrics User Journeys,
  and SLO/SLI data. Visualises the hierarchy: Decathlon → domains → subdomains →
  products → components, with producer/consumer API relationships and User Journey
  SLO dependencies all rendered as a self-contained HTML file (Cytoscape.js).
  Supports scoped views: no filter (full graph), domain/subdomain filter, product
  filter (product + its components), and **incident impact mode** (traces cascade
  from a failing product/component to all impacted user journeys).
  Examples: "show me the full asset graph", "graph the Business Capability Platform domain",
  "show impact if OneFF has an incident", "map what components onecheckout exposes".
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
argument-hint: '[domain | subdomain | product-name | "incident on <name>"]'
user-invocable: true
version: 1.1.0
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  api: graphql+rest
  mcp_required: false
---

# Knowledge Graph Visualizer Skill

Orchestrates two data-source skills to collect Decathlon's digital asset topology,
then generates a self-contained interactive HTML graph using **Cytoscape.js** and
opens it in the browser.

---

## When to Use

- Visualise the full asset hierarchy (org → domain → subdomain → product → component)
- Map producer/consumer API dependencies between components
- Understand which User Journeys are exposed to a product's risk
- **Incident impact analysis**: given a failing product or component, identify all
  impacted components and User Journeys (blast radius)
- Explore a specific domain, subdomain, or product in isolation

---

## Prerequisite Skills

This skill **depends on** the following skills — load all of them in order before starting:

1. `decathlon-api-tool` — provides the `DecathlonApi` tool for authenticated HTTP calls
2. `knowledge-graph-query` — queries the AppReferential Knowledge Graph (GraphQL)
3. `delivery-metrics` — queries User Journeys and their moments from the DeliveryMetrics API

> All skills are referenced by **name only**. Call `read_skill <name>` for each before using it.

---

## Critical Data Model Facts

These facts are derived from the actual APIs and **must** be respected in all queries:

### Knowledge Graph (GraphQL)

- **`orgRefs` is always `{}`** (empty) for all asset kinds. Never use it for domain/team data.
- All governance data lives in **`metadata.governance`**:
  - `metadata.governance.domain` → domain name (e.g., `"BUSINESS CAPABILITY PLATFORM"`)
  - `metadata.governance.sub_domain` → subdomain (e.g., `"CUSTOMER"`, `"ORDER"`)
  - `metadata.governance.support_group` → team (e.g., `"CE-MEMBER-LOGIN"`)
  - `metadata.governance.tiering` → tiering integer (use the top-level `tiering` field too)
- **Domain names are full names** (e.g., `"BUSINESS CAPABILITY PLATFORM"`, `"DIGITAL WORKSPACE"`) — never abbreviations like "BCP".
- Use `metadataFilter: {"governance": {"domain": "EXACT DOMAIN NAME"}}` for domain filtering.
- Products have an **inline `components { name type }` field** — use it instead of separate component queries when doing product-level views.
- Component `relationships` contain `type` values: `"partOf"` (links component to parent product), `"deploysTo"` (links to cluster, skip). There are **no** `"PRODUCES"`/`"CONSUMES"` relationship types.
- **Producer-consumer links are in `metadata`**, not in `relationships`:
  - `metadata.apis_provided` → array of API UUIDs this component **exposes**
  - `metadata.apis_consumed` → array of API UUIDs this component **calls**
  - To build edges: fetch all DECATHLON_API components globally, cross-reference `apis_provided` UUIDs with `apis_consumed` UUIDs across components. A matching UUID means consumer→producer edge.
- **Component types to skip** (noise, not meaningful for dependency graphs): `LIBRARY`, `DOCUMENTATION`

### DeliveryMetrics API (REST)

- **User Journeys do NOT have `slo_keys`** at the top level. The UJ object only has:
  `{ uuid, name, description, domain (UUID), criticality, slo_target }`
- **`slo_keys` live in Moments**, fetched via:
  `GET /api/v1/user_journeys/<uj_uuid>/moments`
  Each moment has: `{ uuid, name, slo_keys: [...], sequence, product_uuids: [...] }`
- **The v2 UJ list is paginated** with: `{ content: [...], page: { size, number, total_elements, total_pages } }`
  Fetch all pages using `page=0,1,2...` until `page.number >= total_pages - 1`.
- Default page size is 20; use `size=50` to reduce API calls.
- UJ `domain` field is a **UUID**, not a human-readable name — cannot filter UJs by domain name directly.

### SLO Key to Product Matching

The `slo_keys` in moments follow the naming convention:
`slo-<product-or-component-slug>-<feature>-<metric>-<env>`

To link a UJ to a KG product/component:
1. For each SLO key, strip the `"slo-"` prefix
2. Extract the first one or two hyphen-separated tokens as the slug (e.g., `"slo-onecheckout-cart-..."` → slug `"onecheckout"`)
3. Normalize KG product/component names to lowercase (e.g., `"OneCheckout"` → `"onecheckout"`)
4. Match: if the KG name lowercase equals the extracted slug, link the UJ to that asset

This is fuzzy but reliable for well-named products. Report unmatched SLO keys as informational.

---

## Thinking Flow

### ⚠️ Critical Rules Before Starting

**The `shell` tool response (or `callDecathlonApi` LM tool) is the single source of
truth** for all API data.
- Never fabricate, guess, or hallucinate asset names, domain names, or SLO keys.
- Never use `http_request` directly — it lacks the bearer token and will return 401.
- If an API call returns empty results for a filter, report "not found" and suggest
  alternatives. Do NOT proceed with invented data.

**Pagination is MANDATORY — never stop at page 1:**
- The KG currently contains **300+ DECATHLON_API components across 5+ pages** (200 per page).
- The DeliveryMetrics API currently has **50+ User Journeys across 3+ pages** (use `size=50`).
- If you stop at page 1 of either dataset, the consumer/UJ map will be severely incomplete
  and the incident impact analysis will be wrong.
- After completing Step 3b, verify your script printed at least 2 page fetches. If you see
  only 1 page, the loop is broken — debug and re-run before proceeding.

---

### Step 1 — Parse User Intent

Extract:

| Field | Description |
|---|---|
| **filter_type** | `none` / `domain` / `subdomain` / `product` |
| **filter_value** | The name to filter on — null if no filter. For domain filter, use full domain name (not abbreviation). |
| **mode** | `normal` or `incident` |
| **incident_target** | The failing product or component name (incident mode only) |

**Incident mode detection** — activate when the user message contains any of:
`incident`, `impact`, `impacted`, `failing`, `failed`, `down`, `outage`, `degraded`,
`what if X fails`, `cascade`

**Domain name resolution**: If the user says "BCP domain", resolve to full name
`"BUSINESS CAPABILITY PLATFORM"`. If unsure, query the KG for a sample of products
without filters, inspect `metadata.governance.domain` values, and pick the closest match.

---

### Step 2 — Load Prerequisite Skills

Call `read_skill` for each required skill in this order:

```
read_skill knowledge-graph-query
read_skill delivery-metrics
```

---

### Step 3 — Collect Asset Hierarchy from the Knowledge Graph

**GraphQL endpoint:** `https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql`

Use `knowledge-graph-query` patterns (via `DecathlonApi` tool) for all queries.

#### 3a — Products + inline components

Fetch products with their inline components. `filter_type` determines the filter:

```json
{
  "query": "query Products($f: AssetFilter!, $n: Int!, $c: String) { assets(filter: $f, first: $n, after: $c) { totalCount edges { node { name id kind type tiering metadata links { type title url } components { name type } } } pageInfo { hasNextPage endCursor } } }",
  "variables": {
    "f": { "kind": "product" },
    "n": 200
  }
}
```

Apply filter in `variables.f`:
- **domain filter**: `"metadataFilter": {"governance": {"domain": "EXACT FULL DOMAIN NAME"}}`
- **subdomain filter**: `"metadataFilter": {"governance": {"domain": "X", "sub_domain": "Y"}}`
- **product filter**: skip this query; use `asset(name: ...)` single lookup instead (see 3c)

Paginate while `pageInfo.hasNextPage = true` using `after: endCursor`.

**From each product node extract** (NOTE: `orgRefs` is always `{}` — use `metadata` only):
```python
metadata = node["metadata"]  # already a dict
domain     = metadata["governance"]["domain"]
subdomain  = metadata["governance"].get("sub_domain")
team       = metadata["governance"].get("support_group")
tiering    = node["tiering"]  # integer 1/2/3 or null
components = node["components"]  # [{"name": "...", "type": "..."}, ...]
```

Build unique domain nodes and subdomain nodes from this data across all products.

**Filter**: When iterating inline `components`, **skip components with these types**:
- `LIBRARY` — library packages, not meaningful for dependency graphs
- `DOCUMENTATION` — doc sites, not meaningful for dependency graphs

Only add nodes for: `DECATHLON_API`, `WEB_FRONTEND`, `BATCH`, `STREAMING`, `BACKEND_FOR_FRONTEND`, and similar service/runtime types.

#### 3b — DECATHLON_API producer-consumer map (global fetch — ALL pages required)

> ⚠️ **CRITICAL: You MUST fetch ALL pages.** The KG currently contains **300+ DECATHLON_API
> components spread across 5+ pages** (max 200 per page). Stopping after the first page will
> silently miss the majority of consumers and produce a wrong/incomplete impact graph.
> The only acceptable exit condition is `pageInfo.hasNextPage === false`.

To build API dependency edges, you must fetch **all** DECATHLON_API components across **all domains**.
Consumers of a BCP API often live in ECOMMERCE, FLTC, IN-STORE, FRANCE, SPAIN and other domains.

**Use this Python script** — run it with `python3` via the `shell` tool. It handles the full
pagination loop and outputs the complete `api_edges` JSON to stdout:

```python
import os, subprocess, json, sys

SCRIPT = os.environ["DECATHLON_API_SCRIPT"]
GRAPH_URL = "https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql"

QUERY = """
query ApiComponents($n: Int!, $c: String) {
  assets(filter: {kind: "component", type: "DECATHLON_API"}, first: $n, after: $c) {
    edges { node { name metadata } }
    pageInfo { hasNextPage endCursor }
  }
}
"""

provided_map = {}   # api_uuid -> {"name": comp_name, "domain": comp_domain}
consumed_by  = {}   # api_uuid -> [{"name": comp_name, "domain": comp_domain}, ...]
cursor = None
page = 0

while True:
    variables = {"n": 200}
    if cursor:
        variables["c"] = cursor

    result = subprocess.run([
        "python3", SCRIPT,
        "--method", "POST",
        "--url", GRAPH_URL,
        "--data", json.dumps({"query": QUERY, "variables": variables})
    ], capture_output=True, text=True)

    resp = json.loads(result.stdout)
    assets_data = resp["data"]["assets"]
    page += 1

    for edge in assets_data["edges"]:
        n    = edge["node"]
        meta = n.get("metadata") or {}
        gov  = meta.get("governance", {})
        name   = n["name"]
        domain = gov.get("domain", "unknown")
        for uuid in meta.get("apis_provided", []):
            provided_map[uuid] = {"name": name, "domain": domain}
        for uuid in meta.get("apis_consumed", []):
            consumed_by.setdefault(uuid, []).append({"name": name, "domain": domain})

    sys.stderr.write(f"Page {page}: fetched {len(assets_data['edges'])} components, hasNextPage={assets_data['pageInfo']['hasNextPage']}\n")

    if not assets_data["pageInfo"]["hasNextPage"]:
        break
    cursor = assets_data["pageInfo"]["endCursor"]

# Build edges
api_edges = []
for api_uuid, producer in provided_map.items():
    for consumer in consumed_by.get(api_uuid, []):
        if consumer["name"] != producer["name"]:   # skip self-loops
            api_edges.append({
                "id":       f"component:{consumer['name']}--component:{producer['name']}--consumes",
                "source":   f"component:{consumer['name']}",
                "target":   f"component:{producer['name']}",
                "type":     "consumes",
                "external": consumer["domain"] != producer["domain"]
            })

print(json.dumps({
    "pages_fetched": page,
    "total_providers": len(provided_map),
    "total_consumer_relations": len(api_edges),
    "api_edges": api_edges
}, indent=2))
```

> **Set `DECATHLON_API_SCRIPT`** environment variable to the path of `decathlon_api.py` from the `decathlon-api-tool` skill.

After running, verify the output shows `pages_fetched >= 2` (expect 5 for the full KG). If you
see `pages_fetched: 1`, **the pagination loop did not execute** — do not proceed with incomplete data.

`external: true` marks edges where the consumer is from a different domain (important for incident impact).

#### 3c — Component details for the filtered domain (team, links)

For the filtered domain, fetch component metadata to enrich nodes with team and links:

```json
{
  "query": "query Components($f: AssetFilter!, $n: Int!, $c: String) { assets(filter: $f, first: $n, after: $c) { edges { node { name type tiering metadata links { type title url } } } pageInfo { hasNextPage endCursor } } }",
  "variables": {
    "f": { "kind": "component", "metadataFilter": {"governance": {"domain": "EXACT DOMAIN"}} },
    "n": 200
  }
}
```

Also paginate this query until `hasNextPage = false` — some domains have > 200 components.

Skip `LIBRARY` and `DOCUMENTATION` components — do not add them to the node list.

> ⚠️ **Never query `kind: "cluster"`** — cluster/infrastructure nodes clutter the graph and
> carry no meaningful business information. Skip all `deploysTo` relationships.

#### 3d — Single product lookup (product filter mode)

When `filter_type = "product"`:

```json
{
  "query": "query Asset($n: String!) { asset(name: $n) { name kind type tiering metadata links { type title url } components { name type metadata } relationships { type targetAsset { name kind tiering } } } }",
  "variables": { "n": "<filter_value>" }
}
```

> ⚠️ **Even in product/incident filter mode, you MUST still run Step 3b** (the global
> DECATHLON_API pagination script). The incident impact analysis requires the full
> cross-domain consumer map. A product-only fetch only shows local components, not who
> depends on them from other domains.

---

### Step 4 — Collect User Journeys and Their Moments

#### 4a — Fetch all UJ pages

Iterate pages until `page.number >= page.total_pages - 1`:

```
GET https://api.decathlon.net/deliverymetrics/api/v2/user_journeys
params: { "size": 50, "page": <page_number> }
```

Response shape:
```json
{
  "content": [
    { "uuid": "...", "name": "...", "description": "...", "domain": "<UUID>", "criticality": 1, "slo_target": 99.9 }
  ],
  "page": { "size": 50, "number": 0, "total_elements": 50, "total_pages": 1 }
}
```

#### 4b — Fetch moments for each UJ

For each UJ UUID collected in 4a, call:
```
GET https://api.decathlon.net/deliverymetrics/api/v1/user_journeys/<uj_uuid>/moments
```

Response (array):
```json
[
  { "uuid": "...", "name": "...", "slo_keys": ["slo-login-auth-...", "slo-core-..."], "sequence": 0, "product_uuids": ["<delivery-metrics-product-uuid>"] }
]
```

From all moments, **aggregate SLO keys per UJ**:
```python
uj_slo_keys = {}  # { uj_uuid: set of all slo_keys across all moments }
for moment in moments:
    uj_slo_keys[uj_uuid].update(moment["slo_keys"])
```

**Efficiency note**: With ~50 UJs this requires ~50 API calls. This is expected and acceptable.
If the dataset is large, prioritise UJs with criticality ≤ 2.

#### 4c — Build the SLO key index

```python
# Build reverse index: normalised_product_slug -> [uj_uuid, ...]
import re
slug_to_ujs = {}
for uj_uuid, slo_keys in uj_slo_keys.items():
    for key in slo_keys:
        # Strip "slo-" prefix (some keys don't have it)
        slug_part = re.sub(r'^slo-', '', key)
        # Take first token as the product/component slug
        slug = slug_part.split('-')[0]
        slug_to_ujs.setdefault(slug, set()).add(uj_uuid)

# Normalise KG product/component names to slugs for matching
def to_slug(name):
    # "OneCheckout" -> "onecheckout", "oneff-api" -> "oneff"
    return re.sub(r'[^a-z0-9]', '', name.lower().split('-')[0])
```

---

### Step 5 — Build Graph Data Model

Construct two arrays: `nodes` and `edges`.

#### Node schema
```json
{
  "id": "component:<name>",
  "label": "<display-name>",
  "group": "org|domain|subdomain|product|component|user_journey",
  "comp_type": "DECATHLON_API",
  "tiering": 1,
  "team": "...",
  "domain": "BUSINESS CAPABILITY PLATFORM",
  "external": false,
  "links": [{ "type": "...", "url": "..." }],
  "incident": false,
  "impacted": false
}
```

`external: true` marks component nodes from outside the filtered domain (cross-domain consumers).

#### Edge schema
```json
{
  "id": "<source>--<target>--<type>",
  "source": "<node-id>",
  "target": "<node-id>",
  "type": "contains|consumes|slo_link",
  "external": false
}
```

#### Hierarchy construction
1. Add root: `{ id: "org:decathlon", label: "Decathlon", group: "org" }`
2. For each unique domain: add node + edge `org:decathlon → domain:<X>` (contains)
3. For each unique subdomain: add node + edge `domain:<X> → subdomain:<Y>` (contains)
4. For each product: add node + edge `subdomain:<Y> → product:<name>` (or `domain:<X>` if no subdomain)
5. For each component (from product's inline `components` list), **skip `LIBRARY` and `DOCUMENTATION` types**:
   - Add component node + edge `product:<name> → component:<comp_name>` (contains)
6. Add producer-consumer edges from the `api_edges` list built in Step 3b:
   - If the consumer node (`component:<name>`) is NOT yet in the nodes list → add it as an `external` node
     `{ id: "component:<name>", label: "<name>", group: "component", domain: "<their-domain>", external: true }`
   - Add the `consumes` edge: `consumer → producer`
7. UJ linking: for each product/component in the filtered domain, compute `to_slug(name)` and check `slug_to_ujs`:
   - If match found: add UJ node (if not yet present) + `slo_link` edge

#### Incident mode tagging
1. Mark the `incident_target` node: `incident: true`
2. BFS outward along all edge types from the incident node (follow `consumes` edges **towards** consumers = who depends on the failing component)
3. Mark all reachable nodes: `impacted: true`

---

### Step 6 — Generate and Display the HTML Graph

Generate a **self-contained HTML file** using Cytoscape.js + the **`fcose`** layout.

#### Why fcose?

`fcose` (Force-directed Compound Spring Embedder) is the recommended Cytoscape layout
for complex graphs with 100–1000 nodes. It groups connected nodes organically so that
product clusters visibly separate from each other, making the graph immediately readable.
It requires 3 CDN scripts loaded in order (all verified working):

```
https://unpkg.com/layout-base@2.0.1/layout-base.js     (dependency of cose-base)
https://unpkg.com/cose-base@2.2.0/cose-base.js          (dependency of fcose)
https://unpkg.com/cytoscape-fcose@2.2.0/cytoscape-fcose.js  (the layout plugin)
```

All three use UMD format and auto-register when `cytoscape` is present in the global scope.
Load them **after** `cytoscape.min.js` and **before** your script block.

> ⚠️ **Never use** `cytoscape-cose-bilkent@4.1.0/dist/cytoscape-cose-bilkent.cjs` — that path
> returns 404. The correct file for cose-bilkent is `.js` not `.cjs`, but fcose is preferred.

#### Required UI controls

The generated HTML **must** include these four controls in the top bar.
The toggle buttons show their current state visually (active = highlighted):

| Button | id | Default state | What it does |
|---|---|---|---|
| ⊡ Fit | `btn-fit` | — | `cy.fit()` to zoom-to-fit all visible nodes |
| 🌐 External Consumers | `btn-external` | **ON** (visible) | Show/hide external consumer nodes + their `consumes` edges |
| 👥 User Journeys | `btn-uj` | **OFF** (hidden) | Show/hide `user_journey` nodes + `slo_link` edges |
| 🏷 Labels | `btn-labels` | **ON** (visible) | Show/hide all node labels |

> **UJs start hidden** because on large domain graphs they add dozens of diamond nodes that
> clutter the layout. The user opts in by clicking the button.
>
> **External consumers start visible** because they are the primary value of incident impact
> mode — hiding them by default would defeat the purpose.

Each toggle button must update its own CSS class to reflect state:
- `btn-on` class → button appears highlighted (active layer is showing)
- `btn-off` class → button appears dimmed (layer is hidden)

#### HTML template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Knowledge Graph — SCOPE_PLACEHOLDER</title>
  <script src="https://unpkg.com/cytoscape@3.31.0/dist/cytoscape.min.js"></script>
  <script src="https://unpkg.com/layout-base@2.0.1/layout-base.js"></script>
  <script src="https://unpkg.com/cose-base@2.2.0/cose-base.js"></script>
  <script src="https://unpkg.com/cytoscape-fcose@2.2.0/cytoscape-fcose.js"></script>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f1117; color: #e0e0e0; }
    #cy { width: 100vw; height: calc(100vh - 52px); }
    #bar { height: 52px; display: flex; align-items: center; gap: 8px; padding: 0 14px; background: #1a1d27; border-bottom: 1px solid #2d3142; flex-wrap: wrap; }
    #bar h1 { font-size: 14px; font-weight: 600; color: #7b8cde; margin-right: 8px; flex-shrink: 0; }
    button { padding: 5px 12px; border-radius: 5px; cursor: pointer; font-size: 12px; border: 1px solid #3d4252; transition: background 0.15s, color 0.15s; }
    button.btn-on  { background: #3d4f8c; color: #e0eaff; border-color: #667eea; }
    button.btn-off { background: #1a1d27; color: #666; border-color: #2d3142; }
    button.btn-neutral { background: #2d3142; color: #d0d0d0; border-color: #3d4252; }
    button:hover { filter: brightness(1.2); }
    .legend { display: flex; gap: 8px; font-size: 11px; margin-left: auto; flex-shrink: 0; }
    .li { display: flex; align-items: center; gap: 4px; }
    .dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
    #tip { position: fixed; background: #1a1d27; border: 1px solid #3d4252; border-radius: 8px;
           padding: 9px 13px; font-size: 12px; pointer-events: none; display: none;
           max-width: 280px; z-index: 9999; line-height: 1.6; }
    #tip strong { color: #a0c4ff; font-size: 13px; display: block; margin-bottom: 2px; }
    #tip small { color: #888; }
    #tip a { color: #7b8cde; text-decoration: none; }
  </style>
</head>
<body>
  <div id="bar">
    <h1>🏢 SCOPE_PLACEHOLDER</h1>
    <button id="btn-fit"      class="btn-neutral" onclick="cy.fit()">⊡ Fit</button>
    <button id="btn-external" class="btn-on"  onclick="toggleExternal()">🌐 External Consumers</button>
    <button id="btn-uj"       class="btn-off" onclick="toggleUJ()">👥 User Journeys</button>
    <button id="btn-labels"   class="btn-on"  onclick="toggleLabels()">🏷 Labels</button>
    <div class="legend">
      <div class="li"><span class="dot" style="background:#4a5568"></span>Org</div>
      <div class="li"><span class="dot" style="background:#667eea"></span>Domain</div>
      <div class="li"><span class="dot" style="background:#4299e1"></span>Subdomain</div>
      <div class="li"><span class="dot" style="background:#38b2ac"></span>Product</div>
      <div class="li"><span class="dot" style="background:#48bb78"></span>Component</div>
      <div class="li"><span class="dot" style="background:#ed8936"></span>UJ</div>
      <div class="li"><span class="dot" style="background:#744210;border:1px dashed #f6ad55"></span>External</div>
    </div>
  </div>
  <div id="cy"></div>
  <div id="tip"></div>
  <script id="graph-data" type="application/json">
{GRAPH_DATA_JSON}
  </script>
  <script>
    const DATA = JSON.parse(document.getElementById('graph-data').textContent);

    // ── Cytoscape instance ────────────────────────────────────────────────────
    const cy = cytoscape({
      container: document.getElementById('cy'),
      elements: [
        ...DATA.nodes.map(n => ({ group: 'nodes', data: n })),
        ...DATA.edges.map(e => ({ group: 'edges', data: e }))
      ],
      style: [
        { selector: 'node', style: {
            'label': 'data(label)',
            'color': '#ddd',
            'font-size': 9,
            'text-valign': 'bottom',
            'text-halign': 'center',
            'text-outline-width': 2,
            'text-outline-color': '#0f1117',
            'background-color': '#555',
            'border-width': 1,
            'border-color': 'rgba(255,255,255,0.15)'
        }},
        { selector: 'node[group = "org"]',          style: { 'background-color': '#4a5568', 'width': 56, 'height': 56, 'font-size': 12, 'font-weight': 'bold' }},
        { selector: 'node[group = "domain"]',       style: { 'background-color': '#667eea', 'width': 42, 'height': 42, 'shape': 'round-rectangle' }},
        { selector: 'node[group = "subdomain"]',    style: { 'background-color': '#4299e1', 'width': 34, 'height': 34, 'shape': 'round-rectangle' }},
        { selector: 'node[group = "product"]',      style: { 'background-color': '#38b2ac', 'width': 26, 'height': 26 }},
        { selector: 'node[group = "component"]',    style: { 'background-color': '#48bb78', 'width': 18, 'height': 18, 'font-size': 8 }},
        { selector: 'node[group = "user_journey"]', style: { 'background-color': '#ed8936', 'width': 22, 'height': 22, 'shape': 'diamond', 'display': 'none' }},
        { selector: 'node[?external]', style: {
            'background-color': '#744210',
            'border-width': 2,
            'border-color': '#f6ad55',
            'border-style': 'dashed'
        }},
        { selector: 'node[?incident]', style: { 'background-color': '#e53e3e', 'border-width': 3, 'border-color': '#fc8181', 'width': 28, 'height': 28 }},
        { selector: 'node[?impacted]', style: { 'background-color': '#c05621', 'border-width': 2, 'border-color': '#fbd38d' }},
        { selector: 'edge', style: {
            'curve-style': 'bezier',
            'target-arrow-shape': 'triangle',
            'line-color': '#3a4060',
            'target-arrow-color': '#3a4060',
            'width': 1,
            'opacity': 0.6
        }},
        { selector: 'edge[type = "consumes"]', style: {
            'line-color': '#4299e1',
            'target-arrow-color': '#4299e1',
            'width': 1.5,
            'opacity': 0.8
        }},
        { selector: 'edge[type = "slo_link"]', style: {
            'line-color': '#d69e2e',
            'target-arrow-color': '#d69e2e',
            'line-style': 'dashed',
            'width': 1.2,
            'display': 'none'
        }},
        { selector: 'edge[?external]', style: { 'line-style': 'dashed', 'opacity': 0.5 }},
        { selector: ':selected', style: { 'border-width': 3, 'border-color': '#f6e05e' }}
      ]
    });

    // ── Layout ────────────────────────────────────────────────────────────────
    function runLayout() {
      cy.layout({
        name: 'fcose',
        quality: 'default',
        animate: false,
        fit: true,
        padding: 50,
        nodeDimensionsIncludeLabels: true,
        nodeRepulsion: 6000,
        idealEdgeLength: 60,
        edgeElasticity: 0.45,
        nestingFactor: 0.1,
        gravity: 0.4,
        gravityRange: 3.8,
        packComponents: true,
        tilingPaddingVertical: 20,
        tilingPaddingHorizontal: 20,
        numIter: 2500
      }).run();
    }
    runLayout();

    // ── Tooltip ───────────────────────────────────────────────────────────────
    const tip = document.getElementById('tip');
    cy.on('mouseover', 'node', evt => {
      const n = evt.target.data();
      const ls = (n.links || []).map(l => '<a href="' + l.url + '" target="_blank">' + (l.type || l.title) + '</a>').join(' · ');
      tip.innerHTML = [
        '<strong>' + n.label + '</strong>',
        '<small>' + n.group + (n.type ? ' · ' + n.type : '') + (n.external ? ' · external' : '') + '</small>',
        n.tiering     ? 'Tier: T' + n.tiering : '',
        n.team        ? 'Team: '  + n.team : '',
        n.domain      ? 'Domain: '+ n.domain : '',
        n.criticality ? 'UJ Criticality: ' + n.criticality : '',
        n.description ? '<em style="color:#aaa;font-size:11px">' + String(n.description).substring(0, 140) + '…</em>' : '',
        ls            ? ls : ''
      ].filter(Boolean).join('<br>');
      tip.style.display = 'block';
    });
    cy.on('mousemove', evt => {
      tip.style.left = (evt.originalEvent.clientX + 14) + 'px';
      tip.style.top  = (evt.originalEvent.clientY + 14) + 'px';
    });
    cy.on('mouseout', 'node', () => { tip.style.display = 'none'; });

    // ── Toggle helpers ────────────────────────────────────────────────────────
    // State: true = layer is visible, false = hidden
    const state = { external: true, uj: false, labels: true };

    function setBtn(id, on) {
      const el = document.getElementById(id);
      el.className = on ? 'btn-on' : 'btn-off';
    }

    function toggleExternal() {
      state.external = !state.external;
      const d = state.external ? 'element' : 'none';
      cy.nodes('[?external]').style('display', d);
      cy.edges('[?external]').style('display', d);
      setBtn('btn-external', state.external);
    }

    function toggleUJ() {
      state.uj = !state.uj;
      const d = state.uj ? 'element' : 'none';
      cy.nodes('[group = "user_journey"]').style('display', d);
      cy.edges('[type = "slo_link"]').style('display', d);
      setBtn('btn-uj', state.uj);
    }

    function toggleLabels() {
      state.labels = !state.labels;
      cy.nodes().style('label', state.labels ? 'data(label)' : '');
      setBtn('btn-labels', state.labels);
    }
  </script>
</body>
</html>
```

#### Embedding graph data

Replace `SCOPE_PLACEHOLDER` with the view description (e.g., `"Business Capability Platform"`, `"Full Graph"`, `"Incident: OneFF"`).

Replace `GRAPH_DATA_JSON` with the actual data as **valid JSON** (generated by `json.dumps()` in Python or `JSON.stringify()` in JS):
```python
# Python approach (CORRECT):
import json
graph_data = {"nodes": [...], "edges": [...]}
graph_json_str = json.dumps(graph_data)
html_content = html_template.replace('{GRAPH_DATA_JSON}', graph_json_str)
```

> ⚠️ **CRITICAL FIX**: Use a `<script type="application/json">` tag to embed the JSON, then parse it with `JSON.parse()` in the main script. This avoids escaping errors and JavaScript syntax issues.
>
> The HTML template uses:
> ```html
> <script id="graph-data" type="application/json">{GRAPH_DATA_JSON}</script>
> <script>
>   const DATA = JSON.parse(document.getElementById('graph-data').textContent);
> </script>
> ```
>
> This ensures all JSON special characters (quotes, newlines, backslashes) are safely handled by the HTML parser.

#### Write and open

```bash
OUTFILE="/tmp/knowledge-graph-$(date +%Y%m%d_%H%M%S).html"
# Write the HTML with DATA replaced using json.dumps(), then:
open "$OUTFILE"       # macOS
# xdg-open "$OUTFILE" # Linux
```

---

## Output Format

Always print a text summary **before** opening the graph:

```markdown
## Knowledge Graph — <scope>

| Entity | Count |
|---|---|
| Domains | N |
| Subdomains | N |
| Products | N (Tier-1: N · Tier-2: N · Tier-3: N) |
| Components (filtered) | N (LIBRARY/DOCUMENTATION excluded) |
| API consumer edges | N (within-domain: N · cross-domain: N) |
| External consumers | N (from other domains) |
| User Journeys linked | N |
| SLO→UJ edges | N |

Graph written to: /tmp/knowledge-graph-<timestamp>.html
Opening in browser…
```

### Incident mode: add impact summary

```markdown
## Incident Impact Analysis — <incident_target>

**Failing asset:** <name> (<type>, Tiering: T<N>)

### Directly impacted components (N)
- `component-a` — team: X
- `component-b` — team: Y

### Impacted User Journeys (N)
| UJ Name | Criticality | Via SLO keys |
|---|---|---|
| Lower Funnel REVAMP Checkout | 1 | slo-onecheckout-cart-... |

> Graph highlights: 🔴 incident node · 🟠 impacted nodes
```

---

## Edge Cases

**Domain name not recognised / 0 products returned**
→ Run a brief sample query without a filter to discover all domain values from `metadata.governance.domain`, then ask the user which one they mean. Never guess.

**Very large graph (> 500 nodes)**
→ Warn: "The graph contains N nodes. Consider adding a domain or subdomain filter for a faster render."

**UJ moments API call fails**
→ Skip that UJ (log it). Continue with others. Report "N UJs skipped due to API errors."

**No SLO key match found between KG and UJs**
→ Add UJ nodes without connecting edges. Note: "User Journeys are shown but could not be linked to assets — SLO key naming patterns did not match any product names."

**DeliveryMetrics returns 401**
→ Generate the graph without User Journey nodes. Note: "DeliveryMetrics API returned 401 — User Journey layer is unavailable."

**`open` command fails (non-macOS)**
→ Print the path and suggest: `xdg-open <path>` or open manually in browser.

---

## References

- [AppReferential GraphQL API](https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql)
- [DeliveryMetrics API](https://api.decathlon.net/deliverymetrics)
- [Cytoscape.js](https://js.cytoscape.org/)
- [cytoscape-fcose layout docs](https://github.com/iVis-at-Bilkent/cytoscape.js-fcose)
