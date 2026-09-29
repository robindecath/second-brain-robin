---
name: decathlon-pixl-search
description: Search Decathlon's PixL DAM (Digital Asset Management) for media assets using natural language. Use when the user asks for a photo, image, video, or media asset (e.g. "find a photo of a kid playing football", "get a Kipsta ball packshot", "show me a soccer player image"). Converts natural language into PixL API queries and returns CDN-ready URLs.
license: Proprietary
metadata:
  audience: all
  domain: platform-engineering
  api: rest
  mcp_required: false
  owner: Decathlon Digital Platform
  version: "1.0.0"
  last-updated: "2026-07-17"
---

# Decathlon PixL DAM Search

Use this skill to find photos, images, and videos from Decathlon's Digital Asset Management platform (PixL / Wedia) using natural language.

## Available script

- **`scripts/pixl_search.py`** — Main search script. Accepts a natural language query and returns media assets with CDN URLs.

## Workflow

### Step 1 — Locate the `decathlon-api-tool` script path

The PixL API requires authentication. The `decathlon-api-tool` skill provides the authenticated HTTP client. Find its script at:

```
<skill-root>/../decathlon-api-tool/scripts/decathlon_api.py
```

Where `<skill-root>` is the directory of **this** skill (`decathlon-pixl-search/`).

### Step 2 — Run the search

```bash
python3 scripts/pixl_search.py \
  --query "<natural language query>" \
  --api-script "../decathlon-api-tool/scripts/decathlon_api.py" \
  [--max 10] \
  [--view comm|product|auto]
```

**Parameters:**

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--query` | Yes | — | Natural language search (e.g. "kid playing football") |
| `--api-script` | Yes | — | Path to `decathlon_api.py` from `decathlon-api-tool` |
| `--max` | No | `10` | Max results to return |
| `--view` | No | `auto` | Force a specific PixL view: `comm` (lifestyle/campaign), `product` (product shots), `auto` (script decides) |

### Step 3 — Interpret results

The script outputs JSON to stdout:

```json
{
  "total": 42,
  "results": [
    {
      "name": "KIPSTA MAILLOT VIRALTO 500 JR ROUGE",
      "uuid": "4febu81j6sm4...",
      "width": 2384,
      "height": 2980,
      "thumbnail": "https://www.mediadecathlon.com/api/wedia/dam/variation/<uuid>/thumbnailSmall",
      "original": "https://www.mediadecathlon.com/api/wedia/dam/variation/<uuid>/original",
      "direct_url": "https://www.mediadecathlon.com:443/file/pixldamproduct/..."
    }
  ]
}
```

**CDN URL variants:**
- `thumbnail` — Small preview, fast to load (~13 KB)
- `original` — Full resolution (up to 50 MB+), suitable for download

### Step 4 — Present results to the user

After running the script, show the user:
1. How many total results were found
2. The results as a table with: asset name, resolution, thumbnail URL, full-res URL
3. Offer to refine the search if results are not relevant
4. Always suggest that the user can also browse PixL directly in the dedicated web application: [https://www.mediadecathlon.com/dam/wedia/home](https://www.mediadecathlon.com/dam/wedia/home)

## Natural language mapping

The script automatically maps natural language to PixL filters. See `references/query-mapping.md` for the full mapping table (sport IDs, photo types, keywords).

## Examples

```bash
# Find a kid playing football
python3 scripts/pixl_search.py \
  --query "kid playing football" \
  --api-script "../decathlon-api-tool/scripts/decathlon_api.py"

# Get high-res Kipsta ball product photos
python3 scripts/pixl_search.py \
  --query "kipsta football ball packshot" \
  --api-script "../decathlon-api-tool/scripts/decathlon_api.py" \
  --view product \
  --max 5

# Find a soccer player lifestyle photo
python3 scripts/pixl_search.py \
  --query "soccer player action shot high resolution" \
  --api-script "../decathlon-api-tool/scripts/decathlon_api.py" \
  --view comm \
  --max 20
```

## Error handling

| Error | Meaning | Action |
|-------|---------|--------|
| `CONNECTION_ERROR` | Network/auth issue | Check VPN, retry once |
| `400/1200` | Bad query syntax | Script will retry with simplified filter |
| `0 results` | No match | Try broader query or different `--view` |
