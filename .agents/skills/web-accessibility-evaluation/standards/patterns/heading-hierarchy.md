# Heading Hierarchy

## Overview

Headings provide navigational structure for screen reader users — most navigate between headings to skim a page. Heading levels must form a logical outline, not be used for visual styling. (WCAG 1.3.1, 2.4.6)

## Rules

**One h1 per page/screen** — represents the page title or main topic.

**Never skip levels downward** — h1 → h2 → h3 is valid; h1 → h3 is not.

**Skipping upward is allowed** — returning from h3 → h2 or h3 → h1 is valid (starting a new section).

**Headings must describe their section** — avoid generic headings like "Content", "Section 1". (WCAG 2.4.6)

**Don't use headings for visual size** — if you want large bold text that isn't a structural heading, use a paragraph with a styling class, not a heading element.

## Correct Heading Structure

```
h1 — Page title
  h2 — Major section
    h3 — Subsection
    h3 — Subsection
  h2 — Major section
    h3 — Subsection
      h4 — Sub-subsection
```

## Cross-Component Heading Violations

Heading violations are often in **deeply nested components** (cards, tables, accordions) — not in the page layout itself. Auditors must grep ALL heading elements (`<h1>`–`<h6>`) across the ENTIRE codebase, not just pages/layouts.

### Fixed heading levels in reusable components

A component that always renders a fixed heading level (e.g., always `<h4>`) creates violations depending on where it's used:

```tsx
// DANGEROUS — always renders <h3> regardless of context
function ProductCard({ title }) {
  return <h3>{title}</h3>;
}
```

If `ProductCard` is used inside a section that already has an `<h3>`, the hierarchy breaks. Mark as **RUNTIME_REQUIRED** — compliance depends on usage context.

### Headings inside `<summary>` elements (trap)

Headings inside `<summary>` elements are **hidden from screen-reader heading lists** and heading-navigation shortcuts entirely. Users navigating by headings will never find them.

```html
<!-- VIOLATION — heading invisible to heading navigation -->
<details>
  <summary><h3>Section Title</h3></summary>
  <p>Content revealed when opened</p>
</details>
```

Headings inside `<details>` content (not `<summary>`) are only reachable via heading navigation when the disclosure is open. Flag both patterns as violations requiring restructuring:

- Heading inside `<summary>` → move heading outside or remove heading role
- Important heading inside closed `<details>` → consider whether content should be visible by default

## Landmarks and Headings Together

Headings work in concert with landmark regions. Each landmark (`main`, `nav`, `aside`, etc.) should contain its own heading where appropriate. Screen reader users navigate by landmarks first, then headings within.

## Platform Implementation

See your platform skill for implementation details:
- **Web**: HTML `<h1>`–`<h6>` — `../../references/references/semantic.md`
- **iOS**: `../../references/references/headings.md` — `.accessibilityAddTraits(.isHeader)` + `.accessibilityHeading(.h2)`
- **Android**: `../../references/references/accessibility-roles.md` — `ViewCompat` heading role via `AccessibilityNodeInfo`

## Resources

- WCAG 1.3.1 Info and Relationships: <https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships>
- WCAG 2.4.6 Headings and Labels: <https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels>
- W3C Headings Tutorial: <https://www.w3.org/WAI/tutorials/page-structure/headings/>
