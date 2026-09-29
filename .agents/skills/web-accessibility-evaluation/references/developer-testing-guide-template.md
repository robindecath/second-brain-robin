# Developer Accessibility Testing Guide — Template

**Purpose**: Generate a personalized, step-by-step manual testing plan for developers, based on the static audit findings of their specific application.

This template is filled in by the `accessibility-auditor` agent after the static scan. It produces a `testing-plan.md` file the developer can follow end-to-end to complete the accessibility validation that no automated tool can perform alone.

---

## How to Use This Template

When generating the testing plan:

1. Replace all `[PLACEHOLDER]` values with information from the actual app being audited
2. Keep only the phases that apply — remove or mark as `N/A` those that don't
3. Add app-specific interaction notes where behavior is unusual or complex
4. Output the final file as `<project>/reports/testing-plan-<date>.md`

---

## Output Template

---

````markdown
# Accessibility Manual Testing Plan — [APP_NAME]

**Generated**: [DATE]  
**Based on static audit**: [LINK_TO_AUDIT_REPORT or "see reports/audit-*.md"]  
**Standard**: WCAG 2.2 Level AA  
**Prepared by**: Accessibility Auditor Agent

---

## Why This Plan Exists

A static code analysis catches **structural violations** — missing labels, wrong element types, hardcoded colors, absent ARIA attributes. But a large portion of accessibility issues only appear at **runtime**, when a real user (or assistive technology) interacts with the interface.

This plan covers what the static scan _cannot_ verify:

| What static scan misses           | Why it matters                                       |
| --------------------------------- | ---------------------------------------------------- |
| Keyboard focus order              | DOM order ≠ visual order in some layouts             |
| Focus visibility in practice      | CSS overrides can neutralize outline after build     |
| Screen reader announcements       | ARIA attributes may be present but wrong value       |
| Live region timing                | Mounted too late → SR misses announcements           |
| Focus after modal close           | Code exists but doesn't execute correctly at runtime |
| Reflow at 320px / 400% zoom       | Layout may break or overlap at extreme magnification |
| Dynamic errors and loading states | Race conditions, async updates                       |
| End-to-end keyboard journeys      | Individual components pass but composited flow traps |

**Recommendation**: perform this plan in order. Each phase builds on the previous one.

---

## Tools to Set Up Before Starting

### Browser

- **Chrome** or **Firefox** (latest stable)
- Extension: **axe DevTools** (free tier) — https://www.deque.com/axe/devtools/
- Extension: **Colour Contrast Analyser** or use browser DevTools inspector

### Screen Readers (install at least one)

| Platform | Screen reader                 | Notes                     |
| -------- | ----------------------------- | ------------------------- |
| macOS    | **VoiceOver** (built-in)      | Activate: ⌘ + F5          |
| Windows  | **NVDA** (free)               | https://www.nvaccess.org/ |
| Windows  | **JAWS** (paid, 40-min trial) | Most used in enterprise   |
| iOS      | **VoiceOver** (built-in)      | Settings → Accessibility  |
| Android  | **TalkBack** (built-in)       | Settings → Accessibility  |

> For this audit, **[RECOMMENDED_SR]** is recommended because **[REASON — e.g., "the app targets a primarily macOS audience" or "NVDA + Chrome is the most common AT combination in your user base"]**.

### Zoom & Reflow

- Set browser zoom to **200%**, then **400%** (View → Zoom)
- Test **text-only zoom** in Firefox (View → Zoom → Zoom Text Only)
- For reflow: resize browser window to **320px wide** (DevTools → Responsive Design Mode → set width to 320)

---

## Routes to Test

The following routes were identified in the application. Follow the testing phases below for **each route**:

[ROUTE_TABLE — generated from app scan, example:]

| Route          | Page name   | Key interactions                           | Priority |
| -------------- | ----------- | ------------------------------------------ | -------- |
| `/`            | Home        | Navigation, hero CTA, featured links       | High     |
| `/catalog`     | Catalog     | Filters, search, item grid, pagination     | Critical |
| `/catalog/:id` | Book Detail | Add to cart, image gallery                 | High     |
| `/cart`        | Cart        | Item removal, quantity change, proceed CTA | Critical |
| `/checkout`    | Checkout    | Multi-field form, payment, submit          | Critical |
| `/account`     | Account     | Profile form, save actions                 | High     |
| `/contact`     | Contact     | Form, submit                               | Medium   |

