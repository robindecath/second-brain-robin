# Vitamin Play Accessibility Auto-Correction Rules

**Purpose**: Instruction tuning for automatic accessibility fixes using Vitamin Play components.

This file contains common accessibility violations and their correct implementations using Vitamin Play Design System.

> **Standards mapping**: Each rule references the relevant WCAG 2.2 success criteria. For RGAA, RAAM, and EN 301 549 equivalents, see `../standards/cross-references/WCAG_CROSS_REFERENCE.toon`.

---

## Rule 1: Use VpButton for Interactive Elements

> **WCAG**: [2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) (A), [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A) | **RGAA**: 7.1, 7.3 | **RAAM**: 5.1, 5.2

### ❌ Anti-pattern: Generic div/span with onClick

```tsx
// WRONG - No keyboard support, no role
<div onClick={handleClick}>Click me</div>
<span onClick={handleSubmit}>Submit</span>
```

### ✅ Correct Pattern

```tsx
import { VpButton } from "@vtmn-play/react";

// Correct - Full keyboard support, proper role
<VpButton onClick={handleClick}>Click me</VpButton>
<VpButton type="submit" onClick={handleSubmit}>Submit</VpButton>
```

```vue
<script setup>
import { VpButton } from "@vtmn-play/vue";
</script>

<template>
  <VpButton @click="handleClick">Click me</VpButton>
  <VpButton type="submit" @click="handleSubmit">Submit</VpButton>
</template>
```

```svelte
<script>
  import { VpButton } from "@vtmn-play/svelte";
</script>

<VpButton on:click={handleClick}>Click me</VpButton>
<VpButton type="submit" on:click={handleSubmit}>Submit</VpButton>
```

**Auto-fix**: Replace any `<div onClick>` or `<span onClick>` with `<VpButton>`.

---

## Rule 2: Use VpIconButton for Icon-Only Actions

> **WCAG**: [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A), [1.1.1 Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) (A) | **RGAA**: 7.1, 1.1 | **RAAM**: 5.1, 5.5, 1.2

### ❌ Anti-pattern: Button without text label

```tsx
// WRONG - No accessible name
<button onClick={handleClose}>
  <CloseIcon />
</button>

<VpButton onClick={handleFavorite}>
  <HeartIcon />
</VpButton>
```

### ✅ Correct Pattern

```tsx
import { VpIconButton } from "@vtmn-play/react";
import { VpCloseIcon, VpHeartIcon } from "@vtmn-play/icons/react";

// Correct - aria-label provides accessible name
<VpIconButton aria-label="Close dialog" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>

<VpIconButton aria-label="Add to favorites" onClick={handleFavorite}>
  <VpHeartIcon />
</VpIconButton>
```

```vue
<script setup>
import { VpIconButton } from "@vtmn-play/vue";
import { VpCloseIcon, VpHeartIcon } from "@vtmn-play/icons/vue";
</script>

<template>
  <VpIconButton aria-label="Close dialog" @click="handleClose">
    <VpCloseIcon />
  </VpIconButton>

  <VpIconButton aria-label="Add to favorites" @click="handleFavorite">
    <VpHeartIcon />
  </VpIconButton>
</template>
```

```svelte
<script>
  import { VpIconButton } from "@vtmn-play/svelte";
  import { VpCloseIcon, VpHeartIcon } from "@vtmn-play/icons/svelte";
</script>

<VpIconButton aria-label="Close dialog" on:click={handleClose}>
  <VpCloseIcon />
</VpIconButton>

<VpIconButton aria-label="Add to favorites" on:click={handleFavorite}>
  <VpHeartIcon />
</VpIconButton>
```

**Auto-fix**: Replace icon-only buttons with `<VpIconButton aria-label="...">`.

---

## Rule 3: Always Label Form Inputs

