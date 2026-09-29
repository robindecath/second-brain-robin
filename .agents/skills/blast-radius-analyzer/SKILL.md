---
name: blast-radius-analyzer
description: >
  Performs incident impact analysis on Decathlon's digital asset topology by simulating
  a product/component failure and identifying all downstream technical impacts (products,
  components) and customer-facing impacts (User Journeys), then opens the blast-radius
  canvas for an interactive visualization (falls back to the browser canvas with an HTML
  file if the extension is unavailable).
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  api: graphql+rest
  mcp_required: false
---

# Blast Radius Analyzer Skill

---

## When to Use

- **Incident impact analysis**: "If product X fails, what breaks?"
- **Risk assessment**: "What's the blast radius of product Y?"
- **Dependency analysis**: "Which User Journeys depend on service Z?"
- **Business impact estimation**: "How many customer experiences are affected by this outage?"
- **Architecture review**: "Is this product a single point of failure?"
- **Disaster planning**: "What's the worst-case scenario for domain X Tier-1 products?"

---

## Prerequisite Skills

This skill **depends on** the following skills — load all of them in order before starting:

1. `decathlon-api-tool` — provides authenticated HTTP calls to Decathlon APIs
2. `knowledge-graph-query` — queries AppReferential Knowledge Graph (GraphQL)
3. `delivery-metrics` — queries User Journeys and SLO keys from DeliveryMetrics API

> All skills are referenced by **name only**. Call `read_skill <name>` for each before using it.

---

## Input Parameters

The user provides:

| Parameter | Description | Examples |
|---|---|---|
| **incident_target** | The failing product or component name | `"OneFF"`, `"onepay-api"`, `"Login"` |
| **scope** (optional) | Limit analysis to a domain | `"BUSINESS CAPABILITY PLATFORM"`, `"ECOMMERCE"` |
| **view_level** (optional) | `"product"` (default) or `"component"` | Controls graph granularity |

---

## Output Format

The skill produces three outputs:

### 1. HTML Visualization

**File**: `/tmp/blast-radius-<target>-<timestamp>.html`

Interactive Cytoscape.js graph showing:
- 🔴 **Red node** = Incident target (failing)
- 🟠 **Orange nodes** = Impacted downstream products/components
- 💔 **Red diamonds** = Impacted User Journeys
- 🟡 **Yellow dashed lines** = SLO links (product → UJ dependency)

**Controls**:
- `🔄 Fit` — reset view to full graph
- `🎯 Focus Impact` — zoom to blast radius
- `🔥 Blast Radius Only` — hide all non-impacted nodes (cleaner view)
- `🔗 External Consumers` — toggle external domain consumers
- `💔 User Journeys` — toggle UJ layer
- `🏷️ Labels` — toggle node labels

**Impact Dashboard** (top-right):
- Failing nodes count
- Impacted products count
- Tier-1 products affected
- User Journeys impacted
- Criticality-1 UJs
- Domains affected
- Revenue loss estimate (if available)
- Per-minute loss rate (if available)

### 2. JSON Impact Report

**File**: `/tmp/blast-radius-<target>-<timestamp>.json`

**Generic template** (all fields computed dynamically):

```json
{
  "incident_target": "<incident_target>",
  "incident_time": "<ISO 8601 timestamp>",
  "scope": "<scope or 'full_graph'>",
  "view_level": "<product|component>",
  "methodology": "UUID-based product linking via DeliveryMetrics moments",
  "impact": {
    "failing_nodes": "<count>",
    "impacted_products": "<count>",
    "impacted_components": "<count>",
    "external_consumers": "<count>",
    "tier1_impacted": "<count>",
    "domains_affected": "<count>",
    "user_journeys_impacted": "<count>",
    "criticality_1_ujs": "<count>",
    "criticality_2_ujs": "<count>",
    "criticality_3_ujs": "<count>",
    "criticality_4_ujs": "<count>",
    "total_blast_radius": "<count>"
  },
  "impacted_products": [
    {
      "name": "<product_name>",
      "tiering": "<1|2|3>",
      "domain": "<domain_name>",
      "team": "<team_name>",
      "subdomain": "<subdomain_name>",
      "component_count": "<count>"
    }
  ],
  "impacted_user_journeys": [
    {
      "uuid": "<uj_uuid>",
      "name": "<uj_name>",
      "criticality": "<1|2|3|4>",
      "slo_target": "<percentage>",
      "linked_products": ["<product_1>", "<product_2>"],
      "linked_via_product_uuids": ["<uuid_1>", "<uuid_2>"],
      "moments_requiring_products": [
        {
          "moment_uuid": "<moment_uuid>",
          "moment_name": "<moment_name>",
          "sequence": "<number>",
          "products": ["<product_1>", "<product_2>"]
        }
      ]
    }
  ],
  "domains_affected": [
    {
      "domain": "<domain_name>",
      "impacted_products": "<count>",
      "tier1_products": "<count>"
    }
  ]
}
```

