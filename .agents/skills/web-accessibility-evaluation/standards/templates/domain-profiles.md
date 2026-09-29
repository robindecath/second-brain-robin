# Domain Profiles (Additive Coverage Extensions)

**Purpose**: Extend the universal coverage matrix with domain-specific controls, while keeping all core checks mandatory.

Profiles are derived from an analysis of the 100 most recently updated repositories in the `dktunited` GitHub organisation (as of April 2026). Each profile maps to one or more actual product surfaces built at Decathlon.

## Governance Rule

- Always complete the RGAA 4.1 audit grid (`./rgaa-audit-template.md`) first.
- Domain profile checks are **additive**.
- Never replace or skip RGAA criteria because a profile is used.
- A single product may use more than one profile (e.g. a circularity app uses both E-commerce and Editorial).

---

## E-commerce Profile

**Applies to:** customer-facing purchase flows, checkout, gifting, post-purchase engagement, circular economy (second-hand, rental, repair).

Add checks for:

- Price/discount semantics and non-color communication (promo badges, club prices, strikethrough prices must use `<del>`/`<ins>` or `aria-label` in addition to visual styling)
- Price display must not rely on visual formatting alone — screen readers must announce original price, discount, and final price clearly (e.g., via `aria-label` on the price block or structured `<del>`/`<ins>`)
- Cart and subtotal announcements after quantity changes (`aria-live="polite"` on cart region, not just a visual update)
- Coupon and loyalty code flows: error messages linked to input via `aria-describedby`, success persistence in live region
- Delivery, returns and circularity status (product condition for second-hand): communicated in text, not colour alone
- Checkout constraints: session timers with visible countdown + keyboard-accessible extension control; payment fallback paths clearly labelled
- Rental and reservation calendars: fully keyboard-navigable date pickers with explicit temporal labels (`aria-label` on each day cell)
- Multi-step forms (deposit, return, repair booking): focus restored to correct position on step transitions, step progress announced
- Product image `alt` must not be empty when image is informative — fallback to product name if no specific alt text is provided by CMS
- "See more" / "View" / "Learn more" links must have unique accessible names per destination (e.g., `aria-label="View Mountain Bike 500"` not just "View")
- Rating/review widgets must label individual bars/stars — each `role="meter"` element needs an `aria-label` describing what it represents (see `patterns/meter-progressbar.md`)
- Product comparison tables: header cells must use `scope="col"` or `scope="row"`; comparison attributes must be announced in context

---

## SaaS / Dashboard Profile

**Applies to:** internal back-offices, operational dashboards, CRC tools, logistics management, supply chain, AI analytics surfaces.

Add checks for:

- Dense tables/grids: `<th scope>` on all header cells; sticky headers remain programmatically associated with their columns; bulk selection state announced (`aria-selected`, live region for count)
- Data refresh and live widgets: announcements via `aria-live` on refresh; focus does not move unexpectedly after auto-update
- Keyboard alternatives for chart interactions: every visualisation must have either a keyboard-navigable interactive layer or a full data table/CSV alternative
- AI-generated content (narrative summaries, chatbot responses): exposed as HTML text, not canvas or image; streaming responses announced via live region at start and end without over-soliciting screen readers
- Conversational interfaces (`loggy`): message history navigable by keyboard (arrow keys); focus sent to latest response; session context preserved on cancel
- Permission/role error messaging: specific, not generic ("You don't have access to this report" rather than "Error 403")
- Accessible filtering, sorting and pinning workflows: active filter state persists and is announced on focus; sort direction communicated via `aria-sort`

---

## Editorial / Media Profile

**Applies to:** product content, sport editorial, AI-generated narratives, Tableau extensions with textual output.

Add checks for:

- Captions, transcripts, audio descriptions for any embedded video or audio content
- Reading mode consistency: heading hierarchy (`h1` → `h2` → `h3`) never skipped; landmark regions present
- Carousel and editorial card controls: pause/stop/resume always accessible; auto-play disabled by default or controllable
- Link purpose in editorial cards and "read more" blocks: never bare "read more" — always supplemented with `aria-label` or visually hidden context
- AI-generated narrative content: must be rendered as accessible HTML; if content updates dynamically, update is announced via live region
- Media player keyboard operability: all controls reachable and operable by keyboard; current position and total duration announced on focus

---

## Mobile Native Profile

**Applies to:** any native Android and iOS applications.

Add checks for:

- TalkBack readability: all interactive elements have a non-empty, meaningful `contentDescription`; decorative elements marked as not important for accessibility
- Touch target sizing: minimum 48×48 dp on all actionable elements, including icon-only buttons and list item actions
- Colour contrast in all active themes: verify both light and dark mode; `instore-android` used in high-ambient-light warehouse environments requires elevated contrast ratio (≥ 7:1 recommended for body text)
- Real-time sport metrics (`csp-decathlon-ride-android-app`): streaming data (speed, cadence, heart rate) exposed via `AccessibilityEvent` or `LiveRegion` at a reasonable announcement rate (not every second)
- Camera/sensor alternative paths: any feature gated on camera (barcode scan, label photo) must offer a manual text entry fallback for users with limited dexterity
- Multi-step flows (session setup, device pairing): focus order follows visual order; each step title announced on navigation; back action does not unexpectedly reset progress
- Notifications and alerts: critical operational alerts use appropriate notification importance level and include actionable text

---

## Authentication / Identity Profile

**Applies to:** any surface with sign-in, account creation, MFA, session management or recovery flows.

Add checks for:

- MFA fallback accessibility: alternative authentication method always offered and reachable without pointer
- Recovery path discoverability: "Forgot password" / "Lost access to authenticator" links visible before and after failed attempt, not only on error
- Session timeout warnings: visible countdown with keyboard-accessible "Extend session" action; warning announced via live region before timeout
- Error handling for failed sign-in: message linked to the triggering field via `aria-describedby`; never clears password field without announcement
- CAPTCHA alternatives: audio CAPTCHA available; or offer support contact escalation path if CAPTCHA is inaccessible

---

## Report Extension Block

When a profile is used, append to the audit report:

- `Profile used: <name>`
- `Profile checks evaluated: <count>`
- `Profile fails: <count>`
- `Profile runtime required: <count>`
