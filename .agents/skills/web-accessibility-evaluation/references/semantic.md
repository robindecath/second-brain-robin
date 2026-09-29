# Semantic HTML & ARIA with Vitamin Play

**Purpose**: Decision trees for choosing the right Vitamin Play component or semantic HTML element, plus ARIA patterns for custom implementations.

---

## Decision Tree: Interactive Elements

### When User Needs to Click/Interact

```
Need clickable element?
│
├─ Navigates to another page/URL?
│  ├─ External link → <VpButton href="..." target="_blank" rel="noopener">
│  └─ Internal navigation → <VpButton href="...">
│
├─ Performs action (no navigation)?
│  ├─ Has visible text → <VpButton onClick={...}>
│  ├─ Icon only → <VpIconButton aria-label="..." onClick={...}>
│  ├─ Submits form → <VpButton type="submit">
│  └─ Opens dialog/menu → <VpButton aria-haspopup="dialog|menu">
│
├─ Toggle state (on/off)?
│  ├─ Boolean choice → <VpCheckbox>
│  └─ Custom toggle → <VpButton> with aria-pressed
│
└─ Not interactive → Use <div> or <span> (no onClick!)
```

### Examples

```tsx
import { VpButton, VpIconButton } from "@vtmn-play/react";
import { VpCloseIcon, VpMenuIcon } from "@vtmn-play/icons/react";

// ✅ Navigation
<VpButton href="/products">View products</VpButton>
<VpButton href="https://example.com" target="_blank" rel="noopener">
  External link
</VpButton>

// ✅ Actions
<VpButton onClick={handleSave}>Save changes</VpButton>
<VpButton type="submit">Submit form</VpButton>

// ✅ Icon-only actions
<VpIconButton aria-label="Close dialog" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>

<VpIconButton aria-label="Open menu" aria-haspopup="menu" onClick={handleMenu}>
  <VpMenuIcon />
</VpIconButton>

// ✅ Toggle (using aria-pressed for custom toggle)
<VpButton
  onClick={handleToggle}
  aria-pressed={isActive}
  aria-label={isActive ? "Mute notifications" : "Unmute notifications"}
>
  {isActive ? "Muted" : "Unmuted"}
</VpButton>
```

---

## Decision Tree: Form Elements

```
Collecting user input?
│
├─ Short text (name, email, search)?
│  └─ <VpInput type="text|email|search"> in <VpFormControl>
│
├─ Password?
│  └─ <VpInput type="password"> with show/hide toggle
│
├─ Number?
│  └─ <VpInput type="number">
│
├─ Date/Time?
│  └─ <VpInput type="date|time"> or custom VpDatePicker
│
├─ Single choice from list?
│  ├─ Few options (2-5) → <VpRadioGroup>
│  └─ Many options (5+) → <VpSelect>
│
├─ Multiple choices?
│  ├─ Few options (2-5) → <VpCheckbox> (multiple instances)
│  └─ Many options → <VpSelect multiple> or custom VpCombobox
│
├─ Long text?
│  └─ <VpTextarea> in <VpFormControl>
│
├─ Boolean toggle?
│  ├─ Agreement/acceptance → <VpCheckbox>
│  └─ On/off setting → <VpSwitch>
│
└─ File upload?
   └─ <input type="file"> (native) with <VpFormControl>
```

### Examples

```tsx
import {
  VpFormControl,
  VpFormLabel,
  VpInput,
  VpCheckbox,
  VpSelect,
  VpTextarea,
} from "@vtmn-play/react";

// ✅ Text input
<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
</VpFormControl>

// ✅ Checkbox for agreement
<VpCheckbox name="terms" required>
  I accept the terms and conditions
</VpCheckbox>

// ✅ Select dropdown
<VpFormControl>
  <VpFormLabel>Country</VpFormLabel>
  <VpSelect name="country">
    <option value="">Select a country</option>
    <option value="fr">France</option>
    <option value="us">United States</option>
  </VpSelect>
</VpFormControl>

// ✅ Textarea
<VpFormControl>
  <VpFormLabel>Message</VpFormLabel>
  <VpTextarea name="message" rows={4} />
</VpFormControl>
```

---

## Decision Tree: Content Structure

```
Organizing content?
│
├─ Self-contained, reusable content?
│  └─ <article>
│     Examples: Blog post, product card, comment
│
├─ Thematic grouping?
│  └─ <section>
│     Examples: Chapter, tab panel, page section
│
├─ Navigation links?
│  └─ <nav>
│     Examples: Main nav, breadcrumbs, pagination
│
├─ Supplementary content?
│  └─ <aside>
│     Examples: Sidebar, related links, callout
│
├─ Main content area (one per page)?
│  └─ <main>
│
├─ Page header?
│  └─ <header>
│
├─ Page footer?
│  └─ <footer>
│
├─ List of items?
│  ├─ Ordered sequence → <ol><li>
│  └─ Unordered list → <ul><li>
│
└─ Generic container (no semantic meaning)?
   └─ <div>
```