> **WCAG**: [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (A), [3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) (A), [2.5.3 Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) (A) | **RGAA**: 11.1, 11.2 | **RAAM**: 9.1, 9.2

### ❌ Anti-pattern: Input without label

```tsx
// WRONG - No programmatic label
<input type="email" placeholder="Email address" />

// WRONG - Placeholder is not a label
<VpInput placeholder="Enter your email" />
```

### ✅ Correct Pattern

```tsx
import { VpFormControl, VpFormLabel, VpInput } from "@vtmn-play/react";

// Correct - VpFormControl links label and input
<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
</VpFormControl>;
```

```vue
<script setup>
import { VpFormControl, VpFormLabel, VpInput } from "@vtmn-play/vue";
</script>

<template>
  <VpFormControl>
    <VpFormLabel>Email address</VpFormLabel>
    <VpInput type="email" name="email" />
  </VpFormControl>
</template>
```

```svelte
<script>
  import { VpFormControl, VpFormLabel, VpInput } from "@vtmn-play/svelte";
</script>

<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
</VpFormControl>
```

**Auto-fix**: Wrap inputs in `VpFormControl` with `VpFormLabel`.

---

## Rule 4: Use Semantic Color Tokens

> **WCAG**: [1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) (AA), [1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) (AA) | **RGAA**: 3.2, 3.3 | **RAAM**: 2.2, 2.3

### ❌ Anti-pattern: Hardcoded hex colors

```tsx
// WRONG - Hardcoded colors, no theme support
<div style={{ color: '#dc2626' }}>Error message</div>
<button style={{ backgroundColor: '#3b82f6' }}>Submit</button>
```

### ✅ Correct Pattern

```tsx
// Correct - Semantic tokens with theme support
<div style={{ color: 'var(--vp-semantic-color-content-negative)' }}>
  Error message
</div>

<VpButton variant="primary">Submit</VpButton>
// VpButton uses tokens internally
```

**Common Semantic Tokens:**

- `--vp-semantic-color-content-primary` - Primary text
- `--vp-semantic-color-content-negative` - Error text
- `--vp-semantic-color-content-positive` - Success text
- `--vp-semantic-color-background-primary` - Primary background
- `--vp-semantic-color-border-primary` - Primary border

**Auto-fix**: Replace hex colors with semantic token CSS variables.

---

## Rule 5: Provide Alt Text for Images

> **WCAG**: [1.1.1 Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) (A) | **RGAA**: 1.1, 1.2, 1.3 | **RAAM**: 1.1, 1.2, 1.3

### ❌ Anti-pattern: Image without alt attribute

```tsx
// WRONG - No alt text
<img src="/product.jpg" />

// WRONG - Generic alt text
<img src="/product.jpg" alt="image" />
```

### ✅ Correct Pattern

```tsx
// Correct - Descriptive alt text
<img src="/product.jpg" alt="Mountain bike with 21 gears" />

// Correct - Decorative image
<img src="/decorative.svg" alt="" role="presentation" />
```

**Auto-fix**: Add descriptive `alt` attribute based on image filename/context.

---

## Rule 6: Use VpCheckbox for Checkboxes

> **WCAG**: [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A), [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (A) | **RGAA**: 11.1, 7.1 | **RAAM**: 9.1, 5.1

### ❌ Anti-pattern: Native checkbox without proper labeling

```tsx
// WRONG - Checkbox without label
<input type="checkbox" />

// WRONG - Label not properly associated
<label>Accept terms</label>
<input type="checkbox" name="terms" />
```

### ✅ Correct Pattern

```tsx
import { VpCheckbox } from "@vtmn-play/react";

// Correct - Built-in label association
<VpCheckbox name="terms" value="accepted">
  I accept the terms and conditions
</VpCheckbox>

// With required state
<VpCheckbox name="terms" required>
  I accept the terms and conditions
</VpCheckbox>
```

**Auto-fix**: Replace native checkboxes with `VpCheckbox` component.

---

## Rule 7: Show Error Messages Accessibly

> **WCAG**: [3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) (A), [3.3.3 Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html) (AA), [4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) (AA) | **RGAA**: 11.10, 11.11, 7.5 | **RAAM**: 9.8, 9.9, 5.4

### ❌ Anti-pattern: Visual-only error indication

```tsx
// WRONG - Color only, no text
<input style={{ borderColor: 'red' }} />

// WRONG - Error message not linked to input
<input name="email" />
<div className="error">Invalid email</div>
```

### ✅ Correct Pattern

```tsx
import {
  VpFormControl,
  VpFormLabel,
  VpInput,
  VpFormError,
} from "@vtmn-play/react";

// Correct - Error linked via aria-describedby
<VpFormControl isInvalid>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" value={email} />
  <VpFormError>Please enter a valid email address</VpFormError>
</VpFormControl>;
// VpFormControl automatically adds aria-invalid and aria-describedby
```

**Auto-fix**: Wrap form fields with errors in `VpFormControl` with `isInvalid` prop and `VpFormError`.

---

## Rule 8: Ensure Focus Visibility

> **WCAG**: [2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) (AA) | **RGAA**: 10.7 | **RAAM**: 8.3

### ❌ Anti-pattern: Removing focus outline

```css
/* WRONG - Removes all focus indicators */
*:focus {
  outline: none;
}

button:focus {
  outline: none;
}
```

### ✅ Correct Pattern

```css
/* Correct - Custom focus indicator with :focus-visible */
*:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}

/* VpButton already includes accessible focus styles */
```

**Auto-fix**: Remove `outline: none` or replace with `:focus-visible` pattern using Vitamin Play tokens.

---

## Rule 9: Use VpModal for Dialogs

> **WCAG**: [2.4.3 Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) (A), [2.1.2 No Keyboard Trap](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html) (A) | **RGAA**: 12.8, 12.9 | **RAAM**: 10.1, 10.3

### ❌ Anti-pattern: Custom modal without focus management

```tsx
// WRONG - No focus trap, no aria attributes
{
  isOpen && (
    <div className="modal">
      <div className="modal-content">
        <h2>Confirm</h2>
        <button onClick={handleClose}>Close</button>
      </div>
    </div>
  );
}
```

### ✅ Correct Pattern

```tsx
import {
  VpModal,
  VpModalDialog,
  VpModalHeader,
  VpModalCloseButton,
  VpModalBody,
  VpButton,
} from "@vtmn-play/react";

// Correct - Focus trap, ARIA, keyboard handling built-in
<VpModal open={isOpen} onClose={handleClose}>
  <VpModalDialog aria-label="Confirmation dialog">
    <VpModalHeader>
      <h2>Confirm</h2>
      <VpModalCloseButton aria-label="Close dialog" />
    </VpModalHeader>
    <VpModalBody>
      <p>Are you sure?</p>
      <VpButton onClick={handleConfirm}>Confirm</VpButton>
    </VpModalBody>
  </VpModalDialog>
</VpModal>;
```

```vue
<script setup>
import {
  VpModal,
  VpModalDialog,
  VpModalHeader,
  VpModalCloseButton,
  VpModalBody,
  VpButton,
} from "@vtmn-play/vue";
</script>

<template>
  <VpModal :open="isOpen" @close="handleClose">
    <VpModalDialog aria-label="Confirmation dialog">
      <VpModalHeader>
        <h2>Confirm</h2>
        <VpModalCloseButton aria-label="Close dialog" />
      </VpModalHeader>
      <VpModalBody>
        <p>Are you sure?</p>
        <VpButton @click="handleConfirm">Confirm</VpButton>
      </VpModalBody>
    </VpModalDialog>
  </VpModal>
</template>
```

```svelte
<script>
  import {
    VpModal,
    VpModalDialog,
    VpModalHeader,
    VpModalCloseButton,
    VpModalBody,
    VpButton,
  } from "@vtmn-play/svelte";
</script>

<VpModal open={isOpen} on:close={handleClose}>
  <VpModalDialog aria-label="Confirmation dialog">
    <VpModalHeader>
      <h2>Confirm</h2>
      <VpModalCloseButton aria-label="Close dialog" />
    </VpModalHeader>
    <VpModalBody>
      <p>Are you sure?</p>
      <VpButton on:click={handleConfirm}>Confirm</VpButton>
    </VpModalBody>
  </VpModalDialog>
</VpModal>
```

**Auto-fix**: Replace custom modals with `VpModal` component.

---

## Rule 10: Proper Heading Hierarchy

> **WCAG**: [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (A), [2.4.6 Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html) (AA) | **RGAA**: 9.1 | **RAAM**: 7.1

### ❌ Anti-pattern: Skipping heading levels

```tsx
// WRONG - Skips from h1 to h3
<h1>Page Title</h1>
<h3>Section Title</h3>

// WRONG - Using headings for styling only
<h2 className="small-text">Not actually a heading</h2>
```

### ✅ Correct Pattern

```tsx
// Correct - Sequential heading levels
<h1>Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>

// Correct - Use CSS for styling, not heading level
<h2 className="h3-size">Properly leveled heading styled smaller</h2>
```

**Auto-fix**: Verify heading hierarchy is sequential (h1 → h2 → h3, etc.).

---

## Rule 11: Loading States Must Be Announced

> **WCAG**: [4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) (AA) | **RGAA**: 7.5 | **RAAM**: 5.4

### ❌ Anti-pattern: Visual-only loading indicator

```tsx
// WRONG - Spinner visible only, no screen reader announcement
{
  isLoading && <div className="spinner" />;
}
```

### ✅ Correct Pattern

```tsx
// Correct - ARIA live region announces loading state
{
  isLoading && (
    <div role="status" aria-live="polite" aria-label="Loading">
      <div className="spinner" aria-hidden="true" />
      <span className="sr-only">Loading content...</span>
    </div>
  );
}

// Better - Use VpSpinner (if available in Vitamin Play)
{
  isLoading && <VpSpinner aria-label="Loading content" />;
}
```

**Auto-fix**: Add `role="status"` and screen reader text to loading indicators.

---

## Rule 12: Link Text Must Be Descriptive

> **WCAG**: [2.4.4 Link Purpose (In Context)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html) (A) | **RGAA**: 6.1 | **RAAM**: —

### ❌ Anti-pattern: Generic link text

```tsx
// WRONG - "Click here" doesn't describe destination
<a href="/products">Click here</a>
<a href="/article/123">Read more</a>
```

### ✅ Correct Pattern

```tsx
// Correct - Link text describes destination
<VpButton href="/products">View all products</VpButton>
<VpButton href="/article/123">Read more about mountain biking</VpButton>

// Correct - Additional context via aria-label
<VpButton href="/article/123" aria-label="Read more about mountain biking">
  Read more
</VpButton>
```

**Auto-fix**: Replace generic link text with descriptive alternatives.

---

## Rule 13: Provide Skip Links and Real Link Targets

> **WCAG**: [2.4.1 Bypass Blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html) (A), [2.4.4 Link Purpose](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html) (A)

### ❌ Anti-pattern

```tsx
<a href="#">Continue</a>
```

### ✅ Correct Pattern

```tsx
<a href="#main-content" className="skip-link">Skip to main content</a>
<main id="main-content" tabIndex={-1}>...</main>
```

**Auto-fix**: Replace fake links (`href="#"`) with real destinations/actions and add skip links on multi-region pages.

---

Search terms: Vp component migration, migrate raw input element to Vitamin Play VpInput component.

## Rule 14: Group Related Inputs with fieldset/legend

> **WCAG**: [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (A), [3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) (A)

### ❌ Anti-pattern

```tsx
<div>
  <VpCheckbox>Fiction</VpCheckbox>
  <VpCheckbox>Science</VpCheckbox>
</div>
```

### ✅ Correct Pattern

```tsx
<fieldset>
  <legend>Filter by genre</legend>
  <VpCheckbox>Fiction</VpCheckbox>
  <VpCheckbox>Science</VpCheckbox>
</fieldset>
```

**Auto-fix**: Wrap related controls (filters, payment options, address blocks) in `fieldset/legend`.

---

## Rule 15: Pagination Needs Current State and Clear Labels

> **WCAG**: [2.4.4 Link Purpose](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html) (A), [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A)

### ❌ Anti-pattern

```tsx
<button>1</button>
<button>2</button>
```

### ✅ Correct Pattern

```tsx
<button aria-label="Page 1">1</button>
<button aria-current="page" aria-label="Page 2, current page">2</button>
```

**Auto-fix**: Add `aria-current="page"` and explicit page labels.

---

## Rule 16: Stable Live Regions for Dynamic Updates

> **WCAG**: [4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) (AA)

### ❌ Anti-pattern

```tsx
{
  showMessage && <p>Code applied</p>;
}
```

### ✅ Correct Pattern

```tsx
<div aria-live="polite" role="status">{message}</div>
<div aria-live="assertive" role="alert">{error}</div>
```

**Auto-fix**: Keep live region mounted and update text content instead of mounting/unmounting message nodes late.

---

## Rule 17: Restore Focus After UI Mutations

> **WCAG**: [2.4.3 Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) (A), [2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) (AA)

### ❌ Anti-pattern

```tsx
removeItem(id); // focus lost after DOM update
```

### ✅ Correct Pattern

```tsx
removeItem(id);
requestAnimationFrame(() => nextFocusableRef.current?.focus());
```

**Auto-fix**: Move focus to logical next target after remove/filter/modal close.

---

## Rule 18: Forms Need Required + Autocomplete Semantics

> **WCAG**: [1.3.5 Identify Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html) (AA), [3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) (A)

### ❌ Anti-pattern

```tsx
<input type="email" />
<input type="tel" />
```

### ✅ Correct Pattern

```tsx
<input type="email" required autoComplete="email" />
<input type="tel" required autoComplete="tel" />
<input type="text" autoComplete="address-line1" />
```

**Auto-fix**: Add `required` and relevant `autocomplete` tokens for checkout/account forms.

---

## Rule 19: Prefer List Semantics for Repeated Item Collections

> **WCAG**: [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (A)

### ❌ Anti-pattern

```tsx
<div className="cart-items">
  <div className="cart-item">...</div>
</div>
```

### ✅ Correct Pattern

```tsx
<ul className="cart-items">
  <li className="cart-item">...</li>
</ul>
```

**Auto-fix**: Convert repeated collections to list semantics unless table semantics are more appropriate.

---

## Rule 20: Minimum Target Size for Critical Icon Actions

> **WCAG**: [2.5.5 Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size.html) (AAA, recommended), EN 301 549 ergonomics guidance

### ❌ Anti-pattern

```tsx
<VpIconButton style={{ width: 16, height: 16 }} />
```

### ✅ Correct Pattern

```tsx
<VpIconButton style={{ minWidth: 44, minHeight: 44 }} />
```

**Auto-fix**: Ensure icon-only controls expose at least a 44x44 hit area when feasible.

---

## Rule 21: `role="alert"` vs `role="status"` — Urgency Matters

> **WCAG**: [4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) (AA) | **RGAA**: 7.5 | **RAAM**: 5.6

### ❌ Anti-pattern: Using `role="alert"` for non-critical feedback

```tsx
// WRONG — interrupts the user for a non-critical update
<div role="alert">3 items added to cart</div>
<div role="alert">Changes saved</div>
```

### ✅ Correct Pattern

```tsx
// Use role="status" (polite) for non-critical feedback
<div role="status">3 items added to cart</div>
<div role="status">Changes saved</div>

// Use role="alert" (assertive) ONLY for critical errors
<div role="alert">Session expires in 30 seconds. Save your work.</div>
<div role="alert">Network connection lost. Changes may not be saved.</div>
```

**Auto-fix**: Replace `role="alert"` with `role="status"` unless the message is critical and time-sensitive.

---

## Rule 22: `role="button"` on Native `<input>` Elements

> **WCAG**: [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A) | **RGAA**: 7.1 | **RAAM**: 5.1

### ❌ Anti-pattern

```tsx
// WRONG — role="button" on input is always incorrect
<input type="submit" role="button" value="Send" />
<input type="reset" role="button" value="Clear" />
```

### ✅ Correct Pattern

```tsx
// Native inputs already have implicit roles — never override
<input type="submit" value="Send" />

// Or use VpButton for consistent styling
<VpButton type="submit">Send</VpButton>
```

**Auto-fix**: Remove `role="button"` from any `<input>` element.

---

## Rule 23: Missing `autocomplete` on Personal Data Inputs

> **WCAG**: [1.3.5 Identify Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html) (AA) | **RGAA**: 11.13 | **RAAM**: 11.4

### ❌ Anti-pattern: Personal data inputs without autocomplete

```tsx
// WRONG — no autocomplete on personal data fields
<input type="email" name="email" />
<input type="tel" name="phone" />
<input name="firstName" />
<input name="address" />
```

### ✅ Correct Pattern

```tsx
// Correct — autocomplete helps AT identify field purpose
<input type="email" name="email" autoComplete="email" />
<input type="tel" name="phone" autoComplete="tel" />
<input name="firstName" autoComplete="given-name" />
<input name="lastName" autoComplete="family-name" />
<input name="address" autoComplete="street-address" />
```

**Auto-fix**: Add appropriate `autocomplete` value to inputs collecting personal data.

---

## Rule 24: `aria-hidden="true"` on Elements with Click Handlers

> **WCAG**: [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A), [2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) (A) | **RGAA**: 10.8 | **RAAM**: 5.1

### ❌ Anti-pattern: Hidden from AT but still interactive

```tsx
// CRITICAL — hidden from screen readers but clickable = keyboard trap
<div aria-hidden="true" onClick={handleAction}>
  <Icon /> Action
</div>

<button aria-hidden="true" onClick={handleClose}>×</button>
```

### ✅ Correct Pattern

```tsx
// Either make it truly hidden (remove interactivity)
<div aria-hidden="true">
  <Icon /> {/* Decorative only, no click handler */}
</div>

// Or make it accessible (remove aria-hidden)
<VpIconButton aria-label="Close" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>
```

**Auto-fix**: Remove `aria-hidden="true"` from any element with `onClick`, or remove the click handler if the element should be truly hidden.

---

## Rule 25: `aria-label` on `<nav>` Must Not Contain "navigation"

> **WCAG**: [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A) | **RGAA**: 12.1 | **RAAM**: 9.1

### ❌ Anti-pattern: Role name repeated in label

```tsx
// WRONG — screen reader reads "Primary navigation navigation"
<nav aria-label="Primary navigation">...</nav>
<nav aria-label="Footer navigation">...</nav>
```

### ✅ Correct Pattern

```tsx
// Correct — only the distinguishing word, role is announced automatically
<nav aria-label="Primary">...</nav>
<nav aria-label="Footer">...</nav>
<nav aria-label="Breadcrumb">...</nav>
```

**Auto-fix**: Remove the word "navigation" from `aria-label` on `<nav>` elements.

---

## Rule 26: `<summary>` Must Not Contain Heading Elements

> **WCAG**: [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (A), [2.4.6 Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html) (AA) | **RGAA**: 9.1 | **RAAM**: 9.2

### ❌ Anti-pattern: Headings inside summary (invisible to heading navigation)

```tsx
// WRONG — heading is hidden from screen reader heading lists
<details>
  <summary><h3>Shipping Information</h3></summary>
  <p>Ships within 3-5 business days...</p>
</details>
```

### ✅ Correct Pattern

```tsx
// Option 1: Heading before the disclosure
<h3>Shipping Information</h3>
<details>
  <summary>View details</summary>
  <p>Ships within 3-5 business days...</p>
</details>

// Option 2: No heading inside summary (summary IS the heading-like element)
<details>
  <summary>Shipping Information</summary>
  <p>Ships within 3-5 business days...</p>
</details>
```

**Auto-fix**: Move headings outside `<summary>` or remove the heading element and let `<summary>` serve as the label.

---

## Rule 27: `disabled` on `<button>` in Toolbar — Consider `aria-disabled`

> **WCAG**: [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) (A) | **RGAA**: 7.1 | **RAAM**: 5.1

### ❌ Anti-pattern: Disabled toolbar button removed from focus order

```tsx
// WRONG — keyboard user can't discover this button exists
<div role="toolbar" aria-label="Text formatting">
  <button disabled onClick={handleBold}>Bold</button>
  <button onClick={handleItalic}>Italic</button>
</div>
```

### ✅ Correct Pattern

```tsx
// Correct — button remains focusable and discoverable
<div role="toolbar" aria-label="Text formatting">
  <button
    aria-disabled="true"
    onClick={(e) => { if (true /* disabled condition */) e.preventDefault(); }}
  >
    Bold
  </button>
  <button onClick={handleItalic}>Italic</button>
</div>
```

**Auto-fix**: Replace `disabled` with `aria-disabled="true"` + click prevention on buttons inside toolbars, action bars, or navigation elements.

---

## Summary: Quick Reference Table

| Violation        | Correct Pattern                     | Component     | WCAG Criteria |
| ---------------- | ----------------------------------- | ------------- | ------------- |
| `<div onClick>`  | `<VpButton>`                        | VpButton      | 2.1.1, 4.1.2  |
| Icon-only button | `<VpIconButton aria-label="...">`   | VpIconButton  | 4.1.2, 1.1.1  |
| Unlabeled input  | `<VpFormControl>` + `<VpFormLabel>` | VpFormControl | 1.3.1, 3.3.2  |
| Hex colors       | `var(--vp-semantic-color-*)`        | Design Tokens | 1.4.3, 1.4.11 |
| Missing alt text | `alt="descriptive text"`            | Native HTML   | 1.1.1         |
| Native checkbox  | `<VpCheckbox>`                      | VpCheckbox    | 4.1.2, 1.3.1  |
| Error message    | `<VpFormError>` in `VpFormControl`  | VpFormControl | 3.3.1, 3.3.3  |
| `outline: none`  | `:focus-visible` with tokens        | CSS           | 2.4.7         |
| Custom modal     | `<VpModal>`                         | VpModal       | 2.4.3, 2.1.2  |
| Heading skip     | Sequential h1→h2→h3                 | Native HTML   | 1.3.1, 2.4.6  |
| Loading spinner  | `role="status"` + sr-only text      | ARIA          | 4.1.3         |
| Generic link     | Descriptive link text               | VpButton      | 2.4.4         |
| `role="alert"` overuse | `role="status"` for non-critical | ARIA       | 4.1.3         |
| Missing autocomplete | `autoComplete="email"` etc.      | Native HTML   | 1.3.5         |
| `aria-hidden` + onClick | Remove one or the other        | ARIA          | 4.1.2, 2.1.1  |
| "navigation" in nav label | Remove role word from label  | ARIA          | 4.1.2         |
| Heading in `<summary>` | Move heading outside           | Native HTML   | 1.3.1, 2.4.6  |
| `disabled` in toolbar | `aria-disabled="true"`          | ARIA          | 4.1.2         |

---

## Auto-Fix Priority

1. **Critical** (breaks keyboard navigation): Rules 1, 2, 9
2. **High** (fails screen readers): Rules 3, 5, 7, 10, 11, 12
3. **Medium** (improves UX): Rules 6, 8
4. **Themeable** (design system consistency): Rules 4

Apply fixes in priority order when multiple violations exist.
