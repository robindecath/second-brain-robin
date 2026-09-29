#!/bin/bash
# Run all benchmark tests with automatic environment setup
# Supports sequential and parallel execution modes
# Compatible with bash 3.2+ (macOS)

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_DIR="$(dirname "$0")"
MODE="${1:-sequential}"  # sequential or parallel
AGENT_FILTER="${2:-}"   # Filter to specific agent (empty = all)
BMAD_PROJECT="${BMAD_PROJECT:-/Users/mmornati/Projects/bmadtest4}"

# Use temp file for results (bash 3.2 compatible)
RESULTS_FILE=$(mktemp)
trap "rm -f $RESULTS_FILE" EXIT

# Emoji mapping (using simple string concatenation)
get_agent_emoji() {
    case "$1" in
        bmad-agent-architect) echo "🏗️" ;;
        bmad-agent-dev) echo "💻" ;;
        bmad-agent-pm) echo "📊" ;;
        bmad-agent-ux-designer) echo "🎨" ;;
        bmad-agent-sre) echo "🔧" ;;
        bmad-build) echo "🔨" ;;
        bmad-sprint-planning) echo "🗂️" ;;
        bmad-architecture) echo "📐" ;;
        *) echo "❓" ;;
    esac
}

echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}         BMAD Benchmark Test Suite - $MODE mode${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo ""

# Verify benchmark tool exists
if ! command -v /Users/mmornati/go/bin/benchmark &> /dev/null; then
    echo -e "${RED}❌ benchmark tool not found${NC}"
    echo -e "${YELLOW}   Expected at: /Users/mmornati/go/bin/benchmark${NC}"
    exit 1
fi

# Helper function to setup a single test
setup_test_env() {
    local agent="$1"
    local config="$2"
    
    # Reuse existing setup script but capture env vars
    local setup_output=$("${SCRIPT_DIR}/setup-test-env.sh" 2>&1)
    
    # Extract the BMAD test directory from output
    local test_dir=$(echo "$setup_output" | grep "BMAD project:" | awk '{print $NF}')
    
    if [ -z "$test_dir" ]; then
        echo "" >&2
        return 1
    fi
    
    echo "$test_dir"
}

# Helper function to run a single benchmark
run_benchmark() {
    local agent="$1"
    local config="$2"
    local test_dir="$3"
    
    # Load env vars
    if [ -f "$test_dir/.env.benchmark" ]; then
        set -a
        source "$test_dir/.env.benchmark"
        set +a
    fi
    
    # Run benchmark
    cd "$REPO_ROOT"
    
    if /Users/mmornati/go/bin/benchmark run --config "$config" > /tmp/benchmark-$agent.log 2>&1; then
        # Extract results
        local passed=$(grep "Total:" /tmp/benchmark-$agent.log 2>/dev/null | grep -oE '[0-9]+/[0-9]+' | cut -d'/' -f1) || passed="?"
        local total=$(grep "Total:" /tmp/benchmark-$agent.log 2>/dev/null | grep -oE '[0-9]+/[0-9]+' | cut -d'/' -f2) || total="?"
        
        # Store result
        echo "$agent|PASS|$passed/$total" >> "$RESULTS_FILE"
        return 0
    else
        echo "$agent|FAIL|ERROR" >> "$RESULTS_FILE"
        return 1
    fi
}

# Find all benchmarks
echo "🔍 Discovering benchmarks..."
BENCHMARKS=()
BENCHMARK_COUNT=0

while IFS= read -r benchmark_file; do
    if [ -z "$benchmark_file" ]; then
        continue
    fi
    
    # Extract agent name from path
    agent=$(basename "$(dirname "$benchmark_file")")
    
    # Filter if agent filter specified
    if [ -n "$AGENT_FILTER" ] && [ "$agent" != "$AGENT_FILTER" ]; then
        continue
    fi
    
    BENCHMARKS+=("$agent|$benchmark_file")
    BENCHMARK_COUNT=$((BENCHMARK_COUNT + 1))
    echo "  ✓ Found: $agent"
done < <(find "$REPO_ROOT" -name "*-benchmark.yml" -type f)

if [ $BENCHMARK_COUNT -eq 0 ]; then
    echo -e "${RED}❌ No benchmarks found${NC}"
    exit 1
fi

echo -e "${GREEN}Found $BENCHMARK_COUNT benchmark(s)${NC}"
echo ""

# Run tests
echo "🏃 Executing benchmarks..."
START_TIME=$(date +%s)

if [ "$MODE" = "parallel" ]; then
    # Parallel execution
    echo -e "${YELLOW}Running in PARALLEL mode (~10-15 minutes)${NC}"
    echo ""
    
    for benchmark in "${BENCHMARKS[@]}"; do
        IFS='|' read -r agent config <<< "$benchmark"
        
        # Setup and run in background
        (
            test_dir=$(setup_test_env "$agent" "$config")
            if [ $? -eq 0 ] && [ -n "$test_dir" ]; then
                run_benchmark "$agent" "$config" "$test_dir"
                # Cleanup
                rm -rf "$(dirname "$test_dir")" 2>/dev/null || true
            fi
        ) &
    done
    
    # Wait for all background jobs
    wait
else
    # Sequential execution
    echo -e "${YELLOW}Running SEQUENTIALLY (~30-40 minutes)${NC}"
    echo ""
    
    for benchmark in "${BENCHMARKS[@]}"; do
        IFS='|' read -r agent config <<< "$benchmark"
        
        test_dir=$(setup_test_env "$agent" "$config")
        if [ $? -eq 0 ] && [ -n "$test_dir" ]; then
            run_benchmark "$agent" "$config" "$test_dir"
            # Cleanup
            rm -rf "$(dirname "$test_dir")" 2>/dev/null || true
        fi
    done
fi

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# Report results
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}                       Test Results${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo ""

PASSED_AGENTS=0

while IFS='|' read -r agent status result; do
    if [ -z "$agent" ]; then
        continue
    fi
    
    emoji=$(get_agent_emoji "$agent")
    
    if [ "$status" = "PASS" ]; then
        echo -e "${GREEN}$emoji $agent${NC}: ✓ $result"
        PASSED_AGENTS=$((PASSED_AGENTS + 1))
    else
        echo -e "${RED}$emoji $agent${NC}: ✗ $result (see /tmp/benchmark-$agent.log)"
    fi
done < "$RESULTS_FILE"

echo ""
echo -e "Agents: ${GREEN}$PASSED_AGENTS/$BENCHMARK_COUNT passed${NC}"
echo "Time: $((DURATION / 60))m $((DURATION % 60))s"
echo ""

# Summary
if [ $PASSED_AGENTS -eq $BENCHMARK_COUNT ]; then
    echo -e "${GREEN}✅ All benchmarks passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Some benchmarks failed${NC}"
    exit 1
fi
