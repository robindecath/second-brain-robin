# Accessible Form Errors — `:user-invalid` + `aria-invalid` Synchronization

## Overview

Standard HTML5 validation can trigger `aria-invalid` state before user interaction, causing screen readers to announce "Invalid entry" when the user merely focuses an empty required field. The correct pattern synchronizes visual and ARIA state only after meaningful interaction.

**WCAG criteria**: 3.3.1 (Error Identification), 3.3.3 (Error Suggestion)

---

## The Problem

```html
<!-- Browser adds :invalid pseudo-class immediately on page load -->
<input type="email" required />
```

If CSS styles `:invalid` with a red border and JavaScript sets `aria-invalid="true"` eagerly, users are "yelled at" before they've even attempted to fill the field.

---

## The Correct Pattern

### Three-Layer Approach

1. **Visual layer**: CSS `:user-invalid` for borders/icons (fires only after user interaction)
2. **Accessibility layer**: `aria-invalid="true"` + `aria-errormessage` to communicate state to AT
3. **Bridge**: JavaScript checking `element.matches(':user-invalid')` on `blur`/`input` events, then setting `aria-invalid` accordingly — not before

### Implementation

```css
/* Visual error — only after user has interacted */
input:user-invalid {
  border-color: var(--color-border-negative);
  outline-color: var(--color-border-negative);
}

/* Fallback for browsers without :user-invalid */
input[aria-invalid="true"] {
  border-color: var(--color-border-negative);
}
```

```tsx
function ValidatedInput({ name, type, required, errorMessage }) {
  const [invalid, setInvalid] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleBlur = () => {
    if (inputRef.current) {
      // Only set aria-invalid AFTER user interaction
      setInvalid(inputRef.current.matches(':user-invalid'));
    }
  };

  const handleInput = () => {
    if (invalid && inputRef.current) {
      // Clear error as soon as input becomes valid
      setInvalid(!inputRef.current.validity.valid ? true : false);
    }
  };

  return (
    <div>
      <input
        ref={inputRef}
        name={name}
        type={type}
        required={required}
        aria-invalid={invalid || undefined}
        aria-errormessage={invalid ? `${name}-error` : undefined}
        onBlur={handleBlur}
        onInput={handleInput}
      />
      {invalid && (
        <span id={`${name}-error`} role="alert">
          {errorMessage}
        </span>
      )}
    </div>
  );
}
```

---

## Detection Patterns

| Pattern | Flag as | Rationale |
| ------- | ------- | --------- |
| `<input required>` without any `aria-invalid` management strategy | REVIEW_NEEDED | Risk of premature error announcement |
| `aria-invalid="true"` set on render/mount without user interaction | FAIL | Announces error before user attempts input |
| `aria-invalid` toggled only on form submit | REVIEW_NEEDED | Late feedback — consider per-field on blur |
| `:invalid` CSS styling without `:user-invalid` fallback | REVIEW_NEEDED | Visual error shown before interaction |
| `aria-errormessage` pointing to non-existent ID | FAIL | Broken reference |
| Error message without `id` matching `aria-errormessage` | FAIL | AT cannot find error text |

---

## Key Rules

1. **Never** set `aria-invalid="true"` on initial render for empty required fields
2. **Always** pair `aria-invalid="true"` with `aria-errormessage` pointing to the error text
3. **Clear** `aria-invalid` as soon as the field becomes valid (don't wait for re-submit)
4. **Use** `role="alert"` or `aria-live="polite"` on error messages so they're announced when they appear
5. **Prefer** per-field validation on `blur` over form-level validation on submit for immediate feedback

---

## Browser Support

`:user-invalid` is supported in Firefox 88+, Chrome 119+, Safari 16.5+. For older browsers, fall back to tracking "has been blurred" state in JavaScript and applying a `.user-touched` class.

---

## Resources

- WCAG 3.3.1 Error Identification: <https://www.w3.org/WAI/WCAG22/Understanding/error-identification>
- MDN :user-invalid: <https://developer.mozilla.org/en-US/docs/Web/CSS/:user-invalid>
- ARIA aria-errormessage: <https://www.w3.org/TR/wai-aria-1.2/#aria-errormessage>
