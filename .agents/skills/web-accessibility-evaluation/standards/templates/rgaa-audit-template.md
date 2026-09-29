# Audit Grid — Full Coverage RGAA 4.1 (106 criteria)

**Purpose**: Provide a structured, standards-anchored audit evidence table for full web accessibility audits. Based on the 106 official RGAA 4.1 criteria, covering all 13 themes.

> **Source of truth for cross-references**: the WCAG 2.2 and RAAM 1.1 columns are sourced from
> `../cross-references/RGAA_CROSS_REFERENCE.toon`.
> In case of discrepancy, the `.toon` file takes precedence.

---

## Usage Protocol (Mandatory for full app audits)

1. Build an inventory of routes, templates, and critical user journeys.
2. For each criterion, fill in **Finding** with one of:
   - `PASS` — verified compliant from code or runtime
   - `FAIL: [short description]` — violation identified
   - `N/A` — criterion not applicable to this product
   - `RUNTIME_REQUIRED` — cannot be assessed from static code alone; must appear in the Developer Testing Plan
3. For every `RUNTIME_REQUIRED`, add a concrete scenario to `reports/testing-plan-<date>.md` using `developer-testing-guide-template.md`.
4. Preserve the grid structure from this template in the generated audit artifact. Do not drop the `Mode`, `WCAG 2.2`, or `RAAM 1.1` columns when duplicating the report.
5. Add a `Full Issues Inventory` section after the RGAA grid. This inventory must enumerate concrete issue instances with route/page reference, criterion mapping, and issue description.
6. Do not close a full-app audit without an explicit coverage summary, a generated Developer Testing Plan, and a populated Full Issues Inventory.

**Detection mode legend:**

- `Static` — detectable by reading source code
- `Runtime` — requires human testing (keyboard, screen reader, zoom, real navigation)
- `Static + Runtime` — partially verifiable statically, runtime confirmation required
- `Content review` — depends on editorial content, not code

---

## Required — Summary block (to include in the audit report)

```
Applicable criteria: X/106
Pass: P
Fails: N criteria in FAIL
Runtime Required (pending manual verification): M criteria
N/A: K/106
Coverage quality note: [browser, screen reader, zoom/reflow conditions tested, limitations]
Developer Testing Plan: reports/testing-plan-<date>.md
```

Where:

- `X = 106 - K`
- `P + N + M = X`

---

## Required — Full Issues Inventory section (to include in the audit report)

The generated audit report must include a section named exactly `Full Issues Inventory` after the RGAA grid and before any remediation recommendations.

Purpose:

- distinguish criterion-level compliance status from concrete issue instances
- show where each issue was found
- allow multiple issue rows to map to the same RGAA criterion
- keep explicit standards traceability at issue level (RGAA -> WCAG 2.2 -> RAAM 1.1)

Required columns:

| ID | RGAA Criterion | WCAG 2.2 | RAAM 1.1 | Route / Page Reference | Issue |
| -- | -------------- | -------- | -------- | ---------------------- | ----- |

Rules:

- one row per concrete issue instance or tightly scoped cluster of identical instances
- use stable identifiers such as `A11Y-001`, `A11Y-002`, etc.
- include global issues when they affect multiple routes (for example header, footer, shared layout)
- a single criterion may appear in multiple rows
- `WCAG 2.2` and `RAAM 1.1` values must be sourced from `../cross-references/RGAA_CROSS_REFERENCE.toon` (single source of truth)
- if a mapping is not defined in the cross-reference source, use `—`
- totals in this section do not need to equal the number of failed criteria in the RGAA grid

---

## Theme 1 — Images

