#!/bin/bash
# Run every tests/*/*-benchmark.yml across a configurable list of Copilot models
# and report a benchmark x model pass-rate matrix.
#
# Purpose: answer "does this model reliably follow the BMAD customization
# directives (persistent_facts/activation_steps/principles), or should it be
# discarded for this workflow?" with data instead of anecdote — see the repo's
# tests/*-benchmark.yml suite (AI Observer benchmark assertions) for what
# "following the customization" means concretely.
#
# v3 (2026-07): migrated to ai-observer PR #100's native multi-model support
# (https://github.com/dktunited/ai-observer/pull/100). The `benchmark` CLI
# itself now accepts a `models:` YAML list and loops over every model for a
# single config internally, printing its own pass-rate comparison matrix —
# this replaces the old approach of this script generating N per-model temp
# config copies via sed and invoking `benchmark run` N times per benchmark.
# One `benchmark run` invocation per benchmark yml now covers every model.
# Requires a `benchmark` binary built from ai-observer commit 3098c01 (PR
# #100) or later — rebuild with:
#   cd /path/to/ai-observer/proxy && go build -o "$(go env GOPATH)/bin/benchmark" ./cmd/benchmark
#
# Requirements (same as the rest of tests/ + scripts/run-all-benchmarks.sh):
#   - `benchmark` CLI on PATH (https://github.com/dktunited/ai-observer releases,
#     PR #100 / commit 3098c01 or later for multi-model support)
#   - LLM_ENDPOINT / LLM_API_KEY pointing at a reachable proxy, OR a local
#     GitHub Copilot proxy (see ai-observer docs/guide/quickstart.md,
#     "Option B — With Copilot proxy") started WITHOUT a fixed COPILOT_MODEL
#     env var, so each benchmark's `model:`/`models:` field is honored per-request:
#       docker run -d --name ai-observer-copilot-proxy -p 29080:29080 \
#         -e LLM_PROVIDER=copilot -e COPILOT_MODEL= -v ai-observer_copilot_data:/data \
#         ai-observer-copilot-proxy
#       export LLM_ENDPOINT=http://localhost:29080/v1/chat/completions
#       export LLM_API_KEY=not-used
#   - A reference BMad project checkout (BMAD_PROJECT) with `.agents/skills/`
#     and `_bmad/scripts/resolve_customization.py` present, matching the
#     convention already used by scripts/setup-test-env.sh.
#   - python3 on PATH (used to inject the `models:` list into each benchmark
#     yml's temp copy — more robust than sed/awk across BSD/GNU differences).
#
# KNOWN LIMITATION (pre-existing, fixed 2026-07 — kept for history): every
# workflow-level benchmark yml's `pre_activate` hook used to call
# resolve_customization.py with a bare skill name and a nonexistent
# --project-root flag, so it silently failed on every run and {resolved_agent}
# was always empty — no benchmark ever actually injected the team's TOML
# customization. This has been fixed: pre_activate now uses a real,
# env-var-driven --skill path (this script exports the *_SKILL_DIR vars
# below) and the correct --key (workflow vs agent). The `skills:` main-skill
# path for workflow benchmarks is now also env-var-driven, so a real
# installed SKILL.md is used instead of the incomplete placeholder stub.
# `tests/comparative-routing` has no skills/pre_activate scaffolding at all
# and is intentionally excluded from this comparison.
#
# Usage:
#   scripts/run-model-comparison.sh                       # default model list, all benchmarks
#   scripts/run-model-comparison.sh bmad-agent-architect  # filter to one benchmark dir
#   MODELS="claude-haiku-4.5,gpt-5-mini" scripts/run-model-comparison.sh
#   BMAD_PROJECT=/path/to/real/bmad/project scripts/run-model-comparison.sh

set -u

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_DIR="$(dirname "$0")"
AGENT_FILTER="${1:-}"

