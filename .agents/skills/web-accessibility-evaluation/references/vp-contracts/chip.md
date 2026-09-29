# chip — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpChip } from "@vtmn-play/react"
```

## Accessibility — Web (ARIA + keyboard)

On web, the Chip component has three distinct variants with different interaction patterns:
- Action Chip - Button-like chips for triggering actions
- Checkbox Chip - Multi-selectable chips for filtering or categorization
- RadioGroup Chip - Single-selection chips for mutually exclusive choices

- Action Chip: Proper `button` or `link` role with keyboard activation support (polymorphic component via `VpPoly`)
- Checkbox Chip: Proper `checkbox` role with checked/unchecked states
- RadioGroup Chip: Proper `radiogroup` and `radio` roles with selection states
- Keyboard navigation: All chip variants respond to appropriate keyboard inputs
- Disabled state: When disabled, chips are neither interactive nor focusable by default
- Native input preservation: For Checkbox and RadioGroup chips, browser native inputs are not fully hidden (not `display: none` or using `sr-only` strategy), maintaining touch-based screen reader navigation and focus interactivity on mobile devices
- Loading states: Action chips support loading state with `aria-busy` and `aria-live` announcements
- Design tokens: Sufficient contrast and appropriate sizing for all chip variants

Development
- Accessible labels: Ensure chips have accessible names via visible text, `aria-label`, or `aria-labelledby`
- Checkbox/Radio groups: Use `role="group"` or `<fieldset>` with proper labels for chip groups
- Descriptions: Use `aria-describedby` for additional context when needed
- Action chip loading: Provide `loadingScreenReaderText` when using loading state
- Form integration: Use `FormControl` component for form-related chip groups
- Required indicators: Replace `*` with explicit "(required)" text
- Disabled state: Consider using `isFocusable` for contextual disabled chips
- Override caution: When overriding with custom `aria-*` attributes, maintain WCAG compliance
- Testing: Verify keyboard navigation and screen reader announcements

The Action Chip component uses a `button` role by default. It can also function as a `link` (`<a>`) thanks to its polymorphic nature (`VpPoly`), in which case it would have a `link` role.

Key attributes:
- Role: `button` or `link` depending on the element used
- Label: Accessible name from text content, `aria-label`, or `aria-labelledby` (must contain visible text per WCAG 2.5.3)
- Description: Optional `aria-describedby` for additional context
- Disabled state: `aria-disabled="true"` when unavailable. When the component is disabled (`disabled` prop set to `true`), it is neither interactive nor focusable by default.
- Loading state: `aria-busy="true"` and `aria-live="polite"` when loading

### Checkbox Chip

The Checkbox Chip component has `role="checkbox"` and manages checked states.

The component rendering is customized by "hiding" the browser native input. However, this native element is not fully removed from the DOM (e.g., `display: none`) nor fully visually removed from the screen's visible bounds (e.g., `sr-only` strategy). This preserves touch-based navigation on mobile devices and maintains proper focus and interactivity.

Key attributes:
- Role: `checkbox`
- Label: Accessible name from text content, `aria-label`, or `aria-labelledby`
- Checked state: `aria-checked="true"` when checked, `"false"` when unchecked
- Mixed state: `aria-checked="mixed"` for tri-state checkboxes
- Disabled state: When disabled, the chip is neither interactive nor focusable by default
- Grouping: Parent `role="group"` with `aria-labelledby` for checkbox groups
- Description: Optional `aria-describedby` for group or individual descriptions

### RadioGroup Chip

The RadioGroup Chip component uses `role="radiogroup"` for the container and `role="radio"` for each item.

The component rendering is customized by "hiding" the browser native input. However, this native element is not fully removed from the DOM (e.g., `display: none`) nor fully visually removed from the screen's visible bounds (e.g., `sr-only` strategy). This preserves touch-based navigation on mobile devices and maintains proper focus and interactivity.

Key attributes:
- Group role: `radiogroup` on the container
- Item role: `radio` on each radio item
- Group label: `aria-label` or `aria-labelledby` on the radiogroup
- Item label: Accessible name from text content, `aria-label`, or `aria-labelledby`
- Checked state: `aria-checked="true"` for selected, `"false"` for unselected
- Disabled state: When disabled, items are neither interactive nor focusable by default
- Description: Optional `aria-describedby` on group or individual radios

table_1[4]{key,action}:
  Tab,Moves focus to the chip (if button role) or to the next focusable element
  Shift + Tab,Moves focus to the previous focusable element
  Enter,Activates the chip (triggers click/navigation)
  Space,Activates the chip (if button role)

Note: When the Action Chip uses a `link` role (via `<a>` element), only Enter activates it. When using `button` role, both Enter and Space activate it.

table_2[3]{key,action}:
  Tab,Moves focus to the first/next checkbox chip
  Shift + Tab,Moves focus to the previous focusable element
  Space,Toggles the checkbox chip's checked state

Note: Checkbox chips do not activate with Enter key, only Space toggles the selection.

table_3[5]{key,action}:
  Tab,"Moves focus into or out of the radio group. Focus goes to the selected radio, or the first radio if none selected"
  Shift + Tab,Moves focus to the previous focusable element
  Arrow Right / Arrow Down,Moves focus to and selects the next radio chip (wraps from last to first)
  Arrow Left / Arrow Up,Moves focus to and selects the previous radio chip (wraps from first to last)
  Space,"If focused radio is not checked, checks it (optional per ARIA APG)"

Navigation patterns:
- Standard (non-toolbar): Arrow keys move focus AND change selection automatically. Only one radio chip in the group can be selected at a time. When moving focus with arrow keys, the previously focused radio is unselected and the newly focused radio is selected.
- Toolbar variant: When a radio group is nested inside a toolbar, users need to navigate among all toolbar elements without changing which radio button is checked. Arrow keys move focus only; Space (or optionally Enter) is required to change selection. This allows keyboard users to explore all options before making a selection.

### Action Chip

The Action Chip's accessible name comes from its text content. For chips with icons only or when additional context is needed, use `aria-label` or `aria-labelledby`. Ensure the visible label is included in the accessible name for WCAG 2.5.3 Label in Name compliance.

```tsx
// Label from text content
<VpActionChip>Filter results</VpActionChip>

