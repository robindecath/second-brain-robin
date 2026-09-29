# Synthesis and modeling

Covers cross-study analysis and the artifacts that carry evidence into product decisions.

For the rigorous version of steps 6–7 below, use the dedicated protocols: [triangulation](triangulation.md) for cross-source validation, [challenger audit](challenger-audit.md) for disconfirming evidence and minority views, [attribution](attribution.md) for citation formats and the evidence ledger, and [confidence and limits](confidence-and-limits.md) for grading and stating sample limits. A finding is not a finding until it is traceable, triangulated where triangulation is possible, and tested against the evidence that would contradict it.

## Analysis sequence

1. **Assemble.** Collect cleaned transcripts, flash debriefs, observation notes, analytics, survey results, and support data for the study.
2. **Organize.** Lay observations out by participant and by research question, so gaps and imbalance are visible.
3. **Code.** Tag observations with behaviors, needs, pain points, motivations, contexts, and workarounds. Let codes emerge from the data before forcing a framework onto it.
4. **Cluster.** Group codes into themes. Name each theme in the users' language, not internal product vocabulary.
5. **Compare.** Contrast segments, contexts, and expertise levels. A theme that only holds for one segment is a segment finding, not a study finding.
6. **Disconfirm.** Actively hunt for evidence against each theme using the [challenger audit](challenger-audit.md). Record what you found and what you failed to find — `searched: none found` is a valid result, an empty field is not.
7. **Weigh.** Rate each theme's evidence strength via [triangulation](triangulation.md) and [confidence grading](confidence-and-limits.md), and state its limitations.
8. **Convert.** Turn themes into insights, then opportunities, then recommendations, then route to a deliverable ([research shareout](../assets/research-shareout-template.md), [debrief deck](../assets/debrief-deck-template.md), [journey](../assets/user-journey-template.md), [personas](../assets/personas-template.md), [JTBD](../assets/jtbd-template.md), [HMW](../assets/hmw-template.md), or [OST workshop](../assets/ost-workshop-template.md)).


## Evidence ladder

| Level | Definition | Example |
| --- | --- | --- |
| Observation | What happened or was said | "P3 opened three tabs to compare prices, then abandoned." |
| Interpretation | What it may mean | "Comparison may be hard within a single view." |
| Insight | Recurring explanation revealing a need or behavior | "Users compare options across tabs because the product offers no side-by-side view, and they abandon when the effort exceeds the value." |
| Opportunity | Valuable problem space | "Make comparison possible without leaving the flow." |
| Recommendation | Proposed next action or experiment | "Prototype in-page comparison and test task completion against the current flow." |

Never present an interpretation as an insight, or an insight as a measurement.

## Evidence strength

State strength for every insight:

- **Strong:** repeated across participants and segments, supported by observed behavior, and corroborated by a second data source.
- **Moderate:** repeated across participants but from one method or one segment.
- **Directional:** appeared a few times, plausible, not yet corroborated.
- **Single observation:** one participant. Report as a hypothesis, never as a finding.

Treat three or four repeated observations as a useful signal, not an automatic universal truth. Always name the sample, the segments covered, and the segments missing.

## Segmentation

Segment by needs, behaviors, contexts, and goals. Use demographics or firmographics only when they genuinely drive different behavior. A segment is only useful if the team would design or prioritize differently for it.

## Personas

Ground every persona in evidence. Include:

- Context and situation
- Goals and jobs to be done
- Actual behaviors and workarounds
- Pain points with supporting evidence
- Decision drivers and constraints
- A representative anonymized scenario
- What is known versus assumed

Avoid invented biographies, stock photos, and personality trivia that does not change a design decision. Below roughly 8 qualitative sessions, or with no segmentable quant, do not produce personas — use the [JTBD template](../assets/jtbd-template.md) or a single-actor journey instead. Use the full [personas template](../assets/personas-template.md) for the built-from citations, evidence strength, and required variation field.

## Journey maps

Build with product design, not alone. For each stage include: user goal, actions, touchpoints and channels, thoughts, emotions, pain points, evidence source, and opportunities. Mark moments of truth and drop-off points, and overlay analytics where available. Note which stages are evidenced and which are assumed. Use the [user journey template](../assets/user-journey-template.md) for the full stage structure, including variant paths for minority journeys.

## Service blueprint

Use when the frontstage experience depends on backstage people, processes, or systems. Layer: user actions, frontstage interactions, backstage actions, support processes and systems, and failure points with owners.

## Jobs to be done

Frame the problem independently of any solution using the [JTBD template](../assets/jtbd-template.md): situation, motivation, expected outcome, functional/emotional/social job type, and the forces of progress (push, pull, anxiety, habit). A job statement never names a feature — if it does, it is a task.

## How Might We

Convert a validated finding into an invitation to solve, sized between "too broad to suggest a starting point" and "too narrow to leave room for ideation", using the [HMW template](../assets/hmw-template.md). Every HMW names its parent finding and carries forward any tension from the challenger audit.

## Opportunity Solution Tree

Connect the chain explicitly:

1. **Desired outcome** — the measurable product outcome the team is accountable for.
2. **Opportunities** — evidence-backed user problems, needs, or desires that, if addressed, move that outcome. Cite the evidence for each.
3. **Solutions** — candidate responses under each opportunity, several per opportunity.
4. **Assumption tests** — the smallest experiments that would tell you whether a solution works.

Prune opportunities with no evidence. Do not attach a favored solution to a fabricated opportunity. For a workshop-ready opportunity space and facilitation guide, use the [OST workshop template](../assets/ost-workshop-template.md).

## Prioritization

Rank opportunities and recommendations on:

- User impact: severity and frequency of the problem
- Business relevance: link to the target outcome
- Evidence strength: how confident the finding is
- Effort and feasibility
- Risk if wrong, and reversibility

Separate "act now", "test first", and "needs more research". Be explicit about which recommendations are still hypotheses.

## Communicating

Use [../assets/research-shareout-template.md](../assets/research-shareout-template.md), or the more rigorous [../assets/debrief-deck-template.md](../assets/debrief-deck-template.md) when the audience holds a live decision and needs a per-finding confidence grade with a mandatory counter-evidence slide.

- Lead with the decision and the most consequential findings, not the methodology.
- Show the evidence chain for each claim, per [attribution](attribution.md).
- Use anonymized verbatims and short clips to make findings concrete.
- Show contradictory evidence rather than hiding it — give it named space, never a footnote.
- Make owners, next steps, and success measures explicit.
- Keep the method detail, sample table, and full evidence ledger in an appendix.

## Closing the loop

After the shareout, track: which decisions changed, which experiments were launched, which outcomes moved, and which questions remain open for the next discovery cycle.
