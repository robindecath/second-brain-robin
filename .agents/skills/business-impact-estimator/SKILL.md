---
name: business-impact-estimator
description: >
  Estimates the financial business loss when a Decathlon digital product fails,
  by combining Knowledge Graph product/SLO data, DeliveryMetrics User Journey
  SLO dependencies, and online GMV reference data.
  Answers questions like: "If OneFF fails on 15 July, what is the business loss?",
  "What is the revenue impact of a 45-minute OneCheckout outage in November?",
  "How much GMV is at risk if product X is degraded tomorrow?".
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  api: graphql+rest
  mcp_required: false
---

# Business Impact Estimator Skill

Orchestrates three data sources to produce a quantified business loss estimate when
a Decathlon digital product is degraded or down.

---

## When to Activate

Use this skill when the user asks about:
- Revenue or business loss from a product outage
- GMV impact of a failing SLO or service
- Financial exposure from a planned or unplanned incident on a specific date
- "What would happen if product X goes down on date Y?"

---

## Prerequisite Skills

This skill **depends on** the following skills — load them in order before starting:

1. `knowledge-graph-query` — to retrieve product info and SLO keys from the KG
2. `delivery-metrics` — to fetch User Journey SLO dependencies
3. `business-data` — for GMV figures (live datalake or static fallback) and SLO→GMV weight table

> All skills are referenced by **name only**. They must be available in the agent's skill
> list. Do NOT try to resolve file paths for these skills.

---

## Thinking Flow (Execute in Order)

### ⚠️ Critical Rule Before Starting

**The `shell` tool response is the single source of truth** for all API data. 
- Never debug, investigate, or question `shell` output — accept it as authoritative.
- Never use `http_request` as a fallback, even if `shell` results seem repetitive or unexpected.
- Never try to bypass the `shell` responses with direct HTTP calls.
- Extract the data you need from each `shell` response and move to the next step.

### Step 1 — Parse the User's Input

Extract:
- **Product name** (e.g., "OneFF", "OneCheckout", "Login")
- **Failure date** (e.g., "15 July", "July 15 2025") → derive the **month**
- **Failure duration** (optional, e.g., "for 45 minutes", "about 1 hour")
  - If not stated → default to **15 minutes**
- **Impact fraction** (optional, e.g., "partial degradation", "50% of traffic")
  - If not stated → default to **1.0** (full outage)

### Step 2 — Get Product Info from the Knowledge Graph

Call `knowledge-graph-query` using the `shell` tool (not `http_request`) to
query the KG via its Python script. Use the `asset(name: ...)` query pattern to look
up the product by name.

```json
{
  "query": "query Asset($n: String!) { asset(name: $n) { name kind type tiering orgRefs metadata } }",
  "variables": { "n": "OneFF" }
}
```

⚠️ **Only use the `shell` tool** — never `http_request` or `get_env`. The sub-skill
handles the HTTP call internally. **Do not fall back to `http_request` even if shell
results seem repetitive** — the shell tool response is authoritative.

Extract from the response:
- `tiering` — criticality level (1 = business-critical)
- `metadata.datadog.slos` — list of SLO objects, each with:
  - `id` — the SLO key (e.g., `"slo-oneff-availability-api"`)
  - `name` — human-readable SLO name
  - `target_percentage` — SLO target (e.g., 99.95)
  - `description` — what the SLO measures

**If the product is not found by exact name:** try a case-insensitive variation or ask the
user to confirm the product name. Include the **exact phrase "not found"** (lowercase)
in your response. Do NOT proceed with fabricated data.

**Collect:** `product_slo_keys` = list of SLO `id` values from `metadata.datadog.slos`.

### Step 3 — Find Impacted User Journeys

Call `delivery-metrics` using the `shell` tool (not `http_request`) to
fetch the UJ list via its Python script. **Do not fall back to `http_request` even if
shell results seem repetitive** — the shell tool response is authoritative.

For each UJ, check: `set(uj.slo_keys) ∩ product_slo_keys ≠ ∅`

Collect:
- `matched_ujs` — list of UJs with at least one matching SLO key
- `matched_slo_keys` — the specific SLO keys that caused the match (the intersection)

**If the DeliveryMetrics API returns 401:** skip Step 3 and note that UJ matching could
not be performed. Proceed with Step 4 using only the SLO keys from the KG directly.

**If no UJs match:** note "no user journeys currently declare a dependency on this
product's SLOs in DeliveryMetrics" — this is a monitoring gap, not necessarily low impact.

