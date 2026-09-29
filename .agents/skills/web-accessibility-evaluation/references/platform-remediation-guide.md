<!-- AUTO-GENERATED from source/. Do not edit here — edit source/ and run `pnpm build`. -->

# Web Accessibility Evaluation (WCAG 2.2 AA)

## Description

This skill provides a comprehensive methodology for auditing and fixing **web** accessibility issues using the Vitamin Play Design System. It enforces WCAG 2.2 Level AA, RGAA 4.1, and EN 301 549 compliance by leveraging Vp\* components with built-in accessibility, semantic design tokens for guaranteed contrast ratios, and established patterns for forms, modals, and interactive elements. Cross-reference tables map every criterion across WCAG 2.2, EN 301 549 v3.2.1, RGAA 4.1, and RAAM 1.1 for complete traceability.

The skill combines automated scanning (axe DevTools, Lighthouse), manual testing (keyboard navigation), and screen reader validation to ensure complete accessibility coverage. All examples are provided in **React syntax** and must be adapted to Vue or Svelte as needed.

## When to use this skill

Use this skill when you need to:

- **Audit existing web code** for accessibility violations (axe-core, Lighthouse reports)
- **Fix specific violations** like missing labels, insufficient contrast, or keyboard issues
- **Implement accessible forms** with proper labeling, error handling, and validation
- **Build accessible modals/dialogs** with focus management and keyboard support
- **Choose the right Vitamin Play component** for interactive elements (buttons, inputs, etc.)
- **Ensure WCAG 2.2 AA compliance** before production deployment
- **Adapt patterns** from React to Vue or Svelte frameworks
- **Generate a Developer Testing Plan** alongside any full app audit — a personalized markdown guide that walks the developer step-by-step through keyboard, screen reader, dynamic states, and reflow checks that code analysis cannot cover

**Load reference files** (`references/*.md`) only when you need deeper guidance on specific topics like ARIA patterns, complete form patterns, or testing methodology.

**Important for full application audits**: if the request targets a full app (multiple routes/pages), load `../standards/templates/rgaa-audit-template.md` first, duplicate it into your audit artifact, and fill it criterion-by-criterion. Preserve the template structure in the generated report, including the `Mode`, `WCAG 2.2`, and `RAAM 1.1` columns. Do not collapse the grid into a reduced table unless the user explicitly requests a simplified export. This template provides the 106 official RGAA 4.1 criteria as a structured audit grid — evaluate every applicable criterion as `PASS`, `FAIL: description`, `N/A`, or `RUNTIME_REQUIRED`, with WCAG 2.2 and RAAM 1.1 equivalences already populated from the shared cross-reference source. The report must also include the `Full Issues Inventory` section defined by the template so that criterion-level failures and concrete issue instances are both documented. Then generate the companion **Developer Testing Plan** using `references/developer-testing-guide-template.md` — this plan walks the developer step-by-step through every check that cannot be verified from static code alone.

---

## Quick Start (5 Minutes)

**⚠️ Important**: All code examples in this skill use **React syntax** (`onClick`, `onChange`, etc.). If working with Vue or Svelte, adapt the syntax accordingly:

- **Vue**: Use `@click`, `@input` and import from `@vtmn-play/vue`
- **Svelte**: Use `on:click`, `on:change` and import from `@vtmn-play/svelte`

### 1. Component-First Philosophy

**Always prefer Vitamin Play components** - they have accessibility built-in:

- **Icons**: Vitamin Play icons are `aria-hidden="true"` by default. You don't need to add it manually unless you're using a raw SVG.

```tsx
// ❌ WRONG - Native elements, manual accessibility
<button onClick={handleClick}>Submit</button>
<div onClick={handleDelete}>Delete</div>

// ✅ CORRECT - Vitamin Play components with built-in a11y
import { VpButton } from "@vtmn-play/react";
<VpButton type="submit" onClick={handleClick}>Submit</VpButton>
```

### 2. Always Label Interactive Elements

Icon-only buttons MUST have accessible names. Use `aria-label` instead of `title` (which is often ignored by screen readers and inaccessible on mobile/keyboard).