| RGAA Criterion | Description                                                                                    | Mode                    | Finding | WCAG 2.2   | RAAM 1.1 |
| -------------- | ---------------------------------------------------------------------------------------------- | ----------------------- | ------- | ---------- | -------- |
| 1.1            | Does every informative image have a text alternative?                                          | Static                  |         | 1.1.1 (A)  | 1.2      |
| 1.2            | Is every decorative image correctly ignored by assistive technologies?                         | Static                  |         | 1.1.1 (A)  | 1.1      |
| 1.3            | For every informative image with a text alternative, is the alternative relevant?              | Content review          |         | 1.1.1 (A)  | 1.3      |
| 1.4            | For every CAPTCHA or test image, does the alternative identify its nature and function?        | Content review          |         | 1.1.1 (A)  | 1.4      |
| 1.5            | For every CAPTCHA, is an accessible alternative solution available?                            | Static + Runtime        |         | 1.1.1 (A)  | 1.5      |
| 1.6            | Does every informative image have a detailed description where necessary?                      | Static + Content review |         | 1.1.1 (A)  | 1.6      |
| 1.7            | For every image with a detailed description, is the description relevant?                      | Content review          |         | 1.1.1 (A)  | 1.7      |
| 1.8            | Is every informative text image replaced by styled text where possible (except special cases)? | Static                  |         | 1.4.5 (AA) | 1.8      |
| 1.9            | Is every image caption correctly linked to its corresponding image?                            | Static                  |         | 1.1.1 (A)  | 1.9      |

---

## Theme 2 — Frames

| RGAA Criterion | Description                                                  | Mode           | Finding | WCAG 2.2  | RAAM 1.1 |
| -------------- | ------------------------------------------------------------ | -------------- | ------- | --------- | -------- |
| 2.1            | Does every frame (`<iframe>`, `<frame>`) have a frame title? | Static         |         | 4.1.2 (A) | —        |
| 2.2            | For every frame with a title, is that title relevant?        | Content review |         | 4.1.2 (A) | —        |

---

## Theme 3 — Colors

| RGAA Criterion | Description                                                                                      | Mode             | Finding | WCAG 2.2    | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------------------------------------ | ---------------- | ------- | ----------- | -------- |
| 3.1            | Is information never conveyed by color alone?                                                    | Static + Runtime |         | 1.4.1 (A)   | 2.1      |
| 3.2            | Is the contrast between text color and its background sufficient (4.5:1 normal, 3:1 large text)? | Runtime          |         | 1.4.3 (AA)  | 2.2      |
| 3.3            | Do the colors of interface components or informative graphical elements meet the 3:1 threshold?  | Runtime          |         | 1.4.11 (AA) | 2.3      |

---

## Theme 4 — Multimedia

| RGAA Criterion | Description                                                                                                  | Mode                    | Finding | WCAG 2.2            | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------- | ------- | ------------------- | -------- |
| 4.1            | Does every pre-recorded time-based media have a text transcript or audio description (except special cases)? | Static + Content review |         | 1.2.1, 1.2.3 (A)    | 3.1      |
| 4.2            | For every pre-recorded time-based media with a transcript or audio description, are they relevant?           | Content review          |         | 1.2.1, 1.2.3 (A)    | 3.2      |
| 4.3            | Does every pre-recorded synchronized time-based media have synchronized captions (except special cases)?     | Static + Content review |         | 1.2.2, 1.2.4 (A/AA) | 3.3      |
| 4.4            | For every synchronized media with captions, are the captions relevant?                                       | Content review          |         | 1.2.2 (A)           | 3.4      |
| 4.5            | Does every pre-recorded time-based media have synchronized audio description (except special cases)?         | Static                  |         | 1.2.5 (AA)          | 3.5      |
| 4.6            | For every synchronized audio description, is it relevant?                                                    | Content review          |         | 1.2.5 (AA)          | 3.6      |
| 4.7            | Is every time-based media clearly identified?                                                                | Static + Content review |         | 1.1.1 (A)           | 3.7      |
| 4.8            | Does every non-time-based object have an alternative?                                                        | Static                  |         | 1.1.1 (A)           | 3.8      |
| 4.9            | For every non-time-based object with an alternative, is the alternative relevant?                            | Content review          |         | 1.1.1 (A)           | 3.9      |
| 4.10           | Is every automatically triggered sound controllable by the user?                                             | Runtime                 |         | 1.4.2 (A)           | 3.10     |
| 4.11           | Is the consultation of every time-based media controllable by keyboard and pointing device?                  | Runtime                 |         | 2.1.1 (A)           | 3.11     |
| 4.12           | Is the consultation of every non-time-based media controllable by keyboard?                                  | Runtime                 |         | 2.1.1 (A)           | 3.12     |
| 4.13           | Does every time-based and non-time-based media expose its name, role, and state to assistive technologies?   | Static                  |         | 4.1.2 (A)           | 3.13     |

