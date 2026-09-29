# score-rating — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpScoreRating } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpScoreRating accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpScoreRating/ACCESSIBILITY.md).

### Alternative text

The component is considered as an image by assistive technologies. If no context is given while using this component (for instance if it is not used in a Product Card or if it not introduced in a titled section), provide an alternative text with an `aria-label` attribute.

### Explicit score context

When using the component standalone, ensure that the Score is understandable as such, and that its meaning is not only conveyed through the Icon shape.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
