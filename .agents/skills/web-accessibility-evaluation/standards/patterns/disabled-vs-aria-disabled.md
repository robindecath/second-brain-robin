# disabled vs aria-disabled

## Overview

The HTML `disabled` attribute and `aria-disabled="true"` have fundamentally different behaviors. Choosing the wrong one creates keyboard accessibility issues or confusing user experiences.

**WCAG criteria**: 4.1.2 (Name, Role, Value)

---

## The Difference

| Attribute | Focus | Clickable | AT announcement | Form submission |
| --------- | ----- | --------- | --------------- | --------------- |
| `disabled` | Removed from tab order | No | "dimmed" / "unavailable" | Value excluded |
| `aria-disabled="true"` | Remains focusable | Yes (must prevent in JS) | "dimmed" / "unavailable" | Value included |

---

## When to Use Each

### Use `disabled` (HTML attribute)

Appropriate for form elements where skipping is acceptable:

- `<input>`, `<textarea>`, `<select>` in forms when the field is irrelevant
- Submit buttons before form validation passes
- Elements the user does not need to discover or understand

```html
<!-- User doesn't need to interact with this field -->
<input type="text" disabled value="Calculated automatically" />
```

### Use `aria-disabled="true"`

Appropriate when the user should **discover** the element and understand it's unavailable:

- Toolbar buttons that are contextually unavailable
- Navigation links to the current page
- Actions that require a prerequisite (e.g., "Delete" before selecting items)
- Any element where the user benefits from knowing it exists but can't use it yet

```tsx
// User can Tab to this, learn it exists, and understand why it's disabled
<button
  aria-disabled="true"
  onClick={(e) => {
    e.preventDefault();
    // Optionally show tooltip explaining why it's disabled
  }}
>
  Delete selected items
</button>
```

---

## Detection Rules

| Pattern | Flag as | Rationale |
| ------- | ------- | --------- |
| `disabled` on `<button>` inside a toolbar or action bar | REVIEW_NEEDED | Should often be `aria-disabled` to keep discoverable |
| `disabled` on navigation `<a>` or `<Link>` | REVIEW_NEEDED | Links should remain focusable for context |
| `aria-disabled="true"` without preventing the click action | FAIL | Must prevent activation in JavaScript |
| `disabled` on `<input>` in a standard form | PASS | Correct usage for irrelevant fields |

---

## Implementation Pattern

```tsx
// Correct aria-disabled pattern
function ToolbarButton({ disabled, onClick, children }) {
  return (
    <button
      aria-disabled={disabled}
      onClick={(e) => {
        if (disabled) {
          e.preventDefault();
          return;
        }
        onClick(e);
      }}
    >
      {children}
    </button>
  );
}
```

---

## Platform Implementation

- **Web**: `disabled` attribute vs `aria-disabled="true"` + JS prevention
- **iOS**: `.disabled(true)` vs `.accessibilityHint("Unavailable until...")` — use hint to explain why unavailable rather than removing from VoiceOver
- **Android**: `isEnabled = false` vs `stateDescription` + click interception — use `importantForAccessibility` to keep element discoverable

---

## Resources

- WCAG 4.1.2 Name, Role, Value: <https://www.w3.org/WAI/WCAG22/Understanding/name-role-value>
- ARIA `aria-disabled`: <https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/#describing_with_aria-disabled>