---

## Theme 5 — Tables

| RGAA Criterion | Description                                                                               | Mode             | Finding | WCAG 2.2         | RAAM 1.1 |
| -------------- | ----------------------------------------------------------------------------------------- | ---------------- | ------- | ---------------- | -------- |
| 5.1            | Does every complex data table have a summary?                                             | Static           |         | 1.3.1 (A)        | 4.1      |
| 5.2            | For every complex data table with a summary, is the summary relevant?                     | Content review   |         | 1.3.1 (A)        | 4.2      |
| 5.3            | For every layout table, does the linearized content remain understandable?                | Static + Runtime |         | 1.3.1, 1.3.2 (A) | —        |
| 5.4            | For every data table, is the first cell of each column or row correctly structured?       | Static           |         | 1.3.1 (A)        | 4.1      |
| 5.5            | For every data table, does each header have a relevant label?                             | Content review   |         | 1.3.1 (A)        | 4.2      |
| 5.6            | For every data table, are headers correctly declared with `<th>`?                         | Static           |         | 1.3.1 (A)        | 4.1      |
| 5.7            | For every data table, are header cells spanning multiple columns/rows correctly declared? | Static           |         | 1.3.1 (A)        | 4.1      |
| 5.8            | Is every layout table free of elements specific to data tables?                           | Static           |         | 1.3.1 (A)        | —        |

---

## Theme 6 — Links

| RGAA Criterion | Description                                                        | Mode                    | Finding | WCAG 2.2         | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------ | ----------------------- | ------- | ---------------- | -------- |
| 6.1            | Is every link explicit (except special cases)?                     | Static + Content review |         | 2.4.4 (A)        | —        |
| 6.2            | On every page, does every link have a label (text or alternative)? | Static                  |         | 4.1.2, 2.4.4 (A) | —        |

---

## Theme 7 — Scripts

| RGAA Criterion | Description                                                                                      | Mode             | Finding | WCAG 2.2         | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------------------------------------ | ---------------- | ------- | ---------------- | -------- |
| 7.1            | Is every script, where necessary, compatible with assistive technologies?                        | Static + Runtime |         | 4.1.2 (A)        | 5.1      |
| 7.2            | For every script with an alternative, is the alternative relevant?                               | Content review   |         | 4.1.2 (A)        | 5.1      |
| 7.3            | Is every script controllable by keyboard and pointing device?                                    | Runtime          |         | 2.1.1 (A)        | 5.2      |
| 7.4            | For every script that initiates a context change, is the user warned or in control?              | Runtime          |         | 3.2.1, 3.2.2 (A) | 5.3      |
| 7.5            | Are status messages correctly rendered by assistive technologies (`aria-live`, `role="status"`)? | Static + Runtime |         | 4.1.3 (AA)       | 5.4      |

---

## Theme 8 — Mandatory Elements

