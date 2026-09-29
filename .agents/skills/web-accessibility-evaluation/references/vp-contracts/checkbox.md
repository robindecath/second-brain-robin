# checkbox — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpCheckbox } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpCheckbox accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpCheckbox/ACCESSIBILITY.md).

### Accessible label

The Checkbox should have an accessible label. It can be provided by one of the following: a visible text content contained within the element with `role="checkbox"`; a visible label referenced by the value of `aria-labelledby` set on the element with `role="checkbox"`; `aria-label` set on the element with `role="checkbox"`.

```tsx
{/* 1. Using a visible text content */}
<VpCheckbox>Checkbox with a label</VpCheckbox>

{/* 2. Using a visible label referenced by the value of `aria-labelledby` */}
<p id="checkbox-label">Checkbox with aria-labelledby</p>
<VpCheckbox aria-labelledby="checkbox-label" />

{/* 3. Using `aria-label` set on the element */}
<VpCheckbox aria-label="Checkbox with aria-label" />
```

### Grouping checkboxes

If a set of checkboxes is presented as a logical group with a visible label, the Checkboxes are included in an element with `role="group"` that has the property `aria-labelledby` set to the ID of the element containing the label.

```tsx
<div role="group" aria-labelledby="id-group-label">
  <h3 id="id-group-label">My logical group of checkboxes</h3>
  <ul>
    <li>
      <VpCheckbox>Checkbox 1</VpCheckbox>
    </li>
    <li>
      <VpCheckbox>Checkbox 2</VpCheckbox>
    </li>
    <li>
      <VpCheckbox>Checkbox 3</VpCheckbox>
    </li>
    <li>
      <VpCheckbox>Checkbox 4</VpCheckbox>
    </li>
  </ul>
</div>
```

It works with the `fieldset` / `legend` tags as well:

```tsx
<fieldset>
  <legend>My logical group of Checkboxes</legend>
  <ul>
    <li>
      <VpCheckbox>Checkbox 1</VpCheckbox>
    </li>
    <li>
      <VpCheckbox>Checkbox 2</VpCheckbox>
    </li>
    <li>
      <VpCheckbox>Checkbox 3</VpCheckbox>
    </li>
    <li>
      <VpCheckbox>Checkbox 4</VpCheckbox>
    </li>
  </ul>
</fieldset>
```

### Focusable and disabled

VpCheckbox can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Mark required properties

When the input is marked as `required`, it is important to ensure that the user is aware of this. The label of the input should have an indication of this, such as "(required)". Our `VpFormControl` component will automatically add an asterisk, although it is recommended to override this with a more descriptive text. This can be done with the `requiredIndicator` property/slot. If you are not using `VpFormControl`, make sure to add this indication yourself.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
