---
name: help-sre
description: >
  Interactive SRE reliability companion. Two modes: Greenfield (new product creation
  — BMAD discovery interview, PRD/architecture challenge, SLO definition, full
  observability design, toil automation, load tests, chaos experiments, SRE task list)
  and Brownfield (existing service reliability audit — maturity scoring across 9
  dimensions, gap analysis against SRE best practices, prioritised remediation backlog).
  Keywords: SRE, reliability, SLO, SLI, SLA, error budget, golden signals, logs,
  traces, APM, monitoring, alerting, toil, automation, chaos engineering, load test,
  BMAD, product onboarding, runbook, capacity planning, resilience, RTO, RPO,
  audit, maturity, brownfield, greenfield.
argument-hint: '<product-or-service-name>'
user-invocable: true
version: 1.1.0
license: MIT
metadata:
  audience: all
  domain: sre
  mcp_required: false
  mcp_tools_brownfield:
    - mcp_datadog_search_datadog_slos
    - mcp_datadog_search_datadog_monitors
---

# Help SRE — Reliability by Design

Two modes depending on the product's lifecycle stage. Always detect the mode first.

## When NOT to use

- **Active incident in progress** → use `incident-investigation` instead
- **Quick SLO status lookup** → use `slo-generator` + Datadog directly
- **Adding or modifying an existing SLO definition** → edit the YAML in `dktunited/slo-generator` directly
- **Checking if a product is healthy** → use `incident-investigation` Mode C (health check)

---

## Reference Data — Context Enrichment

```
.github/skills/incident-investigation/references/uj_mapping.md
```

**Brownfield mode:** Handled automatically in Intake B — silently look up the service and use any matching data to enrich the audit context. Non-blocking.

**Greenfield mode:** Skip for brand-new products. User Journeys are defined during Intake.

---

## Mode Detection *(BLOCKING — ask first)*

Ask first, adapt to user's language:

> 🇫🇷 "Est-ce qu'on travaille sur un **nouveau produit** (création from scratch) ou sur un **produit existant** dont tu veux auditer la maturité SRE ?"
> 🇬🇧 "Are we working on a **new product** (greenfield) or auditing an **existing service** for SRE maturity?"

- **New product / from scratch** → **Mode G — Greenfield** — do NOT call Datadog. User Journeys and SLOs do not exist yet.
- **Existing product / audit** → **Mode B — Brownfield** — immediately load Datadog context (see Intake B automatic data collection).

---

# Mode G — Greenfield

Interactive reliability onboarding for a new product. Conduct the BMAD discovery interview, review the PRD and architecture, define SLOs, design the full observability stack, automate toil, and validate resilience.

Always complete the Intake before Step 1. Never skip Step 3 (alignment) before proceeding to implementation.

---

## Intake G — BMAD Discovery Interview *(BLOCKING)*

> ⛔ **Do NOT proceed to Step G1 until mandatory questions are answered.** Questions marked *(optional)* can be skipped — apply the stated default and note the assumption in the Reliability Baseline Report.

Conduct the interview conversationally — one or two questions at a time. Acknowledge each answer before asking the next. Adapt follow-up questions based on answers received. If the user provides a PRD or `architecture.md`, extract answers from it silently before asking.

### G-A — Product context

1. What is the product or service name, and what problem does it solve for users?
2. Who are the end users — internal (Decathlon employees), B2C (customers), or B2B (partners)?
3. Is this a new creation or a migration / refactor of an existing service?
4. What is the expected launch date, and is there a BMAD PRD or architecture.md I should review?

### G-B — User Journeys and business criticality

5. Which user journeys does this product support? (e.g. "customer places an order", "store staff books a service") — list all you know, even informally.
6. Are any of these journeys revenue-critical or checkout-adjacent? (impacts SLO tier)
7. *(optional)* What is the expected volume at launch (requests/day, orders/day, concurrent users)? *(default: unknown — flag as TBD in the load test plan)*
8. *(optional)* What is the expected peak — Black Friday, sales events, store opening times? *(default: ×5 nominal — standard e-commerce estimate)*

### G-C — SLA commitments and reliability expectations

