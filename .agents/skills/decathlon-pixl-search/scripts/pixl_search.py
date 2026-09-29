#!/usr/bin/env python3
# /// script
# dependencies = []
# requires-python = ">=3.8"
# ///
"""
PixL DAM Search — Decathlon Digital Asset Management
Converts a natural language query into PixL API filters and returns media CDN URLs.

Usage:
    python3 pixl_search.py --query "kid playing football" --api-script ../decathlon-api-tool/scripts/decathlon_api.py
    python3 pixl_search.py --query "kipsta ball packshot" --api-script ... --view product --max 5
    python3 pixl_search.py --help
"""

import argparse
import json
import subprocess
import sys
from typing import Optional

# ---------------------------------------------------------------------------
# Static reference data — sport IDs from PixL V_PIXLSPORT view
# ---------------------------------------------------------------------------
SPORT_IDS = {
    # Football / Soccer
    "football": ["773", "434", "433", "432", "301"],
    "soccer": ["773", "434", "433", "432"],
    "foot": ["773", "434", "433"],
    "futsal": ["472"],
    "beach soccer": ["432"],
    # Basketball
    "basketball": ["60"],
    # Tennis
    "tennis": ["482"],
    # Running
    "running": ["530"],
    "trail": ["547"],
    # Cycling
    "cycling": ["145"],
    "velo": ["145"],
    # Swimming
    "swimming": ["475"],
    "natation": ["475"],
    # Hiking
    "hiking": ["293"],
    "randonnee": ["293"],
    # Fitness
    "fitness": ["214"],
    "gym": ["214"],
    # Rugby
    "rugby": ["533"],
    # Golf
    "golf": ["267"],
    # Yoga
    "yoga": ["604"],
    # Ski
    "ski": ["449"],
    # Surf
    "surf": ["473"],
    # Handball
    "handball": ["289"],
    # Volleyball
    "volleyball": ["519"],
}

# Photo type IDs from V_CAM_PHOTOTYPE
PHOTO_TYPES = {
    "packshot": "1",
    "product shot": "1",
    "product": "1",
    "pack": "1",
    "scene": "2",
    "practice": "2",
    "lifestyle": "2",
    "action": "2",
    "sportive": "2",
    "contextuel": "2",
}

# Keywords that indicate youth / junior content
YOUTH_KEYWORDS = ["kid", "kids", "child", "children", "junior", "jr", "enfant",
                  "youth", "young", "boy", "girl", "ado", "teen"]

# Keywords that indicate the comm/lifestyle view vs product view
COMM_KEYWORDS = ["lifestyle", "campaign", "player", "action", "playing", "scene",
                 "athlete", "sport", "practice", "campagne"]
PRODUCT_KEYWORDS = ["packshot", "pack shot", "product", "produit", "catalogue",
                    "catalog", "shot", "photo produit"]


# ---------------------------------------------------------------------------
# Query parsing
# ---------------------------------------------------------------------------

def parse_query(query: str) -> dict:
    """Map natural language to PixL filter parameters."""
    q = query.lower()

    # Detect sport
    sport_ids = []
    for keyword, ids in SPORT_IDS.items():
        if keyword in q:
            sport_ids = ids
            break
    if not sport_ids and any(w in q for w in ["ball", "ballon"]):
        sport_ids = SPORT_IDS["football"]  # default to football if ball mentioned

    # Detect photo type
    photo_type = None
    for keyword, pt_id in PHOTO_TYPES.items():
        if keyword in q:
            photo_type = pt_id
            break

    # Detect youth/junior content
    is_youth = any(k in q for k in YOUTH_KEYWORDS)

    # Detect preferred view
    wants_comm = any(k in q for k in COMM_KEYWORDS)
    wants_product = any(k in q for k in PRODUCT_KEYWORDS)

    # Detect name keywords (brand, product line)
    name_hints = []
    for brand in ["kipsta", "quechua", "domyos", "kalenji", "artengo",
                  "tribord", "forclaz", "rockrider", "decathlon"]:
        if brand in q:
            name_hints.append(brand.upper())

    return {
        "sport_ids": sport_ids,
        "photo_type": photo_type,
        "is_youth": is_youth,
        "wants_comm": wants_comm,
        "wants_product": wants_product,
        "name_hints": name_hints,
    }


def pick_view(params: dict, view_override: str) -> str:
    """Choose the best PixL view based on parsed query."""
    if view_override == "comm":
        return "V_CAM_DAMCOMM"
    if view_override == "product":
        return "V_PIXLDAMPRODUCT"
    # Auto-detect
    if params["wants_product"] or params["photo_type"] == "1":
        return "V_PIXLDAMPRODUCT"
    # Youth content: comm assets aren't labeled with kid/junior — use product with SCENE phototype
    if params["is_youth"]:
        return "V_PIXLDAMPRODUCT"
    if params["wants_comm"] or params["photo_type"] == "2":
        return "V_CAM_DAMCOMM"
    # Default: product view when brand hints present, comm otherwise
    if params["name_hints"]:
        return "V_PIXLDAMPRODUCT"
    return "V_CAM_DAMCOMM"


