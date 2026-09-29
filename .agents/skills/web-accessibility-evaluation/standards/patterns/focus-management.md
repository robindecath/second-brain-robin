# Focus Management

## Overview

Focus management ensures keyboard and assistive technology users can navigate interfaces predictably. It covers three concerns: visible focus indicators, logical focus order, and programmatic focus control for dynamic content.

## Focus Visibility (WCAG 2.4.7 / 2.4.11)

Every interactive element must have a **visible focus indicator** when focused via keyboard:
- Minimum contrast ratio: **3:1** between focused and unfocused states (WCAG 2.4.11 AA)
- Must not be removed with `outline: none` / `:focus { outline: 0 }` without a custom replacement
- The indicator must have sufficient size (WCAG 2.4.11 recommends ≥2px perimeter)

## Focus Order (WCAG 2.4.3)

Tab order must follow a **logical sequence** consistent with the visual layout and meaning:
- Left-to-right, top-to-bottom for Western languages
- Never trap focus unintentionally (WCAG 2.2.2) — users must always be able to move focus away
- `tabindex > 0` is almost always wrong — rely on DOM/view order instead

## Focus Trap (intentional)

Modals, dialogs, and sheets must **trap focus** while open:
1. On open: move focus to first interactive element inside (or the dialog container)
2. While open: Tab/Shift+Tab cycle within the modal, Escape closes it
3. On close: return focus to the **trigger element** that opened the modal

## Programmatic Focus for Dynamic Content

When content updates (navigation, errors, new panels), move focus explicitly:
- After SPA navigation → move to main heading or skip link
- After form submission with errors → move to error summary
- After dialog open → move to dialog content
- After dialog close → return to trigger

## Platform Implementation

See your platform skill for implementation details:
- **Web**: `../../references/references/navigation-and-focus.md` — `tabindex`, `:focus-visible`, `focus()`
- **iOS**: `../../references/references/focus-management.md` — `@AccessibilityFocusState`
- **Android**: `../../references/references/focus-management.md` — `ACTION_ACCESSIBILITY_FOCUS`, `FocusRequester`

## Resources

- WCAG 2.2.2 No Keyboard Trap: <https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap>
- WCAG 2.4.3 Focus Order: <https://www.w3.org/WAI/WCAG22/Understanding/focus-order>
- WCAG 2.4.7 Focus Visible: <https://www.w3.org/WAI/WCAG22/Understanding/focus-visible>
- WCAG 2.4.11 Focus Appearance: <https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance>
