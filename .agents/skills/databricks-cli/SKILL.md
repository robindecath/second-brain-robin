---
name: databricks-cli
description: >
  Query and manage Decathlon's Databricks workspaces (SQL warehouses, Unity
  Catalog, clusters, jobs, workspace files) through the `databricks` CLI —
  no manually managed personal access token, no MCP install required. Use whenever the user
  asks to run a SQL query against the datalake, browse Unity Catalog
  catalogs/schemas/tables, check a warehouse/cluster/job status, or read a
  Databricks notebook/workspace file, and the `databricks-sql` MCP tools
  aren't available or connected. Examples: "run this SQL against dkt-expl",
  "list the schemas in datalake_gold", "is the sales warehouse running",
  "show me the last runs of job X". Never invents query results — always run
  the query and relay the real output.
license: MIT
metadata:
  audience: all
  domain: business-intelligence
  api: cli
  mcp_required: false
  owner: Decathlon AI Augmented SDLC
  version: "1.0.0"
---

# Databricks CLI

`databricks` is the official Databricks CLI. It is installed by default by
the AI Augmented SDLC platform installer (like `gcloud` and `gws`), together
with two pre-configured `~/.databrickscfg` profiles when creating a new config.
Existing configs are preserved. `DATABRICKS_CONFIG_FILE` overrides the config path.

| Profile | Workspace | Notes |
|---|---|---|
| `dkt-expl` | Decathlon Data Platform — Exploration | Default profile. Use unless told otherwise. |
| `dkt-indus` | Decathlon Data Platform — Indus | Use only when the user names "Indus" / the production data platform explicitly. |

**Never invent query results, table schemas, or job/cluster status — always
run the actual command and relay its real output.**

## When to use this skill

- Running ad-hoc SQL against the datalake (GMV, sales, any Unity Catalog table).
- Browsing Unity Catalog: catalogs, schemas, tables, columns, grants.
- Checking SQL warehouses, clusters, jobs, pipelines status or history.
- Reading/listing Databricks workspace files, notebooks, or repos.
- **If the `databricks-sql` MCP is already connected** (look for tools like
  `execute_sql` / `execute_sql_read_only`), prefer those structured tools —
  they're simpler to call. Fall back to this skill's CLI path whenever the
  MCP isn't installed/connected, which is the common case since MCPs are
  opt-in here.

## Preflight

```bash
scripts/databricks-auth-hint.sh [profile]   # defaults to dkt-expl
```

The helpers require Bash (Git Bash on Windows); the SQL wrapper also requires
Node.js, already included by the platform installer. Enable your Node runtime
if you opted out of installation. No npm packages are required.

Helpers locate the CLI on PATH or in the platform's default install directories
without editing shell startup files. If the direct `databricks` commands below
are not on PATH, source `scripts/databricks-auth-hint.sh` in Bash and use
`databricks_cli` instead; it resolves the executable in those locations.

The preflight prints `databricks: ready (profile dkt-expl)` when good to go,
or diagnostics and setup guidance on stderr with a non-zero exit. The SQL
wrapper performs the same preflight before making a request; relay its
diagnostics rather than assuming every failure is an expired login.