### Examples

```tsx
// ✅ Article (product card)
<article>
  <h2>Mountain Bike Pro</h2>
  <img src="bike.jpg" alt="Mountain bike with 21 gears" />
  <p>$599.99</p>
  <VpButton>Add to cart</VpButton>
</article>

// ✅ Navigation
<nav aria-label="Main navigation">
  <ul>
    <li><VpButton href="/">Home</VpButton></li>
    <li><VpButton href="/products">Products</VpButton></li>
    <li><VpButton href="/about">About</VpButton></li>
  </ul>
</nav>

// ✅ Section with heading
<section>
  <h2>Featured Products</h2>
  <div className="product-grid">
    {/* Product cards */}
  </div>
</section>

// ✅ Main content
<main id="main-content" tabIndex={-1}>
  <h1>Page Title</h1>
  {/* Page content */}
</main>
```

---

## ARIA Patterns for Custom Components

### When to Use ARIA

**Golden Rule**: Use semantic HTML first. ARIA only when HTML can't express the pattern.

```tsx
// ❌ WRONG - Redundant ARIA
<button role="button">Click me</button>

// ✅ CORRECT - Native element
<VpButton>Click me</VpButton>

// ⚠️ NECESSARY - No native pattern exists
<div role="tablist">
  <button role="tab" aria-selected="true">Tab 1</button>
</div>
```

---

## Common ARIA Patterns

### Tabs

```tsx
// Use native Vp component if available
import { VpTabs, VpTabsList, VpTabsTrigger, VpTabsPanel } from "@vtmn-play/react";

<VpTabs defaultValue="overview" aria-label="Product information">
  <VpTabsList>
    <VpTabsTrigger value="overview">Overview</VpTabsTrigger>
    <VpTabsTrigger value="specs">Specifications</VpTabsTrigger>
  </VpTabsList>
  <VpTabsPanel value="overview">Overview content</VpTabsPanel>
  <VpTabsPanel value="specs">Specifications content</VpTabsPanel>
</VpTabs>

// If implementing custom tabs:
<div role="tablist" aria-label="Product information">
  <VpButton
    role="tab"
    aria-selected={activeTab === 0}
    aria-controls="panel-0"
    id="tab-0"
    onClick={() => setActiveTab(0)}
  >
    Overview
  </VpButton>
</div>
<div
  role="tabpanel"
  id="panel-0"
  aria-labelledby="tab-0"
  hidden={activeTab !== 0}
>
  Overview content
</div>
```

### Accordion

```tsx
// Use VpAccordion component if available
import { VpAccordion, VpAccordionItem } from "@vtmn-play/react";

<VpAccordion>
  <VpAccordionItem title="Section 1">
    Content for section 1
  </VpAccordionItem>
  <VpAccordionItem title="Section 2">
    Content for section 2
  </VpAccordionItem>
</VpAccordion>

// If implementing custom accordion:
<div>
  <h3>
    <VpButton
      aria-expanded={isOpen}
      aria-controls="section-1"
      onClick={() => setIsOpen(!isOpen)}
    >
      Section 1
    </VpButton>
  </h3>
  <div id="section-1" hidden={!isOpen}>
    Content for section 1
  </div>
</div>
```

### Menu/Dropdown

```tsx
// Prefer VpMenu if available, or implement with ARIA
<VpButton
  aria-haspopup="menu"
  aria-expanded={isMenuOpen}
  onClick={() => setIsMenuOpen(!isMenuOpen)}
>
  Actions
</VpButton>;

{
  isMenuOpen && (
    <ul role="menu" aria-label="Actions">
      <li role="none">
        <VpButton role="menuitem" onClick={handleEdit}>
          Edit
        </VpButton>
      </li>
      <li role="none">
        <VpButton role="menuitem" onClick={handleDelete}>
          Delete
        </VpButton>
      </li>
    </ul>
  );
}
```

---

## Essential ARIA Attributes

### Labels and Descriptions

```tsx
// aria-label - When no visible label exists
<VpIconButton aria-label="Close dialog" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>

// aria-labelledby - Reference existing text
<section aria-labelledby="products-heading">
  <h2 id="products-heading">Featured Products</h2>
  {/* Products */}
</section>

// aria-describedby - Additional description
<VpFormControl>
  <VpFormLabel htmlFor="password">Password</VpFormLabel>
  <VpInput
    id="password"
    type="password"
    aria-describedby="password-requirements"
  />
  <div id="password-requirements">
    Must be at least 8 characters
  </div>
</VpFormControl>
```

### States

