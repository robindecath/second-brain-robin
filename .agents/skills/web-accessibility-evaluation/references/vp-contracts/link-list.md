# link-list — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpLinkList } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpLinkList accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpLinkList/ACCESSIBILITY.md).

### Ensure an accessible name

The List Item Link has an accessible label. By default, the accessible name is computed from any text content inside the link element. However, it can also be provided with `aria-labelledby` or `aria-label`. Note that [the accessible name should always be containing the text that is presented visually](https://www.w3.org/TR/WCAG22/#label-in-name).

### Connect descriptions

If the component has an associated descriptive text, connect it using the `aria-describedby` attribute set to the ID of the element containing the description.

### Focusable and disabled

VpLinkListItem can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
