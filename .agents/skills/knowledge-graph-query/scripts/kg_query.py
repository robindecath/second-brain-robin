#!/usr/bin/env python3
"""
kg_query.py — direct query helper for the AppReferential knowledge graph.

Vendored to live *inside* this skill so agents don't need a second `read_skill
decathlon-api-tool` call or the fragile `<available_skills>` path-parsing dance
just to run a GraphQL POST. It reuses `decathlon_api.get_access_token()` for
OAuth2 PKCE auth (token cache shared at ~/.config/decathlon-cli/tokens.json —
same file the decathlon-api-tool skill uses), so logging in once from either
tool works for both.

It also adds aggregation shortcuts so common "breakdown / distribution /
group-by" questions don't require fetching every edge and counting client-side
in the model's context — the biggest token-usage lever for this skill.

Usage:
    # Raw GraphQL passthrough (escape hatch — same as calling decathlon_api.py directly)
    python3 kg_query.py raw --data '{"query": "...", "variables": {}}'

    # Counts by an enum-like metadata field, in ONE http round trip
    python3 kg_query.py breakdown --kind product --breakdown-by lifecycle \
        --values GENERAL_AVAILABILITY END_OF_LIFE BETA DEVELOPMENT DEPRECATED

    # All clusters in one call, for client-side region-prefix filtering
    # (replaces "try 4 region variants" with 1 request; ~58 clusters total)
    python3 kg_query.py all-clusters

    # Discover real top-level metadata keys instead of guessing field names
    python3 kg_query.py discover-metadata --kind product --sample 5

Exit codes: 0 success, 1 HTTP/GraphQL error, 2 usage error.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

DEFAULT_GRAPH_URL = "https://knowledge-graph.europe-west1.gcp.priv.dkt.cloud/graphql"
REQUEST_TIMEOUT = 30


def _load_decathlon_api_module():
    """Locate and import decathlon_api.py to reuse its OAuth token logic.

    Resolution order (first match wins) — all are code, not model-guided prompt
    parsing, so this never depends on the model reading an XML block correctly:
      1. DECATHLON_API_SCRIPT env var (explicit override)
      2. Common sibling checkout of the ai-augmented-sdlc repo
      3. Any decathlon_api.py found under ~/Projects (best-effort fallback)
    """
    candidates = []
    env_path = os.environ.get("DECATHLON_API_SCRIPT")
    if env_path:
        candidates.append(env_path)

    home = os.path.expanduser("~")
    candidates.append(
        os.path.join(home, "Projects", "ai-augmented-sdlc", "skills",
                      "decathlon-api-tool", "scripts", "decathlon_api.py")
    )

    for path in candidates:
        if path and os.path.isfile(path):
            spec = importlib.util.spec_from_file_location("decathlon_api", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # type: ignore[union-attr]
            return module

    # Best-effort fallback scan (kept shallow to stay fast)
    projects_dir = os.path.join(home, "Projects")
    if os.path.isdir(projects_dir):
        for root, _dirs, files in os.walk(projects_dir):
            if "decathlon_api.py" in files and "decathlon-api-tool" in root:
                path = os.path.join(root, "decathlon_api.py")
                spec = importlib.util.spec_from_file_location("decathlon_api", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)  # type: ignore[union-attr]
                return module

    return None


def _post_graphql(url: str, query: str, variables: dict) -> dict:
    api = _load_decathlon_api_module()
    if api is None:
        print(json.dumps({
            "error": "Could not locate decathlon_api.py for auth. Set DECATHLON_API_SCRIPT "
                     "to its absolute path, e.g. export DECATHLON_API_SCRIPT=/path/to/decathlon_api.py",
            "code": "AUTH_MODULE_NOT_FOUND",
        }))
        sys.exit(2)

    token = api.get_access_token()
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
    )
    ssl_context = None
    ca_bundle = api._find_ca_bundle() if hasattr(api, "_find_ca_bundle") else None
    if ca_bundle:
        ssl_context = ssl.create_default_context(cafile=ca_bundle)

    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ssl_context) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(json.dumps({"error": f"HTTP {e.code}: {e.reason}", "code": "HTTP_ERROR"}))
        sys.exit(1)
    except urllib.error.URLError as e:
        print(json.dumps({"error": f"Connection failed: {e.reason}", "code": "CONNECTION_ERROR"}))
        sys.exit(1)

    if "errors" in payload:
        print(json.dumps(payload))
        sys.exit(1)
    return payload


def cmd_raw(args: argparse.Namespace) -> None:
    parsed = json.loads(args.data)
    result = _post_graphql(args.url, parsed["query"], parsed.get("variables", {}))
    print(json.dumps(result))


def _nested_metadata_filter(dotted_path: str, value) -> dict:
    """Build a nested metadataFilter dict from a dotted path, e.g.

    "stack.language", "Java" -> {"stack": {"language": "Java"}}

    Confirmed live: metadataFilter matches nested object paths server-side
    (not just top-level metadata keys), e.g. filtering components by
    stack.language / stack.framework without fetching all rows client-side.
    """
    parts = dotted_path.split(".")
    node: dict = {parts[-1]: value}
    for part in reversed(parts[:-1]):
        node = {part: node}
    return node


def cmd_breakdown(args: argparse.Namespace) -> None:
    """Aliased assetCount per known value — one round trip, no raw-edge dump.

    --breakdown-by accepts a dotted path (e.g. "stack.language") to filter on
    nested metadata fields, not just top-level ones (e.g. "lifecycle").
    """
    var_decls = ["$total: AssetFilter!"]
    field_selections = ["total: assetCount(filter: $total)"]
    variables = {"total": {"kind": args.kind}}
    for i, value in enumerate(args.values):
        var_name = f"f{i}"
        var_decls.append(f"${var_name}: AssetFilter!")
        field_selections.append(f"v{i}: assetCount(filter: ${var_name})")
        variables[var_name] = {
            "kind": args.kind,
            "metadataFilter": _nested_metadata_filter(args.breakdown_by, value),
        }

    query = "query Breakdown(%s) { %s }" % (", ".join(var_decls), " ".join(field_selections))
    result = _post_graphql(args.url, query, variables)
    data = result.get("data", {})
    total = data.get("total", 0)
    breakdown = {
        value: {
            "count": data.get(f"v{i}", 0),
            "pct": round(100 * data.get(f"v{i}", 0) / total, 1) if total else 0.0,
        }
        for i, value in enumerate(args.values)
    }
    print(json.dumps({"kind": args.kind, "field": args.breakdown_by, "total": total, "breakdown": breakdown}))


def cmd_all_clusters(args: argparse.Namespace) -> None:
    """Fetch all clusters unfiltered in one call for client-side region matching."""
    query = (
        "query AllClusters($n: Int!) { assets(filter: { kind: \"cluster\" }, first: $n) "
        "{ totalCount edges { node { name metadata relationships { type targetAsset "
        "{ name kind tiering } } } } pageInfo { hasNextPage endCursor } } }"
    )
    result = _post_graphql(args.url, query, {"n": 200})
    print(json.dumps(result))


def cmd_blast_radius(args: argparse.Namespace) -> None:
    """Cluster -> hosted components -> owning products in ONE 2-hop nested query.

    Replaces the historical pattern of (1) fetching all clusters, (2) fetching every
    product with full metadata, then (3) doing one asset(name:...) lookup per hosted
    component to resolve its owning product — which caused an 11-17 shell-call,
    ~1.1M-token outlier on "blast radius if europe-west assets fail" questions.
    GraphQL's `relationships` field supports server-side `type` filtering AND nesting
    one more level on `targetAsset`, so cluster->hosts->component->partOf->product
    resolves in a single round trip (~65KB for all 58 clusters, confirmed live).
    """
    query = (
        "query BlastRadius($n: Int!) { assets(filter: { kind: \"cluster\" }, first: $n) "
        "{ totalCount edges { node { name metadata relationships(type: \"hosts\") "
        "{ targetAsset { name kind relationships(type: \"partOf\") "
        "{ targetAsset { name kind tiering } } } } } } } }"
    )
    result = _post_graphql(args.url, query, {"n": 200})
    edges = result.get("data", {}).get("assets", {}).get("edges", [])

    region_prefix = args.region_prefix
    clusters = []
    components = {}
    products = {}
    for edge in edges:
        node = edge.get("node", {})
        region = ((node.get("metadata") or {}).get("deployment") or {}).get("region", "")
        if region_prefix and not region.startswith(region_prefix):
            continue
        hosted = []
        for rel in node.get("relationships") or []:
            comp = rel.get("targetAsset") or {}
            comp_name = comp.get("name")
            if comp_name:
                components[comp_name] = comp.get("kind")
                hosted.append(comp_name)
            for prel in comp.get("relationships") or []:
                prod = prel.get("targetAsset") or {}
                prod_name = prod.get("name")
                if prod_name:
                    products[prod_name] = prod.get("tiering")
        clusters.append({"name": node.get("name"), "region": region, "hosted_components": hosted})

    print(json.dumps({
        "matching_clusters_total": len(clusters),
        "clusters": clusters,
        "impacted_components": {"count": len(components), "names": sorted(components)},
        "impacted_products": {
            "count": len(products),
            "items": [{"name": k, "tiering": v} for k, v in sorted(products.items())],
        },
    }))


def cmd_libraries(args: argparse.Namespace) -> None:
    """Third-party library/dependency lookups via `Asset.libraries` / `librariesByName`.

    Wraps the "libraries" GraphQL fields documented in SKILL.md so the model doesn't
    have to hand-write the query shape each time. `libraries` is a relationship-style
    field (like `components`/`stack`) that the generic `query`/`list-filtered` engine
    can't reach, so it needs its own single-asset (or top-level) lookup here.

    Never uses the deprecated, capped `stack.dependencies` field — always the live,
    uncapped SBOM-backed `libraries`/`librariesByName` fields (see ADR-025).

    Exactly one of --product, --component, --by-name must be given.
    """
    modes_set = [bool(args.product), bool(args.component), bool(args.by_name)]
    if sum(modes_set) != 1:
        print(json.dumps({
            "error": "Specify exactly one of --product, --component, --by-name",
            "code": "USAGE_ERROR",
        }))
        sys.exit(2)

    if args.by_name:
        query = (
            "query WhoUses($n: String!) { librariesByName(name: $n) "
            "{ library { name version ecosystem license purl } asset { name kind tiering } } }"
        )
        result = _post_graphql(args.url, query, {"n": args.by_name})
        print(json.dumps(result))
        return

    if args.component:
        query = (
            "query CompLibs($n: String!) { asset(name: $n) "
            "{ name libraries { name version ecosystem license purl firstSeenAt lastSeenAt } } }"
        )
        result = _post_graphql(args.url, query, {"n": args.component})
        print(json.dumps(result))
        return

    # --product: resolve the product asset and its owned components in one call,
    # each with its own libraries list (mirrors the documented "components on an
    # asset" pattern — one round trip, not one query per component).
    query = (
        "query ProductLibs($p: String!) { asset(name: $p) "
        "{ name components { name libraries { name version ecosystem license purl } } } }"
    )
    result = _post_graphql(args.url, query, {"p": args.product})
    asset_node = result.get("data", {}).get("asset")
    components = (asset_node or {}).get("components") or []
    if asset_node is not None and not components:
        # Product node exposed no components directly (e.g. not wired via a
        # component-owns relationship) — fall back to filtering components by
        # metadataFilter.governance.product, same field used elsewhere in this
        # skill for product-scoped component lookups.
        fallback_query = (
            "query ProductLibsFallback($f: AssetFilter!, $n: Int!) { assets(filter: $f, first: $n) "
            "{ totalCount edges { node { name libraries { name version ecosystem license purl } } } } }"
        )
        result = _post_graphql(
            args.url, fallback_query,
            {"f": {"kind": "component", "metadataFilter": {"governance": {"product": args.product}}}, "n": 200},
        )
    print(json.dumps(result))


def _get_path(node: dict, dotted_path: str):
    """Read a dotted path (e.g. 'metadata.stack.framework_version') off a node."""
    cur = node
    for part in dotted_path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def cmd_list_filtered(args: argparse.Namespace) -> None:
    """Generic filter + field-projection + auto-pagination in ONE shell call.

    This replaces the historical anti-pattern (still observed live) of the model
    hand-rolling a pagination loop across MANY shell calls with `raw` — one call
    per page, each dumping full asset metadata into context — for questions like
    "list Spring Boot components with version and owning product", "which
    components have no stack info", or "how many components does each team own".
    The script does the paging (server caps `first` at 200/page) and field
    projection/aggregation internally; only the compact result the model
    actually asked for crosses the shell boundary.

    Server-side filtering via --metadata-filter uses nested metadataFilter
    (confirmed to match nested paths, e.g. {"stack": {"framework": "Spring
    Boot"}} — NOT just top-level keys). For conditions the API can't filter on
    (e.g. "field is missing/empty"), use --missing-field for a client-side
    presence check done inside the script, after paging, before printing —
    still one shell call, no per-page dump to the model.

    --group-by tallies occurrences of a field's value across ALL matching rows
    (e.g. "teams active in domain X and how many components each owns" ->
    --group-by orgRefs.team) and returns counts instead of a raw item list —
    for "how many per Y" / "breakdown by Y" questions where Y's possible values
    aren't a small known enum (unlike lifecycle/tiering, which should use the
    `breakdown` subcommand instead since it avoids fetching any edges at all).

    Field paths may reference `metadata.*` (nested JSON), `orgRefs.*` (nested
    JSON — team/owner/domain/subdomain/unit), or bare top-level Asset fields
    (name, tiering, kind, type, businessScore).

    IMPORTANT: a component's owning product is on its OWN metadata at
    metadata.governance.product — no relationship traversal/lookup needed.
    """
    metadata_filter = json.loads(args.metadata_filter) if args.metadata_filter else None
    filt: dict = {"kind": args.kind}
    if metadata_filter:
        filt["metadataFilter"] = metadata_filter

    fields = [f.strip() for f in args.fields.split(",") if f.strip()] if args.fields else []
    query = (
        "query List($f: AssetFilter!, $n: Int!, $after: String) { "
        "assets(filter: $f, first: $n, after: $after) { totalCount "
        "pageInfo { hasNextPage endCursor } "
        "edges { node { name kind type tiering businessScore metadata orgRefs "
        "links { id type title url } } } } }"
    )

    items = []
    group_counts: dict = {}
    after = None
    server_total = None
    pages = 0
    while True:
        result = _post_graphql(args.url, query, {"f": filt, "n": 200, "after": after})
        data = result.get("data", {}).get("assets", {})
        if server_total is None:
            server_total = data.get("totalCount")
        for edge in data.get("edges", []):
            node = edge.get("node", {})
            if args.missing_field:
                val = _get_path(node, args.missing_field)
                if val not in (None, "", [], {}):
                    continue  # field present -> not a match, skip
            if args.group_by:
                val = _get_path(node, args.group_by)
                key = json.dumps(val) if not isinstance(val, str) else (val or "(none)")
                group_counts[key] = group_counts.get(key, 0) + 1
                continue
            row = {"name": node.get("name")}
            for f in fields:
                key = f
                for prefix in ("metadata.", "orgRefs."):
                    if f.startswith(prefix):
                        key = f[len(prefix):]
                        break
                row[key] = _get_path(node, f)
            items.append(row)
        pages += 1
        page_info = data.get("pageInfo", {})
        if not page_info.get("hasNextPage") or pages > 50:  # safety valve
            break
        after = page_info.get("endCursor")

    if args.group_by:
        ranked = sorted(group_counts.items(), key=lambda kv: kv[1], reverse=True)
        print(json.dumps({
            "kind": args.kind,
            "metadata_filter": metadata_filter,
            "group_by": args.group_by,
            "server_side_matched_total": server_total,
            "distinct_groups": len(ranked),
            "groups": [{"value": k, "count": v} for k, v in ranked],
        }))
        return

    limit = args.limit
    print(json.dumps({
        "kind": args.kind,
        "metadata_filter": metadata_filter,
        "missing_field": args.missing_field,
        "server_side_matched_total": server_total,
        "matched_after_filters": len(items),
        "returned": min(len(items), limit),
        "truncated": len(items) > limit,
        "items": items[:limit],
    }))


def _flatten_path(node, parts):
    """Resolve a dotted path with optional '[]' array-broadcast segments.

    e.g. parts=['metadata','sources[]','key'] on a node returns the 'key'
    value from EVERY element of metadata.sources (a list), not just the first.
    Plain (non-'[]') segments behave like a normal dict .get() chain.
    """
    if not parts:
        return [node]
    part = parts[0]
    rest = parts[1:]
    if part.endswith("[]"):
        key = part[:-2]
        lst = node.get(key) if isinstance(node, dict) else None
        if not isinstance(lst, list):
            return []
        out = []
        for item in lst:
            out.extend(_flatten_path(item, rest))
        return out
    nxt = node.get(part) if isinstance(node, dict) else None
    return _flatten_path(nxt, rest)


def _resolve_values(node: dict, dotted_path: str):
    """Resolve a dotted path (with optional [] segments) to a list of values.

    Falls back to looking under `metadata.<path>` when the bare path resolves
    to nothing and doesn't already start with a known top-level container
    (`metadata`/`orgRefs`). This makes --where/--group-by/--sort-by/--fields
    accept the SAME bare paths as `breakdown --breakdown-by` (e.g.
    `stack.language`) instead of silently returning an empty/"(none)" bucket
    just because the caller omitted the `metadata.` prefix — the ambiguity
    that caused a real outlier (agent assumed a field didn't exist and fell
    back to manually paginating + counting client-side).
    """
    parts = dotted_path.split(".")
    values = _flatten_path(node, parts)
    if any(v is not None for v in values) or parts[0] in ("metadata", "orgRefs"):
        return values
    return _flatten_path(node, ["metadata"] + parts)


def _resolve_single(node: dict, dotted_path: str):
    """Resolve a dotted path to a single value (first match, or None)."""
    values = _resolve_values(node, dotted_path)
    return values[0] if values else None


_PRESENT = lambda v: v not in (None, "", [], {})  # noqa: E731


def _eval_where(node: dict, path: str, op: str, value) -> bool:
    values = _resolve_values(node, path)
    if op == "exists":
        return any(_PRESENT(v) for v in values)
    if op == "missing":
        return not any(_PRESENT(v) for v in values)
    if op == "eq":
        return any(str(v) == value for v in values)
    if op == "ne":
        return not any(str(v) == value for v in values) if values else True
    if op == "contains":
        return any(value is not None and str(value).lower() in str(v).lower() for v in values if v is not None)
    if op in ("gt", "gte", "lt", "lte"):
        try:
            fv = float(value)
        except (TypeError, ValueError):
            return False
        for v in values:
            try:
                nv = float(v)
            except (TypeError, ValueError):
                continue
            if op == "gt" and nv > fv:
                return True
            if op == "gte" and nv >= fv:
                return True
            if op == "lt" and nv < fv:
                return True
            if op == "lte" and nv <= fv:
                return True
        return False
    raise ValueError(f"Unknown --where operator: {op!r}")


def _parse_where(raw: str):
    """Parse 'path:op[:value]' into (path, op, value)."""
    parts = raw.split(":", 2)
    if len(parts) < 2:
        raise ValueError(f"--where must be 'path:op[:value]', got {raw!r}")
    path, op = parts[0], parts[1]
    value = parts[2] if len(parts) > 2 else None
    return path, op, value


def cmd_query(args: argparse.Namespace) -> None:
    """Generic filter + aggregate (count/sum/avg/min/max) + group-by + sort,
    all with internal auto-pagination, in ONE shell call.

    This is the general-purpose primitive meant to answer questions THIS SKILL
    HAS NEVER BEEN TUNED FOR, by composing four independent capabilities
    instead of requiring a new hardcoded subcommand per question shape:

      1. --where PATH:OP[:VALUE]  (repeatable, AND-combined) — arbitrary
         client-side predicate. PATH supports '[]' to broadcast over a list,
         e.g. 'metadata.sources[].key' checks every element of that array.
         OP in: exists, missing, eq, ne, contains, gt, gte, lt, lte.
         Examples:
           --where metadata.stack.framework:eq:"Spring Boot"
           --where "metadata.sources[].key:contains:github.com"   (has a GitHub link)
           --where businessScore:gt:80

      2. --metric {count,sum,avg,min,max} + --metric-field PATH — real numeric
         aggregation over ALL matching rows (not a sample). For min/max, the
         matching entity's name is reported too (answers "which one has the
         highest X"). Defaults to metric=count if omitted.

      3. --group-by PATH — buckets by a field's distinct values; combines with
         --metric (e.g. avg-per-group), or defaults to a per-group count.

      4. --sort-by PATH [--order asc|desc] --top N — ranks the filtered set and
         returns the top N rows (with --fields projected) — for "top 5 by X"
         / "which single X has the highest Y" questions.

    If none of --where/--metric/--group-by/--sort-by are given, behaves like a
    plain filtered list (same as `list-filtered`).

    Server-side filtering (--kind, --metadata-filter) is always pushed down to
    GraphQL first to shrink what's paginated; --where/--metric/--group-by/
    --sort-by then run client-side, inside the script, over the (already
    filtered) page stream — no per-page dump ever reaches the model.
    """
    metadata_filter = json.loads(args.metadata_filter) if args.metadata_filter else None
    filt: dict = {"kind": args.kind}
    if metadata_filter:
        filt["metadataFilter"] = metadata_filter

    wheres = [_parse_where(w) for w in (args.where or [])]
    fields = [f.strip() for f in args.fields.split(",") if f.strip()] if args.fields else []

    query = (
        "query Q($f: AssetFilter!, $n: Int!, $after: String) { "
        "assets(filter: $f, first: $n, after: $after) { totalCount "
        "pageInfo { hasNextPage endCursor } "
        "edges { node { name kind type tiering businessScore metadata orgRefs "
        "links { id type title url } } } } }"
    )

    matched = []  # list of node dicts passing --where, after server-side filter
    after = None
    server_total = None
    pages = 0
    while True:
        result = _post_graphql(args.url, query, {"f": filt, "n": 200, "after": after})
        data = result.get("data", {}).get("assets", {})
        if server_total is None:
            server_total = data.get("totalCount")
        for edge in data.get("edges", []):
            node = edge.get("node", {})
            if all(_eval_where(node, p, o, v) for p, o, v in wheres):
                matched.append(node)
        pages += 1
        page_info = data.get("pageInfo", {})
        if not page_info.get("hasNextPage") or pages > 50:  # safety valve
            break
        after = page_info.get("endCursor")

    def project(node):
        row = {"name": node.get("name")}
        for f in fields:
            key = f
            for prefix in ("metadata.", "orgRefs."):
                if f.startswith(prefix):
                    key = f[len(prefix):]
                    break
            row[key] = _resolve_single(node, f)
        return row

    out = {
        "kind": args.kind,
        "metadata_filter": metadata_filter,
        "where": [f"{p}:{o}" + (f":{v}" if v is not None else "") for p, o, v in wheres],
        "server_side_matched_total": server_total,
        "matched_after_where": len(matched),
    }

    if args.group_by:
        groups: dict = {}
        for node in matched:
            gval = _resolve_single(node, args.group_by)
            key = json.dumps(gval) if not isinstance(gval, (str, type(None))) else (gval or "(none)")
            bucket = groups.setdefault(key, {"count": 0, "_values": []})
            bucket["count"] += 1
            if args.metric_field:
                mv = _resolve_single(node, args.metric_field)
                try:
                    bucket["_values"].append(float(mv))
                except (TypeError, ValueError):
                    pass
        result_groups = []
        for key, bucket in groups.items():
            row = {"value": key, "count": bucket["count"]}
            if args.metric_field and args.metric != "count":
                vals = bucket["_values"]
                if vals:
                    row[args.metric] = (
                        sum(vals) if args.metric == "sum"
                        else sum(vals) / len(vals) if args.metric == "avg"
                        else min(vals) if args.metric == "min"
                        else max(vals)
                    )
                else:
                    row[args.metric] = None
            result_groups.append(row)
        result_groups.sort(key=lambda r: r["count"], reverse=True)
        out["group_by"] = args.group_by
        out["distinct_groups"] = len(result_groups)
        out["groups"] = result_groups
        print(json.dumps(out))
        return

    if args.metric != "count" and args.metric_field:
        pairs = []
        for node in matched:
            mv = _resolve_single(node, args.metric_field)
            try:
                pairs.append((float(mv), node.get("name")))
            except (TypeError, ValueError):
                continue
        vals = [v for v, _ in pairs]
        agg = {"count": len(vals)}
        if vals:
            if args.metric == "sum":
                agg["sum"] = sum(vals)
            elif args.metric == "avg":
                agg["avg"] = sum(vals) / len(vals)
            elif args.metric == "min":
                v, n = min(pairs, key=lambda p: p[0])
                agg["min"] = {"value": v, "name": n}
            elif args.metric == "max":
                v, n = max(pairs, key=lambda p: p[0])
                agg["max"] = {"value": v, "name": n}
        out["metric"] = args.metric
        out["metric_field"] = args.metric_field
        out["result"] = agg
        print(json.dumps(out))
        return

    if args.sort_by:
        def sort_key(node):
            v = _resolve_single(node, args.sort_by)
            try:
                return (0, float(v))
            except (TypeError, ValueError):
                return (1, str(v) if v is not None else "")
        matched.sort(key=sort_key, reverse=(args.order == "desc"))
        top_n = matched[: args.top]
        out["sort_by"] = args.sort_by
        out["order"] = args.order
        out["items"] = [project(n) for n in top_n]
        print(json.dumps(out))
        return

    # Plain filtered list mode (equivalent to list-filtered)
    limit = args.limit
    out["returned"] = min(len(matched), limit)
    out["truncated"] = len(matched) > limit
    out["items"] = [project(n) for n in matched[:limit]]
    print(json.dumps(out))


def cmd_discover_metadata(args: argparse.Namespace) -> None:
    """Sample a few assets and report the distinct top-level metadata keys found."""
    query = (
        "query Sample($f: AssetFilter!, $n: Int!) { assets(filter: $f, first: $n) "
        "{ edges { node { metadata } } } }"
    )
    result = _post_graphql(args.url, query, {"f": {"kind": args.kind}, "n": args.sample})
    edges = result.get("data", {}).get("assets", {}).get("edges", [])
    keys = set()
    for edge in edges:
        metadata = edge.get("node", {}).get("metadata") or {}
        keys.update(metadata.keys())
    print(json.dumps({"kind": args.kind, "sample_size": len(edges), "metadata_keys": sorted(keys)}))


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the AppReferential knowledge graph")
    parser.add_argument("--url", default=DEFAULT_GRAPH_URL)
    sub = parser.add_subparsers(dest="mode", required=True)

    p_raw = sub.add_parser("raw", help="Raw GraphQL passthrough (escape hatch)")
    p_raw.add_argument("--data", required=True, help='JSON: {"query": "...", "variables": {}}')
    p_raw.set_defaults(func=cmd_raw)

    p_bd = sub.add_parser("breakdown", help="Aliased assetCount breakdown over a metadata field")
    p_bd.add_argument("--kind", required=True, choices=["product", "component", "cluster"])
    p_bd.add_argument("--breakdown-by", required=True, help="dotted metadata field path, e.g. lifecycle or stack.language")
    p_bd.add_argument("--values", required=True, nargs="+", help="known values of that field")
    p_bd.set_defaults(func=cmd_breakdown)

    p_cl = sub.add_parser("all-clusters", help="Fetch all clusters in one call")
    p_cl.set_defaults(func=cmd_all_clusters)

    p_br = sub.add_parser("blast-radius", help="Cluster -> component -> product impact in one 2-hop call")
    p_br.add_argument("--region-prefix", default=None, help='e.g. "europe-west" to match europe-west1..4')
    p_br.set_defaults(func=cmd_blast_radius)

    p_libs = sub.add_parser("libraries", help="Third-party library/dependency lookup via Asset.libraries / librariesByName (never the deprecated stack.dependencies)")
    p_libs.add_argument("--product", default=None, help='Product name, e.g. "OneFF" — libraries for every component it owns')
    p_libs.add_argument("--component", default=None, help='Exact component asset name, e.g. "oneff" — libraries for that one component')
    p_libs.add_argument("--by-name", default=None, help='Library name (case-insensitive substring), e.g. "log4j" — cross-fleet "who uses X"')
    p_libs.set_defaults(func=cmd_libraries)

    p_disc = sub.add_parser("discover-metadata", help="Sample assets to find real metadata keys")
    p_disc.add_argument("--kind", required=True, choices=["product", "component", "cluster"])
    p_disc.add_argument("--sample", type=int, default=5)
    p_disc.set_defaults(func=cmd_discover_metadata)

    p_lf = sub.add_parser("list-filtered", help="Filter + project fields + auto-paginate in one call")
    p_lf.add_argument("--kind", required=True, choices=["product", "component", "cluster"])
    p_lf.add_argument("--metadata-filter", default=None,
                       help='JSON, e.g. \'{"stack": {"framework": "Spring Boot"}}\' (nested paths supported)')
    p_lf.add_argument("--fields", default="",
                       help="comma-separated dotted paths to include per row, e.g. metadata.stack.framework_version,metadata.governance.product")
    p_lf.add_argument("--missing-field", default=None,
                       help="dotted path; only include rows where this field is missing/empty (client-side, e.g. metadata.stack)")
    p_lf.add_argument("--group-by", default=None,
                       help="dotted path (e.g. orgRefs.team); tally counts per distinct value instead of listing rows — for group-by/breakdown questions over fields without a small known enum")
    p_lf.add_argument("--limit", type=int, default=50, help="max rows to print (server_side_matched_total is always exact); ignored when --group-by is set")
    p_lf.set_defaults(func=cmd_list_filtered)

    p_q = sub.add_parser("query", help="GENERIC: filter (--where) + aggregate (--metric/--group-by) + rank (--sort-by), all auto-paginated in one call")
    p_q.add_argument("--kind", required=True, choices=["product", "component", "cluster"])
    p_q.add_argument("--metadata-filter", default=None, help="JSON, server-side push-down filter (nested paths OK)")
    p_q.add_argument("--where", action="append", default=[],
                      help="repeatable 'path:op[:value]' client-side predicate; op in exists/missing/eq/ne/contains/gt/gte/lt/lte; path supports '[]' to broadcast over a list, e.g. metadata.sources[].key:contains:github.com")
    p_q.add_argument("--fields", default="", help="comma-separated dotted paths to project per row")
    p_q.add_argument("--metric", default="count", choices=["count", "sum", "avg", "min", "max"])
    p_q.add_argument("--metric-field", default=None, help="dotted numeric path for sum/avg/min/max, e.g. businessScore")
    p_q.add_argument("--group-by", default=None, help="dotted path; buckets matching rows by distinct value (combine with --metric for avg/sum-per-group)")
    p_q.add_argument("--sort-by", default=None, help="dotted path; ranks matching rows and returns the top N")
    p_q.add_argument("--order", default="desc", choices=["asc", "desc"])
    p_q.add_argument("--top", type=int, default=10, help="rows to return when --sort-by is set")
    p_q.add_argument("--limit", type=int, default=50, help="rows to return in plain list mode (no metric/group-by/sort-by)")
    p_q.set_defaults(func=cmd_query)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
