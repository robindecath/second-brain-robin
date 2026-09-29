<!-- AUTO-GENERATED from source/. Do not edit here — edit source/ and run `pnpm build`. -->

# Accessibility Audit Methodology

This skill teaches **how to audit** a codebase for accessibility compliance. It is platform-agnostic — use alongside platform-specific references (`web-accessibility-evaluation`, `ios-accessibility-evaluation`, or `android-accessibility-evaluation`) for implementation-level fix code.

---

## 1. Environment Detection (MANDATORY first step)

Before auditing, silently build a context map from the workspace. Never ask the user — detect.

### 1.1 Platform Detection

| Signal                         | Platform | References to load                  |
| ------------------------------ | -------- | ----------------------------------- |
| `.tsx`/`.jsx`/`.vue`/`.svelte` | Web      | `../references/`     |
| `.swift`/`.xib`/`.storyboard`  | iOS      | `../references/`     |
| `.kt`/`.java` + `res/layout/`  | Android  | `../references/` |

### 1.2 Infrastructure Detection

Scan for existing accessibility tooling:

| What to detect        | Where to look                                                | Impact                           |
| --------------------- | ------------------------------------------------------------ | -------------------------------- |
| Runtime testing tools | `package.json` (`@axe-core/playwright`, `jest-axe`, `pa11y`) | Skip axe-detectable issues       |
| CI/CD workflows       | `.github/workflows/**/*.yml` referencing axe/a11y            | Note as existing coverage        |
| Existing reports      | `*.a11y.json`, `axe-results.*`, SARIF files                  | Offer enrichment via Bridge      |
| Existing a11y tests   | `*.a11y.{test,spec}.*`                                       | Mark routes as partially covered |
| Design system         | Vitamin Play, Material, HIG, custom                          | Adapt fix recommendations        |

### 1.3 Behavior Adaptation

- If axe-core is in CI → skip axe-detectable issues, focus on static-only patterns
- If existing a11y tests cover a route → note as "partially covered" in inventory
- If no automated tooling exists → recommend setting up runtime scanning

### 1.4 axe-core Runtime Scan (Web only, optional)

When no runtime tooling is detected, a one-time scan can be run:

```bash
npx @axe-core/cli <url> --reporter json --tags wcag2a,wcag2aa
```

Results are integrated as "Automated Runtime Findings" in the report, placed before static findings. Any issue found by axe is NOT repeated in static findings.

---

## 2. Coverage Strategy

### 2.1 Scope Determination

| Request type       | Action                               | Focus                            |
| ------------------ | ------------------------------------ | -------------------------------- |
| Specific component | Read component + styles + tests      | Component patterns               |
| Entire page/screen | Read page + all used components      | Structure, landmarks, navigation |
| Code directory     | Glob directory, read relevant files  | Pattern consistency              |
| Full application   | Complete inventory + systematic scan | Coverage completeness            |

### 2.2 Coverage Inventory (MANDATORY)

Every audit MUST produce:

- **Route/Screen Inventory** — ALL routes/screens found, each marked:
  - `AUDITED` — file read and patterns run
  - `PARTIALLY_AUDITED` — patterns run but file not fully read
  - `SKIPPED (reason)` — not examined
- **Feature Directory Inventory** — all feature/component directories with audit status
- **File Read Log** — every file explicitly read (becomes appendix)
- **Scope Limitations** — if >200 component files, acknowledge potential gaps

For web form audits, the final findings must explicitly name `autocomplete` for
personal-data inputs and `<fieldset>` / `<legend>` for related control groups
when those checks are in scope. Do not replace these terms with a generic
"form semantics" summary: the report should identify the concrete HTML pattern
and the relevant WCAG criterion.

### 2.3 Audit Template Selection

- Web/RGAA → use RGAA audit template (106 criteria)
- Mobile/RAAM → use RAAM audit template (83 criteria)
- If domain-specific → load domain profiles (e-commerce, media, etc.)

---

## 3. WCAG 2.2 AA Evaluation

Systematically check against the four WCAG principles.

### A. Perceivable

