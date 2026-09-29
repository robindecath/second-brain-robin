---
name: incident-investigation
description: "Incident management investigation process: look up the SLO definition in the slo-generator repo first, then fetch the live SLO value and error budget from Datadog. Also triggered when a Datadog monitor title is pasted (format: [product][env][technology] alert description) — parses the monitor naming convention to extract service, environment, technology hint, and template variables, then runs a full incident investigation. Use when investigating an incident, checking if an SLO is breached, assessing impact, preparing an incident report, checking the health status of a product/asset/service, or when a Datadog monitor alert fires. Keywords: incident, investigation, SLO breach, error budget, reliability, impact, outage, degradation, on-call, postmortem, alert, monitor, monitor alert, monitor title, Datadog monitor, CrashloopBackOff, Kafka lag, pod restart, Kubernetes alert, user journey, health, health check, status, is healthy, is down, is degraded, product health."
argument-hint: "<service-or-feature-name>"
user-invocable: true
license: MIT
metadata:
  version: 1.0.1
  last-updated: 2026-07-08
  audience: all
  domain: sre
  api: rest
  mcp_required: true
  owner: sig-reliability
---

# Incident Investigation

Four-phase process, fully parallelised to minimise investigation time.

Mandatory behavior: always determine if there is an ongoing incident, always output the status of every executed search (with extracted values when present, otherwise explicit no-data), and always query Atlassian (Confluence) via MCP to detect recurrence. If the user asks directly for latest incidents/history, start with Atlassian post-mortems before Datadog/SLO queries.

## When to Use

- An alert fired and you need to assess SLO impact
- Checking whether an ongoing incident has breached an SLO
- Estimating remaining error budget before/during an incident
- Preparing incident report with reliability context
- Post-incident review — understanding which SLOs were affected
- Assessing blast radius across user journeys
- **Checking the health of a product / asset / service** (e.g. "what is the status of oneff?", "is web-checkout healthy?", "onepay health status")
- Confirming whether there is an active incident for a service/feature/infra scope
- **Retrieving latest incidents directly** (e.g. "last incidents for oneff")
- **Datadog monitor alert fired** — user pastes a monitor title such as `[Secondlife-refurbish][production][Kubernetes] Pod {{pod_name.name}} is CrashloopBackOff` or `[OnePromotion][Production] Kafka lag is not decreasing since 1 hour`

---

## Procedure

### Step 0 — Load reference data (best-effort — non-blocking)

Attempt to read the reference file:

```
incident-investigation/references/uj_mapping.md     ← UJ blast radius index
```

**Three outcomes — handle each explicitly:**

| Outcome                              | Action                                                                                                                                                                                              |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ File found AND service present    | Extract `impacted_uj_keys` and `war_room_slack_channels` → use in Phase 0A Tier 3                                                                                                                   |
| ⚠️ File found BUT service not listed | Note `"<service> not yet in uj_mapping.md — referential under construction"`. Proceed without UJ pre-seed; Phase 0A Tier 1 (blast-radius-analyzer) and Tier 2 (KG direct) will resolve UJ coverage. |
| ❌ File not found                    | Note `"uj_mapping.md unavailable"`. Proceed immediately to Phase 0A — do NOT stop. Tier 1 and Tier 2 are fully autonomous; uj_mapping.md is only a fast-path optimisation.                          |

> The referential is under active construction. Missing entries are expected and do NOT indicate an error. Never block an investigation on this file.

---

### Step 1 — Identify the incident scope

> **If the invoking agent already specified the mode** (e.g. `invoke in Mode A — service-level incident on oneff`), use it directly and skip the detection below.

Four modes depending on what the user provides:

**Mode A — Service-level incident** (e.g. "incident on oneff", "onepay is down"):  
Use the service name directly → go to Phase 0A.

**Mode B — Infrastructure-level incident** (e.g. "incident on europe-west1 GCP", "cluster X is down", "GKE namespace Y is failing"):  
Extract the infrastructure signal (region / cluster / namespace / provider) → go to Phase 0B first, then Phase 0A with results.

