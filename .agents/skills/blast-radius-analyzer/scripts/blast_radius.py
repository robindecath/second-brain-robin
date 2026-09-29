#!/usr/bin/env python3
"""
Blast Radius Analyzer — BFS Analysis + Report Generation (Steps 6 & 7)

Performs BFS traversal on a graph produced by build_graph_data.py to find all
downstream products/components and impacted User Journeys, then generates:
  - JSON impact report  (/tmp/blast-radius-<target>-<ts>.json)
  - Interactive HTML    (/tmp/blast-radius-<target>-<ts>.html)
  - Text summary        (printed to stdout)

Usage
-----
  # Incident node ID read from meta (output of build_graph_data.py)
  python3 blast_radius.py /tmp/kg_graph_oneff_20260611T001128Z.json

  # Explicit incident node ID (also works with legacy graph files)
  python3 blast_radius.py /tmp/kg_graph.json product:OneFF

  # Custom HTML template location
  BLAST_RADIUS_TEMPLATE=/path/to/blast-radius-viz.html python3 blast_radius.py ...

Output
------
  Prints two file paths to stdout (one per line):
    /tmp/blast-radius-OneFF-20260611_001128.json
    /tmp/blast-radius-OneFF-20260611_001128.html
"""

import json
import os
import pathlib
import sys
from collections import deque
from datetime import datetime

def find_blast_radius(graph_data, incident_node_id):
    """
    Perform BFS traversal to find all impacted downstream nodes.
    
    Args:
        graph_data: dict with {"nodes": [...], "edges": [...]}
        incident_node_id: str like "product:OneFF"
    
    Returns:
        dict with impact statistics
    """
    nodes = graph_data["nodes"]
    edges = graph_data["edges"]
    
    # Mark incident node
    incident_node = next((n for n in nodes if n["id"] == incident_node_id), None)
    if not incident_node:
        return {"error": f"Incident target '{incident_node_id}' not found"}
    
    incident_node["incident"] = True
    
    # BFS: Follow consumes edges in REVERSE (find who depends on failing node)
    impacted = set()
    queue = deque([incident_node_id])
    visited = {incident_node_id}
    
    while queue:
        current = queue.popleft()
        
        # Find all nodes that consume current node
        for edge in edges:
            if edge["target"] == current and edge["type"] == "consumes":
                consumer = edge["source"]
                if consumer not in visited:
                    visited.add(consumer)
                    impacted.add(consumer)
                    queue.append(consumer)
    
    # Mark impacted nodes
    for node in nodes:
        if node["id"] in impacted:
            node["impacted"] = True
    
    # Calculate impacted products first (already flagged above via BFS)
    impacted_products = [n for n in nodes if n.get("impacted") and n["group"] == "product"]
    impacted_product_ids = {n["id"] for n in impacted_products} | {incident_node_id}

    # Find impacted User Journeys — UJs linked to the failing product OR any product
    # in the blast radius.  A UJ is customer-impacted if ANY of its dependencies fail.
    # Two edge conventions are supported:
    #   "slo_link":          source=user_journey → target=product  (legacy)
    #   "moment_dependency": source=product      → target=user_journey (build_graph_data.py)
    impacted_ujs = set()

    for edge in edges:
        etype = edge.get("type", "")
        if etype == "slo_link":
            if edge["target"] in impacted_product_ids:
                impacted_ujs.add(edge["source"])
        elif etype == "moment_dependency":
            if edge["source"] in impacted_product_ids:
                impacted_ujs.add(edge["target"])

    for node in nodes:
        if node["id"] in impacted_ujs:
            node["impacted"] = True
    impacted_uj_nodes = [n for n in nodes if n.get("impacted") and n["group"] == "user_journey"]
    
    return {
        "incident": incident_node_id,
        "incident_name": incident_node["label"],
        "impacted_products_count": len(impacted_products),
        "impacted_user_journeys_count": len(impacted_uj_nodes),
        "tier1_impacted": len([n for n in impacted_products if n.get("tiering") == 1]),
        "external_consumers": len([n for n in impacted_products if n.get("external")]),
        "domains_affected": len(set(n.get("domain") for n in impacted_products if n.get("domain"))),
        "criticality_1_ujs": len([n for n in impacted_uj_nodes if n.get("criticality") == 1]),
        "total_blast_radius": 1 + len(impacted_products) + len(impacted_uj_nodes),
        "impacted_products": [
            {
                "name": n["label"],
                "tiering": n.get("tiering"),
                "domain": n.get("domain"),
                "team": n.get("team")
            }
            for n in impacted_products
        ],
        "impacted_user_journeys": [
            {
                "name": n["label"],
                "criticality": n.get("criticality"),
                "slo_target": n.get("slo_target"),
                "description": n.get("description")
            }
            for n in impacted_uj_nodes
        ]
    }


