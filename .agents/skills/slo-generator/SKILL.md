---
name: slo-generator
description: >
  Reads and discovers existing SLI YAML files from the dktunited/slo-generator repo.
  MANDATORY before any Datadog SLO query: use this skill first to identify which SLIs
  exist for a product/service, extract their metadata.name (used as Datadog SLO name),
  and retrieve their query_good/query_valid definitions.
  Also used when simulating the impact of an incident on a product (to enumerate all
  impacted SLIs and their goals).
  Keywords: SLO, SLI, discovery, read, list, find, lookup, impact simulation,
  slo-generator, Datadog, availability, latency, reliability, Decathlon SRE.
argument-hint: "<product-or-service-name>"
user-invocable: true
license: MIT
metadata:
  version: 1.0.1
  last-updated: 2026-07-08
  audience: all
  domain: sre
  api: rest
  owner: sig-reliability
  mcp_required: false
---

# SLO Generator — SLI Discovery & Read

Read-only skill. Fetches existing SLI YAML files from
[`dktunited/slo-generator`](https://github.com/dktunited/slo-generator) via GitHub MCP
to identify what to query in Datadog.

## Hard Rules

1. **NEVER use `http_request` for any purpose.** Only use `shell` (gh CLI) for SLI discovery/fetching and `mcp_datadog_search_datadog_slos` for Datadog SLO queries.
2. **Always call `read_skill` first** to load this skill before any other action.
3. **Never guess SLO names** — always derive `metadata.name` from SLI YAML content.
4. **If search returns zero results**, respond with exactly "not found" in your answer.

## When to use this skill

**ALWAYS invoke this skill BEFORE querying Datadog for SLO data**, to:

- Discover which SLIs exist for a product or service
- Extract `metadata.name` → used as the SLO identifier in Datadog
- Retrieve `query_good` / `query_valid` → the exact Datadog metric queries
- Know the `goal` (objective) to assess breach severity
- Enumerate all SLIs for a product when simulating incident impact

**Trigger conditions:**

- Any health check, incident investigation, or SLO lookup for a named product/service
- User asks to simulate or estimate the impact of a failure on a product
- User asks "which SLOs exist for X?" or "what does X monitor?"

---

## Step 1 — Discover SLIs in the repo (gh CLI)

Use `gh search code` or `gh api` on `dktunited/slo-generator`.

### Search by product / service name

```bash
gh search code "<product-name>" --repo dktunited/slo-generator
```

Examples:

```bash
gh search code "checkout" --repo dktunited/slo-generator
gh search code "oneshop" --repo dktunited/slo-generator
gh search code "payment" --repo dktunited/slo-generator
```

### Browse by business unit

Repo structure:

```
sli/
├── <business-unit>/          # e.g.: bcp, ecommerce, customer-growth
│   └── <team-or-service>/   # e.g.: onepayv2, oneshop
│       ├── sli_service-feature-availability.yaml
│       └── sli_service-feature-latency-500ms.yaml
```

List a directory:

```bash
gh api repos/dktunited/slo-generator/contents/sli/<business-unit>/<team>
```

Fetch a specific file:

```bash
gh api repos/dktunited/slo-generator/contents/sli/<bu>/<team>/<file>.yaml --jq '.content' | base64 -d
```

> **If `gh` CLI is unavailable** (e.g. VS Code chat / Copilot context): use the `github_repo` tool with the file path as query in repo `dktunited/slo-generator` to retrieve full file content.

> **Empty / no results handling:** If `gh search code` returns zero matches, respond with exactly **"not found"** in your answer and explain what this means operationally.

---

## Step 1b — Fetch full YAML content for every discovered file (BLOCKING)

> ⛔ **HARD STOP.** Search results (`gh search code`, `github_text_search`) return **file-path excerpts only** — they are NOT sufficient to reliably extract `metadata.name`, `spec.goal`, or `support_group`.

For every file path discovered in Step 1, fetch the complete YAML body before proceeding:

**CLI:**

```bash
gh api repos/dktunited/slo-generator/contents/<full-path-to-file>.yaml --jq '.content' | base64 -d
```

**VS Code / no-CLI fallback:** use the `github_repo` tool with the exact filename (e.g. `slo-oneff-api-get-scenario-latency_600ms-app-eu.yaml`) as query in `dktunited/slo-generator`.

Do NOT proceed to Step 2 until every file's full YAML content is available in context.

---

## Step 2 — Extract key fields from each YAML

For every SLI file found, extract:

| Field                | Path in YAML                                              | Used for                                                                |
| -------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Datadog SLO name** | `metadata.name`                                           | Query Datadog: `mcp_datadog_search_datadog_slos` with this name         |
| **SLO objective**    | `spec.goal`                                               | Assess breach severity. Report as raw decimal (e.g. `0.999`, not 99.9%) |
| **Description**      | `spec.description`                                        | Human-readable context                                                  |
| **SLO type**         | `metadata.labels.slo_name`                                | availability / latency_Xms / quality…                                   |
| **Service**          | `metadata.labels.service_name`                            | Scope of impact                                                         |
| **Feature**          | `metadata.labels.feature_name`                            | Which endpoint/feature                                                  |
| **Team**             | `metadata.labels.support_group`                           | Who to notify                                                           |
| **Datadog queries**  | `spec.service_level_indicator.query_good` / `query_valid` | Direct metric queries if needed                                         |

---

## Step 3 — Hand off to Datadog (describe, do not execute)

After collecting all `metadata.name` values, **describe** how to query Datadog:

```
mcp_datadog_search_datadog_slos  →  name:<metadata.name>
```

One call per SLI, or batch if the tool supports it.

**Do NOT guess SLO names in Datadog.** Always derive them from the YAML `metadata.name`.
**Do NOT call `http_request`** — only reference `mcp_datadog_search_datadog_slos` by name.
**Do NOT execute Datadog queries in this skill.** This skill is read-only discovery; the Datadog handoff is informational.

---

## Impact Simulation Workflow

When user asks: _"what is the impact if service X is down?"_ or _"simulate an incident on product Y"_:

1. **Run this skill** → fetch all SLI files for the product/service
2. **Build impact table** from extracted fields. Report `spec.goal` as the **raw decimal value** (e.g. `0.999` for 99.9%, `0.99` for 99.0%), not as a percentage.

| SLI name                         | Type         | Goal  | Feature  | Team        |
| -------------------------------- | ------------ | ----- | -------- | ----------- |
| `slo-checkout-api-availability`  | availability | 0.999 | checkout | ce-payments |
| `slo-checkout-api-latency-500ms` | latency      | 0.99  | checkout | ce-payments |

3. **Reference the Datadog query step** — state that to check live SLO status, one would call `mcp_datadog_search_datadog_slos` with each `metadata.name`. Do NOT execute `http_request` to the Datadog API.
4. **Assess breach risk**: compare current error rate vs remaining error budget (`1 - goal`)
5. **Report**: list all SLIs at risk, team owners, and estimated business impact

---

## SLI YAML Structure Reference

```yaml
apiVersion: sre.google.com/v2
kind: ServiceLevelObjective
metadata:
  labels:
    service_name: <service-name>
    feature_name: <feature-name>
    slo_name: availability # availability | latency_<N>ms | quality | …
    measure_point: app # browser | cdn | apim | lb | app
    support_group: ce-<team> # must start with ce- or cs-
    business_unit: ecommerce # see enum below
  name: slo-<service>-<feature>-<slo_name> # ← Datadog SLO identifier
spec:
  backend: datadog/DigitalCommerce
  description: Human-readable description
  goal: 0.99 # 0.999 = 99.9%
  method: good_bad_ratio
  service_level_indicator:
    query_good: >- # Datadog metric query for "good" events
      ...
    query_valid: >- # Datadog metric query for all events
      ...
```

### `business_unit` Enum

```
bcp | connected-sports-platform | customer-growth | in-store |
sportproducts | circularity | ecommerce | value-chain |
switzerland | cpe | data | digital-for-people
```

### `slo_name` Patterns

```
availability
latency_<N>ms    (e.g.: latency_500ms, latency_1000ms)
latency_<N>s
freshness_<N>ms / freshness_<N>s
quality | throughput | coverage | correctness | durability
```

---

## File Organisation

```
sli/
├── <business-unit>/              # e.g.: bcp, ecommerce, customer-growth
│   └── <team-or-service>/        # e.g.: onepayv2, oneshop
│       ├── sli_service-feature-availability.yaml
│       └── sli_service-feature-latency-500ms.yaml
```

### Naming Conventions

| Element         | Convention                                | Example                              |
| --------------- | ----------------------------------------- | ------------------------------------ |
| File name       | `sli_<service>-<feature>-<slo-type>.yaml` | `sli_checkout-api-availability.yaml` |
| `metadata.name` | `slo-<service>-<feature>-<slo-type>`      | `slo-checkout-api-availability`      |

---

## Resources

- [slo-generator Repo](https://github.com/dktunited/slo-generator)
- [Browse sli/ directory](https://github.com/dktunited/slo-generator/tree/main/sli)