```tsx
import { VpIconButton } from "@vtmn-play/react";
import { VpCloseIcon } from "@vtmn-play/icons/react";

// ❌ WRONG - No accessible name or unreliable title
<VpIconButton title="Close" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>

// ✅ CORRECT - aria-label provides robust name
<VpIconButton aria-label="Close dialog" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>
```

### 3. State Management for Toggle Elements

When a button toggles between two states (e.g., expanded/collapsed, recto/verso, play/pause), use `aria-pressed` or `aria-expanded`.

```tsx
// ✅ CORRECT - Toggle button state
const [isFlipped, setIsFlipped] = useState(false);
<VpButton
  type="button"
  aria-pressed={isFlipped}
  onClick={() => setIsFlipped(!isFlipped)}
>
  Flip Card
</VpButton>;
```

### 4. Use Semantic Color Tokens

Never hardcode colors - use design system tokens:

```tsx
// ❌ WRONG - Hardcoded colors, no theme support
<div style={{ color: '#dc2626', background: '#fee2e2' }}>
  Error message
</div>

// ✅ CORRECT - Semantic tokens with guaranteed contrast
<div style={{
  color: 'var(--vp-semantic-color-content-negative)',
  background: 'var(--vp-semantic-color-background-negative)'
}}>
  Error message
</div>
```

---

## The 5-Step Accessibility Audit Process

### Step 1: Run Automated Scan

Use **axe DevTools** browser extension (primary tool):

1. Open DevTools (F12)
2. Navigate to "axe DevTools" tab
3. Click "Scan ALL of my page"
4. Review violations by severity
5. Note the WCAG criteria violated

**Common violations detected:**

- Missing alt text on images
- Insufficient color contrast
- Form inputs without labels
- Missing ARIA attributes
- Focus order issues

```tsx
// Example fix: Missing alt text
// axe reports: "Images must have alternate text"

// ❌ Before
<img src="product.jpg" />

// ✅ After
<img src="product.jpg" alt="Mountain bike with 21-speed gears" />
```

### Step 2: Fix Interactive Elements

Replace non-semantic elements with Vitamin Play components:

```tsx
// ❌ WRONG - div is not keyboard accessible
<div onClick={handleSave} className="button">
  Save changes
</div>

// ✅ CORRECT - VpButton has keyboard support
import { VpButton } from "@vtmn-play/react";
<VpButton onClick={handleSave}>Save changes</VpButton>

// ❌ WRONG - Native button with icon, no label
<button onClick={handleEdit}>
  <EditIcon />
</button>

// ✅ CORRECT - VpIconButton with aria-label
import { VpIconButton } from "@vtmn-play/react";
import { VpEditIcon } from "@vtmn-play/icons/react";
<VpIconButton aria-label="Edit product" onClick={handleEdit}>
  <VpEditIcon />
</VpIconButton>
```

**Decision tree for buttons:**

```
Need clickable element?
├─ Has visible text → <VpButton>
├─ Icon only → <VpIconButton aria-label="...">
├─ Navigates to URL → <VpButton href="...">
└─ Submits form → <VpButton type="submit">
```

### Step 3: Fix Form Accessibility

Use `VpFormControl` pattern for all form inputs:

```tsx
import {
  VpFormControl,
  VpFormLabel,
  VpInput,
  VpFormError,
  VpFormHelper,
} from "@vtmn-play/react";

// ❌ WRONG - Input without label
<input type="email" placeholder="Email" />

// ❌ WRONG - Label not programmatically associated
<label>Email</label>
<input type="email" name="email" />

// ✅ CORRECT - VpFormControl handles association
<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
  <VpFormHelper>We'll never share your email</VpFormHelper>
</VpFormControl>

// ✅ CORRECT - With error state
<VpFormControl isInvalid={!!error}>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" value={email} />
  {error && <VpFormError>{error}</VpFormError>}
</VpFormControl>
// VpFormControl automatically adds:
// - aria-invalid="true"
// - aria-describedby linking to error message
```

