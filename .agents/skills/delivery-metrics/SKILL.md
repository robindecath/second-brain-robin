---
name: delivery-metrics
description: >
  Query the Decathlon DeliveryMetrics API across all resource families:
  User Journeys (UJ) and their Moments, Applications, per-application
  Metrics and Benchmarks, cross-application Metrics, and infrastructure Assets.
  Use this skill to answer questions like:
  "list user journeys for domain ECOM", "which UJs depend on slo-oneff-availability-api",
  "get the benchmark for app X on 2024-06-01", "list metrics for application Y",
  "what assets does component Z have", "strategic benchmark for all apps".
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  api: rest
  mcp_required: false
---

# Delivery Metrics Skill

Query the DeliveryMetrics API for User Journeys, Applications, Metrics,
Benchmarks, and Assets.

All HTTP calls use the `DecathlonApi` tool provided by the `decathlon-api-tool` skill.

**Base URL:** `https://api.decathlon.net/deliverymetrics`

The default client ID (`C74d77aa9f495d86eb6480494a5cd4a705ec6f346`) works
for all endpoints below — no override needed.

---

## Quick Intent Routing

| What the user asks about | Jump to |
|---|---|
| User journeys, UJ list, SLO key → UJ mapping, UJ impact of a product | [§ User Journeys](#user-journeys) |
| Application list, find app by name/team, app details | [§ Applications — List](#applications--list) |
| Metrics for an app, scores, benchmark for app X, metric records/timeline | [§ Applications — Metrics & Benchmarks](#applications--metrics--benchmarks) |
| Bulk metrics across multiple apps | [§ Cross-App Metrics](#cross-app-metrics) |
| Strategic benchmark (all apps) | [§ Strategic Benchmark](#strategic-benchmark) |
| Infrastructure assets, component assets, cloud hosting, environment | [§ Assets](#assets) |

---

## Activation

1. Ensure the `decathlon-api-tool` skill is loaded (the `DecathlonApi` tool must be available)
2. Call `read_skill delivery-metrics` (this file) to load these instructions
3. Use the `DecathlonApi` tool for every API call below

---

## User Journeys

### List User Journeys (v2 — primary)

**Endpoint:** `GET /api/v2/user_journeys`

The main endpoint for all UJ queries. Returns an array of UJ objects with `slo_keys`.

**Query parameters (all optional):**

| Parameter | Type | Description |
|---|---|---|
| `with_moment_list` | boolean | Include the moments (steps) for each UJ. Required for `product_uuid_list` filtering. |
| `user_journey_uuid_list` | string[] | Filter to specific UJ UUIDs |
| `product_uuid_list` | string[] | Filter to UJs whose moments link to these product UUIDs. Only effective when `with_moment_list=true` |
| `name_search` | string | Fuzzy name search (4–100 alphanumeric chars, dashes, underscores, spaces, dots) |
| `name` | string | Exact UJ name match |
| `criticality` | integer 1–4 | Filter by criticality level |
| `domains` | string[] | Filter by domain (e.g. `ECOM`, `CSP`) |
| `page` | integer | Page number, default `0` |
| `size` | integer | Page size, default `20` |

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v2/user_journeys"`

**Response shape:**
```json
[
  {
    "uuid": "db0b4377-32f9-4d25-88e7-77f99075d563",
    "name": "CSP-UJ-2-MOM-3-user-associates-to-product-in-mobile-app",
    "description": "As a user, I associate my product to my Decathlon login account uuid",
    "slo_keys": [
      "slo-user-association-associate-device-api-availability",
      "slo-core-services-bff-associate-device-api-availability"
    ],
    "sequence": 2,
    "criticality": 2,
    "domains": ["CSP"],
    "component_uuids": [],
    "product_uuids": []
  }
]
```

Key fields:
- `uuid` — stable UJ identifier
- `slo_keys` — SLO IDs this UJ depends on; use for product→UJ impact mapping
- `criticality` — 1 (highest) to 4 (lowest)

### Match SLO Keys to User Journeys

Given a set of product SLO keys (e.g. from `knowledge-graph-query`), find all
UJs where `slo_keys` intersects:

```python
product_slo_keys = {"slo-oneff-availability-api", "slo-oneff-kafka-consumer-lag"}
matching_ujs = [uj for uj in all_ujs if set(uj["slo_keys"]) & product_slo_keys]
```

Report: number matched, UJ names, descriptions, and which specific `slo_keys` matched.

### Get Moments for a User Journey

**Endpoint:** `GET /api/v1/user_journeys/{user_journey_uuid}/moments`

Returns the ordered steps (moments) with their individual `slo_keys`.
Only call this when the user explicitly asks for moment/step details.

**Exact 2-step sequence — do not deviate:**

1. **Get UUID** — Call `GET /api/v2/user_journeys` to list all UJs. Find the requested UJ by name in the response and extract its `uuid`.
2. **Get moments** — Call `GET /api/v1/user_journeys/{uuid}/moments` with that UUID. Then immediately present the answer.

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/user_journeys/{uuid}/moments"`

---

## Applications — List

**Endpoint:** `GET /api/v1/applications`

**Query parameters (all optional):**

| Parameter | Type | Description |
|---|---|---|
| `name_search` | string | Fuzzy name search (4–100 chars) |
| `application_uuid_list` | string[] | Filter to specific application UUIDs |
| `support_group` | string | Filter by support group name (e.g. `CE-DELIVERY-METRICS`) |
| `with_profile_support_group` | boolean | Auto-filter to apps owned by the caller's profile |
| `with_source_list` | boolean | Include source list in response (hidden by default) |

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/applications"`

**Response:** array of `ApplicationDtoOut` — each with `uuid`, `name`, `support_group`, source metadata.

---

## Applications — Metrics & Benchmarks

All endpoints below require a valid `application_uuid`. Obtain one from
[§ Applications — List](#applications--list) first if you only have a name.

### Latest Metrics (preferred)

**Endpoint:** `GET /api/v1/applications/{application_uuid}/metrics/latest`

Returns the most recent metric value per metric. Use this unless a date range is needed.

**Query parameters (optional):**
- `metric_name_list` — filter to specific metric names
- `theme_list` — filter by theme(s); valid values:
  `ACCELERATE`, `APP_PERFORMANCE`, `ARCHITECTURE`, `CODE`, `DATA_EXCHANGE`,
  `GREEN`, `OPERATION`, `RELIABILITY`, `SECURITY`

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/applications/{uuid}/metrics/latest"`

### Metrics by Date Range

**Endpoint:** `GET /api/v1/applications/{application_uuid}/metrics`

Same filters as above plus:
- `begin_date` — ISO datetime, e.g. `2024-01-01T00:00:00Z`
- `end_date` — ISO datetime

### Metric Records (Timeline)

**Endpoint:** `GET /api/v1/applications/{application_uuid}/metrics/{metric_name}/records`

Returns metric values aggregated by month. Useful for trend charts.

**Required query parameters:**
- `from_date` — e.g. `2024-01-01`
- `to_date` — e.g. `2024-06-01`

### Measures for a Metric

**Endpoint:** `GET /api/v1/applications/{application_uuid}/metrics/{metric_name}/measures`

Returns the raw measures that fed into a metric computation.

**Required query parameters:**
- `source_name`
- `from_date`
- `to_date`

### Benchmark for Application

**Endpoint:** `GET /api/v1/applications/{application_uuid}/benchmarks`

The main benchmark endpoint — returns performance by theme. If `from_date ≠ to_date`,
includes a performance delta between the two dates.

**Required query parameters:**
- `from_date` — e.g. `2024-01-01`
- `to_date` — e.g. `2024-06-01`

**Optional:**
- `compare_mode` — `DEFAULT` | `FROM_DATE` | `TO_DATE`

**Response:** `BenchmarkDtoOut` — per-theme performance levels and delta.

### Benchmark Timelines

**Endpoint:** `GET /api/v1/applications/{application_uuid}/benchmarks/timelines`

Returns benchmark data over a time range. Granularity is automatic:
- ≤ 12 weeks → weekly data points
- \> 12 weeks → monthly data points

**Required query parameters:**
- `from_date`
- `to_date`

---

## Cross-App Metrics

**Endpoint:** `GET /api/v1/metrics`

Bulk metrics query across multiple applications in a single call.

**Query parameters:**

| Parameter | Required | Description |
|---|---|---|
| `application_uuid_list` | **yes** (1+) | List of application UUIDs to query |
| `theme_list` | no | Filter by theme(s) (same enum as above) |
| `metric_name_list` | no | Filter to specific metric names |
| `source_name_list` | no | Filter by data source |
| `begin_date` | no | ISO datetime |
| `end_date` | no | ISO datetime |
| `latest` | no | `true` (default) — only latest value per metric |
| `activated_only` | no | `true` (default) — exclude inactive metrics |
| `with_detail` | no | `true` (default) — include detailed metric metadata |

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/metrics"`

**Response:** array of `ApplicationMetricDtoOut` grouped by application.

---

## Strategic Benchmark

**Endpoint:** `GET /api/v1/benchmarks`

Returns yesterday's benchmark for **all** registered applications at once.
Uses a nightly cache — no date parameters needed or accepted.

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/benchmarks"`

Use this when the user asks for a global overview or comparison across all apps.

---

## Assets

### List Assets

**Endpoint:** `GET /api/v1/assets`

**Query parameters (all optional):**

| Parameter | Description |
|---|---|
| `component_uuid` | Filter to assets belonging to a specific component |
| `environment` | e.g. `production`, `staging` |
| `type` | Asset type (e.g. `KUBERNETES_DEPLOYMENT`, `DATABASE`) |
| `hosting_solution` | e.g. `GCP`, `AWS`, `ON_PREMISE` |
| `location` | Datacenter / region |
| `envelope` | Deployment envelope |
| `page` | Default `0` |
| `size` | Default `20` |

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/assets"`

### Get Asset by UUID

**Endpoint:** `GET /api/v1/assets/{asset_uuid}`

Returns full detail for a single asset.

**Invocation:**
- `method: GET`
- `url: "https://api.decathlon.net/deliverymetrics/api/v1/assets/{uuid}"`

---

## Error Handling

| HTTP status | Meaning | Action |
|---|---|---|
| `401` | No DM API access | Stop; report the error; do not fabricate data |
| `204` | No data for these filters | Report as "no results found"; do not retry with the same filters |
| `404` | UUID not found | Suggest listing the resource first to obtain valid UUIDs |
| `400` | Invalid request (bad filter value, name too short/long) | Surface the error message to the user |
| Pagination | Default: page=0, size=20 | If user asks for "all", iterate pages until an empty array is returned |

---

## Hard Rules

1. **Never fabricate data** — 0 results or an error → report exactly that
2. **Never use `http_request` tool** under any circumstances. All API calls must go through `shell` using the `DecathlonApi` script. If the `shell` tool does not return expected data, do not fall back to `http_request` — present what you have and stop.
3. **Base URL:** `https://api.decathlon.net/deliverymetrics` for all calls
4. **User Journeys:** always call v2 first; call `/moments/{uuid}` only if moment detail is explicitly requested
5. **Application metrics:** prefer `/metrics/latest` unless the user specifies a date range
6. **Benchmarks:** prefer per-application `/benchmarks` over `/benchmarks` (strategic) unless the user asks for all apps
7. **SLO key matching is case-sensitive** — match exactly as returned by the API
8. **Always respond in English**
9. **Maximum 2 `shell` calls total per query** — make at most 2 shell calls to answer any question. After 2 calls, immediately present your answer. Do not re-call the same endpoint, do not iterate, do not debug with `echo` or `env`. If the API does not return the expected data, present what you have and stop.
10. **Report UUIDs** — when referencing a specific resource in your answer, always include its UUID
