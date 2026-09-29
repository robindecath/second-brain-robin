# breadcrumbs — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpBreadcrumbs } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpBreadcrumbs accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpBreadcrumbs/ACCESSIBILITY.md).

### Add a label to the navigation

The Breadcrumbs root element is a navigation landmark region (`<nav>`) that should be labelled via `aria-label` or `aria-labelledby`.

### Mark the current page

The Breadcrumb item representing the current page needs to be marked with the `isCurrent` prop. This way, we can add the `aria-current` property when appropriate.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
