# Audit Grid — Full Coverage RAAM 1.1 (83 criteria)

**Purpose**: Provide a structured, standards-anchored audit evidence table for full mobile accessibility audits.

This matrix is based on the 83 official RAAM 1.1 criteria and is intended for full iOS/Android app audits.

> **Source of truth for cross-references**: WCAG/RGAA mappings come from
> `../cross-references/RAAM_CROSS_REFERENCE.toon`.
> If there is any discrepancy, the `.toon` file takes precedence.

---

## Usage Protocol (Mandatory for full app audits)

1. Build an inventory of screens, reusable templates, and critical user journeys.
2. Evaluate each applicable criterion with one finding:
   - `PASS`
   - `FAIL: <short description>`
   - `N/A`
   - `RUNTIME_REQUIRED`
3. Every `RUNTIME_REQUIRED` item must be mapped to at least one concrete scenario in `reports/testing-plan-<platform>-<date>.md`.
4. Preserve the grid structure from this template in the generated audit artifact. Do not drop the `Mode`, `WCAG 2.2`, or `RGAA 4.1` columns when duplicating the report.
5. Add a `Full Issues Inventory` section after the RAAM grid. This inventory must enumerate concrete issue instances with screen/page reference, criterion mapping, and issue description.
6. Do not close a full-app audit without explicit coverage totals, a generated developer testing plan, and a populated Full Issues Inventory.

**Detection mode legend:**

- `Static` — detectable from code inspection
- `Runtime` — requires manual AT interaction
- `Static + Runtime` — partial static verification, runtime confirmation required
- `Content review` — editorial/UX wording quality validation

---

## Mandatory Coverage Block (for final report)

```
Applicable criteria: X/83
Pass: P
Fails: N criteria in FAIL
Runtime Required (pending manual verification): M criteria
N/A: K/83
Coverage quality note: [OS versions, devices, screen reader stack, scaling conditions, limits]
Coverage source: ../../standards/templates/raam-audit-template.md
Developer Testing Plan: reports/testing-plan-<platform>-<date>.md
```

Where:

- `X = 83 - K`
- `P + N + M = X`

---

## Required — Full Issues Inventory section (to include in the audit report)

The generated audit report must include a section named exactly `Full Issues Inventory` after the RAAM grid and before any remediation recommendations.

Purpose:

- distinguish criterion-level compliance status from concrete issue instances
- show where each issue was found
- allow multiple issue rows to map to the same RAAM criterion

Required columns:

| ID | RAAM Criterion | Screen / Page Reference | Issue |
| -- | -------------- | ----------------------- | ----- |

Rules:

- one row per concrete issue instance or tightly scoped cluster of identical instances
- use stable identifiers such as `A11Y-001`, `A11Y-002`, etc.
- include global/shared issues when they affect multiple screens (for example app shell, tab bar, shared component library)
- a single criterion may appear in multiple rows
- totals in this section do not need to equal the number of failed criteria in the RAAM grid

---

## Theme 1 — Graphic Elements

| RAAM | Validation focus                          | Mode                    | Finding | WCAG 2.2   | RGAA 4.1 |
| ---- | ----------------------------------------- | ----------------------- | ------- | ---------- | -------- |
| 1.1  | Informative images have text alternatives | Static                  |         | 1.1.1 (A)  | 1.2      |
| 1.2  | Decorative images are hidden from AT      | Static                  |         | 1.1.1 (A)  | 1.1      |
| 1.3  | Alternative text quality is meaningful    | Content review          |         | 1.1.1 (A)  | 1.3      |
| 1.4  | CAPTCHA/test images expose purpose        | Content review          |         | 1.1.1 (A)  | 1.4      |
| 1.5  | CAPTCHA has an accessible fallback        | Static + Runtime        |         | 1.1.1 (A)  | 1.5      |
| 1.6  | Long descriptions exist when needed       | Static + Content review |         | 1.1.1 (A)  | 1.6      |
| 1.7  | Long descriptions are relevant            | Content review          |         | 1.1.1 (A)  | 1.7      |
| 1.8  | Text-in-image avoided where possible      | Static                  |         | 1.4.5 (AA) | 1.8      |
| 1.9  | Captions and image semantics are linked   | Static                  |         | 1.1.1 (A)  | 1.9      |