**Mode C — Health check** (e.g. "what is the status of oneff?", "is web-checkout healthy?", "onepay health status"):  
Treat as Mode A but **skip Phase 2 (root cause) and Phase 3 (post-mortems)**. Run Phase 0A + Phase 1 only, and output a **Health Report** (see output format below) instead of the full incident report.

**Mode D — Latest incidents request** (e.g. "last incidents", "last 3 months incidents" for a product/component/UJ):  
Run **Phase 0A then Phase 3 first** (Atlassian MCP post-mortems scoped via UJ keys from `uj_mapping.md`). This is the first source of truth.  
Then:

- if user asked only history/latest incidents: return the historical section directly;
- if user also asked current status: continue with Phase 1 (and Phase 2 if needed).

**Mode E — Datadog monitor alert** (user pastes a monitor title or message body):  
Examples:

- `# [Secondlife-refurbish][production][Kubernetes] Pod {{pod_name.name}} is CrashloopBackOff on namespace {{kube_namespace.name}}`
- `# [OnePromotion][Production] Kafka lag is not decreasing since 1 hour for some of our consumers !`
- `[[OneCheckout] [Production] [APIM] APIM Error Budget Burn Rate 32.701 on checkouts]`

Parse the monitor title using the standard Decathlon monitor naming convention. **Two accepted formats** (normalise before parsing):

```
[<product>][<environment>][<optional: technology>] <alert description>       ← compact (no spaces between brackets)
[[<product>] [<environment>] [<optional: technology>] <alert description>]   ← spaced (outer brackets, spaces between tokens)
```

> Pre-processing: strip one layer of outer `[` `]` if the entire title is wrapped, then collapse any `] [` → `][` so both formats reduce to the same token sequence.

Extraction steps (in order):

1. **Product / service** — first bracket token → becomes the primary investigation scope (e.g. `Secondlife-refurbish`, `OnePromotion`, `OneCheckout`). Normalise: lowercase, replace `-` with space when searching.
2. **Environment** — second bracket token → `production`, `staging`, etc. Scope Datadog queries accordingly.
3. **Technology hint** (optional third bracket) — guides investigation specialisation:
   - `Kubernetes` / `k8s` → treat as **infra-scoped** incident → run Phase 0B (namespace/cluster blast radius) before Phase 0A.
   - `Kafka` / `kafka` → message-queue lag or consumer failure → add `kafka` and `consumer` to log/event queries in Phase 1D and Phase 2E.
   - `APIM` → API Management error budget / burn rate alert → treat as **SLO-focused incident**: skip Phase 0B; in Phase 1 prioritise query B (`mcp_datadog_search_datadog_slos`) and query A (`gh search code` in slo-generator); add `apim` and `burn_rate` as secondary filters in log/event queries; extract the numeric burn rate value from the alert description and include it in the Symptoms section as `current burn rate`.
   - `GCP` / `AWS` / `Azure` → cloud-provider issue → Phase 0B with region from alert body.
   - Any other value (e.g. `Redis`, `PostgreSQL`, `Nginx`) → add as secondary service filter in Phase 2F dependency search.
4. **Numeric values in the alert description** (e.g. `32.701` in `APIM Error Budget Burn Rate 32.701`) — treat as a measured metric value: include verbatim in the Symptoms table under a `Measured value` column, and use it as context when evaluating SLO breach severity.
5. **Template variables** (e.g. `{{pod_name.name}}`, `{{kube_namespace.name}}`) — these are Datadog runtime values. Extract them to use as _additional filters_ in Phase 1 and Phase 2 queries:
   - `{{kube_namespace.name}}` → add `kube_namespace:<value>` tag to log/span queries when the actual value is known from context; otherwise note "namespace: runtime value — will narrow query if provided".
   - `{{pod_name.name}}`, `{{host.name}}` → use as `host:` or container filter in log queries.
   - `{{value}}` / `{{threshold}}` → note in symptoms section, do not use as query filter.
6. **Alert description** (remainder after the last bracket) → used as semantic context for Phase 1C incident search and Phase 2E log pattern.

After extraction, treat this as a **Mode A incident** (full investigation) and proceed from Phase 0B (if tech hint = Kubernetes/infra) or Phase 0A (otherwise). Also fetch the live Datadog monitor status in Phase 1 by adding query:

| #   | Tool                                                                             | Purpose                                                                                   |
| --- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| A′  | `mcp_datadog_search_datadog_monitors` — `<product> <alert description keywords>` | Confirm monitor state + fetch current `{{template.variable}}` values from last evaluation |

If none is provided, ask: **"Which service, cluster, or infrastructure is affected?"**

---

### Phase 0B — Knowledge Graph blast radius (infrastructure incidents only)

> Skip this phase for service-level incidents. Run it **before Phase 0A** when the incident is infrastructure-scoped.

**Primary method — load `blast-radius-analyzer` skill:**

Load and invoke `blast-radius-analyzer` with the impacted region, cluster, or namespace as `incident_target`. It returns the full list of impacted products, components, tiering, and team owners.

**Fallback — if `blast-radius-analyzer` is unavailable**, load
`knowledge-graph-query` and use its bundled `kg_query.py` script. Resolve
`<knowledge-graph-query-skill-dir>` from that skill's `<location>` tag:

```
<knowledge-graph-query-skill-dir>/scripts/kg_query.py
```

#### B1 — Find clusters in the impacted region/zone

```bash
python3 <knowledge-graph-query-skill-dir>/scripts/kg_query.py raw \
  --data '{"query":"query Region($f:AssetFilter!,$n:Int!){assets(filter:$f,first:$n){edges{node{name metadata relationships{type targetAsset{name kind tiering}}}}pageInfo{hasNextPage endCursor}}}","variables":{"f":{"kind":"cluster","metadataFilter":{"deployment":{"region":"<region>"}}},"n":100}}'
```

> ⚠️ If the user says `europe-west1` (or any region without a number), **try ALL variants** (`europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`) in **parallel** and aggregate.

#### B2 — If cluster name is known directly

```bash
python3 <knowledge-graph-query-skill-dir>/scripts/kg_query.py raw \
  --data '{"query":"query Asset($n:String!){asset(name:$n){name kind metadata relationships{type targetAsset{name kind tiering orgRefs}}}}","variables":{"n":"<cluster-name>"}}'
```

#### B3 — If namespace is known

```bash
python3 <knowledge-graph-query-skill-dir>/scripts/kg_query.py raw \
  --data '{"query":"query NS($f:AssetFilter!,$n:Int!){assets(filter:$f,first:$n){edges{node{name metadata orgRefs relationships{type targetAsset{name kind tiering}}}}}pageInfo{hasNextPage endCursor}}}","variables":{"f":{"kind":"component","metadataFilter":{"deployment":{"namespace":"<namespace>"}}},"n":200}}'
```

**From either method**, extract:

- All **products** and **components** in the impact zone
- Their `tiering` (1 = critical, 2 = important, 3 = standard)
- Their `orgRefs` (team owner, domain)

These product/component names become the **service list** for Phase 0A — cross-reference them with `uj_mapping.md`.

---

### Phase 0A — User Journey blast radius (ALWAYS — for both modes)

> ⛔ **HARD STOP.** This phase is synchronous — it must complete fully before Phase 1-pre or Phase 1.

Execute the following **three-tier fallback chain in strict order**. Move to the next tier only if the current one fails or returns no usable data.

---

#### Tier 1 — `blast-radius-analyzer` (PRIMARY — always attempt first)

Load and invoke `blast-radius-analyzer` with the service name as `incident_target`.

It returns the full blast radius: impacted products, components, User Journeys, war room channels, tiering, and team owners.

**If `blast-radius-analyzer` responds with data → stop here. Do NOT call Tier 2 or Tier 3.**

---

#### Tier 2 — `knowledge-graph-query` (FALLBACK — only if Tier 1 fails or is unavailable)

Invoke `knowledge-graph-query` with the service name to retrieve from AppReferential:

- `metadata.deployment.namespace` and cluster assignment
- `metadata.observability` (Datadog service tag, dashboard refs)
- `tiering` (1 = critical, 2 = important, 3 = standard)
- `orgRefs` (team owner, domain)
- upstream/downstream `relationships`

Use the relationships to identify co-risk services. Cross-reference each service found against `uj_mapping.md` (Tier 3 step 1) to resolve UJ keys.

