---
name: decathlon-tech-radar
description: Decathlon Corporate Tech Radar — ALWAYS use this skill whenever ANY technology, programming language, framework, tool, library, service, or solution is mentioned—in questions, code examples, explanations, recommendations, or anywhere else in the conversation. This includes casual mentions, decision questions, technical explanations, code snippets, debugging help, dependency questions, architectural discussions, and version migration questions. This skill validates all technology mentions against the company's tech radar to ensure consistent, policy-compliant guidance. Provides authoritative information about whether a technology can be used, recommended versions, applicable warnings, and alternative solutions. Make sure to consult the tech radar every single time a technology name appears in the conversation, regardless of context.
license: Apache-2.0
compatibility: 'Requires the `decathlon-api-tool` skill to perform authenticated HTTP calls. To install it, run: `npx skills add dktunited/agent-skills --skill decathlon-api-tool`'
metadata:
  owner: Decathlon Digital Platform
  version: "1.3.0"
  last-updated: "2026-07-17"
---

# Tech Radar skill

This skill answers questions by querying the **Decathlon Tech Radar API** in real time,
so the data is always up to date without maintaining any local files.

- **Source (live API):** `https://api.decathlon.net/webb`

All HTTP calls MUST go through the [`decathlon-api-tool`](../decathlon-api-tool/SKILL.md)
skill, which handles OAuth2 authentication and the bearer token. Never call the API
with a raw HTTP client — it will fail with `401`.

## When to Invoke This Skill

Automatically invoke this skill whenever:

- A **user asks about a technology** — "Can we use X?", "What's the recommended version of Y?", "Should we adopt Z?"
- A **user mentions any technology in context** — even in passing references or discussions about solutions
- An **agent generates technology recommendations** — to validate that suggestions align with company policy
- An **agent proposes a technical solution** — to ensure it's consistent with the tech radar
- **Multiple technologies are compared** — to check each against policy before providing guidance
- **A technology appears in code examples or implementation details** — to flag any policy misalignments

The skill acts as a **guardrail**: if a technology, language, framework, tool, or solution is mentioned anywhere, validate it against the tech radar to ensure company-wide consistency.

## Making the API call

Always run technology lookups through the `decathlon-api-tool` skill — it injects the
OAuth2 bearer token and validates the domain. Do **not** use a raw HTTP client.

1. **Load the API tool first.** `read_skill decathlon-api-tool` to obtain its
   execution instructions and resolve its script path.
2. **Execute the request** using whichever mechanism that skill exposes in the
   current environment:
   - **VS Code:** the `callDecathlonApi` LM tool.
   - **CLI agents:** the bundled Python script, e.g.
     ```bash
     python3 <decathlon-api-tool-dir>/scripts/decathlon_api.py \
       --method GET \
       --url "https://api.decathlon.net/webb/api/v1/technologies" \
       --param "search=Java"
     ```
3. **On failure**, retry once (per the api-tool rules). If it still fails, tell the
   user the Tech Radar could not be reached and do not fabricate an answer.

### Endpoints