- **1.1.1** Non-text Content — all informative images have text alternatives
- **1.3.1** Info and Relationships — semantic structure matches visual presentation
- **1.3.5** Identify Input Purpose — personal data fields have `autocomplete` / `textContentType` / `autofillHints`
- **1.4.3** Contrast — text ≥ 4.5:1, large text ≥ 3:1
- **1.4.11** Non-text Contrast — UI components/graphics ≥ 3:1
- **1.4.12** Text Spacing — no content loss when spacing increased
- **1.4.13** Content on Hover or Focus — dismissible, hoverable, persistent

### B. Operable

- **2.1.1** Keyboard — all functionality via keyboard/switch
- **2.1.2** No Keyboard Trap — focus can always escape
- **2.4.1** Bypass Blocks — skip navigation mechanism available
- **2.4.3** Focus Order — logical, matches visual order
- **2.4.7** Focus Visible — visible focus indicator on interactive elements
- **2.5.3** Label in Name — visible text matches accessible name
- **2.5.8** Target Size — touch targets ≥ 24×24px (web) / **44pt minimum** (iOS) / **48dp minimum** (Android)

### C. Understandable

- **3.1.1** Language of Page — language declared
- **3.2.1** On Focus — no unexpected context changes
- **3.3.1** Error Identification — errors identified in text
- **3.3.2** Labels or Instructions — inputs have labels
- **3.3.3** Error Suggestion — correction guidance provided

### D. Robust

- **4.1.2** Name, Role, Value — semantic elements or correct ARIA
- **4.1.3** Status Messages — dynamic updates announced

---

## 4. Classification Rules

### 4.1 Conditional Compliance Classifier (MANDATORY)

When evaluating attributes whose value comes from a variable (prop, API data, state):

| Pattern                                                 | Classification       | Rationale                            |
| ------------------------------------------------------- | -------------------- | ------------------------------------ |
| Code guarantees non-empty accessible value in ALL cases | **PASS**             | Structurally compliant               |
| Code has fallback to empty string or null               | **RUNTIME_REQUIRED** | Empty fallback = potential violation |
| No fallback and source could be empty                   | **FAIL**             | No guarantee of compliance           |

**Rule**: Never mark a data-dependent attribute as PASS unless code structurally guarantees compliance.

### 4.2 Content Visibility Decision Matrix

| Intent                   | Visual | Screen Reader | Focusable            | Implementation                                       |
| ------------------------ | ------ | ------------- | -------------------- | ---------------------------------------------------- |
| Visible to all           | Yes    | Yes           | Yes                  | Standard rendering                                   |
| Screen reader only       | No     | Yes           | Yes (if interactive) | Visually-hidden utility                              |
| Visual only (decorative) | Yes    | No            | No                   | `aria-hidden="true"` / `role="presentation"`         |
| Hidden for all           | No     | No            | No                   | `hidden` / `display:none` / `isHidden` / `View.GONE` |

**Critical rule**: If an element can receive focus, it MUST NOT be hidden from AT. Flag as CRITICAL.

### 4.3 Severity Levels

| Level        | Definition                        | Examples                                                         |
| ------------ | --------------------------------- | ---------------------------------------------------------------- |
| **Critical** | Blocks keyboard/AT users entirely | Focus trap, form unusable with AT, focusable but hidden          |
| **High**     | Significantly degrades usability  | No accessible name, no focus indicator, broken heading hierarchy |
| **Medium**   | Minor usability concern           | Non-optimal semantics, borderline contrast, missing hint text    |
| **Low**      | Convention improvement            | Component consolidation, documentation gaps                      |

### 4.4 Confidence Levels

- **HIGH**: Violation is deterministic from code (wrong role, missing attribute)
- **MEDIUM**: Likely violation but depends on runtime values
- **LOW**: Pattern suggests violation but depends entirely on external data

### 4.5 Risk Assessment

| Condition                                           | Risk Level       |
| --------------------------------------------------- | ---------------- |
| 0 CRITICAL + 0-2 HIGH + all HIGH confidence         | 🟢 LOW RISK      |
| 0 CRITICAL + 3+ HIGH, or many RUNTIME_REQUIRED      | 🟡 MODERATE RISK |
| 1+ CRITICAL, or 5+ HIGH with deterministic evidence | 🔴 HIGH RISK     |