**If `knowledge-graph-query` responds with data → use it to build the blast radius, then complete missing UJ/moment detail via Tier 3 steps 1–4 only. Do NOT re-run the full Tier 3 chain independently.**

Note in the Search Execution Status: `Phase 0A: Tier 1 unavailable — fell back to Tier 2 (KG direct) + Tier 3 UJ lookup`.

---

#### Tier 3 — `uj_mapping.md` (LAST RESORT — only if both Tier 1 and Tier 2 fail, OR to fill gaps left by Tier 2)

> ⚠️ The referential is under active construction. If the service is not listed, this is expected — proceed with what Tier 1/2 returned.

**Steps (execute sequentially, 1 → 5):**

1. **Reverse lookup**: find `service_id` in `uj_mapping.md` reverse index → read `impacted_uj_keys` directly. This is the primary blast radius set.
   - **If service not found**: skip steps 2–4, note `"<service> not yet in uj_mapping.md"` in Search Execution Status, and proceed with an empty UJ set. Do NOT block.

2. **Forward expansion** — use the **UJ hierarchy section** of `uj_mapping.md`: for each UJ key from step 1, look up the moment → services table to enumerate every service involved in each moment. These additional services are at risk.

3. **Single transitive pass**: for each new service discovered in step 2 that was not in the original scope, run step 1 once (no further recursion) to catch any additional UJ keys.

4. **Deduplicate** the full merged UJ key set from steps 1 and 3.

5. Build the **blast radius table** (see output format below).

Note in the Search Execution Status: `Phase 0A: Tier 1 and Tier 2 unavailable — used uj_mapping.md only. Tier and namespace unknown.` if Tier 2 was also skipped.

---

### Phase 1-pre — SLO Contract Discovery (BLOCKING — complete before Phase 1)

> ⛔ **HARD STOP.** Invoke the `slo-generator` skill for each service in scope. Do NOT fire any Phase 1 query until this step is complete.

For each service identified in Phase 0:

1. Invoke `slo-generator` with the service name — it discovers every SLI YAML in `dktunited/slo-generator` and reads each file's full content
2. Collect every `metadata.name` value — this is the **exact Datadog SLO identifier** (e.g. `slo-oneff-api-get-scenario-latency_600ms-app-eu`)
3. Also collect per SLI: `spec.goal`, `metadata.labels.feature_name`, `metadata.labels.slo_name`, `metadata.labels.support_group`
4. If slo-generator returns no YAMLs for a service, note it explicitly — do NOT skip or omit the SLO table from the report

Build an SLI registry before continuing:

| `metadata.name`                             | feature | slo_name | goal  | support_group |
| ------------------------------------------- | ------- | -------- | ----- | ------------- |
| `slo-<service>-<feature>-<type>-<platform>` | …       | …        | XX.X% | ce-…          |

Only when this registry is complete, proceed to Phase 1.

---

### Phase 1 — Launch ALL queries in parallel (no waiting between them)

Fire all of the following tool calls **simultaneously** in a single batch — one set per impacted service identified in Phase 0:

| #   | Tool                                                                                                           | Purpose                                |
| --- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| B   | `mcp_datadog_search_datadog_slos` — **one call per SLI**: `name:<metadata.name>` (from Phase 1-pre registry)   | Live SLO status + error budget per SLI |
| C   | `search_datadog_monitors` — `status:(alert OR warn`                                                            | Firing monitors                        |
| D   | `search_datadog_logs` — `service:<service> status:(error OR critical)`, `use_log_patterns:true`, `from:now-2h` | Recent error patterns                  |

> **Query B MUST use `name:<metadata.name>`** — one Datadog call per SLI from Phase 1-pre. Do NOT use `service:<service>`: it returns unrelated SLOs and misses platform-scoped variants (EU, US, AS).

#### Incident presence decision (required after Phase 1):

Evaluate the firing monitors returned by **Query C** for the target **investigated_scope** (e.g., service name) to set `incident_in_progress`:

1. **Exclusion Pre-processing:**
   - **Ignore** any firing monitor that **lacks a Priority OR lacks Handles** which are in a composite monitor. These are sub-component monitors used inside composite alerts and do not represent standalone anomalies.