> **Note**: Prioritize "Critical" routes first. These are user journeys where an accessibility failure directly blocks task completion.

---

## Phase 1 — Automated Scan Baseline

**Time**: ~15 min  
**Tool**: axe DevTools browser extension

For each route:

1. Navigate to the page
2. Open DevTools → axe DevTools tab → "Scan ALL of my page"
3. Record violations with their WCAG criterion reference
4. Screenshot each violation for the report
5. Re-run after fixes to verify resolution

### Checklist — Phase 1

- [ ] Scan complete for all routes listed above
- [ ] All Critical/Serious violations documented
- [ ] No new violations introduced since static audit

---

## Phase 2 — Keyboard-Only Navigation

**Time**: ~30 min  
**Setup**: Physically unplug or disable your mouse/trackpad  
**Browser**: Chrome or Firefox (no screen reader active)

### Global checks (do once, on any page)

- [ ] Press **Tab** from the browser address bar — does a **skip link** appear?
- [ ] Does pressing **Enter** on the skip link move focus directly to the main content area?
- [ ] Is the **focus indicator** visible at all times as you Tab through the page?
- [ ] Does focus ever **disappear** (jumps to `<body>` or becomes invisible)?

### Per-route keyboard checks

For each route, Tab through the **entire page** and verify:

- [ ] All interactive elements are **reachable by Tab** key
- [ ] **Tab order** is logical (matches visual reading order top-to-bottom, left-to-right)
- [ ] Buttons activate on **Enter** and **Space**
- [ ] Links activate on **Enter**
- [ ] Dropdowns/selects open on **Space** or arrow keys
- [ ] **Escape** closes modals, drawers, and overlays
- [ ] After closing a modal, **focus returns** to the trigger element

### App-specific keyboard scenarios to test

[KEYBOARD_SCENARIOS — generated from audit findings, example:]

> These scenarios were identified as **runtime-required** in the static audit:

| Scenario                         | Route       | What to verify                                                                       |
| -------------------------------- | ----------- | ------------------------------------------------------------------------------------ |
| Genre filter checkboxes          | `/catalog`  | Tab reaches each filter, Space toggles, focus order within fieldset is logical       |
| "Remove item" in cart            | `/cart`     | After removal, focus must not be lost — should move to next item or cart heading     |
| Checkout form submit with errors | `/checkout` | On failed submit, focus must move to first error or error summary                    |
| Modal (if present)               | [ROUTE]     | Escape closes, focus returns to trigger, cannot Tab outside while open               |
| Pagination                       | `/catalog`  | Tab reaches all page links, current page has `aria-current`, arrow keys not required |

### Keyboard — Pass Criteria

All critical user journeys can be completed start-to-finish using only Tab, Enter, Space, Escape, and arrow keys.

---

## Phase 3 — Screen Reader Testing

**Time**: ~45 min  
**Setup**: Enable [RECOMMENDED_SR], close unnecessary browser tabs  
**Browser**: [RECOMMENDED_BROWSER]  
**Mode**: Browse Mode (virtual cursor) for reading, Forms Mode for inputs

> **Tip for new screen reader users**: Start with VoiceOver (macOS) or NVDA (Windows). Learn to use the **heading navigation** shortcut (H on NVDA/JAWS, `VO + Command + H` on VoiceOver) to jump between sections quickly.

### Global checks (do once)

- [ ] Navigate to site — is the **page title** announced on load?
- [ ] Use heading navigation (H) — are all headings announced in logical order?
- [ ] Use landmark navigation (D on NVDA) — are `main`, `nav`, `header`, `footer` present and announced?
- [ ] Navigate to an image — is the **alt text** read? Decorative images should be silent.

### Per-route screen reader checks

For each route, navigate using virtual cursor (arrow keys) and verify:

- [ ] **Page title** is meaningful and unique (not just the app name)
- [ ] **Headings** (`h1`, `h2`…) create a coherent outline of the page
- [ ] **Links** are described — no "click here" or bare URLs read aloud
- [ ] **Buttons** announce their name AND role ("Add to cart, button")
- [ ] **Images** have descriptions or are ignored (decorative)
- [ ] **Form inputs**: label is read before or with the input ("Email, edit text")
- [ ] **Error messages** are announced — either via live region or when navigating to invalid field
- [ ] **Loading states**: spinner/skeleton triggers a SR announcement (not silent)
- [ ] **Toasts / banners**: SR reads the message (polite live region)

### App-specific SR scenarios to test

[SR_SCENARIOS — generated from audit findings, example:]

| Scenario              | Route          | What the SR should announce                                          |
| --------------------- | -------------- | -------------------------------------------------------------------- |
| Add item to cart      | `/catalog/:id` | A status message like "Product added to cart" (live polite region)   |
| Cart total update     | `/cart`        | Updated total must be announced after quantity change                |
| Form error on submit  | `/checkout`    | "3 errors were found" or focus to first error with error description |
| Filter results update | `/catalog`     | "X results" or similar after filter change                           |
| Empty cart state      | `/cart`        | "Your cart is empty" is read, not silently shown                     |

### Screen Reader — Pass Criteria

A user navigating only with a screen reader (no visual reference) can understand all content, operate all controls, and complete all critical journeys independently.

---

## Phase 4 — Dynamic States and Interactions

**Time**: ~20 min  
**Setup**: Normal browser with DevTools open (Network tab optional)  
**Tools**: axe DevTools, manual observation

These checks target **state transitions** that only occur at runtime:

### Loading states

- [ ] Trigger an async operation (search, filter, page load)
- [ ] Is there a visible loading indicator?
- [ ] Does the SR announce the loading state?
- [ ] When loading completes, does the SR announce the result or is focus moved appropriately?

### Error states

- [ ] Submit a form with invalid data
- [ ] Are error messages visible and styled clearly (not color-only)?
- [ ] Are errors associated with their fields (announced when navigating to the field)?
- [ ] Is an error summary present for multi-field forms?
- [ ] Does focus move to the error summary or first invalid field?

### Success / confirmation states

- [ ] Complete a successful action (e.g., add to cart, submit form)
- [ ] Is a success message shown AND announced by SR?
- [ ] Is the message permanent enough to be read? (Not dismissed in < 2 seconds)

### Modals and overlays

- [ ] Open a modal — does focus move inside?
- [ ] Can you Tab within the modal only (no escape to background)?
- [ ] Escape closes the modal — does focus return to the trigger?
- [ ] Is background content inert (not reachable by keyboard or SR)?

### App-specific dynamic scenarios

[DYNAMIC_SCENARIOS — generated from audit findings, example:]

| Scenario                           | Expected behavior                                                      |
| ---------------------------------- | ---------------------------------------------------------------------- |
| Filter change updates product list | SR announces "X results found" or heading is updated                   |
| Removing cart item                 | SR announces confirmation or item count; focus moves to next item      |
| Checkout step progression          | New step title/heading is announced; step indicator shows current step |

---

## Phase 5 — Forms Deep-Dive

**Time**: ~20 min  
**Relevant routes**: [FORM_ROUTES — e.g., `/checkout`, `/contact`, `/account`]

For each form:

- [ ] Every field has a visible, persistent **label** (not just placeholder)
- [ ] Labels are still visible when the field is filled
- [ ] **Required fields** are marked visually AND semantically (`required` / `aria-required`)
- [ ] Fields that accept personal data have appropriate `autocomplete` tokens (`email`, `tel`, `name`, `address-line1`…)
- [ ] **Related fields are grouped** (e.g., billing address uses `fieldset/legend`)
- [ ] Validation fires at an appropriate time (not on every keystroke)
- [ ] Error messages describe **what is wrong and how to fix it**
- [ ] Error messages are linked to their field (not just shown near it)

### Specific form checks for this app

[FORM_CHECKS — generated from audit findings]

---

## Phase 6 — Zoom and Reflow

**Time**: ~15 min  
**Setup**: Modern Chrome or Firefox, DevTools for width simulation

### Text zoom

- [ ] Set Firefox to **Zoom Text Only** at 200%
- [ ] Is all text still readable? Does it overflow or clip?
- [ ] Are interactive targets still usable?