def generate_impact_report(impact_data, output_file):
    """
    Generate JSON impact report with timestamp and metadata.
    """
    report = {
        "incident_target": impact_data["incident_name"],
        "incident_time": datetime.now().isoformat(),
        "scope": "full_graph",
        "view_level": "product",
        "impact": {
            "failing_nodes": 1,
            "impacted_products": impact_data["impacted_products_count"],
            "impacted_user_journeys": impact_data["impacted_user_journeys_count"],
            "external_consumers": impact_data["external_consumers"],
            "tier1_impacted": impact_data["tier1_impacted"],
            "domains_affected": impact_data["domains_affected"],
            "criticality_1_ujs": impact_data["criticality_1_ujs"],
            "total_blast_radius": impact_data["total_blast_radius"]
        },
        "impacted_products": impact_data["impacted_products"],
        "impacted_user_journeys": impact_data["impacted_user_journeys"]
    }
    
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)
    
    return report


def print_summary(impact_data):
    """
    Print text summary to console.
    """
    print(f"\n## 💥 Blast Radius Analysis — {impact_data['incident_name']}\n")
    print("| Metric | Count | Details |")
    print("|--------|-------|---------|")
    print(f"| 🔴 Failing | 1 | {impact_data['incident_name']} |")
    print(f"| 🟠 Impacted Products | {impact_data['impacted_products_count']} | {impact_data['tier1_impacted']} Tier-1 |")
    print(f"| 💔 Impacted User Journeys | {impact_data['impacted_user_journeys_count']} | {impact_data['criticality_1_ujs']} Criticality-1 (CRITICAL) |")
    print(f"| 🌐 External Consumers | {impact_data['external_consumers']} | Cross-domain dependencies |")
    print(f"| 🎯 Domains Affected | {impact_data['domains_affected']} | |")
    print(f"| 💥 Total Blast Radius | {impact_data['total_blast_radius']} | Products + UJs affected |\n")
    
    if impact_data['criticality_1_ujs'] > 0:
        print("### 💔 CRITICAL Customer Impact\n")
        critical_ujs = [uj for uj in impact_data['impacted_user_journeys'] if uj.get('criticality') == 1]
        for uj in critical_ujs[:5]:  # Show first 5
            print(f"- **{uj['name']}** (Criticality 1)")
        print()


def find_template_path() -> str:
    """
    Resolve path to blast-radius-viz.html template.

    Search order:
      1. BLAST_RADIUS_TEMPLATE env var
      2. Adjacent templates/ folder (sibling of this script's parent)
    """
    env_path = os.environ.get("BLAST_RADIUS_TEMPLATE")
    if env_path and os.path.isfile(env_path):
        return env_path

    this_dir = pathlib.Path(__file__).resolve().parent
    candidate = (this_dir / ".." / "templates" / "blast-radius-viz.html").resolve()
    if candidate.is_file():
        return str(candidate)

    raise FileNotFoundError(
        "Cannot find blast-radius-viz.html template. "
        "Set BLAST_RADIUS_TEMPLATE env var or ensure the templates/ folder "
        "exists as a sibling of the scripts/ folder."
    )


def _compute_severity(impact_data: dict) -> tuple[str, str]:
    """Return (severity_label, css_class) based on impact counts."""
    tier1 = impact_data.get("tier1_impacted", 0)
    crit1 = impact_data.get("criticality_1_ujs", 0)
    products = impact_data.get("impacted_products_count", 0)
    if tier1 >= 10 or crit1 >= 5 or products >= 50:
        return "CRITICAL", "critical"
    if tier1 >= 3 or crit1 >= 1 or products >= 20:
        return "HIGH", "high"
    if tier1 >= 1 or products >= 5:
        return "MEDIUM", "medium"
    return "LOW", "low"


