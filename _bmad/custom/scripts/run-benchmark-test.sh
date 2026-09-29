#!/bin/bash
# Run benchmark test against the temporary BMAD environment

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CUSTOMIZATION_ROOT="$(dirname "$SCRIPT_DIR")"

# Find the BMAD test copy (bmadtest4 in temp directory)
TEST_COPY=$(find /tmp/bmad-test-* -name ".test-marker" -type f 2>/dev/null | head -1 | xargs dirname)

if [ -z "$TEST_COPY" ] || [ ! -d "$TEST_COPY" ]; then
  echo -e "${RED}❌ No test environment found. Run 'make test-benchmark-setup' first.${NC}"
  exit 1
fi

echo -e "${GREEN}🔬 Running benchmark test...${NC}"
echo -e "${YELLOW}Test copy: $TEST_COPY${NC}"
echo -e "${YELLOW}Customization: $CUSTOMIZATION_ROOT${NC}"

# Load environment variables
ENV_FILE="$TEST_COPY/.env.benchmark"
if [ ! -f "$ENV_FILE" ]; then
  echo -e "${RED}❌ Environment file not found: $ENV_FILE${NC}"
  exit 1
fi

set -a
source "$ENV_FILE"
set +a

# Verify environment variables are set
if [ -z "$PROJECT_ROOT" ]; then
  echo -e "${RED}❌ PROJECT_ROOT not set${NC}"
  exit 1
fi

if [ ! -d "$PROJECT_ROOT/.agents/skills" ]; then
  echo -e "${RED}❌ Skills directory not found: $PROJECT_ROOT/.agents/skills${NC}"
  exit 1
fi

echo -e "${BLUE}📋 Environment:${NC}"
echo "  PROJECT_ROOT=$PROJECT_ROOT"
echo "  ARCH_AGENT_SKILL_DIR=$ARCH_AGENT_SKILL_DIR"
echo "  TECH_RADAR_PATH=$(basename "$TECH_RADAR_PATH")"
echo "  TECH_COMPLIANCE_PATH=$(basename "$TECH_COMPLIANCE_PATH")"
echo "  ASSET_KG_PATH=$(basename "$ASSET_KG_PATH")"
echo ""

# Verify benchmark config exists in customization
if [ ! -f "$CUSTOMIZATION_ROOT/tests/bmad-agent-architect/bmad-agent-architect-benchmark.yml" ]; then
  echo -e "${RED}❌ Benchmark config not found: $CUSTOMIZATION_ROOT/tests/bmad-agent-architect/bmad-agent-architect-benchmark.yml${NC}"
  exit 1
fi

# Run benchmark from the customization repo directory (where config is)
echo -e "${GREEN}📊 Executing benchmark...${NC}"
echo "  Config: tests/bmad-agent-architect/bmad-agent-architect-benchmark.yml"
echo ""

cd "$CUSTOMIZATION_ROOT"

# Export all env vars for benchmark
export PROJECT_ROOT
export ARCH_AGENT_SKILL_DIR
export TECH_RADAR_PATH
export TECH_COMPLIANCE_PATH
export ASSET_KG_PATH
export FEDID_SPRING_PATH
export FEDID_ASTRO_PATH

# Run the benchmark test
if ! /Users/mmornati/go/bin/benchmark run --config "$CUSTOMIZATION_ROOT/tests/bmad-agent-architect/bmad-agent-architect-benchmark.yml"; then
  echo ""
  echo -e "${RED}❌ Benchmark test failed${NC}"
  exit 1
fi

echo ""
echo -e "${GREEN}✅ Benchmark test completed${NC}"

# Find and display the captures file
CAPTURES_DIR="$HOME/.benchmark/captures"
if [ -d "$CAPTURES_DIR" ]; then
  LATEST_CAPTURE=$(ls -t "$CAPTURES_DIR"/*.jsonl 2>/dev/null | head -1)
  if [ -n "$LATEST_CAPTURE" ]; then
    echo -e "${BLUE}📝 LLM Thinking Capture:${NC}"
    echo "  $LATEST_CAPTURE"
    echo -e "${YELLOW}💡 Analyze this file to review the LLM's reasoning during the test${NC}"
  fi
fi