> **Note**: Risk assessment is NOT a compliance score. Only full automated + manual audit determines conformance.

---

## 5. Systematic Scan Checklist (all platforms)

Run **every** group below — do not stop at the obvious WCAG violations. Many real
defects are missing semantics on elements that "look fine", and each item here is a
separate finding when present. Report each occurrence, then note systemic patterns.

**Precision discipline** — every finding must point to a concrete defect in the code:

- Before flagging **colour-only**, confirm no adjacent text conveys the same meaning. A visible text label beside a coloured cue (e.g. a status word next to a colour) is sufficient — do **not** flag it.
- Before flagging a **new-window** link, confirm `target="_blank"` is actually present on that link.
- Do not raise speculative preferences (e.g. "this could be a list") unless the missing semantics cause a real barrier, and never re-flag a correct implementation.

### 5.1 Names & text alternatives

- Interactive elements (links, buttons, icon-buttons, custom controls) without an accessible name
- Informative images/icons with no text alternative (and `alt=""` on images that ARE informative)
- Non-text status conveyed by glyphs/colour only (e.g. star ratings) with no text equivalent
- **Mobile (iOS)**: irreversible or payment actions without `.accessibilityHint(...)` — FAIL; use the term `accessibilityHint` in the finding
- **Mobile (Android)**: non-button tappable elements without `Modifier.clickable(onClickLabel = ...)` — FAIL; use the term `onClickLabel` in the finding

### 5.2 Structure, landmarks & headings

- **Landmark completeness**: a banner/`<header>`, `<main>`, `<nav>` (labelled when more than one), and `<footer>`/contentinfo. Flag a masthead that is a bare `<div>`, and groups of nav links not inside a `<nav>`.
- **Heading completeness**: every content section has a heading; no skipped levels; exactly one logical `<h1>`; **no styled `<p>`/`<div>` acting as a visual heading**; no duplicate/ambiguous headings reused for different sections.
- **Real semantics, not visual fakes**: lists built from `<div>`s + bullet/number glyphs instead of `<ul>`/`<ol>`; data tables using `<td>` for headers (require `<th scope>` + `<caption>`).
- **Document title**: in SPAs, the `<title>` must be unique and updated per route — flag a single static/generic title.
- **Language**: page `lang`, and `lang` on inline passages in another language.

### 5.3 Forms

- Every control has a programmatically-associated label (not placeholder-only, not a sibling `<span>`, not a `htmlFor` pointing at a non-existent id)
- **Related controls grouped** in `<fieldset>` with a `<legend>` (consent blocks, radio/checkbox groups)
- **Required fields** are programmatically required (`required`/`aria-required`) and indicated by more than colour (not a red `*` alone)
- **Errors**: associated to their field (`aria-describedby` + `aria-invalid`), announced on submit (live region and/or focus moved to first invalid/summary), and give **correction guidance** (expected format), not just "X is required"
- Personal-data fields have correct `autocomplete` tokens (web) / `textContentType` (iOS) / `KeyboardOptions(keyboardType = ...)` (Android)
- **Mobile (iOS)**: every `TextField`/`VpTextField` for payment or personal data must set `textContentType`; missing → FAIL
- **Mobile (Android)**: every `OutlinedTextField`/`VpTextField` for payment or personal data must set `keyboardType`; missing → FAIL

### 5.4 Composite widgets — check the WHOLE pattern, not one symptom

- **Tabs**: role=tab/tablist AND keyboard AND `aria-selected` AND panels associated (`role=tabpanel`/`aria-labelledby`)
- **Dialog/modal**: `role=dialog`+`aria-modal` AND accessible name AND focus moved in/trapped AND **Escape + a labelled close control** AND focus restored
- **Disclosure/accordion**: `<button aria-expanded>` (not clickable `<div>`)
- **Carousel**: a labelled region/group, and slide changes announced
- **Progress**: `role=progressbar` with `aria-valuenow/min/max` (not a bare styled `<div>`)
- **Mobile (iOS) grouping**: cards and list rows with multiple sub-elements must use `.accessibilityElement(children: .combine)` — missing → FAIL; use the term `combine` in the finding
- **Mobile (Android) grouping**: cards and list rows with multiple sub-elements must use `Modifier.semantics(mergeDescendants = true)` — missing → FAIL; use the term `mergeDescendants` in the finding

