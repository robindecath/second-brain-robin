---
name: sre-platform-setup
description: Setup and verification for the SRE Platform Reliability module. Registers the bmad-agent-sre skill, verifies external skill and MCP tool availability, and optionally deploys Copilot CLI agent files for standalone use. Triggers on 'setup', 'configure', or 'sre-platform-setup'.
---

# SRE Platform Reliability — Setup

## Overview

This skill registers the `sre-platform` module and verifies that all required external
skills and MCP tools are available.

Skills fetched from external repositories via `skills.config.json`:

| Skill | Source repo |
|---|---|
| `help-sre` | `dktunited/ai-augmented-sdlc` |
| `incident-investigation` | `dktunited/ai-augmented-sdlc` |
| `datadog-slo-lookup` | `dktunited/ai-augmented-sdlc` |
| `slo-generator` | `dktunited/ai-augmented-sdlc` |

> `datadog-slo-lookup` and the `dd-*` Datadog skills are declared in
> `sre-platform-setup/assets/module.yaml` but are **not** yet listed in this
> repo's `skills.config.json`, so they are not installed by the bundle. Tracked
> separately — see the PR that aligned this repo with BMAD-METHOD 6.11.0.

## Module Contents

### BMAD Agent
| Component | Path |
|---|---|
| Morgan (bmad-agent-sre) | `bmad-agent-sre/SKILL.md` |

## On Activation

### Step 1: Verify External Skills

Check that the skills listed above appear in the active session's `<available_skills>`.
For each:
- ✅ present → proceed
- ❌ missing → warn: "Skill `<name>` is not installed. Run the BMAD installer or check `skills.config.json`."

### Step 2: Verify MCP Tools

> **Note:** MCP servers are not auto-provisioned by this repo. Each developer must configure them manually in their Copilot CLI settings (`~/.copilot/mcp-config.json`) or in VS Code (`mcp` settings).

| MCP Server | Required Tools | Purpose |
|---|---|---|
| `mcp_datadog_*` | `search_datadog_monitors`, `search_datadog_slos`, `search_datadog_incidents`, `search_datadog_logs`, `search_datadog_events`, `aggregate_events`, `search_datadog_rum_events` | Incident investigation, SLO lookup, audit |
| `confluence_*` (optional) | `confluence_search`, `confluence_get_page_by_id` | Post-mortem history |

Report any missing tools but do not fail — the agent degrades gracefully.
GitHub access uses `gh` CLI (always available in terminal).

### Step 3: Deploy Skills (optional)

If the user wants to use Morgan as a standalone Copilot CLI agent (without BMAD),
deploy the skills to the project's `.github/` directory:

```bash
# From project root — run once per project

# Deploy help-sre skill from this module
mkdir -p .github/skills
cp -r _bmad/modules/sre-platform/help-sre .github/skills/

# Skills installed by the BMAD installer into _bmad/skills/<name>/
for skill in incident-investigation slo-generator datadog-slo-lookup; do
  [ -d "_bmad/skills/$skill" ] && cp -r "_bmad/skills/$skill" .github/skills/
done
```

After deployment, Morgan is available as `bmad-agent-sre` (BMAD) and the skills
`help-sre` and `incident-investigation` are available in `.github/skills/`.

### Step 4: Report Status

```
## SRE Platform Reliability — Module Status

### Agent
- ✅ bmad-agent-sre (Morgan) — loaded from this module

### Bundled Skills
- ✅ help-sre (this module)

### External Skills (from skills.config.json)
- ✅ / ❌  incident-investigation  (dktunited/ai-augmented-sdlc)
- ✅ / ❌  datadog-slo-lookup      (dktunited/ai-augmented-sdlc)
- ✅ / ❌  slo-generator           (dktunited/ai-augmented-sdlc)

### MCP Tool Status
| Tool Group | Status |
|---|---|
| Datadog    | ✅ / ❌ |
| Confluence (optional) | ✅ / ❌ / ⚠️ not required |

### Quick Start
Invoke Morgan with: `bmad-agent-sre`
Menu options: HS (Help SRE) — II (Incident Investigation)
```