```tsx
// aria-expanded - Collapsible/expandable
<VpButton
  aria-expanded={isOpen}
  aria-controls="content-1"
  onClick={() => setIsOpen(!isOpen)}
>
  Toggle content
</VpButton>

// aria-pressed - Toggle button state
<VpButton
  aria-pressed={isMuted}
  onClick={() => setIsMuted(!isMuted)}
>
  {isMuted ? "Unmute" : "Mute"}
</VpButton>

// aria-selected - Selected item in a group
<VpButton role="tab" aria-selected={isActive}>
  Tab
</VpButton>

// aria-checked - Checkbox/radio state (handled by VpCheckbox)
<VpCheckbox checked={isChecked} onChange={handleChange}>
  Option
</VpCheckbox>
```

### Live Regions

```tsx
// aria-live - Announce dynamic content changes
<div role="status" aria-live="polite">
  {successMessage}
</div>

<div role="alert" aria-live="assertive">
  {errorMessage}
</div>

// Common patterns
{isLoading && (
  <div role="status" aria-live="polite">
    <span className="sr-only">Loading...</span>
    <div className="spinner" aria-hidden="true" />
  </div>
)}

{itemsCount > 0 && (
  <div role="status" aria-live="polite" aria-atomic="true">
    {itemsCount} items found
  </div>
)}
```

### Hidden Content

```tsx
// aria-hidden - Hide decorative content from screen readers
<VpButton>
  <VpHeartIcon aria-hidden="true" />
  Add to favorites
</VpButton>

// hidden attribute - Hide content from everyone
<div hidden={!isOpen}>
  Hidden content
</div>
```

---

## Heading Hierarchy

### Rules

- **One `<h1>` per page** (main page title)
- **Sequential levels** - Never skip (h1 → h2 → h3, not h1 → h3)
- **Use CSS for styling** - Don't choose heading level based on size

```tsx
// ✅ CORRECT hierarchy
<h1>Product Page</h1>
<section>
  <h2>Description</h2>
  <p>Product description...</p>

  <h3>Features</h3>
  <ul>...</ul>

  <h3>Specifications</h3>
  <ul>...</ul>
</section>

<section>
  <h2>Reviews</h2>
  <article>
    <h3>Customer review</h3>
    <p>Review content...</p>
  </article>
</section>

// ❌ WRONG - Skips h2
<h1>Product Page</h1>
<h3>Description</h3>

// ❌ WRONG - Multiple h1s
<h1>Site Title</h1>
<h1>Page Title</h1>
```

---

## Landmarks

### Use Semantic HTML for Landmarks

```tsx
// ✅ HTML5 elements provide automatic landmarks
<header>
  <nav aria-label="Main navigation">
    {/* Nav links */}
  </nav>
</header>

<main id="main-content">
  {/* Main content */}
</main>

<aside aria-label="Related products">
  {/* Sidebar */}
</aside>

<footer>
  {/* Footer content */}
</footer>

// Only use role when HTML5 element not available
<div role="navigation" aria-label="Breadcrumbs">
  {/* Breadcrumb links */}
</div>
```

### Labeling Multiple Landmarks

```tsx
// When multiple navs, label them
<nav aria-label="Main navigation">
  {/* Main nav */}
</nav>

<nav aria-label="Footer navigation">
  {/* Footer nav */}
</nav>

// When multiple sections, use aria-labelledby
<section aria-labelledby="featured-heading">
  <h2 id="featured-heading">Featured Products</h2>
</section>

<section aria-labelledby="sale-heading">
  <h2 id="sale-heading">On Sale</h2>
</section>
```

---

## Summary: Component Selection Quick Reference

| Need              | Use This                             | Package                  |
| ----------------- | ------------------------------------ | ------------------------ |
| Button with text  | `<VpButton>`                         | @vtmn-play/react         |
| Icon-only button  | `<VpIconButton aria-label>`          | @vtmn-play/react         |
| Link (navigation) | `<VpButton href>`                    | @vtmn-play/react         |
| Text input        | `<VpInput>` in `<VpFormControl>`     | @vtmn-play/react         |
| Checkbox          | `<VpCheckbox>`                       | @vtmn-play/react         |
| Select dropdown   | `<VpSelect>`                         | @vtmn-play/react         |
| Textarea          | `<VpTextarea>`                       | @vtmn-play/react         |
| Modal dialog      | `<VpModal>`                          | @vtmn-play/react         |
| Icon              | Import from `@vtmn-play/icons/react` | @vtmn-play/icons         |
| Color             | Use `var(--vp-semantic-color-*)`     | @vtmn-play/design-tokens |

**Framework Adaptation**:

- **Vue**: Import from `@vtmn-play/vue`, use `@click` instead of `onClick`
- **Svelte**: Import from `@vtmn-play/svelte`, use `on:click` instead of `onClick`
