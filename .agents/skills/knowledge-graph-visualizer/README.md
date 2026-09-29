# Knowledge Graph Visualizer Skill

## 📌 Overview

The **Knowledge Graph Visualizer** skill generates an interactive network graph of Decathlon's complete digital asset topology by combining:

- **AppReferential Knowledge Graph**: Products, components, API dependencies
- **DeliveryMetrics API**: User Journeys and their SLO dependencies
- **Asset tiering & governance**: Domain, subdomain, and team ownership

The visualization renders the full hierarchy (Organization → Domains → Subdomains → Products → Components) with interactive filtering, relationship mapping, and incident impact analysis.

## 🎯 What It Does

1. **Fetches data** from:
   - AppReferential Knowledge Graph (GraphQL) — all products, components, API dependencies
   - DeliveryMetrics API (REST) — User Journeys and SLO key mappings

2. **Builds the graph** with:
   - Node types: domain, subdomain, product, component, user_journey
   - Edge types: hierarchy links, API producer/consumer relationships, SLO dependencies

3. **Supports multiple view scopes**:
   - Full graph (all assets)
   - Domain/subdomain filtered views
   - Product-specific views (product + its components)
   - Incident impact mode (traces cascade from a failing asset to all affected user journeys)

4. **Renders interactive HTML** using Cytoscape.js with:
   - Force-directed layout (fcose)
   - Color-coded nodes by type
   - Edge type indicators (API, SLO, hierarchy, etc.)
   - Real-time search and filtering
   - Tooltip information on hover

## 🚀 Use Cases

- **Visualize the full asset hierarchy** — understand organizational structure
- **Map API dependencies** — find producer/consumer relationships between components
- **Assess incident risk** — show blast radius when a product/component fails
- **Explore domain architecture** — isolate and analyze specific domains
- **Understand User Journey exposure** — which customer experiences depend on which assets

## 📦 Outputs

- **Interactive HTML file** (self-contained, no external dependencies)
- **Text summary** with entity counts and statistics
- **Graph data** in JSON format (nodes and edges)

## 🔧 Implementation

The skill orchestrates dependent skills:

1. **decathlon-api-tool** — Authenticated HTTP calls to Decathlon APIs
2. **knowledge-graph-query** — GraphQL queries to AppReferential
3. **delivery-metrics** — REST calls to DeliveryMetrics for User Journeys

The generated HTML embeds the graph data as JSON and uses Cytoscape.js to render the interactive visualization.

---

See **SKILL.md** for detailed usage, API facts, examples, and implementation details.