# Default model list — v2, refreshed after ai-observer PR #97 (dynamic Copilot
# model discovery + expanded static allowlist), PR #98 (max_tokens passthrough
# fix) and PR #99 (reasoning-tier param stripping + upstream error logging).
# Re-verified with direct curl against a FULLY REBUILT proxy image
# (`docker build -f proxy/Dockerfile.copilot` from origin/main @ 8cc20b8) and
# a fresh container recreate (COPILOT_MODEL explicitly cleared to empty — the
# Docker image bakes in ENV COPILOT_MODEL=gpt-4o, which silently overrides
# every request's model unless cleared with `-e COPILOT_MODEL=`).
#
# NEWLY CONFIRMED WORKING (thanks to PR #97's expanded allowlist/dynamic
# discovery): claude-sonnet-4.6, claude-sonnet-5, claude-opus-4.8,
# gemini-3.1-pro-preview, gemini-2.5-pro. claude-sonnet-5 replaces
# claude-sonnet-4.5 as the primary Sonnet candidate below: Anthropic's own
# Sonnet 5 announcement states it is a "substantial improvement over ...
# Sonnet 4.6 ... on reasoning, tool use, coding, and knowledge work", and it
# is priced LOWER than 4.5/4.6 under current promo pricing ($2/$10 per 1M
# tokens vs $3/$15, through Aug 2026). claude-sonnet-4.6 is kept alongside it
# purely as a diagnostic: the v1 report found claude-sonnet-4.5 has a
# repeatable bug where it never calls read_skill for workflow-phrased
# prompts (bmad-create-architecture, bmad-dev-story, etc.) — running 4.6
# tells us if that's Sonnet-family-wide or specific to the 4.5 checkpoint.
# (Round 2 result: 4.6 is a regression vs 4.5, not a fix — see
# docs/MODEL_COMPARISON_REPORT.md.)
#
# STILL NOT USABLE, RE-VERIFIED AFTER THE FULL #97/#98/#99 REBUILD (these are
# NOT proxy bugs anymore — confirmed via docker logs' new upstream-error
# logging from PR #99, tested both with and without a `temperature` field to
# rule out the reasoning-tier param theory):
#   - gpt-5.6-luna, gpt-5.6-sol, gpt-5.6-terra, gpt-5.5, gpt-5.4-mini,
#     gpt-5.3-codex: real API error "not accessible via the /chat/completions
#     endpoint" — these need a different, agent-style API (e.g. a /responses
#     endpoint), which this proxy does not implement. PR #99's temperature/
#     top_p stripping does NOT fix this (verified: identical rejection with
#     or without temperature in the request) — it only helps in the case
#     where a caller sends those fields at all; the endpoint-shape mismatch
#     is a separate, deeper limitation.
#   - claude-fable-5, kimi-k2.7-code: "model_not_supported" — per PR #99's
#     own doc update, these require explicit org/enterprise admin opt-in
#     separate from being listed; not a bug to fix here.
#   - gpt-5.4-nano, raptor-mini, claude-sonnet-4, gemini-3.1-pro (no
#     "-preview" suffix): not in this account's real available-model list at
#     all (confirmed via live "model not available" error enumerating every
#     real ID for this integrator).
#   - mai-code-1-flash (and -picker/-secondary/-tertiary variants): all
#     still return errors from the real Copilot API on this account — no
#     Microsoft model works via /chat/completions here.
#
# Premium/"Powerful" tier models confirmed available (claude-opus-4.8,
# gemini-3.1-pro-preview, gemini-2.5-pro) are intentionally excluded from the
# default sweep to keep run time/cost reasonable — override via MODELS= to
# include them.
DEFAULT_MODELS="gpt-5-mini,gpt-5.4,claude-haiku-4.5,claude-sonnet-4.6,claude-sonnet-5,gemini-3.5-flash,gemini-3-flash-preview"
IFS=',' read -r -a MODEL_LIST <<< "${MODELS:-$DEFAULT_MODELS}"

BMAD_PROJECT="${BMAD_PROJECT:-/Users/mmornati/Projects/bmadtest4}"

if ! command -v benchmark &> /dev/null; then
  echo -e "${RED}❌ benchmark CLI not found on PATH${NC}"
  echo -e "${YELLOW}   Install from https://github.com/dktunited/ai-observer releases${NC}"
  exit 1
fi

if ! command -v python3 &> /dev/null; then
  echo -e "${RED}❌ python3 not found on PATH (needed to inject the models: list)${NC}"
  exit 1
fi

