---
name: decathlon-api-discovery
description: Discover Decathlon internal APIs and endpoints using the DocAPI semantic search service. Use when someone asks which API or endpoint to call for a given business need (e.g. "what API gives me product info", "how do I get warehouse orders").
license: Apache-2.0
metadata:
  owner: Decathlon Digital Platform
  version: "1.1.0"
  last-updated: "2026-06-11"
---

# Decathlon API Discovery

Use this skill whenever a user needs to find a Decathlon internal API or a specific endpoint for a given business requirement.

The DocAPI service at `ai-sdlc.europe-west1.gcp.priv.dkt.cloud` exposes a **semantic search** index over all Decathlon internal APIs and their endpoints. Always query it before answering any question like "which API should I use for…" or "what endpoint do I call to…".

---

## When to use this skill

- A user asks which Decathlon API covers a domain ("what API for product information?", "which service handles warehouse orders?")
- A user asks for a specific endpoint ("what should I call to search for a product by EAN?")
- A user wants to browse all available APIs
- A user wants to explore the endpoints of a particular API by topic/tag
- A user needs to understand what a specific Decathlon API offers

---

## Available endpoints

Base URL: `ai-sdlc.europe-west1.gcp.priv.dkt.cloud`

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/docapi/search/api?query=<text>` | Semantic search — find which **API** best matches a business need |
| `GET` | `/docapi/search/endpoint?query=<text>` | Semantic search — find the **endpoint** that best matches a specific operation |
| `GET` | `/docapi/endpoint?apiName=<name>&method=<verb>&endpoint=<path>` | Fetch one specific endpoint by API name, HTTP method and path |
| `GET` | `/docapi/apis` | List all available API names |
| `GET` | `/docapi/apis/{apiName}` | Get full information about a specific API |
| `GET` | `/docapi/apis/{apiName}/endpoints?tag=<tag>` | List endpoints of an API filtered by tag |

### Query parameters

- **`/docapi/search/api`** and **`/docapi/search/endpoint`** accept optional filters:
  - `domain` *(optional)* — restrict results to one of the known business domains (see [Domains](#domains)).
  - `country` *(optional)* — restrict results to a given country.
- **`/docapi/search/endpoint`** also accepts:
  - `withOpenApi` *(optional, default `true`)* — include the OpenAPI definition in each result. Set to `false` for lighter responses when the spec isn't needed.
- **`/docapi/endpoint`** requires `apiName`, `method` and `endpoint` and returns a single `SearchResult` (or `404` if not found).

---

## Domains

The service classifies APIs into a **fixed** set of business domains. When the user's request maps clearly to one of these, pass it via the `domain` query parameter to narrow the search:

- `Catalog, Offer & Product Lifecycle Management (PLM)`
- `Supply Chain, Planning & Sourcing`
- `Warehouse Management & Internal Logistics (WMS)`
- `Transport, Customs & Global Trade`
- `Omnichannel Inventory & Stock Reliability`
- `Order Management System (OMS) & Fulfillment`
- `Commerce, Cart & Digital Checkout`
- `POS (Point of Sale) & In-Store Solutions`
- `Payment, Fraud & Financial Compliance`
- `Customer, Identity & Loyalty (CRM)`
- `Marketing, Personalization & AI Services`
- `Reverse Logistics & Circular Economy (Second Life)`
- `HR, Workforce & Corporate Workspace`
- `Infrastructure, DevOps & Technical Foundations`
- `Observability, Security & Monitoring`

Only use a value from this list — do not invent domain names. If you're unsure which domain applies, omit the `domain` parameter and let the semantic search rank across all of them.

---

## Decision tree — which endpoint to call

```
User asks about a domain / business capability?
  └─> GET /docapi/search/api?query=<user question>[&domain=<domain>][&country=<country>]

User asks about a specific operation or action?
  └─> GET /docapi/search/endpoint?query=<user question>[&domain=<domain>][&country=<country>][&withOpenApi=false]

User already knows the exact API + method + path?
  └─> GET /docapi/endpoint?apiName=<name>&method=<verb>&endpoint=<path>

User wants to list all available APIs?
  └─> GET /docapi/apis

User wants details about a named API?
  └─> GET /docapi/apis/{apiName}

User wants endpoints for a named API filtered by topic?
  └─> GET /docapi/apis/{apiName}/endpoints?tag=<topic>
