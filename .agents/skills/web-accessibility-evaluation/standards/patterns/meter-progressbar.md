# Meter & Progressbar Accessible Names

## Overview

Elements with `role="meter"` or `role="progressbar"` MUST have an accessible name. Without one, screen readers announce the value (e.g., "3 out of 5") but not what the value represents, leaving users unable to understand the context.

**WCAG criteria**: 1.1.1 (Non-text Content), 4.1.2 (Name, Role, Value)

---

## Rules

### Every meter/progressbar must have an accessible name

```html
<!-- WRONG — no accessible name -->
<div role="meter" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5"></div>

<!-- CORRECT — aria-label provides context -->
<div role="meter" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5"
     aria-label="Product rating">
</div>

<!-- CORRECT — aria-labelledby references visible text -->
<h3 id="rating-heading">Customer Rating</h3>
<div role="meter" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5"
     aria-labelledby="rating-heading">
</div>
```

### Rating bar patterns

When a rating widget shows multiple individual bars/stars, each one needs a descriptive label:

```html
<!-- WRONG — multiple meters with no distinguishing names -->
<div role="meter" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100"></div>
<div role="meter" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
<div role="meter" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>

<!-- CORRECT — each meter labeled with what it represents -->
<div role="meter" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100"
     aria-label="5-star reviews, 45%">
</div>
<div role="meter" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"
     aria-label="4-star reviews, 30%">
</div>
<div role="meter" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"
     aria-label="3-star reviews, 15%">
</div>
```

### Progressbar patterns

```html
<!-- Loading indicator -->
<div role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
     aria-label="Uploading file">
</div>

<!-- Indeterminate progress (no value) -->
<div role="progressbar" aria-label="Loading search results"></div>
```

---

## Detection Patterns

```bash
# Find meters and progressbars — verify each has aria-label or aria-labelledby
grep -r "role=\"meter\"\|role=\"progressbar\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html"
```

Flag as **FAIL** if `role="meter"` or `role="progressbar"` appears without `aria-label` or `aria-labelledby` in the same element.

---

## Platform Implementation

- **Web**: `role="meter"` / `role="progressbar"` with `aria-label` or `aria-labelledby`
- **iOS**: `ProgressView` automatically announces progress; custom meters need `.accessibilityLabel()` + `.accessibilityValue()`
- **Android**: `ProgressBar` with `contentDescription`; Compose `LinearProgressIndicator` with `Modifier.semantics { contentDescription = "..." }`

---

## Resources

- WCAG 1.1.1 Non-text Content: <https://www.w3.org/WAI/WCAG22/Understanding/non-text-content>
- WCAG 4.1.2 Name, Role, Value: <https://www.w3.org/WAI/WCAG22/Understanding/name-role-value>
- ARIA meter role: <https://www.w3.org/TR/wai-aria-1.2/#meter>
- ARIA progressbar role: <https://www.w3.org/TR/wai-aria-1.2/#progressbar>
