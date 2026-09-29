---
name: decathlon-find-mcp-server
description: >
  Discover and install MCP servers from the Decathlon curated catalog. Fetches
  mcp.catalog.json from dktunited/ai-augmented-sdlc, matches the current context
  against each entry's description and example, and guides installation — via the
  AI Augmented SDLC canvas on Copilot App, or manual serverConfig elsewhere.
  Triggers on: "what MCPs are available", "find MCP server", "which MCP should I use",
  "install MCP", "add MCP", "MCP catalog", "MCP servers", "connect Jira", "connect Figma",
  "connect Datadog", "dkt-find-mcp".
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  mcp_required: false
---

# Decathlon MCP Server Discovery

## Overview

This skill browses or searches the Decathlon curated MCP catalog (`mcp.catalog.json`) to
match your current context to the right MCP server and guide you through installation.

Available MCP servers cover: Decathlon API Management, SMA-X IT Service Management,
Atlassian (Jira/Confluence), SonarQube, Statsig A/B testing, Datadog, Databricks SQL,
Chrome DevTools, and Figma.

Unlike generic web searches, this skill:
- Reads the **team-maintained `mcp.catalog.json`** — the single source of truth for
  installable MCP servers at Decathlon
- Matches your **active context** (URLs, tool mentions, task description) against each
  entry's `description` and `example` fields
- Guides installation via the **AI Augmented SDLC canvas** on Copilot App, or provides
  the exact `serverConfig` block for manual setup in VS Code and other IDEs

## When to use this skill

Auto-invoke this skill when any of the following are true:

- The user asks which MCP servers are available (e.g. "what MCPs can I install?", "show me the MCP catalog")
- The user asks how to connect a tool to their agent (e.g. "how do I connect Jira to Copilot?", "add Datadog to my agent")
- The user pastes or references content from an external platform that maps to a known MCP:
  - A Jira issue URL or Confluence page link → `atlassian`
  - A Figma file or component link → `figma`
  - A Datadog dashboard, log, or alert URL → `datadog`
  - A SonarQube report or quality gate mention → `sonarqube`
  - A Statsig experiment or feature flag mention → `statsig`
  - A Databricks notebook or SQL query mention → `databricks-sql`
  - An SMA-X ticket or IT service request mention → `smax`
  - A Decathlon API or APIM reference → `decathlon-apim`
- The user explicitly asks to browse the MCP catalog
- The user types `dkt-find-mcp`

## On Activation

### Step 1 — Determine mode

Classify the activation into one of two modes:

- **Context match mode**: the user's message or active context contains a specific external
  tool reference, URL, or mention that maps to a known MCP server. Skip the catalog browse
  and proceed directly to Step 3 to match the entry.
- **Browse mode**: the user is asking generally about available MCPs or what can be installed.
  Proceed through all steps, presenting a full catalog table in Step 3.

### Step 2 — Fetch the catalog

> **Canonical source: `dktunited/ai-augmented-sdlc@main`** — always fetch live; never use
> a local copy or vendored snapshot. The catalog changes with every MCP server PR and a
> stale copy would silently expose wrong `serverConfig` blocks or missing entries.

**Primary — `gh api` with raw Accept header** (handles org SSO/SAML automatically):

```bash
gh api "repos/dktunited/ai-augmented-sdlc/contents/mcp.catalog.json?ref=main" \
  -H "Accept: application/vnd.github.raw"
```

The `Accept: application/vnd.github.raw` header returns the raw file bytes directly —
no base64 decoding needed.

**Fallback — `curl` with a token from `gh auth token`** (use if `gh api` fails):

```bash
curl -fsSL \
  -H "Authorization: Bearer $(gh auth token)" \
  -H "Accept: application/vnd.github.raw" \
  "https://api.github.com/repos/dktunited/ai-augmented-sdlc/contents/mcp.catalog.json?ref=main"
```

**If both fail**, stop and surface an actionable error — never silently invent catalog
entries:

> "Unable to fetch `mcp.catalog.json` from `dktunited/ai-augmented-sdlc`. Check your
> authentication (`gh auth status`) and network access to the org (VPN/Zscaler). I cannot
> suggest MCP servers without the catalog — I will not invent entries."

Parse the resulting JSON array. Each entry has the fields:
`id`, `name`, `description`, `icon`, `category`, `example`, `docsHref`, `authType`,
`parameters`, and `serverConfig`.

### Step 3 — Match context to catalog

**Context match mode:**
Scan each entry's `description` and `example` for relevance to the current context.
Check for tool names, platform keywords, and URL domains. If a clear match is found
(confidence ≥ 70%), skip Step 4 and go directly to Step 5 with that entry.
If multiple entries match, present the top matches ranked by relevance and ask the user
to confirm which one to use.

**Browse mode:**
Present all MCPs in a table:

| Icon | Name | Category | Auth | Example use case |
|------|------|----------|------|-----------------|
| 🏢 | API Management | internal | none | `#search-apis get API endpoints for ...` |
| 🎫 | SMA-X — IT Service Management | internal | none | `#smax find open incidents assigned to my team` |
| 🔷 | Atlassian — Jira / Confluence | external | oauth2 | `Create a Jira about this TODO code ...` |
| … | … | … | … | … |

Ask the user: "Which MCP server would you like to install?"

### Step 4 — Confirm intent

Before proceeding with installation guidance, confirm with the user:

> "I found **[icon] [MCP name]** — [description]. Would you like to install it?"

If the user confirms, proceed to Step 5. If not, return to the catalog table (Step 3,
browse mode) so the user can pick a different entry.

### Step 5 — Installation guidance

Detect the install path based on the current environment:

**On GitHub Copilot App** (check if the `ai-sdlc` canvas is available in the current
tool context — i.e. the `open_canvas` tool is present):

> "You can install **[MCP name]** directly from the AI Augmented SDLC canvas:
> 1. Open the **AI Augmented SDLC canvas** (click the canvas icon or ask me to open it)
> 2. Navigate to the **MCP Catalog** tab
> 3. Click **[MCP name]** — the canvas handles authentication and server configuration automatically."

Offer to open the canvas immediately:
```
open_canvas({ canvasId: "ai-sdlc" })
```

**Manual / VS Code / other IDE:**

Provide the exact `serverConfig` block from the catalog entry. Tailor instructions
by `authType`:

- **`authType: none`** (e.g. `decathlon-apim`, `smax`, `chrome-devtools`): configuration
  is straightforward — paste the `serverConfig` block into your MCP settings.

- **`authType: oauth2`** (e.g. `atlassian`, `datadog`, `figma`): auth is interactive on
  first use — paste the `serverConfig` and complete the OAuth flow when prompted.

- **`authType: apikey`** (e.g. `sonarqube`, `statsig`): provide the parameter names from
  `parameters[]` and the `docsHref` link for token generation. Example for SonarQube:
  ```
  Required parameter:
    SONARQUBE_TOKEN — your SonarQube user token
    How to get it: Settings → Security → Generate Token
    Docs: [docsHref]
  ```

- **`authType: env`** (e.g. `databricks-sql`): list all `parameters[]` entries with their
  labels and placeholder values, plus the `docsHref` link.

For VS Code, the user adds the `serverConfig` to `.vscode/mcp.json` (workspace-level) or
their user settings under `mcp.servers`.

### Step 6 — Post-install

After confirming the user has installed the MCP, provide:

1. A summary of key tools the MCP exposes (inferred from the `description` field).
2. A suggested first command using the catalog's `example` field:
   > "Try this to get started: `[example]`"
3. A link to the full documentation if `docsHref` is not null:
   > "Full docs: [docsHref]"
