# navigation-header — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpNavigationHeader } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpNavigationHeader accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpNavigationHeader/ACCESSIBILITY.md).

### Differentiate banner elements

The component renders as a `header` element on pages, which has the implicit ARIA role of `banner` as long as it is not a descendant from a `aside`, `article`, `main`, `nav`, or `section`. If your page includes several elements with this role, please differentiate them with a different accessible name (`aria-label`, for example).

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
