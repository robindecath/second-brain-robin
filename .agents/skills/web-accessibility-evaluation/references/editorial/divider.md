# Vitamin Play accessibility guidance — divider (web)

Source: vitamin-play-documentation/src/content/components-accessibility/divider.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Divider component provides these built-in accessibility features out-of-the-box.

          - **Decorative by default**: By default, dividers are purely visual with no screen reader announcement, keeping the accessibility tree clean
          - **Semantic option**: When `isSemantic` is set to true, the divider signals a semantic break with `role="separator"`, allowing screen readers to optionally announce it

## What you need to do

          **Design / Content**
          - **Content grouping:** Use dividers to visually separate distinct sections of content; ensure the content hierarchy is clear through proper semantic structure (headings, lists, etc.)
          - **Visual clarity:** By default, the divider is decorative, so no minimum contrast ratio is required. However, if the divider is made semantic (announced by screen readers), ensure it meets a minimum contrast ratio of 3:1 against the background to comply with accessibility guidelines.

          **Development**
          - **Semantic breaks:** Only set `isSemantic={true}` when the divider represents a meaningful thematic break in content (e.g., between major sections or topics)
          - **Content structure:** Ensure proper semantic HTML structure (headings, sections, articles) to convey hierarchy; dividers should enhance, not replace, semantic structure
          - **Override caution:** If you add `aria-*` attributes or change divider behavior, validate against this doc and re-test with screen readers

## Accessibility attributes

        When `isSemantic` is set to true, the divider:
        - Has `role="separator"` which signals a semantic break between content
        - Appears in the accessibility tree as a separator landmark
        - May be announced by screen readers (e.g., "Horizontal splitter" or "Separator"), though many screen readers choose to ignore it

## Semantic divider usage

            Set `isSemantic={true}` only when the divider signals a meaningful thematic break between content sections. This adds a [semantic separator](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/separator_role) to the [accessibility tree](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree). Screen readers can choose to announce or ignore it.

            **Use semantic dividers for:**
            - Separating major topics in a long article
            - Dividing distinct functional areas (e.g., header from main content)
            - Meaningful thematic breaks in content

            **Don't use semantic dividers for:**
            - Purely visual styling or spacing
            - List items or table rows
            - Repeating UI patterns (creates verbose announcements)

            ```tsx
            // Default: decorative (not announced)

              First paragraph of content...

              Second paragraph of content...

            // Semantic: announced as separator

                Far out in the uncharted backwaters of the 
                unfashionable end of the western spiral arm 
                of the Galaxy lies a small unregarded yellow sun.

                Orbiting this at a distance of roughly 
                ninety-two million miles is an utterly 
                insignificant little blue green planet...

                This planet has - or rather had - a problem, 
                which was this: most of the people on it were 
                unhappy for pretty much of the time.

                And so the problem remained; lots of the 
                people were mean, and most of them were 
                miserable, even the ones with digital watches.

            ```

## Design system guarantees

    ### ARIA & Accessibility Attributes

| **RGAA criterion** | **Requirement**                                                                                | **Responsibilities** |
| ------------ | ---------------------------------------------------------------------------------------------- | :------------------: |
|              | If you set `isSemantic` to true, the `VpDivider` will signal a semantic break between content. | 👥                |

Using Vitamin Play design tokens ensures sufficient contrast ratios, appropriate component sizing, and consistent spacing across all chip variants and platforms. The design system's color and spacing tokens are calibrated to meet WCAG AA standards automatically.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment**    | **React** | **Svelte** | **Vue** |
| ------------------ | :-------: | :--------: | :-----: |
| Firefox + NVDA     | ✅        |            |         |
| IE + JAWS          |           |            |         |
| Safari + VoiceOver | ✅        |            |         |
| Android + TalkBack |           |            |         |
| iOS + VoiceOver    |           |            |         |

## Testing and compliance

The component is tested through:
- [Deque Systems' Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core/tree/master) for compliance with [WCAG Level A & AA rules & accessibility best practices](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)
- Manual testing with NVDA, JAWS, and VoiceOver to ensure proper screen reader behavior
- Verification that decorative dividers don't pollute the accessibility tree
- Validation that semantic dividers are only announced when meaningful

## Sources

- [ARIA: separator role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/separator_role)
- [ARIA Authoring Practices Guide (APG): Separator Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/separator/)
- [RGAA (General Accessibility Improvement Framework, France)](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
- [Accessibility Tree - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree)
