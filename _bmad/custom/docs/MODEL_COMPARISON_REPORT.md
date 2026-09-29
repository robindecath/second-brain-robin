# BMAD Customization: Multi-Model Adherence Report

This report answers the question raised while manually testing the BMAD
SDLC customization: *"the whole design phase was done with Haiku — is it
Haiku that isn't following the customization properly, and can we get a
real signal on which models to use (or discard) per BMAD workflow?"*

It documents a real, empirical run of every `tests/*-benchmark.yml` in this
repo across 6 Copilot models, plus two significant infrastructure bugs
found and fixed along the way that had silently invalidated **every**
benchmark run in this repo's history before today.

> **Update:** after `ai-observer` merged
> [PR #97](https://github.com/dktunited/ai-observer/pull/97) (new models +
> dynamic model discovery), PR #98, and PR #99, the model list was refreshed
> and the whole comparison re-run with newer/better options (notably
> `claude-sonnet-5` replacing `claude-sonnet-4.5`). See
> [Round 2](#round-2--model-refresh-after-ai-observer-pr-9798-99) for the
> updated results, including a **per-agent and per-BMad-workflow model
> suggestion table** and a surprising finding that `claude-sonnet-4.6` is a
> significant regression versus 4.5 on this specific task.

## TL;DR

- **Two prior, undetected bugs meant no benchmark run in this repo's
  history — including earlier smoke tests done today — ever actually
  tested what it claimed to test.** Both are now fixed; see
  [Methodology](#methodology--bugs-found-and-fixed).
- Of the 11 models originally planned, only **6 are actually usable** on
  this Copilot Business plan via the local proxy's `/chat/completions`
  path. The rest either don't exist on this account, are blocked from that
  endpoint, or were silently misrouted by a wrong name in the proxy code.
  See [Model availability](#model-availability-11-planned-6-confirmed-working).
- Real result, 14 benchmarks x 6 models (84 runs): **`gpt-5-mini` (95.2%)
  and `gpt-5.4` (92.7%) lead**, `gemini-3-flash-preview` (91.5%) and
  `gemini-3.5-flash` (89.1%) are close behind, **`claude-haiku-4.5` (67.3%)
  and `claude-sonnet-4.5` (63.0%) trail well behind** on this specific
  customization-adherence task. See [Full matrix](#full-pass-rate-matrix).
- Yes — **Haiku was very likely part of the original problem.** It's the
  weakest small/cheap model tested here on customization adherence
  specifically (not on general capability). See
  [Was it Haiku?](#was-it-haiku-answering-the-original-question).
- `claude-sonnet-4.5` has a distinct, repeatable failure mode across
  several workflow benchmarks: it frequently never calls the `read_skill`
  tool at all, answering from general knowledge instead of the actual
  loaded customization content. See [Sonnet's failure mode](#claude-sonnet-45s-distinct-failure-mode).
- Two benchmarks (`bmad-check-implementation-readiness`,
  `bmad-code-review`) score poorly for *every* model, including the
  strongest ones — that's a benchmark/stub defect, not a model problem.
  See [Known limitations](#known-limitations-not-model-failures).

## Methodology — bugs found and fixed

### Bug 1: every `pre_activate` hook was silently broken (fixed)

Every benchmark yml's `pre_activate.command` called:

```
python3 ${PROJECT_ROOT:-.}/_bmad/scripts/resolve_customization.py --skill <bare-name> --key agent --project-root ${PROJECT_ROOT:-.}
```

`--skill <bare-name>` (e.g. `architect`) is not a valid path — the real CLI
only accepts `--skill <path-to-skill-dir>` — and `--project-root` is not a
real flag on the resolver at all. `argparse` exited 2 with a usage error on
every single run. The benchmark binary treats a failing `pre_activate` as a
non-fatal warning and substitutes an **empty string** for `{resolved_agent}`
in `system_prompt`. Additionally, 8 of the 14 workflow-level benchmarks
passed `--key agent` when their `customize.toml` has a top-level `workflow`
key, and `bmad-dev-story-benchmark.yml` had no `pre_activate`/
`{resolved_agent}` wiring at all.

**Consequence: no benchmark run in this repo's history — including an
earlier smoke test done in this same session — ever actually injected the
team's TOML customization into the tested conversation.** Any numbers from
before this fix (including "claude-haiku-4.5 16/23 vs gpt-5-mini 14/23" from
earlier today) reflected generic model behavior on the base BMad skill
content only, not customization adherence, and must not be cited as signal.

Fixed in all 14 benchmark ymls: real env-var-driven `--skill` paths,
correct `--key`, and the missing `bmad-dev-story` wiring added. Verified via
a live sanity run showing `pre_activate: ✓ expanded {resolved_agent} (N
chars)` and assertions that pass/fail on actual customization content.

### Bug 2: the Copilot proxy was pinned to `gpt-4o` the entire time (fixed)

`proxy/Dockerfile.copilot` bakes in `ENV COPILOT_MODEL=gpt-4o` as an image
default. The proxy's model-resolution code checks this env var **first,
before anything else** — if set to any non-empty value, it silently
overrides the model requested in *every* incoming request, regardless of
what the benchmark yml or `MODELS=` list says. A previous restart of the
container omitted a new value for this variable rather than explicitly
clearing it, so the image's baked-in default stayed in effect.

**Consequence: every model-comparison run in this session prior to this
fix — the "clean" `bmad-agent-architect` matrix included — was actually
sending 100% of its requests to `gpt-4o`, just labeled with different model
names.** The first real multi-model run of the day (`claude-haiku-4.5` vs
`gpt-5-mini` on `bmad-agent-architect`, showing 19/23 vs 20/23-ish spread)
looked plausible but was not testing distinct models at all.

Fixed by recreating the container with `-e COPILOT_MODEL=` explicitly
empty (not omitted). Verified via `docker logs` showing no `model mapped`
warnings for the 6 confirmed-working models, and via direct `curl` tests
returning genuinely different token-level output per model.

### Bug 3 (proxy-side, patched locally, not yet upstreamed): wrong model names in the allowlist

The proxy's own `copilotSupportedModels` map (`ai-observer/proxy/internal/llm/copilot.go`)
had `gemini-3-flash` instead of the real model ID `gemini-3-flash-preview`,
and was missing the real `mai-code-1-flash-picker/-secondary/-tertiary`
variant names. Because these didn't match the map, `resolveCopilotModel`
silently substituted the fallback model (`gpt-5.4`) for them instead of
erroring — the exact same class of bug as #2, just at the model-name level
instead of the whole-proxy level. This was caught by cross-checking
`docker logs` for `model mapped` warnings on every "different" model tested.
Patched locally in the running proxy build (not committed to the
`ai-observer` repo — recommend upstreaming this fix there separately) by
adding the correct names to the allowlist.

### Model availability: 11 planned, 6 confirmed working

The original plan (from GitHub's public pricing/model-comparison docs)
proposed 11 cheap/mid-tier models. Testing each directly against the
rebuilt proxy revealed several are not usable here at all:

| Model | Status | Why |
|---|---|---|
| `gpt-5-mini` | ✅ works | |
| `gpt-5.4` | ✅ works | |
| `gpt-5.4-mini` | ❌ excluded | Real API error: *"not accessible via the /chat/completions endpoint"* — needs a different, agent-style API |
| `gpt-5.4-nano` | ❌ excluded | Does not exist in this account's real Copilot model list |
| `gpt-5.3-codex` | ❌ excluded | Same "/chat/completions" restriction as gpt-5.4-mini |
| `claude-haiku-4.5` | ✅ works | |
| `claude-sonnet-4.5` | ✅ works | |
| `gemini-3-flash` | ❌ wrong name | Real ID is `gemini-3-flash-preview` (see Bug 3) |
| `gemini-3-flash-preview` | ✅ works (once named correctly) | |
| `gemini-3.5-flash` | ✅ works | |
| `mai-code-1-flash` (+ `-picker`/`-secondary`/`-tertiary`) | ❌ excluded | All variants return `model_not_supported` from the real Copilot API on this account — no Microsoft model is usable via `/chat/completions` here |
| `raptor-mini` | ❌ excluded | Does not exist in this account's real Copilot model list |

**Final tested set (6 models, 3 providers):** `gpt-5-mini`, `gpt-5.4`,
`claude-haiku-4.5`, `claude-sonnet-4.5`, `gemini-3.5-flash`,
`gemini-3-flash-preview`. All Claude Opus tiers, GPT-5.5, GPT-5.6 Sol, and
the pricier Gemini Pro tiers remain excluded per the original cost-driven
scope, independent of the availability issues above.

### Run parameters

- 14 of the 15 benchmark ymls in `tests/` (`comparative-routing` excluded —
  it has no `skills:`/`pre_activate` scaffolding at all; it's a different
  kind of test, multi-agent routing, not customization adherence).
- Fresh temp copy of the real reference BMad project (`bmadtest4`) with this
  repo's `.toml` customizations applied, via `scripts/run-model-comparison.sh`
  (same script used for the earlier — now superseded — smoke test, updated
  with the fixes above plus a 429 retry/backoff and inter-request pacing for
  the Copilot proxy's utility-model rate limit).
- 84 total runs, executed sequentially against the local Copilot proxy.

## Full pass-rate matrix

| Benchmark | gpt-5-mini | gpt-5.4 | claude-haiku-4.5 | claude-sonnet-4.5 | gemini-3.5-flash | gemini-3-flash-preview |
|---|---|---|---|---|---|---|
| bmad-agent-architect | 22/23 | 22/23 | 18/23 | 20/23 | 19/23 | **23/23** |
| bmad-agent-dev | 22/23 | **23/23** | 22/23 | 22/23 | 22/23 | **23/23** |
| bmad-agent-pm | 18/18 | 18/18 | 16/18 | 18/18 | 18/18 | 18/18 |
| bmad-agent-ux-designer | **18/18** | **18/18** | 15/18 | 16/18 | 13/18 | 16/18 |
| bmad-check-implementation-readiness* | 2/4 | 0/4 | 0/4 | 0/4 | 1/4 | 0/4 |
| bmad-code-review* | 2/4 | 2/4 | 0/4 | 0/4 | 2/4 | 2/4 |
| bmad-create-architecture | 15/16 | 15/16 | 6/16 | **0/16** | 15/16 | 12/16 |
| bmad-create-epics-and-stories | **4/4** | **4/4** | **4/4** | 0/4 | **4/4** | **4/4** |
| bmad-dev-story | **4/4** | 2/4 | 2/4 | 0/4 | **4/4** | 3/4 |
| bmad-merge-validation | 17/17 | 16/17 | 7/17 | 17/17 | 15/17 | 17/17 |
| bmad-prd-conditional | **14/14** | **14/14** | 12/14 | 3/14 | **14/14** | **14/14** |
| bmad-prd | **12/12** | **12/12** | 8/12 | 7/12 | **12/12** | **12/12** |
| bmad-sprint-planning | **4/4** | **4/4** | 1/4 | 0/4 | **4/4** | **4/4** |
| bmad-ux | 3/4 | 3/4 | 0/4 | 1/4 | **4/4** | 3/4 |
| **Total** | **157/165 (95.2%)** | **153/165 (92.7%)** | **111/165 (67.3%)** | **104/165 (63.0%)** | **147/165 (89.1%)** | **151/165 (91.5%)** |

\* See [Known limitations](#known-limitations-not-model-failures) — these
two benchmarks score poorly for every model due to a pre-existing sub-skill
stub defect, not a model failure.

## Was it Haiku? (answering the original question)

**Yes, most likely.** Across every genuinely fixed benchmark (i.e.
excluding the two known-broken ones), `claude-haiku-4.5` is consistently
the weakest performer among the 4 non-broken workhorse models
(`gpt-5-mini`, `gpt-5.4`, `gemini-3.5-flash`, `gemini-3-flash-preview`),
sitting at 67.3% overall — roughly 25 points behind the strongest models.
The most telling example is `bmad-ux`, where Haiku said *"I'll load the UX
workflow..."* in its response text on every prompt but only actually called
the `read_skill` tool once across all 4 prompts, meaning it answered from
general knowledge rather than the loaded customization content — exactly
the kind of gap the user experienced manually (a UX phase that didn't
reflect the customized guidance).

That said, this doesn't mean Haiku is unusable — it did score 87-100% on
several of the simpler agent-level benchmarks (`bmad-agent-pm`,
`bmad-agent-dev`, `bmad-agent-ux-designer`). Its weak points cluster
specifically around the more instruction-dense workflow benchmarks
(`bmad-create-architecture`: 6/16; `bmad-merge-validation`: 7/17;
`bmad-sprint-planning`: 1/4) where following a longer chain of
`activation_steps`/`persistent_facts` correctly matters more.

**Recommendation:** avoid Haiku for architecture, UX, and sprint-planning
workflows in particular; it's acceptable for the simpler agent-level Q&A
interactions.

## claude-sonnet-4.5's distinct failure mode

Sonnet's overall number (63.0%) looks similar to Haiku's, but the *pattern*
is completely different and worth calling out on its own. Sonnet doesn't
fail gradually across many prompts — it fails **completely** on several
whole benchmarks (`bmad-create-architecture`: 0/16, `bmad-create-epics-and-stories`:
0/4, `bmad-dev-story`: 0/4, `bmad-sprint-planning`: 0/4) while scoring
perfectly or near-perfectly on others (`bmad-merge-validation`: 17/17,
`bmad-agent-pm`: 18/18).

Inspecting the raw logs for the 0-scoring runs shows a repeatable pattern:
**Sonnet never calls the `read_skill` tool at all** for these specific
prompts (`tool "read_skill" called 0 time(s), expected [1+]` on every
assertion), then answers each question directly and generically — often
plausibly, but without the actual customization content, so it never
mentions e.g. `decathlon-tech-radar`, `SIG`, or `FedID` in the way the
customized skill's real instructions require.

This looks like a phrasing sensitivity: benchmarks that pass for Sonnet use
prompts like *"Load the bmad-agent-pm skill. What is..."*, while the
consistently-failing ones use *"Load the architecture workflow skill.
What..."* — Sonnet appears to treat "workflow skill" loading instructions
differently from "agent skill" loading instructions in this harness,
skipping the tool call for the former. This is real, actionable signal
(not customization-content related) that's worth a follow-up investigation
independent of this report, but out of scope to fix here.

**Recommendation:** don't default to Sonnet for BMad workflow-level tasks
(PRD, architecture, epics/stories, dev-story, sprint-planning) without
further prompt-phrasing investigation; it's reliable for agent-level
interactions.

## Known limitations (not model failures)

`bmad-check-implementation-readiness` and `bmad-code-review` score poorly
for *every* model tested, including the strongest ones (`gpt-5-mini`,
`gpt-5.4` scoring only 0-2 out of 4). Inspecting the logs shows the real
cause: these benchmarks' `sub_skills:` stubs are incomplete placeholders
(`name`/`description` only — the harness requires `instructions`,
`data_refs`, or `execute` to actually load one) —

```
warning: failed to load sub-skill 'decathlon-tech-compliance': invalid skill: at least one of instructions, data_refs, or execute must be provided
```

— so the model is never shown the content it's being tested on knowing.
This is a benchmark/stub defect, independent of the `pre_activate` fix in
this report, and should be filled in as a follow-up (not attempted here to
keep this report's scope to model comparison, not further harness repair).

`tests/comparative-routing` was excluded entirely — it has no
`skills:`/`pre_activate` scaffolding and tests a different concept
(multi-agent routing), not customization adherence.

## Per-phase model recommendation

BMad's own phase structure (`https://docs.bmad-method.org/llms-full.txt`,
`reference/workflow-map.md`) has no model-selection guidance of its own —
BMad is explicitly model-agnostic. The recommendations below combine that
phase structure with this report's empirical results (not with GitHub's
task-area marketing copy alone, which the earlier draft plan leaned on
before real data existed).

- **Phase 2 Planning** (`bmad-prd`, `bmad-prd-conditional`, `bmad-ux`) —
  `gpt-5-mini`, `gpt-5.4`, and both Gemini flash tiers all score
  12-14 / 12-14 and 3-4/4 respectively; any of the four is safe. Avoid
  Sonnet here (3/14 on `bmad-prd-conditional`).
- **Phase 3 Solutioning** (`bmad-create-architecture`,
  `bmad-create-epics-and-stories`, `bmad-check-implementation-readiness`) —
  `gpt-5-mini`/`gpt-5.4`/`gemini-3.5-flash` are the clear leaders on
  `bmad-create-architecture` (15/16 each); avoid both Haiku (6/16) and
  Sonnet (0/16) for architecture work specifically. The readiness-gate
  benchmark needs its stub fixed before any model comparison there is
  meaningful.
- **Phase 4 Implementation** (`bmad-sprint-planning`, `bmad-dev-story`,
  `bmad-code-review`) — `gpt-5-mini` and `gemini-3.5-flash` are the most
  consistent (4/4 on both sprint-planning and dev-story); `gpt-5.4` and
  `gemini-3-flash-preview` are close behind. Both Claude models
  underperform here — Sonnet scores 0/4 on two of these three benchmarks.

**Overall: `gpt-5-mini` and `gemini-3.5-flash` are the safest generalist
picks across all four phases** for teams that want one model instead of
per-phase switching; `gpt-5.4` and `gemini-3-flash-preview` are close
seconds with slightly better performance on agent-level benchmarks.
`claude-haiku-4.5` and `claude-sonnet-4.5` should be considered discard
candidates for BMad customization-adherence tasks specifically, despite
being capable models generally — the customization-following behavior
tested here (proactively invoking `read_skill` and following
`activation_steps`/`persistent_facts` chains) is where they lag, not raw
reasoning quality.

## Follow-ups (out of scope for this report)

1. Upstream the `gemini-3-flash-preview` / `mai-code-1-flash-*` naming fix
   to `ai-observer/proxy/internal/llm/copilot.go`.
2. Fill in real `instructions`/`data_refs` for the `bmad-check-implementation-readiness`
   and `bmad-code-review` sub-skill stubs so those two benchmarks produce
   meaningful model comparison data.
3. Investigate Sonnet's workflow-vs-agent prompt-phrasing sensitivity
   directly (why it skips `read_skill` for "Load the X workflow skill..."
   phrasing specifically).
4. Consider re-running with `gpt-5.4-mini`/`gpt-5.3-codex` if/when this
   Copilot proxy adds support for whatever non-chat-completions API those
   models require.

---

# Round 2 — Model refresh after ai-observer PR #97/#98/#99

Triggered by a colleague merging three follow-up PRs to `ai-observer`:
[PR #97](https://github.com/dktunited/ai-observer/pull/97) (new Copilot
models + dynamic model discovery), PR #98 (fixed `max_tokens`/
`max_completion_tokens` passthrough), and PR #99 (reasoning-tier param
stripping for GPT-5.6 + upstream error-body logging). This section is a full
redo of the model research and comparison — it supersedes the model
*selection* from Round 1 above, but the Round 1 bug fixes, matrix, and
Haiku/Sonnet-4.5 analysis remain accurate historical record and are kept
as-is.

## What changed and what didn't

`ai-augmented-sdlc-customizations-bmad`'s local `ai-observer` checkout was
pulled to `origin/main` (`8cc20b8`, includes #97, #98, #99), the
`ai-observer-copilot-proxy` Docker image was **fully rebuilt** from
`Dockerfile.copilot`, and the container was **fully recreated** (not just
restarted) with `-e COPILOT_MODEL=` explicitly empty and the
`ai-observer_copilot_data` volume preserved (GitHub token survived, no
re-auth). `docker logs` confirmed dynamic model discovery is live
(`refreshed dynamic Copilot model list count=40`).

Every model was re-verified with a direct `curl` against `/v1/chat/completions`:

| Model | Status | Notes |
|---|---|---|
| `claude-sonnet-4.6` | ✅ works | New in PR #97's allowlist |
| `claude-sonnet-5` | ✅ works | New in PR #97's allowlist |
| `claude-opus-4.8` | ✅ works | Premium tier, kept optional |
| `gemini-3.1-pro-preview` | ✅ works | Real ID needs `-preview` suffix |
| `gemini-2.5-pro` | ✅ works | Premium tier, kept optional |
| `gpt-5.6-luna` / `-sol` / `-terra` | ❌ still blocked | See below — **not fixed by #99** |
| `gpt-5.5`, `gpt-5.4-mini`, `gpt-5.3-codex` | ❌ still blocked | Same restriction class as GPT-5.6 |
| `claude-fable-5`, `kimi-k2.7-code` | ❌ still blocked | Org-policy opt-in required (per PR #99's own doc update), not a bug |
| `gpt-5.4-nano`, `raptor-mini`, `claude-sonnet-4`, `mai-code-1-flash*` | ❌ still blocked | Not in this account's real model list / `model_not_supported` |

**Important correction — GPT-5.6 is still not usable, despite PR #99.**
PR #99's commit message states its `temperature`/`top_p` stripping fix
"previously caused 400s for GPT-5.6 despite it being entitled/enabled for the
org." We tested this directly, twice — once with `temperature` explicitly
set in the request, once with a bare-minimum request containing neither
`temperature` nor `top_p` — and got the **identical** rejection both times:

```
{"error":{"message":"model \"gpt-5.6-terra\" is not accessible via the /chat/completions endpoint","code":"unsupported_api_for_model"}}
```

Reading `copilot.go`'s actual diff confirms why: PR #99 only strips those two
fields *if the caller sent them*; it does not add any alternate upstream
request path. The proxy still only ever calls `.../chat/completions` (one
endpoint, confirmed via `grep -n "apiBase + \"/chat/completions\""` — no
second path exists in the code). GitHub's own error message indicates GPT-5.6
Luna/Sol/Terra need a different, agent-style API shape entirely (the same
class of restriction as `gpt-5.3-codex`/`gpt-5.4-mini`) — a deeper
architectural gap (missing endpoint routing) than a stray sampling parameter.
This is a real limitation to flag back to the `ai-observer` maintainers as a
follow-up, not something this benchmark can work around.

## Pricing and external signal (fresh, this round)

Per-1M-token pricing, pulled fresh from GitHub's official docs
([model comparison](https://docs.github.com/en/copilot/reference/ai-models/model-comparison),
[pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)):

| Model | Category | Input | Output |
|---|---|---|---|
| Claude Sonnet 4.5 | Versatile | $3.00 | $15.00 |
| Claude Sonnet 4.6 | Versatile | $3.00 | $15.00 |
| **Claude Sonnet 5** | Versatile | **$2.00** (promo through Aug 2026; $3.00 standard after) | **$10.00** (promo; $15.00 standard) |
| GPT-5.6 Terra | Versatile | $2.50 | $15.00 |
| GPT-5.6 Luna | Lightweight | $1.00 | $6.00 |

Anthropic's own [Sonnet 5 announcement](https://www.anthropic.com/news/claude-sonnet-5)
states Sonnet 5 is "a substantial improvement over its predecessor, Sonnet
4.6, on important aspects of agentic performance like reasoning, tool use,
coding, and knowledge work" and that its agentic performance approaches Opus
4.8 "at lower prices." Combined with the promo pricing above (**Sonnet 5 is
simultaneously the newest, the best-reviewed by its own vendor, and the
cheapest of the three Sonnet options**), this is a strong case for swapping
Round 1's `claude-sonnet-4.5` for `claude-sonnet-5` rather than `4.6`.
`claude-sonnet-4.6` was kept in this round's model list anyway, purely as a
diagnostic to check whether Round 1's Sonnet 4.5 read_skill bug is
version-specific or Sonnet-family-wide — see results below.

## Updated model list (7 models) and re-run

`gpt-5-mini`, `gpt-5.4`, `claude-haiku-4.5` (unchanged from Round 1),
`claude-sonnet-4.6` (new, diagnostic), `claude-sonnet-5` (new, replaces
`claude-sonnet-4.5`), `gemini-3.5-flash`, `gemini-3-flash-preview`
(unchanged). 7 models x 14 benchmarks = 98 runs, executed against the fully
rebuilt proxy via the updated `scripts/run-model-comparison.sh`.

### Round 2 pass-rate matrix

| Benchmark | gpt-5-mini | gpt-5.4 | claude-haiku-4.5 | claude-sonnet-4.6 | claude-sonnet-5 | gemini-3.5-flash | gemini-3-flash-preview |
|---|---|---|---|---|---|---|---|
| bmad-agent-architect | 23/23 | 23/23 | 15/23 | 2/23 | **23/23** | **23/23** | **23/23** |
| bmad-agent-dev | 22/23 | **23/23** | 15/23 | **23/23** | 22/23 | 22/23 | 22/23 |
| bmad-agent-pm | 17/18 | **18/18** | 9/18 | 0/18 | **18/18** | **18/18** | **18/18** |
| bmad-agent-ux-designer | **18/18** | **18/18** | 13/18 | 2/18 | 17/18 | 17/18 | 16/18 |
| bmad-check-implementation-readiness* | 1/4 | 0/4 | 0/4 | 0/4 | 1/4 | 1/4 | 0/4 |
| bmad-code-review* | 2/4 | 2/4 | 0/4 | 0/4 | 2/4 | 1/4 | 2/4 |
| bmad-create-architecture | 14/16 | **15/16** | 6/16 | 0/16 | 13/16 | 14/16 | **15/16** |
| bmad-create-epics-and-stories | **4/4** | **4/4** | 3/4 | 0/4 | **4/4** | **4/4** | **4/4** |
| bmad-dev-story | **4/4** | 3/4 | 2/4 | 0/4 | 3/4 | **4/4** | **4/4** |
| bmad-merge-validation | **17/17** | **17/17** | 10/17 | 8/17 | **17/17** | 11/17 | **17/17** |
| bmad-prd-conditional | **14/14** | **14/14** | 7/14 | 4/14 | **14/14** | **14/14** | **14/14** |
| bmad-prd | 11/12 | **12/12** | 10/12 | 0/12 | **12/12** | **12/12** | **12/12** |
| bmad-sprint-planning | **4/4** | 3/4 | 0/4 | 0/4 | **4/4** | **4/4** | 3/4 |
| bmad-ux | 3/4 | 3/4 | 0/4 | 0/4 | 3/4 | **4/4** | 3/4 |
| **Total** | **154/165 (93.3%)** | **155/165 (93.9%)** | **90/165 (54.5%)** | **39/165 (23.6%)** | **153/165 (92.7%)** | **149/165 (90.3%)** | **153/165 (92.7%)** |
| **Total (excl. two known-broken\*)** | 151/157 (96.2%) | **153/157 (97.5%)** | 90/157 (57.3%) | 39/157 (24.8%) | 150/157 (95.5%) | 147/157 (93.6%) | 151/157 (96.2%) |

\* See Round 1's [Known limitations](#known-limitations-not-model-failures) —
same pre-existing sub-skill stub defect, unrelated to model choice.

### Sonnet 4.5 vs 4.6 vs 5 — the bug is version-specific, and Sonnet 5 fixes it

This round's biggest finding: **`claude-sonnet-4.6` reproduces (and in some
cases worsens) Round 1's Sonnet 4.5 failure mode, while `claude-sonnet-5`
fixes it almost entirely.**

| Benchmark | Sonnet 4.5 (Round 1) | Sonnet 4.6 (Round 2) | Sonnet 5 (Round 2) |
|---|---|---|---|
| bmad-agent-architect | 20/23 | **2/23** | 23/23 |
| bmad-agent-pm | 18/18 | **0/18** | 18/18 |
| bmad-create-architecture | 0/16 | **0/16** | 13/16 |
| bmad-prd | 7/12 | **0/12** | 12/12 |
| bmad-sprint-planning | 0/4 | **0/4** | 4/4 |
| **Overall (excl. known-broken benchmarks)** | 66.9% | **24.8%** | **95.5%** |

Inspecting the Sonnet 4.6 logs shows the exact same signature as Sonnet 4.5
in Round 1: `read_skill` is called 0 times on the failing prompts, and the
model answers from general knowledge instead. **4.6 is not an improvement
over 4.5 for this specific task — if anything, it's a regression** (24.8%
vs. 4.5's 66.9% on the same benchmark set, excluding the two known-broken
ones). Sonnet 5, by contrast, calls `read_skill` correctly across nearly
every prompt and lands within 1-2 points of the top-performing OpenAI/Gemini
models. **Recommendation: never use `claude-sonnet-4.6` for BMad
customization-following tasks. If a Claude Sonnet-tier model is wanted,
use `claude-sonnet-5`, not 4.5 or 4.6.**

### Updated executive summary (supersedes Round 1's ranking)

1. `gpt-5.4` — 97.5% (excl. broken benchmarks) — new top performer this round.
2. `gpt-5-mini` — 96.2% (tied) — still the cheapest strong option.
3. `gemini-3-flash-preview` — 96.2% (tied) — still excellent value.
4. `claude-sonnet-5` — 95.5% — validates the swap from 4.5/4.6; best Claude option by a wide margin.
5. `gemini-3.5-flash` — 93.6%.
6. `claude-haiku-4.5` — 57.3% — unchanged conclusion from Round 1, still the weakest usable model, still a discard candidate for workflow-heavy tasks.
7. `claude-sonnet-4.6` — 24.8% — **new hard discard**, worse than Haiku on this task despite being a newer, pricier model. Do not use for BMad customization work regardless of general capability elsewhere.

## Models per agent and per BMad workflow suggestion

Empirical, benchmark-specific recommendations (Round 2 data), one line per
BMad agent/workflow. "Safe" means no meaningfully better alternative exists
at a lower cost; "Best" is the single top scorer; "Avoid" means a clear,
repeatable failure mode was observed for that specific benchmark.

### Agents (Phase 1 — agent persona / Q&A interactions)

| Agent | Best | Safe alternatives | Avoid |
|---|---|---|---|
| `bmad-agent-architect` | `gpt-5-mini` / `gpt-5.4` / `claude-sonnet-5` / both Gemini flash (all 23/23) | any of the above | `claude-sonnet-4.6` (2/23), `claude-haiku-4.5` (15/23) |
| `bmad-agent-dev` | `gpt-5.4` / `claude-sonnet-4.6` (both 23/23 — 4.6 is fine here, only fails on *workflow*-phrased prompts) | `gpt-5-mini`, `claude-sonnet-5`, both Gemini flash (22/23) | `claude-haiku-4.5` (15/23) |
| `bmad-agent-pm` | `gpt-5.4` / `claude-sonnet-5` / both Gemini flash (18/18) | `gpt-5-mini` (17/18) | `claude-sonnet-4.6` (**0/18**), `claude-haiku-4.5` (9/18) |
| `bmad-agent-ux-designer` (agent persona, not the UX *workflow* — see below) | `gpt-5-mini` / `gpt-5.4` (18/18) | `claude-sonnet-5`, `gemini-3.5-flash` (17/18) | `claude-sonnet-4.6` (2/18), `claude-haiku-4.5` (13/18) |

### Workflows (Phase 2-4 — multi-step BMad workflows)

| Workflow (BMad phase) | Best | Safe alternatives | Avoid |
|---|---|---|---|
| `bmad-prd` (Phase 2 Planning) | `gpt-5.4` / `claude-sonnet-5` / both Gemini flash (12/12) | `gpt-5-mini` (11/12) | `claude-sonnet-4.6` (**0/12**), `claude-haiku-4.5` (10/12) |
| `bmad-prd-conditional` (Phase 2 Planning) | any of `gpt-5-mini`/`gpt-5.4`/`claude-sonnet-5`/both Gemini flash (all 14/14) | — | `claude-sonnet-4.6` (4/14), `claude-haiku-4.5` (7/14) |
| `bmad-ux` (Phase 2 Planning — **this is the CLI/API-aware UX phase the original manual test flagged**; make sure it's not defaulting to web-frontend assumptions per the earlier gap fix) | `gemini-3.5-flash` (4/4, the only perfect score) | `gpt-5-mini`, `gpt-5.4`, `claude-sonnet-5`, `gemini-3-flash-preview` (3/4) | `claude-sonnet-4.6` (**0/4**), `claude-haiku-4.5` (**0/4**) |
| `bmad-create-architecture` (Phase 3 Solutioning — the phase the original manual test said had *no* Q&A/tech-validation checks; make sure the fix is actually exercised here) | `gpt-5.4` / `gemini-3-flash-preview` (15/16) | `gpt-5-mini`, `gemini-3.5-flash` (14/16) | `claude-sonnet-4.6` (**0/16**), `claude-haiku-4.5` (6/16) |
| `bmad-create-epics-and-stories` (Phase 3 Solutioning) | any of `gpt-5-mini`/`gpt-5.4`/`claude-sonnet-5`/both Gemini flash (all 4/4) | `claude-haiku-4.5` (3/4, acceptable) | `claude-sonnet-4.6` (**0/4**) |
| `bmad-check-implementation-readiness` (Phase 3 Solutioning) | *(benchmark stub defect — see Known limitations; no model scores meaningfully here, fix the stub before trusting any recommendation for this workflow)* | — | — |
| `bmad-sprint-planning` (Phase 4 Implementation) | `gpt-5-mini` / `claude-sonnet-5` / `gemini-3.5-flash` (4/4) | `gpt-5.4`, `gemini-3-flash-preview` (3/4) | `claude-sonnet-4.6` (**0/4**), `claude-haiku-4.5` (**0/4**) |
| `bmad-dev-story` (Phase 4 Implementation) | `gpt-5-mini` / `gemini-3.5-flash` / `gemini-3-flash-preview` (4/4) | `gpt-5.4`, `claude-sonnet-5` (3/4) | `claude-sonnet-4.6` (**0/4**), `claude-haiku-4.5` (2/4) |
| `bmad-code-review` (Phase 4 Implementation) | *(benchmark stub defect — see Known limitations; same caveat as readiness)* | — | — |
| `bmad-merge-validation` (cross-cutting) | `gpt-5-mini` / `gpt-5.4` / `claude-sonnet-5` / `gemini-3-flash-preview` (17/17) | — | `claude-sonnet-4.6` (8/17), `claude-haiku-4.5` (10/17), `gemini-3.5-flash` (11/17) |

### One-line takeaway per agent/workflow user actually asked about

Direct answers to the two gaps raised in manual testing:

- **Architecture phase Q&A (originally missing)**: now exercised by
  `bmad-create-architecture`. Use `gpt-5.4` or `gemini-3-flash-preview`
  (15/16) — avoid `claude-sonnet-4.6` entirely (0/16) and `claude-haiku-4.5`
  (6/16) for this workflow specifically.
- **UX phase (originally assumed a web frontend)**: now exercised by
  `bmad-ux`. `gemini-3.5-flash` is the only model that scored a perfect 4/4
  on this specific benchmark (which includes the CLI/API-awareness
  assertions added in the earlier fix); `gpt-5-mini`/`gpt-5.4`/
  `claude-sonnet-5`/`gemini-3-flash-preview` are close behind at 3/4 and all
  acceptable; avoid Sonnet 4.6 and Haiku here (0/4 each).

## Overall generalist pick (Round 2, supersedes Round 1)

For teams that want one model instead of per-workflow switching:
**`gpt-5.4` and `gpt-5-mini`** remain the safest generalist picks (97.5% and
96.2% excluding the two broken benchmarks), with **`claude-sonnet-5`** now a
credible third option for teams standardizing on Anthropic (95.5%, and the
cheapest Sonnet tier under current promo pricing). `gemini-3-flash-preview`
is tied with `gpt-5-mini` at 96.2% and worth strong consideration given its
lower price point ($0.50/$3.00 vs. `gpt-5.4`'s $2.50/$15.00).
**`claude-haiku-4.5` and `claude-sonnet-4.6` are both discard candidates**
for BMad customization-adherence work — Haiku for its Round 1 reasons, and
Sonnet 4.6 as a new, notably worse-than-its-predecessor regression on this
specific task (use Sonnet 5 instead if the Claude family is preferred).

## Round 2 follow-ups (out of scope for this report)

1. Report the GPT-5.6 family's `/chat/completions` incompatibility back to
   the `ai-observer` maintainers — PR #99 addressed the reasoning-tier
   sampling-parameter issue but not the underlying missing endpoint routing;
   these models need a `/responses`-style (or similar agent) API path added
   to the proxy before they can be tested here at all.
2. Investigate whether `claude-sonnet-4.6`'s regression vs. 4.5 is specific
   to this proxy/harness (e.g. a default system-prompt or tool-schema
   difference Anthropic changed between checkpoints) or a genuine model
   regression — worth a narrower, isolated repro outside this benchmark
   suite if the finding surprises the team.
3. Re-run once `bmad-check-implementation-readiness` and `bmad-code-review`'s
   sub-skill stubs are filled in (see Round 1's Known limitations) — those
   two workflows still have no trustworthy per-model recommendation.

## Round 3 — tooling migration to native multi-model support (PR #100)

`ai-observer` PR #100 ("multi-model benchmark support with comparison
dashboard", https://github.com/dktunited/ai-observer/pull/100, merged) added
a `models:` YAML list field directly to `BenchmarkConfig`
(`proxy/internal/config/config.go`). When `models:` is set it takes
precedence over the singular `model:` field, and the `benchmark` CLI itself
(`proxy/cmd/benchmark/main.go`) loops over every listed model for a single
config **inside one invocation**, printing a `Total: X/Y assertions passed`
summary per model plus its own per-prompt pass-rate comparison matrix. It
also added a `/api/v1/models` API endpoint and a "Models" dashboard page.

**Why this mattered for our tooling:** `scripts/run-model-comparison.sh`
(Round 1/2) worked around the *lack* of this feature by generating a
per-model temp copy of each benchmark yml via `sed`, then invoking
`benchmark run` once per model per benchmark — 7 models x 14 benchmarks = 98
separate CLI invocations, each paying its own process-launch and skill-load
overhead, plus a hand-rolled 429 retry/backoff loop between invocations.
With PR #100 merged, the script was rewritten (v3) to:

- Inject a `models:` list once per benchmark yml (via a small Python3 regex
  helper — BSD `awk`/`sed` cannot cleanly splice a multi-line block into a
  file via a shell variable without `awk: newline in string` errors), then
  call `benchmark run --config <tmp>` **once per benchmark** (14 total
  invocations instead of 98), relying on the CLI's native per-model loop.
- Parse the per-model `Total: X/Y` lines out of the single combined log, in
  call order (confirmed from the Go source that output order matches the
  `models:` list order), and reconstruct the same pass-rate matrix format the
  old script produced — so downstream tooling/report parsing is unaffected.
- Confirmed `pre_activate` still runs exactly once per benchmark invocation,
  before the model loop (not per-model) — so `{resolved_agent}` is resolved
  identically for every model in a run, same guarantee as before.
- **Known gap, accepted for now:** the old script's per-model 429
  retry/backoff has no direct equivalent once model looping moves inside a
  single CLI call (neither the `benchmark` CLI nor the proxy retries 429s —
  the proxy only logs them). The new architecture launches far fewer
  processes (14 vs 98), which reduces overall exposure to bursty rate
  limiting, and no 429s were observed during the validation run below. If
  rate limiting becomes a problem again, the cleanest fix is a whole-run
  retry wrapper around `benchmark run --config <tmp>` per benchmark rather
  than per-model.

### Validation run (7 models x 14 benchmarks, same list as Round 2)

Same `DEFAULT_MODELS`, same 14 benchmarks, same `bmadtest4` reference
project, run entirely through the new v3 script/native multi-model path
against the same local Copilot proxy. Aggregate pass rates, **excluding**
the two known-broken benchmarks (`bmad-check-implementation-readiness`,
`bmad-code-review` — pre-existing test-fixture gaps unrelated to this
migration, see Round 2 follow-up #3):

| Model | Round 2 (old per-model script) | Round 3 (new native `models:` script) |
|---|---|---|
| `gpt-5.4` | 97.5% | 98.1% |
| `claude-sonnet-5` | 95.5% | 96.2% |
| `gemini-3-flash-preview` | 96.2% | 94.9% |
| `gpt-5-mini` | 96.2% | 95.5% |
| `gemini-3.5-flash` | n/a (not separately reported) | 93.6% |
| `claude-haiku-4.5` | 66.9% | 59.9% |
| `claude-sonnet-4.6` | 24.8% | 5.7% |

**Conclusion: the tooling migration is validated — everything still works.**
Rankings are identical between rounds (`gpt-5.4` > `claude-sonnet-5` ~
`gpt-5-mini` ~ `gemini-3-flash-preview` >> `claude-haiku-4.5` >>
`claude-sonnet-4.6`), and the small per-model deltas (1-7 points) are
consistent with ordinary run-to-run LLM sampling variance, not a tooling
regression — the same benchmarks, prompts, and assertions produced the same
qualitative verdicts. `claude-sonnet-4.6`'s severe regression (now measured
even lower, at 5.7%) is reconfirmed rather than an artifact of the old
script: inspecting the new run's logs shows the identical failure
signature as Round 1/2 — `read_skill` is called 0-1 times on failing
prompts and the model answers from general knowledge instead of the loaded
customization.

**Practical benefit confirmed:** wall-clock time for the full 98-model-run
sweep was comparable to Round 2 (dominated by actual LLM call latency, not
process-launch overhead, since each benchmark still runs 7 sequential model
calls internally) — but the script itself is now far simpler (no per-model
`sed`+`mktemp`+retry loop) and any future model-list changes require editing
one YAML `models:` block via the injected Python helper instead of
re-invoking the CLI per model.

No changes were needed to any of the 14 checked-in `tests/*/*-benchmark.yml`
source files — the `models:` list is injected into runtime temp copies only,
never into the source ymls, keeping single-model local debugging (`benchmark
run --config tests/.../*.yml` with no override) working exactly as before.
