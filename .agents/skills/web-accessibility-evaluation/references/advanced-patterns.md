# Advanced Accessible Patterns with Vitamin Play

**Purpose**: Complete implementations of complex interactive patterns (tabs, accordions, menus, tooltips) using Vitamin Play components with full accessibility support.

---

## Sommaire

- [Tabs Pattern](#tabs-pattern)
- [Accordion Pattern](#accordion-pattern)
- [Combobox / Dropdown Menu Pattern](#combobox--dropdown-menu-pattern)
- [Tooltip Pattern](#tooltip-pattern)
- [Disclosure Pattern (Expandable Section)](#disclosure-pattern-expandable-section)
- [Breadcrumb Navigation](#breadcrumb-navigation)
- [Pagination Pattern](#pagination-pattern)
- [Alert/Banner Pattern](#alertbanner-pattern)
- [Framework Adaptation](#framework-adaptation)
- [Testing Checklist](#testing-checklist)

---

## Tabs Pattern

### Using VpTabs Component

Vitamin Play provides a complete `VpTabs` component with built-in accessibility. Use it instead of building custom tabs.

```tsx
import {
  VpTabs,
  VpTabsList,
  VpTabsTrigger,
  VpTabsPanel,
} from "@vtmn-play/react";

function ProductTabs() {
  return (
    <VpTabs
      defaultValue="details"
      aria-label="Product information"
      tabPanelSlot={
        <>
          <VpTabsPanel value="details">
            <h3 className="vp-title-s">Product Details</h3>
            <p>Detailed product information goes here.</p>
          </VpTabsPanel>

          <VpTabsPanel value="specs">
            <h3 className="vp-title-s">Specifications</h3>
            <ul>
              <li>Weight: 2.5 kg</li>
              <li>Dimensions: 30x20x10 cm</li>
            </ul>
          </VpTabsPanel>

          <VpTabsPanel value="reviews">
            <h3 className="vp-title-s">Customer Reviews</h3>
            <p>User reviews appear here.</p>
          </VpTabsPanel>
        </>
      }
    >
      <VpTabsList>
        <VpTabsTrigger value="details">Details</VpTabsTrigger>
        <VpTabsTrigger value="specs">Specifications</VpTabsTrigger>
        <VpTabsTrigger value="reviews">Reviews</VpTabsTrigger>
      </VpTabsList>
    </VpTabs>
  );
}
```

**Controlled tabs:**

```tsx
import { useState } from "react";

function ControlledTabs() {
  const [activeTab, setActiveTab] = useState("details");

  return (
    <VpTabs
      value={activeTab}
      onChange={setActiveTab}
      aria-label="Product information"
      tabPanelSlot={/* panels */}
    >
      <VpTabsList>
        <VpTabsTrigger value="details">Details</VpTabsTrigger>
        <VpTabsTrigger value="specs">Specifications</VpTabsTrigger>
      </VpTabsList>
    </VpTabs>
  );
}
```

**Built-in accessibility features:**

- ✅ **Automatic activation**: Tabs activate on focus by default (configurable with `activateOnFocus={false}`)
- ✅ **Keyboard navigation**: Arrow Left/Right, Home/End
- ✅ **Roving tabindex**: Only active tab is in tab order
- ✅ **ARIA attributes**: `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls`, `aria-labelledby`
- ✅ **Focus management**: Focus returns correctly after navigation

**Accessibility requirements for users:**

- **MUST** provide `aria-label` on `VpTabs` to describe the tab group
- **MUST** use unique `value` props for each tab/panel pair
- **CAN** disable automatic activation with `activateOnFocus={false}` if tab content is not preloaded
- **CAN** disable tabs with `disabled` prop on `VpTabsTrigger`

**Vue/Svelte adaptation:**

- **Vue**: `@change` event, import from `@vtmn-play/vue`
- **Svelte**: `on:change` event, import from `@vtmn-play/svelte`

---

## Accordion Pattern

### Using VpAccordion Component

Vitamin Play provides a complete `VpAccordion` component with built-in accessibility.

```tsx
import {
  VpAccordion,
  VpAccordionItem,
  VpAccordionItemHeader,
  VpAccordionItemHeaderLabel,
  VpAccordionItemHeaderIcon,
  VpAccordionItemPanel,
  VpAccordionDivider,
} from "@vtmn-play/react";

function FAQSection() {
  return (
    <VpAccordion
      id="faq-accordion"
      variant="primary"
      variantStyle="regular"
      multiple={false}
    >
      <VpAccordionItem value="shipping">
        <h2>
          <VpAccordionItemHeader>
            <VpAccordionItemHeaderLabel>
              What are the shipping options?
            </VpAccordionItemHeaderLabel>
            <VpAccordionItemHeaderIcon />
          </VpAccordionItemHeader>
        </h2>
        <VpAccordionItemPanel>
          <p>We offer standard, express, and overnight shipping.</p>
        </VpAccordionItemPanel>
      </VpAccordionItem>

      <VpAccordionDivider />

      <VpAccordionItem value="returns">
        <h2>
          <VpAccordionItemHeader>
            <VpAccordionItemHeaderLabel>
              What is the return policy?
            </VpAccordionItemHeaderLabel>
            <VpAccordionItemHeaderIcon />
          </VpAccordionItemHeader>
        </h2>
        <VpAccordionItemPanel>
          <p>Returns accepted within 30 days of purchase.</p>
        </VpAccordionItemPanel>
      </VpAccordionItem>

      <VpAccordionDivider />

      <VpAccordionItem value="warranty">
        <h2>
          <VpAccordionItemHeader>
            <VpAccordionItemHeaderLabel>
              Do products come with a warranty?
            </VpAccordionItemHeaderLabel>
            <VpAccordionItemHeaderIcon />
          </VpAccordionItemHeader>
        </h2>
        <VpAccordionItemPanel>
          <p>All products include a 1-year manufacturer warranty.</p>
        </VpAccordionItemPanel>
      </VpAccordionItem>
    </VpAccordion>
  );
}
```

**Controlled accordion:**

```tsx
import { useState } from "react";
import { VpButton } from "@vtmn-play/react";

function ControlledAccordion() {
  const [openItems, setOpenItems] = useState(["shipping"]);

  const closeAll = () => setOpenItems([]);

  return (
    <>
      <VpButton onClick={closeAll}>Close all items</VpButton>
      <VpAccordion
        id="controlled-accordion"
        value={openItems}
        onChange={setOpenItems}
      >
        {/* accordion items */}
      </VpAccordion>
    </>
  );
}
```

**Built-in accessibility features:**

- ✅ **ARIA attributes**: `aria-expanded`, `aria-controls`, `role="region"`
- ✅ **Keyboard support**: Enter/Space to toggle, Tab to navigate headers
- ✅ **Heading structure**: Wrap headers in `<h2>` or appropriate level
- ✅ **Focus management**: Focus stays on trigger after toggle
- ✅ **Multiple/Single mode**: Controlled with `multiple` prop

**Accessibility requirements for users:**

- **MUST** provide unique `id` prop for the accordion
- **MUST** use unique `value` props for each accordion item
- **MUST** wrap `VpAccordionItemHeader` in a heading element (`<h2>`, `<h3>`, etc.)
- **SHOULD** use `VpAccordionDivider` between items for visual separation
- **CAN** allow multiple items open with `multiple={true}`
- **CAN** disable items with `disabled` prop

**Variants:**

- `variant`: `"primary"` | `"secondary"` (styling)
- `variantStyle`: `"regular"` | `"on-brand"` (color scheme)

**Vue/Svelte adaptation:**

- **Vue**: `@change` event, `v-model:value`, import from `@vtmn-play/vue`
- **Svelte**: `on:change` event, `bind:value`, import from `@vtmn-play/svelte`

---

## Combobox / Dropdown Menu Pattern

### Using VpCombobox Component

Vitamin Play provides `VpCombobox` for dropdown/select functionality with built-in accessibility.

```tsx
import {
  VpCombobox,
  VpComboboxListbox,
  VpComboboxOption,
} from "@vtmn-play/react";
import { VpAsset } from "@vtmn-play/react";

// Basic dropdown menu for country selection
function CountrySelector() {
  const countries = ["fr", "de", "es", "us", "it", "gb", "nl"];

  return (
    <VpCombobox
      name="country"
      placeholder="Select your country"
      aria-label="Shipping country"
    >
      <VpComboboxListbox>
        {countries.map((country) => (
          <VpComboboxOption
            key={country}
            id={`option-${country}`}
            value={country}
          >
            <VpAsset name={`flag-${country}`} />
            {new Intl.DisplayNames(["en"], { type: "region" }).of(
              country.toUpperCase(),
            )}
          </VpComboboxOption>
        ))}
      </VpComboboxListbox>
    </VpCombobox>
  );
}
```

**With search/filtering (editable combobox):**

```tsx
function SearchableCombobox() {
  const [value, setValue] = useState("");

  return (
    <VpCombobox
      name="search"
      placeholder="Search countries"
      aria-label="Search for a country"
      editable={true}
      value={value}
      onChange={setValue}
    >
      <VpComboboxListbox>{/* Options */}</VpComboboxListbox>
    </VpCombobox>
  );
}
```

**With checkbox/radio mode:**

```tsx
function MultiSelectCombobox() {
  return (
    <VpCombobox
      name="sports"
      placeholder="Select sports"
      aria-label="Sports preferences"
      multiple={true}
      optionMode="checkbox"
    >
      <VpComboboxListbox>
        <VpComboboxOption id="opt-1" value="running">
          Running
        </VpComboboxOption>
        <VpComboboxOption id="opt-2" value="cycling">
          Cycling
        </VpComboboxOption>
        <VpComboboxOption id="opt-3" value="swimming">
          Swimming
        </VpComboboxOption>
      </VpComboboxListbox>
    </VpCombobox>
  );
}
```

**With VpFormControl:**

```tsx
import {
  VpFormControl,
  VpFormLabel,
  VpFormHelper,
  VpFormError,
} from "@vtmn-play/react";

function FormCombobox() {
  const [status, setStatus] = useState(undefined);

  return (
    <VpFormControl status={status} required>
      <VpFormLabel>Country</VpFormLabel>
      <VpCombobox name="country" placeholder="Select country">
        <VpComboboxListbox>{/* options */}</VpComboboxListbox>
      </VpCombobox>
      <VpFormHelper>Select your shipping destination</VpFormHelper>
      {status === "error" && <VpFormError>Please select a country</VpFormError>}
    </VpFormControl>
  );
}
```

**Built-in accessibility features:**

- ✅ **ARIA attributes**: `role="combobox"`, `aria-expanded`, `aria-controls`, `aria-autocomplete`
- ✅ **Keyboard navigation**: Arrow Up/Down, Home/End, Enter/Space, Escape
- ✅ **Search/filter**: Type to filter options (with `editable={true}`)
- ✅ **Screen reader**: Announces options, selection, and filtering
- ✅ **Multiple selection**: With `multiple={true}` prop
- ✅ **Option modes**: Checkbox/radio visual indicators with `optionMode`

**Accessibility requirements for users:**

- **MUST** provide `aria-label` OR use within `VpFormControl` with `VpFormLabel`
- **MUST** provide unique `id` for each `VpComboboxOption`
- **MUST** provide `value` for each option
- **SHOULD** use `VpFormControl` for form context
- **CAN** disable options with `disabled` prop
- **CAN** make focusable when disabled with `isFocusable={true}`

**Variants & sizes:**

- `variant`: `"default"` | `"subtle"` | `"float"`
- `size`: `"small"` | `"medium"` | `"large"`

**Vue/Svelte adaptation:**

- **Vue**: `@change`, `v-model:value`, import from `@vtmn-play/vue`
- **Svelte**: `on:change`, `bind:value`, import from `@vtmn-play/svelte`

---

## Tooltip Pattern

### Accessible Tooltip with VpButton

```tsx
import { VpIconButton } from "@vtmn-play/react";
import { VpInfoIcon } from "@vtmn-play/icons/react";
import { useState, useRef, useEffect } from "react";

interface TooltipProps {
  content: string;
  children: React.ReactNode;
}

function VpTooltip({ content, children }: TooltipProps) {
  const [isVisible, setIsVisible] = useState(false);
  const tooltipId = useRef(
    `tooltip-${Math.random().toString(36).substr(2, 9)}`,
  );

  return (
    <span style={{ position: "relative", display: "inline-block" }}>
      <span
        onMouseEnter={() => setIsVisible(true)}
        onMouseLeave={() => setIsVisible(false)}
        onFocus={() => setIsVisible(true)}
        onBlur={() => setIsVisible(false)}
        aria-describedby={isVisible ? tooltipId.current : undefined}
      >
        {children}
      </span>

      {isVisible && (
        <span
          id={tooltipId.current}
          role="tooltip"
          style={{
            position: "absolute",
            bottom: "100%",
            left: "50%",
            transform: "translateX(-50%)",
            marginBottom: "0.5rem",
            padding: "0.5rem 0.75rem",
            background: "var(--vp-semantic-color-background-inverse)",
            color: "var(--vp-semantic-color-content-inverse)",
            borderRadius: "0.25rem",
            fontSize: "0.875rem",
            whiteSpace: "nowrap",
            zIndex: 1000,
          }}
        >
          {content}
          <span
            style={{
              position: "absolute",
              top: "100%",
              left: "50%",
              transform: "translateX(-50%)",
              width: 0,
              height: 0,
              borderLeft: "6px solid transparent",
              borderRight: "6px solid transparent",
              borderTop:
                "6px solid var(--vp-semantic-color-background-inverse)",
            }}
          />
        </span>
      )}
    </span>
  );
}

// Usage
function HelpButton() {
  return (
    <VpTooltip content="Click for more information">
      <VpIconButton aria-label="Help">
        <VpInfoIcon />
      </VpIconButton>
    </VpTooltip>
  );
}
```

**Best practices:**

- Use `aria-describedby` to associate tooltip
- Show on both hover AND focus
- Don't use tooltips for essential information
- Keep content concise
- Ensure sufficient contrast for tooltip

---

## Disclosure Pattern (Expandable Section)

```tsx
import { VpButton } from "@vtmn-play/react";
import { VpChevronDownIcon } from "@vtmn-play/icons/react";
import { useState } from "react";

interface DisclosureProps {
  title: string;
  children: React.ReactNode;
  defaultExpanded?: boolean;
}

function VpDisclosure({
  title,
  children,
  defaultExpanded = false,
}: DisclosureProps) {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);
  const disclosureId = `disclosure-${title.replace(/\s+/g, "-").toLowerCase()}`;

  return (
    <div>
      <VpButton
        onClick={() => setIsExpanded(!isExpanded)}
        aria-expanded={isExpanded}
        aria-controls={disclosureId}
        variant="ghost"
        style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}
      >
        <VpChevronDownIcon
          style={{
            transform: isExpanded ? "rotate(180deg)" : "rotate(0deg)",
            transition: "transform 0.2s",
          }}
          aria-hidden="true"
        />
        <span>{title}</span>
      </VpButton>

      {isExpanded && (
        <div id={disclosureId} style={{ padding: "1rem", paddingLeft: "2rem" }}>
          {children}
        </div>
      )}
    </div>
  );
}

// Usage
function ProductDetails() {
  return (
    <VpDisclosure title="Show detailed specifications">
      <ul>
        <li>Weight: 2.5 kg</li>
        <li>Dimensions: 30x20x10 cm</li>
        <li>Material: Aluminum</li>
      </ul>
    </VpDisclosure>
  );
}
```

---

## Breadcrumb Navigation

### Using VpBreadcrumbs Component

Vitamin Play provides `VpBreadcrumbs` component for navigation breadcrumbs.

```tsx
import { VpBreadcrumbs, VpBreadcrumbsItem } from "@vtmn-play/react";

function ProductPage() {
  return (
    <VpBreadcrumbs aria-label="Breadcrumb navigation">
      <VpBreadcrumbsItem href="/">Home</VpBreadcrumbsItem>
      <VpBreadcrumbsItem href="/camping">Camping</VpBreadcrumbsItem>
      <VpBreadcrumbsItem href="/camping/tents">Tents</VpBreadcrumbsItem>
      <VpBreadcrumbsItem isCurrent>Pop up tents</VpBreadcrumbsItem>
      <VpBreadcrumbsItem isBrandLink href="/brand">
        High Mountains
      </VpBreadcrumbsItem>
    </VpBreadcrumbs>
  );
}
```

**With custom links (for routing libraries):**

```tsx
import { VpBreadcrumbsItem, VpBreadcrumbsLink } from "@vtmn-play/react";
import { Link } from "react-router-dom";

function RoutedBreadcrumbs() {
  return (
    <VpBreadcrumbs aria-label="Breadcrumb">
      <VpBreadcrumbsItem
        linkSlot={
          <VpBreadcrumbsLink asChild>
            <Link to="/">Home</Link>
          </VpBreadcrumbsLink>
        }
      />
      <VpBreadcrumbsItem
        linkSlot={
          <VpBreadcrumbsLink asChild>
            <Link to="/sports">Sports</Link>
          </VpBreadcrumbsLink>
        }
      />
      <VpBreadcrumbsItem isCurrent>Running</VpBreadcrumbsItem>
    </VpBreadcrumbs>
  );
}
```

**Controlled collapse state:**

```tsx
import { useState } from "react";
import { VpButton } from "@vtmn-play/react";

function CollapsibleBreadcrumbs() {
  const [collapsed, setCollapsed] = useState(true);

  return (
    <>
      <VpButton onClick={() => setCollapsed(!collapsed)}>
        Toggle breadcrumbs
      </VpButton>
      <VpBreadcrumbs
        aria-label="Breadcrumb"
        collapsed={collapsed}
        onCollapsedChange={setCollapsed}
      >
        {/* breadcrumb items */}
      </VpBreadcrumbs>
    </>
  );
}
```

**Built-in accessibility features:**

- ✅ **Navigation landmark**: Rendered as `<nav>` element
- ✅ **ARIA attributes**: `aria-current="page"` on current item
- ✅ **Semantic structure**: Uses ordered list internally
- ✅ **Chevron separators**: Automatically added, `aria-hidden`
- ✅ **Collapse functionality**: For long breadcrumb trails

**Accessibility requirements for users:**

- **MUST** provide `aria-label` on `VpBreadcrumbs` (e.g., "Breadcrumb navigation")
- **MUST** mark current page with `isCurrent` prop
- **SHOULD** use `isBrandLink` for brand-specific breadcrumb items
- **CAN** control collapse state with `collapsed` and `onCollapsedChange`
- **CAN** customize collapse trigger with `collapseTriggerLabel`

**Props:**

- `collapsed`: Boolean - whether breadcrumbs are collapsed
- `collapseTriggerLabel`: String - label for the collapse/expand button
- `isCurrent`: Boolean - marks the current page item
- `isBrandLink`: Boolean - styles as brand link

**Vue/Svelte adaptation:**

- **Vue**: Import from `@vtmn-play/vue`
- **Svelte**: Import from `@vtmn-play/svelte`

---

## Pagination Pattern

```tsx
import { VpButton, VpIconButton } from "@vtmn-play/react";
import { VpChevronLeftIcon, VpChevronRightIcon } from "@vtmn-play/icons/react";

interface PaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

function VpPagination({
  currentPage,
  totalPages,
  onPageChange,
}: PaginationProps) {
  const getPageNumbers = () => {
    const pages: (number | string)[] = [];
    const showEllipsis = totalPages > 7;

    if (!showEllipsis) {
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
      }
    } else {
      // Always show first, last, current, and neighbors
      if (currentPage <= 3) {
        pages.push(1, 2, 3, 4, "...", totalPages);
      } else if (currentPage >= totalPages - 2) {
        pages.push(
          1,
          "...",
          totalPages - 3,
          totalPages - 2,
          totalPages - 1,
          totalPages,
        );
      } else {
        pages.push(
          1,
          "...",
          currentPage - 1,
          currentPage,
          currentPage + 1,
          "...",
          totalPages,
        );
      }
    }

    return pages;
  };

  return (
    <nav aria-label="Pagination">
      <ul
        style={{
          display: "flex",
          listStyle: "none",
          padding: 0,
          gap: "0.5rem",
          alignItems: "center",
        }}
      >
        {/* Previous Button */}
        <li>
          <VpIconButton
            onClick={() => onPageChange(currentPage - 1)}
            disabled={currentPage === 1}
            aria-label="Go to previous page"
          >
            <VpChevronLeftIcon />
          </VpIconButton>
        </li>

        {/* Page Numbers */}
        {getPageNumbers().map((page, index) => (
          <li key={index}>
            {page === "..." ? (
              <span style={{ padding: "0.5rem" }}>…</span>
            ) : (
              <VpButton
                onClick={() => onPageChange(page as number)}
                variant={currentPage === page ? "primary" : "secondary"}
                aria-current={currentPage === page ? "page" : undefined}
                aria-label={`Go to page ${page}`}
              >
                {page}
              </VpButton>
            )}
          </li>
        ))}

        {/* Next Button */}
        <li>
          <VpIconButton
            onClick={() => onPageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
            aria-label="Go to next page"
          >
            <VpChevronRightIcon />
          </VpIconButton>
        </li>
      </ul>
    </nav>
  );
}

// Usage
function ProductList() {
  const [currentPage, setCurrentPage] = useState(1);

  return (
    <div>
      {/* Product list here */}
      <VpPagination
        currentPage={currentPage}
        totalPages={10}
        onPageChange={setCurrentPage}
      />
    </div>
  );
}
```

**ARIA attributes:**

- `aria-label="Pagination"` on `<nav>`
- `aria-current="page"` on current page button
- `aria-label` on prev/next buttons
- Disable prev on first page, next on last page

---

## Alert/Banner Pattern

```tsx
import { VpButton } from "@vtmn-play/react";
import {
  VpCheckCircleIcon,
  VpXCircleIcon,
  VpAlertTriangleIcon,
  VpInfoIcon,
  VpXIcon,
} from "@vtmn-play/icons/react";

type AlertType = "success" | "error" | "warning" | "info";

interface AlertProps {
  type: AlertType;
  message: string;
  onClose?: () => void;
}

function VpAlert({ type, message, onClose }: AlertProps) {
  const config = {
    success: {
      icon: VpCheckCircleIcon,
      bg: "var(--vp-semantic-color-background-positive)",
      color: "var(--vp-semantic-color-content-positive)",
      role: "status",
    },
    error: {
      icon: VpXCircleIcon,
      bg: "var(--vp-semantic-color-background-negative)",
      color: "var(--vp-semantic-color-content-negative)",
      role: "alert",
    },
    warning: {
      icon: VpAlertTriangleIcon,
      bg: "var(--vp-semantic-color-background-warning)",
      color: "var(--vp-semantic-color-content-warning)",
      role: "alert",
    },
    info: {
      icon: VpInfoIcon,
      bg: "var(--vp-semantic-color-background-info)",
      color: "var(--vp-semantic-color-content-info)",
      role: "status",
    },
  };

  const { icon: Icon, bg, color, role } = config[type];

  return (
    <div
      role={role}
      aria-live={role === "alert" ? "assertive" : "polite"}
      style={{
        display: "flex",
        alignItems: "center",
        gap: "0.75rem",
        padding: "1rem",
        background: bg,
        color: color,
        borderRadius: "0.5rem",
      }}
    >
      <Icon aria-hidden="true" />
      <span style={{ flex: 1 }}>{message}</span>
      {onClose && (
        <VpButton
          onClick={onClose}
          variant="ghost"
          size="sm"
          aria-label="Dismiss alert"
        >
          <VpXIcon />
        </VpButton>
      )}
    </div>
  );
}

// Usage
function NotificationExample() {
  const [showAlert, setShowAlert] = useState(true);

  return (
    <>
      {showAlert && (
        <VpAlert
          type="success"
          message="Your changes have been saved successfully."
          onClose={() => setShowAlert(false)}
        />
      )}
    </>
  );
}
```

**ARIA attributes:**

- `role="alert"` for errors/warnings (assertive)
- `role="status"` for success/info (polite)
- `aria-live="assertive"` for critical messages
- `aria-live="polite"` for non-critical updates
- Icons are `aria-hidden="true"`

---

## Framework Adaptation

All examples use **React syntax**. Adapt for:

- **Vue**: `@click`, `@keydown`, `v-if`, import from `@vtmn-play/vue`
- **Svelte**: `on:click`, `on:keydown`, `{#if}`, import from `@vtmn-play/svelte`

---

## Testing Checklist

For each pattern:

- [ ] Keyboard navigation works (Tab, Arrow keys, Enter, Escape)
- [ ] Screen reader announces correctly (test with NVDA/VoiceOver)
- [ ] Focus visible at all times
- [ ] ARIA attributes correct (use axe DevTools)
- [ ] Focus trap works (for modals/menus)
- [ ] Focus restoration works (after closing)
- [ ] Works with keyboard only (no mouse)
- [ ] Color contrast passes WCAG AA
- [ ] Semantic tokens used for theming
- [ ] Works in both light and dark modes
