# text-input — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpTextInput } from "@vtmn-play/react"
```

## Accessibility

Search terms: VpInput label, VpFormControl, VpFormLabel, accessible label
association, input label association.

All accessibility features and expected behaviors are described in the [VpInput accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpInput/ACCESSIBILITY.md).

### Accessible label

The Input should have an accessible label. If you are not using `VpFormControl`, it can be provided by one of the following: a visible and close label element using the `for` attribute on the label that corresponds to the input's `id` attribute ; a visible label referenced by the value of `aria-labelledby`; an `aria-label` or at least a `title`.

```tsx
{/* 1. Using a visible text content */}
<label for="my-input-id">Purpose of my Input</label>
<VpInput id="my-input-id" />

{/* 2. Using a visible label referenced by the value of `aria-labelledby` */}
<p id="my-input-label">Input with aria-labelledby</p>
<VpInput labelId="my-input-label" />

{/* 3. Using `aria-label` set on the element */}
<VpInput fieldSlot={<VpInputField aria-label="my-input-label"/>} />
```

### Grouping checkboxes

If a set of Input is presented as a logical group with a visible label, the Inputs are included in an element with `role="group"` that has the property `aria-labelledby` set to the ID of the element containing the label.

```tsx
<div role="group" aria-labelledby="id-group-label">
  <h3 id="id-group-label">My logical group of Inputs</h3>
  <div>
    <label for="shipping-name">Shipping Name:</label>
    <VpInput name="shipping-name" id="shipping-name" />
  </div>
  <div>
    <label for="billing_head">Billing Name:</label>
    <VpInput name="billing_head" id="billing_head" />
  </div>
</div>
```

It works with the `fieldset` / `legend` tags as well:

```tsx
<fieldset>
  <legend>My logical group of Inputs</legend>
  <div>
    <label for="shipping-name">Shipping Name:</label>
    <VpInput name="shipping-name" id="shipping-name" />
  </div>
  <div>
    <label for="billing_head">Billing Name:</label>
    <VpInput name="billing_head" id="billing_head" />
  </div>
</fieldset>
```

### Connect descriptions

If the component has an associated descriptive text, connect it using the `aria-describedby` attribute set to the ID of the element containing the description.

### Focusable and disabled

VpInput can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Mark required properties

When the input is marked as `required`, it is important to ensure that the user is aware of this. The label of the input should have an indication of this, such as "(required)". Our `VpFormControl` component will automatically add an asterisk, although it is recommended to override this with a more descriptive text. This can be done with the `requiredIndicator` property/slot. If you are not using `VpFormControl`, make sure to add this indication yourself.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