**For checkboxes:**

```tsx
import { VpCheckbox } from "@vtmn-play/react";

// ❌ WRONG - Native checkbox without proper label
<input type="checkbox" id="terms" />
<label htmlFor="terms">I accept terms</label>

// ✅ CORRECT - VpCheckbox with built-in label
<VpCheckbox name="terms" required>
  I accept the terms and conditions
</VpCheckbox>
```

### Step 4: Fix Color Contrast

Check and fix contrast issues with semantic tokens:

```tsx
// ❌ WRONG - Insufficient contrast (2.8:1)
<p style={{ color: '#999999', background: '#ffffff' }}>
  Gray text on white - fails WCAG AA
</p>

// ✅ CORRECT - Semantic token ensures 4.5:1 minimum
<p style={{
  color: 'var(--vp-semantic-color-content-primary)',
  background: 'var(--vp-semantic-color-background-primary)'
}}>
  Primary text with sufficient contrast
</p>

// ✅ CORRECT - Status colors with paired backgrounds
<div style={{
  color: 'var(--vp-semantic-color-content-negative)',
  background: 'var(--vp-semantic-color-background-negative)',
  border: '1px solid var(--vp-semantic-color-border-negative)'
}}>
  Error message with accessible contrast
</div>
```

**Quick contrast check:**

- **4.5:1** required for normal text (< 18pt)
- **3:1** required for large text (18pt+) and UI components
- **Use semantic tokens** to guarantee compliance

### Step 5: Test Keyboard Navigation

**Manual keyboard test** (unplug your mouse!):

1. Press **Tab** - Does focus move to all interactive elements?
2. Is **focus indicator visible** at all times?
3. Press **Enter/Space** - Do buttons activate?
4. Press **Escape** - Do modals close?
5. Check **tab order** - Is it logical (top to bottom, left to right)?

```tsx
// ✅ Ensure focus visibility (VpButton has this built-in)
// Custom elements need this CSS:
.custom-button:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}

// ❌ NEVER remove focus outlines
.button:focus {
  outline: none; // DON'T DO THIS
}
```

**Skip link implementation:**

```tsx
// Add at top of your layout
<a href="#main-content" className="skip-link">
  Skip to main content
</a>

<style>{`
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: var(--vp-semantic-color-background-brand);
    color: var(--vp-semantic-color-content-brand);
    padding: 0.5rem 1rem;
    z-index: 9999;
  }
  .skip-link:focus {
    top: 0;
  }
`}</style>

<main id="main-content" tabIndex={-1}>
  {/* Page content */}
</main>
```

---

## Common Violations & Quick Fixes

### Violation 1: Missing Alt Text

```tsx
// axe violation: "Images must have alternate text"
// ❌ Before
<img src="product.jpg" />

// ✅ After - Descriptive alt text
<img src="product.jpg" alt="Mountain bike with 21-speed gears" />

// ✅ After - Decorative image
<img src="decoration.svg" alt="" role="presentation" />
```

### Violation 2: Form Input Without Label

```tsx
// axe violation: "Form elements must have labels"
// ❌ Before
<input type="email" placeholder="Email" />

// ✅ After
<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
</VpFormControl>
```

### Violation 3: Insufficient Color Contrast

```tsx
// axe violation: "Elements must have sufficient color contrast"
// ❌ Before (2.8:1 contrast)
<span style={{ color: '#999999' }}>Important text</span>

// ✅ After (uses semantic token with 4.5:1+)
<span style={{ color: 'var(--vp-semantic-color-content-primary)' }}>
  Important text
</span>
```

### Violation 4: Button Without Accessible Name

```tsx
// axe violation: "Buttons must have discernible text"
// ❌ Before
<VpButton onClick={handleClose}>
  <VpCloseIcon />
</VpButton>

// ✅ After
<VpIconButton aria-label="Close dialog" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>
```

### Violation 5: Interactive Element Not Keyboard Accessible