**Example output** (OneFF incident):

```json
{
  "incident_target": "OneFF",
  "incident_time": "2026-06-11T00:11:28Z",
  "scope": "full_graph",
  "view_level": "product",
  "methodology": "UUID-based product linking via DeliveryMetrics moments",
  "impact": {
    "failing_nodes": 1,
    "impacted_products": 33,
    "tier1_impacted": 13,
    "domains_affected": 8,
    "user_journeys_impacted": 4,
    "criticality_1_ujs": 3,
    "criticality_3_ujs": 1,
    "total_blast_radius": 38
  },
  "impacted_products": [
    { "name": "OneCheckout", "tiering": 1, "domain": "BUSINESS CAPABILITY PLATFORM", "team": "CE-ONECHECKOUT" },
    { "name": "OneBooking", "tiering": 1, "domain": "BUSINESS CAPABILITY PLATFORM", "team": "CE-ONEBOOKING" }
  ],
  "impacted_user_journeys": [
    {
      "uuid": "f88b9194-3582-435f-96c6-0951a620ec3a",
      "name": "Lower Funnel REVAMP Checkout - Availability",
      "criticality": 1,
      "slo_target": 99.9,
      "moments_requiring_products": [
        {"moment_name": "I MANAGE MY ITEMS", "sequence": 2},
        {"moment_name": "I CHOOSE MY DELIVERY OPTIONS", "sequence": 7}
      ]
    }
  ],
  "domains_affected": [
    { "domain": "BUSINESS CAPABILITY PLATFORM", "impacted_products": 15, "tier1_products": 8 },
    { "domain": "ECOMMERCE", "impacted_products": 8, "tier1_products": 2 }
  ]
}
```

### 3. Text Summary

**Printed to console** (generic template):

```markdown
## 💥 Blast Radius Analysis — <incident_target>

| Metric | Count | Details |
|--------|-------|---------|
| 🔴 Failing | <count> | <incident_target> (Tier-<N>, <M> components) |
| 🟠 Impacted Products | <count> | <tier1_count> Tier-1 · <other_count> Tier-2/3 |
| 💔 Impacted User Journeys | <count> | <crit1_count> Criticality-1 (CRITICAL) |
| 🌐 External Consumers | <count> | Cross-domain dependencies |
| 🎯 Domains Affected | <count> | <domain_list> |
| 💥 Total Blast Radius | <count> nodes | Products + UJs affected |

### 💔 Customer Impact: <uj_count> User Journeys

**By Criticality**:
- Criticality 1 (CRITICAL): <crit1_count> UJs
- Criticality 2 (High): <crit2_count> UJs
- Criticality 3 (Medium): <crit3_count> UJs
- Criticality 4 (Low): <crit4_count> UJs

**Top Impacted User Journeys**:
<for each criticality 1 UJ>
- <uj_name> (SLO: <slo_target>%)
  - Moments requiring <incident_target>: <moment_count>
  - Key moments: <moment_1>, <moment_2>, ...
</for each>

### 🚨 Assessment

<incident_target> impact analysis:
- ✅ <impacted_products_count> technical products affected
- ✅ <uj_count> customer experiences impacted (<crit1_count> critical)
- ✅ <domains_count> domains affected
- ✅ <tier1_count> Tier-1 products in blast radius

**Severity**: <Low|Medium|High|Critical>
- Low: < 5 products, 0 Tier-1, 0 Criticality-1 UJs
- Medium: 5-20 products, 1-3 Tier-1, 0-1 Criticality-1 UJs
- High: 20-50 products, 3-10 Tier-1, 1-5 Criticality-1 UJs
- Critical: 50+ products OR 10+ Tier-1 OR 5+ Criticality-1 UJs

**Visualization**: /tmp/blast-radius-<target>-<timestamp>.html
**Impact report**: /tmp/blast-radius-<target>-<timestamp>.json
```