2. **Set `incident_in_progress = true`** if **ANY** of the remaining valid firing monitors meet either condition:
   - Priority is **P1** or **P2** **AND** matches the `investigated_scope`.
   - Priority is **P3**, **P4**, or **P5** **AND** matches the `investigated_scope` **AND** has a high probability/confidence of being linked to the current incident.

3. **Set `incident_in_progress = false`** under all other circumstances (e.g., Query C returns no monitors, all firing monitors were excluded in step 1, monitors fall outside the `investigated_scope`, or remaining P3+ monitors have low confidence).

If `incident_in_progress == false`, continue investigation in health/degradation mode and still provide all output sections that are available, including per-query status and extracted values.

Note : **No incidents are declared in Datadog**. Do not try to find incidents in Datadog. It's not relevant because we use SMAX as a ITSM.

#### Per-query status capture (required):

For each query A/B/C/D (and E/F/G/H/I/J/K when executed), record:

- `status`: `success_with_data` | `success_no_data` | `error`
- `query_used`: the final query string used (including fallback attempts)
- `key_values`: extracted values (SLO %, error budget %, incident ids/states, dominant error/count, dependency names, deployment versions, post-mortem links)
- `notes`: fallback/retry behavior and ambiguity notes

#### From Phase 1-pre (slo-generator):

The SLI registry built in Phase 1-pre is the authoritative source for all SLO data. Verify it contains at minimum:
| Field | What it tells you |
|-------|-------------------|
| `metadata.name` | Exact Datadog SLO identifier — used as `name:` query in query B |
| `metadata.labels.feature_name` | Specific feature/endpoint covered |
| `metadata.labels.slo_name` | Type of SLO: availability, latency… |
| `metadata.labels.support_group` | **Team responsible (for escalation)** |
| `spec.goal` | The SLO target (e.g. `0.999` = 99.9%) |

If slo-generator returned no YAMLs, note it explicitly — do NOT skip the SLO table in the output.

#### From query B (Datadog SLOs):

Query B fires one `mcp_datadog_search_datadog_slos` call per `metadata.name` from Phase 1-pre. For each result, read: current `status` (ok / alert / breached), `error_budget_remaining` for 7d and 30d, `sli` value.

If a `name:<metadata.name>` query returns no result, retry once with the name without its platform suffix (e.g. drop `-app-eu` → `name:slo-oneff-api-get-scenario-latency_600ms-app`). Do NOT fall back to `service:<service>` — this query is too broad and does not map 1-to-1 to SLIs.

#### From query D (logs):

Identify the **dominant error pattern** (highest count). Note the exact error message — it drives Phase 2.

---

### Phase 2 — Root cause: one parallel batch

Once Phase 1 results are available, fire these **simultaneously**:

| #   | Tool                                                                                                                                                                           | When to use                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| E   | `mcp_datadog_search_datadog_logs` — `service:<service> "<dominant error from D>"`, `use_log_patterns:false`, add `extra_fields:["error.message","http.status_code","version"]` | Get error details                |
| F   | `mcp_datadog_search_datadog_service_dependencies` — `service:<service>`, scope to `env:prod OR env:production`                                                                 | Identify downstream dependencies |
| G   | `mcp_datadog_search_datadog_events` — `service:<service> env:production`, `from:now-8h`                                                                                        | Spot recent deployments          |

Then, based on results:

- If a **downstream dependency returns 503/timeout**: get a sample trace with `mcp_datadog_get_datadog_trace` using a trace_id from the error logs
- If a **config/file missing error** appears in a dependency: search that dependency's logs with `mcp_datadog_search_datadog_logs`
- If a **deployment event** correlates with the incident start: note the version and cluster

---

### Phase 3 — Post-mortem correlation (Atlassian MCP / Confluence)

> **MCP tools required:** `confluence_search`, `confluence_get_page_by_id` — provided by the Atlassian MCP server. If the MCP is unavailable, skip this phase and note it in the Search Execution Status.

Run **simultaneously** with or after Phase 2.

If `incident_in_progress == false`, this phase becomes mandatory for historical analysis and must include a 3-month lookback.

#### Step 1 — Identify Confluence search scope from `uj_mapping.md`

