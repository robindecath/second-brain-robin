---
name: decathlon-ai-augmented-development-docs
description: >
  Read the official AI Augmented Development documentation portal
  (ai-augmented-development.decathlon.net) without logging into the site. The
  portal is login-gated, so this skill fetches the versioned, full-content
  `llms-full.txt` bundle from the public/llms/ folder of
  dktunited/ai-augmented-development via the authenticated gh CLI, and uses it to
  answer questions about AI at Decathlon: GitHub Copilot (what it is, billing,
  quota policy, best practices), the AI Augmented SDLC (standards, tools, canvases,
  installer, going to production), agent skills, MCP servers, coding standards,
  trainings, talks and monthly community calls. The whole-site
  `public/llms/llms-full.txt` inlines every documentation page AND every classic
  portal page, with their links preserved — it is the single complete source.
  Triggers on: "AI augmented development docs", "ai-augmented-development.decathlon.net",
  "Decathlon Copilot docs", "Copilot billing/quota at Decathlon", "AI Augmented SDLC docs",
  "how does the SDLC platform work", "read the AI dev portal", "dkt-ai-dev-docs".
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  mcp_required: false
---

# Decathlon AI Augmented Development Docs

## Overview

The documentation portal at **https://ai-augmented-development.decathlon.net** is the
single source of truth for AI Augmented Development at Decathlon — GitHub Copilot usage,
the AI Augmented SDLC platform, coding standards, reusable Agent Skills, MCP servers,
trainings and community resources.

That site is **login-gated**, so an agent cannot browse it directly. To stay usable by
agents anyway, the portal publishes a plain-text, full-content bundle following the
[llms.txt](https://llmstxt.org/) convention, and that bundle is **committed to GitHub** in
the `dktunited/ai-augmented-development` repository under `public/llms/`. This skill reads
it from GitHub via the authenticated `gh` CLI — no login, no scraping.

## The one rule: only read `llms-full.txt`

There are several bundles under `public/llms/`, but **you must only read the
`llms-full.txt` files** — nothing else in that folder. Only those contain the
*complete inlined content* of the site.

The whole-site `public/llms/llms-full.txt` is the default and the single most
complete source: it inlines **every documentation page and every classic portal
page** (Trainings & Tutorials, Talks & Presentations, Monthly Community Calls,
MCP Servers, Agent Skills, Standards, …), with their **links preserved** as
Markdown so you can cite and follow external URLs.

Everything else under `public/llms/` — `llms.txt`, `llms-pages.txt`, any
`*/llms.txt`, and the `index.json` manifest — is **off limits**. The `*.txt`
indexes are link-only lists that point back to the login-gated site (an agent
following them gets lost); `index.json` is just bundle metadata. Ignore them all
and read only `llms-full.txt`.

| Path under `public/llms/` | Read it? | Why |
|---|---|---|
| `llms-full.txt` | ✅ **Yes — default** | Whole site: every doc **and** every classic page inlined, links preserved. |
| `docs/<product>/llms-full.txt` | ✅ Optional | Docs-only full content for one product, when you only need that product. |
| `llms.txt`, `llms-pages.txt`, `*/llms.txt` | ❌ **No** | Link-only indexes pointing at the login-gated site. |
| `index.json`, anything else | ❌ **No** | Not full content — bundle metadata / out of scope. |

`<product>` is one of: `github-copilot`, `ai-augmented-sdlc`.

## Prerequisites

- An authenticated `gh` CLI with access to the private Decathlon org
  (`gh auth status` should show `github.com`). The same access used by the other
  `decathlon-*` skills.
- Network access to `api.github.com`.

## How to use this skill

### Step 1 — Fetch the full-content bundle

Default (whole portal — recommended for almost every question):

```bash
gh api repos/dktunited/ai-augmented-development/contents/public/llms/llms-full.txt \
  -H "Accept: application/vnd.github.raw" --cache 1h
```

Scoped to a single product (smaller, docs-only, when the question is clearly about just one):

```bash
# GitHub Copilot only
gh api repos/dktunited/ai-augmented-development/contents/public/llms/docs/github-copilot/llms-full.txt \
  -H "Accept: application/vnd.github.raw" --cache 1h

# AI Augmented SDLC only
gh api repos/dktunited/ai-augmented-development/contents/public/llms/docs/ai-augmented-sdlc/llms-full.txt \
  -H "Accept: application/vnd.github.raw" --cache 1h
```

The whole-site bundle already contains everything (all docs **and** all classic
pages), so prefer it and only reach for a per-product bundle to reduce size. Do
**not** read `index.json` or any other file to "discover" bundles — the two
paths above are the only `llms-full.txt` files that exist.

### Step 2 — Answer from the bundle

- Treat the fetched `llms-full.txt` as the authoritative content and answer directly from it.
- Each doc in the bundle is preceded by a `Source:` line with its canonical URL — cite that
  URL when you reference a specific page, but **do not fetch it** (it is login-gated).
- If the bundle does not cover the question, say so plainly rather than guessing or falling
  back to the link-only indexes.

## Notes

- The bundles are regenerated from the portal's content (Markdown docs plus the
  rendered React pages) on every build, and a CI check keeps the committed copies
  in sync, so what you read here matches the live site.
- Always fetch from the `main` branch (the default), which is what `gh api .../contents/...`
  returns unless you pass `?ref=`.