**Example output** (OneFF incident):

```markdown
## 💥 Blast Radius Analysis — OneFF

| Metric | Count | Details |
|--------|-------|---------|
| 🔴 Failing | 1 product | OneFF (Tier-1, 18 components) |
| 🟠 Impacted Products | 33 | 13 Tier-1 · 20 Tier-2/3 |
| 💔 Impacted User Journeys | 4 | 3 Criticality-1 (CRITICAL) |
| 🌐 External Consumers | 24 | Cross-domain dependencies |
| 🎯 Domains Affected | 8 | BCP, ECOMMERCE, FLTC, etc. |
| 💥 Total Blast Radius | 38 nodes | Products + UJs affected |

### 💔 Customer Impact: 4 User Journeys

**Criticality 1 (CRITICAL) — 3 UJs**:
- Lower Funnel REVAMP Checkout - Availability (SLO: 99.9%)
  - 4 moments require OneFF
  - Cart management, delivery options
- Create connected order (SLO: 99.0%)
  - 3 moments require OneFF
  - Product search, cart management
- WIP - CATALOG INTEGRATION Revamp (SLO: 99.5%)
  - 1 moment requires OneFF

**Criticality 3 (Medium) — 1 UJ**:
- Booking funnel ONEBOOKING (SLO: 99.0%)

### 🚨 Assessment

OneFF impact analysis:
- ✅ 33 technical products affected
- ✅ 4 customer experiences impacted (3 critical)
- ✅ 8 domains affected
- ✅ 13 Tier-1 products in blast radius

**Severity**: Critical
- Reason: 13 Tier-1 products + 3 Criticality-1 UJs affected

**Visualization**: /tmp/blast-radius-oneff-20260611_001128.html
**Impact report**: /tmp/blast-radius-oneff-20260611_001128.json
```
```

---

## Workflow Steps

### Step 1 — Parse Input

Extract:
- `incident_target` (required) — the failing product/component name
- `scope` (optional) — domain filter (full name, e.g., `"BUSINESS CAPABILITY PLATFORM"`)
- `view_level` (default: `"product"`) — `"product"` or `"component"`

### Step 2 — Load Prerequisite Skills

```bash
read_skill knowledge-graph-query
read_skill delivery-metrics
```

### Step 3 — Fetch Knowledge Graph Topology + Build Graph Data Model

Run the **`build_graph_data.py`** script. It covers Steps 3, 4, and 5 in a single
repeatable execution — fetching products, API edges, User Journeys, assembling the
graph model, and resolving the incident target — outputting a single JSON file ready
for BFS analysis in Step 6.

```bash
python3 scripts/build_graph_data.py \
  --target "<incident_target>" \
  [--scope "<domain_name>"] \
  [--view-level product|component] \
  [--output /tmp/my_graph.json] \
  [--no-uj] \
  [--cache]
