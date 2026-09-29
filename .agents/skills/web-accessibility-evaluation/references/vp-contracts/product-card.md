# product-card — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpProductCard } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpProductCard accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpProductCard/ACCESSIBILITY.md).

### Card accessibility

If the image inside the card is decorational and does not provide any additional context, it should have an empty alt text. This signals to screenreaders that it is a decorative image. If you use the `mediaSrc` prop, this behavior is automatic.

### Action element naming

The product card's action element should have a relevant accessible name (either with an explicit visual label or a relevant `aria-label`).

### Multiple cards usage

When displaying multiple cards, it is recommended to use lists to enhance assistive technology users' experience: screen readers provide shortcuts to lists and between list items, and enumerate the items so users know how many are available.

### Reviews accessibility

The `VpProductCardReviews` component uses the `VpScoreRating` component for displaying the average score of the reviews, and defines the whole component as an image (`role="image"`) that needs an accessible label. You can make sure its content is understandable by using the `VpProductCardReviews` component with a relevant `aria-label`.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
