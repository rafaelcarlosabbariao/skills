# {{PROJECT}} — project deep dive

*Prepared presentation for the Anthropic-style project deep-dive round. 20 minutes prepared
+ ~20 minutes Q&A. Built section-by-section from {{PRESENTER}}'s answers; nothing here is
invented. Every figure carries provenance. Drafted {{DATE}}.*

**Format source:** {{YOUR NOTES ON THE ROUND'S FORMAT, IF ANY}}
**Numbers source:** {{WHERE THE FIGURES COME FROM, WITH THE DATE THEY WERE VERIFIED}}

---

## Status

| § | Section | Minutes | Slides | Status |
|---|---|---|---|---|
| 1 | Context & problem | 2–3 | 1–2 | — |
| 2 | Role & ownership | 1–2 | 1 | — |
| 3 | Architecture & decisions | 6–7 | 4–5 | — |
| 4 | Trade-offs | 3 | 2 | — |
| 5 | What went wrong | 4–5 | 2–3 | — |
| 6 | Outcome & impact | 3 | 2 | — |

**Calibration rule:** the deck is shallow, the preparation is deep. One idea per slide, and
behind every claim there must be ~three layers to descend through under questioning — the
claim, the reasoning, the evidence with its sample size. Anything that can't be spoken to
exhaustively for ten minutes does not go on a slide.

---

## §1 · Context and problem

<!-- The test: if the problem statement doesn't imply the architecture, it's backstory. Cut it.
     Aim for the version where a competent person handed the same brief would get it wrong. -->

{{THE PROBLEM, STATED SO THE ARCHITECTURE BECOMES INEVITABLE}}

**Why it's hard.** {{WHAT A COMPETENT PERSON WOULD GET WRONG}}

**Constraints, each forcing part of the architecture:**

1. **{{CONSTRAINT}}** → {{WHAT IT FORCES}}
2. **{{CONSTRAINT}}** → {{WHAT IT FORCES}}
3. **{{CONSTRAINT}}** → {{WHAT IT FORCES}}
4. **{{CONSTRAINT}}** → {{WHAT IT FORCES}}

<!-- If §5's failure has an origin decision, name it here so the deck closes a loop. -->

---

## §2 · Role and ownership

<!-- Explicit. Never make the panel infer it. "That was decided by the team" ends the round —
     so it must never need saying. -->

{{WHAT YOU PERSONALLY DESIGNED, DECIDED, IMPLEMENTED, OWNED}}

**Where other people touched it:**

- **{{WHO}}, {{WHEN}}** — {{WHAT, AND EXPLICITLY WHETHER ANY PRODUCT DECISION WAS THEIRS}}
- **{{WHO}}** — {{WHAT}}

**What I didn't own:** {{SCOPE STATEMENT — and note that it means the failures are yours}}

---

## §3 · Architecture and design decisions

<!-- The core section. Required shape per decision:
     evaluated X and Y; chose X because [reasoning]; Y would have [trade-off].
     A decision with no rejected alternative is a DEFAULT — label it honestly as one
     ("this was the obvious choice because…") rather than dressing it up. Aim for 3–5. -->

### Decision 1 — {{NAME}}

**Evaluated:** {{OPTION A}} vs. {{OPTION B}}

**Chose** {{WHAT}}{{, WITH DATE / COMMIT / MIGRATION IF THERE IS ONE}}

**Reasoning:** {{WHY — the load-bearing part, the bit a competent person would leave out}}

**Rejected** {{THE ALTERNATIVE}} because {{WHY}}

**Cost:** {{WHAT IT COST — omit only if genuinely free, which is rare}}

<!-- Material prepared but NOT presented goes in a block like this: -->
*Held in reserve for Q&A:* {{DEPTH THAT ONLY COMES OUT IF ASKED}}

### Decision 2 — {{NAME}}

{{same shape}}

### Decision 3 — {{NAME}}

{{same shape}}

### Say this out loud at the end of §3

<!-- If the decisions share a disposition — declining the easy option, choosing reversibility,
     refusing to ship what you can't measure — name it. Don't hope they notice. -->

{{THE PATTERN ACROSS THE DECISIONS}}

---

## §4 · Trade-offs

<!-- A trade-off with no cost is not a trade-off. If every choice sounds free, push harder. -->

| Gave up | Under what constraint | Cost |
|---|---|---|
| {{WHAT}} | {{WHY YOU HAD TO}} | {{WHAT IT COST}} |
| {{WHAT}} | {{WHY YOU HAD TO}} | {{WHAT IT COST}} |

{{THE SYNTHESIS — if several trades are the same trade, say so}}

---

## §5 · What went wrong

<!-- MANDATORY. A polished success story with no failure section is flagged red.
     Best answers name a failure discovered through instrumentation — it proves the system
     was built to be judged. "I'd do it the same" is not credible.
     A failure with no extracted lesson is just an anecdote. -->

**1.** {{ADMISSION}}

**2.** {{ADMISSION}}

**3.** {{THE STRUCTURAL ONE — the diagnosis that explains several symptoms at once}}

**What I'd do differently:** {{SPECIFIC, GENUINE, AND COSTED}}

> **Delivery guardrail.** Present §5 as what you see now, never as what you knew then, unless
> the record supports contemporaneous awareness. Implying it loses the section.

---

## §6 · Outcome and impact

<!-- Every figure needs a source and a sample size, and must match anything else that is
     public — resume, repo, site — exactly. A number that appears only here is a liability. -->

### The ledger

{{WHAT HAPPENED, FAILURE FIRST IF THERE WAS ONE}}

### What it returned

1. **{{FINDING}}** — {{EVIDENCE, WITH n}}
2. **{{FINDING}}** — {{EVIDENCE, WITH n}}

### What carried forward

{{WHAT YOU DO DIFFERENTLY NOW BECAUSE OF IT}}

### Close

{{ONE LINE}}

<!-- Record any cut figure and WHY, so nobody re-adds it later without seeing the reason. -->

---

## Appendix A — timeline of inputs

| Date | Input | Source |
|---|---|---|
| {{DATE}} | {{WHAT}} | {{git / doc / DB}} |

## Appendix B — scale

| Fact | Value |
|---|---|
| {{METRIC}} | {{VALUE}} |

---

## Red-flag pass

- [ ] Real failure section present (absent = flagged red, non-negotiable)
- [ ] Every architectural claim has a rejected alternative attached
- [ ] Nothing present that can't be spoken to exhaustively
- [ ] No sentence that would require "the team decided that"
- [ ] No generic architecture talk without why it beat the alternative
- [ ] Every number has a source and a sample size
- [ ] Specific, genuine answer to "what would you do differently"

## Open items

1. {{WHAT'S LEFT}}
