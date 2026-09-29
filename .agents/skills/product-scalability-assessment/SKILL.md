---
name: product-scalability-assessment
description: >
  Produce an evidence-based scalability-readiness / tech-debt assessment for an existing
  (brownfield) Decathlon product before it is promoted or scaled to more regions/countries.
  Use this whenever the user asks whether a named Decathlon product is ready to scale / be
  promoted to new regions or countries, wants a tech-debt, architecture, or readiness
  assessment of an existing product, or wants a product's risks / version currency /
  reliability posture characterised. Chains the AppReferential knowledge graph, Decathlon
  Tech Radar, endoflife.date, DeliveryMetrics (reliability/DORA/SonarQube/QuAPI),
  infrastructure mapping, contribution-concentration (Gini/bus-factor) and the SIG maturity
  matrix into a single Now/Next/Later report with linked annexes. Triggers on phrasings like
  "scalability assessment", "readiness assessment", "can we scale <product>", "is <product>
  ready to scale", "tech debt report", "architecture assessment", "assess <product> before
  we roll it out to more countries/regions".
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  audience: all
  domain: architecture
  mcp_required: false
---

# Product Scalability & Tech-Debt Assessment

## Overview

You produce a **scalability-readiness assessment** for a named Decathlon product: *can it be
safely promoted / scaled to more regions or countries, and what must happen first?* Every
figure MUST trace to an authoritative source — never estimate or fabricate asset data,
versions, metrics, or ownership. The output is a two-part document: a tight **summary**
(verdict + scorecard + Now/Next/Later) that links to **annexes** holding the detailed
evidence per axis.

This skill is a **read-only analysis** — it does not change code or infrastructure.

## When to Use

- The user asks whether a product is ready to scale / be promoted to new regions or countries.
- The user asks for a tech-debt, architecture, or readiness assessment of an existing (brownfield) Decathlon product.
- The user names a Decathlon product and wants its risks/currency/reliability posture characterised.

## Required skills & data sources

Invoke these in the flow below (never fabricate their output):

| Axis | Skill / source |
|------|----------------|
| Asset map, ownership, infra, SLOs | `knowledge-graph-query` (AppReferential) |
| Technology compliance | `decathlon-tech-radar` (ADOPT/TRIAL/ASSESS/HOLD) |
| Runtime/framework currency | `endoflife.date` public API (`https://endoflife.date/api/v1/products/<slug>`) |
| API exposure (provided/consumed) | `decathlon-api-discovery` (DocAPI) + QuAPI catalog; cross-check KG `apis_provided/consumed/apim_applications` |
| Reliability, DORA, SonarQube, QuAPI, SIG maturity | `delivery-metrics` |
| SIG maturity matrix (6 domains) + `tech_debt.md` contract | `decathlon-tech-compliance` |
| Reliability remediation (SLO design) | `slo-generator` (recommend, don't run, unless asked) |
| Contribution concentration | **User-supplied** Gini / bus-factor extraction (`stats team gini` + `stats team knowledge`) — NOT available in AppReferential/DeliveryMetrics; must be provided by the user (see Step 7) |

## Method — run in order

### Step 0 — Resolve the product
If unsure of the exact name/casing, resolve it first: `knowledge-graph-query` with
`--where "name:contains:<text>" --fields name,tiering`. Confirm the product before proceeding.

### Step 1 — Map the asset (KG)
`asset(name: <product>)` → capture: `tiering`, `businessScore`, `orgRefs` (unit/domain/subdomain/teamOwner),
`lifecycle`, `description`, `components{name type}`, `links`, and the `metadata.datadog.slos`/`monitors`
block if present. Then fetch each component's detail (stack, links/repo, `deployments`,
`relationships`, and `metadata`: `apis_provided`, `apis_consumed`, `apim_applications`,
`observability`, `technical.scalingPolicy`, `sources` for QuAPI/SonarQube keys).
**Flag immediately:** `tiering: null` or `businessScore: 0` (ungoverned criticality).

### Step 2 — Tech Radar compliance
For every language/framework/build tool found, call `decathlon-tech-radar`. Classify each as
ADOPT / ADOPT-with-exceptions / TRIAL / ASSESS / HOLD. **HOLD is a red flag** — see the Tech
Radar gate in the Principles. Present the classification as a visible table.

### Step 3 — Runtime & framework currency (endoflife.date)
Read the **exact** versions from the repos (composer.json, package.json/.nvmrc, MODULE.bazel/pom,
Dockerfile/app.yaml/OCI base image tag), then check each against endoflife.date. Report per
tech: in-use version, EOL/support status **relative to today's date**, latest patch, and whether
it is behind (past-EOL) OR ahead (running a non-LTS about to EOL). Both directions are risks.

### Step 4 — API exposure
Determine what the product **provides** and **consumes**, and whether it is gateway-governed
(APIM/Gravitee). Cross-check the KG fields against the QuAPI/DocAPI catalog via
`decathlon-api-discovery` — **the KG relationship fields are frequently under-populated**, so
treat an empty `apis_consumed`/`apis_provided` as "verify in QuAPI", not as truth. Assess real
**exposure risk**: no external consumers + internal-only scope ⇒ LOW (a missing APIM entry is
then a governance/data-quality item, not a scaling blocker). External consumers or public
exposure ⇒ require rate-limiting/quota/gateway controls before multi-region load.