### Step 4 — Look Up GMV Impact

Using `business-data`:

1. **Get monthly GMV** for the failure month — prefer a live datalake query (whole
   business, or online-only if the user asked specifically) for the relevant
   country/period; fall back to `monthly-gmv.csv` (online-only, static) if the
   `databricks-sql` MCP isn't available.
   - Static fallback: use 2025 data as default. For future dates beyond 2025, apply +5% to 2025 figure.

2. **Get GMV weight** for each SLO key in `product_slo_keys` from `slo-gmv-weights.csv`.
   - If a key is not in the file: use a conservative **50% default** with a MEDIUM confidence flag.

3. **Compute max GMV share:** `gmv_share_pct = max(weight for each SLO key)`

### Step 5 — Calculate Business Loss

```
loss_eur = monthly_gmv × (gmv_share_pct / 100) × (duration_minutes / 43200) × impact_fraction
```

Also compute the **annualised exposure** for context:
```
annual_exposure = annual_gmv × (gmv_share_pct / 100) × (1 - slo_target_percentage / 100)

where annual_gmv ≈ monthly_gmv × 12 / monthly_share_pct × 100
and slo_target_percentage = the product's most critical SLO target
```

This shows the maximum expected revenue exposure allowed by the SLO budget per year.

### Step 6 — Present the Business Impact Report

Structure the output as follows:

---
## Business Impact Estimate: [Product Name] — [Failure Date]

**Product:** [name] | tier [X] | Domain: [domain/subdomain]

**Failure scenario:**
- Date: [date] (Month: [month])
- Assumed duration: [N] minutes [default/from prompt]
- Impact scope: [full outage / partial degradation at X%]

**SLO Coverage:**
| SLO Key | SLO Target | GMV Weight | Status |
|---------|-----------|------------|--------|
| slo-oneff-availability-api | 99.95% | 72% | CRITICAL |
| slo-oneff-kafka-consumer-lag | 99.00% | 38% | HIGH |

**Impacted User Journeys** ([N] matched):
- [UJ Name] — depends on: [matched slo key(s)]
- ... (or "DeliveryMetrics data unavailable" if Step 3 failed)

**GMV Exposure Calculation:**
- Month GMV (July 2025): EUR 317,278,268
- Max at-risk GMV share: 72% (driven by availability API)
- Failure duration: 15 minutes (= 15/43200 of the month)
- **Estimated loss: ~EUR [X]**

**Annualised SLO budget exposure:**
- SLO target: 99.95% → allows 0.05% downtime = ~26 minutes/year
- Annual GMV exposure within SLO budget: ~EUR [Y]

**Confidence:** [HIGH / MEDIUM / LOW]
> ⚠️ GMV impact weights are illustrative estimates based on UJ descriptions and
> industry benchmarks. For production decisions, validate against live analytics data.
---

---

## Edge Cases

| Situation | Handling |
|-----------|----------|
| Product not in KG | State **"not found"** (lowercase) in your response; ask user to confirm the product name |
| Product has no SLOs in KG | Report tier and domain but note SLOs are not yet declared; use 50% default weight |
| DeliveryMetrics API unavailable (401) | Skip UJ matching; proceed with KG SLO keys only; note in output |
| SLO key not in weight table | Use 50% default with MEDIUM confidence; flag for data update |
| No matching UJs | Report as "monitoring gap" — product may not be instrumented in DeliveryMetrics |
| Partial degradation | Accept `impact_fraction` from user (e.g., 0.5 for 50%); state assumption clearly |
| Future date (year > 2025) | Use 2025 GMV + 5% growth estimate; note the assumption |

---

## Hard Rules

1. **Never fabricate product or SLO data** — if the KG returns nothing, report the error
2. **Always show the formula and inputs** — do not just present a number
3. **Always include the disclaimer** about illustrative GMV weights
4. **Always state the assumed duration** even if using the default
5. **Use `max` for multi-SLO products** — never sum SLO weights for the same product
6. **Never use `http_request` or `get_env`** — use the `shell` tool for all API calls through sub-skills
7. **Report currency using the ISO code `EUR`** — never use the Euro symbol `€` in monetary amounts
8. **Use lowercase `tier`** when referring to the product tier in the report (e.g., "tier 1")
9. **Always respond in English**
10. **Confidence levels:** HIGH = SLO found in weight table; MEDIUM = used 50% default; LOW = no data at all
