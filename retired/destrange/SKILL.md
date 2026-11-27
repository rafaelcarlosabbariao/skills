---
name: destrange
description: "Run the DeStrange on a draft or claim — screen a cultural retrodiction's facts and register, then validate it or reposition it into a testable instrument-led piece with a full build spec. Trigger on 'run the destrange', 'screen this piece', 'was X inevitable', 'is this claim solid', or any request to pressure-test a why-did-this-happen essay before it ships."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# The DeStrange — retrodiction screening and repositioning

You are running **the DeStrange**: an instrument that takes a claimed-inevitable cultural
outcome and its proposed causes, checks the facts, and asks of every cause *was it structure
or scaffolding?* — by removing it against a population of comparable cases rather than
asserting over a single story. The name is the method: to de-strange a thing is to take the
strangeness out of how it happened. The standing question it puts to any retrodiction:
**how many branches did you run?**

The flow below is fixed. Do not skip the screen and jump to repositioning; the screen's
findings are what make the repositioning specific.

## Phase 0 — Locate and attribute

- Find the piece (notes vault, CMS, repo, wherever it lives) and every sibling document
  on the same subject.
- **Establish authorship before judging:** which prose is the author's, which is
  AI-drafted. AI-drafted analysis gets zero benefit of the doubt on facts; treat its
  every statistic as unverified.
- Note what the piece's *own* strongest asset is (usually the author's opening observation
  or a receipt they personally ran). That survives every repositioning.

## Phase 1 — The screen

Extract every load-bearing claim: statistics, dates, attributions, firsts ("pioneered",
"invented", "the only"), and causal assertions. Verify each against sources — WebSearch /
WebFetch, primary documents over aggregators (company filings > SEO stat pages; the
Wayback Machine dates what sites actually said). Check coined terms and names for
collisions while you are at it (an existing framework, a podcast, an SEO clash — and
whether the phrase is becoming LLM-speak, which is disqualifying for this desk).

**Output the screen table** — this exact shape, always:

| Claim in the piece | Status | What's actually true | Source |
|---|---|---|---|

Status vocabulary: **Correct** · **Fabricated** (no basis found; say how far off) ·
**Conflated** (two real stats spliced) · **Wrong attribution** · **Unsupported** (could be
true, no source found) · **Correct but miscredited**. Every non-Correct row gets the real
figure and a link.

Also screen the **register**: does the piece assert convergence/inevitability without a
comparison set? Does it dress metaphor as mechanism (Hebbian culture-wiring, quantum
entanglement of trends, computational irreducibility, city-grid analogies)? Unfalsifiable
scaffolding is a register defect even when no individual fact is wrong.

## Phase 1.5 — The travel check

The screen tests whether the piece is *right*; this tests whether it *travels*. Audit the
five patterns that recur across practitioners whose public analytical work lands (from a
survey of about 45 writers and researchers). Always emitted, on
both verdicts — a factually valid piece can still travel badly.

**Output the travel table** — this exact shape:

| Pattern | Test | Verdict | Fix |
|---|---|---|---|
| **Named instrument** | Does the piece run a named, repeatable procedure with a stated method — not a one-off take? Is the cadence or the next run visible? | | |
| **Coinage** | Does it mint portable, collision-checked language a reader can cite without ever visiting the site? (The distinction usually travels farther than the procedure.) | | |
| **Linked deliverables** | Is the method its own citable object — repo, dataset, standalone method note — linked from the piece, so "trust me" converts to "check me"? | | |
| **Declared lens** | Is the author's position stated in the opening lines and then *demonstrated* by what follows, so it reads as positioning rather than a hobby? | | |
| **Open door** | Can a cold reader orient in ten seconds — a plain summary, tally, or start-here equivalent before the deep material begins? | | |

Verdict vocabulary: **pass** · **partial** · **missing**. Every non-pass row gets a
one-line fix. A piece with two or more missing rows should not ship yet even if the screen
came back clean.

## Phase 2 — The verdict

One of two, stated plainly with the reasoning:

- **VALIDATE** — facts hold and the register survives a research screen. Deliver the screen
  and travel tables, list minor fixes, stop. Do not invent a repositioning for a piece that
  doesn't need one.
- **REPOSITION** — fabricated/conflated facts, or an unfalsifiable only-way claim carried
  by voice instead of method. Proceed to Phase 3.

## Phase 3 — The repositioning (only on REPOSITION)

### 3a. The explanation

