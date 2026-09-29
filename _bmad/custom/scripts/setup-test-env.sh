#!/bin/bash
# Setup benchmark test environment using reference BMAD project

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
REFERENCE_BMAD="/Users/mmornati/Projects/bmadtest4"

echo -e "${GREEN}🔍 Checking BMAD reference project...${NC}"

# Verify reference BMAD exists
if [ ! -d "$REFERENCE_BMAD" ]; then
  echo -e "${RED}❌ Reference BMAD not found at: $REFERENCE_BMAD${NC}"
  echo -e "${YELLOW}📝 Expected a BMAD project at: $REFERENCE_BMAD${NC}"
  echo -e "${YELLOW}   You can check /Users/mmornati/Projects/bmadtest4 or set BMAD_PROJECT_PATH${NC}"
  exit 1
fi

if [ ! -d "$REFERENCE_BMAD/.agents/skills" ]; then
  echo -e "${RED}❌ Skills not found in reference BMAD${NC}"
  exit 1
fi

if [ ! -f "$REFERENCE_BMAD/_bmad/scripts/resolve_customization.py" ]; then
  echo -e "${RED}❌ BMAD scripts not found in reference project${NC}"
  exit 1
fi

echo -e "${GREEN}✅ Reference BMAD found at: $REFERENCE_BMAD${NC}"

# Create unique temp copy
TEST_DIR="/tmp/bmad-test-$(date +%s)-$$"
mkdir -p "$TEST_DIR"

echo -e "${GREEN}📁 Creating test copy at: $TEST_DIR${NC}"

# Copy reference BMAD to temp location
cp -r "$REFERENCE_BMAD" "$TEST_DIR/"
BMAD_COPY="$TEST_DIR/$(basename "$REFERENCE_BMAD")"

echo -e "${GREEN}✅ Reference BMAD copied${NC}"

# Copy/update customization to _bmad/custom
echo -e "${GREEN}🔄 Applying customization to _bmad/custom...${NC}"
mkdir -p "$BMAD_COPY/_bmad/custom"
cp -r "$PROJECT_ROOT"/* "$BMAD_COPY/_bmad/custom/" 2>/dev/null || true

# Clean up non-customization files
cd "$BMAD_COPY/_bmad/custom"
rm -rf .git .github .gitignore || true
rm -rf tests/bmad-agent-architect/stubs 2>/dev/null || true

echo -e "${GREEN}✅ Customization applied${NC}"

# Verify skill locations
echo -e "${GREEN}🧩 Verifying skills...${NC}"
SKILLS_FOUND=0
for skill in "decathlon-tech-radar" "decathlon-tech-compliance" "knowledge-graph-query" "spring-boot-fedid-resource-server" "better-auth-fedid-configuration-astro"; do
  if [ -f "$BMAD_COPY/.agents/skills/$skill/SKILL.md" ]; then
    SKILLS_FOUND=$((SKILLS_FOUND + 1))
    echo "  ✓ $skill"
  else
    echo "  ✗ $skill (not found)"
  fi
done

echo -e "${GREEN}✅ Found $SKILLS_FOUND/5 required skills${NC}"

# Export env vars for use by benchmark test
echo -e "${GREEN}📝 Setting up environment variables...${NC}"
cat > "$BMAD_COPY/.env.benchmark" << EOF
PROJECT_ROOT=$BMAD_COPY
ARCH_AGENT_SKILL_DIR=$BMAD_COPY/.agents/skills/bmad-agent-architect
TECH_RADAR_PATH=$BMAD_COPY/.agents/skills/decathlon-tech-radar/SKILL.md
TECH_COMPLIANCE_PATH=$BMAD_COPY/.agents/skills/decathlon-tech-compliance/SKILL.md
ASSET_KG_PATH=$BMAD_COPY/.agents/skills/knowledge-graph-query/SKILL.md
FEDID_SPRING_PATH=$BMAD_COPY/.agents/skills/spring-boot-fedid-resource-server/SKILL.md
FEDID_ASTRO_PATH=$BMAD_COPY/.agents/skills/better-auth-fedid-configuration-astro/SKILL.md
EOF

echo "export TEST_DIR=$TEST_DIR" >> "$BMAD_COPY/.env.benchmark"

cat "$BMAD_COPY/.env.benchmark" | grep -v "^#" | grep "=" | while IFS='=' read -r key value; do
  echo "  $key=...$(basename "$value")"
done

# Save TEST_DIR for cleanup
echo "$BMAD_COPY" > "$BMAD_COPY/.test-marker"

echo -e "${GREEN}✅ Test environment ready${NC}"
echo -e "${YELLOW}📊 BMAD project: $BMAD_COPY${NC}"
echo -e "${YELLOW}💡 To clean up: rm -rf $TEST_DIR${NC}"