// Icon-only chip with aria-label
<VpActionChip aria-label="Close filter">
  <VpIcon name="close" />
</VpActionChip>

// With aria-describedby for additional context
<VpActionChip aria-describedby="chip-desc">
  Apply filters
</VpActionChip>
<span id="chip-desc" className="sr-only">5 filters selected</span>
```

Loading state:

When using the loading state, provide `loadingScreenReaderText` for screen reader users:

```tsx
<VpActionChip
  loading
  loadingScreenReaderText="Adding item to the bag"
>
  Add to bag
</VpActionChip>
```

The component automatically adds `aria-busy="true"` and `aria-live="polite"`. The `loadingScreenReaderText` provides alternative text visible in the DOM but hidden visually, ensuring screen reader users understand the loading action even if CSS is disabled.

### Checkbox Chip

Each Checkbox Chip needs an accessible name from its text content or `aria-label`. When grouping multiple checkbox chips, use `role="group"` or `<fieldset>` with a group label.

```tsx
// Single checkbox chip
<VpCheckboxChip checked={isChecked} onChange={handleChange}>
  Sports
</VpCheckboxChip>

// Group with role="group"
<div role="group" aria-labelledby="categories-label">
  <span id="categories-label" className="form-label">Categories</span>
  <VpCheckboxChip checked={sports} onChange={e => setSports(e.target.checked)}>
    Sports
  </VpCheckboxChip>
  <VpCheckboxChip checked={tech} onChange={e => setTech(e.target.checked)}>
    Technology
  </VpCheckboxChip>
  <VpCheckboxChip checked={fashion} onChange={e => setFashion(e.target.checked)}>
    Fashion
  </VpCheckboxChip>
</div>

// Group with fieldset
<fieldset>
  <legend>Filter by category</legend>
  <VpCheckboxChip checked={outdoor} onChange={e => setOutdoor(e.target.checked)}>
    Outdoor
  </VpCheckboxChip>
  <VpCheckboxChip checked={indoor} onChange={e => setIndoor(e.target.checked)}>
    Indoor
  </VpCheckboxChip>
</fieldset>
```

### RadioGroup Chip

The RadioGroup Chip requires a group label using `aria-label` or `aria-labelledby` on the container with `role="radiogroup"`.

Group label options:

```tsx
{/* Using aria-label on radiogroup */}
<VpRadioGroupChip aria-label="Select size" value={size} onChange={setSize}>
  <VpRadioGroupChip.Item value="s">Small</VpRadioGroupChip.Item>
  <VpRadioGroupChip.Item value="m">Medium</VpRadioGroupChip.Item>
  <VpRadioGroupChip.Item value="l">Large</VpRadioGroupChip.Item>
</VpRadioGroupChip>

{/* Using aria-labelledby referencing visible element */}
<div>
  <span id="size-label" className="form-label">T-shirt size</span>
  <VpRadioGroupChip aria-labelledby="size-label" value={size} onChange={setSize}>
    <VpRadioGroupChip.Item value="xs">XS</VpRadioGroupChip.Item>
    <VpRadioGroupChip.Item value="s">S</VpRadioGroupChip.Item>
    <VpRadioGroupChip.Item value="m">M</VpRadioGroupChip.Item>
    <VpRadioGroupChip.Item value="l">L</VpRadioGroupChip.Item>
    <VpRadioGroupChip.Item value="xl">XL</VpRadioGroupChip.Item>
  </VpRadioGroupChip>
</div>
```

Each radio item needs an accessible name from text content or `aria-label`.

Individual item label options:

```tsx
{/* 1. Visible text content */}
<VpRadioGroupChip.Item value="option1">Option label</VpRadioGroupChip.Item>

