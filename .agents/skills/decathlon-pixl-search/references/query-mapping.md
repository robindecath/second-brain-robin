# PixL Query Mapping Reference

Full reference for sport IDs, photo types, and view names used by `scripts/pixl_search.py`.

---

## PixL Views

| View name | Purpose | Best for |
|-----------|---------|----------|
| `V_CAM_DAMCOMM` | Communication / lifestyle assets | Campaign photos, athlete shots, action scenes |
| `V_PIXLDAMPRODUCT` | Product assets | Packshots, studio product photos |
| `V_SPID` | All assets (products + comm) | Broad search |
| `V_360` | 360° product views | Interactive product viewers |

---

## Sport IDs (football-related)

| Sport | IDs |
|-------|-----|
| Football (generic) | 773 |
| Football à 11 | 434 |
| Foot5 | 433 |
| Football à 7 | 301 |
| Beach Soccer | 432 |
| Futsal | 472 |
| Flag Football | 428 |
| Football américain | 429, 774 |
| Football gaélique | 949, 1025 |
| Football australien | 272, 912 |

## Photo Type IDs

| ID | Code | Meaning |
|----|------|---------|
| 1 | PSHOT | Packshot / studio white background |
| 2 | SCENE | Sportive practice / action / lifestyle |
| 4 | STOCK | Other types |
| 11 | DRAW | Sketch / illustration |

---

## Common querydkt filter syntax

The `querydkt` parameter accepts a URL-encoded JSON string with these operators:

```json
{
  "fieldName": { "in": ["value1", "value2"] },
  "fieldName": { "like": "%partial%" }
}
```

**Supported filter fields per view:**

### V_CAM_DAMCOMM
- `sports` — sport ID list
- `typecomm` — comm type (3=COMMERCIAL CAMPAIGNS, 5=PERMANENT, 6=WEB, 4=OTHERS)

### V_PIXLDAMPRODUCT
- `sports` — sport ID list
- `phototype` — photo type ID list (1=packshot, 2=scene)
- `photocontextuel` — contextual photo flag

---

## Youth / Junior keyword detection

The script post-filters results by checking asset names for these keywords:

`kid`, `kids`, `child`, `children`, `junior`, `jr`, `enfant`, `youth`, `young`, `boy`, `girl`, `ado`, `teen`

Examples of youth Kipsta product names in the DAM:
- `KIPSTA MAILLOT MC KIDS BOREAL VERT / BLEU`
- `KIPSTA SHORT JR F500 SS20 NOIR`
- `KIPSTA VIRALTO III JR MG/AG PEPPERMINT`
- `KIPSTA ESKUDO CLUB TF JR EASY LIME`
- `KIPSTA TOP JR KEEPDRY LS CN GREY`

---

## CDN URL patterns

All media is served from `https://www.mediadecathlon.com`:

```
# Thumbnail (small preview ~13 KB)
https://www.mediadecathlon.com/api/wedia/dam/variation/<uuid>/thumbnailSmall

# Original full resolution
https://www.mediadecathlon.com/api/wedia/dam/variation/<uuid>/original

# Direct file (product assets only)
https://www.mediadecathlon.com:443/file/pixldamproduct/<path>/<filename>.jpg
```

No authentication is required to access these CDN URLs — they are publicly accessible.