Name the genre problem: retrodiction is cheap because any outcome can be handed a
convergence story after the fact; the cure is to make it expensive. The standard move is
**instrument, not argument** — the piece stops asserting the claim and instead runs a named,
repeatable test on it, with the original subject as specimen 001. Then work out what the
evidence actually supports:

- **Structure vs scaffolding.** For each proposed cause, remove it and ask if the outcome
  survives. *Structure*: remove it and the thing stops. *Scaffolding*: remove it and the
  thing still happens, slower or smaller. Scaffolding fools retrodiction because it is loud
  while the thing goes up and gone by the time you look back.
- **Find where reality ran the counterfactual** — a natural experiment (a ban, a payment
  cutoff, a platform policy reversal) beats any simulation. Measure **magnitude** and
  **latency** of the response.
- **Find the natural control** — the comparable case with the same infrastructure and one
  different rule. It isolates the variable better than argument can.
- **Honor the surprise.** If the test overturns the piece's own opening hypothesis, that
  contradiction is the piece's best moment, not a problem — it is the proof the procedure
  worked. Slot it as "what the test did to my prior."

### 3b. Quantifiability

An inevitability claim needs **n > 1, not a chart**. The three standard runs:

1. **Shock test** — every instance where the candidate-structural variable was actually
   withdrawn; measure magnitude and latency per event.
2. **Trend-break test** — fit the pre-shock curve, project, subtract from actual; the
   residual is the accelerant's measured contribution. Run the same projection on control
   cases to separate sector effects from subject effects.
3. **Condition table** — crisp-set **QCA** (Ragin; cite it — applying a standard tool is
   the credential, inventing rigor is not). Cases as rows (~12–15, and rows with
   outcome = 0 are mandatory or the test is worthless), conditions as columns coded 1/0
   under written rules, a stated outcome threshold. Compute **consistency** (necessity
   conventionally ≥ 0.90) and **coverage** (guards against trivial necessity).

**Pre-registration is non-negotiable:** the case list, coding rules, and outcome threshold
are written and committed with a timestamp *before* looking at outcomes, and the
falsification condition is published up front ("if condition E scores ≥ 0.90 the original
claim survives and this repositioning is wrong").

Data sourcing order: primary documents (company filings via Companies House / SEC,
Wayback-archived ToS pages — the dated evidence for what platforms permitted when) →
behavioral measures (Wikipedia Pageviews API for absolute counts, Google Trends for
attention with its normalization caveated, app-rank history) → discourse corpora
(MediaCloud, GDELT, Reddit archives). Aggregator statistics are flagged low-confidence and
triangulated across three sources before they carry weight. Publish the repo — data,
coding sheet, script.

### 3c. The prediction standard

Every repositioned piece carries one forward-looking, falsifiable prediction, quantified
before the window closes: **corpus, unit, coding rule (term sets), metric, threshold,
deadline** — and the explicit sentence that if the threshold isn't met, the prediction
failed and the update saying so gets posted.

### 3d. The build spec (the deliverable)

Emit, in order:

1. **The repositioning in one line** — from what, to what.
2. **Corrections it forces** — claim, finding, method.
3. **Body structure table** — sections mapped to the six-slot skeleton
   (claim-arguable / sample / instrument / finding-with-surprise / caveat-in-public /
   check-me-link), with word budgets and which sections carry a chart or table.
4. **The condition table spec** — outcome, threshold, conditions with coding rules, case
   list including negative cases, what gets computed, the falsification sentence.
5. **Data sources and harvest order** — pre-registration first, always.
6. **The prediction and its quantification standard** — all six commitments.
7. **Publishing spec** — two citable objects (the essay + a standalone method note so the
   instrument can be cited without the essay — the method note doubles as the open door);
   render format; series; portfolio mirror if quantified; the reader hook that feeds
   specimen 002.
8. **The travel check, re-run against the spec** — the Phase 1.5 table again, now scored as
   the piece *will ship*: instrument named, coinage collision-checked, deliverables linked,
   lens declared in the opening lines, door open. Non-pass rows become build tasks.
9. **Kill list / keep list** — what gets cut (with why), what survives (with the verified
   figure attached).

## Standing rules

- The author's opening observation is the spine; never reposition it away.
- The structure/scaffolding verdict vocabulary is the instrument's output language — use it.
- Never hand the author prose in their voice as finished copy; structure and receipts are
  the deliverable, the writing is theirs.
- Cite the screen's sources inline in the table. A screen row without a link is an opinion.
- No em dashes in emitted report prose.
