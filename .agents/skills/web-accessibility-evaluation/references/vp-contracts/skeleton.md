# skeleton — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpSkeleton } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpSkeleton accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpSkeleton/ACCESSIBILITY.md).

### Use in live region

The component should be encapsulated in a loading state by adding the `aria-busy` attribute or putting it inside an `aria-live` region.

```tsx
<div aria-busy="true" aria-live="polite">
  <VpSkeleton />
</div>
```

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
