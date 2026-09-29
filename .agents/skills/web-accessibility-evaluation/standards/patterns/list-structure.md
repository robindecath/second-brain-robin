# List Structure

## Overview

Semantic lists allow screen reader users to understand grouped items, navigate between them, and know how many items exist in a group. Incorrect list markup or CSS that strips semantics creates invisible structure problems.

**WCAG criteria**: 1.3.1 (Info and Relationships)

---

## Rules

### Use semantic list elements for grouped items

```html
<!-- Correct: semantic list -->
<ul>
  <li>Item one</li>
  <li>Item two</li>
</ul>

<!-- Wrong: visual list without semantics -->
<div class="list">
  <div class="item">Item one</div>
  <div class="item">Item two</div>
</div>
```

### Anti-patterns

- `<div>` children inside `<ul>` or `<ol>` (only `<li>` is valid)
- `<li>` inside `<div>` (must be inside `<ul>`, `<ol>`, or `<menu>`)
- Flex/grid container of identical items without list semantics

---

## Safari List Semantics Stripping (Critical)

When `list-style: none`, `display: flex`, or `display: grid` is applied to `<ul>`/`<ol>` **outside** a `<nav>` element, Safari **strips list semantics**. VoiceOver will NOT announce "list, X items" or "bullet" — the list becomes invisible to AT.

### When `role="list"` is REQUIRED (not redundant)

```html
<!-- Safari strips semantics because of list-style: none -->
<ul class="product-grid" style="list-style: none; display: grid">
  <li>Product 1</li>
  <li>Product 2</li>
</ul>

<!-- FIX: role="list" restores semantics in Safari -->
<ul class="product-grid" role="list" style="list-style: none; display: grid">
  <li>Product 1</li>
  <li>Product 2</li>
</ul>
```

### When `role="list"` is NOT needed

Lists inside `<nav>` elements are NOT affected by this Safari behavior:

```html
<!-- No role needed — Safari preserves semantics inside <nav> -->
<nav aria-label="Primary">
  <ul style="list-style: none; display: flex">
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

### Auditor Rule

> The auditor MUST NOT flag `role="list"` as "redundant ARIA" if `list-style: none`, `display: flex`, or `display: grid` is applied to the list AND the list is outside a `<nav>`. Verify CSS before flagging.

---

## Detection Patterns

```bash
# Find role="list" usage — verify it's needed (not inside <nav>)
grep -r "role=\"list\"\|role=\"listitem\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte"

# Find CSS that strips list semantics — cross-reference with <ul>/<ol> usage
grep -r "list-none\|list-style.*none" . --include="*.css" --include="*.scss"
```

---

## Platform Implementation

- **Web**: HTML `<ul>`, `<ol>`, `<dl>` + `role="list"` when CSS strips semantics
- **iOS**: SwiftUI `List` or `ForEach` with proper grouping — see `../../references/references/lists.md`
- **Android**: `RecyclerView` with `CollectionInfo` / Compose `LazyColumn` with semantics — see `../../references/references/accessibility-roles.md`

---

## Resources

- WCAG 1.3.1 Info and Relationships: <https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships>
- Scott O'Hara — "Fixing Lists": <https://www.scottohara.me/blog/2019/01/12/lists-and-safari.html>
- WebKit Bug — VoiceOver list semantics: <https://bugs.webkit.org/show_bug.cgi?id=170179>