### 5.5 Media

- `<video>`/`<audio>`: captions (`<track kind="captions">`) / transcript; **no autoplay without a pause/stop**; native (or accessible) controls and an accessible name

### 5.6 Navigation & consultation

- Skip link to main content; logical focus/navigation order; no positive `tabindex`
- Ambiguous link text ("click here", "read more", repeated identical link text)
- Links opening a new window/tab warn the user
- Status messages announced; live region urgency appropriate (no `assertive` where `polite` suffices); hidden content not focusable
- **Mobile (iOS)**: every dynamic state update (cart total, search results, error) must call `UIAccessibility.post(notification: .announcement, ...)` — missing → FAIL or RUNTIME_REQUIRED; use the word `announcement` in the finding
- **Mobile (Android)**: every dynamic state update must call `view.announceForAccessibility(...)` or set `Modifier.semantics { liveRegion = LiveRegionMode.Polite }` — missing → FAIL or RUNTIME_REQUIRED; use the term `announceForAccessibility` in the finding

### 5.7 Design System Conformance (when a design system is detected)

If environment detection found a design system (e.g. **Vitamin Play**, Material, HIG), run a
conformance pass **in addition** to the WCAG checks: **every raw element used where an
accessible design-system component exists is a finding** (severity **medium**,
type _design-system migration_) — even if it is otherwise accessible — because the
component ships extra accessibility guarantees the hand-rolled version lacks.

Load the platform's design-system rules (e.g. `references/`/`rules/`) for the exact
component map, then flag raw uses such as:

| Raw element used                      | Should use (Vitamin Play example)                         |
| ------------------------------------- | --------------------------------------------------------- |
| `<button>` / `<div onClick>` action   | `VpButton`                                                |
| icon-only action                      | `VpIconButton` (forces an accessible name)                |
| `<input>` / `<textarea>` / `<select>` | `VpInput` / `VpTextarea` / `VpSelect` (+ `VpFormControl`) |
| native checkbox/radio                 | `VpCheckbox` / `VpRadio`                                  |
| number stepper                        | `VpInputQuantity`                                         |
| custom modal                          | `VpModal`                                                 |
| custom tabs / accordion               | the DS tabs / `VpAccordion`                               |
| hand-built nav/header                 | `VpNavigationHeader` / `VpLink`                           |

Emit a **separate** finding (type _design-system migration_) for **each** such raw
element — even when you have already raised a WCAG finding on that same element. The
two are distinct: the WCAG finding is the accessibility defect; the migration finding
is the missed design-system guarantee. Enumerate every instance, then also summarise
them as one systemic "adopt the design system" recommendation. A raw `<button>` with
text is still a migration finding even though it has an accessible name.

#### Design-system **contract compliance** (the component is used, but misused)

A design system splits responsibility: it handles some accessibility for you, but each
component has a **consumer-side contract** — things YOU must still provide. A `Vp*`
component used **without fulfilling its contract is a finding**, even though the component
itself is correct (this is the most common real-world failure in a codebase that already
uses the design system).

For every design-system component you see in the code, load its contract from
`references/vp-contracts/<component>.md` and verify each consumer requirement is met:

| Component used                        | Common unmet consumer requirement                                    |
| ------------------------------------- | -------------------------------------------------------------------- |
| `VpModal` / dialog                    | no accessible name (`aria-label`/labelled title)                     |
| `VpInput` / `VpSelect` / `VpTextarea` | not wrapped in `VpFormControl` + `VpFormLabel` (no associated label) |
| `VpIconButton`                        | missing `aria-label`                                                 |
| `VpCheckbox` / `VpRadio`              | no accessible label; group missing `role=group`/legend               |
| any required field                    | required state not indicated to the user (`requiredIndicator`/text)  |