## Theme 2 — Colors

| RAAM | Validation focus                        | Mode             | Finding | WCAG 2.2    | RGAA 4.1 |
| ---- | --------------------------------------- | ---------------- | ------- | ----------- | -------- |
| 2.1  | Information not conveyed by color alone | Static + Runtime |         | 1.4.1 (A)   | 3.1      |
| 2.2  | Text contrast thresholds respected      | Runtime          |         | 1.4.3 (AA)  | 3.2      |
| 2.3  | Non-text contrast thresholds respected  | Runtime          |         | 1.4.11 (AA) | 3.3      |

## Theme 3 — Multimedia

| RAAM | Validation focus                            | Mode                    | Finding | WCAG 2.2        | RGAA 4.1 |
| ---- | ------------------------------------------- | ----------------------- | ------- | --------------- | -------- |
| 3.1  | Time-based media has transcript/AD          | Static + Content review |         | 1.2.1,1.2.3 (A) | 4.1      |
| 3.2  | Transcript/AD quality is relevant           | Content review          |         | 1.2.1,1.2.3 (A) | 4.2      |
| 3.3  | Synchronized captions exist                 | Static + Content review |         | 1.2.2 (A)       | 4.3      |
| 3.4  | Captions quality is relevant                | Content review          |         | 1.2.2 (A)       | 4.4      |
| 3.5  | Audio description is provided when required | Static                  |         | 1.2.5 (AA)      | 4.5      |
| 3.6  | Audio description quality is relevant       | Content review          |         | 1.2.5 (AA)      | 4.6      |
| 3.7  | Time-based media is identifiable            | Static                  |         | 1.1.1 (A)       | 4.7      |
| 3.8  | Non-time media alternatives are provided    | Static                  |         | 1.1.1 (A)       | 4.8      |
| 3.9  | Non-time media alternatives are relevant    | Content review          |         | 1.1.1 (A)       | 4.9      |
| 3.10 | Auto-playing audio is controllable          | Runtime                 |         | 1.4.2 (A)       | 4.10     |
| 3.11 | Media controls are keyboard/AT operable     | Runtime                 |         | 2.1.1 (A)       | 4.11     |
| 3.12 | Non-time controls are keyboard/AT operable  | Runtime                 |         | 2.1.1 (A)       | 4.12     |
| 3.13 | Media exposes name/role/value to AT         | Static + Runtime        |         | 4.1.2 (A)       | 4.13     |

## Theme 4 — Tables

| RAAM | Validation focus                                | Mode           | Finding | WCAG 2.2  | RGAA 4.1        |
| ---- | ----------------------------------------------- | -------------- | ------- | --------- | --------------- |
| 4.1  | Data table structure and headers are correct    | Static         |         | 1.3.1 (A) | 5.1,5.4,5.6,5.7 |
| 4.2  | Data table labeling/summary quality is relevant | Content review |         | 1.3.1 (A) | 5.2,5.5         |

## Theme 5 — Interactive Components

| RAAM | Validation focus                                                | Mode             | Finding | WCAG 2.2        | RGAA 4.1 |
| ---- | --------------------------------------------------------------- | ---------------- | ------- | --------------- | -------- |
| 5.1  | Components expose role/state/value to AT                        | Static + Runtime |         | 4.1.2 (A)       | 7.1,7.2  |
| 5.2  | Components are keyboard/AT operable                             | Runtime          |         | 2.1.1 (A)       | 7.3      |
| 5.3  | Scripted interactions do not trigger unexpected context changes | Runtime          |         | 3.2.1,3.2.2 (A) | 7.4      |
| 5.4  | Status updates are announced accessibly                         | Static + Runtime |         | 4.1.3 (AA)      | 7.5      |
| 5.5  | Component labels are robust (visible/programmatic parity)       | Static + Runtime |         | 4.1.2,2.5.3 (A) | 7.1      |

## Theme 6 — Mandatory Elements

| RAAM | Validation focus                             | Mode             | Finding | WCAG 2.2  | RGAA 4.1 |
| ---- | -------------------------------------------- | ---------------- | ------- | --------- | -------- |
| 6.1  | Screen/page title exists                     | Static           |         | 2.4.2 (A) | 8.5      |
| 6.2  | Screen/page title quality is relevant/unique | Static + Runtime |         | 2.4.2 (A) | 8.6      |
| 6.3  | Default language is declared                 | Static           |         | 3.1.1 (A) | 8.3      |
| 6.4  | Declared language is correct                 | Static           |         | 3.1.1 (A) | 8.4      |

