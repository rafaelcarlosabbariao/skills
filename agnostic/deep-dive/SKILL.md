---
name: deep-dive
description: "Use to build or pressure-test a project deep-dive presentation — the 20-minute prepared deck for an engineering interview panel (Anthropic-style), or any writeup that has to survive 'why did you choose X over Y'. Trigger on 'deep dive', 'project presentation', 'prep me for the project round', 'write up this project', or when filling the problem / decisions / tradeoffs / what_went_wrong fields on a portfolio project record."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# Deep Dive — the prepared project presentation

You are building a **20-minute prepared presentation** about one project, for a panel that
will spend the following 20 minutes finding the edges of the presenter's knowledge.

Configure: if you keep your own notes on the round's format (a probe list, red flags from past
panels), point this line at that file and read it first.

## The thing to understand first

This is **a values round wearing technical clothes.** The panel is not scoring whether the
system was impressive. It is scoring whether the person understands their own work
honestly. That inverts the usual instinct: the failure section is not damage to be
minimized, it is the section that makes every other section believable.

So the job here is not to help someone sound good. It is to help them be *accurate at
depth* — and to refuse to manufacture the parts only they can know.

## The five sections

Produce these, in order. The field names are suggestions for a project record (a database
row, a YAML file, a portfolio CMS), so the output can go straight into one.

| # | Section | Field | What it must contain |
|---|---|---|---|
| 1 | Context and problem | `problem` | The problem, the constraints, why it was non-trivial, who the users were. One or two slides. Stakes, not backstory. |
| 2 | Role and ownership | `role` + `what_i_did` | Explicitly what *they* designed, implemented, decided. And explicitly where they touched something someone else decided. |
| 3 | Architecture and decisions | `decisions` | Each major choice, its reasoning, **the alternatives considered and why they were rejected**. |
| 4 | Trade-offs | `tradeoffs` | What was given up, and under what constraint. Concrete. |
| 5 | What went wrong | `what_went_wrong` | A real failure or a decision they'd change. **Mandatory.** |
| 6 | Outcome and impact | `outcome` | What it achieved, which metrics mattered, what people actually did with it. Grounded — inflated numbers get probed. |

(Six rows, five sections: trade-offs is section 3's second half, split out because the
record stores it separately and because it is the half people skip.)

## How to run it

**Interview, don't invent.** For each section, ask before you write. The presenter is the
only source for decisions, alternatives, and failures. Writing plausible-sounding
trade-offs *for* them is the single worst thing this skill could do — it manufactures
exactly the material the panel is built to detect, and the presenter will not be able to
defend it under questioning.

Work section by section. For each:

1. Ask the specific question (below).
2. Write the section in their voice, from their answer.
3. **Immediately probe it** the way the panel will. If the probe has no answer, that's a
   hole — say so plainly and leave it marked, rather than smoothing it over.

### Section questions and their probes

**1 — Problem.** *What was actually hard about this? What would a competent person have
gotten wrong?*
→ Probe: if the problem statement doesn't imply the architecture, it's backstory. Cut it.

**2 — Ownership.** *Which decisions were yours? Where does your ownership stop?*
→ Probe: for each claim, "could you defend this choice for ten minutes?" If not, it comes
out of the deck. "That was decided by the team" ends the round — so it must never need
saying.

**3 — Decisions.** *For each major choice: what else did you consider, and why did you
reject it?*
→ Required shape: *evaluated X and Y; chose X because [reasoning]; Y would have
[trade-off]*. A decision with no rejected alternative is not a decision, it's a default —
label it as one honestly ("this was the obvious choice because…") rather than dressing it up.
→ Probe: "what happens if [component] fails?" Trace the real failure modes now.

**4 — Trade-offs.** *What did you give up, and what forced it?*
→ Probe: a trade-off with no cost is not a trade-off. If every choice sounds free, push
harder.

**5 — What went wrong.** *What broke, what did you get wrong, what would you rebuild?*
→ "I'd do it the same" is not credible — say so directly if you hear it.
→ Best answers name a failure that was *discovered through instrumentation*, because that
shows the system was built to be judged.
→ Probe: what did you change afterwards? A failure with no extracted lesson is just an
anecdote.

**6 — Outcome.** *Which numbers, and where do they come from?*
→ Probe: every figure needs a source and a sample size. Numbers must match whatever else
is public (resume, repo, site) exactly. A number that only appears here is a liability.