```

**Parameters**

| Flag | Description | Default |
|---|---|---|
| `--target` | Product / component / User Journey name (**required**) | — |
| `--scope` | Domain filter, e.g. `"BUSINESS CAPABILITY PLATFORM"` | full graph |
| `--view-level` | `product` or `component` | `product` |
| `--output` | Output JSON path | `/tmp/kg_graph_<target>_<ts>.json` |
| `--no-uj` | Skip User Journey fetching (faster, technical graph only) | off |
| `--cache` | Reuse cached API data if < 1 h old | off |
| `--api-script` | Explicit path to `decathlon_api.py` (auto-detected if omitted) | auto |

**What it fetches internally**

- **3a** Products (all pages) — includes `reference` UUID field (matches DeliveryMetrics `product_uuids`)
- **3b** DECATHLON_API components (5+ pages) — builds producer/consumer API edge map
- **4a** User Journey list via v2 API (paginated)
- **4b** Moments per UJ via v1 API (`with_moment_list=true`)
- **4c–4d** Product→UJ edges via UUID matching (`reference` ↔ `product_uuids`)

**Output JSON shape**

```json
{
  "meta": {
    "incident_target": "OneFF",
    "incident_node_id": "product:OneFF",
    "incident_type": "product",
    "scope": "full_graph",
    "view_level": "product",
    "generated_at": "2026-06-11T00:11:28+00:00",
    "stats": {
      "total_products": 889,
      "total_uj": 50,
      "total_nodes": 1024,
      "total_edges": 2341,
      "api_edges": 512,
      "uj_edges": 217
    }
  },
  "nodes": [
    {
      "id": "product:OneFF",
      "label": "OneFF",
      "group": "product",
      "tiering": 1,
      "domain": "BUSINESS CAPABILITY PLATFORM",
      "subdomain": "PAYMENT",
      "team": "CE-ONEFF",
      "reference": "0d7f51c6-d45c-463a-a411-52bb73d8b676",
      "color": "#2b6cb0",
      "size": 35
    }
  ],
  "edges": [
    {
      "id": "e:product:OneCheckout->product:OneFF",
      "source": "product:OneCheckout",
      "target": "product:OneFF",
      "type": "consumes",
      "external": false
    },
    {
      "id": "uj:OneFF--f88b9194-...",
      "source": "product:OneFF",
      "target": "user_journey:f88b9194-...",
      "type": "moment_dependency"
    }
  ]
}
```

**Node groups**: `org` · `domain` · `subdomain` · `product` · `component` · `user_journey`

**Edge types**: `contains` (hierarchy) · `consumes` (API dependency) · `moment_dependency` (product→UJ)

**For Cytoscape.js** (HTML template), wrap nodes/edges in `{"data": ...}`:
```python
cyto_nodes = [{"data": n} for n in graph["nodes"]]
cyto_edges = [{"data": e} for e in graph["edges"]]
```

**Expected runtime**: ~20 s (5 s for products + API pages, 15 s for ~50 UJ moment fetches)

**Caching**: Use `--cache` for repeated runs during the same session. Cache files:
- `/tmp/kg_products_cache.json` — products (1-hour TTL)
- `/tmp/kg_api_edges_cache.json` — API edges (1-hour TTL)
- `/tmp/kg_api_edges_cache.json` — User Journeys (1-hour TTL)

**Example invocation**:
```bash
GRAPH_JSON=$(python3 scripts/build_graph_data.py --target OneFF --cache)
echo "Graph saved to: $GRAPH_JSON"
```

> The script prints progress to **stderr** and the output file path to **stdout**,
> making it easy to capture the path in a shell variable.

> **Steps 4 and 5** (User Journey fetching and graph model assembly) are fully
> handled inside this script. No separate action is needed.
>
> **Graph node groups**: `org` · `domain` · `subdomain` · `product` · `component` · `user_journey`
>
> **Graph edge types**: `contains` (hierarchy) · `consumes` (API dependency, aggregated to product level by default) · `moment_dependency` (product → user_journey via UUID matching)

### Step 6 — Perform Incident Impact Analysis (BFS)

Run `scripts/blast_radius.py` with the graph file from Step 3.
The incident node ID is read from `meta.incident_node_id` automatically:

```bash
python3 scripts/blast_radius.py "$GRAPH_JSON"

# Or with an explicit incident node ID (backward-compatible with legacy graph files)
python3 scripts/blast_radius.py /tmp/kg_graph_oneff_20260611T001128Z.json product:OneFF
```

The script runs BFS to find all impacted products/components (following `consumes`
edges in reverse), then marks impacted User Journeys (any UJ linked via
`moment_dependency` to an impacted product).

### Step 7 — Generate Outputs

`blast_radius.py` generates all three outputs automatically after BFS:

| Output | File | Description |
|---|---|---|
| JSON report | `/tmp/blast-radius-<target>-<ts>.json` | Machine-readable impact summary (metrics only) |
| Marked graph | `/tmp/blast-radius-<target>-graph-<ts>.json` | Full graph with incident/impacted flags (for canvas) |
| HTML graph | `/tmp/blast-radius-<target>-<ts>.html` | Interactive Cytoscape.js visualization (fallback) |
| Text summary | stdout | Markdown table for chat response |

The script prints all output paths to stdout on completion:
```
**Impact report**: /tmp/blast-radius-OneOM-20260612_161800.json
**Marked graph (for canvas)**: /tmp/blast-radius-OneOM-graph-20260612_161800.json
**HTML visualization**: /tmp/blast-radius-OneOM-20260612_161800.html
```
Extract the marked graph path — this is what the canvas needs.

#### HTML template placeholders (reference only)

The HTML uses `templates/blast-radius-viz.html`. All `{{PLACEHOLDER}}` tokens are
filled by `blast_radius.py` — no manual replacement needed.
Placeholders: `{{INCIDENT_TARGET}}`, `{{SCOPE}}`, `{{GRAPH_DATA_JSON}}`,
`{{FAILING_COUNT}}`, `{{IMPACTED_PRODUCTS}}`, `{{TIER1_COUNT}}`, `{{UJ_COUNT}}`,
`{{CRIT1_COUNT}}`, `{{DOMAINS_COUNT}}`, `{{REVENUE_LOSS}}`, `{{PER_MINUTE}}`,
`{{SEVERITY_LEVEL}}`, `{{SEVERITY_CSS}}`, `{{IMPACTED_PRODUCTS_JSON}}`, `{{IMPACTED_UJS_JSON}}`.

### Step 8 — Open Visualization

After `blast_radius.py` completes, open the **blast-radius canvas** (the dedicated
extension) using the **marked graph JSON file** (contains incident/impacted flags).
This gives SSE real-time updates, severity badge, and actions.

#### Primary: blast-radius canvas extension

```python
# marked_graph_path = path printed by blast_radius.py as "**Marked graph (for canvas)**: ..."
#                     e.g. /tmp/blast-radius-OneOM-graph-20260612_161800.json
# incident_target   = human-readable name, e.g. "OneOM"

