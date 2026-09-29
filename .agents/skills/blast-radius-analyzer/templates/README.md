# Blast Radius Visualization Template

## Overview

This HTML template provides a complete, production-ready visualization for blast radius analysis with all standard controls including the **Blast Radius Only** button.

## Location

`templates/blast-radius-viz.html`

## Features

### Controls (Top-Left Panel)

1. **🔄 Fit** — Reset view to full graph
2. **🎯 Focus Impact** — Zoom to impacted nodes only
3. **🔥 Blast Radius Only** — Hide all non-impacted nodes (NEW)
4. **🔗 External Consumers** — Toggle external domain consumers
5. **💔 User Journeys** — Toggle User Journey nodes
6. **🏷️ Labels** — Toggle node labels

### Impact Dashboard (Top-Right Panel)

- Failing nodes count
- Impacted products count
- Tier-1 products affected
- User Journeys impacted
- Criticality-1 UJs
- Domains affected
- Revenue loss estimate
- Per-minute loss rate

### Node Styling

- 🔴 **Red node with thick border** = Incident (failing)
- 🟠 **Orange nodes** = Impacted (downstream consumers)
- 💔 **Red diamonds** = User Journeys
- 🔵 **Blue arrows** = API consumption edges
- 🔴 **Red dashed lines** = SLO links (product → UJ)

## Usage

### 1. Read the Template

```bash
cat templates/blast-radius-viz.html
```

### 2. Replace Placeholders

```python
import json

# Load template
with open("templates/blast-radius-viz.html", "r") as f:
    html_template = f.read()

# Replace placeholders
html = html_template.replace("{{INCIDENT_TARGET}}", "OneFF")
html = html.replace("{{SCOPE}}", "Full Graph")
html = html.replace("{{GRAPH_DATA_JSON}}", json.dumps(cytoscape_elements))
html = html.replace("{{FAILING_COUNT}}", "1")
html = html.replace("{{IMPACTED_PRODUCTS}}", "33")
html = html.replace("{{TIER1_COUNT}}", "13")
html = html.replace("{{UJ_COUNT}}", "8")
html = html.replace("{{CRIT1_COUNT}}", "3")
html = html.replace("{{DOMAINS_COUNT}}", "8")
html = html.replace("{{REVENUE_LOSS}}", "EUR 32,110")
html = html.replace("{{PER_MINUTE}}", "EUR 6,422/min")

# Write output
with open("/tmp/blast-radius-oneff.html", "w") as f:
    f.write(html)
```

### 3. Prepare Graph Data

Cytoscape.js elements format:

```json
{
  "nodes": [
    {
      "data": {
        "id": "product:OneFF",
        "label": "OneFF",
        "group": "product",
        "tiering": 1,
        "domain": "BUSINESS CAPABILITY PLATFORM",
        "team": "CE-ONEFF",
        "color": "#e53e3e",
        "size": 40,
        "incident": true
      }
    },
    {
      "data": {
        "id": "product:OneCheckout",
        "label": "OneCheckout",
        "group": "product",
        "tiering": 1,
        "domain": "BUSINESS CAPABILITY PLATFORM",
        "team": "CE-ONECHECKOUT",
        "color": "#c05621",
        "size": 40,
        "impacted": true
      }
    },
    {
      "data": {
        "id": "user_journey:abc123",
        "label": "Lower Funnel REVAMP Checkout",
        "group": "user_journey",
        "criticality": 1,
        "slo_target": 99.9,
        "color": "#e53e3e",
        "size": 30,
        "impacted": true
      }
    }
  ],
  "edges": [
    {
      "data": {
        "id": "edge1",
        "source": "product:OneCheckout",
        "target": "product:OneFF",
        "type": "consumes"
      }
    },
    {
      "data": {
        "id": "edge2",
        "source": "user_journey:abc123",
        "target": "product:OneCheckout",
        "type": "slo_link"
      }
    }
  ]
}
```

### 4. Open in Browser

```bash
open /tmp/blast-radius-oneff.html  # macOS
xdg-open /tmp/blast-radius-oneff.html  # Linux
start /tmp/blast-radius-oneff.html  # Windows
```

## Blast Radius Only Button Details

### JavaScript Implementation