9. Have you made any SLA commitments to internal stakeholders, partners, or customers? (e.g. "99.9% availability", "< 2s response time")
10. What is the maximum acceptable downtime per month before it becomes a business problem?
11. *(optional)* Is there a defined **RTO** (Recovery Time Objective — max time to restore service after failure)? *(default: 30 min for Tier-1, 2h for Tier-2)*
12. *(optional)* Is there a defined **RPO** (Recovery Point Objective — max data loss window acceptable)? *(default: 1h for stateful services, N/A for stateless)*

### G-D — Architecture and dependencies

13. What are the upstream and downstream dependencies? (databases, APIs, Kafka topics, third-party services)
14. Is the service stateful (holds data) or stateless?
15. Where will it run — GKE, Cloud Run, on-premise, hybrid?
16. *(optional)* Are there any known single points of failure in the design? *(default: unknown — flag for G1B architecture review)*

### G-E — Operational context

17. Which team owns this service, and what is their Slack channel?
18. Is there an on-call rotation for this team? If not, who handles incidents?
19. *(optional)* What manual operational tasks do you anticipate (deployments, restarts, config changes)? *(default: standard deploy + config change — document in G5 toil inventory)*

---

## Step G1 — Assess Reliability and Challenge the PRD / Architecture

**Goal:** establish a reliability baseline and surface SRE concerns in the product design.

### G1A — Review existing signals (migration or refactor only)

> Skip for brand-new products. Only run if G-A.3 confirmed this is a **migration or refactor** of an existing service.

Query Datadog:
- `mcp_datadog_search_datadog_slos` → existing SLOs and current compliance
- `mcp_datadog_search_datadog_monitors` → active monitors and muted alerts

### G1B — Review PRD and architecture.md

If the user provided or referenced a PRD or architecture.md, read it and challenge it from a reliability perspective. Look for and flag:

| SRE concern | What to look for |
|-------------|-----------------|
| **Missing SLA / SLO** | Document mentions "reliable" or "available" without quantitative targets |
| **Single points of failure** | One DB, one region, no replica, no circuit breaker |
| **No degraded mode** | All-or-nothing design — no fallback if a dependency is down |
| **Undefined RTO/RPO** | Recovery objectives not specified for stateful components |
| **No capacity model** | Expected load stated but no autoscaling or load test plan |
| **Implicit retry storms** | Sync chains between services with no backoff / bulkhead |
| **No observability hooks** | No mention of structured logs, traces, or health endpoints |
| **Alert-less launch** | Go-live plan with no mention of alerting or on-call |
| **Missing data contract** | Kafka/event schema changes not versioned or backward-compatible |

For each concern found: quote the relevant section, state the risk, propose a concrete fix.

### G1C — Produce Reliability Baseline Report

- Current SLO targets (if any) and compliance %
- Estimated toil level (Low / Medium / High)
- UJs defined during Intake
- List of reliability gaps and PRD/architecture challenges flagged in G1B

---

## Step G2 — Define SLOs

**Goal:** translate SLA commitments into measurable SLIs with quantitative targets and error budgets.

> **SLA vs SLO**: SLA is a contractual commitment. SLO is the internal target — always **stricter** than the SLA. If SLA = 99.9%, set SLO = 99.95%.

For each User Journey (from Intake) that involves this service:

1. Identify the **SLI**:
   - **Availability** — `successful_requests / total_requests`
   - **Latency** — % of requests under threshold (p99, p95)
   - **Error rate** — `error_requests / total_requests`
   - **Freshness** (data pipelines) — data age < threshold
   - **Correctness** (data products) — % of outputs matching expected schema/values

2. Set a **quantitative target**:
   - Tier-1 / revenue-critical UJs → minimum 99.9% availability
   - Tier-2 / internal UJs → 99.5% availability
   - Batch / async → freshness SLO agreed with product team
   - Always set SLO **above** any stated SLA

3. **Calculate the error budget**:
   - Monthly budget = `(1 - target) × 30 × 24 × 60` minutes
   - Example: 99.9% → 43.8 min/month, 99.5% → 3.6 h/month

