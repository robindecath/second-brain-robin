# badge — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpBadge } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpBadge accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpBadge/ACCESSIBILITY.md).

### Supply contextual information

Most of the time, the content of the badge is understood through its context. For example, a badge on a button or an icon can be understood as a notification, except for when it is a shopping cart, where it indicates the number of items in the cart. This information is usually visual, so it is necessary to make the same context available through alternative text, such as non-visible content, an `aria-label`, or a `title` attribute.

### Describe an empty Badge

When Badge is empty, please provide an alternative text, such as a non-visible content, an `aria-label`, or a `title` attribute.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
