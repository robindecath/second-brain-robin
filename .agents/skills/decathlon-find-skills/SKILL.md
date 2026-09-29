---
name: decathlon-find-skills
description: >
  Automatic, context-driven skill discovery for Decathlon. Two modes: Full Discovery
  (reads the project's architecture document, extracts technology signals, proposes ranked
  candidates, and installs on confirmation) and Quick Context Scan (lightweight, silent check
  against codebase artifacts — package.json, pom.xml, build.gradle, Package.swift, k8s manifests,
  etc. — that surfaces a one-line nudge when new relevant skills exist, without blocking or
  requiring an explicit ask). Both modes match against the curated skills.catalog.json registry
  and deduplicate against already-installed skills.
  Triggers on: "discover skills", "find skills", "suggest skills", "what skills should I install",
  "dkt-discover-project-skills", "scan for skills", "quick skill scan".
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  mcp_required: false
---

# Decathlon Automatic Skill Discovery

## Overview

This skill determines a project's technology stack and proposes relevant skills from the
Decathlon curated catalog (`skills.catalog.json`) — with minimal need for anyone to explicitly
ask for a specific skill by name.

Unlike generic skill finders that rely on keyword searches against the public internet,
this skill:
- Reads **actual project signals** — the architecture document and/or codebase artifacts —
  instead of relying on a user-typed query
- Matches against the **team-maintained `skills.catalog.json`**, fetched live from its single
  canonical source `dktunited/ai-augmented-sdlc@main` (requires an authenticated `gh` CLI and
  network access to the org)
- Filters out skills **already installed** (read from `skills-lock.json`, `_bmad/custom/skills.config.json`
  and `.agents/skills/`)
- Proposes candidates **grouped by category** with match rationale and install commands
- Runs `npx skills add` on confirmation, which updates the lock file (`skills-lock.json`)

## Two Modes

| | **Full Discovery Mode** | **Quick Context Scan Mode** |
|---|---|---|
| Trigger | Explicit invocation, or `bmad-architecture` `on_complete` | Automatic, silent, at the start of `bmad-build` and `bmad-code-review` activation |
| Signal source | The project's architecture document | Codebase artifacts (manifests, project files) — no architecture doc required |
| Output | Full ranked table grouped by category, with rationale and install commands | A single one-line nudge if new matches exist; nothing if none found |
| Blocking? | Yes — waits for user review of the candidate table | No — never interrupts the workflow, just leaves a short notice |
| Installs skills? | Only on explicit user confirmation | Never installs directly — always defers to Full Discovery or a manual run for the actual install step |

Both modes share the same catalog-matching logic (Steps 3–5 below). They differ in how
technology signals are gathered (Step 2) and how results are presented (Step 6).

## Conventions

- `{project-root}` resolves to the project's working directory (the consumer project, **not**
  the `dktunited/ai-augmented-sdlc` repository).
- `{skill-root}` resolves to this skill's installed directory — in a consumer project this is
  `{project-root}/.agents/skills/decathlon-find-skills/`.

A project set up through the AI Augmented SDLC canvas (or the Decathlon SDLC VS Code extension)
has this layout:

```
{project-root}/
├── _bmad/
│   └── custom/                    ← ai-augmented-sdlc-customizations-bmad extracted here
│       ├── bmad-agent-*.toml
│       ├── skills.config.json     ← real location of skills.config.json
│       └── modules/
├── .agents/
│   └── skills/<skill-name>/       ← full folder of each installed skill
│       ├── SKILL.md
│       └── scripts/, templates/…
├── _specs/
└── skills-lock.json               ← at the project root
```

Note what is **not** there: no `skills.catalog.json` and no `skills.config.json` at the project
root. The catalog is never vendored into a project — it is always fetched from GitHub (Step 3).

## On Activation

### Step 0: Determine the Mode

- If invoked explicitly by name, or from `bmad-architecture` `on_complete` → **Full Discovery Mode**.
- If invoked silently from `bmad-build` or `bmad-code-review` activation steps → **Quick Context Scan Mode**.
- If ambiguous, default to Full Discovery Mode and ask the user which they'd prefer.

### Step 1: Gather Signal Sources

**Full Discovery Mode** — locate the architecture document (see Step 1a below). This is
the primary signal source; codebase artifacts are optional supplements if the architecture
doc is thin on stack detail.

**Quick Context Scan Mode** — skip the architecture document search entirely (it may not
exist yet, and this mode must never block). Go directly to Step 1b (codebase artifact scan).

#### Step 1a: Locate the Architecture Document

Search for the architecture document under `{project-root}` in this order:

1. `docs/architecture.md`
2. `docs/arch.md`
3. `architecture.md`
4. Any file matching `docs/*architecture*.md` (glob)
5. Any file matching `docs/*arch*.md` (glob)
6. Any file in `docs/` whose name contains "architect" (case-insensitive)

If **no architecture document is found** (Full Discovery Mode only), stop and inform the user:
> "No architecture document was found in this project. Please run the `bmad-architecture`
> workflow to create one, or point me to your architecture document path."