## Theme 7 — Information Structure

| RAAM | Validation focus                               | Mode             | Finding | WCAG 2.2           | RGAA 4.1 |
| ---- | ---------------------------------------------- | ---------------- | ------- | ------------------ | -------- |
| 7.1  | Headings and structural semantics are coherent | Static + Runtime |         | 1.3.1,2.4.6 (A/AA) | 9.1      |
| 7.2  | Overall structural grouping is coherent        | Static + Runtime |         | 1.3.1 (A)          | 9.2      |

## Theme 8 — Presentation of Information

| RAAM | Validation focus                                               | Mode                    | Finding | WCAG 2.2    | RGAA 4.1  |
| ---- | -------------------------------------------------------------- | ----------------------- | ------- | ----------- | --------- |
| 8.1  | Visual structure remains understandable in alternate rendering | Runtime                 |         | 1.3.1 (A)   | 10.1,10.2 |
| 8.2  | Reading sequence remains meaningful                            | Runtime                 |         | 1.3.2 (A)   | 10.3      |
| 8.3  | Focus visibility is maintained                                 | Runtime                 |         | 2.4.7 (AA)  | 10.7      |
| 8.4  | Content supports 200% text scaling                             | Runtime                 |         | 1.4.4 (AA)  | 10.4      |
| 8.5  | Reflow/viewport adaptation without loss                        | Runtime                 |         | 1.4.10 (AA) | 10.11     |
| 8.6  | Text spacing overrides do not break UI                         | Runtime                 |         | 1.4.12 (AA) | 10.12     |
| 8.7  | Instructions do not rely on sensory cues only                  | Static + Content review |         | 1.3.3 (A)   | 10.9      |
| 8.8  | Typography/symbol-only meaning has text equivalent             | Static                  |         | 1.3.3 (A)   | 10.10     |
| 8.9  | Hover/focus-triggered content is controllable                  | Runtime                 |         | 1.4.13 (AA) | 10.13     |

## Theme 9 — Forms

| RAAM | Validation focus                                 | Mode                    | Finding | WCAG 2.2                       | RGAA 4.1 |
| ---- | ------------------------------------------------ | ----------------------- | ------- | ------------------------------ | -------- |
| 9.1  | Form fields have visible and programmatic labels | Static                  |         | 1.3.1,2.4.6,2.5.3,3.3.2 (A/AA) | 11.1     |
| 9.2  | Label wording is relevant                        | Content review          |         | 1.3.1,2.4.6,2.5.3 (A/AA)       | 11.2     |
| 9.3  | Repeated field labels are consistent             | Static + Content review |         | 3.2.4 (AA)                     | 11.3     |
| 9.4  | Labels/instructions are present and associated   | Static                  |         | 3.3.2 (A)                      | 11.4     |
| 9.5  | Related fields are grouped semantically          | Static                  |         | 1.3.1,3.3.2 (A)                | 11.5     |
| 9.6  | Group legends/titles are present                 | Static                  |         | 1.3.1,3.3.2 (A)                | 11.6     |
| 9.7  | Group legends/titles are relevant                | Content review          |         | 1.3.1,3.3.2 (A)                | 11.7     |
| 9.8  | Input errors are identified and accessible       | Static + Runtime        |         | 3.3.1,3.2.2 (A)                | 11.10    |
| 9.9  | Error suggestions are provided where possible    | Content review          |         | 3.3.3 (AA)                     | 11.11    |
| 9.10 | Critical submissions support review/correction   | Runtime                 |         | 3.3.4 (AA)                     | 11.12    |
| 9.11 | Input purpose/autofill semantics are set         | Static                  |         | 1.3.5 (AA)                     | 11.13    |

## Theme 10 — Navigation

