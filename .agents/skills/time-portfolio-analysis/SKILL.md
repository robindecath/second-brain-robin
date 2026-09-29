---
name: time-portfolio-analysis
description: >
  Generate an interactive TIME (Technology Investment Management & Evaluation) Portfolio
  Analysis for any domain with quadrant visualization, timeline evolution, lifecycle
  analysis, strategy recommendations, and executive summary.
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
metadata:
  audience: all
  domain: platform-engineering
  api: graphql+rest
  mcp_required: false
---

# TIME Portfolio Analysis

## When to Use This Skill

Invoke this skill when:
- User requests a "TIME portfolio analysis" or "TIME analysis"
- User wants to visualize a domain's product portfolio
- User asks for strategic assessment of a product domain
- User wants to see portfolio evolution over time

## How to Invoke

```
I need to generate a TIME portfolio analysis for [DOMAIN_NAME]
```

Replace [DOMAIN_NAME] with the target domain (e.g., "ORDER", "PAYMENT", "BUSINESS CAPABILITY PLATFORM").

## What the Skill Does

The skill executes these steps automatically:

1. **Query AppReferential Knowledge Graph** for all products in the specified domain
2. **Enrich with Synthetic Metrics**:
   - Tech performance scores (correlated with lifecycle and business scores)
   - Budget allocations (based on product tiering)
3. **Generate Historical Timeline** (5 quarters by default):
   - Realistic score variations (±3-15 points)
   - Lifecycle transitions (GA→BETA, EOL→EOS)
   - Budget fluctuations (5-15%)
4. **Create Interactive HTML Visualization**
5. **Start HTTP Server** on an available port
6. **Open Browser Canvas** with the visualization

## Visualization Features

### 📊 TIME Quadrant Chart
- X-axis: Tech Performance (0-100)
- Y-axis: Business Value (0-100)
- Bubble size: Budget allocation
- Color: Lifecycle stage
- Framework labels: INVEST, IMPROVE, MAINTAIN, ELIMINATE

### 📅 Timeline Slider
- Sticky at top (compacts when scrolling)
- Explore 5 quarters (Q1-2025 to Q1-2026)
- Real-time updates: chart, lifecycle, strategies, summary

### 📊 Lifecycle Distribution
- Doughnut chart: Product count by stage
- Bar chart: Budget allocation by stage
- Statistics panel with averages

### 📋 Strategy Recommendations
Seven strategic buckets:
- 🚀 **D - Accelerate**: High value + high tech (invest heavily)
- 🔄 **G - Replace/Buy**: High value + low tech (rewrite or buy)
- 🔧 **F - Improve**: Medium-high value + medium-high tech (optimize)
- ⚠️ **B - Rescue**: Medium value + medium tech (stabilize)
- 📈 **C - Increase Value**: Medium value + high tech (drive adoption)
- 💰 **E - Reduce Cost**: Low value + high tech (consolidate)
- 🌅 **A - Sunset**: Low value + low tech (phase out)

### ⭐ Executive Summary
- Portfolio health score
- Key metrics dashboard (products, budget, health, stars)
- Strategic priorities list
- Risk assessment

## Example Usage

### User Request
```
Generate a TIME portfolio analysis for the ORDER domain
```

### Agent Actions
1. Read this skill file
2. Invoke `knowledge-graph-query` to query ORDER products
3. Enrich 42 products with tech performance and budget data
4. Generate 5 quarters of timeline with variations
5. Create `/tmp/order_portfolio_analysis.html` from template
6. Start HTTP server: `python3 -m http.server 9999 --directory /tmp`
7. Open browser canvas at `http://localhost:9999/order_portfolio_analysis.html`
8. Report: "✅ TIME Portfolio Analysis ready for ORDER domain (42 products, €187M budget)"

## Template Location

The HTML template is stored at:
```
~/.agents/skills/time-portfolio-analysis/template.html
```

This is a self-contained file (~160KB) with:
- All CSS styles embedded
- Chart.js library via CDN
- Complete JavaScript logic
- Placeholder for portfolio data injection

## Data Injection

The skill replaces these placeholders in the template:
- `{{DOMAIN_NAME}}` → Actual domain name
- `{{PORTFOLIO_DATA}}` → JSON with timeline data
- `{{CURRENT_QUARTER}}` → Latest quarter (e.g., "Q1-2026")

## Dependencies

- **knowledge-graph-query**: Query product data from AppReferential
- **Python 3**: Generate data and serve HTTP
- **Modern browser**: Display interactive visualization

## Output Format

The skill reports completion with:
- ✅ Success message
- Domain name
- Product count
- Total budget
- Browser canvas URL

## Error Handling

If domain not found:
- Try correcting domain name (e.g., "BCP" → "BUSINESS CAPABILITY PLATFORM")
- Suggest using `knowledge-graph-query` to list available domains

If HTTP port unavailable:
- Try alternate ports (9999, 8888, 8000)
- Report actual port in use

## Notes

- The template is based on the stable working version created on 2026-06-09
- All data calculations are deterministic with seeded randomness for consistency
- The visualization is fully self-contained and works offline once loaded

## Author

Decathlon Architecture Team

## Version

1.0.0 (Stable - 2026-06-09)
