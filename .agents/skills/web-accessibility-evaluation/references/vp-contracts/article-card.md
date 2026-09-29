# article-card — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpArticleCard } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpArticleCard accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpArticleCard/ACCESSIBILITY.md).

### Wrap multiple cards in a list

When displaying multiple cards, it is recommended to use lists to enhance assistive technology users' experience. Screen readers provide shortcuts to lists and between list items, and enumerate the items so users know how many items are available.

### Titles go first in semantic order

The order of the elements in the Card is important for screen reader users. The Title should be the first element of the Card, followed by the Label and then the Call to Action. This is because the Title is usually the most important information, and it should be read first. The Label provides additional context, and the Call to Action is the last element that users will interact with. If you want to change this order, you can use CSS to visually rearrange them, but make sure to keep the semantic order intact for screen readers.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
