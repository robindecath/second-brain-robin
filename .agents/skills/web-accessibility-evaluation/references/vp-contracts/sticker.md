# sticker — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpSticker } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpSticker accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpSticker/ACCESSIBILITY.md).

### Provide alternative text for non-visible content

If there is information that are only conveyed through shape, size, or position, please provide an alternative text such as non-visible content, an `aria-label`, or a `title` attribute.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