def build_querydkt(params: dict, view: str) -> Optional[str]:
    """Build the querydkt JSON filter string."""
    filters = {}

    if params["sport_ids"]:
        filters["sports"] = {"in": params["sport_ids"]}

    if view == "V_PIXLDAMPRODUCT":
        # For youth content without explicit photo type, default to SCENE (action shots)
        pt = params["photo_type"]
        if pt is None and params["is_youth"]:
            pt = "2"  # SPORTIVE PRACTICE
        if pt:
            filters["phototype"] = {"in": [pt]}

    if not filters:
        return None
    return json.dumps(filters)


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------

def call_pixl(api_script: str, view: str, querydkt: Optional[str],
              max_results: int, offset: int = 0) -> dict:
    """Call the PixL API via decathlon_api.py and return parsed JSON."""
    cmd = [
        sys.executable, api_script,
        "--method", "GET",
        "--url", "https://api-eu.decathlon.net/pixl_api/view",
        "--param", f"viewName={view}",
        "--param", f"max={max_results}",
        "--param", f"from={offset}",
    ]
    if querydkt:
        cmd += ["--param", f"querydkt={querydkt}"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        try:
            error_data = json.loads(result.stdout)
        except Exception:
            error_data = {"raw": result.stdout or result.stderr}
        raise RuntimeError(f"API call failed: {error_data}")

    return json.loads(result.stdout)


# ---------------------------------------------------------------------------
# Result formatting
# ---------------------------------------------------------------------------

CDN_BASE = "https://www.mediadecathlon.com"


def format_results(items: list, view: str, name_hints: list, is_youth: bool) -> list:
    """Extract and format relevant fields from raw PixL items."""
    out = []
    for item in items:
        name = item.get("name", "") or item.get("nameen", "") or ""
        uuid = item.get("$uuid", "")
        w = item.get("width", 0) or 0
        h = item.get("height", 0) or 0

        # For product view, get direct binary URL
        direct_url = ""
        if view == "V_PIXLDAMPRODUCT":
            binary = item.get("binary", {}) or {}
            direct_url = binary.get("remoteURL", "") or binary.get("localURL", "")

        # Apply youth filter if requested (post-filter since API doesn't support it)
        if is_youth:
            name_lower = name.lower()
            if not any(k in name_lower for k in YOUTH_KEYWORDS):
                continue

        # Apply name hint filter
        if name_hints:
            name_lower = name.lower()
            if not any(hint.lower() in name_lower for hint in name_hints):
                continue

        out.append({
            "name": name,
            "uuid": uuid,
            "width": w,
            "height": h,
            "resolution": f"{w}x{h}" if w and h else "unknown",
            "thumbnail": f"{CDN_BASE}/api/wedia/dam/variation/{uuid}/thumbnailSmall",
            "original": f"{CDN_BASE}/api/wedia/dam/variation/{uuid}/original",
            **({"direct_url": direct_url} if direct_url else {}),
        })

    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Search Decathlon PixL DAM using natural language.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 pixl_search.py --query "kid playing football" --api-script ../decathlon-api-tool/scripts/decathlon_api.py
  python3 pixl_search.py --query "kipsta ball packshot" --api-script ... --view product --max 5
  python3 pixl_search.py --query "soccer player action shot" --api-script ... --view comm --max 20
        """,
    )
    parser.add_argument("--query", required=True,
                        help="Natural language search query")
    parser.add_argument("--api-script", required=True,
                        help="Path to decathlon_api.py from decathlon-api-tool skill")
    parser.add_argument("--max", type=int, default=10,
                        help="Maximum number of results (default: 10)")
    parser.add_argument("--view", choices=["comm", "product", "auto"], default="auto",
                        help="Force PixL view: comm=V_CAM_DAMCOMM, product=V_PIXLDAMPRODUCT, auto (default)")
    args = parser.parse_args()

    # 1. Parse natural language query
    params = parse_query(args.query)
    view = pick_view(params, args.view)
    querydkt = build_querydkt(params, view)

    # Debug info to stderr
    print(f"[pixl_search] view={view}", file=sys.stderr)
    print(f"[pixl_search] querydkt={querydkt}", file=sys.stderr)
    print(f"[pixl_search] youth_filter={params['is_youth']}", file=sys.stderr)
    print(f"[pixl_search] name_hints={params['name_hints']}", file=sys.stderr)

    # 2. Call PixL API — fetch more than requested to allow post-filtering
    fetch_count = args.max
    if params["is_youth"]:
        fetch_count = 200  # need large batch to find youth-labeled items
    elif params["name_hints"]:
        fetch_count = args.max * 10
    fetch_count = min(fetch_count, 200)  # API cap

    try:
        raw = call_pixl(args.api_script, view, querydkt, fetch_count)
    except RuntimeError as e:
        # Retry without querydkt if it failed (syntax issue)
        print(f"[pixl_search] Retrying without querydkt filter: {e}", file=sys.stderr)
        try:
            raw = call_pixl(args.api_script, view, None, fetch_count)
        except RuntimeError as e2:
            print(json.dumps({"error": str(e2), "results": []}))
            sys.exit(1)

    total = raw.get("response", {}).get("total", 0)
    items = raw.get("response", {}).get("data", [])

    # 3. Format and post-filter
    results = format_results(items, view, params["name_hints"], params["is_youth"])

    # 4. Trim to requested max
    results = results[:args.max]

    # 5. Output
    output = {
        "query": args.query,
        "view": view,
        "total_in_dam": total,
        "returned": len(results),
        "results": results,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