def generate_html(impact_data: dict, graph_data: dict, output_file: str, scope: str = "Full Graph") -> str:
    """
    Generate interactive HTML visualization by filling in the blast-radius-viz.html template.

    Converts graph nodes/edges to Cytoscape.js format and replaces all {{PLACEHOLDER}} tokens.
    """
    template_path = find_template_path()
    with open(template_path, "r") as f:
        html = f.read()

    # Build Cytoscape.js elements from flat nodes/edges
    cyto_elements = (
        [{"data": n} for n in graph_data.get("nodes", [])]
        + [{"data": e} for e in graph_data.get("edges", [])]
    )

    severity_label, severity_css = _compute_severity(impact_data)

    replacements = {
        "{{INCIDENT_TARGET}}":       impact_data["incident_name"],
        "{{SCOPE}}":                 scope,
        "{{GRAPH_DATA_JSON}}":       json.dumps(cyto_elements),
        "{{FAILING_COUNT}}":         "1",
        "{{IMPACTED_PRODUCTS}}":     str(impact_data["impacted_products_count"]),
        "{{TIER1_COUNT}}":           str(impact_data["tier1_impacted"]),
        "{{UJ_COUNT}}":              str(impact_data["impacted_user_journeys_count"]),
        "{{CRIT1_COUNT}}":           str(impact_data["criticality_1_ujs"]),
        "{{DOMAINS_COUNT}}":         str(impact_data["domains_affected"]),
        "{{REVENUE_LOSS}}":          "N/A",
        "{{PER_MINUTE}}":            "N/A",
        "{{SEVERITY_LEVEL}}":        severity_label,
        "{{SEVERITY_CSS}}":          severity_css,
        "{{IMPACTED_PRODUCTS_JSON}}": json.dumps(impact_data.get("impacted_products", [])),
        "{{IMPACTED_UJS_JSON}}":     json.dumps(impact_data.get("impacted_user_journeys", [])),
    }
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    with open(output_file, "w") as f:
        f.write(html)

    return output_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python blast_radius.py <graph_json_file> [incident_node_id]")
        print("  incident_node_id is optional when the file was produced by build_graph_data.py")
        print("  (the incident node is then read from meta.incident_node_id)")
        print("Example: python blast_radius.py /tmp/kg_graph_oneff_20260611T001128Z.json")
        print("         python blast_radius.py /tmp/kg_graph.json product:OneFF")
        sys.exit(1)

    graph_file = sys.argv[1]

    # Load graph data
    with open(graph_file, "r") as f:
        raw = json.load(f)

    # Support both formats:
    #   - legacy: {"nodes": [...], "edges": [...]}
    #   - build_graph_data.py: {"meta": {...}, "nodes": [...], "edges": [...]}
    meta = raw.get("meta", {})
    graph_data = raw  # nodes/edges are always at top level

    # Resolve incident_id from CLI arg or meta.incident_node_id
    if len(sys.argv) >= 3:
        incident_id = sys.argv[2]
    elif meta.get("incident_node_id"):
        incident_id = meta["incident_node_id"]
        print(f"Incident node from graph meta: {incident_id}")
    else:
        print("ERROR: incident_node_id required (not found in CLI args or meta.incident_node_id)")
        sys.exit(1)
    
    # Perform analysis
    impact_data = find_blast_radius(graph_data, incident_id)
    
    if "error" in impact_data:
        print(f"ERROR: {impact_data['error']}")
        sys.exit(1)
    
    # Generate outputs
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    safe_name = incident_id.split(':')[-1]
    output_json = f"/tmp/blast-radius-{safe_name}-{ts}.json"
    output_graph = f"/tmp/blast-radius-{safe_name}-graph-{ts}.json"
    output_html = f"/tmp/blast-radius-{safe_name}-{ts}.html"

    scope = meta.get("scope", "full_graph")
    scope_label = "Full Graph" if scope == "full_graph" else scope

    generate_impact_report(impact_data, output_json)

    # Output the marked graph (with incident/impacted flags) for the canvas
    marked_graph = {
        "meta": meta,
        "nodes": graph_data["nodes"],
        "edges": graph_data["edges"],
        "financial": graph_data.get("financial")
    }
    with open(output_graph, "w") as f:
        json.dump(marked_graph, f)

    try:
        generate_html(impact_data, graph_data, output_html, scope=scope_label)
        html_generated = True
    except FileNotFoundError as exc:
        print(f"WARNING: HTML not generated — {exc}", file=sys.stderr)
        html_generated = False

    # Print summary
    print_summary(impact_data)
    print(f"**Impact report**: {output_json}")
    print(f"**Marked graph (for canvas)**: {output_graph}")
    if html_generated:
        print(f"**HTML visualization**: {output_html}")
