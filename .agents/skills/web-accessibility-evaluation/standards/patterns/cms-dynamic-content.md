# CMS & Dynamic Content Evaluation

## Overview

Many accessibility violations are invisible to static code analysis because the actual content comes from a CMS, API, or database at runtime. This pattern provides guidance for identifying and classifying these data-dependent accessibility concerns.

**WCAG criteria**: 1.1.1 (Non-text Content), 2.4.4 (Link Purpose), 4.1.2 (Name, Role, Value)

---

## The Problem

Static analysis can verify that an `alt` attribute **exists**, but not that its **value** is meaningful. When content is data-driven, the code may be structurally correct yet produce accessibility violations at runtime depending on data quality.

---

## How to Identify CMS-Driven Patterns

### Pattern 1: Props or variables as accessibility values

```tsx
// Data-dependent alt — compliance depends on API data quality
<img src={product.image} alt={product.caption} />

// Data-dependent link text — compliance depends on CMS content
<a href={item.url}>{item.title}</a>

// Data-dependent aria-label
<button aria-label={action.label}>{action.icon}</button>
```

### Pattern 2: Empty-string fallbacks

```tsx
// DANGEROUS — fallback to "" makes informative image decorative
<img src={product.image} alt={product.caption ?? ""} />

// DANGEROUS — link with potentially empty text
<a href={item.url}>{item.title || ""}</a>
```

### Pattern 3: Links wrapping only child content from data

```tsx
// If the image has no alt and no aria-label on the link,
// the link has no accessible name when caption is empty
<Link href={product.url}>
  <img src={product.image} alt={product.caption} />
</Link>
```

---

## Classification Rules

| Code pattern | Classification | Rationale |
| ------------ | -------------- | --------- |
| `alt={variable}` where variable can be null/empty | **RUNTIME_REQUIRED** | Cannot guarantee non-empty |
| `alt={variable \|\| "Fallback description"}` | **PASS** | Guaranteed non-empty accessible text |
| `alt={variable ?? ""}` on informative image | **RUNTIME_REQUIRED** | Empty fallback on informative image |
| `aria-label={t("key")}` | **PASS** | Translation system guarantees value |
| `<a>` wrapping only `<img>` without explicit `aria-label` | **RUNTIME_REQUIRED** | Link name depends entirely on child content |
| `alt=""` on explicitly decorative image | **PASS** | Correctly hidden from AT |

---

## The Rule

> If a text value comes from an API/CMS/database and the code does not guarantee a non-empty fallback, mark **RUNTIME_REQUIRED**, not PASS.

---

## Audit Guidance

When auditing code with CMS-driven content:

1. **Search for variable alt text**: `alt={`, `alt="` followed by template expressions
2. **Search for empty fallbacks**: `?? ""`, `|| ""`, `?? ''`, `|| ''` on accessibility-critical attributes
3. **Search for links wrapping only dynamic content**: `<a>` or `<Link>` containing only `{variable}` or `<img>` with data-driven alt
4. **Classify each instance** using the table above
5. **Generate testing plan items** for all RUNTIME_REQUIRED instances — these require manual verification of actual rendered content

---

## Platform Implementation

- **Web**: Check JSX/TSX props, template literals in Vue/Svelte
- **iOS**: Check `Text()` views with variable content used as `.accessibilityLabel()`
- **Android**: Check `contentDescription` set from ViewModel/LiveData/StateFlow data

---

## Resources

- WCAG 1.1.1 Non-text Content: <https://www.w3.org/WAI/WCAG22/Understanding/non-text-content>
- WCAG 2.4.4 Link Purpose: <https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context>