| RGAA Criterion | Description                                                                                                         | Mode             | Finding | WCAG 2.2   | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------- | ------- | ---------- | -------- |
| 8.1            | Is every page defined by a valid document type (`DOCTYPE`)?                                                         | Static           |         | 4.1.1 (A)  | —        |
| 8.2            | Is the source code of every page valid per its declared document type (no duplicate IDs, properly nested elements)? | Static + Runtime |         | 4.1.1 (A)  | —        |
| 8.3            | On every page, is the default language declared (`html[lang]`) and correct?                                         | Static           |         | 3.1.1 (A)  | 6.3      |
| 8.4            | For every page, is the `html[lang]` language code relevant?                                                         | Static           |         | 3.1.1 (A)  | 6.4      |
| 8.5            | Does every page have a page title (`<title>`)?                                                                      | Static           |         | 2.4.2 (A)  | 6.1      |
| 8.6            | For every page with a title, is that title relevant and unique?                                                     | Static + Runtime |         | 2.4.2 (A)  | 6.2      |
| 8.7            | On every page, is each language change indicated in source code (`lang` on the element)?                            | Static           |         | 3.1.2 (AA) | —        |
| 8.8            | Is the language code for each change valid and relevant?                                                            | Static           |         | 3.1.2 (AA) | —        |
| 8.9            | Are HTML tags not used solely for presentation purposes (no stylistic `<b>`, decorative `<i>`, etc.)?               | Static           |         | 1.3.1 (A)  | —        |
| 8.10           | On every page, are reading direction changes signaled with the `dir` attribute?                                     | Static           |         | 1.3.2 (A)  | —        |

---

## Theme 9 — Information Structure

| RGAA Criterion | Description                                                                                       | Mode   | Finding | WCAG 2.2            | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------------------------------------- | ------ | ------- | ------------------- | -------- |
| 9.1            | On every page, is information structured by a consistent heading hierarchy (`h1`→`h2`→`h3`…)?     | Static |         | 1.3.1, 2.4.6 (A/AA) | 7.1      |
| 9.2            | On every page, is the document structure coherent (landmarks: `main`, `nav`, `header`, `footer`)? | Static |         | 1.3.1 (A)           | 7.2      |
| 9.3            | On every page, is every list correctly structured (`<ul>`, `<ol>`, `<dl>`)?                       | Static |         | 1.3.1 (A)           | —        |
| 9.4            | On every page, is every quotation (block or inline) correctly marked up (`<blockquote>`, `<q>`)?  | Static |         | 1.3.1 (A)           | —        |

---

## Theme 10 — Information Presentation

| RGAA Criterion | Description                                                                                                      | Mode                    | Finding | WCAG 2.2    | RAAM 1.1 |
| -------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------- | ------- | ----------- | -------- |
| 10.1           | Are stylesheets used to control presentation (no systematic inline styles)?                                      | Static                  |         | 1.3.1 (A)   | 8.1      |
| 10.2           | Does visible content remain present when stylesheets are disabled?                                               | Runtime                 |         | 1.3.2 (A)   | 8.1      |
| 10.3           | Does information remain understandable when stylesheets are disabled?                                            | Runtime                 |         | 1.3.2 (A)   | 8.2      |
| 10.4           | Does text remain readable and functional when character size is increased to 200%?                               | Runtime                 |         | 1.4.4 (AA)  | 8.4      |
| 10.5           | Are CSS background color and font color declarations made on the same elements (no orphaned color)?              | Static                  |         | 1.4.3 (AA)  | —        |
| 10.6           | Is every non-obvious link visually distinguishable from surrounding text (not by color alone)?                   | Static + Runtime        |         | 1.4.1 (A)   | —        |
| 10.7           | For every element receiving focus, is focus visible and not suppressed?                                          | Static + Runtime        |         | 2.4.7 (AA)  | 8.3      |
| 10.8           | Are hidden contents intended to be ignored by assistive technologies (`aria-hidden`, `visibility:hidden`, etc.)? | Static                  |         | 4.1.2 (A)   | —        |
| 10.9           | Is information never conveyed solely by the shape, size, or position of an element?                              | Static + Content review |         | 1.3.3 (A)   | 8.7      |
| 10.10          | Is information never conveyed solely by a typographic character (icon, symbol) without a text alternative?       | Static                  |         | 1.3.3 (A)   | 8.8      |
| 10.11          | Can content be presented without loss of information or functionality in reflow mode (320 CSS px)?               | Runtime                 |         | 1.4.10 (AA) | 8.5      |
| 10.12          | Can text spacing properties be overridden by the user without loss of content or functionality?                  | Runtime                 |         | 1.4.12 (AA) | 8.6      |
| 10.13          | Are additional contents appearing on hover or focus controllable by the user (dismissable, persistent)?          | Runtime                 |         | 1.4.13 (AA) | 8.9      |
| 10.14          | Are additional contents generated via CSS (`:before`, `:after` with informative content) accessible by keyboard? | Static + Runtime        |         | 2.1.1 (A)   | —        |

