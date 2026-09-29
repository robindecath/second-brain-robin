# Deliverable — Jobs to be Done

**For:** framing the problem independently of any solution, so the team can evaluate alternatives against a stable need.

A job is what the user is trying to accomplish. It is solution-agnostic and durable — it survives changes to your product. "Use the filter" is a task. "Narrow down options without losing ones I might want" is a job.

---

## Job statement format

```
When [situation],
I want to [motivation],
so I can [expected outcome].
```

Each component is cited.

```
JOB J-02
When   I'm about to enter my payment details on a site I haven't used before
       [P02:17:55, P05:08:40, P07:24:10]
I want to  see exactly what I will be charged, itemised
       [P07:24:55, P11:30:48]
So I can   commit without the risk of being surprised afterwards
       [P02:20:05, SURVEY:Q14 n=418]

JOB TYPE      Functional (primary) + Emotional (avoid feeling duped)
FORCES
  Push        Previous experience of hidden fees            [P05:10:20]
  Pull        Wants the item; ready to buy                  [EVT:checkout_enter]
  Anxiety     "What if there's a delivery charge later"     [P02:18:40]
  Habit       Currently screenshots the basket instead      [P11:31:02]
CURRENT SOLUTION   Opens pricing page in a second tab; abandons if unresolved
SUCCESS CRITERIA   Zero surprise between displayed total and charged total
  measurable: pre-commit total views → completion rate
NOT THIS JOB       Enterprise buyers, whose totals are contract-governed [SURVEY:segment=ent]
EVIDENCE           4/12 qual · SURVEY:Q14 34% · EVT:checkout_back_nav
CONFIDENCE         High, bounded to consumer tier
```

---

## Job types

Capture all three where evidence supports them. Most failures of adoption are emotional or social jobs that were never named.

| Type | Question | Example |
|---|---|---|
| Functional | What task must be done? | Confirm the total before committing |
| Emotional | How do they want to feel? | In control; not naive |
| Social | How do they want to be seen? | As someone who does not get ripped off |

---

## Forces of progress

Every job carries four forces. Design works by increasing push and pull, and reducing anxiety and habit — but only the ones evidenced.

- **Push** — what makes the current situation unsatisfactory
- **Pull** — what attracts them to a new approach
- **Anxiety** — what makes the new approach risky
- **Habit** — what holds them to the existing way

An empty force field is left empty and marked `not evidenced`, never filled speculatively for symmetry.

---

## Rules

- **No solutions in job statements.** If the job names a feature, it's a task. Ask "why" until it doesn't.
- **Jobs are stable; tasks are not.** If a job would change when you ship a feature, it wasn't a job.
- **Derive from behaviour and struggle**, not from asking people what job they're doing.
- **Struggle is the signal.** Workarounds, abandonments, and improvisation locate jobs more reliably than stated preferences.
- **Hierarchy where useful:** big job → little jobs → tasks. Keep the levels labelled.
- **Not-this-job field is required** — it bounds the job and comes from the [challenger audit](../references/challenger-audit.md).

---

## Job map

Where a job has phases, map it so intervention points become visible:

`Define → Locate → Prepare → Confirm → Execute → Monitor → Modify → Conclude`

Mark where users currently struggle, with citations. Struggle points feed [HMW](hmw-template.md) and [OST opportunities](ost-workshop-template.md).

---

## Prioritisation

Where quant exists, rank by **importance × dissatisfaction** — jobs rated important but poorly served. Cite both dimensions with n. Where no quant exists, rank by frequency of struggle in the qual corpus and **say that the ranking is qualitative**, not an opportunity score.