4. Output the **SLO Definition Table**:

| SLI | Measurement query | Target | Error budget (30d) | UJ | SLA if any |
|-----|-------------------|--------|--------------------|----|-----------|
| Availability | good_requests / total | 99.95% | 21.9 min | ecommerce-checkout | 99.9% |
| Latency p99 | requests < 500 ms | 99.5% | 3.6 h | product-catalog | — |

---

## Step G3 — Verify Alignment *(BLOCKING)*

> ⛔ **Do NOT proceed to Step G4 until the user explicitly confirms.**

Present the SLO Definition Table and ask (adapt to user's language):

> 🇫🇷 "Est-ce que ces cibles SLO reflètent les attentes de vos utilisateurs et la capacité de votre équipe à répondre aux violations ? Si le budget d'erreur est épuisé, êtes-vous prêts à geler le développement de fonctionnalités jusqu'à ce que la fiabilité soit restaurée ?"
> 🇬🇧 "Do these SLO targets reflect your users' expectations and your team's ability to respond to violations? If the error budget is exhausted, are you prepared to freeze feature development until reliability is restored?"

- Agreed → proceed to G4.
- Adjusted → update table and re-confirm.
- Unsure → explain: tighter SLOs = more pager load + automation investment. Recommend 99.5% baseline, tighten after one quarter of data.

---

## Step G4 — Design Observability

**Goal:** define the full observability stack — golden signals, structured logs, distributed traces, monitors, and alerting.

For each subsection, explain the recommendation and ask if any constraints apply (existing tooling, log volume budget, sampling limits).

### G4A — Golden Signals (Metrics)

| Signal | Metric pattern | Warn | Page |
|--------|---------------|------|------|
| **Latency** | `trace.web.request.duration` p99 | > 500 ms | > 1 s |
| **Traffic** | `trace.web.request.hits` | Drop > 50% vs 1w avg | Drop > 80% |
| **Errors** | `trace.web.request.errors / hits` | > 1% | > 5% |
| **Saturation** | CPU utilization | > 80% | > 95% |
| **Saturation** | Memory utilization | > 80% | > 95% |

Also instrument **business metrics** (orders/min, payment success rate) — early signals that infra metrics miss.

### G4B — Structured Logging

1. **Format** — JSON, never free text. Mandatory fields: `timestamp`, `level`, `service`, `trace_id`, `span_id`, `env`, `message` + context.
2. **Log levels** — `ERROR` wakes someone up; `WARN` degraded/no action; `INFO` normal business events; `DEBUG` disabled in prod, enabled on demand.
3. **What to log** — request/response boundaries, external call outcomes, state transitions, errors with full stack traces.
4. **What NOT to log** — PII (name, email, card number), credentials, secrets. Challenge any log line that could contain user data.
5. **Volume** — estimate at peak load. Flag if it exceeds Datadog budget; propose sampling for high-volume DEBUG paths.
6. **Correlation** — every log in a request chain must carry the same `trace_id`.

### G4C — Distributed Tracing (APM)

1. **Instrumentation** — Datadog APM SDK (dd-trace). All inbound HTTP/gRPC handlers + all outbound calls (HTTP, DB, Kafka) emit spans. Tags: `service`, `env`, `version` on every span.
2. **Span naming** — `<verb>.<resource>`: e.g. `http.post /orders`, `db.query orders`, `kafka.produce order-created`
3. **Sampling** — head-based 10% for high volume; always-sample errors and slow traces (p99 > SLO threshold); never-sample `/healthz`, `/readyz`.
4. **Service map** — after first deployment, verify expected topology. Flag unexpected dependencies.
5. **Error tracking** — `error.type`, `error.message`, `error.stack` on all error spans. Verify they surface in Datadog Error Tracking.

### G4D — Monitors and Alerting

| Monitor | Condition | Severity | Routing |
|---------|-----------|----------|---------|
| SLO error budget burn — fast | Burn rate > 14× over 1 h | 🔴 Critical | PagerDuty on-call |
| SLO error budget burn — slow | Burn rate > 2× over 6 h | 🟡 Warning | Slack war room |
| Latency p99 breach | p99 > page threshold | 🔴 Critical | PagerDuty |
| Error rate spike | error% > page threshold | 🔴 Critical | PagerDuty |
| Traffic anomaly | drop > 80% vs 1w avg | 🔴 Critical | PagerDuty |
| Saturation | CPU/memory > 95% | 🟡 Warning | Slack |
| Business metric drop | (if applicable) | 🔴 Critical | PagerDuty |

**Naming convention** (Decathlon standard): `[<Product>][<Environment>][<Technology?>] <alert description>`

**Runbook template** for each Critical monitor:
```markdown
## Alert: <name>
### What this means
### Impact on users / SLO
### Immediate actions (< 5 min)
### Escalation path
### Known causes and fixes
### How to silence safely
```

Deliverable: Terraform or Datadog YAML per monitor for version control.

---

## Step G5 — Automate Toil

**Goal:** identify repetitive operational tasks and eliminate them.

1. From Intake G-E.19 and G1C gaps, list all known manual tasks.
2. Classify each:

| Task | Frequency | Root cause | Automation | Effort |
|------|-----------|------------|-----------|--------|
| Manual pod restart after OOM | Daily | Memory limit too low | HPA + memory tuning | Low |
| Manual deploy approve | Per sprint | No auto-merge policy | GitHub Actions on green CI | Medium |
| Certificate renewal | Quarterly | No cert-manager | cert-manager Terraform | Low |

3. For Low/Medium effort tasks: propose a concrete solution (HPA config, GitHub Actions, Terraform, script).
4. Track toil%: current → target. **Never accept >50% toil without a timeline.**

---

## Step G6 — Load Testing and Resilience

**Goal:** validate capacity at peak load, design chaos experiments, verify RTO/RPO.

### G6A — Load Test Plan

From Intake G-B.7, G-B.8, G-C.11/12. If optional questions were skipped, use their defaults: nominal volume = TBD (note as assumption in the plan), peak multiplier = ×5 nominal, RTO = 30 min (Tier-1) / 2h (Tier-2), RPO = 1h (stateful) / N/A (stateless).

1. **Scenarios**:
   - Nominal: requests/day → req/s sustained 30 min
   - Peak: event multiplier (ask team; default ×5)
   - Ramp-up: 10 min to nominal, then spike to peak

2. **Success criteria** (from SLOs):
   - p99 latency < SLO threshold at peak
   - Error rate < SLO target at peak
   - No cascading failures downstream
   - Auto-scaling activates before saturation threshold

3. **Tooling**: k6 (preferred for GKE), Gatling, or Locust. k6 template:
   ```javascript
   import http from 'k6/http';
   import { check } from 'k6';
   export const options = {
     stages: [
       { duration: '10m', target: <nominal_rps> },
       { duration: '30m', target: <nominal_rps> },
       { duration: '5m',  target: <peak_rps> },
       { duration: '5m',  target: 0 },
     ],
     thresholds: {
       http_req_duration: ['p(99)<500'],
       http_req_failed:   ['rate<0.01'],
     },
   };
   ```

4. **Never run in production** without team approval and off-peak scheduling.

### G6B — Chaos Experiments

For each critical dependency (Intake D.13):

```
Hypothesis: if <dependency> is unavailable, <service> degrades gracefully
and recovers within RTO = <X min> / RPO = <Y min>.
Steady state: SLO compliance > target, error rate < 1%.
Chaos action: <kill pods | inject latency | block egress | saturate CPU | drop DB connection>
Expected outcome: circuit breaker opens, fallback activates, retries succeed within RTO.
```

Execute with Chaos Mesh, Gremlin, or `kubectl`. Validate with Datadog Synthetics. Do NOT mark complete until RTO and RPO are both validated.

---

## Output G — Reliability Design Document + SRE Task List

### Artefact 1 — Reliability Design Document

1. **SLO definitions** — SLI measurements, targets, error budgets, UJ mapping, SLA vs SLO delta
2. **PRD / architecture challenges** — gaps from G1B with proposed fixes
3. **Observability design** — log schema, trace checklist, monitor YAML/Terraform, alerting routing
4. **Load test plan** — scenarios, success criteria, k6 script skeleton
5. **Chaos experiment designs** — one per critical dependency
6. **Toil inventory** — current tasks, automation proposals, target toil%

### Artefact 2 — Prioritised SRE Task List

**P0 — Before launch (blocking)**
- [ ] Implement structured logging with `trace_id` correlation
- [ ] Deploy APM instrumentation (dd-trace) on all endpoints
- [ ] Create SLO in Datadog with error budget monitor (fast + slow burn)
- [ ] Create Critical monitors with PagerDuty routing
- [ ] Define and document RTO/RPO in the runbook
- [ ] Run nominal load test and validate SLO thresholds hold

**P1 — First sprint after launch**
- [ ] Create Datadog dashboard (golden signals + SLO widget + business metrics)
- [ ] Set up Warning monitors routing to Slack war room
- [ ] Write runbooks for each Critical monitor
- [ ] Run first chaos experiment on top dependency
- [ ] Identify and automate top-3 toil tasks

**P2 — First quarter**
- [ ] Run peak load test (Black Friday scenario)
- [ ] Complete chaos experiment coverage for all Tier-1 dependencies
- [ ] Review SLO targets after 30 days of production data
- [ ] Eliminate all toil tasks classified as Low effort

Challenge the team to accept each P0 task as a BMAD story before the product is marked ready for launch.

---

# Mode B — Brownfield

Reliability maturity audit for an existing service. Score the current state across 9 SRE dimensions, identify gaps, and produce a prioritised remediation backlog.

---

## Intake B — Audit Context *(BLOCKING)*

> ⛔ **Do NOT start the audit until automatic data collection is complete and the questions below are answered.**

### Automatic data collection (run in parallel before asking anything)

> ⚠️ **Datadog MCP required for Brownfield mode.** If `mcp_datadog_*` tools are unavailable, warn the user and fall back to questions-only audit (scoring based on team answers, not live data).

**Datadog:**
- `mcp_datadog_search_datadog_slos` — existing SLOs, targets, current compliance %
- `mcp_datadog_search_datadog_monitors` — active monitors, muted monitors, monitor count

**Reference file (best-effort, non-blocking):**
- Read `.github/skills/incident-investigation/references/uj_mapping.md` → look up the service
- Found: extract `impacted_uj_keys`, `war_room_slack_channels`, critical-tier UJs, team owner — use to pre-populate context and skip questions already answered
- Not found or file unavailable: continue normally, no error

Present a brief **auto-collected summary** to the user before asking questions:
```
Auto-collected for <service>:
- SLOs: <N found / none>
- Monitors: <N active, N muted>
- UJ mapping: <found: <UJ keys> / not yet indexed>
```

### Questions — ask only what data collection couldn't answer

Ask conversationally, one or two at a time. Skip any question already answered above:

1. What is the service name? *(skip if already known from argument)*
2. How long has this service been in production?
3. Any significant incidents in the last 6 months? Any recurring ones without a postmortem?
4. Is there an on-call rotation? Who gets paged? *(skip if found in uj_mapping.md)*
5. Is there a runbook? When was it last updated?
6. What is the team's biggest reliability pain point today?

---

## Step B1 — Reliability Maturity Scoring

Score each of the 9 dimensions using the scale below. Base the score on Datadog data (from Intake B queries) and answers from the team.

**Scoring scale:**
- 🔴 **Not in place** — missing or broken
- 🟡 **Partial** — exists but incomplete or not enforced
- 🟢 **Mature** — fully implemented, maintained, and effective

---

### Dimension 1 — SLOs and Error Budgets

| Check | Evidence needed | Score |
|-------|----------------|-------|
| SLOs defined for all user-facing endpoints | `mcp_datadog_search_datadog_slos` returns results | |
| SLO targets reflect user expectations (not arbitrary) | Team can explain the business rationale | |
| Error budget calculated and tracked | Error budget monitor exists (fast + slow burn) | |
| SLO compliance > target over last 30 days | Datadog SLO compliance % | |
| SLO reviewed and adjusted after significant incidents | Evidence of version history | |

**Questions to ask:**
- Are your SLOs tied to user journeys or just infra metrics?
- When did you last breach your error budget? What happened?
- Do devs check error budget before shipping a risky change?

---

### Dimension 2 — Golden Signals (Metrics)

| Check | Evidence needed | Score |
|-------|----------------|-------|
| Latency (p99) measured and alerted | Monitor on `trace.web.request.duration` or equivalent | |
| Traffic measured (request rate / business volume) | Dashboard widget or monitor | |
| Error rate measured and alerted | Monitor on error rate | |
| Saturation measured (CPU/memory) | HPA or saturation monitor in place | |
| Business metrics instrumented (orders/min, etc.) | Dashboard or custom metric | |

**Questions to ask:**
- Do you get alerted before users notice a problem, or after?
- Do you have business metrics that show user impact beyond infra signals?

---

### Dimension 3 — Structured Logging

| Check | Evidence needed | Score |
|-------|----------------|-------|
| Logs are structured JSON (not free text) | Sample log line in Datadog | |
| `trace_id` present on every log line | Cross-service correlation works in Datadog | |
| Log levels used consistently (ERROR/WARN/INFO/DEBUG) | No spurious ERROR logs in prod | |
| No PII in logs | GDPR / data privacy review done | |
| Log volume under control (no runaway DEBUG in prod) | Log ingestion cost reasonable | |

**Questions to ask:**
- Can you trace a single user request end-to-end across all services using only logs?
- Have you ever had a GDPR incident from a log line?

---

### Dimension 4 — Distributed Tracing (APM)

| Check | Evidence needed | Score |
|-------|----------------|-------|
| dd-trace (or equivalent) deployed on all services | Service appears in Datadog APM service map | |
| All inbound and outbound calls instrumented | Service map shows expected topology | |
| `service`, `env`, `version` tags on all spans | Span metadata complete in Datadog | |
| Error tracking configured (`error.type/message/stack`) | Errors surface in Datadog Error Tracking | |
| Sampling strategy defined (not 100% or 0%) | Sampling config documented | |

**Questions to ask:**
- When an incident fires, can you find the failing span in < 2 minutes?
- Have you ever had a service missing from your service map?

---

### Dimension 5 — Alerting and Runbooks

| Check | Evidence needed | Score |
|-------|----------------|-------|
| Critical monitors route to PagerDuty | Monitor message contains `@pagerduty-*` | |
| Warning monitors route to Slack | Monitor message contains `@slack-*` | |
| Every Critical monitor has a runbook | Runbook URL in monitor description | |
| Runbooks are actionable (not just "check logs") | Runbook has immediate actions < 5 min | |
| Alert fatigue is low (< 5 pages/week per person) | Ask team | |
| No permanently muted monitors | `mcp_datadog_search_datadog_monitors` — muted count | |

**Questions to ask:**
- When you get paged at 2am, is the runbook enough to act without calling anyone?
- How many alerts did you get last week? How many were actionable?

---

### Dimension 6 — Incident Management and Postmortems

| Check | Evidence needed | Score |
|-------|----------------|-------|
| Incident response process documented | Runbook / war room protocol exists | |
| War room Slack channel defined | `uj_mapping.md` or team knowledge | |
| MTTR tracked and improving | Incident history from team / Confluence | |
| Blameless postmortems written for all P0/P1 incidents | Confluence postmortem pages exist | |
| Recurring incidents identified and fixed | No incident appearing > 2× in last 90 days | |

**Questions to ask:**
- What is your current MTTR? Is it improving?
- Can you show me the postmortem for your last P0 incident?
- Are there incidents you've seen more than twice without fixing the root cause?

---

### Dimension 7 — Toil and Automation

| Check | Evidence needed | Score |
|-------|----------------|-------|
| Toil level estimated and tracked | Team can quantify % of time on manual ops | |
| Deployments are automated (no manual steps) | CI/CD pipeline with auto-deploy on green | |
| No recurring manual restarts or config changes | Ask team | |
| HPA / auto-scaling configured | GKE HPA or KEDA config exists | |
| Toil < 50% of team operational time | Team confirms | |

**Questions to ask:**
- What is the one task you do most often that you wish was automated?
- How long does a deployment take end-to-end, including manual steps?

---

### Dimension 8 — Capacity and Load Testing

| Check | Evidence needed | Score |
|-------|----------------|-------|
| Expected peak load documented | Architecture or capacity plan | |
| Load test run against nominal load | Load test results exist | |
| Load test run against peak load (Black Friday scenario) | Peak test results exist | |
| Auto-scaling validated under load | HPA triggered during load test | |
| SLO thresholds hold at peak | Load test report confirms p99/error rate | |

**Questions to ask:**
- When was your last load test? Did it include a peak scenario?
- What happens to your service during a Black Friday spike — do you know?

---

### Dimension 9 — Resilience and RTO/RPO

| Check | Evidence needed | Score |
|-------|----------------|-------|
| RTO and RPO defined for all stateful components | Architecture doc or runbook | |
| At least one chaos experiment run | Experiment report or Chaos Mesh history | |
| Circuit breakers / graceful degradation implemented | Code review or architecture review | |
| Recovery validated within stated RTO | Post-chaos test results | |
| No single points of failure in production | Architecture review | |

**Questions to ask:**
- Have you ever intentionally broken your service to see how it recovers?
- If your primary database goes down, what does your service do?

---

## Step B2 — Produce Maturity Scorecard

After scoring all 9 dimensions, produce the scorecard:

```
Reliability Maturity — <Service Name>  (assessed: <date>)

Dimension                        Score   Key gap
───────────────────────────────────────────────────────
1. SLOs & Error Budgets          🟡      No fast-burn monitor
2. Golden Signals                🔴      No business metrics
3. Structured Logging            🟢      —
4. Distributed Tracing (APM)     🟡      version tag missing on 2 services
5. Alerting & Runbooks           🔴      3 Critical monitors have no runbook
6. Incident Management           🟡      No postmortem for last 2 P1s
7. Toil & Automation             🔴      ~60% toil, no HPA
8. Capacity & Load Testing       🔴      No load test ever run
9. Resilience / RTO-RPO          🔴      RTO undefined, no chaos experiments

Overall: 1× 🟢  4× 🟡  4× 🔴
```

---

## Step B3 — Produce Remediation Backlog

Group by priority. Each item includes: gap, action, owner (team vs SRE), and effort.

**P0 — Critical reliability risks (fix before next incident)**
- [ ] Create fast-burn SLO monitor (burn rate > 14× over 1h) → team, effort: Low
- [ ] Write runbooks for all Critical monitors → team, effort: Medium
- [ ] Define RTO/RPO for stateful components → team + SRE, effort: Low
- [ ] Fix spurious ERROR logs (alert fatigue) → team, effort: Medium

**P1 — Significant gaps (next sprint)**
- [ ] Instrument business metrics (orders/min, payment success rate) → team, effort: Medium
- [ ] Add `version` tag to all APM spans → team, effort: Low
- [ ] Write postmortems for last 2 unreviewed incidents → team, effort: Low
- [ ] Configure HPA for top-traffic services → team + SRE, effort: Medium

**P2 — Maturity improvements (next quarter)**
- [ ] Run first nominal load test and validate SLO thresholds → SRE, effort: Medium
- [ ] Run peak load test (Black Friday scenario) → SRE, effort: High
- [ ] Design and run first chaos experiment on top dependency → SRE, effort: High
- [ ] Eliminate top-3 toil tasks → team, effort: Medium

For each P0 and P1 item: propose it as a BMAD story to the product team so it enters the backlog formally.

---

## Output B — Reliability Maturity Report

### Artefact 1 — Reliability Maturity Scorecard
The completed scorecard from Step B2: 9-dimension scoring table with overall summary (N× 🟢 / N× 🟡 / N× 🔴) and one key gap per dimension.

### Artefact 2 — Prioritised Remediation Backlog
The full backlog from Step B3 with P0/P1/P2 items, owner (team vs SRE), and effort estimate per item.

Present both artefacts together. For each P0 and P1 item, propose it as a BMAD story so it enters the team's formal backlog.