---

## Theme 11 — Forms

| RGAA Criterion | Description                                                                                                      | Mode                    | Finding | WCAG 2.2                          | RAAM 1.1 |
| -------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------- | ------- | --------------------------------- | -------- |
| 11.1           | Does every form field have a visible label programmatically associated to it?                                    | Static                  |         | 1.3.1, 2.4.6, 2.5.3, 3.3.2 (A/AA) | 9.1      |
| 11.2           | Is every label associated with a field relevant (not just "Field 1")?                                            | Content review          |         | 1.3.1, 2.4.6, 2.5.3 (A/AA)        | 9.2      |
| 11.3           | Are labels for fields with the same repeated function consistent across the page?                                | Static + Content review |         | 3.2.4 (AA)                        | 9.3      |
| 11.4           | In every form, is each label visually and structurally adjacent to its corresponding field?                      | Static                  |         | 3.3.2 (A)                         | 9.4      |
| 11.5           | Are related fields grouped where necessary (`<fieldset>`)?                                                       | Static                  |         | 1.3.1, 3.3.2 (A)                  | 9.5      |
| 11.6           | In every form, does each field group have a legend (`<legend>`)?                                                 | Static                  |         | 1.3.1, 3.3.2 (A)                  | 9.6      |
| 11.7           | For every field group, is the legend relevant?                                                                   | Content review          |         | 1.3.1, 3.3.2 (A)                  | 9.7      |
| 11.8           | Are items of the same kind in a select list (`<select>`) grouped with `<optgroup>` where necessary?              | Static                  |         | 1.3.1, 3.3.2 (A)                  | —        |
| 11.9           | Is the label of every form button relevant?                                                                      | Static + Content review |         | 4.1.2 (A)                         | —        |
| 11.10          | Is data input validated and are input errors rendered accessible (text error message associated with the field)? | Static + Runtime        |         | 3.3.1, 3.2.2 (A)                  | 9.8      |
| 11.11          | Are correction suggestions provided on error where possible?                                                     | Content review          |         | 3.3.3 (AA)                        | 9.9      |
| 11.12          | For critical form submissions (data deletion, transactions), can the user review and correct before confirming?  | Runtime                 |         | 3.3.4 (AA)                        | 9.10     |
| 11.13          | Do personal data fields have a relevant `autocomplete` attribute?                                                | Static                  |         | 1.3.5 (AA)                        | 9.11     |

---

## Theme 12 — Navigation