For each impacted UJ identified in Phase 0A, read the **Confluence Coordinates** section of `uj_mapping.md` and extract:

- `confluence_space_id` — the Confluence space to scope the search
- `confluence_parent_id` — the parent page ID under which post-mortems are filed

Also extract from context already available:

- `service_id` (from the investigation scope)
- `impacted_uj_keys` (from the reverse index)
- `war_room_slack_channels`

If `confluence_space_id` and `confluence_parent_id` are filled in → use **scoped CQL** (Step 2A).
If they are empty → fall back to **full-text CQL** (Step 2B).

#### Step 2A — Scoped CQL (when `confluence_space_id` and `confluence_parent_id` are available)

Fire these **simultaneously**:

| #   | Tool                | Query                                                                                                                                                                                                                                              |
| --- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H   | `confluence_search` | CQL: `space = "<confluence_space_id>" AND ancestor = <confluence_parent_id> AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC`                                                                  |
| I   | `confluence_search` | CQL: `space = "<confluence_space_id>" AND ancestor = <confluence_parent_id> AND text ~ "<service>" ORDER BY lastModified DESC`                                                                                                                     |
| L   | `confluence_search` | CQL (no-active-incident mode): `space = "<confluence_space_id>" AND ancestor = <confluence_parent_id> AND lastmodified >= startOfDay("-90d") AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC` |

#### Step 2B — Full-text CQL fallback (when no coordinates available)

Fire these **simultaneously**:

| #   | Tool                | Query                                                                                                                                                                                           |
| --- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H   | `confluence_search` | CQL: `text ~ "<service>" AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC`                                                                  |
| I   | `confluence_search` | CQL: `text ~ "<uj-key>" AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC`                                                                   |
| L   | `confluence_search` | CQL (no-active-incident mode): `text ~ "<service>" AND lastmodified >= startOfDay("-90d") AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC` |

If the above returns no results, fall back to:

| #   | Tool                | Query                                                                                                                                              |
| --- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| J   | `confluence_search` | CQL: `text ~ "<service alias or short name>" AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC` |
| K   | `confluence_search` | CQL: `text ~ "<dominant error from D>" AND (title ~ "post mortem" OR title ~ "postmortem") ORDER BY lastModified DESC` — only if error is specific |

If `incident_in_progress == false`, also run a global fallback for historical view:

| #   | Tool                | Query                                                                                                                                                                                                            |
| --- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| M   | `confluence_search` | CQL: `(text ~ "<service or alias>" OR title ~ "<service or alias>") AND lastmodified >= startOfDay("-90d") AND (title ~ "post mortem" OR title ~ "postmortem" OR title ~ "incident") ORDER BY lastModified DESC` |

**Expand scope if still no results**: retry with known aliases for the service (e.g., common short names or team-prefixed variants like `CE-ONEFF`, `ONEFF`).

#### Step 3 — Extract post-mortem content

For each matching page, retrieve with `confluence_get_page_by_id` and extract:

- **date**, **impacted services**, **root cause**, **resolution**, **duration**, **follow-up actions**
- **incident summary** — a brief 1-2 sentence description of what happened (extracted from page body or incident title + first paragraph)

**Similarity scoring** — a post-mortem is relevant if it matches ≥ 2 of:

- Same service impacted
- Same error type (database, timeout, OOM, deploy, config…)
- Same downstream dependency failing
- Same time-of-day pattern (optional)

#### Step 4 — Historical incidents summary when no active incident

If `incident_in_progress == false`, build a 3-month history from H/I/L/J/K/M results for all products/services in impacted UJs:

- deduplicate by Confluence page id;
- keep only entries with incident/post-mortem semantics;
- sort by date desc;
- include up to 20 entries in detail and a per-product count summary.

---

## Output Format

_Note: Whenever you mention Datadog data (SLOs, monitors, logs, events), always include a link to the "explorer" view of the query in Datadog, so the user can click through to see the live data._