| RAAM | Validation focus                               | Mode    | Finding | WCAG 2.2        | RGAA 4.1 |
| ---- | ---------------------------------------------- | ------- | ------- | --------------- | -------- |
| 10.1 | Focus order and keyboard sequence are coherent | Runtime |         | 2.4.3,2.1.1 (A) | 12.8     |
| 10.2 | Navigation consistency across screens          | Runtime |         | 3.2.3 (AA)      | 12.2     |
| 10.3 | No keyboard trap in navigation flows           | Runtime |         | 2.1.2 (A)       | 12.9     |
| 10.4 | Single-key shortcuts are controllable          | Runtime |         | 2.1.4 (A)       | 12.10    |

## Theme 11 — Consultation

| RAAM  | Validation focus                               | Mode           | Finding | WCAG 2.2    | RGAA 4.1 |
| ----- | ---------------------------------------------- | -------------- | ------- | ----------- | -------- |
| 11.1  | Orientation changes do not block use           | Runtime        |         | 1.3.4 (AA)  | 13.9     |
| 11.2  | Time limits are controllable                   | Runtime        |         | 2.2.1 (A)   | 13.1     |
| 11.3  | Moving/auto-updating content is controllable   | Runtime        |         | 2.2.2 (A)   | 13.8     |
| 11.4  | Flashing content thresholds are respected      | Runtime        |         | 2.3.1 (A)   | 13.7     |
| 11.5  | Complex gestures have simple alternatives      | Runtime        |         | 2.5.1 (A)   | 13.10    |
| 11.6  | Pointer cancellation is supported              | Runtime        |         | 2.5.2 (A)   | 13.11    |
| 11.7  | Motion-actuated functionality has alternatives | Runtime        |         | 2.5.4 (A)   | 13.12    |
| 11.8  | Target size is sufficient (recommended)        | Runtime        |         | 2.5.5 (AAA) | —        |
| 11.9  | Downloadable docs have accessible alternative  | Content review |         | —           | 13.3     |
| 11.10 | Accessible alternative docs are relevant       | Content review |         | —           | 13.4     |

## Theme 12 — Documentation & Accessibility

| RAAM | Validation focus                                       | Mode           | Finding | WCAG 2.2 | RGAA 4.1 |
| ---- | ------------------------------------------------------ | -------------- | ------- | -------- | -------- |
| 12.1 | Accessibility documentation is available to users      | Content review |         | —        | —        |
| 12.2 | Accessibility documentation is discoverable and usable | Content review |         | —        | —        |
| 12.3 | Accessibility conformance statements are provided      | Content review |         | —        | —        |

## Theme 13 — Editing Tools

| RAAM | Validation focus                                     | Mode                     | Finding | WCAG 2.2 | RGAA 4.1 |
| ---- | ---------------------------------------------------- | ------------------------ | ------- | -------- | -------- |
| 13.1 | Authoring/editing features support accessible output | Runtime + Process review |         | —        | —        |

## Theme 14 — Support Services

| RAAM | Validation focus                                    | Mode                     | Finding | WCAG 2.2 | RGAA 4.1 |
| ---- | --------------------------------------------------- | ------------------------ | ------- | -------- | -------- |
| 14.1 | Support channels are accessible                     | Runtime + Content review |         | —        | —        |
| 14.2 | Support interactions include accessibility handling | Runtime + Process review |         | —        | —        |
| 14.3 | Support docs/help content are accessible            | Content review           |         | —        | —        |

## Theme 15 — Real-time Communication

| RAAM | Validation focus                                                   | Mode                     | Finding | WCAG 2.2 | RGAA 4.1 |
| ---- | ------------------------------------------------------------------ | ------------------------ | ------- | -------- | -------- |
| 15.1 | Real-time communication supports accessibility features            | Runtime                  |         | —        | —        |
| 15.2 | Bi-directional communication accessibility is supported            | Runtime                  |         | —        | —        |
| 15.3 | Captions/transcripts/signaling support is available where required | Runtime + Content review |         | —        | —        |
| 15.4 | Emergency/priority communication remains accessible                | Runtime + Process review |         | —        | —        |

---

## Optional Domain Profiles

After completing all 15 themes above, you may extend the audit with a domain-specific profile from `./domain-profiles.md`. The **Mobile Native** profile is particularly relevant for iOS/Android app audits and adds checks for warehouse/sport-specific scenarios, offline modes, and platform-specific patterns.

> Domain profiles are **additive** — they never replace or reduce RAAM criteria.
