# toggle — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpToggle } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpToggle accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpToggle/ACCESSIBILITY.md).

### Consistent labeling

The label of the toggle should not change when the state changes. Use the same label text regardless of whether the toggle is on or off.

### Accessible naming

The toggle must have an accessible name provided by a visible label referenced by `aria-labelledby` or an `aria-label` attribute on the element with `role="switch"`.

### Logical grouping

If multiple components form a logical group with a visible label, they should be enclosed in an element with `role="group"` that has `aria-labelledby` set to the ID of the element containing the group label. Alternatively, use the native `<fieldset>` and `<legend>` elements. For example:

```html
<div
  role="group"
  aria-labelledby="id-group-label"
  aria-describedby="id-group-description"
>
  <h3 id="id-group-label">My logical group</h3>
  <p id="id-group-description">
    A beautiful description of why my content is grouped together.
  </p>
  <!-- Your components here -->
</div>
```

### Connect descriptions

If the component has an associated descriptive text, connect it using the `aria-describedby` attribute set to the ID of the element containing the description.

### Focusable and disabled

VpToggle can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Mark required properties

When the input is marked as `required`, it is important to ensure that the user is aware of this. The label of the input should have an indication of this, such as "(required)". Our `VpFormControl` component will automatically add an asterisk, although it is recommended to override this with a more descriptive text. This can be done with the `requiredIndicator` property/slot. If you are not using `VpFormControl`, make sure to add this indication yourself.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
