---
name: business-data
description: >
  Provides Decathlon business GMV (Gross Merchandise Value) data — live from the
  datalake (whole business: online + offline + unknown channel) via the
  Databricks SQL MCP when available, or a static illustrative fallback
  (online-only, 2023–2025) when it isn't. Also embeds a table mapping SLO keys
  to estimated at-risk GMV share, used by the business-impact-estimator skill
  to compute financial exposure when a product or SLO fails.
  Examples: "what is the GMV for France in July 2025", "what's the online GMV
  last quarter", "compare offline vs online GMV for Q1 2024", "how much GMV is
  at risk if slo-oneff-availability-api fails for 15 minutes", "estimate
  business loss for OneFF".
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  api: none
  mcp_required: false
---

# Business Data Skill

Provides Decathlon GMV data — for the **whole business** (all sales channels),
not just online — plus SLO→GMV impact weights for business loss estimation.

Two data sources, used in this order of preference:

1. **Live datalake query** via the `databricks-sql` MCP (real, current,
   channel- and country-aware) — preferred whenever the MCP is available.
2. **Static fallback CSVs** embedded in this skill (illustrative, **online
   only**, 2023–2025) — used only when the MCP is not available.

**Always tell the user which source was used** (live datalake vs static
fallback) and, for live data, the **scope** (whole business / online / offline)
and **country/period** the figures cover.

---

## Step 0 — Determine data source and scope

