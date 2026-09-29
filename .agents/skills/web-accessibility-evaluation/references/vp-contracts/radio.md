# radio — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpRadio } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpRadioGroup accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpRadioGroup/ACCESSIBILITY.md).

### Items should have accessible labels

Each RadioGroup Item should have an accessible label provided by one of the following: a visible text content contained within the element with `role="radio"`; a visible label referenced by the value of `aria-labelledby` set on the element with `role="radio"`; `aria-label` set on the element with `role="radio"`.

```tsx
{/* 1. Using a visible text content */}
<VpRadioGroupItem>RadioGroup Item with a label</VpRadioGroupItem>

{/* 2. Using a visible label referenced by the value of `aria-labelledby` */}
<VpRadioGroupItem aria-labelledby="radio-item-label" />
<p id="radio-item-label">RadioGroup Item with aria-labelledby</p>

{/* 3. Using `aria-label` set on the element */}
<VpRadioGroupItem aria-label="RadioGroup Item with aria-label" />
```

### Label for the group

When not using the `VpFormControl`, make sure that the radiogroup element has a visible label referenced by `aria-labelledby` or has a label specified with `aria-label`.

```tsx
{
  /* 1. Using a visible label referenced by the value of `aria-labelledby` */
}
<VpRadioGroup aria-labelledby="radio-group-label">
  <h4 id="radio-group-label">RadioGroup with aria-labelledby</h4>
  {/* ... */}
</VpRadioGroup>;

{
  /* 2. Using `aria-label` set on the element */
}
<VpRadioGroup aria-label="RadioGroup with aria-label">
  {/* ... */}
</VpRadioGroup>;
```

When using the `VpFormControl`, make sure to use the `fieldset` property of it to define a correct semantic block for the input. Avoiding this setting can break the way label and interactions works on the radiogroup element.

```tsx
<VpFormControl fieldset>
  <VpFormLabel>Legend of the control</VpFormLabel>
  <VpRadioGroup {...props}>
    <VpRadioGroupItem value="..."> ... </VpRadioGroupItem>
    {/* ... */}
  </VpRadioGroup>
</VpFormControl>
```

### Connect descriptions

If the component has an associated descriptive text, connect it using the `aria-describedby` attribute set to the ID of the element containing the description.

### Focusable and disabled

VpRadioGroupItem and VpRadioGroup can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Mark required properties

When the input is marked as `required`, it is important to ensure that the user is aware of this. The label of the input should have an indication of this, such as "(required)". Our `VpFormControl` component will automatically add an asterisk, although it is recommended to override this with a more descriptive text. This can be done with the `requiredIndicator` property/slot. If you are not using `VpFormControl`, make sure to add this indication yourself.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
