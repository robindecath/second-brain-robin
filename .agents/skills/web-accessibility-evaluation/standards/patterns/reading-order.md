# Reading Order

## Overview

Reading order (also called traversal order or content sequence) defines the order in which assistive technologies encounter content. It must convey the same meaning and relationships as the visual presentation. (WCAG 1.3.2)

## The Core Problem

Visual layout and AT traversal order can diverge when:
- **CSS reordering**: `order`, `flex-direction: row-reverse`, `position: absolute` place elements visually out of DOM order
- **Platform layout engines**: SwiftUI stacks, Android ConstraintLayout, CSS Grid may render elements in an order different from the source
- **Tab index manipulation**: `tabindex > 0` values create an artificial keyboard order disconnected from visual flow

**Rule**: The reading sequence must not depend on visual presentation alone.

## What Must Be Preserved

- Headings appear before the content they describe
- Labels appear before (or clearly associated with) their controls
- Error messages are near the fields they reference
- Contextual actions appear after the content they act on
- List items flow in a logical order (chronological, alphabetical, hierarchical)

## When to Override Default Order

Override only when the default platform order does not match reading intent:
- **Web**: CSS `order` must never create a mismatch — change DOM order instead
- **iOS**: Use `.accessibilitySortPriority()` sparingly for complex custom layouts
- **Android**: Use `android:accessibilityTraversalBefore/After` for ConstraintLayout exceptions

## Platform Implementation

See your platform skill for implementation details:
- **Web**: DOM source order drives tab and screen reader order — avoid CSS-only reordering
- **iOS**: `../../references/references/reading-order.md` — `.accessibilitySortPriority()`
- **Android**: `../../references/references/compose-semantics.md` — traversal order APIs

## Resources

- WCAG 1.3.2 Meaningful Sequence: <https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence>
- ARIA in HTML — Focus Order: <https://www.w3.org/TR/html-aria/>
