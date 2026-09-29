# TIME Portfolio Analysis - Reusable Package

## ✅ Created: Reusable Skill

**Location**: `.agents/skills/time-portfolio-analysis/`

### Files
- `SKILL.md` (4.6KB) - Skill documentation and usage guide
- `template.html` (158KB) - Complete HTML template with all features

## How Teammates Can Use It

### Method 1: Natural Language (Recommended)
```
Generate a TIME portfolio analysis for the ORDER domain
```

```
Create a TIME analysis for PAYMENT with the full timeline
```

### Method 2: Explicit Skill Invocation
```
Use the time-portfolio-analysis skill to analyze the MEMBER domain
```

## What It Generates

A complete interactive web application with:

1. **📊 TIME Quadrant Chart**
   - 50+ products positioned by business value (y) vs tech performance (x)
   - Bubble size = budget
   - Color = lifecycle stage
   - Interactive hover details

2. **📅 Timeline Slider** (Sticky)
   - Explore 5 quarters of evolution
   - Compacts when scrolling
   - Updates all sections in real-time

3. **📊 Lifecycle Distribution**
   - Doughnut chart: Product counts
   - Bar chart: Budget allocation
   - Statistics panel

4. **📋 Strategy Recommendations**
   - 7 strategic buckets (Accelerate, Replace/Buy, Improve, etc.)
   - Product lists per strategy
   - Budget totals

5. **⭐ Executive Summary**
   - Portfolio health score
   - 4 key metrics dashboard
   - Strategic priorities
   - Risk assessment

## Technical Approach

The skill will:
1. **Query** AppReferential Knowledge Graph for domain products
2. **Enrich** with synthetic tech performance & budget (realistic algorithms)
3. **Generate** timeline data with quarterly variations
4. **Inject** data into HTML template
5. **Serve** via HTTP server (port 9999 or alternate)
6. **Open** in browser canvas automatically

## Data Sources

- **Real**: Product names, business scores, lifecycle stages, tiering (from AppReferential)
- **Synthetic**: Tech performance scores, budget allocations (generated algorithmically)
- **Timeline**: Historical variations (±3-15 points, lifecycle transitions, budget fluctuations)

## Dependencies

- `knowledge-graph-query` skill (for querying AppReferential)
- Python 3 with http.server
- Modern browser with JavaScript

## Agent Workflow

When user requests analysis:

1. Agent reads `.agents/skills/time-portfolio-analysis/SKILL.md`
2. Invokes `knowledge-graph-query` to get products
3. Applies enrichment algorithms:
   ```python
   tech_performance = lifecycle_base + business_correlation + tier_adjustment + random_noise
   budget = tier_range[min, max] * random()
   ```
4. Generates timeline (5 quarters) with variations
5. Loads `template.html` and injects:
   - `{{DOMAIN_NAME}}` → e.g., "ORDER"
   - `{{PORTFOLIO_DATA}}` → JSON with all quarters
   - `{{CURRENT_QUARTER}}` → e.g., "Q1-2026"
6. Writes to `/tmp/[domain]_portfolio_analysis.html`
7. Starts HTTP server: `python3 -m http.server 9999 --directory /tmp`
8. Opens browser canvas: `http://localhost:9999/[domain]_portfolio_analysis.html`
9. Reports completion with summary

## Output Example

```
✅ TIME Portfolio Analysis ready for ORDER domain

📊 Analysis Summary:
   • 42 products analyzed
   • €187M total portfolio budget
   • Health score: 68% (moderate)
   • 6 star products identified

🌐 View at: http://localhost:9999/order_portfolio_analysis.html
```

## Consistency

- **Deterministic**: Same input = same output (seeded random)
- **Realistic**: Correlations between metrics (lifecycle ↔ tech, tier ↔ budget)
- **Professional**: Production-ready visualization with Decathlon branding

## Version

1.0.0 (Stable - 2026-06-09)

## Author

Decathlon Architecture Team

---

## Usage Summary

**For users**: Just ask "Generate TIME analysis for [DOMAIN]"

**For agents**: Read `.agents/skills/time-portfolio-analysis/SKILL.md` and follow the workflow

**Result**: Interactive portfolio analysis served at http://localhost:9999
