# Blast Radius Analyzer Skill

## 📌 Overview

The **Blast Radius Analyzer** skill performs incident impact analysis on Decathlon's digital asset topology. Given a failing product or component, it identifies:

- **Technical impact**: All downstream products/components that depend on the failing asset
- **Customer impact**: All User Journeys (customer experiences) that are affected
- **Business impact**: Domains affected, Tier-1 products impacted, criticality assessment

## 🎯 What It Does

1. **Fetches data** from:
   - AppReferential Knowledge Graph (products, components, API dependencies)
   - DeliveryMetrics API (User Journeys, SLO keys)

2. **Performs BFS analysis** to find all downstream consumers of the failing asset

3. **Links technical failures to customer experiences** via SLO key matching

4. **Generates three outputs**:
   - Interactive HTML visualization (Cytoscape.js graph)
   - JSON impact report
   - Text summary

## 📦 Dependencies

This skill requires three prerequisite skills:

- `decathlon-api-tool` — authenticated API calls
- `knowledge-graph-query` — GraphQL queries to Knowledge Graph
- `delivery-metrics` — REST queries to DeliveryMetrics API

## 🚀 Usage

### Via Copilot Chat

```
"Analyze the blast radius if OneFF fails"
"What's the impact if Login product goes down?"
"Show me the blast radius of onepay-api at component level"
```

### Via Skill Invocation

```python
# Load the skill
read_skill blast-radius-analyzer

# Follow the workflow in SKILL.md:
# 1. Parse input (incident_target, scope, view_level)
# 2. Load prerequisite skills
# 3. Fetch KG topology
# 4. Fetch User Journeys
# 5. Build graph data model
# 6. Perform BFS analysis
# 7. Generate outputs
# 8. Open visualization
```

## 📤 Outputs

### 1. HTML Visualization
**Location**: `/tmp/blast-radius-<target>-<timestamp>.html`

Interactive graph with:
- 🔴 Red node = failing asset
- 🟠 Orange nodes = impacted products
- 💔 Red diamonds = impacted User Journeys
- 🟡 Yellow dashed lines = SLO links

**Controls**:
- 🔄 Fit — reset view to full graph
- 🎯 Focus Impact — zoom to blast radius
- 🔥 Blast Radius Only — hide all non-impacted nodes (cleaner view)
- 🔗 External Consumers — toggle external domain consumers
- 💔 User Journeys — toggle UJ layer
- 🏷️ Labels — toggle node labels

**Impact Dashboard** (top-right):
- Failing nodes count
- Impacted products count
- Tier-1 products affected
- User Journeys impacted
- Criticality-1 UJs
- Domains affected
- Revenue loss estimate
- Per-minute loss rate

### 2. JSON Impact Report
**Location**: `/tmp/blast-radius-<target>-<timestamp>.json`

Structured data with:
- Impact metrics (products, UJs, domains, tiers)
- List of impacted products (name, tiering, domain, team)
- List of impacted User Journeys (name, criticality, SLO target)
- Domains affected breakdown
- Business impact assessment

### 3. Text Summary
Printed to console with:
- Impact statistics table
- Critical customer impact (Criticality-1 UJs)
- Business recommendations
- File paths for outputs

## 🧪 Example: OneFF Failure

**Command**:
```bash
python3 scripts/blast_radius.py /tmp/kg_graph.json product:OneFF
```

**Output**:
```
## 💥 Blast Radius Analysis — OneFF

| Metric | Count | Details |
|--------|-------|---------|
| 🔴 Failing | 1 | OneFF (Tier-1, 18 components) |
| 🟠 Impacted Products | 33 | 13 Tier-1 |
| 💔 Impacted User Journeys | 8 | 3 Criticality-1 (CRITICAL) |
| 🌐 External Consumers | 24 | Cross-domain dependencies |
| 🎯 Domains Affected | 8 | BCP, ECOMMERCE, FLTC, IN-STORE |
| 💥 Total Blast Radius | 42 | Products + UJs affected |

### 💔 CRITICAL Customer Impact
- Lower Funnel REVAMP Checkout (main checkout flow) — 100% revenue loss
- Create connected order (IoT products) — Connected business line blocked
- Remove a product from sale (product lifecycle) — Cannot delist products
```

## 🔧 How to Share This Skill

### Option 1: Share the skill folder

```bash
# Zip the skill folder
cd .agents/skills
tar -czf blast-radius-analyzer.tar.gz blast-radius-analyzer/

# Share the tarball
# Recipient extracts it to their .agents/skills/ directory
```

### Option 2: Use Copilot's share_extension tool

```
User: "Share the blast-radius-analyzer skill"
Agent: [calls share_extension tool]
→ Creates a private GitHub gist
→ Returns shareable URL
```

Recipient installs via:
```
User: "Install extension from <gist-url>"
Agent: [calls install_extension tool]
→ Downloads skill to .agents/skills/
→ Reloads extensions
→ Skill is ready to use
```

### Option 3: Add to project repository

```bash
# Commit the skill to version control
git add .agents/skills/blast-radius-analyzer/
git commit -m "Add blast radius analyzer skill"
git push

# Team members get it via:
git pull
```

## 📝 Customization

### Visualization Features

The HTML visualization includes all standard controls:

**🔥 Blast Radius Only Button** (NEW):
- Hides all non-impacted nodes for cleaner view
- Perfect for presentations and executive reports
- Shows only failing node + impacted products + UJs
- Auto-zooms to blast radius
- Respects other toggle states (UJs, external consumers)

**Use cases**:
- 📊 Executive presentations — clean view without technical noise
- 🔍 Incident response — focus only on what's affected
- 📸 Documentation — screenshot the blast radius for runbooks
- 👥 Team communication — "Here's what your product depends on"

The template at `templates/blast-radius-viz.html` includes this feature by default.

### Modify Analysis Parameters

Edit `SKILL.md` to change:
- Default view level (product vs component)
- BFS traversal algorithm (e.g., add depth limits)
- SLO key matching patterns
- Output formatting

### Add Custom Scripts

Add helper scripts to `scripts/`:
- `generate_html.py` — HTML visualization generator
- `fetch_kg_data.py` — Knowledge Graph data fetcher
- `fetch_uj_data.py` — User Journey data fetcher

### Extend Output Formats

Add new output types:
- PDF reports
- Slack notifications
- Datadog incident annotations
- Jira ticket creation

## 🔬 Testing

```bash
# Test with existing graph data
python3 scripts/blast_radius.py \
  /tmp/kg_graph_products_oneff_with_ujs.json \
  product:OneFF

# Should output:
# - Text summary to console
# - JSON report to /tmp/blast-radius-OneFF-<timestamp>.json
```

## 📚 References

- **SKILL.md**: Complete workflow documentation
- **scripts/blast_radius.py**: Example BFS implementation
- **Parent skill**: `knowledge-graph-visualizer`

## 🛠️ Maintenance

**Version**: 1.0.0  
**Last updated**: 2026-06-11  
**Maintainer**: Architecture team  
**Dependencies**: decathlon-api-tool, knowledge-graph-query, delivery-metrics

---

## 🤝 Contributing

To improve this skill:

1. Update `SKILL.md` with new workflow steps
2. Add helper scripts to `scripts/`
3. Test with various incident targets
4. Document edge cases in SKILL.md
5. Share improvements with the team

## 📖 See Also

- `knowledge-graph-visualizer` — General KG visualization
- `incident-investigation` — Real-time incident analysis
- `business-impact-estimator` — Financial impact calculation