- CLI not found by the helper → re-run the platform
  installer, or see
  [the manual install docs](https://docs.databricks.com/dev-tools/cli/install.html).
- Config missing or missing the selected profile → relay the helper's
  profile-specific `auth login --host ...` command below. Re-running the
  installer will **not** modify an existing config or add missing profiles.
- Workspace unreachable → inspect the CLI error. Network and permission
  problems are not necessarily expired authentication.
- Authentication expired → sign in below.

**Never run `databricks auth login` yourself.** It opens a browser OAuth
consent flow and blocks on a localhost redirect listener until a human
approves — it would hang your turn, exactly like `gws auth login`. Instead,
relay the exact command and stop:

```
databricks auth login -p dkt-expl --host https://decathlon-dataplatform-exploration.cloud.databricks.com
```

Tell the user what to expect: it opens `https://login.databricks.com/…` (or
directly the workspace's OAuth page) in their browser; they sign in with
their Decathlon account and approve, and the command finishes on its own.
The supplied workspace guidance expects login roughly **once a day**;
renewal depends on the organization's session policy, not a fixed CLI timeout.
For `dkt-indus`, use its corresponding host from the preflight hint.

Once the user confirms they signed in, re-run the preflight check and carry on.

## Running SQL

There is no single "run a query" CLI verb; SQL runs through the **Statement
Execution API**, wrapped for you by `scripts/databricks-sql.sh`:

```bash
# 1. Find a warehouse ID (ask the user if there are several and it matters):
databricks warehouses list -p dkt-expl -o json

# 2. Submit and poll for up to 30 attempts after the initial wait.
#    Prints JSON; inspect the exit code for incomplete or still-running results:
scripts/databricks-sql.sh dkt-expl <warehouse_id> "SELECT * FROM datalake_gold.sales.sales_detail LIMIT 10"

# Optional catalog/schema defaults (avoids fully-qualifying every table):
scripts/databricks-sql.sh dkt-expl <warehouse_id> "SELECT * FROM sales_detail LIMIT 10" datalake_gold sales
```

Exit codes:

| Code | Meaning |
|---|---|
| `0` | Succeeded with a complete inline result. |
| `1` | Statement failed/canceled, CLI request failed, or response was invalid. Inspect stderr; terminal statement failures also print diagnostic JSON. |
| `2` | CLI/workspace preflight failed; relay its diagnostics. |
| `3` | Succeeded, but results are **incomplete**, chunked, truncated, or externally linked. JSON on stdout is not a complete answer. |
| `4` | Still pending/running after the polling limit. The query has **not** been canceled. |

On code `4`, do not submit the statement again, especially for writes. Use
the exact resume command printed on stderr, which only polls the existing ID:

```bash
scripts/databricks-sql.sh --resume dkt-expl <statement_id>
```

The JSON response follows the
[Statement Execution API](https://docs.databricks.com/api/workspace/statementexecution/executestatement)
shape: `status.state`, `manifest.schema.columns[]` (names/types), and
`result.data_array` (rows, values as strings). Read columns and rows from
there — do not guess column order or types. On code `3`, explicitly tell the
user results are partial. For chunked inline results, use
`databricks api get <result.next_chunk_internal_link> -p <same-profile> -o json`
and follow further chunk links until exhausted, respecting a reasonable
output limit and disclosing it. Only use relative links under
`/api/2.0/sql/statements/<same-statement-id>/result/chunks/`.
If `manifest.truncated` is true, more chunks will not recover omitted data:
use a narrower query or agree on an export strategy. Never silently count or
summarize the first chunk as though it were all rows.

For other read-only exploration (no need to run raw SQL), use the direct
CLI commands instead of the Statement Execution API:

```bash
databricks catalogs list -p dkt-expl -o json
databricks schemas list <catalog> -p dkt-expl -o json
databricks tables list <catalog> <schema> -p dkt-expl -o json
databricks tables get <catalog>.<schema>.<table> -p dkt-expl -o json
```

## Other common operations

```bash
databricks clusters list -p dkt-expl -o json
databricks jobs list -p dkt-expl -o json
databricks jobs list-runs --job-id <id> -p dkt-expl -o json
databricks workspace list /Shared -p dkt-expl -o json
databricks current-user me -p dkt-expl -o json   # who am I, for a sanity check
```

Every subcommand mirrors a Databricks REST API and accepts `-o json` for
structured output — use `databricks <group> --help` to discover the exact
verb for anything not listed above; don't guess flags.

## Safety

- Read-only by default in intent: prefer `SELECT`/`list`/`get` operations.
  Only run a mutating statement (`INSERT`/`UPDATE`/`DELETE`/DDL, or a
  `create`/`delete`/`edit` CLI verb) when the user explicitly asked for it.
- Never paste a bearer token, PAT, or the contents of `~/.databrickscfg`
  into chat output — profiles use OAuth (`auth_type = databricks-cli`), not
  long-lived secrets, but treat the config file as sensitive regardless.