### Page zoom at 200%

- [ ] Zoom browser to **200%** on each route
- [ ] Can you still complete all critical journeys?
- [ ] Does horizontal scrolling appear? (Should not, except for tables/maps)

### Reflow at 320px

- [ ] In DevTools responsive mode, set viewport width to **320px**
- [ ] Is all content visible without horizontal overflow?
- [ ] No content is hidden or clipped at this viewport
- [ ] All interactive elements still reachable

### Text spacing override

- [ ] In browser DevTools (or a userscript), inject:
  ```css
  * {
    line-height: 1.5 !important;
    letter-spacing: 0.12em !important;
    word-spacing: 0.16em !important;
  }
  ```
````

- [ ] Does any content break, overlap, or become unreadable?

---

## Phase 7 — End-to-End Critical User Journeys

**Time**: ~30 min  
**Mode**: Keyboard-only first, then repeat with screen reader

These are the highest-priority journeys to verify **start to finish**:

[CRITICAL_JOURNEYS — generated from app structure, example:]

### Journey 1: [JOURNEY_NAME]

**Route sequence**: [e.g., Home → Catalog → Detail → Cart → Checkout]  
**Keyboard**: Can this journey be completed without a mouse?  
**Screen reader**: Can a SR user understand each step and continue independently?

Steps:

1. [STEP_1]
2. [STEP_2]
3. [STEP_N]

**Pass criteria**: Journey completed start-to-finish without keyboard traps, missed announcements, or unintelligible states.

---

## Phase 8 — Content Review (CMS/API-Dependent Items)

**Time**: ~20 min  
**Mode**: Visual inspection of rendered content, cross-referencing with code audit findings  
**Relevant items**: All findings marked `RUNTIME_REQUIRED` or `MEDIUM`/`LOW` confidence in the static audit

This phase verifies that data-dependent accessibility attributes produce meaningful values at runtime. These cannot be validated from source code because their values come from CMS, APIs, or databases.

### Images with data-dependent alt text

[CONTENT_REVIEW_IMAGES — generated from audit findings, example:]

| Component/File | Location | What to verify |
| -------------- | -------- | -------------- |
| `ProductCard.tsx:42` | `/catalog` | `alt={product.caption}` — verify rendered images have meaningful alt, not empty strings |
| `HeroSection.tsx:15` | `/` | `alt={banner.altText ?? ""}` — verify CMS provides non-empty alt for informative hero images |

**How to test**: Navigate to each page, inspect images with browser DevTools (right-click → Inspect → check `alt` attribute value). Informative images must have descriptive alt text, not empty or generic values.

### Links with data-dependent accessible names

[CONTENT_REVIEW_LINKS — generated from audit findings, example:]

| Component/File | Location | What to verify |
| -------------- | -------- | -------------- |
| `ProductCard.tsx:38` | `/catalog` | Link wraps only `<img>` — verify link has accessible name (via alt or aria-label) |
| `ArticleList.tsx:22` | `/blog` | `<a>{article.title}</a>` — verify titles are never empty in CMS |

**How to test**: Use screen reader to navigate links (NVDA: K key, VoiceOver: VO+Command+L). Each link should announce its purpose clearly. "Link, image" or "Link" with no name = failure.

### Dynamic headings

[CONTENT_REVIEW_HEADINGS — generated from audit findings, example:]

| Component/File | Location | What to verify |
| -------------- | -------- | -------------- |
| `ProductDetail.tsx:8` | `/catalog/:id` | `<h1>{product.name}</h1>` — verify heading is never empty |
| `CategoryPage.tsx:12` | `/catalog` | `<h2>{category.title}</h2>` — verify hierarchy maintained with CMS categories |

**How to test**: Use heading navigation (H key in screen readers). Headings should form a logical outline and never be empty.

### Content Review — Pass Criteria

All data-dependent accessibility attributes render meaningful, non-empty values with actual production content. No informative images have empty alt text, no links are announced without a name, and heading hierarchy is maintained.

---

## Summary Checklist

