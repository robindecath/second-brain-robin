# Interactive SVG Accessibility Patterns

## Overview

SVGs used as interactive elements (buttons, links, toggles) require the same keyboard accessibility as any other interactive element. The most common violation is an SVG with `role="button"` and `tabIndex` but no keyboard event handler — creating a **keyboard trap** where the element is focusable but not activatable.

**WCAG criteria**: 2.1.1 (Keyboard), 4.1.2 (Name, Role, Value)

---

## Rules

### Rule 1: SVG with `role="button"` + `tabIndex` MUST have `onKeyDown`

```tsx
// ❌ CRITICAL — focusable but no keyboard activation
<svg
  role="button"
  tabIndex={0}
  onClick={handleAction}
  aria-label="Add to favorites"
>
  <path d="..." />
</svg>

// ✅ CORRECT — keyboard handler matches button behavior
<svg
  role="button"
  tabIndex={0}
  onClick={handleAction}
  onKeyDown={(e) => {
    if (e.key === 'Enter') handleAction(e);
  }}
  onKeyUp={(e) => {
    if (e.key === ' ') {
      e.preventDefault();
      handleAction(e);
    }
  }}
  aria-label="Add to favorites"
>
  <path d="..." />
</svg>
```

### Rule 2: Prefer wrapping in `<button>` over role="button" on SVG

```tsx
// ✅ BEST — native button with SVG inside
<button onClick={handleAction} aria-label="Add to favorites">
  <svg aria-hidden="true">
    <path d="..." />
  </svg>
</button>

// ✅ BEST (with Design System) — IconButton wraps the icon
<VpIconButton aria-label="Add to favorites" onClick={handleAction}>
  <HeartIcon />
</VpIconButton>
```

### Rule 3: Enter fires on `keydown`, Space fires on `keyup`

Native `<button>` behavior:
- **Enter**: fires on `keydown` (immediate)
- **Space**: fires on `keyup` (prevents scroll, allows cancel by moving off)

Custom interactive elements MUST match this behavior:

```tsx
onKeyDown={(e) => {
  if (e.key === 'Enter') handleAction(e);
  if (e.key === ' ') e.preventDefault(); // Prevent page scroll
}}
onKeyUp={(e) => {
  if (e.key === ' ') handleAction(e);
}}
```

### Rule 4: SVG tooltip triggers via Radix/HeadlessUI `asChild`

When SVG is used as a tooltip trigger with `asChild` composition pattern, verify the trigger element has proper keyboard support:

```tsx
// ❌ WRONG — Trigger renders as SVG without keyboard handler
<Tooltip.Trigger asChild>
  <svg tabIndex={0} aria-label="Info">...</svg>
</Tooltip.Trigger>

// ✅ CORRECT — Trigger wraps in a proper button
<Tooltip.Trigger asChild>
  <button aria-label="More information">
    <svg aria-hidden="true">...</svg>
  </button>
</Tooltip.Trigger>
```

### Rule 5: Decorative SVGs inside buttons must be hidden

```tsx
// ✅ CORRECT — SVG is decorative, button has its own label
<button aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false">
    <path d="..." />
  </svg>
</button>
```

Note: `focusable="false"` prevents SVG from receiving focus in IE/older Edge (legacy support).

---

## Detection Patterns

```bash
# SVG with role="button" — verify onKeyDown/onKeyUp exists
grep -r "role=\"button\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte"

# SVG with tabIndex or onClick — flag if no keyboard handler
grep -r "<svg.*onClick\|<svg.*tabIndex" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte"

# Radix/HeadlessUI asChild with SVG triggers
grep -r "Trigger.*asChild\|asChild.*Trigger" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte"
```

---

## Severity Classification

| Pattern | Severity | Reason |
| ------- | -------- | ------ |
| SVG `role="button"` + `tabIndex` + no `onKeyDown` | **CRITICAL** | Keyboard trap — focusable but not activatable |
| SVG with `onClick` + no `tabIndex` + no keyboard | **HIGH** | Not reachable by keyboard at all |
| SVG trigger via `asChild` without button wrapper | **HIGH** | Tooltip inaccessible by keyboard |
| SVG inside button without `aria-hidden` | **MEDIUM** | May duplicate accessibility tree information |

---

## Resources

- WCAG 2.1.1 Keyboard: <https://www.w3.org/WAI/WCAG22/Understanding/keyboard>
- WCAG 4.1.2 Name, Role, Value: <https://www.w3.org/WAI/WCAG22/Understanding/name-role-value>
- ARIA Button Pattern: <https://www.w3.org/WAI/ARIA/apg/patterns/button/>
