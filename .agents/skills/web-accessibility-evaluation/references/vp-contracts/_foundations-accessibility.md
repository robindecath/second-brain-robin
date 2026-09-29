# Accessibility — Vitamin Play Design System

## What is digital accessibility?

Digital accessibility aims to ensure access to digital services and products without any form of discrimination, regardless of the ability of their users. It focuses on removing barriers so that people with long-term physical, mental, intellectual, or sensory impairments can navigate, understand, and interact with a user interface to fully enjoy their rights and fundamental freedoms on an equal basis with others.

## Digital accessibility at Decathlon

As part of its core mission to **make sports accessible to everyone**, Decathlon treats digital accessibility as a natural extension of this commitment. This is not just a technical obligation but a deep conviction embedded in Decathlon's DNA.

The Decathlon Design System is committed to following and complying with digital accessibility best practices standards:

- **RGAA** (France's national web accessibility framework, aligned with WCAG) for web
- **RAAM** (Mobile App Accessibility Assessment Framework) for mobile
- **WCAG 2.2** (Web Content Accessibility Guidelines) as the international reference

The system was audited in March 2022 (Vitamin) and December 2024 (Vitamin Play). After several fixes, **100% compliance across all platforms** has been reached.

## The four principles of accessibility (POUR)

All content must be:

1. **Perceivable** — Cannot be invisible to all of a user's senses. Provide text alternatives, captions, sufficient contrast.
2. **Operable** — Interface cannot require interaction that a user cannot perform. Support keyboard, voice, switch access.
3. **Understandable** — Content or operation cannot be beyond their understanding. Use plain language, predictable navigation.
4. **Robust** — Users must be able to access the content as technologies advance. Use semantic HTML, valid ARIA.

## Accessibility is a shared responsibility

The design system provides components with accessible foundations that meet around twenty criteria from the RGAA and RAAM standards. However, when these components are used with real content, product teams must ensure many additional criteria that cannot be checked out of context.

### What the design system guarantees

- Color contrast compliance
- Keyboard operability of all components
- Correct ARIA roles and semantics
- Focus visibility and management
- Screen reader compatibility
- Icons hidden from accessibility tree (require explicit labeling)

### What product teams must provide

- Meaningful labels (text or aria-label)
- Correct semantic usage (actions vs navigation)
- Logical tab order in the page context
- Dynamic state management (disabled, expanded, pressed)
- Communicating state changes via ARIA attributes
- Alternative text for images and media
- Proper heading hierarchy (H1→H2→H3)
- Content language declarations

Each component in Vitamin Play includes a dedicated **Accessibility** tab documenting ARIA requirements, keyboard patterns, screen reader announcements, focus management, and testing procedures.

## Best practices

### For blind users (structure)

- **Heading hierarchy**: Start with a single H1, then use descending levels (H2→H3→H4) without skipping.
- **Semantic landmarks**: Use `<header>`, `<nav>`, `<main>`, `<footer>` to define major page regions.
- **Logical reading sequence**: DOM order must match visual order and functional intent.
- **Alternative text**: Every non-decorative image and interactive element must have meaningful alternative text or an accessible name.

### For low vision users (visual perception)

- **Text resizing**: Allow text to reflow/wrap without truncation when zoomed to 200%.
- **Contrast**: Provide a uniform dark overlay under text over imagery to guarantee 4.5:1 contrast.
- **Responsiveness**: Support 320px width & 400% zoom with no horizontal scrolling for primary content.

### For colorblind users (colors)

- **Never use color alone**: Always pair color with text, icons, or patterns to convey meaning.

### For motor disabilities (interaction & keyboard)

- **Focus order**: Tab sequence must follow functional and visual progression.
- **Touch target sizes**: Buttons ≥ 44×44px; inline links ≥ 24×24px.
- **No time limits**: Allow users to complete actions without time pressure.

### For cognitive disabilities (persistence & clarity)

- **Consistent layout**: Keep necessary guidance visible during input.
- **Plain language**: Use short sentences (10–15 words), active voice, common vocabulary.
- **Predictable navigation**: Persistent elements, no unexpected visual shifts.

## Content accessibility

| What               | Who benefits               | Key requirements                                        |
| :----------------- | :------------------------- | :------------------------------------------------------ |
| **Plain language** | Everyone                   | 10-15 word sentences, active voice, common vocabulary   |
| **Link text**      | Screen reader users        | Descriptive links that make sense out of context        |
| **Media**          | Deaf/hard of hearing       | Synchronized captions & transcripts for all video/audio |
| **Structure**      | Dyslexic & cognitive users | Clear headings, short paragraphs, no justified text     |
| **Easy-to-read**   | Cognitive disabilities     | Single idea per sentence, bullet lists, visual aids     |
| **Alt text**       | Blind users                | Concise, descriptive, functional text for all images    |

## Testing accessibility

### Screen reader testing

The most critical manual method. Validate:

- Reading and focus order is logical
- Controls are properly named
- A user can complete an entire task without confusion

Recommended combinations:

- **Web Desktop**: Firefox + NVDA (Windows), Edge + JAWS (Windows), Safari + VoiceOver (macOS)
- **Mobile**: Android + TalkBack, iOS + VoiceOver

### Inspecting the accessibility tree

Use browser DevTools to check:

- **Role**: Does the element have the correct role (button, link, heading)?
- **Name**: Does it have the expected accessible name?
- **State**: Is its current state correct (checked, expanded, disabled)?

### Automated testing

Use tools like Lighthouse or Axe in your CI/CD pipeline to catch 30–40% of common issues (contrast failures, missing alt attributes, improper ARIA roles). Automated tests complement but never replace manual testing.

### Audits

- **Internal audits**: Performed by Decathlon's Accessibility SIG before major launches.
- **External audits**: Performed by specialized third-party companies for certification.
- Contact <digitalaccessibility@decathlon.com> for guidance.

### Testing with disabled users

The ultimate test. Observe real users with their own assistive technologies attempting key tasks on your product. This reveals practical problems that no compliance audit can detect.

## Standards and references

| Standard       | Scope                                      | Link                                                                                        |
| :------------- | :----------------------------------------- | :------------------------------------------------------------------------------------------ |
| **WCAG 2.2**   | Web applications, websites, mobile web     | <https://www.w3.org/TR/WCAG22/>                                                               |
| **RGAA**       | French national standard (based on WCAG)   | <https://accessibilite.numerique.gouv.fr/>                                                    |
| **RAAM**       | Mobile app accessibility (iOS and Android) | <https://accessibilite.public.lu/en/raam1.1/index.html>                                       |
| **EN 301 549** | European ICT accessibility standard        | <https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf> |

## Platform-specific guides

- **Web**: Component-level accessibility, ARIA patterns, keyboard navigation, screen reader testing → <https://github.com/dktunited/vitamin-play-web/blob/main/ACCESSIBILITY_RESOURCES.md>
- **iOS**: VoiceOver support, Dynamic Type, Voice Control, Switch Control → Apple Human Interface Guidelines
- **Android**: TalkBack support, touch target sizes, content descriptions, Accessibility Scanner → Android Accessibility Guide

## Tools

- **Automated scanners**: Integrate into CI/CD for continuous monitoring (Lighthouse, Axe, Pa11y).
- **Manual audit assistants**: Screen readers, contrast checkers, accessibility tree inspectors.
- **Decision tree**: Use the Accessibility SIG's decision tree to select appropriate tools for your context.

## Self-audit templates

- **Web audit template (RGAA/WCAG)**: For auditing web-based products and services.
- **Mobile audit template (RAAM/WCAG)**: For auditing iOS/Android mobile apps.

## Need help?

- **Accessibility SIG**: The Special Interest Group maintains guidelines and provides support. Contact via Slack #digital-accessibility or the SIG wiki.
- **Email**: <digitalaccessibility@decathlon.com>