Base URL: `https://api.decathlon.net/webb`

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/api/v1/technologies?search={name}` | Search technologies by name/alias. Returns a **paginated summary list** (no alternatives, no description). |
| `GET` | `/api/v1/technologies/{uuid}` | Full detail for one technology, **including `alternatives`, `description`, `when_to_use`, `when_not_to_use`, and detailed `versions`**. |

> The search endpoint returns lightweight records. Whenever you need alternatives or
> full version detail, take the `uuid` from the search result and call the detail
> endpoint.

## Data model (API response)

### Search response — `GET /api/v1/technologies?search=`

```jsonc
{
  "content": [
    {
      "uuid": "3fa85f64-...",
      "name": "Java",
      "aliases": ["..."],
      "categories": ["BACKEND"],
      "usage": "CAN_USE",              // CAN_USE | CAN_USE_WITH_WARNINGS | CANNOT_USE
      "usage_warnings": ["ADOPT_WITH_EXCEPTIONS"],
      "warnings": ["MISSING_ALTERNATIVE"],
      "versions": [
        { "name": "21", "status": "ADOPT", "recommended": true, "has_exceptions": false }
      ],
      "website": "..."
    }
  ],
  "page": { "number": 0, "size": 20, "total_elements": 1, "total_pages": 1 }
}
```

### Detail response — `GET /api/v1/technologies/{uuid}`

Same technology fields as above, **plus**:

- `description`, `when_to_use`, `when_not_to_use` — human context.
- `alternatives[]` — recommended replacements, each a full technology object
  (`name`, `uuid`, `usage`, `version`). Use these directly for `CANNOT_USE`
  technologies instead of resolving UUIDs yourself.
- `versions[]` — detailed, with `status`, `recommended`, `has_exceptions`,
  `effective_date`, `decommission_date`, `license_type`, `open_source_license`.

### Field reference

- `usage` — `CAN_USE` | `CAN_USE_WITH_WARNINGS` | `CANNOT_USE`.
- `usage_warnings[]` — array of warning codes (e.g. `ADOPT_WITH_EXCEPTIONS`,
  `HETEROGENEOUS_VERSIONS_STATUSES`).
- `warnings[]` — data-quality flags (e.g. `MISSING_ALTERNATIVE`).
- `versions[].status` — `WATCH` | `TRIAL` | `ADOPT` | `ON_HOLD` | `FORBIDDEN`.
- `versions[].recommended` — `true` marks the version to recommend first.

## Interpretation rules

### Usage values

- `CAN_USE` — the technology is allowed without restrictions.
- `CAN_USE_WITH_WARNINGS` — the technology is allowed, but warnings may apply.
- `CANNOT_USE` — the technology must not be used.

### Warning types

If a technology has `CAN_USE_WITH_WARNINGS`, one or both of these warnings may apply:

- `ADOPT_WITH_EXCEPTIONS`
    - Technology has at least one `ADOPT` version that is concerned by exceptions.

- `HETEROGENEOUS_VERSIONS_STATUSES`
    - Use this when the technology has versions with different statuses.
    - Example: some versions are `ADOPT` while others are `WATCH` or `TRIAL`.

### Version statuses

- `ADOPT` — Recommended standard. Validated, secure, fully supported by Ops/Platform.
- `TRIAL` — Authorized for PoCs or specific use cases after validation.
- `WATCH` — Under evaluation. Not yet authorized.
- `ON_HOLD` — Do not use for new projects. Migration required if found.
- `FORBIDDEN` — Explicitly banned

## How to answer

When asked about a technology:
1. `read_skill decathlon-api-tool`, then call
   `GET /api/v1/technologies?search=<name>` through it.
2. Pick the best match from `content[]` (compare `name` and `aliases`). If several
   plausible matches remain, ask the user to clarify.
3. Read its `usage`.
4. Summarize the `versions[]` statuses; note the `recommended` version if present.
5. Include any `usage_warnings[]` in the answer.
6. If you need alternatives, a description, or full version detail, call
   `GET /api/v1/technologies/{uuid}` with the matched `uuid`.
7. If the technology is `CANNOT_USE`, list the `alternatives[]` returned by the
   detail endpoint. If the API returns none, you may suggest alternatives from your
   own knowledge — but only ones you have confirmed as authorized via the API.
8. If the technology is `CAN_USE_WITH_WARNINGS`, explain the relevant warnings.

If every API attempt fails, tell the user the Tech Radar could not be reached.
Never fabricate a recommendation.

## Recommendation logic

### If usage is `CAN_USE`

Respond that the technology is allowed.

If versions exist, prefer the version flagged `recommended: true`, otherwise an
`ADOPT` version when available.

### If usage is `CAN_USE_WITH_WARNINGS`

Respond that the technology is allowed with caveats.

Include the warnings listed in `usage_warnings`.

If `usage_warnings` is empty but the status is still `CAN_USE_WITH_WARNINGS`,
fall back to summarizing the version status spread and mention any versions with
non-`ADOPT` statuses.

### If usage is `CANNOT_USE`

Respond that the technology should not be used.

If alternatives are available, recommend them.

## Suggested response format

Keep responses short and clear:

- Start with the final recommendation.
- Then add a brief reason.
- Then list relevant versions and warnings.
- If applicable, list alternatives.
- If there is only one version, do not list it separately.

## Example outputs

### Allowed technology

> Yes — this technology can be used.
> Recommended version: `X.Y.Z` (`ADOPT`).

### Allowed with warnings

> This technology can be used, but with warnings.
> Warning: `HETEROGENEOUS_VERSIONS_STATUSES`.
> Some versions are `ADOPT`, while others are `WATCH` or `TRIAL`.

### Not allowed

> No — this technology cannot be used.
> Alternative: `Other Technology`.

## Answering style

- Be concise.
- Prefer factual answers derived from the live API response.
- Do not invent recommendations that are not supported by the data.
- If a technology is not found, say so clearly.
- If multiple technologies match a partial name, ask for clarification.