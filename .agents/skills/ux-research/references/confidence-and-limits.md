# Protocol — Confidence & Limits

**Purpose:** Give every finding a confidence grade the audience can act on, and state the limits of the study in the deliverable rather than in a caveat nobody reads.

---

## 1. Grades

| Grade | Criteria | How stakeholders should use it |
|---|---|---|
| **High** | Two or more source types converge; challenger audit run and bounded; adequate sample for the claim; consistent across segments or boundary stated | Act on it |
| **Medium** | Single source type but strong internal consistency (e.g. 8 of 12 participants), or multi-source with partial divergence | Act with a check; design so it can be reversed |
| **Low** | Few instances, single source, or unresolved rival explanations | Treat as hypothesis; test before building |
| **Assumption** | No supporting evidence; provided at stakeholder request | Do not act; validate first |

Confidence is about the strength of evidence, not the importance of the finding. A high-confidence minor finding and a low-confidence critical one both exist and are labelled honestly.

---

## 2. What downgrades a finding

- Only one source type available (not a flaw, but a ceiling)
- Evidence concentrated in one segment while the claim is general
- Mostly moderator-prompted rather than unprompted mentions
- Rival explanations that the data cannot distinguish
- Recency: prior-study evidence on a surface that has since changed
- Self-report used to support a behavioural claim
- Small or skewed sample relative to the claim's scope

Name the downgrade reason in the ledger. "Medium" with no reason is not useful.

---

## 3. Sample limits block

Ships with every deliverable, in the deliverable, not as an appendix.

```
WHO THIS REPRESENTS
In scope       Consumer tier, EU + US, 25–54, existing customers <12 months
Not in scope   Enterprise, APAC, new prospects, assistive-technology users
Fielding       Qual 3–14 Mar 2026 · Survey 18–29 Mar 2026 · Analytics Q1 2026
Known skew     Survey respondents over-index on high-frequency users (recruited in-product)
```

Sample skew is stated even when it is inconvenient. In-product recruitment systematically excludes the users who left.

---

## 4. Open questions

Every synthesis ends with what it could not answer. Each entry names a method, so the list is actionable rather than decorative.

| # | Question | Why unanswered | Method to close | Effort |
|---|---|---|---|---|
| Q1 | Does the cost-clarity effect hold for enterprise? | No enterprise sessions; n=57 survey only | 6 enterprise interviews | 2 weeks |
| Q2 | Is the drop-off caused by ambiguity or by price? | Correlational only | Pre-commit total A/B | 1 sprint |

---

## 5. Honesty under pressure

Stakeholders will ask for more certainty than the evidence carries. The response is not to soften the grade — it is to give them something they can actually use:

- Say what the evidence *does* support, at what confidence, for whom.
- Offer the cheapest test that would raise the grade.
- Where a decision must be made now, say so and frame it as a bet with a named assumption and a reversal signal: *"proceed on F-02 (medium); if task success doesn't move 5 points in 4 weeks, the assumption was wrong."*

Never resolve a divergence between sources by choosing the one the stakeholder prefers.