if [ -z "${LLM_ENDPOINT:-}" ]; then
  echo -e "${YELLOW}⚠ LLM_ENDPOINT not set — relying on ~/.benchmark/.env or ./.env${NC}"
fi

echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}         Model Comparison — BMAD Customization Adherence${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo "Models: ${MODEL_LIST[*]}"
echo ""

# Discover benchmarks (optionally filtered to one agent/workflow dir name).
# comparative-routing has no skills/pre_activate scaffolding at all (a
# different kind of test) and is always excluded from this comparison.
BENCHMARKS=()
while IFS= read -r benchmark_file; do
  [ -z "$benchmark_file" ] && continue
  agent=$(basename "$(dirname "$benchmark_file")")
  if [ "$agent" = "comparative-routing" ]; then
    continue
  fi
  if [ -n "$AGENT_FILTER" ] && [ "$agent" != "$AGENT_FILTER" ]; then
    continue
  fi
  BENCHMARKS+=("$agent|$benchmark_file")
done < <(find "$REPO_ROOT/tests" -mindepth 2 -maxdepth 2 -name "*-benchmark.yml" -type f | sort)

if [ ${#BENCHMARKS[@]} -eq 0 ]; then
  echo -e "${RED}❌ No benchmarks found${NC}"
  exit 1
fi

echo "Benchmarks: ${#BENCHMARKS[@]}"
for b in "${BENCHMARKS[@]}"; do
  echo "  - ${b%%|*}"
done
echo ""

RESULTS_FILE=$(mktemp)
trap 'rm -f "$RESULTS_FILE"' EXIT

# --- Set up one temp BMad copy with this repo's customizations applied, reused
#     across all model runs (mirrors scripts/setup-test-env.sh). ---
setup_env() {
  if [ ! -d "$BMAD_PROJECT" ]; then
    echo -e "${RED}❌ Reference BMAD project not found: $BMAD_PROJECT (set BMAD_PROJECT)${NC}" >&2
    return 1
  fi
  local test_dir
  test_dir="/tmp/bmad-model-cmp-$(date +%s)-$$"
  mkdir -p "$test_dir"
  cp -r "$BMAD_PROJECT" "$test_dir/bmad"
  mkdir -p "$test_dir/bmad/_bmad/custom"
  cp "$REPO_ROOT"/*.toml "$test_dir/bmad/_bmad/custom/" 2>/dev/null || true
  echo "$test_dir/bmad"
}

PROJECT_COPY=$(setup_env) || exit 1
echo -e "${GREEN}✅ Test project ready: $PROJECT_COPY${NC}"
echo ""
trap 'rm -f "$RESULTS_FILE"; rm -rf "$(dirname "$PROJECT_COPY")"' EXIT

export PROJECT_ROOT="$PROJECT_COPY"

# One *_SKILL_DIR env var per benchmark, pointing at the real installed skill
# in the temp project copy — this is what makes pre_activate resolve real
# customization content (and, for workflow benchmarks, use the real SKILL.md
# instead of the incomplete placeholder stub).
export ARCH_AGENT_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-agent-architect"
export DEV_AGENT_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-agent-dev"
export PM_AGENT_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-agent-pm"
export UX_AGENT_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-agent-ux-designer"
export PRD_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-prd"
export ARCH_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-architecture"
export EPICS_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-create-epics-and-stories"
export SPRINT_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-sprint-planning"
export CODE_REVIEW_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-code-review"
export UX_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-ux"
# BMAD-METHOD 6.11.0: bmad-check-implementation-readiness was removed (folded
# into bmad-sprint-planning's readiness gate) and bmad-dev-story became a
# v6-shims forwarding skill superseded by bmad-build.
export BUILD_WORKFLOW_SKILL_DIR="$PROJECT_COPY/.agents/skills/bmad-build"
# Sub-skill env vars used by tests/bmad-agent-architect's stubs vs real skills
export TECH_RADAR_PATH="$PROJECT_COPY/.agents/skills/decathlon-tech-radar/SKILL.md"
export TECH_COMPLIANCE_PATH="$PROJECT_COPY/.agents/skills/decathlon-tech-compliance/SKILL.md"
export ASSET_KG_PATH="$PROJECT_COPY/.agents/skills/knowledge-graph-query/SKILL.md"
export FEDID_SPRING_PATH="$PROJECT_COPY/.agents/skills/spring-boot-fedid-resource-server/SKILL.md"
export FEDID_ASTRO_PATH="$PROJECT_COPY/.agents/skills/better-auth-fedid-configuration-astro/SKILL.md"

# Build a temp copy of a benchmark yml with a top-level `models:` list
# injected right after the existing `model:` line (ai-observer PR #100:
# `models:` takes precedence over `model:` when both are present, and the
# `benchmark` CLI runs the full prompt suite for every listed model in a
# single invocation — this replaces the old per-model sed/mktemp loop).
inject_models() {
  local config="$1" out="$2"
  shift 2
  local models_csv
  models_csv=$(IFS=,; echo "$*")
  python3 - "$config" "$out" "$models_csv" <<'PYEOF'
import re
import sys

config_path, out_path, models_csv = sys.argv[1], sys.argv[2], sys.argv[3]
models = models_csv.split(",")
block = "models:\n" + "\n".join(f"  - copilot/{m}" for m in models)

with open(config_path) as f:
    content = f.read()

new_content, n = re.subn(r'^model:.*$', lambda m: m.group(0) + "\n" + block, content, count=1, flags=re.MULTILINE)
if n == 0:
    sys.stderr.write(f"warning: no top-level 'model:' line found in {config_path}\n")
    new_content = content

with open(out_path, "w") as f:
    f.write(new_content)
PYEOF
}

# Run one benchmark yml against every configured model in a single `benchmark`
# invocation (native multi-model support), then split the per-model "Total:
# X/Y assertions passed" lines out of the combined log in call order.
run_benchmark_all_models() {
  local agent="$1" config="$2"
  local tmp_config
  tmp_config=$(mktemp /tmp/bmad-bench-XXXXXX)
  mv "$tmp_config" "${tmp_config}.yml"
  tmp_config="${tmp_config}.yml"

  inject_models "$config" "$tmp_config" "${MODEL_LIST[@]}"

  local log
  log="/tmp/model-cmp-${agent}.log"

  benchmark run --config "$tmp_config" > "$log" 2>&1
  rm -f "$tmp_config"

  # One "Total: X/Y assertions passed" line is printed per model, in the same
  # order as `models:` in the config (models_to_run iteration order).
  # (mapfile/readarray is bash 4+ only — macOS ships bash 3.2, so build the
  # array with a plain while-read loop instead.)
  local totals=()
  while IFS= read -r line; do
    totals+=("$line")
  done < <(grep -oE 'Total: [0-9]+/[0-9]+' "$log" | grep -oE '[0-9]+/[0-9]+')

  local i=0
  for model in "${MODEL_LIST[@]}"; do
    local val="${totals[$i]:-}"
    if [ -z "$val" ]; then
      if grep -qi "status 429\|rate limit" "$log"; then
        val="RATE_LIMITED"
      else
        val="ERROR"
      fi
    fi
    echo "    $model: $val"
    echo "$agent|$model|$val" >> "$RESULTS_FILE"
    i=$((i + 1))
  done
}

for b in "${BENCHMARKS[@]}"; do
  agent="${b%%|*}"
  config="${b#*|}"
  echo -e "${YELLOW}▶ ${agent}${NC}"
  run_benchmark_all_models "$agent" "$config"
done

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}                    Pass-Rate Matrix${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
printf "%-38s" "benchmark"
for model in "${MODEL_LIST[@]}"; do printf "%-20s" "$model"; done
echo ""
for b in "${BENCHMARKS[@]}"; do
  agent="${b%%|*}"
  printf "%-38s" "$agent"
  for model in "${MODEL_LIST[@]}"; do
    val=$(grep "^${agent}|${model}|" "$RESULTS_FILE" | tail -1 | cut -d'|' -f3)
    printf "%-20s" "${val:-?}"
  done
  echo ""
done
echo ""
echo "Per-benchmark combined logs (all models): /tmp/model-cmp-<benchmark>.log"
echo "(comparative-routing is intentionally excluded — no skills/pre_activate"
echo " scaffolding; see the header comment at the top of this script.)"