open_canvas(
    canvasId="blast-radius",
    instanceId="blast-radius-viz",
    input={
        "graphDataPath": marked_graph_path,  # ← marked graph with incident/impacted flags
        "incidentTarget": incident_target
    }
)
```

> **Which JSON file**: Pass the **`blast-radius-*-graph-*.json`** file (marked graph),
> NOT the impact report. The marked graph contains incident/impacted node flags so the
> canvas can color-code the blast radius.

#### Fallback: browser canvas (HTML file)

If `open_canvas` with `canvasId="blast-radius"` raises an error (extension not
installed or unavailable), fall back to the HTML file in the browser canvas:

```python
# html_path = path printed by blast_radius.py as "**HTML visualization**: ..."
open_canvas(canvasId="browser", instanceId="blast-radius-viz",
            input={"url": f"file://{html_path}"})
```

#### Last-resort: system browser

If neither canvas is available:
```bash
open "$HTML_PATH"        # macOS
xdg-open "$HTML_PATH"   # Linux
```

---

## Critical Data Model Facts

### Knowledge Graph
- **`reference` field** — **CRITICAL**: Contains product UUID matching DeliveryMetrics `product_uuids`
  - The `id` field is just a numeric ID (e.g., "1", "2") — **NOT the product UUID**
  - The `reference` field is the actual UUID (e.g., `0d7f51c6-d45c-463a-a411-52bb73d8b676`)
  - **Always include `reference` in GraphQL queries** when building UJ links
  - Without `reference`, UUID-based linking finds 0 matches
- `orgRefs` is always `{}` — use `metadata.governance` for domain/team
- Domain names are full (e.g., `"BUSINESS CAPABILITY PLATFORM"`, not `"BCP"`)
- Products have inline `components { name type }` field
- Component relationships: only `partOf`, `deploysTo` — no `PRODUCES`/`CONSUMES`
- Producer-consumer links in `metadata`: `apis_provided`, `apis_consumed` (UUIDs)
- Skip component types: `LIBRARY`, `DOCUMENTATION`

### DeliveryMetrics
- UJ list is paginated: `/api/v2/user_journeys?size=20&page=N`
- **v2 API does NOT return moments or product UUIDs** — only basic metadata
- **v1 API required for moments**: `/api/v1/user_journeys?user_journey_uuid_list=<uuid>&with_moment_list=true`
- Each moment has: `{ uuid, name, product_uuids: [...], slo_keys: [...] }`
- **Use `product_uuids` for linking** — exact UUID match against KG products

### UUID-Based Product → UJ Linking (Recommended)
- **Algorithm**: Match `product_uuids` from DeliveryMetrics moments against KG product `reference` field
- **Key insight**: Use KG's `reference` field (not `id`) for UUID matching
- **Advantages**: No string parsing, stable across renames, official API field, exact matches
- **Performance**: ~50 UJs × 0.5s = 25 seconds to fetch all moments
- **Match rate**: ~86% of UJs get linked (43/50 UJs in production data)
- **Example**: 
  - DeliveryMetrics moment has `product_uuids: ["0d7f51c6-d45c-463a-a411-52bb73d8b676"]`
  - KG product "Merch Engine" has `reference: "0d7f51c6-d45c-463a-a411-52bb73d8b676"`
  - Match found → create edge `product:Merch Engine → uj:<uuid>`

### ~~SLO Key Matching~~ (Deprecated — Use UUID Matching Instead)
- ❌ **Old approach**: Parse `slo-<product-slug>-...` and fuzzy match to product name
- ❌ **Problems**: Breaks on renames, requires string parsing, false positives possible
- ✅ **Replacement**: Use `product_uuids` field from moments for exact UUID matching

---

## Edge Cases

**Incident target not found in KG**
→ Print: `"ERROR: Product/component '<incident_target>' not found in Knowledge Graph. Check spelling or try a different name."`
→ Suggest alternatives: query all products, fuzzy match, show closest 5 names.

**No downstream consumers found**
→ Print: `"No downstream consumers found — <incident_target> is a leaf node (not consumed by anyone)."`
→ Still show the graph with just the incident node highlighted.

**User Journey API returns 401**
→ Skip UJ layer. Print: `"WARNING: DeliveryMetrics API returned 401 — User Journey impact layer unavailable."`
→ Generate graph with technical impact only (products/components).

**No product UUID matches found in moments**
→ Show UJ nodes unlinked. Print: `"User Journeys collected but could not be linked to products — no product UUIDs in moments matched Knowledge Graph products."`
→ This indicates either: (a) UJs not instrumented yet, (b) products not in KG, or (c) API data mismatch

**Multiple nodes match incident_target**
→ Ask user to clarify: `"Multiple assets match '<incident_target>': <list>. Which one?"`

---

## Example Invocations

### Example 1: Single product blast radius
```
User: "Analyze the blast radius if OneFF fails"

