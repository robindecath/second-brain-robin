#!/usr/bin/env python3
"""
build_graph_data.py — Graph Data Builder for Blast Radius Analyzer

Fetches the complete dependency graph from:
  - AppReferential Knowledge Graph   (products, components, API edges)
  - DeliveryMetrics API              (User Journeys + product→UJ edges via UUID matching)

Covers blast-radius-analyzer SKILL.md Steps 3, 4, and 5 in one repeatable script,
producing a JSON file that is directly consumed by blast_radius.py (Step 6 BFS)
and the blast-radius-viz.html template (Step 7 visualization).

Usage
-----
  # Product/component as incident target
  python3 build_graph_data.py --target OneFF
  python3 build_graph_data.py --target OneFF --scope "BUSINESS CAPABILITY PLATFORM"
  python3 build_graph_data.py --target onepay-api --view-level component

  # User Journey as incident target
  python3 build_graph_data.py --target "Lower Funnel REVAMP Checkout"

  # Custom output path
  python3 build_graph_data.py --target OneFF --output /tmp/mygraph.json

  # Skip UJ fetching (faster, technical graph only)
  python3 build_graph_data.py --target OneFF --no-uj

  # Reuse cached API responses (1-hour TTL)
  python3 build_graph_data.py --target OneFF --cache

Output
------
  JSON file (default: /tmp/kg_graph_<target>_<timestamp>.json)

  Top-level keys:
    meta   — generation metadata + incident target info + graph statistics
    nodes  — flat node list (compatible with blast_radius.py and Cytoscape.js)
    edges  — flat edge list

  Node shape:
  {
    "id":        "product:OneFF",
    "label":     "OneFF",
    "group":     "product",          // org | domain | subdomain | product | component | user_journey
    "tiering":   1,                  // products only: 1|2|3|null
    "domain":    "BUSINESS CAPABILITY PLATFORM",
    "subdomain": "PAYMENT",
    "team":      "CE-ONEFF",
    "reference": "<UUID>",           // products only: KG reference UUID (matches DM product_uuids)
    "color":     "#2b6cb0",
    "size":      35
  }

  Edge shape:
  {
    "id":       "e:product:Consumer->product:Producer",
    "source":   "product:Consumer",
    "target":   "product:Producer",
    "type":     "consumes",          // contains | consumes | moment_dependency
    "external": false                // consumes edges only
  }

  For the Cytoscape.js HTML template each node/edge must be wrapped in {"data": ...}:
    cyto_nodes = [{"data": n} for n in graph["nodes"]]
    cyto_edges = [{"data": e} for e in graph["edges"]]
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import time
from datetime import datetime, timezone

# ─── Constants ─────────────────────────────────────────────────────────────────

KG_URL = "https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql"
DM_BASE = "https://api.decathlon.net/deliverymetrics"

CACHE_TTL_SECONDS = 3600  # 1 hour

CACHE_KG_FILE = "/tmp/kg_products_cache.json"
CACHE_API_FILE = "/tmp/kg_api_edges_cache.json"
CACHE_UJ_FILE = "/tmp/uj_data_cache.json"

# Node colors
COLOR_ORG = "#1a202c"
COLOR_DOMAIN = "#805ad5"
COLOR_TIER1 = "#2b6cb0"       # blue  — tier-1 product
COLOR_TIER2 = "#2f855a"       # green — tier-2 product
COLOR_TIER3 = "#4a5568"       # grey  — tier-3 / untiered product
COLOR_UJ_CRIT1 = "#e53e3e"    # red
COLOR_UJ_CRIT2 = "#dd6b20"    # orange
COLOR_UJ_CRIT3 = "#d69e2e"    # yellow
COLOR_UJ_CRIT4 = "#48bb78"    # green

# Node sizes
SIZE_ORG = 20
SIZE_DOMAIN = 18
SIZE_TIER1 = 35
SIZE_TIER2 = 25
SIZE_TIER3 = 20
SIZE_UJ = 28

# Component types excluded from the graph
SKIP_COMPONENT_TYPES = {"LIBRARY", "DOCUMENTATION"}

# ─── GraphQL queries ───────────────────────────────────────────────────────────

KG_PRODUCTS_QUERY = """
query Products($f: AssetFilter!, $n: Int!, $c: String) {
  assets(filter: $f, first: $n, after: $c) {
    totalCount
    edges {
      node {
        name
        id
        reference
        kind
        type
        tiering
        metadata
        components { name type }
      }
    }
    pageInfo { hasNextPage endCursor }
  }
}
"""

KG_API_COMPONENTS_QUERY = """
query ApiComponents($n: Int!, $c: String) {
  assets(filter: {kind: "component", type: "DECATHLON_API"}, first: $n, after: $c) {
    edges { node { name metadata } }
    pageInfo { hasNextPage endCursor }
  }
}
"""


# ─── Helpers ───────────────────────────────────────────────────────────────────

def find_api_script() -> str:
    """
    Resolve path to decathlon_api.py.

    Search order:
      1. DECATHLON_API_SCRIPT environment variable
    """
    env_path = os.environ.get("DECATHLON_API_SCRIPT")
    if env_path and os.path.isfile(env_path):
        return env_path

    raise FileNotFoundError(
        "Cannot find decathlon_api.py. "
        "Set DECATHLON_API_SCRIPT env var to the path of decathlon_api.py "
        "from the decathlon-api-tool skill."
    )


def api_call(script: str, method: str, url: str, data: dict | None = None) -> object:
    """Run one authenticated HTTP call via decathlon_api.py and return parsed JSON."""
    cmd = ["python3", script, "--method", method, "--url", url]
    if data:
        cmd += ["--data", json.dumps(data)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"API call failed [{method} {url}]:\n{result.stderr.strip()}"
        )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Non-JSON response from [{method} {url}]:\n{result.stdout[:400]}"
        ) from exc


def _cache_valid(path: str) -> bool:
    p = pathlib.Path(path)
    if not p.exists():
        return False
    return time.time() - p.stat().st_mtime < CACHE_TTL_SECONDS


def _load_cache(path: str) -> object:
    with open(path) as f:
        return json.load(f)


def _save_cache(path: str, data: object) -> None:
    with open(path, "w") as f:
        json.dump(data, f)


# ─── Step 3a: Fetch products from Knowledge Graph ─────────────────────────────

def fetch_products(script: str, scope: str | None, use_cache: bool) -> list[dict]:
    """
    Fetch all products (paginated) from the AppReferential Knowledge Graph.

    CRITICAL: The `reference` field contains the product UUID that matches
    DeliveryMetrics `product_uuids` in moments.  The `id` field is only a
    numeric internal ID and must NOT be used for UJ linking.
    """
    if use_cache and _cache_valid(CACHE_KG_FILE):
        data = _load_cache(CACHE_KG_FILE)
        print(f"[cache] {len(data)} products loaded from {CACHE_KG_FILE}", file=sys.stderr)
        return data

    print("Step 3a — Fetching products from Knowledge Graph...", file=sys.stderr)
    variables: dict = {"f": {"kind": "product"}, "n": 200}
    if scope:
        variables["f"]["metadataFilter"] = {"governance": {"domain": scope}}

    products: list[dict] = []
    page = 0
    while True:
        resp = api_call(script, "POST", KG_URL, {"query": KG_PRODUCTS_QUERY, "variables": variables})
        assets_data = resp["data"]["assets"]
        page += 1
        batch = [edge["node"] for edge in assets_data["edges"]]
        products.extend(batch)
        print(
            f"  Page {page}: {len(batch)} products "
            f"(running total {len(products)} / {assets_data['totalCount']})",
            file=sys.stderr,
        )
        if not assets_data["pageInfo"]["hasNextPage"]:
            break
        variables["c"] = assets_data["pageInfo"]["endCursor"]

    print(f"✅ Fetched {len(products)} products ({page} pages)", file=sys.stderr)
    if use_cache:
        _save_cache(CACHE_KG_FILE, products)
    return products


# ─── Step 3b: Fetch DECATHLON_API components (producer/consumer map) ──────────

def fetch_api_edges(script: str, use_cache: bool) -> list[dict]:
    """
    Fetch all DECATHLON_API components (5+ pages in production) and build
    component-level consumes edges using apis_provided / apis_consumed UUIDs.
    """
    if use_cache and _cache_valid(CACHE_API_FILE):
        data = _load_cache(CACHE_API_FILE)
        print(f"[cache] {len(data)} API edges loaded from {CACHE_API_FILE}", file=sys.stderr)
        return data

    print("Step 3b — Fetching DECATHLON_API components (producer/consumer map)...", file=sys.stderr)

    # uuid → producer component info
    provided_map: dict[str, dict] = {}
    # uuid → list of consumer component infos
    consumed_by: dict[str, list[dict]] = {}

    variables: dict = {"n": 200}
    page = 0
    while True:
        resp = api_call(script, "POST", KG_URL, {"query": KG_API_COMPONENTS_QUERY, "variables": variables})
        assets_data = resp["data"]["assets"]
        page += 1
        for edge in assets_data["edges"]:
            node = edge["node"]
            meta = node.get("metadata") or {}
            gov = meta.get("governance", {})
            name = node["name"]
            domain = gov.get("domain", "unknown")
            for uuid in meta.get("apis_provided", []):
                provided_map[uuid] = {"name": name, "domain": domain}
            for uuid in meta.get("apis_consumed", []):
                consumed_by.setdefault(uuid, []).append({"name": name, "domain": domain})
        print(f"  Page {page}: {len(assets_data['edges'])} API components", file=sys.stderr)
        if not assets_data["pageInfo"]["hasNextPage"]:
            break
        variables["c"] = assets_data["pageInfo"]["endCursor"]

    # Build component→component edges (deduplicated)
    edges: list[dict] = []
    seen: set[tuple] = set()
    for api_uuid, producer in provided_map.items():
        for consumer in consumed_by.get(api_uuid, []):
            if consumer["name"] == producer["name"]:
                continue
            key = (consumer["name"], producer["name"])
            if key in seen:
                continue
            seen.add(key)
            edges.append({
                "id": f"api:{consumer['name']}->{producer['name']}",
                "source": f"component:{consumer['name']}",
                "target": f"component:{producer['name']}",
                "type": "consumes",
                "external": consumer["domain"] != producer["domain"],
            })

    print(
        f"✅ Built {len(edges)} component-level API edges "
        f"({page} pages, {len(provided_map)} producing APIs)",
        file=sys.stderr,
    )
    if use_cache:
        _save_cache(CACHE_API_FILE, edges)
    return edges


# ─── Step 4a-4b: Fetch User Journeys with moments ─────────────────────────────

def fetch_user_journeys(script: str, use_cache: bool) -> list[dict]:
    """
    Fetch all User Journeys from DeliveryMetrics (paginated v2 list, then v1 moments).

    Strategy: fetch full UJ list via v2, then enrich each with moments via v1.
    The v2 API does NOT return product_uuids — v1 with_moment_list=true is required.
    """
    if use_cache and _cache_valid(CACHE_UJ_FILE):
        data = _load_cache(CACHE_UJ_FILE)
        print(f"[cache] {len(data)} User Journeys loaded from {CACHE_UJ_FILE}", file=sys.stderr)
        return data

    # 4a — paginated UJ list from v2
    print("Step 4a — Fetching User Journey list (v2 API)...", file=sys.stderr)
    uj_index: dict[str, dict] = {}
    page = 0
    while True:
        url = f"{DM_BASE}/api/v2/user_journeys?page={page}&size=50"
        resp = api_call(script, "GET", url)
        # Handle both list (legacy) and paginated (current) response shapes
        if isinstance(resp, list):
            items: list[dict] = resp
            has_more = False
        else:
            items = resp.get("content", [])
            pg = resp.get("page", {})
            has_more = page < pg.get("total_pages", 1) - 1
        for uj in items:
            uj_index[uj["uuid"]] = uj
        print(f"  Page {page}: {len(items)} UJs (running total {len(uj_index)})", file=sys.stderr)
        if not has_more:
            break
        page += 1

    # 4b — fetch moments for each UJ from v1
    print(f"Step 4b — Fetching moments for {len(uj_index)} User Journeys (v1 API)...", file=sys.stderr)
    enriched: list[dict] = []
    for idx, (uj_uuid, uj_meta) in enumerate(uj_index.items(), 1):
        url = (
            f"{DM_BASE}/api/v1/user_journeys"
            f"?user_journey_uuid_list={uj_uuid}&with_moment_list=true"
        )
        try:
            resp = api_call(script, "GET", url)
            uj_data = resp[0] if isinstance(resp, list) and resp else resp
            uj_meta["moments"] = uj_data.get("moments", [])
            uj_meta.setdefault("slo_target", uj_data.get("slo_target"))
        except Exception as exc:
            print(
                f"  WARNING: Could not fetch moments for UJ {uj_uuid}: {exc}",
                file=sys.stderr,
            )
            uj_meta["moments"] = []
        enriched.append(uj_meta)
        if idx % 10 == 0:
            print(f"  Processed {idx}/{len(uj_index)} UJs...", file=sys.stderr)
        time.sleep(0.3)  # rate limiting

    print(f"✅ Fetched {len(enriched)} User Journeys with moments", file=sys.stderr)
    if use_cache:
        _save_cache(CACHE_UJ_FILE, enriched)
    return enriched


# ─── Step 4c-4d: Build product→UJ edges via UUID matching ─────────────────────

def build_uj_edges(products: list[dict], user_journeys: list[dict]) -> list[dict]:
    """
    Create product→UJ moment_dependency edges by matching DeliveryMetrics
    `product_uuids` against the KG `reference` field.

    CRITICAL: Use `reference` (not `id`) — the KG `id` is a numeric internal ID,
    while `reference` is the actual UUID that matches DeliveryMetrics product_uuids.
    """
    print("Step 4c — Building product→UJ edges (UUID matching)...", file=sys.stderr)

    product_by_uuid: dict[str, dict] = {
        p["reference"]: p for p in products if p.get("reference")
    }
    print(
        f"  UUID map: {len(product_by_uuid)}/{len(products)} products have reference UUIDs",
        file=sys.stderr,
    )

    edges: list[dict] = []
    matched_ujs = 0

    for uj in user_journeys:
        uj_uuid = uj.get("uuid", "")
        products_in_uj: set[str] = set()
        moment_details: dict[str, list[dict]] = {}

        for moment in uj.get("moments", []):
            for p_uuid in moment.get("product_uuids", []):
                if p_uuid not in product_by_uuid:
                    continue
                products_in_uj.add(p_uuid)
                moment_details.setdefault(p_uuid, []).append({
                    "moment_uuid": moment.get("uuid", ""),
                    "moment_name": moment.get("name", ""),
                    "sequence": moment.get("sequence"),
                })

        if products_in_uj:
            matched_ujs += 1

        for p_uuid in products_in_uj:
            product = product_by_uuid[p_uuid]
            edges.append({
                "id": f"uj:{product['name']}--{uj_uuid}",
                "source": f"product:{product['name']}",
                "target": f"user_journey:{uj_uuid}",
                "type": "moment_dependency",
                "metadata": {
                    "product_uuid": p_uuid,
                    "uj_uuid": uj_uuid,
                    "uj_name": uj.get("name", ""),
                    "uj_criticality": uj.get("criticality"),
                    "moments": moment_details[p_uuid],
                },
            })

    print(
        f"✅ Created {len(edges)} product→UJ edges "
        f"({matched_ujs}/{len(user_journeys)} UJs linked)",
        file=sys.stderr,
    )
    return edges


# ─── Step 5: Build graph data model ───────────────────────────────────────────

def _product_color(tiering: int | None) -> str:
    if tiering == 1:
        return COLOR_TIER1
    if tiering == 2:
        return COLOR_TIER2
    return COLOR_TIER3


def _product_size(tiering: int | None) -> int:
    if tiering == 1:
        return SIZE_TIER1
    if tiering == 2:
        return SIZE_TIER2
    return SIZE_TIER3


def _uj_color(criticality: int | None) -> str:
    return {1: COLOR_UJ_CRIT1, 2: COLOR_UJ_CRIT2, 3: COLOR_UJ_CRIT3}.get(criticality, COLOR_UJ_CRIT4)


def build_graph_model(
    products: list[dict],
    api_edges: list[dict],
    user_journeys: list[dict],
    uj_edges: list[dict],
    view_level: str,
) -> dict:
    """
    Assemble the complete node/edge graph ready for BFS analysis.

    Node groups:
      org, domain, subdomain, product (or component), user_journey

    Edge types:
      contains          — hierarchy (org→domain→subdomain→product→component)
      consumes          — API dependency (consumer→producer)
      moment_dependency — product→user_journey (via UUID matching)

    When view_level=product (default):
      - Component nodes are omitted (products are the leaves)
      - Component-level API edges are aggregated to product-to-product edges

    When view_level=component:
      - Component nodes are included under their parent product
      - Raw component-level API edges are included unchanged
    """
    print(f"Step 5 — Building graph model (view_level={view_level})...", file=sys.stderr)

    nodes: list[dict] = []
    edges: list[dict] = []

    # Org root
    nodes.append({
        "id": "org:decathlon",
        "label": "Decathlon",
        "group": "org",
        "color": COLOR_ORG,
        "size": SIZE_ORG,
    })

    domains_seen: set[str] = set()
    subdomains_seen: set[str] = set()

    for product in products:
        meta = product.get("metadata") or {}
        gov = meta.get("governance", {})
        domain = gov.get("domain") or "unknown"
        subdomain = gov.get("sub_domain") or ""
        team = gov.get("support_group") or ""
        tiering = product.get("tiering")
        name = product["name"]
        p_id = f"product:{name}"

        # Domain node
        d_id = f"domain:{domain}"
        if domain not in domains_seen:
            domains_seen.add(domain)
            nodes.append({"id": d_id, "label": domain, "group": "domain", "color": COLOR_DOMAIN, "size": SIZE_DOMAIN})
            edges.append({"id": f"e:org->{d_id}", "source": "org:decathlon", "target": d_id, "type": "contains"})

        # Subdomain node
        sd_id = f"subdomain:{subdomain}" if subdomain else None
        if subdomain:
            sd_key = f"{domain}::{subdomain}"
            if sd_key not in subdomains_seen:
                subdomains_seen.add(sd_key)
                nodes.append({"id": sd_id, "label": subdomain, "group": "subdomain", "color": COLOR_DOMAIN, "size": SIZE_DOMAIN})
                edges.append({"id": f"e:{d_id}->{sd_id}", "source": d_id, "target": sd_id, "type": "contains"})

        # Product node
        nodes.append({
            "id": p_id,
            "label": name,
            "group": "product",
            "tiering": tiering,
            "domain": domain,
            "subdomain": subdomain,
            "team": team,
            "reference": product.get("reference", ""),
            "color": _product_color(tiering),
            "size": _product_size(tiering),
        })
        parent_id = sd_id if subdomain else d_id
        edges.append({"id": f"e:{parent_id}->{p_id}", "source": parent_id, "target": p_id, "type": "contains"})

        # Component nodes (only in component view)
        if view_level == "component":
            for comp in product.get("components", []):
                if comp.get("type") in SKIP_COMPONENT_TYPES:
                    continue
                c_name = comp["name"]
                c_id = f"component:{c_name}"
                nodes.append({
                    "id": c_id,
                    "label": c_name,
                    "group": "component",
                    "domain": domain,
                    "team": team,
                    "color": _product_color(tiering),
                    "size": SIZE_TIER3,
                })
                edges.append({"id": f"e:{p_id}->{c_id}", "source": p_id, "target": c_id, "type": "contains"})

    # API dependency edges
    if view_level == "component":
        edges.extend(api_edges)
    else:
        # Aggregate component→component edges to product→product
        comp_to_product: dict[str, str] = {}
        for product in products:
            for comp in product.get("components", []):
                comp_to_product[comp["name"]] = product["name"]

        pp_seen: set[tuple] = set()
        for e in api_edges:
            consumer_comp = e["source"].replace("component:", "")
            producer_comp = e["target"].replace("component:", "")
            consumer_prod = comp_to_product.get(consumer_comp)
            producer_prod = comp_to_product.get(producer_comp)
            if not consumer_prod or not producer_prod or consumer_prod == producer_prod:
                continue
            key = (consumer_prod, producer_prod)
            if key in pp_seen:
                continue
            pp_seen.add(key)
            edges.append({
                "id": f"e:product:{consumer_prod}->product:{producer_prod}",
                "source": f"product:{consumer_prod}",
                "target": f"product:{producer_prod}",
                "type": "consumes",
                "external": e.get("external", False),
            })

    # User Journey nodes
    for uj in user_journeys:
        uj_uuid = uj.get("uuid", "")
        criticality = uj.get("criticality")
        nodes.append({
            "id": f"user_journey:{uj_uuid}",
            "label": uj.get("name", uj_uuid),
            "group": "user_journey",
            "criticality": criticality,
            "slo_target": uj.get("slo_target"),
            "description": uj.get("description", ""),
            "color": _uj_color(criticality),
            "size": SIZE_UJ,
        })

    # Product→UJ moment dependency edges
    edges.extend(uj_edges)

    consumes_count = sum(1 for e in edges if e["type"] == "consumes")
    uj_edge_count = sum(1 for e in edges if e["type"] == "moment_dependency")
    print(
        f"✅ Graph model: {len(nodes)} nodes, {len(edges)} edges "
        f"({consumes_count} consumes, {uj_edge_count} UJ links)",
        file=sys.stderr,
    )
    return {"nodes": nodes, "edges": edges}


# ─── Target resolution ─────────────────────────────────────────────────────────

def resolve_incident_node(target: str, nodes: list[dict]) -> tuple[str, str]:
    """
    Find the graph node ID and group for the given incident target name.

    Search order:
      1. Exact case-insensitive label match (product, component, user_journey)
      2. Substring match (returns single unambiguous match)

    Raises ValueError with suggestions if not found or ambiguous.
    """
    target_lower = target.lower()
    candidate_groups = {"product", "component", "user_journey"}

    for node in nodes:
        if node["group"] in candidate_groups and node["label"].lower() == target_lower:
            return node["id"], node["group"]

    matches = [
        n for n in nodes
        if n["group"] in candidate_groups and target_lower in n["label"].lower()
    ]
    if len(matches) == 1:
        return matches[0]["id"], matches[0]["group"]
    if len(matches) > 1:
        names = [m["label"] for m in matches[:10]]
        raise ValueError(
            f"Multiple assets match '{target}': {names}. "
            "Provide a more specific name."
        )

    available = sorted(n["label"] for n in nodes if n["group"] in ("product", "component"))[:20]
    raise ValueError(
        f"Asset '{target}' not found in the Knowledge Graph. "
        f"Sample available names: {available}"
    )


# ─── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Build the complete dependency graph for blast radius analysis.\n"
            "Covers blast-radius-analyzer SKILL.md Steps 3, 4, and 5."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--target", required=True,
        help="Incident target: product name, component name, or User Journey name",
    )
    parser.add_argument(
        "--scope", default=None,
        help="Domain filter, e.g. 'BUSINESS CAPABILITY PLATFORM' (default: full graph)",
    )
    parser.add_argument(
        "--view-level", choices=["product", "component"], default="product",
        help="Graph granularity: product (default) or component",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output JSON path (default: /tmp/kg_graph_<target>_<timestamp>.json)",
    )
    parser.add_argument(
        "--no-uj", action="store_true",
        help="Skip User Journey fetching for a faster technical-only graph",
    )
    parser.add_argument(
        "--cache", action="store_true",
        help="Reuse cached API data if < 1 hour old (skips network calls)",
    )
    parser.add_argument(
        "--api-script", default=None,
        help="Explicit path to decathlon_api.py (auto-detected if omitted)",
    )
    args = parser.parse_args()

    # Resolve decathlon_api.py
    try:
        api_script = args.api_script or find_api_script()
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"API script: {api_script}", file=sys.stderr)

    # Step 3a — products
    products = fetch_products(api_script, args.scope, args.cache)

    # Step 3b — API edges (component-level)
    api_edges = fetch_api_edges(api_script, args.cache)

    # Steps 4a-4d — User Journeys + product→UJ edges
    user_journeys: list[dict] = []
    uj_edges: list[dict] = []
    if not args.no_uj:
        user_journeys = fetch_user_journeys(api_script, args.cache)
        uj_edges = build_uj_edges(products, user_journeys)

    # Step 5 — assemble graph model
    graph = build_graph_model(products, api_edges, user_journeys, uj_edges, args.view_level)

    # Resolve incident target → node ID
    try:
        incident_node_id, incident_type = resolve_incident_node(args.target, graph["nodes"])
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"✅ Incident node resolved: {incident_node_id} (group: {incident_type})", file=sys.stderr)

    # Determine output path
    safe_target = args.target.lower().replace(" ", "_").replace("/", "-")
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = args.output or f"/tmp/kg_graph_{safe_target}_{ts}.json"

    consumes_count = sum(1 for e in graph["edges"] if e["type"] == "consumes")
    uj_edge_count = sum(1 for e in graph["edges"] if e["type"] == "moment_dependency")

    output = {
        "meta": {
            "incident_target": args.target,
            "incident_node_id": incident_node_id,
            "incident_type": incident_type,
            "scope": args.scope or "full_graph",
            "view_level": args.view_level,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "stats": {
                "total_products": len(products),
                "total_uj": len(user_journeys),
                "total_nodes": len(graph["nodes"]),
                "total_edges": len(graph["edges"]),
                "api_edges": consumes_count,
                "uj_edges": uj_edge_count,
            },
        },
        "nodes": graph["nodes"],
        "edges": graph["edges"],
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    # Print summary to stderr
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Graph data saved: {output_path}", file=sys.stderr)
    print(f"  Incident target : {incident_node_id}", file=sys.stderr)
    print(f"  Nodes           : {output['meta']['stats']['total_nodes']}", file=sys.stderr)
    print(f"  Edges           : {output['meta']['stats']['total_edges']}", file=sys.stderr)
    print(f"    consumes      : {consumes_count}", file=sys.stderr)
    print(f"    UJ links      : {uj_edge_count}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"\nNext step (BFS analysis):", file=sys.stderr)
    print(f"  python3 blast_radius.py {output_path} \"{incident_node_id}\"", file=sys.stderr)

    # Print the output path to stdout so callers can capture it
    print(output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