### Step 5 — Delivery metrics & reliability
Find the DeliveryMetrics application (`/applications?name_search=` or `?support_group=`), then
pull `/benchmarks` (6-month window) and `/metrics/latest`. Extract:
- **Benchmark themes** and levels — ACCELERATE, ARCHITECTURE, CODE, DATA_EXCHANGE, OPERATION,
  SECURITY, and crucially **RELIABILITY / APP_PERFORMANCE / GREEN**. **If a theme returns no
  data, say so explicitly** — a missing RELIABILITY score on a business-facing app is a
  first-order scaling blocker.
- **SIG maturity** (delivery/dev/infra/operation/quality/security, 1–5) + scan dates (flag stale).
- **QuAPI** quality gate %.
- **SonarQube** per repo: coverage, bugs, code_smells, duplication, vulnerabilities, hotspots.

### Step 6 — Infrastructure & regional footprint
From KG `relationships` (`deploysTo` clusters, `uses` infra-assets) and
`assets(metadataFilter:{deployment:{namespace:...}})`, determine whether infra is **mapped** and
whether the product is **single- or multi-region**. Empty `deployments[]` + 0 namespace assets ⇒
infra unmapped (scaling blocker: you cannot capacity-plan an invisible topology). Note data
residency implications for distant regions.

### Step 7 — Contribution concentration (truck factor / Gini)
**The Gini index / bus-factor is NOT available in AppReferential or DeliveryMetrics — the skill
cannot retrieve it automatically. It MUST be supplied by the user** (e.g. an attached extraction
or report), or generated out-of-band with the `stats team gini` + `stats team knowledge` CLI and
then handed to the skill.

Handling:
1. **Explicitly ask the user** for a Gini/bus-factor extraction for the owning team(s) at the
   start of this step (or note that they attached one).
2. If provided, summarise: per-team **Gini** (commit-share inequality, 0 = equal → 1 = one owner)
   and per-repo **bus/truck factor** (min contributors owning >80% of files). Highlight the
   **strategic** component's key-person risk and any bus-factor-1 repos.
3. If **not** provided, mark the "Organizational readiness (truck factor)" scorecard row as
   **⚪ not measured (input required)**, state plainly that AppReferential/DeliveryMetrics do not
   expose this metric, and recommend the user run `stats team gini` / `stats team knowledge`
   scoped to the owning team and re-supply it. **Never invent Gini or bus-factor numbers.**

### Step 8 — SIG maturity / code compliance
Invoke `decathlon-tech-compliance`. Use the aggregate SIG maturity scores from Step 5 as the
domain proxy, and — when the scaling decision needs it — do a targeted per-requirement audit of
the highest-value domains (Security L1–3 baseline, Infrastructure, Testing) against the actual
repo contents. Be explicit about which was done (aggregate proxy vs line-by-line audit).

### Step 9 — Synthesise verdict, horizons, and report
Produce the report (structure below). Assign every finding to a **Now / Next / Later** horizon
with a **Gartner TIME** disposition. Every **Tech Radar HOLD carries a negotiated 0→X-month
exit deadline** — never "Later", never open-ended.

## Report structure (output contract)

Write two linked parts in one Markdown file under the project's planning-artifacts folder
(e.g. `_specs/planning-artifacts/<product>-scalability-readiness.md`):

**Part 1 — Summary (one screen, no redundancy)**
- Header: author, date, question, evidence sources, "every figure traces to a source".
- **Verdict** — 🔴 not ready / 🟠 conditional / 🟢 ready, one paragraph.
- **Scalability scorecard** — one row per axis (Reliability/SLO, Criticality governance,
  Infrastructure, Organizational readiness/truck factor, Architecture, Data/multi-region,
  API exposure, Delivery throughput, Runtime currency, Observability, Security), each 🔴/🟠/🟢
  and **linked to its annex**.
- **The 3 things that matter most** — each linking to its annex.
- **Remediation horizons** — 🟥 NOW (0–3 mo, incl. negotiated HOLD exit) / 🟧 NEXT (3–9 mo) /
  🟨 LATER (9+ mo).
- **Path to scale** — gated phases (Measurable → Safe to grow → Regional → Throughput).

**Part 2 — Annexes** (self-contained, one per axis): A Asset map · B Reliability & SLO ·
C Infrastructure · D Tech Radar & runtime currency · E API exposure · F Delivery metrics ·
G Truck factor & Gini · H Full remediation tables (Now/Next/Later with TIME dispositions).
Optionally an **Annex Z — comparison** vs another product.

Use in-document anchor links from the summary to each annex so the reader drills only where needed.

## Hard rules

1. **Never fabricate** asset data, versions, metrics, SLOs, or ownership — cite the source for every figure; if a source returns nothing, say so.
2. **Tech Radar HOLD is a conversational gate**: present the full ADOPT/TRIAL/ASSESS/HOLD table to the user; HOLD gets a negotiated 0→X-month exit deadline; require explicit user response on TRIAL/ASSESS.
3. **A missing RELIABILITY score / missing tier / missing SLO on a business-facing app is a first-order scaling blocker** — call it out prominently, and route remediation to `slo-generator` + SRE onboarding.
4. **Treat empty KG relationship fields as "verify in QuAPI/DocAPI", not as truth** — the graph is frequently under-populated for API and deployment edges.
5. **The Gini / bus-factor (truck factor) is not auto-retrievable** — it is not in AppReferential or DeliveryMetrics. Ask the user to supply it; if absent, mark the axis "not measured (input required)" and never invent the numbers.
6. **Cover all axes** even when an axis is clean or unmeasured (write "not measured" / "no gaps found" rather than omitting it).
7. **Respond in the project's `communication_language`; write documents in `document_output_language`.**
8. Keep the summary tight; push detail to annexes; link between them.
