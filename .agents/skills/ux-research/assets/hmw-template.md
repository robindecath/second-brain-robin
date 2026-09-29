# Deliverable — How Might We

**For:** teams moving from validated insight into ideation.

An HMW converts a finding into an invitation to solve, without prescribing the solution. It is the bridge between synthesis and design — and it inherits the confidence of the finding behind it.

---

## Sizing

The most common failure is the wrong altitude.

| Too broad | Right | Too narrow |
|---|---|---|
| HMW make checkout better? | HMW help buyers confirm exactly what they'll be charged before committing? | HMW add a tooltip to the total field? |

Test: too broad if it doesn't suggest where to start; too narrow if it names the solution. If the HMW contains a UI element, it's too narrow.

---

## Format

```
HMW-04
How might we help first-time buyers confirm exactly what they'll be charged
before they commit?

FROM FINDING   F-03 (confidence: HIGH, bounded consumer tier)
FOR            "Cautious Comparer" · new consumer-tier buyers
JOB            J-02 — see a full itemised charge before committing
JOURNEY STAGE  04 · Payment
EVIDENCE       7/12 qual [P02,P05,P07,P11 …] · SURVEY:Q14 34% (n=418)
               · EVT:checkout_back_nav 41% of abandons
SUCCESS SIGNAL Abandonment at payment ↓; pre-commit total interaction ↑
CONSTRAINTS    Totals cannot be final before address entry (tax rules)
TENSION        Two participants wanted *less* detail here [P04:22:10, P12:16:44]
               — solutions must not force detail on everyone
CONFIDENCE     High
```

The `TENSION` field carries minority evidence forward from the [challenger audit](../references/challenger-audit.md). Ideation without it optimises for the majority and breaks the edge cases.

---

## Generating a set

For a single finding, vary the framing to open different solution spaces:

| Lens | Example |
|---|---|
| Amplify the good | HMW make the moment of confirmed cost feel reassuring? |
| Remove the bad | HMW remove the need to verify the total at all? |
| Explore the opposite | HMW make committing before knowing the total feel safe? |
| Question the assumption | HMW remove cost uncertainty earlier, before the basket? |
| Adapt from elsewhere | HMW borrow the receipt-preview pattern from ticketing? |
| Change who acts | HMW have the system prove the total rather than the user check it? |

Each generated HMW still traces to the same finding ID. Lens variation is not licence to drift from the evidence.

---

## Rules

- Every HMW names its parent finding. No orphans.
- An HMW from a low-confidence finding is labelled as such — teams should know they may be designing for a hypothesis.
- Problem framing only. No feature names, no UI elements, no technology.
- Name the user and the moment. "HMW help users…" with no segment or stage is unactionable.
- Carry constraints so ideation stays in the feasible space.
- 5–10 HMWs per workshop. More produces shallow coverage.
- Do not invent HMWs to fill a theme with no evidence behind it. An uneven set is honest.

---

## Handoff

Cluster HMWs by theme, sequence by the journey stage they address, and mark which are high-confidence (ready to solve) versus low-confidence (need validation first). Where a set is heading into an [OST workshop](ost-workshop-template.md), map each HMW to the opportunity it sits under so the tree and the ideation stay connected.