| RGAA Criterion | Description                                                                                       | Mode                    | Finding | WCAG 2.2         | RAAM 1.1 |
| -------------- | ------------------------------------------------------------------------------------------------- | ----------------------- | ------- | ---------------- | -------- |
| 12.1           | Does the site provide at least two navigation systems (menu, site map, search engine)?            | Static + Content review |         | 2.4.5 (AA)       | —        |
| 12.2           | Are the navigation menu and bars located at the same position on every page?                      | Runtime                 |         | 3.2.3 (AA)       | —        |
| 12.3           | Is the site map page relevant and up to date?                                                     | Content review          |         | 2.4.5 (AA)       | —        |
| 12.4           | If a search engine is present, is it reachable in the same way from every page?                   | Static + Runtime        |         | 2.4.5 (AA)       | —        |
| 12.5           | Is each group of links of the same type identifiable (nav with label, structured list)?           | Static                  |         | 2.4.5 (AA)       | —        |
| 12.6           | Are navigation links available to quickly reach the main content areas (`<main>`, `<nav>`, etc.)? | Static                  |         | 2.4.1 (A)        | —        |
| 12.7           | Is a skip link or quick access link to the main content area present and functional?              | Static + Runtime        |         | 2.4.1 (A)        | —        |
| 12.8           | Is the tab order consistent with the reading order (no `tabIndex` > 0)?                           | Static + Runtime        |         | 2.4.3, 2.1.1 (A) | 10.1     |
| 12.9           | Does navigation contain no keyboard trap (focus never gets stuck)?                                | Runtime                 |         | 2.1.2 (A)        | 10.3     |
| 12.10          | Are single-key keyboard shortcuts controllable by the user (disableable or remappable)?           | Static + Runtime        |         | 2.1.4 (A)        | 10.4     |
| 12.11          | Can additional contents appearing on focus or hover be dismissed or filtered?                     | Runtime                 |         | 2.1.1 (A)        | —        |

---

## Theme 13 — Consultation

| RGAA Criterion | Description                                                                                        | Mode                    | Finding | WCAG 2.2            | RAAM 1.1 |
| -------------- | -------------------------------------------------------------------------------------------------- | ----------------------- | ------- | ------------------- | -------- |
| 13.1           | Does the user have control over every time limit that modifies content (session, timeout)?         | Runtime                 |         | 2.2.1 (A)           | 11.2     |
| 13.2           | Is every new window or tab opened at the user's initiative, or with prior warning?                 | Static + Content review |         | 3.2.1 (A)           | —        |
| 13.3           | Does every downloadable office document have an accessible version where necessary?                | Content review          |         | — (10.x EN 301 549) | 11.9     |
| 13.4           | For every office document with an accessible version, is that version relevant?                    | Content review          |         | — (10.x EN 301 549) | 11.10    |
| 13.5           | Does every cryptic content (ASCII art, emoticons, cryptic syntax) have a text alternative?         | Static + Content review |         | 1.1.1 (A)           | —        |
| 13.6           | For every cryptic content with an alternative, is the alternative relevant?                        | Content review          |         | 1.1.1 (A)           | —        |
| 13.7           | Do sudden brightness changes or flash effects meet thresholds (no more than 3 flashes per second)? | Runtime                 |         | 2.3.1 (A)           | 11.4     |
| 13.8           | Can every automatically moving or updating content be controlled (pause, stop)?                    | Runtime                 |         | 2.2.2 (A)           | 11.3     |
| 13.9           | Is content viewable regardless of screen orientation (portrait and landscape)?                     | Runtime                 |         | 1.3.4 (AA)          | 11.1     |
| 13.10          | Are features available via a complex gesture also available via a simple gesture?                  | Runtime                 |         | 2.5.1 (A)           | 11.5     |
| 13.11          | Can actions triggered by a pointing device be cancelled (no irreversible action on `mousedown`)?   | Runtime                 |         | 2.5.2 (A)           | 11.6     |
| 13.12          | Can features requiring device motion be satisfied by an alternative input?                         | Runtime                 |         | 2.5.4 (A)           | 11.7     |

---

## Optional Domain Profiles (Additive — do not replace the RGAA grid)

After completing the full RGAA grid, add profile-specific checks when relevant:

- **E-commerce**: cart totals, coupon flows, checkout constraints, delivery and returns comprehension
- **Media/Editorial**: transcripts, captions, reading modes, chapter and playlist navigation
- **Data-heavy/Admin**: dense tables, bulk actions, virtualization, command discoverability
- **Authentication/Identity**: MFA fallback, timeout messaging, recovery flow accessibility

See `domain-profiles.md` for details on each profile.
