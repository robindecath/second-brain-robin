# quantity-input — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpQuantityInput } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpInputQuantity accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpInputQuantity/ACCESSIBILITY.md).

### Accessible label

The Input Quantity should have an accessible label. If you are not using `VpFormControl`, it can be provided by one of the following: a visible and close label element using the `for` attribute on the label that corresponds to the input's `id` attribute ; a visible label referenced by the value of `aria-labelledby`; an `aria-label` or at least a `title`.

```tsx
{/* 1. Using a visible text content */}
<label for="my-input-id">Purpose of my Input</label>
<VpInputQuantity id="my-input-id" />

{/* 2. Using a visible label referenced by the value of `aria-labelledby` */}
<p id="my-input-label">Input with aria-labelledby</p>
<VpInputQuantity labelId="my-input-label" />

{/* 3. Using `aria-label` set on the element */}
<VpInputQuantity fieldSlot={<VpInputField aria-label="my-input-label"/>} />
```

### Grouping inputs

If a set of Input Quantity is presented as a logical group with a visible label, the inputs are included in an element with `role group` that has the property `aria-labelledby` set to the ID of the element containing the label.

```tsx
<div role="group" aria-labelledby="id-group-label">
  <h3 id="id-group-label">My logical group of Inputs</h3>
  <div>
    <label for="shipping-name">Shipping Name:</label>
    <VpInputQuantity name="shipping-name" id="shipping-name" />
  </div>
  <div>
    <label for="billing_head">Billing Name:</label>
    <VpInputQuantity name="billing_head" id="billing_head" />
  </div>
</div>
```

It works with the `fieldset` / `legend` tags as well:

```tsx
<fieldset>
  <legend>My logical group of Inputs</legend>
  <div>
    <label for="shipping-name">Shipping Name:</label>
    <VpInputQuantity name="shipping-name" id="shipping-name" />
  </div>
  <div>
    <label for="billing_head">Billing Name:</label>
    <VpInputQuantity name="billing_head" id="billing_head" />
  </div>
</fieldset>
```

### Descriptive context

If the presentation includes additional descriptive static text relevant to an Input Quantity or group, the Input Quantity or group has the property `aria-describedby` set to the ID of the element containing the description.

```tsx
<div
  role="group"
  aria-labelledby="id-group-label"
  aria-describedby="id-group-description"
>
  <h3 id="id-group-label">My logical group of Inputs</h3>
  <p id="id-group-description">
    A beautiful description of why my Inputs are grouped together.
  </p>
  <div>
    <label for="shipping-name">Shipping Name:</label>
    <VpInputQuantity name="shipping-name" id="shipping-name" />
  </div>
  <div>
    <label for="billing_head">Billing Name:</label>
    <VpInputQuantity name="billing_head" id="billing_head" />
  </div>
</div>
```

### Understable value text

If the value of `aria-valuenow` is not user-friendly, e.g., the day of the week is represented by a number, the `aria-valuetext` property is set on the Input Quantity element to a string that makes the Input Quantity value understandable.

```tsx
<VpInputQuantity
  name="section-count"
  value={1}
  fieldSlot={<VpInputField aria-valuetext="First section" />}
/>
```

### Out of range values

The Input Quantity element has `aria-invalid` set to `true` if the value is outside the allowed range. Note that in our implementation, we prevent input of invalid values, but in some scenarios, blocking all invalid input may not be practical.

### Button labels

The increment and decrement buttons have descriptive `aria-label` attributes to ensure screen reader users understand their function ("Decrease/increase value"). If you want, you can customize these labels by rendering your own buttons via the `startSlot` and `endSlot` props.

```tsx
<VpInputQuantity
  startSlot={
    <VpInputQuantityStartButton aria-label="Decrease value">
      <VpSubtractIcon />
    </VpInputQuantityStartButton>
  }
  endSlot={
    <VpInputQuantityEndButton aria-label="Increase value">
      <VpAddIcon />
    </VpInputQuantityEndButton>
  }
/>
```

### Focusable and disabled

VpInputQuantity can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Mark required properties

When the input is marked as `required`, it is important to ensure that the user is aware of this. The label of the input should have an indication of this, such as "(required)". Our `VpFormControl` component will automatically add an asterisk, although it is recommended to override this with a more descriptive text. This can be done with the `requiredIndicator` property/slot. If you are not using `VpFormControl`, make sure to add this indication yourself.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