→ incident_target = "OneFF"
→ scope = None (full graph)
→ view_level = "product"
```

**Output**:
- `/tmp/blast-radius-oneff-20260611_001128.html` (interactive graph)
- `/tmp/blast-radius-oneff-20260611_001128.json` (impact report)
- Console summary showing 33 products + 8 UJs impacted

---

### Example 2: Domain-scoped component-level analysis
```
User: "What's the blast radius of onepay-api within BCP domain at component level?"

→ incident_target = "onepay-api"
→ scope = "BUSINESS CAPABILITY PLATFORM"
→ view_level = "component"
```

**Output**:
- More detailed graph with individual components visible
- Limited to BCP domain dependencies (external consumers still shown if they consume BCP components)

---

### Example 3: Multi-product catastrophe simulation
```
User: "Simulate all BCP Tier-1 products failing"

→ incident_target = ["Login", "OneFF", "OneCheckout", "OneOM", ...] (array)
→ scope = "BUSINESS CAPABILITY PLATFORM"
→ view_level = "product"
```

**Modification**: Support array of incident_targets, mark all as `incident: true`, run BFS from all simultaneously.

---

## Performance Notes

- **Full graph fetch** (`build_graph_data.py`): ~5 s (889 products, 5 API pages)
- **User Journey fetch** (Steps 4a–4b): ~15 s (50 UJs × 0.3 s rate limit)
- **BFS traversal** (`blast_radius.py`): < 1 s (even on 1 000+ node graphs)
- **HTML generation**: < 1 s
- **Total runtime**: ~20 s for full analysis

Use `--cache` on repeated runs — the three cache files have a 1-hour TTL:
- `/tmp/kg_products_cache.json` — products
- `/tmp/kg_api_edges_cache.json` — API edges
- `/tmp/uj_data_cache.json` — User Journeys with moments

---

## Scripts Reference

| Script | Description | Covers |
|---|---|---|
| `scripts/build_graph_data.py` | Fetches all data and builds graph model | Steps 3, 4, 5 |
| `scripts/blast_radius.py` | BFS impact analysis | Step 6 |
| `templates/blast-radius-viz.html` | Cytoscape.js visualization template | Step 7b |

---

## References

- [AppReferential GraphQL API](https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql)
- [DeliveryMetrics API](https://api.decathlon.net/deliverymetrics)
- [Cytoscape.js](https://js.cytoscape.org/)
- Parent skill: `knowledge-graph-visualizer`

---

## Maintenance

**Skill maintainer**: Architecture team  
**Last updated**: 2026-06-12  
**Version**: 1.2.0