```markdown
## Incident Investigation — `<service / infra scope>`

### Incident Presence

- `incident_in_progress`: `true|false`
- `incident_sources`: Datadog incidents query C (+ ids/states when present)
- `decision`: Active incident / No active incident (health-degradation assessment only)

### 🔴 Root Cause

<1-2 sentence summary of what is broken and why>

---

### 🏗️ Infrastructure Blast Radius (Knowledge Graph)

> _Only present for infrastructure-scoped incidents (region / cluster / namespace). Omit section for pure service-level incidents._

| Asset                 | Kind                | Tiering      | Team     | Domain     | Deployed On |
| --------------------- | ------------------- | ------------ | -------- | ---------- | ----------- |
| `<product/component>` | product / component | T1 / T2 / T3 | `<team>` | `<domain>` | `<cluster>` |

**Impacted clusters:** `<cluster-1>`, `<cluster-2>`  
**Region:** `<region>`

---

### 💥 Blast Radius — User Journeys

| User Journey | War Room Slack     | Impacted Moment Keys               | Other Services at Risk       |
| ------------ | ------------------ | ---------------------------------- | ---------------------------- |
| `<uj-key>`   | `#<slack-channel>` | `<moment-key-1>`, `<moment-key-2>` | `<service-a>`, `<service-b>` |

---

### 📊 SLO Impact per Impacted Service

> **MANDATORY.** This table must be present in every report. Populate from Phase 1-pre (slo-generator) + Phase 1 query B (Datadog live values). If slo-generator returned no YAMLs, state: `No SLI definitions found in dktunited/slo-generator for <service>.` — do NOT omit the section.

| Service     | SLO Name          | Feature          | Target | Status       | Error Budget 7d | Error Budget 30d |
| ----------- | ----------------- | ---------------- | ------ | ------------ | --------------- | ---------------- |
| `<service>` | `<metadata.name>` | `<feature_name>` | XX.X%  | ✅ / ⚠️ / 🔴 | XX% remaining   | XX% remaining    |

---

### 📚 Similar Past Incidents (Post-mortems)

| Date       | Title          | Link              | Incident Summary             | Root Cause | Impacted Services | Resolution    |
| ---------- | -------------- | ----------------- | ---------------------------- | ---------- | ----------------- | ------------- |
| YYYY-MM-DD | `<page title>` | [Confluence](url) | `<1-2 sentence description>` | <summary>  | <services>        | <fix applied> |

> _No similar post-mortems found_ — if table is empty.

---

### 🗂️ Historical Incidents — Last 3 Months (only when `incident_in_progress == false`)

| Date       | Product/Service | UJ         | Title          | Link              | Incident Summary             | Recurrence Hint                                          |
| ---------- | --------------- | ---------- | -------------- | ----------------- | ---------------------------- | -------------------------------------------------------- |
| YYYY-MM-DD | `<service>`     | `<uj-key>` | `<page title>` | [Confluence](url) | `<1-2 sentence description>` | `same symptom` / `same dependency` / `same service only` |

If no entries were found in the last 90 days, output:

- `No incident historized in Confluence for impacted UJs over the last 3 months.`

---

### Symptoms

| Service     | Error              | Volume (2h) | Since     |
| ----------- | ------------------ | ----------- | --------- |
| `<service>` | `<dominant error>` | N           | HH:MM UTC |

---

### SLO Contract (slo-generator) — primary service

| Field            | Value                  |
| ---------------- | ---------------------- |
| Service          | `<service_name>`       |
| Feature          | `<feature_name>`       |
| SLO type         | availability / latency |
| Target           | XX.X%                  |
| Responsible team | `<support_group>`      |
| Repo file        | [link]                 |

---

### Recommended Actions

- [ ] Escalate to `<support_group>`
- [ ] Notify war rooms: `<slack channels from impacted UJs>`
- [ ] <specific fix based on root cause>
- [ ] If similar post-mortem found: check if previous fix still applies (`<resolution from PM>`)
- [ ] Monitor error budget consumption on all impacted services

---

### Search Execution Status (mandatory, even when no active incident)

