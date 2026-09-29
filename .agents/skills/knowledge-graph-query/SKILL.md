---
name: knowledge-graph-query
description: >
  Query the AppReferential knowledge graph to answer any question about digital
  assets, products, components, deployments, team ownership, technology stacks,
  SLOs, incidents, and their relationships. Translates natural language questions
  into GraphQL queries and executes them via direct HTTP calls to the Graph API.
  Examples: "how many products are in the ORDER domain", "what stack does product X use",
  "which services have no monitoring", "blast radius if cluster Y fails",
  "what team owns monitor 12345".
  Also use whenever the user mentions any Decathlon product, API, service, domain, team,
  or component by name — even in passing, not just when asking an explicit graph
  question — to ground the reference in verified data (ownership, tier, stack,
  documentation) before responding.
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
compatibility: opencode
metadata:
  audience: all
  domain: platform-engineering
  api: graphql
  mcp_required: false
---

# AppReferential Knowledge Graph Skill

Translate any natural language question about Decathlon's digital asset registry into GraphQL queries, execute them, and present results in plain language.

---

## When to Use This Skill

Use this skill in **both** of these situations:

1. **Explicit graph question** — the user asks something analytical about the registry
   directly: counts, filters, ownership, stacks, monitoring gaps, blast radius, etc.
   (see the frontmatter `description` for phrasing examples).
2. **Named-entity mention in passing** — the user simply *mentions* a Decathlon product,
   API, service, domain, team, or component by name, even without asking a graph-shaped
   question (e.g. "checkout-api has been flaky today", "we're deprecating catalog-search
   next quarter", "can team-order-front look at this?"). In this case, invoke the skill
   silently to ground the reference in verified data (ownership, tier, stack, docs) so
   the rest of the response is grounded in facts, before continuing the conversation.

Don't wait for an explicit "query the graph" instruction — any recognizable named entity
is enough of a signal to activate this skill.

---

## Activation — Follow These Steps in Order

### Step 1 — Execute the query

**Detect your environment:** if `callDecathlonApi` appears in your available tools, use the VS Code method; otherwise use the CLI method.

**VS Code (Copilot LM tool):**
Use the `callDecathlonApi` tool directly:
```yaml
tool: callDecathlonApi
arguments:
  method: POST
  url: "https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql"
  param:
    query: "..."
    variables: {}
```

**CLI:** Use the `kg_query.py` script **bundled with this skill** — no second skill,
no path-parsing, no `read_skill decathlon-api-tool` needed for standard queries:

```bash
python3 <this-skill-dir>/scripts/kg_query.py raw --data '{"query": "...", "variables": {...}}'
```
`<this-skill-dir>` is this skill's own directory. **Read it directly from the
`<location>` tag on THIS skill's own entry in `<available_skills>`** (the same
tag used for cross-repo skills below) — it is typically `skills/knowledge-graph-query`
relative to the project root. Do **not** call `get_env`, `find`, or `ls` to
locate it — the path is already given to you in `<available_skills>`; probing
for it wastes a shell call for no reason. On first run it opens a browser for
Decathlon login (OAuth2 PKCE); the token is cached at
`~/.config/decathlon-cli/tokens.json` (shared with `decathlon-api-tool` if you
have it installed elsewhere).

**For any aggregation, filter, or list question — even ones this skill has never
seen before — start with `query`, the generic engine:**

```bash
python3 <this-skill-dir>/scripts/kg_query.py query --kind component \
  --where "metadata.stack.framework:eq:Spring Boot" \
  --fields metadata.stack.framework_version,metadata.governance.product --limit 50
```

