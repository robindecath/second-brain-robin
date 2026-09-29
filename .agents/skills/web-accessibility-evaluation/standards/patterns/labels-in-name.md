# Labels in Name

## Overview

When an interactive element has a visible text label, the element's **accessible name** must contain that visible text. This allows speech input users (Voice Control, Voice Access) to activate controls by speaking the text they see on screen. (WCAG 2.5.3 AA)

## The Problem

A button visually reads "Submit Order" but its `aria-label` is set to "submit". A Voice Control user says "Submit Order" and nothing happens — the spoken phrase doesn't match the accessible name.

## Rule

The **accessible name must include the visible label text** (case-insensitive). The accessible name can be longer, but the visible text must be present as a substring.

| Visible text | Accessible name | Valid? |
|---|---|---|
| "Delete" | "Delete" | ✅ |
| "Delete" | "Delete item from cart" | ✅ (contains "Delete") |
| "Delete" | "Remove" | ❌ (doesn't contain "Delete") |
| "Submit Order" | "submit" | ❌ (missing "Order") |
| "X" | "Close dialog" | ✅ (icon-only — no visible text to match) |

## When This Does NOT Apply

- Icon-only controls with no visible text label (only an icon)
- Controls where the visible label is purely decorative or symbolic
- Images used as controls where the alt text serves as the label

## Common Violations

**`aria-label` that replaces instead of extending visible text:**
```html
<!-- ❌ aria-label replaces "Edit", breaking voice input -->
<button aria-label="Edit profile settings">Edit</button>

<!-- ✅ aria-label contains "Edit" -->
<button aria-label="Edit profile settings">Edit</button>
<!-- Actually fine! "Edit" is a substring of "Edit profile settings" -->

<!-- ❌ completely different label -->
<button aria-label="Modify">Edit</button>
```

**Screen reader text that prepends to visible label:** If you visually display "Delete" but add hidden text before it making the accessible name "Remove item: Delete" — the word "Delete" is present, so this passes.

## Platform Implementation

See your platform skill for implementation details:
- **Web**: Ensure `aria-label`, `aria-labelledby`, or `<label>` values contain the visible button/link text
- **iOS**: `../../references/references/accessibility-input-labels.md` — `.accessibilityInputLabels()` must include the visual label
- **Android**: `contentDescription` must include visible text for Voice Access compatibility

## Resources

- WCAG 2.5.3 Label in Name: <https://www.w3.org/WAI/WCAG22/Understanding/label-in-name>
- Technique F96: <https://www.w3.org/WAI/WCAG22/Techniques/failures/F96>