Flag each unmet requirement as a finding citing the contract. Both directions matter:
**raw-where-a-component-exists** (migrate) AND **component-used-but-contract-unmet** (fulfil it).

---

## 6. Report Format

```markdown
# Accessibility Audit Report

**Target**: [app/component/screen name]
**Date**: [audit date]
**Platform**: [Web | iOS | Android]
**Standard**: WCAG 2.2 Level AA
**Additional standards**: [RGAA 4.1 | RAAM 1.1 | EN 301 549]

---

## Executive Summary

- ❌ **X Critical Issues** — Block keyboard/AT users entirely
- ⚠️ **Y High Priority Issues** — Significantly degrade usability
- ℹ️ **Z Medium Priority Issues** — Minor usability concerns
- ✅ **N Good Practices** — Correct implementations found

**Risk Assessment**: [🟢 LOW RISK | 🟡 MODERATE RISK | 🔴 HIGH RISK]

---

## Violation Table

| #   | Severity | WCAG SC | Location  | Description | Confidence |
| --- | -------- | ------- | --------- | ----------- | ---------- |
| 1   | CRITICAL | 4.1.2   | file:line | …           | HIGH       |

---

## Detailed Findings

### Issue #N: [Title]

**Severity**: [level]
**WCAG Criterion**: [Number] [Name]
**Location**: `[file:line]`
**Confidence**: [HIGH | MEDIUM | LOW] — [reason]

**Problem**: [explanation + user impact]

**Current Code**:
\`\`\`[language]
[problematic code]
\`\`\`

**Fix**:
\`\`\`[language]
[corrected code]
\`\`\`

---

## Positive Findings

| Pattern checked | Finding |
| --------------- | ------- |
| …               | ✅ …    |

---

## Priority Fix Order

1. [Issue] — **Blocks [users]** — Est. X min

---

## Appendix: Coverage Inventory

## Appendix: Blind Spots
```

---

## 7. Developer Testing Plan (MANDATORY for full audits)

Static analysis cannot verify: keyboard behavior, screen reader announcements, focus restoration, dynamic states, live region timing, zoom/reflow. Generate a companion testing plan covering:

| Category                  | Source                                            |
| ------------------------- | ------------------------------------------------- |
| Routes/Screens            | Inventory from environment detection              |
| Keyboard/Switch scenarios | RUNTIME_REQUIRED items from focus/keyboard checks |
| Screen reader scenarios   | RUNTIME_REQUIRED items from announcements         |
| Dynamic state scenarios   | RUNTIME_REQUIRED items from state transitions     |
| Form routes/screens       | Where form components were found                  |
| Critical journeys         | 1-3 core user paths inferred from app structure   |
| Content review items      | All CMS/API-dependent accessible values           |

**Minimum requirements**:

- Every RUNTIME_REQUIRED item appears at least once
- Routes/screens listed by name and path
- At least one end-to-end journey defined

---

## 8. Multi-Standard Mapping

Evaluate against WCAG 2.2 AA. To map findings to other standards, use cross-reference tables:

- WCAG → RGAA / RAAM / EN 301 549
- RGAA → WCAG / RAAM / EN 301 549
- RAAM → WCAG / RGAA / EN 301 549

---

## 9. Quality Assurance Checklist

Before finalizing any audit:

- [ ] Coverage Inventory produced
- [ ] Blind Spots Disclaimer included
- [ ] All applicable criteria evaluated
- [ ] Every finding has: WCAG SC, severity, location, confidence
- [ ] Conditional Compliance Classifier applied to data-dependent attributes
- [ ] Before/after code examples for every finding
- [ ] User impact explained for every finding
- [ ] Positive findings section included
- [ ] Risk Assessment stated
- [ ] Developer Testing Plan generated (full audits)
- [ ] Priority fix order established
- [ ] Dynamic content items (announcements, live regions) tagged `RUNTIME_REQUIRED` where device testing is needed — use the literal keyword `RUNTIME_REQUIRED` in the report
