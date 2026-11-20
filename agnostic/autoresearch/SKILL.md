---
name: autoresearch
description: "Run the autoresearch loop: an autonomous overnight experiment cycle where you edit one file, measure against one fixed metric under a fixed budget, and let git arbitrate keep vs discard, logging every trial to results.tsv. Trigger on 'run autoresearch', 'kick off a new experiment', 'let it run while I sleep', 'tune this overnight', 'optimize X autonomously', or pointing at a repo with a program.md."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# autoresearch: the autonomous experiment loop

You are running **autoresearch**: a fixed-budget, single-metric, git-arbitrated experiment
loop that runs unattended for hours. The human sets it going and leaves. You do not stop
until they come back and stop you.

Ported from [karpathy/autoresearch](https://github.com/karpathy/autoresearch) (March 2026),
where the original target was 5-minute single-GPU LLM pretraining scored on validation bits
per byte. **That is one instance of the pattern, not the pattern.** The loop works for any
search where a cheap honest number can be produced on demand.

The inversion that makes it work: the human stops editing the work product and starts
editing *your instructions*. In the original repo the human's artifact is `program.md`, the
agent's is `train.py`. If the human wants better results they revise the brief, not the code.

## Phase 0: The contract

**Do not start the loop until all four of these are pinned down.** If any is missing, ask
for it. This is the one moment where stopping to ask is correct; after this, never again.

1. **One metric, one direction.** A single scalar the run prints, where better is
   unambiguous. It must be resistant to the changes you are about to make. In the original,
   bits per byte is used precisely because it is vocab-size-independent, so a tokenizer
   change cannot flatter the score. Ask: *what could I change that would move this number
   without actually improving anything?* If there is an answer, the metric is wrong.
2. **A fixed budget.** Wall clock, tokens, dollars, iterations. Every trial gets the same
   one. This is what makes trials comparable when everything else is in play, and it means
   the search converges on the best result *for this machine in this budget* rather than on
   an abstract optimum. Accept the tradeoff: results are not comparable across machines.
3. **Exactly one editable surface.** Name the file (or the tight set) you may modify.
   Everything else, especially the evaluation harness and the data pipeline, is read-only.
   The agent grading its own homework is the failure mode this prevents.
4. **A dedicated branch.** `autoresearch/<tag>`, tag usually today's date. It must not
   already exist. Refuse to run this on a branch with work on it.

Then: confirm the harness runs green once, unmodified. **The first trial is always the
untouched baseline.** You cannot tell improvement from noise without it.

## Phase 1: Initialize

- `git checkout -b autoresearch/<tag>` from the current main branch.
- Read every in-scope file end to end. These repos are small on purpose; there is no excuse
  for guessing at what a constant does.
- Verify the fixtures exist (cached data, credentials, a warm build) and tell the human to
  run the prep step if not. Do not start a 100-trial run against a missing cache.
- Create `results.tsv` with the header row only. **Leave it untracked.** It is the record of
  the search, not a member of the tree the search is mutating.
- Confirm setup with the human. This is the last confirmation.

## Phase 2: LOOP FOREVER

1. Check git state: what branch, what commit.
2. Hack one idea directly into the editable file. One idea per trial. Two changes in one
   commit means you learn nothing from the result.
3. `git commit`.
4. Run it, **redirecting all output to a log file**: `<cmd> > run.log 2>&1`. Do not use
   `tee`. Do not let the run stream into your context. Over a hundred trials, context is the
   scarcest resource you have, and this is the single instruction most often violated.
5. Read out only the metric: `grep "^<metric>:" run.log`.
6. Empty grep means it crashed. `tail -n 50 run.log` for the trace.
7. Append a row to `results.tsv`.
8. **Improved → keep the commit, the branch advances.**
9. **Equal or worse → `git reset` back to where you started.**

The branch *is* the state of the search. A regression never happened.

### results.tsv

Tab-separated, never commas, because descriptions contain commas.

```
commit	metric	cost	status	description
a1b2c3d	0.997900	44.0	keep	baseline
b2c3d4e	0.993200	44.2	keep	increase LR to 0.04
c3d4e5f	1.005000	44.0	discard	switch to GeLU activation
d4e5f6g	0.000000	0.0	crash	double model width (OOM)
```

Short commit hash, the metric (`0.000000` for crashes), the secondary resource cost
(memory, spend, whatever is the soft constraint), `keep` / `discard` / `crash`, and a one
line description of what was tried. The description is the deliverable. A human reading
fifty rows at breakfast should be able to reconstruct your reasoning without the diffs.

## The standing rules

**NEVER STOP.** Once the loop begins, do not ask "should I keep going?" or "is this a good
stopping point?" The human is asleep or gone and expects you to work indefinitely until
manually interrupted. If you run out of ideas, you have not run out of ideas: re-read the
in-scope files for angles you missed, read the papers or docs referenced in the code,
recombine previous near-misses, try a change more radical than the ones that failed. The
loop runs until interrupted, period. This rule is load-bearing; the default failure mode of
an agent on a long autonomous loop is checking in, and checking in at 3am wastes the night.

**Simplicity criterion.** All else equal, simpler wins. A 0.001 gain that adds twenty lines
of hack is not worth it. The same 0.001 gain from *deleting* code is a definite keep. A
change that is net zero on the metric but leaves the code much simpler is a keep. Without
this rule the loop ratchets into unreadable slop by trial forty.

**Soft constraints.** Secondary resources (VRAM, memory, spend) may grow somewhat for a real
gain in the metric, but must not blow up. Use judgment and log the number every trial so the
human can see the drift.

**Crashes.** Something dumb and local (typo, missing import, off-by-one) gets fixed and
re-run. An idea that is fundamentally broken gets logged as `crash` and abandoned. Do not
spend four trials rescuing a bad idea. If you cannot get a fix working in a few attempts,
give up on it and move on.

**Timeouts.** A trial that runs past roughly twice its budget gets killed and treated as a
failure: discard, revert, log it.

**Rewinding.** You may rewind the branch if you believe the search is stuck in a local
optimum. Do this very rarely, if ever, and log it.

## Adapting to a new domain

Most of the work is Phase 0. To port the loop somewhere new, answer:

- What is the cheap honest number? (val loss, p95 latency, benchmark pass rate, eval-set
  accuracy, bundle size, cost per request)
- What is the fixed budget that makes trials comparable?
- What single file holds all the knobs, and what must be frozen so the metric stays honest?
- How many trials fit in one night? At five minutes a trial that is roughly twelve an hour
  and about a hundred over an average human sleep. Size the budget to the number of trials
  you want, not the other way around.

**Do not use this loop** when the metric is a matter of taste, when a trial costs more than
a few minutes, when the thing being tuned has side effects outside the repo (writes to prod,
sends mail, spends real money per trial), or when a regression cannot be cleanly reverted by
`git reset`. The loop's safety comes entirely from trials being cheap, isolated, and
undoable.

## Analysis, when the human wakes up

Do not summarize from memory. Read `results.tsv` and report:

- total trials, and the keep / discard / crash split with a keep rate
- every `keep` row in order, which is the story of the night
- the running minimum of the metric, which is the frontier
- the secondary cost drift from baseline to best
- what you tried that failed, grouped by theme, since the negative results are usually the
  more useful half and the human paid for them too

The original repo ships an `analysis.ipynb` that plots exactly this: discards as faint grey
dots, keeps as prominent points, running minimum as the frontier line, all clipped to the
region at or below baseline. If the run has a notebook, use it.

## Worked example: the original

For reference when someone points you at karpathy/autoresearch itself.

| Slot | Value |
|---|---|
| Metric | `val_bpb`, validation bits per byte, lower better |
| Budget | 300s wall clock training, excluding startup and compile |
| Editable | `train.py`: model, optimizer, training loop, all hyperparameters |
| Frozen | `prepare.py`: constants, data, tokenizer, dataloader, `evaluate_bpb` |
| Brief | `program.md`: the human's artifact |
| Run | `uv run train.py > run.log 2>&1` |
| Baseline | depth-8 GPT, ReLU² MLP, RoPE + QK-norm, GQA via FlashAttention-3, `SSSL` windowed attention, ResFormer value embeddings on alternating layers, Muon for matrices + AdamW for embeddings and scalars, time-based LR schedule |
| Hardware | one NVIDIA GPU, tested on H100 |

Karpathy calls `program.md` "essentially a super lightweight skill," which is why this file
exists. Note the shipped `program.md` is deliberately a bare-bones baseline: iterating on the
brief to find the research-org code that produces the fastest progress is the actual game.
When a night's results disappoint, the first thing to revise is the instructions, not the
code.
