# Keyboard Navigation & Focus Management

**Purpose**: Complete guide to keyboard navigation patterns, focus management, and skip links using Vitamin Play components.

---

## Sommaire

- [Core Principles](#core-principles)
- [Focus Visibility](#focus-visibility)
- [Tab Order](#tab-order)
- [Skip Links](#skip-links)
- [Keyboard Patterns](#keyboard-patterns)
- [Focus Management After Interactions](#focus-management-after-interactions)
- [Roving tabindex (for Component Groups)](#roving-tabindex-for-component-groups)
- [Focus Traps (Modals)](#focus-traps-modals)
- [Common Pitfalls](#common-pitfalls)
- [Testing Checklist](#testing-checklist)
- [Quick Reference](#quick-reference)
- [Resources](#resources)

---

## Core Principles

Search terms: skip navigation, skip link, bypass blocks, keyboard bypass link.

1. **All interactive elements must be keyboard-accessible** - Tab key navigates to all buttons, links, inputs
2. **Focus order must be logical** - Follows visual/reading order (top-to-bottom, left-to-right)
3. **Focus must be visible** - Clear visual indicator (never remove without replacement)
4. **Focus must not be trapped** - User can always Tab away (except in modals where intentional)
5. **Restore focus after interactions** - Return focus to trigger element when closing dialogs

---

## Focus Visibility

### The :focus-visible Pattern

```css
/* ❌ WRONG - Removes all focus indicators */
*:focus {
  outline: none;
}

button:focus {
  outline: none;
}

/* ✅ CORRECT - Custom indicator on keyboard focus only */
*:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}

/* Optional: Remove indicator on mouse/touch */
*:focus:not(:focus-visible) {
  outline: none;
}
```

**`:focus-visible`** shows outline only for keyboard navigation, not mouse clicks.

### Vitamin Play Components

```tsx
// ✅ VpButton has built-in focus styles
import { VpButton } from "@vtmn-play/react";

<VpButton>Accessible button</VpButton>
// Automatically includes :focus-visible styles with correct contrast

// Custom focus styling (when needed)
<VpButton
  style={{
    "--focus-outline-color": "var(--vp-semantic-color-border-focus)",
  }}
>
  Custom focus
</VpButton>
```

### Contrast Requirements

Focus indicators must have **3:1 contrast** against background (WCAG 2.4.11).

```css
/* ✅ PASS - Focus token ensures sufficient contrast */
*:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}

/* ❌ FAIL - Light gray on white fails 3:1 */
*:focus-visible {
  outline: 2px solid #cccccc;
}
```

---

## Tab Order

### Natural Tab Order

Tab order follows DOM order. Don't use `tabindex` > 0.

```tsx
// ✅ CORRECT - Natural tab order: 1 → 2 → 3 → 4
<VpInput type="text" name="name" />
<VpInput type="email" name="email" />
<VpCheckbox name="terms">Accept terms</VpCheckbox>
<VpButton type="submit">Submit</VpButton>
```

### Managing tabindex

```html
<!-- tabindex="0" - Adds to natural tab order -->
<div role="button" tabindex="0" onclick="...">Custom interactive element</div>

<!-- tabindex="-1" - Programmatically focusable only -->
<main id="main-content" tabindex="-1">
  <!-- Can receive focus via JS but not Tab key -->
</main>

<!-- ❌ tabindex="1+" - NEVER USE - breaks natural order -->
<button tabindex="5">Don't do this</button>
```

**Rules**:

- Use `tabindex="0"` for custom interactive elements
- Use `tabindex="-1"` for programmatic focus (skip links, dialogs)
- **Never** use positive integers

---

## Skip Links

Allow keyboard users to skip repetitive content.

### Implementation

```tsx
// Place at very top of layout
export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>

      <header>
        <nav>{/* Navigation */}</nav>
      </header>

      <main id="main-content" tabIndex={-1}>
        {children}
      </main>
    </>
  );
}
```

### Skip Link Styles

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--vp-semantic-color-background-brand);
  color: var(--vp-semantic-color-content-brand);
  padding: 0.5rem 1rem;
  text-decoration: none;
  z-index: 9999;
  border-radius: 0 0 0.25rem 0;
}

.skip-link:focus {
  top: 0;
}
```

### Multiple Skip Links

```tsx
<div className="skip-links">
  <a href="#main-content" className="skip-link">
    Skip to main content
  </a>
  <a href="#nav" className="skip-link">
    Skip to navigation
  </a>
  <a href="#search" className="skip-link">
    Skip to search
  </a>
</div>

{/* Targets */}
<nav id="nav">{/* Navigation */}</nav>
<div id="search">{/* Search */}</div>
<main id="main-content" tabIndex={-1}>{/* Content */}</main>
```

### Focusing Skip Link Target

```tsx
import { useEffect, useRef } from "react";

function MainContent() {
  const mainRef = useRef<HTMLElement>(null);

  useEffect(() => {
    // Handle skip link clicks
    const handleHashChange = () => {
      if (window.location.hash === "#main-content") {
        mainRef.current?.focus();
      }
    };

    window.addEventListener("hashchange", handleHashChange);
    handleHashChange(); // Check on mount

    return () => window.removeEventListener("hashchange", handleHashChange);
  }, []);

  return (
    <main ref={mainRef} id="main-content" tabIndex={-1}>
      {/* Content */}
    </main>
  );
}
```

---

## Keyboard Patterns

### Standard Keys

| Key             | Action                                   |
| --------------- | ---------------------------------------- |
| **Tab**         | Move to next focusable element           |
| **Shift + Tab** | Move to previous focusable element       |
| **Enter**       | Activate button/link                     |
| **Space**       | Activate button/checkbox                 |
| **Escape**      | Close dialog/menu                        |
| **Arrow keys**  | Navigate within components (tabs, menus) |
| **Home**        | Move to first item in list               |
| **End**         | Move to last item in list                |

### VpButton Keyboard Support

```tsx
import { VpButton } from "@vtmn-play/react";

// ✅ Automatically handles Enter and Space
<VpButton onClick={handleClick}>
  Click me
</VpButton>
// Activates on Enter key AND Space bar

// ✅ Link button navigates on Enter
<VpButton href="/products">
  View products
</VpButton>
```

### Custom Keyboard Handlers

```tsx
import { VpButton } from "@vtmn-play/react";

function ExpandableSection() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div>
      <VpButton
        onClick={() => setIsExpanded(!isExpanded)}
        aria-expanded={isExpanded}
        aria-controls="content-1"
      >
        Toggle content
      </VpButton>

      <div id="content-1" hidden={!isExpanded}>
        Content
      </div>
    </div>
  );
}
```

---

## Focus Management After Interactions

### Closing Dialogs

```tsx
import { useRef, useEffect } from "react";
import { VpButton } from "@vtmn-play/react";

function DialogExample() {
  const [isOpen, setIsOpen] = useState(false);
  const triggerRef = useRef<HTMLButtonElement>(null);

  const handleOpen = () => {
    setIsOpen(true);
  };

  const handleClose = () => {
    setIsOpen(false);
    // Restore focus to trigger button
    triggerRef.current?.focus();
  };

  return (
    <>
      <VpButton ref={triggerRef} onClick={handleOpen}>
        Open dialog
      </VpButton>

      {isOpen && (
        <div role="dialog">
          <h2>Dialog title</h2>
          <VpButton onClick={handleClose}>Close</VpButton>
        </div>
      )}
    </>
  );
}
```

### Deleting Items

```tsx
function ItemList() {
  const [items, setItems] = useState(["Item 1", "Item 2", "Item 3"]);

  const handleDelete = (index: number) => {
    setItems(items.filter((_, i) => i !== index));

    // Focus next item, or previous if last, or container if empty
    setTimeout(() => {
      const nextButton = document.querySelector(
        `[data-item-index="${index}"]`,
      ) as HTMLElement;

      if (nextButton) {
        nextButton.focus();
      } else {
        const prevButton = document.querySelector(
          `[data-item-index="${index - 1}"]`,
        ) as HTMLElement;
        prevButton?.focus();
      }
    }, 0);
  };

  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>
          {item}
          <VpButton
            data-item-index={index}
            onClick={() => handleDelete(index)}
            aria-label={`Delete ${item}`}
          >
            Delete
          </VpButton>
        </li>
      ))}
    </ul>
  );
}
```

---

## Roving tabindex (for Component Groups)

Use roving tabindex for component groups (tabs, toolbars, listboxes).

### Tab Component Example

```tsx
import { useState, useRef, useEffect } from "react";
import { VpButton } from "@vtmn-play/react";

function Tabs() {
  const [activeTab, setActiveTab] = useState(0);
  const tabRefs = useRef<(HTMLButtonElement | null)[]>([]);

  const tabs = ["Overview", "Specifications", "Reviews"];

  const handleKeyDown = (e: React.KeyboardEvent, index: number) => {
    let newIndex = index;

    switch (e.key) {
      case "ArrowLeft":
        e.preventDefault();
        newIndex = index > 0 ? index - 1 : tabs.length - 1;
        break;
      case "ArrowRight":
        e.preventDefault();
        newIndex = index < tabs.length - 1 ? index + 1 : 0;
        break;
      case "Home":
        e.preventDefault();
        newIndex = 0;
        break;
      case "End":
        e.preventDefault();
        newIndex = tabs.length - 1;
        break;
    }

    if (newIndex !== index) {
      setActiveTab(newIndex);
      tabRefs.current[newIndex]?.focus();
    }
  };

  return (
    <div role="tablist" aria-label="Product information">
      {tabs.map((tab, index) => (
        <VpButton
          key={index}
          ref={(el) => (tabRefs.current[index] = el)}
          role="tab"
          aria-selected={activeTab === index}
          aria-controls={`panel-${index}`}
          tabIndex={activeTab === index ? 0 : -1}
          onClick={() => setActiveTab(index)}
          onKeyDown={(e) => handleKeyDown(e, index)}
        >
          {tab}
        </VpButton>
      ))}
    </div>
  );
}
```

**Pattern**:

- Only active tab has `tabIndex={0}`
- Other tabs have `tabIndex={-1}`
- Arrow keys move focus between tabs
- Tab key moves out of tab group

---

## Focus Traps (Modals)

See `dialog.md` for complete modal focus trap patterns with `VpModal`.

---

## Common Pitfalls

### ❌ Removing Focus Outline Without Replacement

```css
/* NEVER do this */
*:focus {
  outline: none;
}
```

### ❌ Focusable Elements Not in Tab Order

```tsx
// WRONG - div is not focusable
<div onClick={handleClick}>Click me</div>

// CORRECT - Use VpButton
<VpButton onClick={handleClick}>Click me</VpButton>
```

### ❌ Using Positive tabindex

```tsx
// WRONG - Breaks natural tab order
<VpButton tabIndex={1}>First</VpButton>
<VpButton tabIndex={2}>Second</VpButton>

// CORRECT - Natural DOM order
<VpButton>First</VpButton>
<VpButton>Second</VpButton>
```

### ❌ Not Restoring Focus After Dialog Close

```tsx
// WRONG - Focus lost after closing
const handleClose = () => {
  setIsOpen(false);
  // Where does focus go? Lost!
};

// CORRECT - Restore to trigger
const handleClose = () => {
  setIsOpen(false);
  triggerRef.current?.focus();
};
```

---

## Testing Checklist

### Manual Keyboard Testing

- [ ] **Tab** navigates to all interactive elements
- [ ] **Tab order** is logical (follows visual order)
- [ ] **Focus indicator** is visible at all times
- [ ] **Enter/Space** activates buttons
- [ ] **Escape** closes dialogs/menus
- [ ] **Skip link** works and is visible on focus
- [ ] **Focus restored** after closing dialogs
- [ ] **No keyboard traps** (can Tab away from everything except modals)

### Screen Reader Testing

- [ ] Skip link announced
- [ ] Focus changes announced
- [ ] Button/link roles announced correctly
- [ ] Expanded/collapsed states announced

### Tools

- **Tab key** - Primary testing tool!
- **axe DevTools** - Detects focus order issues
- **Accessibility Insights** - Tab stops visualization
- **WAVE** - Highlights keyboard issues

---

## Quick Reference

| Pattern          | Implementation                                           |
| ---------------- | -------------------------------------------------------- |
| Focus visibility | `:focus-visible` with `--vp-semantic-color-border-focus` |
| Skip link        | `<a href="#main-content">` at top of page                |
| Tab order        | Natural DOM order, `tabindex="0"` or `"-1"` only         |
| Restore focus    | Save ref before opening dialog, focus on close           |
| Roving tabindex  | Active item `tabindex="0"`, others `"-1"`                |
| Focus trap       | Use `VpModal` or custom hook                             |
| SPA navigation   | Focus main content on route change                       |

---

## Resources

- **WCAG 2.4.3 Focus Order**: <https://www.w3.org/WAI/WCAG22/Understanding/focus-order>
- **WCAG 2.4.7 Focus Visible**: <https://www.w3.org/WAI/WCAG22/Understanding/focus-visible>
- **ARIA Authoring Practices**: <https://www.w3.org/WAI/ARIA/apg/patterns/>