`query` composes four independent capabilities so you don't need a new script
feature for every new question shape — see "Generic query engine" in API
Schema below for the full grammar (`--where`, `--metric`/`--metric-field`,
`--group-by`, `--sort-by`/`--top`). It covers: filtered lists, numeric
aggregation (sum/avg/min/max — e.g. "average business score of Tier-1
products"), group-by counts/averages (e.g. "components per team"), and
top-N ranking (e.g. "which single product has the highest business score").

A few narrower shortcuts exist for common enum-based or multi-hop cases where
they're simpler than composing `--where`/`--metric` yourself — prefer these
when they match:

```bash
# Enum-field breakdown (lifecycle, typology, ...) with counts + percentages, one call
python3 <this-skill-dir>/scripts/kg_query.py breakdown --kind product \
  --breakdown-by lifecycle --values GENERAL_AVAILABILITY END_OF_LIFE BETA DEVELOPMENT DEPRECATED

# All clusters in one call (small dataset, ~58 total) — filter client-side by region prefix
python3 <this-skill-dir>/scripts/kg_query.py all-clusters

# Discover real top-level metadata keys instead of guessing field names
python3 <this-skill-dir>/scripts/kg_query.py discover-metadata --kind product --sample 5

# Cluster -> component -> product multi-hop impact (see "Blast radius" pattern below)
python3 <this-skill-dir>/scripts/kg_query.py blast-radius --region-prefix europe-west

# Libraries/dependencies for a product's components, a single component, or cross-fleet "who uses X"
python3 <this-skill-dir>/scripts/kg_query.py libraries --product OneFF
python3 <this-skill-dir>/scripts/kg_query.py libraries --component oneff
python3 <this-skill-dir>/scripts/kg_query.py libraries --by-name log4j
```

`list-filtered` (plain filter+project+paginate, no `--where`/`--metric`/
`--group-by`) still works too but `query` is a strict superset of it — prefer
`query` for anything new.

If `kg_query.py` is missing or fails to locate an auth module (rare — only if this
skill was copied without its `scripts/` folder), fall back to the `decathlon-api-tool`
skill: `read_skill decathlon-api-tool`, resolve `<decathlon-api-skill-dir>` from the
`<location>` tag in `<available_skills>` (that skill lives in a different repository —
never guess its path), then run
`python3 <decathlon-api-skill-dir>/scripts/decathlon_api.py --method POST --url "$GRAPH_URL" --data '...'`.

Never use `http_request` directly — it lacks the bearer token and will fail with 401.

Select the right query/shortcut from the patterns below, run it, then follow Steps 2 and 3.

### Step 2 — Check for Errors

The `bash` tool returns both stdout and the exit code. Inspect both:
- If the exit code is non-zero → report the error message from stdout/stderr and stop.
- If the body contains a top-level `"errors"` array → report each error message and stop. Do **not** answer from partial data unless `"data"` is also present and you can clearly satisfy the request from it.

### Step 3 — Present Results

**CRITICAL: Respond in English only.** Never use any other language.

Summarise in plain language. **CRITICAL: Always use lowercase entity names** (`product`, `component`, `cluster`) when reporting results — never capitalise them. For counts: state totals per kind (e.g. "found 889 products and 2709 components"). For technology distributions: ALWAYS include counts AND percentages (e.g. "Java: 120 components (45%)" based on the sample). Compute percentages from the sample data and clearly state the sample size. For lists: name, kind, tiering. For gaps: flag Tier-1 items as critical. Never output raw JSON.

---

## API Schema (validated — do not guess field names)

**`assets(filter: AssetFilter, first: Int, after: String)`** → `AssetConnection`

- `AssetFilter` fields: `kind` (String), `type` (String), `tiering` (**Int** — use integers: `1`, `2`, `3`; never strings like `"tier-1"`), `teamOwner` (String), **`metadataFilter`** (JSON containment, via variables)
- `AssetConnection` fields: `edges { cursor node { ... } }`, `pageInfo { hasNextPage endCursor }`, **`totalCount`** (full match count, independent of pagination — use this instead of a separate `assetCount` call when you're already fetching edges)
- **Page size cap: 200** — the API ignores `first` values above 200 and returns at most 200 edges per page. Always use `first: 200` for paginated scans.
- Asset node fields: `id`, `name`, `kind`, `type`, `tiering`, `metadata`, `orgRefs`, `businessScore`, `links { id type title url }`, `stack { language languageVersion buildTool framework frameworkVersion lastScannedAt }`, `libraries(name: String) { purl ecosystem name version license firstSeenAt lastSeenAt }`, `components { name type metadata }`, `relationships(type: String) { type targetAsset { name kind tiering } }`, `deployments { name type metadata }`

**`libraries(name: String)`** — third-party dependencies used by a component, sourced from the GitHub dependency-graph SBOM (confirmed live — e.g. the `oneff` component alone returns 179 entries spanning `golang`, `maven`, and `githubactions` ecosystems). Always returns a list (never null); empty means no SBOM data ingested yet for that asset. Pass `name` to filter to one library by case-insensitive substring match (e.g. `libraries(name: "log4j")`); omit it for the full list. **This is the correct field for any "what libraries/dependencies does X use" question — do NOT use `stack.dependencies` (see deprecation warning below).**

> ⚠️ **`stack.dependencies` is deprecated — never use it to answer a library/dependency question.** It's capped at ~20 entries, Maven/Node.js-only, no longer written by adapter syncs, and silently gives an incomplete/stale answer instead of erroring. Always use `Asset.libraries` (per-component) or `librariesByName` (cross-fleet) instead — both are confirmed live and return real, versioned, licensed SBOM data across every ecosystem (not just Maven/Node).
- **`relationships` supports multi-hop traversal in ONE query** (confirmed live): `targetAsset` is itself a full `Asset`, so you can nest `relationships` again on it — e.g. `relationships(type: "hosts") { targetAsset { name relationships(type: "partOf") { targetAsset { name kind tiering } } } }` resolves cluster→component→product in a single round trip. **Always pass the `type` filter** (e.g. `"hosts"`, `"partOf"`) to avoid pulling in unrelated relationship types (`deploysTo`, etc.) that bloat the response. Prefer nesting over issuing a separate `asset(name: ...)` lookup per intermediate node — the latter is the anti-pattern that caused a historical multi-round-trip token blowup (see "Blast radius" pattern below).

**`assetCount(filter: AssetFilter)`** → `Int!` — dedicated count query; runs a single COUNT(*) with no edges fetched. **Prefer this when you only need a count and no edges.** You can alias multiple `assetCount` calls in one request: `{ total: assetCount(filter:{kind:"component"}) monitored: assetCount(filter:{kind:"component", metadataFilter:{...}}) }`

**`asset(name: String)`** — single-asset lookup (no pagination); use for "tell me about asset X" questions

**`librariesByName(name: String!)`** → `[LibraryUsage]` — cross-fleet lookup: every component using a library whose name matches (case-insensitive substring), each paired with its owning asset. Confirmed live. This is the "who depends on X" query (e.g. "who's exposed to this CVE", "who needs to upgrade before we drop support for X") — a single indexed server-side query, not a fetch-everything-and-filter-client-side loop. Each `LibraryUsage` is `{ library: Library!, asset: Asset! }`. Example: `librariesByName(name: "log4j") { library { name version } asset { name kind } }`.

**`Library`** shape: `purl` (package URL, non-null), `ecosystem` (e.g. `maven`, `golang`, `npm`, `githubactions`), `name`, `version` (nullable — some SBOM entries, e.g. GitHub Actions, have no semver), `license` (nullable), `firstSeenAt`, `lastSeenAt`.

**`kind` values:** `"product"` | `"component"` | `"cluster"`

**`tiering` values:** integer `1` (business-critical/Tier-1), `2` (important/Tier-2), `3` (standard/Tier-3); `null` = unclassified

**`orgRefs`** is a JSON scalar — query as `orgRefs` (no sub-selection). Structure (confirmed live): `{ teamOwner, product, domain, subdomain, unit }` — the team field is **`teamOwner`**, not `team` (a common wrong guess that silently returns `null` for every row).

**`metadata`** is also a JSON scalar — query as `metadata` (no sub-selection). Parse the returned JSON client-side. Common structures (validated live against the API):
- Products/components (top level): `{ "lifecycle", "typology", "tiering", "businessScore", "displayName", "slug", "reference", "links": [...], "sources": [...], "description", "governance": { "unit", "domain", "sub_domain", "support_group", "tiering", "lifecycle", "business_score" }, "stack": { "name", "language", "language_version", "framework", "build_tool" }, "observability": "datadog" | null }`
- Clusters: `{ "deployment": { "region", "namespace", "environment", "cluster_type", "cloud_provider" }, "infrastructure": { "datadog": { "cluster_monitoring" } } }`

> ⚠️ **Duplicate fields**: `tiering`, `lifecycle`, and `businessScore`/`business_score` each appear **both** top-level in `metadata` **and** nested again under `metadata.governance`. Always filter/read the **top-level** key (`metadataFilter: { lifecycle: "..." }`, not `{ governance: { lifecycle: "..." } }`) — `metadataFilter` matches top-level keys directly. The `governance.*` copies are informational duplicates, not required for filtering.

**`lifecycle` values** (string, top-level `metadata` field — confirmed live counts on products): `GENERAL_AVAILABILITY` (majority), `END_OF_LIFE`, `BETA`, `DEVELOPMENT`, `DEPRECATED`. Treat this as the authoritative enum; do not invent other values or filter operators (e.g. there is no `lifecycle_not` — negate by aliasing the counts you need instead, see "Lifecycle / typology breakdown" pattern below).

> ⚠️ **Never sub-select** `metadata` or `orgRefs` — they are opaque JSON scalars. Use `metadata` or `orgRefs` as bare fields; the full JSON blob is returned.

**`metadataFilter` examples** (always pass via `variables`, never inline):

| Goal | Value |
|------|-------|
| Domain ORDER products | `{ "governance": { "domain": "ORDER" } }` |
| Java 17 components | `{ "stack": { "language": "Java", "language_version": "17" } }` |
| Spring Boot components | `{ "stack": { "framework": "Spring Boot" } }` (exact nested match — confirmed live, not just `language`) |
| Datadog-monitored | `{ "observability": "datadog" }` |
| GCP region cluster | `{ "deployment": { "region": "europe-west4" } }` |
| Namespace filter | `{ "deployment": { "namespace": "oneff" } }` |
| Sub-domain filter | `{ "governance": { "domain": "X", "sub_domain": "Y" } }` |
| Lifecycle filter | `{ "lifecycle": "END_OF_LIFE" }` (top-level key, **not** `{ "governance": { "lifecycle": ... } }`) |
| Typology filter | `{ "typology": "MAKE" }` |

> Keys: `language_version` (underscore), `sub_domain` (underscore). Top-level `domain`/`subdomain` AssetFilter fields are non-functional — always use `metadataFilter`.

> ⚠️ **If a field isn't listed above, don't guess.** After 2 failed/empty-result attempts at a metadata field name or operator, stop guessing and run the schema-discovery query in "Discovering unknown metadata fields" below instead of inventing more field names — this is what caused a real 9-round-trip, ~770K-token outlier on a lifecycle-breakdown question before this field was documented.

---

## Generic query engine — `kg_query.py query` (use this for anything not covered by a named pattern below)

**Why this exists:** every narrow, one-off shortcut (`breakdown`, `blast-radius`,
`list-filtered`) only covers the exact question shape it was built for. The
first genuinely novel question that doesn't fit one of them (e.g. "average
business score of Tier-1 products", "which components have a linked GitHub
repo") has historically forced a fallback to hand-rolled multi-page `raw`
calls — the same anti-pattern documented throughout this file, just on a new
question shape each time. `query` is a single composable primitive covering
filter + aggregate + group + rank, so you should be able to answer most novel
questions by combining its flags, not by inventing a new pagination loop.

```bash
python3 <this-skill-dir>/scripts/kg_query.py query --kind <product|component|cluster> \
  [--metadata-filter '<JSON, server-side push-down>'] \
  [--where "path:op[:value]"]...  \
  [--metric count|sum|avg|min|max --metric-field <path>] \
  [--group-by <path>] \
  [--sort-by <path> [--order asc|desc] --top N] \
  [--fields <path>,<path>,...] [--limit N]
```

Always paginates internally (server caps `first` at 200/page) — one shell call
regardless of dataset size. `--metadata-filter` is pushed to the GraphQL server
(fastest, use it whenever the condition is a known filterable field — see the
`metadataFilter` table above); `--where` runs client-side over the already
server-filtered stream for anything the API can't filter on directly.

**Scope: `query`/`list-filtered` fetch `name kind type tiering businessScore metadata orgRefs links` per row — nothing else.** `--where`/`--fields`/`--group-by`/`--sort-by` can only resolve paths under those fields (plus their `[]`-broadcast sub-paths). Relationship-style fields that need their OWN GraphQL sub-selection — `components { name type }`, `relationships(type:...) { ... }`, `stack { language ... }`, `libraries(name:...) { ... }` (the typed GraphQL field, not `metadata.stack`) — are **not reachable** through `query`'s `--fields`/`--where` and will silently resolve to nothing. For a question that needs one of those (e.g. "list the components owned by product X", "what libraries does X use"), use the single-asset lookup (`asset(name: ...)`) pattern instead, in ONE `raw` call with the exact sub-fields you need — don't try `query --fields components.name` first and then fall back; go straight to `asset(name:...)`. For libraries specifically, `kg_query.py libraries` (below) wraps this pattern so you don't have to hand-write the query.

**`--where PATH:OP[:VALUE]`** (repeatable, AND-combined):
- `PATH` is dotted, e.g. `metadata.stack.framework`, `orgRefs.teamOwner`, `businessScore`. Add `[]` after a segment to broadcast over a list — e.g. `metadata.sources[].key` checks every element of that array (matches if ANY element satisfies the condition). A leading `metadata.` prefix is optional for nested metadata fields — `stack.language` and `metadata.stack.language` resolve to the same value (the resolver falls back to `metadata.<path>` automatically when the bare path is empty), so you don't need to know in advance whether a field lives top-level or under `metadata`.
- `OP` ∈ `exists` | `missing` | `eq` | `ne` | `contains` (substring, case-insensitive) | `gt` | `gte` | `lt` | `lte` (numeric)
- Examples: `--where "businessScore:gt:80"`, `--where "orgRefs.teamOwner:eq:CE-IDP"`.
- **GitHub / repository links — use `links[]`, not `metadata.sources[]`.** Every asset has a top-level `links[]` array of `{ id, type, title, url }`; the canonical repo URL is the entry with `type: "repository"`. Prefer this over `metadata.sources[].key` (a slug like `github.com/project-slug`, not a full URL) or the flattened `metadata.github_*` keys — those exist but `links[]` is the cleanest, most direct source. Examples: `--where "links[].type:eq:repository"` (has a linked repo), `--fields "links[].url"` (get the repo URL directly, filtered by `--where "links[].type:eq:repository"` first to avoid picking up a non-repo link like monitoring/SonarQube).

**`--metric {count,sum,avg,min,max} --metric-field <path>`** — real aggregation over the ENTIRE matching set (not a sample). For `min`/`max`, the winning entity's `name` is included — this directly answers "which single X has the highest/lowest Y". Example: average + highest business score among Tier-1 products —
```bash
python3 <this-skill-dir>/scripts/kg_query.py query --kind product --where "tiering:eq:1" --metric avg --metric-field businessScore
python3 <this-skill-dir>/scripts/kg_query.py query --kind product --where "tiering:eq:1" --metric max --metric-field businessScore
```

**`--group-by <path>`** — buckets the matching set by a field's distinct values (for fields WITHOUT a small known enum — if the field has ~5 known values like `lifecycle`/`typology`, use `breakdown` instead, it's cheaper since it never fetches edges). Combine with `--metric-field`/`--metric` for an avg/sum PER group, not just counts:
```bash
python3 <this-skill-dir>/scripts/kg_query.py query --kind component --metadata-filter '{"governance": {"domain": "ORDER"}}' --group-by orgRefs.teamOwner
```

**`--sort-by <path> --order desc --top N`** — ranks the (already filtered/where'd) set and returns the top N rows with `--fields` projected. Use for "top 5 by X" style questions when you need more than just the single winner (`--metric max` already gives you the single winner more cheaply).

**No aggregation flags at all** → plain filtered list (same behavior as `list-filtered`).

**Anti-pattern this replaces:** issuing one `raw` call per page with an `after`
cursor to manually sum/average/filter/group in the model's own context —
regardless of which specific field or condition is involved. If you find
yourself about to write a second `raw` pagination call for the SAME question,
stop and re-express it as `query` flags instead.

---

## Query Patterns

For each pattern, use the CLI command from **Step 1**. `<decathlon-api-skill-dir>` must come from the `<location>` tag in `<available_skills>` — never guess it.

### Count products and components

Use `assetCount` — or alias multiple counts in one request:

```json
{
  "query": "{ products: assetCount(filter: { kind: \"product\" }) components: assetCount(filter: { kind: \"component\" }) clusters: assetCount(filter: { kind: \"cluster\" }) }",
  "variables": {}
}
```
Returns all counts in one HTTP request. Each response returns `{ "data": { "products": N, "components": N, "clusters": N } }`.

**Do NOT paginate when you only need counts.** `assetCount` is a single COUNT(*) and is always accurate regardless of dataset size.

### Single asset lookup

Use `asset(name: ...)` when the user asks about a specific named asset:

```json
{
  "query": "query Asset($n: String!) { asset(name: $n) { name kind type tiering orgRefs metadata stack { language languageVersion framework frameworkVersion lastScannedAt } links { type title url } components { name type } relationships { type targetAsset { name kind tiering } } } }",
  "variables": { "n": "oneff-api" }
}
```
Returns full details for a single asset. Only request fields you'll use — omit `metadata` if not needed. **A product/cluster asset's own `components { name type }` field lists everything it directly owns/hosts in the SAME call** — don't issue a second query (e.g. filtering components by `metadata.governance.product`) just to enumerate what a product owns; that information is already on the asset itself.

**Asset `name` is an exact, case-sensitive match — don't guess capitalization.** If you're not 100% sure how a name is cased (e.g. "oneff" vs "OneFF"), resolve it first with `query --where "name:contains:<text>" --fields name` (case-insensitive substring, one call) instead of retrying `asset(name: ...)` with different casings. Example: `query --kind product --where "name:contains:login" --fields name` → returns the exact names (`Login`, `Login With Decathlon`) to disambiguate before the real lookup.

**Comparing entity COUNTS scoped to a named product** (e.g. "which product has more components, X or Y") — if you already did a full `asset(name:...)` lookup that included `components { name type }`, just count that array's length client-side; don't issue a second query for the same count. Otherwise (count-only, no need for the full list), use `query --metadata-filter '{"governance":{"product":"<exact-name>"}}' --metric count` per side (one call each) — it does a server-side count without fetching every component.

### Libraries used by a product's components

Use the CLI shortcut for one-call convenience:

```bash
python3 <this-skill-dir>/scripts/kg_query.py libraries --product OneFF
```

Or the equivalent `raw` call — a single-asset lookup on the **product**, nesting `libraries` under its `components` (mirrors the existing `components { name type }` pattern — don't issue a separate query per component):

```json
{
  "query": "query ProductLibs($p: String!) { asset(name: $p) { name components { name libraries { name version ecosystem license purl } } } }",
  "variables": { "p": "OneFF" }
}
```

Confirmed live: e.g. the `oneff` backend component alone returns 179 SBOM entries spanning `golang`, `maven`, and `githubactions` ecosystems. If the product's `asset(name:...)` lookup doesn't expose its components directly (e.g. the product node itself has no `components` edges), fall back to `assets(filter: { kind: "component", metadataFilter: { governance: { product: "OneFF" } } }) { edges { node { name libraries { ... } } } }`.

**Do not use `stack.dependencies` for this** — it's deprecated, capped at ~20 entries, and Maven/Node.js-only (see warning in API Schema above). Always use `libraries`.

**For a single named component**, use `kg_query.py libraries --component <name>` or `asset(name: "<component>") { libraries { name version ecosystem license } }` directly.

### Which components depend on library X (cross-fleet)

Use `librariesByName` — a single indexed server-side query, not a fetch-everything-and-filter loop:

```bash
python3 <this-skill-dir>/scripts/kg_query.py libraries --by-name log4j
```

```json
{
  "query": "query WhoUses($n: String!) { librariesByName(name: $n) { library { name version ecosystem license } asset { name kind tiering } } }",
  "variables": { "n": "log4j" }
}
```

Confirmed live. Answers "who's exposed to this CVE" / "who needs to upgrade before we drop support for X" directly — flag any Tier-1 (`tiering: 1`) assets in the results as critical per the Step 3 presentation rule.

### Assets by tiering (criticality)

`tiering` is an **Int** in `AssetFilter` — use integers `1`, `2`, `3`, never strings:

```json
{
  "query": "query Tier($f: AssetFilter!, $n: Int!) { assets(filter: $f, first: $n) { totalCount edges { node { name kind type tiering orgRefs } } pageInfo { hasNextPage endCursor } } }",
  "variables": { "f": { "kind": "product", "tiering": 1 }, "n": 200 }
}
```
Tiering values: `1` = business-critical (Tier-1), `2` = important (Tier-2), `3` = standard (Tier-3). Use `totalCount` to report how many there are without extra queries.

### Products in a domain

```json
{
  "query": "query ByDomain($f: AssetFilter!, $n: Int!) { assets(filter: $f, first: $n) { totalCount edges { node { name tiering metadata } } pageInfo { hasNextPage endCursor } } }",
  "variables": { "f": { "kind": "product", "metadataFilter": { "governance": { "domain": "ORDER" } } }, "n": 100 }
}
```

### Teams and components in a domain

Use the `list-filtered` shortcut with `--group-by` — tallies per-team counts
server-page-by-page inside the script, in ONE shell call:

```bash
python3 <this-skill-dir>/scripts/kg_query.py list-filtered --kind component \
  --metadata-filter '{"governance": {"domain": "ORDER"}}' \
  --group-by orgRefs.teamOwner
```

Note: the field is `orgRefs.teamOwner` (not `orgRefs.team` — a common wrong guess).
Returns `{ distinct_groups, groups: [{value, count}, ...] }` sorted by count desc,
covering every matching component regardless of total size (internal pagination,
`first: 200` cap handled automatically). **Anti-pattern that caused a real
8-shell-call, ~449K-token outlier:** issuing one `raw` call per page with an
`after` cursor and manually tallying `orgRefs.team` (wrong field name, so every
count came back null) in the model's own context — always prefer
`list-filtered --group-by` for "how many X per Y" questions where Y's values
aren't a small known enum.

### Components by stack (Java 17)

```json
{
  "query": "query Stack($f: AssetFilter!, $n: Int!) { assets(filter: $f, first: $n) { edges { node { name stack { language languageVersion framework frameworkVersion } links { type url } } } pageInfo { hasNextPage endCursor } } }",
  "variables": { "f": { "kind": "component", "metadataFilter": { "stack": { "language": "Java", "language_version": "17" } } }, "n": 100 }
}
```

### Technology distribution (all stacks)

`stack.language` is filterable server-side via nested `metadataFilter` (confirmed
live) — **never** paginate through all components to count languages client-side.
Use the `breakdown` shortcut with the known language values, same one-call pattern
as lifecycle:

```bash
python3 <this-skill-dir>/scripts/kg_query.py breakdown --kind component \
  --breakdown-by stack.language --values Java JavaScript Python Go TypeScript
```

This returns exact counts + percentages for every value in ONE HTTP round trip —
no sampling, no pagination, no client-side counting. If you don't know which
language values exist, run `discover-metadata` first, or sample a handful of
`stack.language` values from a small `list-filtered` call (`--limit 10`) before
building the breakdown. **Anti-pattern that caused a real 12-shell-call,
~237K-token outlier:** issuing a `raw` query per page and re-querying with
different `after` cursors to manually tally languages — always prefer
`breakdown` for any "how many X vs Y vs Z" / distribution question.

### Lifecycle / typology breakdown (ratio, distribution, "how many are END_OF_LIFE")

`lifecycle` is a **known enum** (see API Schema section) — never paginate + eyeball this.
**Preferred:** use the bundled shortcut, which does this in one call and returns
ready-made percentages:

```bash
python3 <this-skill-dir>/scripts/kg_query.py breakdown --kind product \
  --breakdown-by lifecycle --values GENERAL_AVAILABILITY END_OF_LIFE BETA DEVELOPMENT DEPRECATED
```

Or the equivalent raw aliased `assetCount` request if you need it inline:

```json
{
  "query": "{ total: assetCount(filter: { kind: \"product\" }) ga: assetCount(filter: { kind: \"product\", metadataFilter: { \"lifecycle\": \"GENERAL_AVAILABILITY\" } }) eol: assetCount(filter: { kind: \"product\", metadataFilter: { \"lifecycle\": \"END_OF_LIFE\" } }) beta: assetCount(filter: { kind: \"product\", metadataFilter: { \"lifecycle\": \"BETA\" } }) dev: assetCount(filter: { kind: \"product\", metadataFilter: { \"lifecycle\": \"DEVELOPMENT\" } }) deprecated: assetCount(filter: { kind: \"product\", metadataFilter: { \"lifecycle\": \"DEPRECATED\" } }) }",
  "variables": {}
}
```
Compute percentages from each alias against `total` in one round trip. Same approach
for `typology` (values include `MAKE`; ask for/paginate a small sample first only if
you need to discover other typology values). **Do not** fully paginate all products
with `metadata` attached just to count lifecycle/typology buckets client-side — that
wastes a full-dataset fetch on data `assetCount` already answers in one call.

### Discovering unknown metadata fields

If the user's question references a concept not covered by "API Schema" above (e.g. an
attribute you haven't seen documented), don't invent field names or filter operators.
**Preferred:** run the bundled shortcut, which returns just the distinct key names
(no need to eyeball raw JSON):

```bash
python3 <this-skill-dir>/scripts/kg_query.py discover-metadata --kind product --sample 5
```

Or the equivalent raw query if you need it inline:

```json
{
  "query": "query Sample($n: Int!) { assets(filter: { kind: \"product\" }, first: $n) { edges { node { metadata } } } }",
  "variables": { "n": 5 }
}
```
Parse the returned `metadata` JSON client-side to find the real top-level key names,
then use that exact key in `metadataFilter` (top-level, not nested under `governance`
unless the key genuinely only exists there). Stop after this one lookup — do not keep
guessing filter shapes or non-existent operators (e.g. `fieldname_not`); if you need a
negated count, alias the positive counts you need and subtract/compare instead.

### Services with no monitoring

Use the aliased-count shortcut for the quick picture (one HTTP call):

```json
{
  "query": "{ total: assetCount(filter: { kind: \"component\" }) monitored: assetCount(filter: { kind: \"component\", metadataFilter: { observability: { datadog: [] } } }) }",
  "variables": {}
}
```
Note: `observability.datadog` is an **array**, not a scalar — equality filtering on it doesn't reliably express "non-empty", so this quick count is approximate. **For an accurate list of names** (and whenever the user asks "which services"), use the `list-filtered` shortcut with `--missing-field` — a single call that pages internally and only prints the (small) matching set:

```bash
python3 <this-skill-dir>/scripts/kg_query.py list-filtered --kind component \
  --missing-field metadata.observability.datadog --fields metadata.tiering --limit 50
```

This does server-side pagination (all pages, capped at 200/page) **inside the
script** and only returns components with an empty/missing `observability.datadog`
array, each annotated with `tiering` so you can flag Tier-1 (tiering `1`) gaps as
critical. **Anti-pattern that caused a real 7-shell-call, ~178K-token outlier:**
issuing separate `raw` pagination calls per page to manually scan for missing
`observability` — always prefer `list-filtered --missing-field` for "which X have
no Y configured" questions.

### Blast radius — clusters in a GCP region

⚠️ **Cluster `relationships` only reach one hop (`hosts` → component) — there is no
direct cluster→product edge.** Getting affected *products* requires a **second hop**:
each hosted component has its own `relationships(type: "partOf")` → product. GraphQL
lets you nest this in a **single query** (confirmed live), so don't discover this by
trial and error at runtime — this exact gap previously caused an **11-17 shell-call,
~1.1M-token outlier**: the model fetched all clusters (1 call), then all 834 products
with full `metadata` (one ~127KB call) trying to cross-reference names, then did a
separate `asset(name: ...)` lookup per hosted component to find its owning product.

**Preferred:** use the bundled shortcut — one call, does the 2-hop resolution and
de-duplicates components/products for you:

```bash
python3 <this-skill-dir>/scripts/kg_query.py blast-radius --region-prefix europe-west
```
(omit `--region-prefix` for all clusters). Returns `{ matching_clusters_total, clusters:
[{ name, region, hosted_components }], impacted_components: { count, names },
impacted_products: { count, items: [{ name, tiering }] } }` — ready to summarize
directly, no further queries needed.

Or the equivalent raw nested query if you need it inline (note the nested
`relationships(type: "partOf")` on `targetAsset` — this is what resolves products in
the same round trip):

```json
{
  "query": "query BlastRadius($n: Int!) { assets(filter: { kind: \"cluster\" }, first: $n) { totalCount edges { node { name metadata relationships(type: \"hosts\") { targetAsset { name kind relationships(type: \"partOf\") { targetAsset { name kind tiering } } } } } } } }",
  "variables": { "n": 200 }
}
```
Clusters are a small dataset (confirmed live: ~58 total, well under the `first: 200`
page cap) — fetch them unfiltered and filter by `metadata.deployment.region` prefix
client-side, rather than issuing one exact-match query per region variant (region
matching via `metadataFilter` is exact, e.g. `europe-west4`, not a `europe-west` prefix).

> ⛔ **Do not**: fetch all products with `metadata` to cross-reference names, or issue
> one `asset(name: ...)` lookup per hosted component to find its product — both are the
> exact anti-pattern that caused the historical outlier. The nested query above (or the
> `blast-radius` shortcut) resolves everything in one round trip.
>
> ⚠️ **Your answer MUST always contain the word "product"** — either listing found products, or explicitly noting their absence if `impacted_products.count` is 0.

### Named cluster detail

When the user asks about a specific cluster by name (region, cloud provider, hosted components):


```json
{
  "query": "query ClusterDetail($n: String!) { asset(name: $n) { name kind type tiering metadata relationships { type targetAsset { name kind tiering } } } }",
  "variables": { "n": "dcp-eu-02-prod-24cu-production" }
}
```

Parse `metadata.deployment` for infrastructure info: `region`, `cloud_provider`, `environment`, `cluster_type`. List hosted assets from `relationships` — filter `targetAsset.kind == "component"` for services running on that cluster.

### Assets in a deployment namespace

```json
{
  "query": "query Namespace($f: AssetFilter!, $n: Int!) { assets(filter: $f, first: $n) { totalCount edges { node { name kind type tiering metadata } } pageInfo { hasNextPage endCursor } } }",
  "variables": { "f": { "metadataFilter": { "deployment": { "namespace": "oneff" } } }, "n": 200 }
}
```
Returns all assets (any `kind`) deployed in the given namespace. Only request the fields you need — use `name kind type` for lists, add `metadata` only when full details are required. If paginating, use `first: 200` (the page cap).

### Spring Boot components

`stack.framework` is filterable server-side via nested `metadataFilter` (confirmed
live — filters exactly, no client-side substring check needed). A component's
**owning product is on its own metadata** at `metadata.governance.product` — there
is **no relationship traversal needed** to resolve it (components are not linked
to products via `relationships` in this graph; that field is only populated for
cluster→component `hosts` edges — see "Blast radius" below).

```bash
python3 <this-skill-dir>/scripts/kg_query.py list-filtered --kind component \
  --metadata-filter '{"stack": {"framework": "Spring Boot"}}' \
  --fields metadata.stack.framework_version,metadata.governance.product --limit 50
```

One shell call, server-side filtered, paginates internally, returns just
`{ name, framework_version, governance.product }` per row plus an exact
`server_side_matched_total`. **Anti-pattern that caused a real 6-shell-call,
~321K-token outlier:** filtering only by `stack.language: "Java"` (too broad —
matches all Java components, not just Spring Boot) then trying to resolve each
component's product via a `relationships` lookup (which returns empty — there's
no such edge) instead of just reading `metadata.governance.product` directly.

### Unscanned components (no stack)

```bash
python3 <this-skill-dir>/scripts/kg_query.py list-filtered --kind component \
  --missing-field metadata.stack --limit 50
```

One shell call — the script pages through all components internally (server caps
`first` at 200/page) and returns only the ones with a missing/null `metadata.stack`
block, i.e. never scanned. **Anti-pattern that caused a real 13-shell-call,
~525K-token outlier:** manually issuing one `raw` request per page with an `after`
cursor and eyeballing each page's `stack` field in the model's own context —
always prefer `list-filtered --missing-field` instead.

---

## Hard Rules

1. **Never fabricate data** — if API returns 0 results, say so
2. **`metadataFilter` via variables** — pass JSON filter objects as variables, never inline them in the query string (avoids escaping errors)
3. **Use `assetCount` for counts** — `assetCount(filter: { kind: $kind })` runs a single COUNT(*) and is always accurate; never paginate when you only need totals; alias multiple `assetCount` calls in one request to avoid extra round trips
4. **`totalCount` avoids extra count queries** — include `totalCount` in any `assets(...)` query to know the full size without a separate `assetCount` call
5. **Minimal field selection** — request only fields you will use in the answer; omit `metadata`, `relationships`, `deployments`, `links`, `orgRefs` unless the question requires them
6. **Retry on failure** — if the script exits non-zero or returns an HTTP error, retry ONCE with a simpler query (remove `metadata`, `orgRefs`, `relationships` if present, reduce `first` to 50). If the second attempt also fails, report the error and stop.
7. **Stop on repeated errors** — report and stop after the same error twice; treat a top-level `errors` array in the response body as a failure (unless partial `data` is also present and sufficient to answer)
8. **Pagination:** `first` + `after` always; use `first: 200` (API hard cap — higher values are silently capped at 200); paginate via `after: endCursor` until `hasNextPage` is false; stop paginating as soon as you have enough data to answer
9. **Omit `after` on the first page** — only include it in subsequent paginated calls; missing optional variables are safe to omit in GraphQL
10. **Always respond in English**
11. **Use the bundled `kg_query.py`, not a second skill** — this skill's own `scripts/kg_query.py` handles auth and the GraphQL POST directly. Only fall back to `read_skill decathlon-api-tool` (a different repository) if `kg_query.py` is missing or cannot locate an auth module.
12. **Never use `http_request` or `get_env` tools** — use the `shell` tool with `kg_query.py` (or the `decathlon-api-tool` fallback); `http_request` will fail with 401, and `get_env` will not find script paths.
13. **Stop guessing after 2 failed field/operator attempts** — if a `metadataFilter` key or a filter operator you tried returns an error or an implausible result (e.g. `0` when you expected matches) twice in a row, stop inventing more field names. Run the "Discovering unknown metadata fields" pattern (one 5-row sample) instead of continuing to probe — this is cheaper and prevents multi-round-trip token blowups on undocumented fields.
14. **Never fully paginate to compute a breakdown over a known enum field** (`lifecycle`, `tiering`, `typology`, language, framework) — use aliased `assetCount` calls (one per bucket, one HTTP round trip) instead of fetching every edge with `metadata` and counting client-side.
15. **Never resolve a multi-hop relationship (e.g. cluster→component→product) with one `asset(name: ...)` lookup per intermediate node** — nest `relationships(type: "...")` on `targetAsset` instead to resolve all hops in a single query. Use the `blast-radius` shortcut for cluster→product impact analysis specifically.
16. **`metadataFilter` matches nested paths, not just top-level keys** — e.g. `{ "stack": { "framework": "Spring Boot" } }` filters exactly server-side. Never fetch all rows and filter client-side for a nested field you haven't confirmed is unfilterable.
17. **A component's owning product is on its own `metadata.governance.product`** — never traverse `relationships` to find it; components have no product-pointing relationship edges in this graph (only clusters→components via `hosts`).
18. **Never hand-roll a pagination loop across multiple shell calls** for "list all X matching Y" or "which X are missing field Y" — use `list-filtered` (server-side `--metadata-filter` and/or client-side `--missing-field`, both paginate internally in ONE shell call) instead of issuing one `raw` call per page with `after` cursors.
19. **For any question not covered by a named pattern below (novel/unexpected phrasing, averaging, thresholds, top-N, group-by on a field without a small enum, presence-of-a-nested-array-element checks, etc.) — use `query` (see "Generic query engine" above) before falling back to `raw` pagination.** Compose `--where`/`--metric`/`--group-by`/`--sort-by` to express the question; do not invent a new script feature or hand-roll pagination just because the exact phrasing hasn't been seen before.
20. **Request every field you'll need in a SINGLE `--fields` list, not one call per attribute.** If a question needs several attributes of the same entity (e.g. tiering AND businessScore AND lifecycle of a product), put them all in one `--fields a,b,c` (or one `asset(name:...)` lookup with all the sub-fields) instead of re-querying the same entity again later for an attribute you could have asked for the first time. If you already fetched an asset's `components[]` array in a lookup, **count its length client-side** — do not also issue a separate `--metric count` / `metadataFilter` query for the same count; you already have the data.
