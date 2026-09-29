# Deliverable — Opportunity Solution Tree Workshop

**For:** teams and leadership choosing between bets — connecting a desired outcome to evidenced opportunities, then to solutions and the experiments that test them.

The tree is only as good as the evidence under its opportunities. The researcher's job is to supply an opportunity space that is real, and to prevent the tree becoming a sanctioned list of things people already wanted to build.

---

## Structure

```
OUTCOME            one measurable business/product outcome
  └── OPPORTUNITY  an evidenced unmet need, pain point, or desire
        └── SOLUTION      a way to address it
              └── EXPERIMENT   the test of the riskiest assumption
```

Rules of the tree:
- **One outcome.** Multiple outcomes means multiple trees.
- **Opportunities are needs, not solutions.** If it has a verb like "build", "add", or "redesign", it belongs a level down.
- **Every opportunity carries citations.** An uncited opportunity is a stakeholder preference wearing research clothes.
- **Solutions are compared within a single opportunity**, never across. Cross-opportunity comparison is how the easiest thing wins rather than the most valuable.

---

## The opportunity space (research output)

Prepared before the workshop and handed to the facilitator.

```
OUTCOME  Reduce checkout abandonment for new consumer-tier buyers
         baseline 38% (Q1 2026) [FUNNEL:checkout · payment · 2026 Q1]

O-02  "I can't confirm what I'll be charged before committing"
      SOURCE      F-03 · Job J-02 · Journey stage 04
      EVIDENCE    7/12 qual [P02,P05,P07,P11] · SURVEY:Q14 34% (n=418)
                  · EVT:checkout_back_nav 41% of abandons
      SIZE        ~34% of respondents; 41% of observed abandons
      CONFIDENCE  High (bounded: consumer tier, new users)
      TENSION     2 participants want less detail here [P04:22:10, P12:16:44]

O-05  "I don't know if this seller is legitimate"
      SOURCE      F-06
      EVIDENCE    3/12 qual — single source
      SIZE        unknown
      CONFIDENCE  Low — hypothesis; validate before investing

O-07  [ASSUMPTION] "Buyers want instalment options"
      EVIDENCE    none in this study; stakeholder-raised
      STATUS      Not an opportunity yet. Validation: add to next survey wave
```

Opportunities are grouped, not ranked by preference: **evidenced and sized · evidenced but unsized · hypothesis · assumption**. Ranking happens in the room, with the evidence visible.

---

## Running the session

| Phase | Time | Content |
|---|---|---|
| Frame | 10 min | The outcome, its baseline, its measure |
| Evidence walk | 20 min | The opportunity space, including the low-confidence and assumption tiers |
| Challenge | 15 min | What's missing? Who isn't represented? — surface the [sample limits](../references/confidence-and-limits.md) |
| Select | 15 min | Choose one target opportunity: size × confidence × outcome fit |
| Ideate | 30 min | 3+ distinct solutions for the *same* opportunity ([HMW](hmw-template.md) set) |
| Assumption map | 20 min | Per solution: desirability, viability, feasibility, usability assumptions |
| Test plan | 20 min | Smallest experiment for the riskiest assumption |
| Close | 10 min | Owners, dates, what would make us abandon this branch |

The challenge phase is where flattening gets caught by the room rather than by the agent. Present the minority evidence there explicitly — do not let it stay in the appendix.

---

## Facilitation guards

- If the room jumps to solutions during the evidence walk, park them and return to the opportunity.
- If someone proposes an opportunity with no evidence, add it to the assumption tier in full view — do not argue it down, and do not let it be promoted without data.
- If the chosen opportunity is low-confidence, the output is a **learning experiment**, not a build.
- Only one solution branch per opportunity may proceed to build at a time. Parallel branches are parallel bets and should be named as such.
- Record what would falsify the bet before anyone starts building.

---

## Output pack

1. The tree — outcome, opportunities with confidence tiers, selected solutions, experiments
2. Assumption map per selected solution, riskiest assumption marked
3. Experiment briefs: assumption, method, success threshold, decision rule, owner, date
4. The parked list — opportunities not selected, with why, so they are not relitigated
5. The [evidence ledger](../references/attribution.md) attached in full