```tsx
// axe violation: "Elements with click handlers must be focusable"
// ❌ Before
<div onClick={handleClick}>Click me</div>

// ✅ After
<VpButton onClick={handleClick}>Click me</VpButton>
```

---

## Modals & Dialogs

For accessible modal/dialog implementations, **load `references/dialog.md`** which covers:

- Complete VpModal patterns (confirmation, form, alert dialogs)
- Focus management and keyboard interactions
- ARIA attributes and announcements
- Advanced patterns (nested modals, complex forms)

---

## When to Load Reference Files

**Load these files only when you need deeper guidance:**

### `references/semantic.md` - Load when

- Choosing between multiple component options
- Need ARIA patterns for custom implementations
- Questions about heading hierarchy or landmarks
- "Which Vitamin Play component should I use?"

### `references/forms.md` - Load when

- Implementing complex forms with validation
- Need error message patterns
- Working with multiple form components
- Questions about live validation or error summaries

### `references/colors.md` - Load when

- Need complete list of semantic tokens
- Troubleshooting specific contrast issues
- Implementing dark mode support
- Manual contrast verification (includes tools & methodology)
- "Which color token should I use?"

### `references/navigation-and-focus.md` - Load when

- Implementing skip links
- Managing focus after interactions
- Custom keyboard navigation patterns
- Focus trap implementations

### `references/dialog.md` - Load when

- Advanced modal patterns (nested modals, form dialogs)
- Custom focus management in modals
- Multiple modal types (alert, confirmation, form)

### `references/advanced-patterns.md` - Load when

- Implementing tabs, accordions, dropdown menus
- Building tooltips, breadcrumbs, pagination
- Need alert/banner patterns
- Complex interactive patterns beyond basic buttons/forms
- "How do I build an accessible [tabs/accordion/menu]?"

### `references/testing.md` - Complete testing methodology, screen reader guide

### `../standards/templates/rgaa-audit-template.md` - RGAA 4.1 Audit Grid template (106 criteria)

- Use when auditing multiple routes/pages in any product domain (SaaS, media, e-commerce, admin, public sector)
- Structured around the 106 official RGAA 4.1 criteria across 13 themes — directly traceable to the normative standard
- Shared single source template used by Web, iOS, and Android skills
- Each criterion includes: detection mode (Static / Runtime / Content review), a `Finding` column to fill during the audit, and pre-populated WCAG 2.2 and RAAM 1.1 equivalences sourced from `../standards/cross-references/RGAA_CROSS_REFERENCE.toon`
- Forces explicit status per criterion (`PASS` / `FAIL: description` / `N/A` / `RUNTIME_REQUIRED`)
- Includes optional domain profiles as additive extensions (never replacing the RGAA grid)
- Requires explicit coverage reporting: `X/applicable` criteria, fails, runtime-pending

### `references/developer-testing-guide-template.md` - Personalized developer testing plan generator

- Use after every full app audit, alongside the audit report
- Generates a `reports/testing-plan-<date>.md` file tailored to the specific app (real routes, discovered interactions, identified runtime checks)
- Guides the developer through 7 phases: automated baseline, keyboard-only navigation, screen reader, dynamic states, forms deep-dive, zoom/reflow, end-to-end critical journeys
- Explains clearly why static analysis is insufficient and what must be verified by a human tester
- Every `RUNTIME_REQUIRED` check from the coverage matrix is mapped to a concrete scenario in the plan

### `../standards/templates/domain-profiles.md` - Optional domain-specific extensions for professional audits

- Use only after completing all core checks
- Adds controls for e-commerce, SaaS/dashboard, editorial/media, public sector, and identity flows
- Keeps deliverables traceable with profile-level coverage and failure counts

### `../standards/wcag-checklist.md` - Full WCAG 2.2 AA compliance checklist

### Standards cross-references (TOON) — Load from `../standards/cross-references/`

**`WCAG_CROSS_REFERENCE.toon`** — Load when:

- Need to find the RGAA, RAAM, or EN 301 549 equivalent of a WCAG criterion
- Mapping WCAG success criteria across all four accessibility standards
- Preparing a multi-standard compliance report
- "What is the RGAA equivalent of WCAG 1.4.3?"

