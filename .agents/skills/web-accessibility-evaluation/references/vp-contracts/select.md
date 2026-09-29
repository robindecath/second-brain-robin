# select — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpSelect } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpSelect accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpSelect/ACCESSIBILITY.md).

### Accessible labeling

The select must have an accessible label provided by one of the following: a visible `<label>` with `for` attribute matching the select's `id`, a visible label referenced by `aria-labelledby`, an `aria-label`, or at least a `title` attribute.

### Logical grouping

If multiple selects form a logical group with a visible label, they should be enclosed in an element with `role="group"` that has the property `aria-labelledby` set to the ID of the element containing the group label. Alternatively, use the native `<fieldset>` and `<legend>` elements.

### Connect descriptions

If the component has an associated descriptive text, connect it using the `aria-describedby` attribute set to the ID of the element containing the description.

### Required field indication

Mandatory fields should be clearly marked, either with general text placed prominently before the form or by employing an asterisk in both the visible label and its accessible counterpart.

### Focusable and disabled

VpSelect can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Mark required properties

When the input is marked as `required`, it is important to ensure that the user is aware of this. The label of the input should have an indication of this, such as "(required)". Our `VpFormControl` component will automatically add an asterisk, although it is recommended to override this with a more descriptive text. This can be done with the `requiredIndicator` property/slot. If you are not using `VpFormControl`, make sure to add this indication yourself.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
