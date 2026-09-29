# divider — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpDivider } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpDivider accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpDivider/ACCESSIBILITY.md).

### Semantic separation

If you set `isSemantic` to true, the `VpDivider` will signal a semantic break between content by using the `hr` element. The effect on the browser's [accessibility tree](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree) will be that there will be a [semantic separator](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/separator_role) added to the tree. Screen readers can choose to announce or ignore it.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