| Query             | Tool                                   | Status                                            | Query Used                     | Values Found                                  | Notes                                           |
| ----------------- | -------------------------------------- | ------------------------------------------------- | ------------------------------ | --------------------------------------------- | ----------------------------------------------- |
| 0A-T1             | `blast-radius-analyzer` skill          | `success_with_data` / `skipped` / `error`         | `<service name passed>`        | `<UJs, tiers, orgRefs>`                       | `<if skipped: reason>`                          |
| 0A-T2             | `knowledge-graph-query`                | `success_with_data` / `skipped` / `error`         | `<service name passed>`        | `<namespace, cluster, tiering, orgRefs>`      | `<only if Tier 1 failed>`                       |
| 0A-T3             | `uj_mapping.md`                        | `success_with_data` / `skipped` / `error`         | —                              | `<impacted_uj_keys, war_room_channels>`       | `<only if Tier 1+2 failed, or to fill UJ gaps>` |
| 1-pre             | `slo-generator` skill                  | `success_with_data` / `success_no_data` / `error` | `<service name passed>`        | `<list of metadata.name extracted>`           | `<nb SLIs found, any files unreadable>`         |
| B                 | `mcp_datadog_search_datadog_slos` (×N) | `success_with_data` / `success_no_data` / `error` | `name:<metadata.name>` per SLI | `<status, error_budget_7d, error_budget_30d>` | `<nb calls fired, any name-suffix retry>`       |
| C                 | `mcp_datadog_search_datadog_incidents` | `success_with_data` / `success_no_data` / `error` | `<final query>`                | `<incident ids, states, started_at>`          | `<used for incident_in_progress decision>`      |
| D                 | `mcp_datadog_search_datadog_logs`      | `success_with_data` / `success_no_data` / `error` | `<final query>`                | `<dominant error, count, since>`              | `<pattern mode enabled>`                        |
| E/F/G/H/I/J/K/L/M | `<tool>`                               | `success_with_data` / `success_no_data` / `error` | `<final query>`                | `<key extracted fields>`                      | `<only if query executed>`                      |
```

---

## Edge Cases

- **No YAML in slo-generator**: note it, proceed with Datadog only.
- **SLO not breached but incident ongoing**: report remaining error budget and burn rate so the team can decide.
- **Multiple dependencies failing**: list all, prioritise the one with the highest error count.
- **No Datadog SLO results with `service:<name>`**: retry once with `<name>` only (no prefix).
- **Service not found in uj_mapping.md**: note it explicitly — the service may not be part of any instrumented user journey yet.
- **No post-mortems found with service name**: retry with known aliases or short names for the service.
- **No active incident found**: still run Atlassian MCP historical search over `lastmodified >= startOfDay("-90d")` for all impacted UJ products/services and include the dedicated 3-month section.
- **Post-mortem page requires authentication**: note the Confluence URL and let the user open it manually.
- **Knowledge graph returns no products for a region**: report the impacted components and note that no products are directly linked in the registry; cross-reference component names against `uj_mapping.md` manually.
- **Region variant unknown**: try all `europe-west1/2/3/4` in parallel, aggregate non-empty results.

---

## Health Report Format (Mode C only)

```markdown
## Health Report — `<service>`

### Status: ✅ Healthy / ⚠️ Degraded / 🔴 Down

| SLO Name     | Target | Current | Error Budget 7d | Error Budget 30d |
| ------------ | ------ | ------- | --------------- | ---------------- |
| `<slo_name>` | XX.X%  | XX.X%   | XX% remaining   | XX% remaining    |

### User Journeys potentially affected

| User Journey | War Room Slack     | Criticality              |
| ------------ | ------------------ | ------------------------ |
| `<uj-key>`   | `#<slack-channel>` | critical / high / medium |

### Active incidents

_None_ — or list from Datadog

### Search Execution Status (mandatory)

| Query                 | Status                                            | Values Found                     |
| --------------------- | ------------------------------------------------- | -------------------------------- |
| A (SLO YAML)          | `success_with_data` / `success_no_data` / `error` | `<slo fields or no-data>`        |
| B (Datadog SLO)       | `success_with_data` / `success_no_data` / `error` | `<current, budgets>`             |
| C (Datadog incidents) | `success_with_data` / `success_no_data` / `error` | `<incident ids/states or none>`  |
| D (Logs patterns)     | `success_with_data` / `success_no_data` / `error` | `<dominant error/count or none>` |

### Recent errors (2h)

_None_ — or dominant error pattern + volume
```

## References

- [UJ Blast Radius Index](./references/uj_mapping.md)