**`RGAA_CROSS_REFERENCE.toon`** — Load when:

- Auditing against the French RGAA 4.1 standard (106 criteria)
- Working on a French public sector project requiring RGAA compliance
- "What WCAG criteria does RGAA 11.1 correspond to?"

**`RAAM_CROSS_REFERENCE.toon`** — Load when:

- Cross-platform audit: comparing web (RGAA) and mobile (RAAM) coverage
- Understanding RAAM themes 12-15 (EN 301 549-only, no WCAG equivalent)

### `rules/vitamin-play-a11y.md` - Batch auto-correction patterns & anti-patterns

### `rules/interactive-svg-patterns.md` - Interactive SVG accessibility rules (keyboard, roles, focus)

### Web-Specific Scan Patterns: `references/web-scan-patterns.md`

Grep patterns used by the Scout agent when auditing web codebases. Includes core patterns, advanced patterns (P1), and Vitamin Play design system patterns.

---

## Limitations

This skill performs **static code analysis**. It CANNOT reliably detect:

- Color contrast ratios (requires rendered pixels and computed styles)
- Keyboard interaction behavior (requires event loop)
- Screen reader announcement quality (requires AT)
- Tab/focus order (requires rendered CSS layout)
- Content relevance of alt text (requires semantic understanding of images)
- CMS/API data quality (requires runtime data)
- Custom element ARIA via `ElementInternals` (invisible in markup)
- Live region debounce and timing behavior (runtime-dependent)

Items that depend on these factors are marked `RUNTIME_REQUIRED` in reports.
Always complement this audit with runtime testing (axe-core) and manual testing.

See `../standards/templates/coverage-disclaimer.md` for the full mandatory blind spots appendix.

---

## Risk Assessment (replaces numeric scoring)

Audit reports use a **Risk Assessment** instead of a numeric score. A numeric score (e.g., 85/100) can falsely reassure a team actually at 60% RGAA compliance.

| Risk Level | Meaning |
| ---------- | ------- |
| 🟢 LOW RISK | Few or no deterministic violations. Ready for runtime testing. |
| 🟡 MODERATE RISK | Several violations + RUNTIME_REQUIRED items needing verification. |
| 🔴 HIGH RISK | Multiple critical violations. Fix before proceeding to runtime testing. |

> **Note**: This is NOT a compliance score. Only a full audit (automated + manual) can determine WCAG/RGAA conformance level.

---

## Testing Checklist

After fixes, verify with this checklist:

### Automated

- [ ] axe DevTools scan shows 0 violations
- [ ] Lighthouse accessibility score > 90
- [ ] All images have alt text
- [ ] All form inputs have labels
- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 UI)

### Keyboard

- [ ] Tab navigates to all interactive elements
- [ ] Focus indicator visible at all times
- [ ] Tab order is logical
- [ ] Enter/Space activate buttons
- [ ] Escape closes modals
- [ ] Skip link appears on first Tab

### Screen Reader (spot check)

- [ ] VoiceOver/NVDA announces page title
- [ ] Button roles announced correctly
- [ ] Form labels read with inputs
- [ ] Error messages announced
- [ ] Modal opens and title announced

---

## Resources

- **Vitamin Play Components**: `@vtmn-play/react`, `@vtmn-play/vue`, `@vtmn-play/svelte`
- **Design Tokens**: `@vtmn-play/design-tokens`
- **Icons**: `@vtmn-play/icons/react`, `@vtmn-play/icons/vue`, `@vtmn-play/icons/svelte`
- **axe DevTools**: <https://www.deque.com/axe/devtools/>
- **WCAG 2.2**: <https://www.w3.org/WAI/WCAG22/quickref/>
- **EN 301 549 v3.2.1**: <https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf>
- **RGAA 4.1**: <https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/>
- **RAAM 1.1**: <https://accessibilite.public.lu/fr/raam1.1/referentiel-technique.html>

**Note**: All code examples use React syntax. Adapt to your framework (Vue/Svelte) as needed.
