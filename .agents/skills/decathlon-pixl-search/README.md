# decathlon-pixl-search

Search Decathlon's PixL DAM (Digital Asset Management) for media assets using natural language.

## What it does

Converts a natural language query into PixL API filters and returns CDN-ready media URLs (thumbnail + full resolution). Use when you need to find a photo, image, or video from Decathlon's internal DAM without knowing the exact API query syntax.

## Usage

```
Use when the user asks for a photo, image, video, or media asset from Decathlon:
- "find a photo of a kid playing football"
- "get a Kipsta ball packshot"
- "show me a soccer player image"
- "give me a lifestyle photo for Quechua hiking"
```

## Dependencies

- **`decathlon-api-tool`** — required for OAuth2 authentication against the PixL API

## How it works

1. Parses natural language into PixL filter parameters (sport IDs, photo types, youth flag)
2. Selects the best PixL view (`V_CAM_DAMCOMM` for lifestyle, `V_PIXLDAMPRODUCT` for product shots)
3. Calls `api-eu.decathlon.net/pixl_api/view` via `decathlon-api-tool`
4. Returns assets with thumbnail and original CDN URLs from `mediadecathlon.com`

## Key facts

- **PixL / Wedia DAM** — Decathlon's Digital Asset Management platform
- **Youth content** is only labeled (JR/KIDS) in `V_PIXLDAMPRODUCT`, not in `V_CAM_DAMCOMM`
- CDN URLs are **publicly accessible** — no auth needed to display images
- The `original` variation returns full-res files (up to 50MB+, 4K+)

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Agent instructions (agentskills.io spec) |
| `scripts/pixl_search.py` | Main search script |
| `references/query-mapping.md` | Sport IDs, photo types, CDN URL patterns |
| `bmad-manifest.json` | BMAD metadata and trigger patterns |