If **multiple candidates** are found, present the list and ask the user to confirm which one
to use before proceeding.

If **no architecture document is found in Full Discovery Mode**, offer to fall back to a
codebase artifact scan (Step 1b) instead of stopping entirely — this gives the user a result
even without an architecture doc.

#### Step 1b: Scan Codebase Artifacts

Used in Quick Context Scan Mode always, and as a fallback/supplement in Full Discovery Mode.

Look for the following files under `{project-root}` (do not fail if some are missing — just
skip them):

| Artifact | Signals extracted |
|---|---|
| `package.json` | JS/TS, framework deps (react, next, astro, vue, svelte), `engines.node` |
| `pom.xml` | Java, Spring Boot version, parent POM, `<dependencies>` (e.g. spring-boot-starter-*) |
| `build.gradle` / `build.gradle.kts` | Java/Kotlin, Spring Boot, Android (`com.android.application` plugin) |
| `Package.swift` | Swift, target platforms (iOS/macOS/tvOS/watchOS/visionOS) |
| `*.xcodeproj` / `*.xcworkspace` | iOS/macOS/Apple platform |
| `AndroidManifest.xml` | Android |
| `go.mod` | Go |
| `requirements.txt` / `pyproject.toml` | Python |
| `Gemfile` | Ruby |
| Kubernetes manifests (`*.yaml`/`*.yml` with `kind: Deployment/StatefulSet/CronJob` etc., or a `k8s/`, `deploy/`, `charts/` directory) | Kubernetes/infrastructure |
| `docker-compose.yml` / `Dockerfile` | Containerization (weak signal, doesn't map to a specific catalog tag alone) |
| Presence of `.feature` files or a `tzatziki-*` dependency | BDD/Cucumber testing |
| Presence of FedID/OAuth2 config (`application.yml` with `oauth2`, `.env` with `FEDID`, etc.) | FedID/OAuth2 auth |

Produce the same normalized lowercase technology tag list as Step 2 would from an architecture
doc (e.g. `["java", "spring-boot", "kubernetes"]`).

### Step 2: Extract Technology Signals

Read the gathered sources (architecture document text, and/or codebase artifacts from Step 1b)
and extract all technology signals. Look for:

- **Languages**: Java, Go, Kotlin, Swift, TypeScript, JavaScript, Python, Rust, etc.
- **Frameworks**: Spring Boot, Next.js, Astro, React, Vue, Svelte, Quarkus, Micronaut, Jetpack Compose, SwiftUI, etc.
- **Platforms/runtimes**: Node.js, JVM, GraalVM, Vercel, Kubernetes, Android, iOS/macOS/tvOS/watchOS/visionOS, etc.
- **Integrations**: Datadog, FedID, AppReferential, OAuth2, REST APIs, gRPC, MCP servers, etc.
- **Patterns**: BDD/Cucumber, accessibility, SLO/SLI, API Gateway, E2E testing, etc.
- **Databases**: PostgreSQL, MySQL, MongoDB, Redis, etc. (may hint at backend stack)

Produce a normalized list of **technology tags** (lowercase, e.g. `["java", "spring-boot", "datadog", "oauth2", "fedid", "bdd"]`).

**Full Discovery Mode** — briefly tell the user what signals you extracted:
> "From the architecture document, I detected: Java, Spring Boot, FedID OAuth2, Datadog, and BDD testing."

**Quick Context Scan Mode** — do not narrate the signal extraction; it happens silently as
part of activation. Only the final nudge (Step 6) is visible to the user.

### Step 3: Load the Skill Catalog

The catalog is **not** present in a consumer project — do not look for it on disk. Its single
canonical source is `dktunited/ai-augmented-sdlc@main`, fetched live. This mirrors what the AI
Augmented SDLC canvas does (`src/copilot-extensions/decathlon-ai-augmented-sdlc/src/catalog.ts`):
a vendored snapshot goes stale the moment a PR updates the catalog, so there is deliberately no
copy shipped inside this skill.

**1. Primary — `gh api` with the raw media type** (handles the org's SSO/SAML automatically via
the stored token):

```bash
gh api "repos/dktunited/ai-augmented-sdlc/contents/skills.catalog.json?ref=main" \
  -H "Accept: application/vnd.github.raw"
```

⚠️ `Accept: application/vnd.github.raw` returns the raw file bytes. Do **not** pipe through
`--jq '.content' | base64 -d` — the response is already the JSON document.

**2. Fallback — `curl` with a token from `gh auth token`** (same fallback as `catalog.ts`):

```bash
curl -fsSL -H "Authorization: Bearer $(gh auth token)" \
  -H "Accept: application/vnd.github.raw" \
  "https://api.github.com/repos/dktunited/ai-augmented-sdlc/contents/skills.catalog.json?ref=main"
```

**3. If both fail** — never stay silent and never invent skills.

- **Full Discovery Mode** — stop and report an actionable error:
  > "Impossible de récupérer `skills.catalog.json` depuis `dktunited/ai-augmented-sdlc`.
  > Vérifie `gh auth status` et ton accès réseau à l'org (VPN/Zscaler). Je ne peux pas proposer
  > de skills sans le catalog — je ne vais pas en inventer."

- **Quick Context Scan Mode** — output **nothing at all** and let activation continue. This mode
  must stay silent and non-blocking, so a catalog fetch failure is swallowed rather than surfaced.

### Step 4: Load Installed Skills

Build the set of already-installed skill names by merging the sources below, in order. Each one
is optional — read what exists, skip what doesn't, and never fail if a file is missing.

1. **`{project-root}/skills-lock.json`** — the most reliable source (what is actually installed).
   The keys of its `skills` object are the skill names:
   ```json
   { "version": 1, "skills": { "blast-radius-analyzer": { "source": "dktunited/ai-augmented-sdlc" } } }
   ```
2. **`{project-root}/_bmad/custom/skills.config.json`** — skills declared for auto-install. It maps
   a repo (`"dktunited/agent-skills"`) to an array of skill names; ignore any key starting with `_`
   (e.g. `_migrations`, `_notes`), which is metadata, not a repo.
   Fallback for older setups: `{project-root}/skills.config.json`.
3. *(optional)* the directory names under **`{project-root}/.agents/skills/`** — each installed skill
   lives in its own folder there.

If none of them is found, continue **without** deduplication rather than failing — proposing an
already-installed skill is a much smaller problem than producing no result at all.

### Step 5: Match and Score Candidates

For each skill entry in every catalog category:

1. Compute a **match score**: count how many of the skill's `tech` tags appear in the
   extracted technology signals. Also check partial matches (e.g. "spring" matches "spring-boot").
2. Skip skills with a score of 0.
3. Skip skills already in the installed set (from Step 4).

Group remaining candidates by their catalog category, sorted by score descending within
each group.

### Step 6: Present Candidates

**Full Discovery Mode:**

If **no candidates** remain after filtering:
> "All relevant skills for this project's technology stack are already installed. 🎉"

Otherwise, render a table grouped by category. For each candidate include:

| Skill | Source | Match rationale | Install command |
|---|---|---|---|
| `spring-boot-fedid-resource-server` | `dktunited/agent-skills` | Java, Spring Boot, FedID, OAuth2 | `npx skills add dktunited/agent-skills --skill spring-boot-fedid-resource-server` |

After the table, add a summary line:
> "Found **N skill(s)** across **M category(ies)** matching your project's stack."

Proceed to Step 7 to offer installation.

**Quick Context Scan Mode:**

If **no candidates** remain after filtering, output nothing at all — stay completely silent
and let the workflow's normal activation continue.

If **one or more candidates** are found, output a single line and nothing else (no table, no
per-skill detail, no installation prompt):

> "💡 N relevant skills available for this stack — run skill discovery to review."

Do not proceed to Step 7 in this mode — Quick Context Scan never installs. If the user reacts
to the nudge and explicitly asks to review or install, switch to Full Discovery Mode
(re-run from Step 1a) to show the full table and offer confirmation.

### Step 7: Confirm and Install (Full Discovery Mode only)

Ask the user:
> "Would you like me to install all suggested skills? Running `npx skills add` for each
> will update the lock file (`skills-lock.json`), which you should commit to version control.
> Other developers will then get all skills automatically with `npm install`. You can also
> select specific skills to install, or skip this step and run the commands manually."

**If the user confirms all or a subset:**

1. For each selected skill, run:
   ```bash
   npx skills add <repo> --skill <skill> -y
   ```
   This updates `skills-lock.json` (or equivalent lock file managed by the skills CLI).
2. Report the result:
   ```
   ✅ spring-boot-fedid-resource-server  (dktunited/agent-skills)
   ✅ add-cucumber-tests                 (Decathlon/tzatziki)
   
   Lock file updated. Commit skills-lock.json so other developers get these skills on npm install.
   ```

**If the user declines:**
> "No changes made. You can install any skill later with:
> `npx skills add <repo> --skill <skill>`"

## Tips for Effective Matching

- The architecture document should describe technologies explicitly (e.g., "Spring Boot 3.x",
  "Next.js 15", "Go 1.22"). Vague descriptions reduce match quality.
- If the architecture covers multiple services with different stacks, extract signals from
  all services and propose skills for each detected technology.
- Skills in the `compliance` and `knowledge-graph` categories are broadly applicable —
  mention them if they are not already installed, regardless of stack.
- Codebase artifact scanning (Step 1b) is intentionally shallow and fast — it should complete
  in well under a second of reasoning and never read full file contents beyond what's needed
  to detect a signal (e.g. a grep for `spring-boot-starter` in `pom.xml`, not a full parse).
  Quick Context Scan Mode must stay lightweight enough to run on every `bmad-build` and
  `bmad-code-review` activation without adding noticeable latency.
- Quick Context Scan Mode must never write to `_bmad/custom/skills.config.json` or
  `skills-lock.json`, and must never run `npx skills add`. It only ever nudges — installation
  stays a deliberate, confirmed action performed via Full Discovery Mode. It also never surfaces
  a catalog fetch error (see Step 3).
