# modal — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpModal } from "@vtmn-play/react"
```

## Accessibility

Search terms: VpModal contract, modal accessible name, aria-label dialog,
aria-labelledby visible title.

All accessibility features and expected behaviors are described in the [VpModal accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpDialog/VpModal/ACCESSIBILITY.md).

### Dialog elements

All elements required to operate the dialog must be descendants of the element that has role `dialog`. They should be structured with sub-components for header, body, and footer.

### Dialog labeling

The dialog must have either a value set for the `aria-labelledby` property that refers to a visible dialog title, or a label specified by `aria-label`.

### Content accessibility

Content within the Modal header, body and footer must be accessible, including proper use of headings, readable text, and meaningful descriptions for images and interactive elements. Maintain a logical reading order for screen readers by structuring the content appropriately.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