| Phase                         | Status        | Issues found |
| ----------------------------- | ------------- | ------------ |
| Phase 1 — Automated scan      | ☐ Not started | —            |
| Phase 2 — Keyboard navigation | ☐ Not started | —            |
| Phase 3 — Screen reader       | ☐ Not started | —            |
| Phase 4 — Dynamic states      | ☐ Not started | —            |
| Phase 5 — Forms               | ☐ Not started | —            |
| Phase 6 — Zoom & reflow       | ☐ Not started | —            |
| Phase 7 — End-to-end journeys | ☐ Not started | —            |
| Phase 8 — Content review      | ☐ Not started | —            |

Update each phase status to `✅ Complete`, `⚠️ Issues found`, or `⏭️ Not applicable`.

---

## Reporting Runtime Findings

For each issue found during manual testing, document:

```markdown
### [ISSUE_ID] [Short description]

**Phase**: [Phase where found]  
**Route**: [URL]  
**WCAG criterion**: [e.g., 2.4.3 Focus Order (A)]  
**Severity**: Critical / High / Medium / Low  
**Steps to reproduce**:

1. Navigate to [route]
2. [Action]
3. [Observed behavior]

**Expected behavior**: [What should happen]  
**Actual behavior**: [What happens instead]  
**Assistive technology**: [SR + version + browser if applicable]
```

---

_This plan was generated automatically from the static audit of [APP_NAME]. Update it as issues are fixed and re-tested._

```

---

## Notes for the Auditor Agent

When generating the testing plan output:

- **[APP_NAME]**: Use the app package name or root heading found in the codebase
- **[DATE]**: Use current date
- **[ROUTE_TABLE]**: Build from routes discovered during file scanning (React Router, Next.js pages, etc.)
- **[RECOMMENDED_SR]**: Default to "NVDA + Chrome" unless the codebase or README indicates a specific audience
- **[KEYBOARD_SCENARIOS]**: Include all items marked `RUNTIME_REQUIRED` in the coverage matrix where the check domain is keyboard/focus (checks 021–040)
- **[SR_SCENARIOS]**: Include all items marked `RUNTIME_REQUIRED` related to announcements/live regions (checks 061–080)
- **[DYNAMIC_SCENARIOS]**: Include items marked `RUNTIME_REQUIRED` related to state transitions
- **[FORM_ROUTES]**: List routes where `<form>`, `<input>`, or form components were found during scan
- **[FORM_CHECKS]**: Include specific form validation items from the audit — especially `aria-invalid` timing and `autocomplete` checks
- **[CRITICAL_JOURNEYS]**: Identify 1–3 core user journeys based on the app's apparent purpose (e.g., "complete a purchase", "submit a contact request", "register an account") — include every route that is part of the journey
- **[CONTENT_REVIEW_IMAGES]**: All findings where `alt={variable}` patterns were flagged as RUNTIME_REQUIRED — list file:line and what to verify
- **[CONTENT_REVIEW_LINKS]**: All findings where link accessible names depend on dynamic content
- **[CONTENT_REVIEW_HEADINGS]**: All findings where heading content is data-driven

### Mapping Audit Findings to Test Items

Every item in the audit report feeds a specific test phase:

| Audit finding type | Maps to test phase |
| ------------------ | ------------------ |
| RUNTIME_REQUIRED (keyboard/focus) | Phase 2 — Keyboard scenarios |
| RUNTIME_REQUIRED (announcements) | Phase 3 — Screen reader scenarios |
| RUNTIME_REQUIRED (state transitions) | Phase 4 — Dynamic states |
| RUNTIME_REQUIRED (form validation) | Phase 5 — Forms |
| RUNTIME_REQUIRED (CMS/API content) | Phase 8 — Content review |
| MEDIUM confidence findings | Phases 2-4 (verify the violation exists at runtime) |
| LOW confidence findings | Phase 8 (verify data quality produces actual violations) |

**Minimum requirements:**
- Every `RUNTIME_REQUIRED` check from the coverage matrix appears at least once in the plan
- Every `MEDIUM` or `LOW` confidence finding appears as a verification item
- Routes are listed by name and path (not generic)
- At least one end-to-end journey is defined under Phase 7
- The intro paragraph (Why This Plan Exists) is kept verbatim

Always generate the testing plan **alongside** the audit report, not as a replacement. Both documents serve different audiences: the audit report documents violations; the testing plan guides the developer through what to verify themselves.
```
