# search — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpSearch } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpSearch accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpSearch/ACCESSIBILITY.md).

### Semantic labeling

It is recommended to add a semantic label to the search input field by using the `aria-label` or `aria-labelledby` attribute.

### Modal search accessibility

When using the modal variation, an accessible description must be provided to the dialog with the `aria-label` property on the root. If not provided, "Search" will be used as default.

### Cancel button labeling

The cancel button needs an accessible label, as it cannot be derived from the inner content. Set this by passing the `cancelAriaLabel` property. If not provided, "Cancel" will be used as default.

### Focusable and disabled

VpSearch can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