{/* 2. Using aria-labelledby */}
<VpRadioGroupChip.Item value="option2" aria-labelledby="option2-label" />
<p id="option2-label">Option with external label</p>

{/* 3. Using aria-label */}
<VpRadioGroupChip.Item value="option3" aria-label="Option with aria-label" />
```

Using aria-describedby for additional context:

```tsx
<p id="group-desc">A global description about the radio group.</p>
<p id="item-desc">A specific description about the first radio input.</p>

<VpRadioGroupChip 
  name="contact" 
  aria-label="Contact method"
  aria-describedby="group-desc"
>
  <VpRadioGroupChip.Item value="email" aria-describedby="item-desc">
    Email
  </VpRadioGroupChip.Item>
  <VpRadioGroupChip.Item value="phone">Phone</VpRadioGroupChip.Item>
  <VpRadioGroupChip.Item value="mail">Mail</VpRadioGroupChip.Item>
</VpRadioGroupChip>
```

### Keyboard interaction

keyboard_interaction[4]{variant,rgaa_criterion,requirement,responsibilities}:
  Action Chip,7.3,The action chip is keyboard accessible and can be activated with Enter or Space (when button role),✅
  Checkbox Chip,7.3,The checkbox chip is keyboard accessible and can be toggled with Space key,✅
  RadioGroup Chip,7.3,"The radio group chip is keyboard accessible with arrow key navigation, Tab key moves focus into/out of the group (focusing selected or first radio), and arrow keys move focus and change selection",✅
  All variants,7.3,Keyboard commands do not rely solely on character keys,✅

### ARIA and accessibility attributes

aria_a11y_attributes[9]{variant,rgaa_criterion,requirement,responsibilities}:
  Action Chip,7.1,"The action chip has `role=""button""` or `role=""link""` depending on the element used, `aria-disabled=""true""` when disabled, and `aria-busy=""true""` with `aria-live` announcements when loading",✅
  Action Chip,7.1,"If additional descriptive text is relevant, the chip has `aria-describedby` set to the description's ID",👥
  Action Chip,11.1,"The action chip has an accessible label provided by visible text content, `aria-label`, or `aria-labelledby`",👥
  Checkbox Chip,7.1,"The checkbox chip has `role=""checkbox""` with `aria-checked` states (""true""/""false""/""mixed"" for checked/unchecked/partially checked)",✅
  Checkbox Chip,7.1,"If checkbox chips are presented as a logical group with a visible label, they are included in an element with `role=""group""` that has `aria-labelledby` set to the label's ID. If additional descriptive text is relevant, the checkbox or group has `aria-describedby` set to the description's ID",👥
  Checkbox Chip,11.1,"The checkbox chip has an accessible label provided by visible text content, `aria-label`, or `aria-labelledby`",👥
  RadioGroup Chip,7.1,"The radio group container has `role=""radiogroup""`, each radio chip has `role=""radio""`, and `aria-checked` states (""true""/""false"" for selected/unselected)",✅
  RadioGroup Chip,7.1,"If additional descriptive text is relevant, the radio group or individual radios have `aria-describedby` set to the description's ID",👥
  RadioGroup Chip,11.1,"The radio group and each radio chip have accessible labels via `aria-label`, `aria-labelledby`, or text content",👥

### Form integration

form_integration[4]{variant,rgaa_criterion,requirement,responsibilities}:
  Checkbox Chip,11.10,"When used with FormControl, error messages are clearly associated with the checkbox chip and announced by screen readers, and helper text is programmatically associated",✅
  Checkbox Chip,11.10,"Required checkbox chips display a clear indicator (preferably ""(required)"" instead of """")",👥
  RadioGroup Chip,11.10,"When used with FormControl, error messages are clearly associated with the radio group and announced by screen readers, and helper text is programmatically associated",✅
  RadioGroup Chip,11.10,"Required radio groups display a clear indicator (preferably ""(required)"" instead of """")",👥

### Visual accessibility

visual_a11y[4]{rgaa_criterion,requirement,responsibilities}:
  3.1,State changes are not conveyed by color alone,✅
  3.2,Chip text and background have sufficient color contrast (4.5:1 minimum),✅
  10.7,Focus indicator is clearly visible with sufficient contrast,✅
  ,Chip is appropriately sized (minimum 44x44px touch target),✅

table_4[3]{environment,action_chip,checkbox_chip,radiogroup_chip}:
  Safari + VoiceOver,✅,✅,✅
  Chrome + NVDA,,,
  Chrome + JAWS,,,

The Vitamin Play Chip component is tested with:

- Deque Systems' Axe Core accessibility testing engine
- Compliance with WCAG 2.1 Level A & AA rules
- ARIA Authoring Practices Guide (APG):
- Action Chip: Button Pattern
- Checkbox Chip: Checkbox Pattern
- RadioGroup Chip: Radio Group Pattern
- RGAA - French Accessibility Guidelines

- MDN: ARIA: button role
- MDN: ARIA: checkbox role
- MDN: ARIA: radio role
- MDN: ARIA: radiogroup role
