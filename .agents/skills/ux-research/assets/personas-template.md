# Deliverable — Personas

**For:** teams needing a shared, evidence-based model of who they serve.
**Guard:** personas are the artefact most likely to become fiction. Every attribute traces to evidence or is removed.

---

## Precondition

Personas require enough evidence to distinguish groups. Before producing any:

- Fewer than ~8 qualitative sessions, or no segmentable quant → do **not** produce personas. Produce a [JTBD set](jtbd-template.md) or a single-actor [journey](user-journey-template.md) instead, and say why.
- If a stakeholder insists, produce **provisional personas** clearly marked `[ASSUMPTION-BASED]`, in visibly different styling, with the validation plan attached.

---

## Differentiate on behaviour, not demographics

Personas are segmented by what differentiates **behaviour and need**, which is rarely age or job title.

Strong axes: goals · mental model · risk tolerance · frequency of use · expertise · constraints (time, budget, connectivity, access needs) · decision authority · workaround strategies.

Weak axes on their own: age · gender · location · company size.

If two personas would take the same actions for the same reasons, they are one persona.

---

## Attributes — all cited

| Attribute | Rule |
|---|---|
| Name and label | Descriptive of behaviour ("Cautious Comparer"), not a stock first name alone |
| Which participants | The actual IDs this persona is built from — **required** |
| Goals | What they are trying to achieve, cited |
| Behaviours | Observed, not stated where possible |
| Mental model | How they think the system works, in their words |
| Frustrations | Linked to findings |
| Workarounds | What they do instead — often the richest design input |
| Context | Environment, constraints, interruptions |
| Success criteria | How they judge whether it went well |
| Quote | One verbatim, real, cited |
| Variation within | Where members of this group differ from each other |
| Evidence strength | How many sessions, which quant support, confidence grade |

**Never include** unless evidenced and relevant: photos standing in for real people, invented brand preferences, fictional biographies, personality traits, "favourite apps", filler demographics.

---

## Template

```
PERSONA 02 · "The Cautious Comparer"

BUILT FROM     P02, P05, P07, P11 (4 of 12 sessions)
               + SURVEY segment "low prior purchase confidence" 31% (n=418)
CONFIDENCE     Medium — qual-led, survey-consistent, no analytics segmentation

GOAL           Avoid being surprised by cost after committing.
                                                          [P07:24:55, P02:18:40]
MENTAL MODEL   Assumes fees are added late unless proven otherwise; treats
               unexplained totals as a signal to leave.    [P05:09:12]
BEHAVIOURS     Opens pricing in a second tab; re-scrolls the basket; abandons
               rather than asks.                           [EVT:checkout_back_nav]
WORKAROUND     Screenshots the basket before proceeding.   [P11:31:02]
FRUSTRATION    Cannot verify total pre-commit → F-03
SUCCESS        "I knew exactly what I'd be charged before I clicked"  [P02:20:05]

QUOTE          "I'm not clicking that until I know what it's actually
                going to charge me"                        [P07:24:55]

VARIATION      P11 does the same checks but completes anyway — higher trust
               from a prior good experience.               [P11:33:40]

NOT THIS PERSONA
               Returning users with saved payment (P09) show none of this.
```

---

## Anti-patterns

- Personas built from stakeholder assumption and given a research veneer.
- "Average user" personas that describe no one.
- Persona sets covering 100% of the market — real sets leave edges uncovered, and say so.
- Segments defined by internal org structure rather than user behaviour.
- Rounding away intra-persona variation. The `VARIATION` field is mandatory; `none observed` is a valid entry only after the [challenger audit](../references/challenger-audit.md) has been run.

---

## Maintenance

Every persona carries a creation date, the study IDs behind it, and a review trigger (product change, market shift, or 12 months, whichever is first). A persona without a date silently becomes fiction.
