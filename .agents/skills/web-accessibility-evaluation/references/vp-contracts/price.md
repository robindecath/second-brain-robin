# price — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpPrice } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpPrice accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpPrice/ACCESSIBILITY.md).

### Provide alternative text for non-visible content

An alternative text is provided for information that are only conveyed through shape, size, or position, such as a non-visible content, an `aria-label`, or a `title` attribute. For example:

```tsx
<VpPrice>
  <VpPriceAmount variant="sale">3000€</VpPriceAmount>
  <VpPriceAmount variant="barred" aria-label="Former price: 4000€">
    4000€
  </VpPriceAmount>
  <VpPriceDiscount>25% off</VpPriceDiscount>
</VpPrice>
```

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
