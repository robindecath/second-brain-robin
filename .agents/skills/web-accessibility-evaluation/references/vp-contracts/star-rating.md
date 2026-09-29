# star-rating — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpStarRating } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpStarRating accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpStarRating/ACCESSIBILITY.md).

### Alternative text

Please provide an alternative text for information that are only conveyed through shape, size, or position, such as a non-visible content, an `aria-label`, or a `title` attribute.

### Visual representation

The component uses star icons to visually represent a score. Make sure this visual representation is accompanied by an accessible label that conveys the same information.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
