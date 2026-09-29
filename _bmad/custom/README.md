# AI Augmented SDLC - Customizations for BMAD agents & workflows

[Website](https://ai-augmented-development.decathlon.net/ai-augmented-sdlc)
[Project board](https://github.com/orgs/dktunited/projects/775)

This repository provides the **team-level customization bundle** for Decathlon’s AI-augmented SDLC setup, centered on BMAD agent behavior and shared Copilot configuration.

Its goal is to keep delivery teams aligned on a common engineering baseline by shipping:

1. **Agent customizations** for Analyst, PM, Architect, Dev, UX, and SRE roles (`bmad-agent-*.toml`), including operating principles, mandatory skill gates (e.g. the `ux-research` methodology gate on Analyst, PM, and UX Designer), and IDE execution/debug guidance (notably recommending `.vscode/tasks.json` and `.vscode/launch.json`, plus a `.github/github-app.yml` repository configuration for the GitHub Copilot App, for GitHub Copilot App and VS Code workflows on technical roles).
2. **Workflow customizations** for 8 BMAD workflows (`bmad-*.toml` at repo root), including workflow-specific activation steps, knowledge routing, and on-complete actions:
   - `bmad-brainstorming.toml` — Guided Ideation (asks explicit user consent, then archives finished brainstorming artefacts to `dktunited/brainstorming-artifacts` only if approved)
   - `bmad-prd.toml` — Product Requirements Document
   - `bmad-architecture.toml` — System Architecture Design
   - `bmad-create-epics-and-stories.toml` — Epic and Story Elaboration
   - `bmad-build.toml` — Implementation (the official Phase 4 loop as of BMAD-METHOD 6.11.0)
   - `bmad-sprint-planning.toml` — Sprint Planning & Prioritization, **including the implementation-readiness gate**
   - `bmad-code-review.toml` — Code Review & Quality Assurance
   - `bmad-ux.toml` — UX/UI Design (also enforces the `ux-research` methodology gate — see [CUSTOMIZATION_STRATEGY.md](./docs/CUSTOMIZATION_STRATEGY.md#ux-research-customization-ux-research))

   > **BMAD-METHOD 6.11.0 alignment.** The official implementation chain is now
   > `bmad-sprint-planning` → `bmad-build` → `bmad-code-review`.
   > `bmad-check-implementation-readiness` was removed upstream and folded into
   > `bmad-sprint-planning`, which opens with a PASS / CONCERNS / FAIL readiness
   > gate — readiness is no longer its own skill, so it is no longer its own
   > override file. `bmad-dev-story`, `bmad-create-story`, `bmad-quick-dev` and
   > `bmad-create-architecture` are now forwarding shims under `v6-shims/` and
   > will be dropped at the v7 cut; this bundle targets their replacements
   > directly. Project context is centred on a verified block in `AGENTS.md`
   > produced by the new `bmad-project-context` skill, with a legacy
   > `project-context.md` still read as a source during the migration.
   > Rendered BMAD skills now require `uv` with Python 3.11+.
3. **Shared platform configuration** (`config.toml`, `skills.config.json`, `tools.config.json`) defining required skills and tooling prerequisites.
4. **Skills catalog** (`skills.catalog.json`) with 150+ available skills, organized by domain for skill discovery and recommendation.
5. **A release artifact pipeline** (`.github/workflows/release.yml`) that packages these customizations into `customizations.zip` for automated consumption during project setup.
6. **Comprehensive benchmark tests** for each agent (`tests/bmad-agent-*/`) and workflow (`tests/bmad-*/`) that validate persona adoption, principle enforcement, skill routing, and knowledge source activation using the [AI Observer](https://github.com/dktunited/ai-observer) benchmark engine.

## Testing the Customizations

### Understanding Agent vs Workflow Customizations

Before testing, it's important to understand how agent and workflow customizations work together.

**See [CUSTOMIZATION_STRATEGY.md](./docs/CUSTOMIZATION_STRATEGY.md) for a detailed explanation of:**
- Why we have both agent AND workflow customizations (they're not redundant)
- How the 3-layer TOML merge model works
- When to use each type of customization
- Skill routing patterns (mandatory gates vs conditional sources)

**TL;DR:** Agents define global persona principles; workflows add phase-specific guidance. Both are necessary.

---

Each agent customization ships with a benchmark that validates:
- **Persona adoption**: name, title, and icon from the resolved TOML merge
- **Principle enforcement**: mandatory skill invocations (Tech Radar, Tech Compliance, KG lookup)
- **Sub-skill routing**: correct skill selected for each scenario

Each workflow customization ships with a benchmark that validates:
- **Activation steps**: correct skills invoked at workflow start
- **Persistent facts**: phase-specific knowledge applied
- **External sources**: conditional routing (on-demand, not always invoked)
- **On-complete actions**: proper workflow finalization steps

**See [TESTING.md](./TESTING.md) for comprehensive testing guidance.**

### Running Tests

There are two ways to run tests:

### 1. Single Agent (Detailed Analysis)

For deep testing of one agent with detailed output:

```bash
make test-benchmark                # Run bmad-agent-architect
```

See [TESTING.md](./TESTING.md) for comprehensive single-agent testing guide.

### 2. All Agents (Test Suite)

For quick validation across all 5 agents with zero manual config:

```bash
make test-all                       # Sequential (~30-40 min)
make test-all-parallel              # Parallel (~10-15 min)
make test-agent-dev                 # Specific agent
```

**No environment variable configuration needed!**

The test suite auto-discovers all benchmarks and sets up environments automatically.

See [TESTING-SUITE.md](./TESTING-SUITE.md) for comprehensive multi-agent testing guide.

### Prerequisites

Install the `benchmark` binary from [ai-observer releases](https://github.com/dktunited/ai-observer/releases):

```bash
# macOS (Apple Silicon)
gh release download --repo dktunited/ai-observer --pattern "benchmark_darwin_arm64.tar.gz" -O - | tar xz && chmod +x benchmark && sudo mv benchmark /usr/local/bin/
```

Configure an LLM endpoint:

```bash
export LLM_ENDPOINT=https://openrouter.ai/api/v1/chat/completions
export LLM_API_KEY=sk-or-v1-...
# Or use the Copilot proxy: see https://github.com/dktunited/ai-observer docs
```

### Run All Benchmarks (Original Stub Method)

For offline testing without a BMAD installation (uses stub skills):

```bash
# All top-level agent benchmarks (offline, stubs)
for cfg in tests/*/; do
  agent=$(basename "$cfg")
  echo "▶ $agent"
  benchmark run --config "${cfg}${agent}-benchmark.yml"
done

# SRE module benchmark (full module with SKILL.md)
benchmark run --config modules/sre-platform/bmad-agent-sre/tests/bmad-agent-sre-benchmark.yml
```

### Comparing Models (Adherence Benchmark)

Every `tests/*-benchmark.yml` hardcodes `model: copilot/claude-haiku-4.5`. Since
`persistent_facts`/`activation_steps`/`principles` are natural-language directives
(not enforced code), a cheaper model can silently drop them even though a benchmark
written against a stronger model passes cleanly. `scripts/run-model-comparison.sh`
runs the existing benchmark suite across a configurable list of models and reports a
benchmark × model pass-rate matrix, so you can decide — with data — whether a given
model should be trusted for a given phase or discarded:

```bash
export LLM_ENDPOINT=http://localhost:29080/v1/chat/completions   # or your OpenRouter endpoint
export LLM_API_KEY=not-used
export BMAD_PROJECT=/path/to/a/real/bmad/project   # needs .agents/skills + _bmad/scripts

scripts/run-model-comparison.sh                        # all benchmarks, default model list
scripts/run-model-comparison.sh bmad-agent-architect    # just one benchmark
MODELS="claude-haiku-4.5,gpt-5-mini" scripts/run-model-comparison.sh
```

Default model list is cheap/mid-tier only (`claude-haiku-4.5`, `claude-sonnet-4.5`,
`gpt-5-mini`, `gpt-5.4-mini`, `gemini-3.5-flash`) — override with `MODELS` to include
others. If using the Copilot proxy, start it **without** a pinned `COPILOT_MODEL` env
var so each benchmark's `model:` field is honored per request.

> **Known limitation:** the workflow-level stub skills under `tests/*/stubs/bmad-*-workflow.skill.yml`
> currently ship as placeholders (`name`/`description` only) and fail to load under the
> current AI Observer skill schema, independent of which model is used — so workflow
> benchmarks (`bmad-prd`, `bmad-architecture`, `bmad-ux`, etc.) will show `0/N`
> for every model until those stubs are filled in with real `instructions`. The
> `bmad-agent-*` benchmarks have complete stubs today and give a meaningful comparison
> out of the box.

### Test Structure

```
tests/
  bmad-agent-dev/
    bmad-agent-dev-benchmark.yml      ← agent benchmark
    stubs/                             ← offline stub skills
  bmad-agent-pm/
    bmad-agent-pm-benchmark.yml
    stubs/
  bmad-agent-architect/
    bmad-agent-architect-benchmark.yml
    stubs/
  bmad-agent-ux-designer/
    bmad-agent-ux-designer-benchmark.yml
    stubs/
  bmad-prd/
    bmad-prd-benchmark.yml            ← workflow benchmark
    stubs/
  bmad-architecture/
    bmad-architecture-benchmark.yml
    stubs/
  bmad-build/
    bmad-build-benchmark.yml
    stubs/
  bmad-sprint-planning/
    bmad-sprint-planning-benchmark.yml   ← incl. the readiness-gate cases
    stubs/
  bmad-code-review/
    bmad-code-review-benchmark.yml
    stubs/
  bmad-create-epics-and-stories/
    bmad-create-epics-and-stories-benchmark.yml
    stubs/
  bmad-ux/
    bmad-ux-benchmark.yml
    stubs/
modules/sre-platform/bmad-agent-sre/
  tests/
    bmad-agent-sre-benchmark.yml      ← SRE full module benchmark
    stubs/

```

**Total:** 4 agent benchmarks + 7 workflow benchmarks = 11 comprehensive test suites
(plus the `bmad-prd-conditional`, `bmad-merge-validation` and `comparative-routing`
diagnostic suites, and the SRE module benchmark)

For a full guide on the testing methodology, see the [BMAD Customization Testing](https://ai-augmented-development.decathlon.net/ai-augmented-sdlc/guide/bmad-customization-testing) page in the AI Observer docs.

---

## Third-party software & trademarks

These customizations are layered on top of
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) (MIT License, © 2025
BMad Code, LLC) through its documented customization and custom-module mechanisms.
BMAD is not vendored here — this repository ships Decathlon-authored TOML overrides,
personas and modules only.

BMad™, BMad Method™, BMad Core™ and BMad Code™ are trademarks of BMad Code, LLC and are
not covered by the MIT License. **Decathlon is not affiliated with, endorsed by, or
certified by BMad Code, LLC, and this is not an official BMad module or distribution** —
the repository name and the `bmad-*` file and command prefixes are descriptive, identifying
which upstream agent or workflow each file customizes.

See [`NOTICE.md`](./NOTICE.md) for the full attribution.