```javascript
let blastOnlyActive = false;

function toggleBlastOnly() {
  blastOnlyActive = !blastOnlyActive;
  const btn = document.getElementById('btn-blast-only');
  
  if (blastOnlyActive) {
    // Hide all nodes that are NOT incident or impacted
    cy.nodes('[!incident][!impacted]').style('display', 'none');
    cy.edges().style('display', function(edge) {
      const src = edge.source();
      const tgt = edge.target();
      return (src.visible() && tgt.visible()) ? 'element' : 'none';
    });
    
    // Auto-zoom to blast radius
    const blastNodes = cy.nodes('[?incident], [?impacted]').filter(':visible');
    if (blastNodes.length > 0) {
      cy.fit(blastNodes, 80);
    }
    
    btn.classList.remove('btn-neutral');
    btn.classList.add('btn-active');
  } else {
    // Restore all nodes (respect other toggle states)
    cy.nodes().style('display', 'element');
    
    // Re-apply toggle states
    if (!showExternalConsumers) {
      cy.nodes('[?external_consumer]').style('display', 'none');
    }
    if (!showUserJourneys) {
      cy.nodes('[group="user_journey"]').style('display', 'none');
    }
    
    // Show edges where both endpoints are visible
    cy.edges().style('display', function(edge) {
      const src = edge.source();
      const tgt = edge.target();
      return (src.visible() && tgt.visible()) ? 'element' : 'none';
    });
    
    cy.fit();
    btn.classList.remove('btn-active');
    btn.classList.add('btn-neutral');
  }
}
```

### Behavior

- **ON** (blue button):
  - Hides org, domains, subdomains, unaffected products
  - Shows only: 1 incident + N impacted products + M UJs
  - Auto-zooms to blast radius
  - Respects UJ and external consumer toggle states
  
- **OFF** (gray button):
  - Restores full graph
  - Re-applies other toggle states (UJs, external consumers)
  - Resets zoom to full view

### Use Cases

1. **Executive Presentation**: "Here's exactly what breaks if OnePay fails"
2. **Incident Response**: Focus on affected services during outage
3. **Architecture Review**: Visual proof of single point of failure
4. **Team Communication**: "Your service depends on these 5 products"
5. **Documentation**: Screenshot for runbooks and playbooks

## Customization

### Change Color Scheme

Edit the CSS color variables:

```css
/* Incident node */
node[?incident] { background-color: #e53e3e; }  /* Red */

/* Impacted nodes */
node[?impacted] { background-color: #c05621; }  /* Orange */

/* User Journeys */
node[group="user_journey"] { background-color: #e53e3e; }  /* Red */
```

### Adjust Layout

The template uses **optimized fcose parameters** for organic network visualization:

```javascript
layout: {
  name: 'fcose',
  quality: 'proof',
  randomize: true,           // Prevents linear layout
  animate: true,             // 1-second spread animation
  animationDuration: 1000,   // Animation time in ms
  nodeSeparation: 200,       // Generous node spacing
  nodeRepulsion: 15000,      // Strong push-apart force
  idealEdgeLength: 150,      // Long edges for clarity
  edgeElasticity: 0.45,      // Edge flexibility
  nestingFactor: 0.1,        // Compound node handling
  gravity: 0.1,              // Low gravity (organic spread)
  numIter: 5000,             // High iteration count
  tile: true,                // Enable 2D tiling
  tilingPaddingVertical: 50,
  tilingPaddingHorizontal: 50,
  gravityRangeCompound: 1.5,
  gravityCompound: 1.0,
  gravityRange: 3.8,
  initialEnergyOnIncremental: 0.3
}
```

**Key parameters:**
- **randomize: true** — Crucial for preventing linear/hierarchical layout
- **animate: true** — Shows nodes spreading out in real-time
- **nodeRepulsion: 15000** — High value prevents overlapping (2.5x default)
- **gravity: 0.1** — Low value creates organic spread instead of center collapse
- **tile: true** — Enables 2D distribution algorithm

### Add New Metrics

Add to Impact Dashboard:

```html
<div class="metric">
  <span class="metric-label">New Metric</span>
  <span class="metric-value">{{NEW_VALUE}}</span>
</div>
```

## Dependencies

- **Cytoscape.js**: v3.31.0 (graph visualization)
- **layout-base**: v2.0.1 (layout algorithm base)
- **cose-base**: v2.2.0 (COSE algorithm)
- **cytoscape-fcose**: v2.2.0 (force-directed layout)

All loaded via CDN — no local dependencies required.

## Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## Performance

- **Small graphs** (<100 nodes): Instant render
- **Medium graphs** (100-500 nodes): 1-2 seconds
- **Large graphs** (500-1000 nodes): 2-5 seconds
- **Very large graphs** (1000+ nodes): Consider filtering at data level

## Troubleshooting

### Graph doesn't render

1. Check browser console for JavaScript errors
2. Verify `{{GRAPH_DATA_JSON}}` is valid JSON
3. Ensure all CDN dependencies loaded (check Network tab)

### Blast Radius Only button doesn't work

1. Verify nodes have `incident` or `impacted` flags
2. Check JavaScript console for errors
3. Ensure Cytoscape.js selectors are correct: `[?incident]`, `[?impacted]`

### Dashboard shows wrong values

1. Verify all `{{PLACEHOLDER}}` values were replaced
2. Check for typos in placeholder names
3. Ensure values are strings (wrap numbers in quotes)

## Version History

- **v1.0.0** (2026-06-11): Initial release with Blast Radius Only button

## License

Internal use only — Decathlon Architecture Team