## Safety-conscious framing (this is scored)

Interviewers specifically watch for whether failure modes come up *unprompted*. Weave in,
where true:
- correctness guarantees **or their absence**, stated plainly
- risks knowingly accepted, and why that was the right call at the time
- what the system does under partial failure
- where it breaks, and how you'd know

Someone who volunteers "here's where this is unsound" reads as safety-conscious. Someone
who has to be asked reads as someone who ships first.

## Before calling it done — the red-flag pass

Run this checklist and report failures bluntly:

- [ ] Is there a real failure section? (Absent = flagged red. Non-negotiable.)
- [ ] Does every architectural claim have a rejected alternative attached?
- [ ] Is there anything here they cannot speak to exhaustively? Cut it.
- [ ] Any sentence that would make them say "the team decided that"? Cut it.
- [ ] Any generic architecture talk ("microservices and a queue") with no *why it beat the
      alternative*? Rewrite or cut.
- [ ] Does every number have a source?
- [ ] Is there a specific, genuine answer to "what would you do differently"?

## Output — always two artifacts

The round *is* a presentation, so a document alone is never the finished deliverable.
**Always produce both**, in this order, and say which is which:

**1. The prep document.** Section-per-heading, in the presenter's voice, everything known
about each section including the material that will not be presented. This is what they read
beforehand and keep open during Q&A. It carries: the running order with per-section minute
budgets, the full decision blocks (evaluated / chose / because / rejected / cost), the
timeline of inputs, provenance for every figure, and any cuts with the reason recorded so
nobody re-adds them later. Mark held-back material visibly — the panel never sees it, but the
presenter needs to know it is prepared and deliberate.

**2. The slides.** Roughly 12–16, one idea each. **Slides carry numbers, structure, and
figures. Prose stays in the presenter's mouth** — a line they will say out loud is redundant
on screen and splits the room's attention between reading and listening. Three rules:

- The one-line slides (the pattern statement, the key figure, the closing line) each get their
  own screen with almost nothing on them. Whitespace is what signals weight.
- Every number on a slide shows its sample size. `+15.7` invites the question; `+15.7 · n=18`
  shows they already knew.
- Nothing from the prep document's held-back sections appears on a slide.

Keep §5 at full weight in both — it must never shrink to a bullet at the end. §3 and §5
together hold more than half the clock; if rehearsal runs long, time comes out of §1 and §2.

Budget guide: §1 2–3 min · §2 1–2 · **§3 6–7** · §4 3 · **§5 4–5** · §6 3.

**Format.** HTML is the default for both — the deck needs keyboard navigation and the document
needs to be readable on a phone the morning of. Self-contained, no external requests. Offer to
publish as an Artifact rather than doing it unasked — deep-dive material is candid by design.

**Start from the templates. Do not rebuild the shell.** In `templates/` beside this file:

| File | Use |
|---|---|
| `deep-dive.template.md` | The source of record. Section skeleton with the probes inlined as HTML comments. |
| `document.template.html` | The prep document — sticky TOC with minute budgets, `.plate` / `.callout` / `.under` / `.cut` blocks. |
| `slides.template.html` | The deck — one `<section class="slide">` each, arrow-key nav, scroll-snap, print-to-PDF, **slide numbers generated by JS so adding or removing a slide never means renumbering**. |

They ship with one house style (a cream ground with an espresso toggle, every table and figure
on a cream plate, one accent color, a fixed three-color chart order, system fonts). Restyle the
`:root` tokens to taste. Copy, replace the `{{PLACEHOLDERS}}`, delete the
blocks you don't need. Fix the templates rather than working around them when something is
wrong — they are the durable artifact.

If the project also lives in a structured record (a portfolio database, a CMS), writing the
section copy into its fields is a third output. Check that the record has fields for
*decisions*, *trade-offs* and *what went wrong*; many do not.

## What not to do

- Do not write decisions, trade-offs, or failures the presenter did not tell you.
- Do not soften a failure into a humblebrag ("we were too ambitious"). A real mistake has a
  cost attached.
- Do not let a section be filled with adjectives where a number belongs.
- Do not produce only the success story. If the presenter resists section 5, tell them
  plainly what its absence signals and ask again.