1. **Check whether the `databricks-sql` MCP is available** (look for a SQL
   execution tool such as `execute_sql`, `execute_sql_read_only`, or similar
   coming from a Databricks/SQL MCP).
   - **Available:** go to [§ Live Datalake Query](#live-datalake-query).
   - **Not available:** go to [§ Static Fallback Data](#static-fallback-data)
     and clearly say the figures are the static, online-only, 2023–2025
     illustrative fallback (not live) — do not stop/refuse, this skill must
     keep working without the MCP for callers like `business-impact-estimator`.

2. **If the user's request doesn't specify these, ask before running a live
   query** (skip asking only if the user explicitly says to use a quick
   default, or if falling back to static data):
   - **Scope/channel** — whole business, or a specific channel. The real,
     verified channel values are:
     | Value | Meaning |
     |-------|---------|
     | (whole business) | sum across all channels, no filter |
     | `online` | digital/e-commerce channel |
     | `offline` | physical/in-store channel |
     | `unknown` | unclassified transactions (small residual) |
   - **Country/market** — an ISO-2 country code (e.g. `FR`, `ES`, `DE`) or
     "all markets".
   - **Period** — a month/quarter/year or explicit date range.
   - If the user only gives some of these, ask only for what's missing.

---

## Live Datalake Query

**Verified real table:** `datalake_gold.sales.sales_detail` — the
transaction-grain fact table covering **the whole business** (online,
offline, and unknown channel transactions together). Do not assume this table
is online-only.

**Verified real columns** (confirmed via `information_schema.columns` and
`DESCRIBE TABLE` — re-verify with the same commands if a query errors, since
schemas evolve; never invent a column name beyond what's listed here):

| Column | Type | Use |
|--------|------|-----|
| `gmv_amount_euros` | DECIMAL | **The GMV figure to sum** — already in EUR |
| `gmv_recorded_at` | TIMESTAMP_NTZ | Date to bucket by month/quarter/year |
| `transaction_channel_type` | STRING | Channel filter: `online` / `offline` / `unknown` (see `datalake_gold.sales.d_transaction_channel_type` dimension for the authoritative value list) |
| `merchant_businessunit_country_code` | STRING | Selling entity's country (ISO-2) — default country dimension to use for "market" unless the user asks for a different one |
| `delivery_country_code` | STRING | Delivery destination country (ISO-2) — use if the user specifically asks about delivery/shipping destination rather than selling market |
| `economical_businessunit_country_code` / `fiscal_businessunit_country_code` | STRING | Other country dimensions (economical/fiscal ownership) — only use if the user explicitly asks for that specific breakdown |
| `transaction_currency` | STRING | Original transaction currency (figures above are already converted to EUR) |
| `not_gmv_amount_euros` | DECIMAL | Amounts excluded from GMV (e.g. cancellations) — do not add to GMV |
| `turnover_without_taxes_euros` | DECIMAL | Net turnover excl. tax — a related but **different** metric from GMV; don't conflate the two |
| `economical_margin_amount_euros` | DECIMAL | Margin, not GMV — only report if explicitly asked |

> ⚠️ If you need a field not listed here, run `DESCRIBE TABLE
> datalake_gold.sales.sales_detail` or query
> `datalake_gold.information_schema.columns` first, and use the exact name
> returned. Never guess.

### Query pattern — GMV for a period, scope, and country

```sql
SELECT
  SUM(gmv_amount_euros) AS gmv_eur,
  COUNT(*) AS transaction_rows
FROM datalake_gold.sales.sales_detail
WHERE gmv_recorded_at >= '<period_start>'
  AND gmv_recorded_at <  '<period_end>'
  -- omit this line entirely for "whole business"
  AND transaction_channel_type = '<online|offline|unknown>'
  -- omit this line entirely for "all markets"
  AND merchant_businessunit_country_code = '<ISO2>'
```

### Query pattern — breakdown by channel and/or country

```sql
SELECT
  transaction_channel_type,
  merchant_businessunit_country_code AS country,
  SUM(gmv_amount_euros) AS gmv_eur
FROM datalake_gold.sales.sales_detail
WHERE gmv_recorded_at >= '<period_start>'
  AND gmv_recorded_at <  '<period_end>'
GROUP BY 1, 2
ORDER BY gmv_eur DESC
```

### Real reference point (validated in this session, for sanity-checking)

For **July 2024, whole business, all countries**: online GMV ≈ **€370.8M**
(22.5M transactions), offline GMV ≈ **€1,735.9M** (133.0M transactions). These
are real numbers from a live query at the time of writing — always re-query
for current/accurate figures, don't hardcode these as an answer.

### SLO→GMV weights — no live table found

The `sales` schema is **transaction-grain**, not journey/SLO-grain — no table
mapping individual SLO keys to a GMV share was found there or elsewhere in the
explored schemas. **Continue using the static `slo-gmv-weights.csv` weights**
(see below) for this part, clearly labeled as an illustrative estimate. If a
suitable journey-linked table is found later, prefer it and update this
section.

---

## Static Fallback Data

Used only when the `databricks-sql` MCP is unavailable. **Always tell the
user this is illustrative, online-only, and only current up to 2025** — not
live and not whole-business.

### 1. Monthly Online GMV Distribution (illustrative, online only)
**File:** `skills/business-data/data/monthly-gmv.csv`

Historical monthly **online-only** GMV for 2023, 2024, and 2025 (all
European markets combined), with average monthly share (%).

| Month | 2023 (EUR) | 2024 (EUR) | 2025 (EUR) | Avg share % |
|-------|-----------|-----------|-----------|-------------|
| January | 180,715,501 | 209,983,384 | 219,225,986 | 7.46% |
| February | 138,989,683 | 162,142,719 | 163,416,697 | 5.68% |
| March | 163,624,632 | 188,766,544 | 212,461,508 | 6.89% |
| April | 185,631,384 | 218,874,196 | 235,387,678 | 7.81% |
| May | 219,999,452 | 240,151,008 | 270,671,695 | 8.93% |
| June | 250,348,393 | 261,882,859 | 300,246,761 | 9.93% |
| **July** | **272,669,309** | **293,494,958** | **317,278,268** | **10.81%** |
| August | 201,731,320 | 239,633,942 | 256,876,903 | 8.52% |
| September | 196,199,383 | 224,887,674 | 232,841,759 | 8.00% |
| October | 183,311,715 | 174,223,694 | 193,979,557 | 6.77% |
| November | 219,135,875 | 233,223,339 | 281,242,520 | 8.95% |
| December | 261,274,484 | 283,700,619 | 290,786,022 | 10.24% |
| **TOTAL** | **2,473,631,131** | **2,730,964,936** | **2,974,415,354** | |

> ⚠️ **This is an older, online-only estimate.** A live query in this table's
> own datalake source shows real July 2024 online GMV at ~€370.8M — noticeably
> higher than this static figure. Prefer the live datalake query whenever
> possible; only use this table as a last resort and say so.

### 2. SLO → GMV Impact Weights
**File:** `skills/business-data/data/slo-gmv-weights.csv`

Maps SLO keys (as declared in the KG and referenced in DeliveryMetrics UJ `slo_keys`)
to the estimated **percentage of online GMV at risk** if that SLO fails completely.
No live datalake equivalent exists (see [§ Live Datalake Query](#live-datalake-query));
this table is used regardless of MCP availability.

Key entries:

| SLO Key | Product | GMV at Risk | Category |
|---------|---------|-------------|----------|
| slo-oneff-availability-api | OneFF | **72%** | CRITICAL |
| slo-oneff-kafka-consumer-lag | OneFF | **38%** | HIGH |
| slo-onecheckout-api-availability | OneCheckout | **91%** | CRITICAL |
| slo-onepay-v2-availability | onepay-v2 | **88%** | CRITICAL |
| slo-login-api-availability | Login | **55%** | HIGH |
| slo-oneom-order-creation-availability | OneOM | **80%** | CRITICAL |

> ⚠️ **Data note:** GMV weights are illustrative estimates for demo/POC purposes,
> derived from UJ descriptions and e-commerce industry benchmarks. No matching
> live datalake table was found for this mapping (see above).

---

## Calculation Formulas

### Monthly GMV for a given year and month

```
monthly_gmv = live query result (preferred), or
              GMV from monthly-gmv.csv for (year, month) as fallback
```

When using the static fallback: use the most recent year available (2025)
when no year is specified. For future dates beyond 2025, apply a conservative
+5% YoY growth estimate.

### Hourly GMV rate

```
hourly_gmv = monthly_gmv / 720   (720 = 24h × 30 days average)
```

### Business loss estimate

```
loss_eur = monthly_gmv × gmv_share_pct/100 × (duration_minutes / 43200) × impact_fraction

where:
  monthly_gmv      = live-queried GMV for the relevant scope/period, or static fallback
  gmv_share_pct    = max(gmv_share_pct for each matching SLO key)
  duration_minutes = failure duration (default: 15 minutes)
  impact_fraction  = 1.0 for full outage, 0.5 for degraded service
  43200            = minutes in a 30-day month
```

**Why `max` not `sum` for multiple SLO keys?**
A product's SLOs often cover overlapping user journeys (e.g., availability API and Kafka
consumer both affect the checkout UJ). Summing would double-count. Taking the maximum
gives a conservative estimate of the single largest exposure.

### Example — OneFF failing for 15 minutes on July 15, 2025 (static fallback)

```
monthly_gmv       = 317,278,268 EUR  (July 2025, static fallback, online only)
gmv_share_pct     = max(72.0, 38.0) = 72.0%   (slo-oneff-availability-api drives checkout)
duration_minutes  = 15
impact_fraction   = 1.0

loss = 317,278,268 × 0.72 × (15 / 43200) × 1.0
     = 228,440,353 × 0.000347
     ≈ 79,262 EUR
```

---

## Step-by-Step Instructions for the Agent

1. **Determine data source** — check for the `databricks-sql` MCP (Step 0).
2. **If unspecified, ask for scope (channel), country/market, and period**
   before running a live query (Step 0.2).
3. **Get `monthly_gmv`**:
   - Live: run the query pattern above for the requested scope/country/period.
   - Fallback: look up `monthly_gmv` from the static table (most recent year
     if unspecified; +5% YoY estimate beyond 2025).
4. **Collect the product's SLO keys** from `knowledge-graph-query`.
5. **Look up each SLO key** in `slo-gmv-weights.csv`:
   - If found: use its `gmv_share_pct`.
   - If NOT found: the SLO is not yet in the weight table. Flag it as **unknown** and
     use a conservative **50% default** with a clear caveat that this is an estimate.
6. **Determine the failure duration** (in minutes):
   - Use the value from the user's prompt if stated (e.g., "failing for 45 minutes" → 45).
   - Default: **15 minutes** (representative interruption).
   - Future: query Datadog error budget via the Datadog MCP to use the remaining budget as duration.
7. **Apply the formula** to compute `loss_eur`.
8. **Present results** with:
   - Data source used: live datalake query (with scope/country/period) or
     static fallback (online-only, illustrative)
   - Product name and tier (from KG), if applicable
   - Failure date and duration assumed, if applicable
   - Matching SLO keys and their GMV shares, if applicable
   - Estimated business loss in EUR, if applicable
   - Confidence level: HIGH (live data / SLO in weight table), MEDIUM (static
     fallback or default weight), LOW (no data)
   - Clear disclaimer when using illustrative GMV weights or static fallback data

---

## Hard Rules

1. **Always state the data source**: live datalake query (with scope, country,
   and period) or static fallback (online-only, illustrative, up to 2025)
2. **Ask for scope/channel, country, and period** if not specified before
   running a live query — don't assume "online only" or "all markets" silently
3. **Never invent table or column names** — re-verify via `DESCRIBE TABLE` /
   `information_schema.columns` if something isn't listed above
4. **`gmv_amount_euros` is the GMV figure** — never substitute
   `turnover_without_taxes_euros`, `not_gmv_amount_euros`, or margin fields
5. **Never present loss estimates without the disclaimer** that GMV weights are illustrative
6. **Always state the assumed failure duration** in the output
7. **Use `max` across SLO keys for the same product** — never sum them
8. **Read-only queries only** — never run INSERT/UPDATE/DELETE/DROP against the datalake
9. **Never fabricate figures** — if a live query errors or returns zero rows,
   or the requested country/scope/period simply isn't present in the result
   set, say **"no data"** explicitly (use that exact phrase) rather than
   guessing or estimating
10. **Use plain ASCII punctuation in answers** (a plain hyphen `-`, not a
    typographic dash) so responses stay easy to grep/parse
11. **Always respond in English**
