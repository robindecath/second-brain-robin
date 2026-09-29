# Deliverable — User Journey

**For:** cross-functional teams that need a shared, evidence-backed view of the experience over time.
**Guard:** a journey is one of the easiest artefacts to fabricate. Every stage, emotion, and pain point must trace to a finding.

---

## Scoping questions

1. **Whose journey?** One actor per journey. A journey that averages two segments describes neither. If segments diverge, produce two journeys or one with an explicit divergence band.
2. **Which journey?** End-to-end lifecycle, a single task, or a service episode. Name the start and end trigger.
3. **Current or future state?** Current state is evidence. Future state is design — mark it as such and never interleave the two in one row.

---

## Structure

Stages across the top, lanes down the side.

| Lane | Content | Source |
|---|---|---|
| **Stage** | Named in the user's language where possible, not internal funnel names | Qual |
| **Goal** | What the user is trying to achieve here | Qual |
| **Actions** | What they actually do | Qual + analytics |
| **Touchpoints** | Channels, surfaces, people, documents | Qual + analytics |
| **Thinking** | Mental model, expectations, questions | Qual |
| **Feeling** | Emotional trajectory, with evidence per point | Qual |
| **Pain points** | Frictions, with severity and frequency | Qual + quant |
| **Moments of truth** | Where the relationship is won or lost | Triangulated |
| **Evidence** | Citation row — IDs for everything above | All |
| **Opportunities** | Where intervention is possible → feeds HMW / OST | Derived |

The evidence row is a lane, not a footnote. If a cell above it is populated and its evidence cell is empty, the cell is an assumption and must be marked.

---

## Rules

- **Stage names come from participants.** If users call it "waiting to hear back", don't call it "Review SLA".
- **Emotion curves need evidence per plotted point.** An emotion line drawn to look like a satisfying dip and recovery is illustration, not research. Where emotion is inferred from behaviour rather than stated, mark it.
- **Pain points carry severity and frequency separately.** A minor irritant hitting everyone and a blocker hitting a few are different problems with different fixes.
- **Backstage matters.** Where internal process causes user-facing friction, include it; otherwise the journey proposes fixes at the wrong layer.
- **Non-linear reality.** Real journeys loop, stall, and abandon. Show loops and exits rather than forcing a clean left-to-right line.
- **Variant paths get shown, not averaged.** Per the [challenger audit](../references/challenger-audit.md), the minority path is drawn — as a branch, a band, or a second row.

---

## Stage template

```
STAGE 04 · "Working out what it'll cost me"
Trigger        Reached payment step
Goal           Confirm the total before committing
Actions        Scroll up to re-check items; open pricing page in new tab; abandon
               [P02, P05, P07, P11] [EVT:checkout_back_nav 41% of abandons]
Thinking       "There's probably a fee they haven't shown me"        [P07:24:55]
Feeling        Suspicion → withdrawal    (stated, 4 participants; inferred for 3 via re-scroll)
Pain point     Total not visible pre-commit
               Severity HIGH · Frequency 7/12 qual, 34% survey  [SURVEY:Q14]
Variant        Returning users with saved payment pass through unaffected [P09:12:30]
Moment of truth  Yes — trust decision point
Opportunity    Itemised total before commit → HMW-04, O-02
Confidence     HIGH (bounded: consumer tier, new users)
```

---

## Do not

- Do not invent stages to complete a symmetrical arc.
- Do not smooth the emotion line for visual appeal.
- Do not merge two segments' journeys into one composite actor.
- Do not include a stage with no evidence unless it is explicitly marked as an assumption to be validated.
- Do not present a future-state journey in the same visual language as a current-state one.