```

---

## Step-by-step workflow

### 1. Search for an API by business need

When the user says something like *"what API should I use to get product information?"*:

```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/search/api?query=product+information
```

The response is a ranked list of `SearchResult` objects. Present the **top results** with their names and descriptions.

If the request clearly belongs to one of the known [domains](#domains), narrow the search:

```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/search/api?query=product+information&domain=Catalog,%20Offer%20%26%20Product%20Lifecycle%20Management%20(PLM)
```

### 2. Search for a specific endpoint

When the user says *"what endpoint do I call to get a warehouse order?"*:

```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/search/endpoint?query=get+warehouse+order
```

Present the results with method, path, and description. Add `&domain=` / `&country=` to filter, and `&withOpenApi=false` if you don't need the OpenAPI spec in the response.

### 3. Fetch one specific endpoint

When the exact API, method and path are already known:

```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/endpoint?apiName=stock-api&method=GET&endpoint=/v1/availability
```

Returns a single `SearchResult`, or `404` if that endpoint doesn't exist.

### 4. Deep-dive into a specific API

Once you know the API name (e.g. from the search results or from the user), fetch its full description:

```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/apis/my-api-name
```

### 5. Browse endpoints by tag

If the user wants to see all endpoints for a given API related to a topic:

```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/apis/my-api-name/endpoints?tag=orders
```

---

## How to present results

After calling the API, synthesize the results into a clear, structured answer:

1. **Name the API** and give its purpose in one sentence.
2. **Show the relevant endpoint(s)**: HTTP method + path + short description.
3. **Indicate the base URL** if available from the API info.
4. **If multiple good matches exist**, list the top 3 and briefly explain the difference.
5. **If no result is found**, say so clearly and suggest the user rephrase or browse `/docapi/apis` to explore manually.

### Example response format

> **API:** `product-catalog-api`
> **Purpose:** Manages Decathlon's product catalog — descriptions, prices, media, and attributes.
>
> **Relevant endpoint:**
> ```
> GET /v1/products/{ean}
> ```
> Returns full product details (title, description, price, images) for a given EAN code.
>
> **Base URL:** `https://api.decathlon.net/product-catalog`

---

## Examples

### Example 1: Find the API for product information

**User:** "What API should I use to get product information?"

**Agent action:**
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/search/api?query=product+information
```

### Example 2: Find an endpoint for warehouse orders

**User:** "What should I call to get warehouse orders?"

**Agent action:**
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/search/endpoint?query=get+warehouse+order
```

### Example 3: List all available APIs

**User:** "What internal APIs are available at Decathlon?"

**Agent action:**
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/apis
```

Then present the full list grouped by domain if discernible, or as a plain list.

### Example 4: Explore a specific API

**User:** "Tell me more about the `stock-api`"

**Agent actions (in order):**
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/apis/stock-api
```
If you want endpoints by topic:
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/apis/stock-api/endpoints?tag=availability
```

### Example 5: Narrow a search to a domain

**User:** "Which API handles in-store checkout at the POS?"

**Agent action:**
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/search/api?query=in-store+checkout&domain=POS%20(Point%20of%20Sale)%20%26%20In-Store%20Solutions
```

### Example 6: Fetch a known endpoint directly

**User:** "Show me the `GET /v1/availability` endpoint of the stock-api."

**Agent action:**
```http
GET ai-sdlc.europe-west1.gcp.priv.dkt.cloud/docapi/endpoint?apiName=stock-api&method=GET&endpoint=/v1/availability
```

---

## What to avoid

- **Don't guess API names or endpoints** — always call the search service first.
- **Don't return raw JSON** to the user — synthesize a human-readable answer.
- **Don't call both `/search/api` and `/search/endpoint` for every query** — choose the most relevant one based on the user's intent (domain/capability → `/search/api`, specific operation → `/search/endpoint`).
- **Don't fabricate base URLs or authentication requirements** — only report what the API returns.
- **Don't invent `domain` values** — only use the fixed list under [Domains](#domains); omit the filter if unsure.

---

## References

- DocAPI service: `ai-sdlc.europe-west1.gcp.priv.dkt.cloud`
- [Decathlon Digital Platform](https://decathlon.atlassian.net/wiki/spaces/TO)
