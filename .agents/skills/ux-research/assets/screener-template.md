# Screener: [study name]

Produce two versions: an **internal version** with routing tags, and a **participant version** with the tags removed.

## Introduction (shown to participants)

> We are running a short study on [topic] to improve [product or experience]. This questionnaire takes about [2–3] minutes and helps us find the right people.
>
> Sessions last [duration] and take place [format and window]. [State recording if applicable.] Your answers are confidential, reported anonymously, and there are no right or wrong answers. Participation is voluntary.
>
> [Internal studies: This is not an evaluation of you or your work, and nothing you say is shared with your manager in identifiable form.]

## Section 1 — Conflict of interest

**Q1. Have you been involved in designing, building, or owning [product/feature]?**
- Yes, directly `[REJECT]`
- I work adjacent to the team but not on it `[NEUTRAL]`
- No `[QUALIFIED]`

**Q2. Have you taken part in a research session about [product] in the last [3] months?**
- Yes `[REJECT]`
- No `[QUALIFIED]`

## Section 2 — Profile and quotas

**Q3. What best describes your role?**
- [Target role] `[QUALIFIED]`
- [Adjacent role] `[NEUTRAL]`
- [Non-target role] `[REJECT]`
- Other: ______ `[NEUTRAL]`

**Q4. [Business unit / segment / region]** — capture for quota balance `[NEUTRAL]`

**Q5. How long have you been in this role?**
- Less than 3 months `[NEUTRAL]`
- 3–12 months `[QUALIFIED]`
- More than 12 months `[QUALIFIED]`

## Section 3 — Behavioral qualification

**Q6. In the last month, how often did you [specific target task]?**
- Daily `[QUALIFIED]`
- A few times a week `[QUALIFIED]`
- A few times a month `[QUALIFIED]`
- Less than once a month `[NEUTRAL]`
- Never `[REJECT]`

**Q7. Which of these have you done in the last [3] months? (Select all that apply)**
*Include plausible distractors so the qualifying option is not guessable.*
- [Target behavior] `[QUALIFIED]`
- [Distractor] `[NEUTRAL]`
- [Distractor] `[NEUTRAL]`
- None of these `[REJECT]`

**Q8. Describe the last time you [target task]. What were you trying to do?**
*Open text. Use to verify the answers above are genuine.*

## Section 4 — Logistics

**Q9. Availability** — [list session windows]
**Q10. Contact** — [minimum contact detail needed to schedule]

> We will only use your contact details to arrange this session.

## Routing logic (internal only)

- Any `[REJECT]` → screen out politely and thank them.
- All required `[QUALIFIED]` → invite, subject to quota.
- Mixed `[NEUTRAL]` → waitlist as backup.

## Quota table (internal only)

| Group | Criteria | Target | Recruited |
| --- | --- | --- | --- |
| [Group 1] | [criteria] | [n] | |

## Screen-out message

> Thank you for your time. For this particular study we are looking for a specific profile, so we won't schedule a session with you this time — but we would love to include you in future research.
