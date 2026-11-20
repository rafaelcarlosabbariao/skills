---
name: forecast-call
description: "Make one dated, sealed, falsifiable forecast call and file it in a forecast register (forecasts.json). Runs one call per invocation, opening with a counted summary of what the evidence supports so the caller knows what they are standing on. Trigger on 'make a forecast', 'seal a call', 'forecast call', 'file a prediction', 'what do I think happens with X', 'let's do a forecast', or any moment where a claim about the future is about to be made in public (an essay, a post, a brief, a pitch) and ought to be on the record first."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# The forecast call

One call per invocation. Never batch them, never file two in a sitting, and never revise a sealed
row. The register's value is that it cannot be edited after the fact, and a register filled in bulk
is one nobody believes.

**Configure:** the register's path (default `forecasts.json` in the current repo, or
`docs/validation/forecasts.json`), and where your evidence lives (datasets, dashboards, prior
analyses) so step 1 can count it.

## Why this exists

A method can be fully disclosed and still unvalidated. Until claims are scored against outcomes,
nobody (including the caller) knows whether the readings were right. A register of sealed,
dated, falsifiable calls is the cheapest way to start that record.

An absent register and an empty one read the same in prose and are different facts. The first
invocation creates the file.

## Step 1: Standing. What the caller is holding.

Always open here, with counted figures in place of adjectives. A forecast made without knowing
your evidentiary position is a guess; one made with that knowledge can be made with nerve.

Read the current state; do not recite numbers from memory. State four things:

1. **The data.** Row count, source count, and what fraction carries the fields the call depends on
   (dates are the usual one; measure freshness from publication date, never ingest date).
2. **The instruments that bear on this call**, and how far each has been validated. If a metric is
   named but nothing is measured behind it, say so.
3. **What is already sealed.** Prior calls in the register and their outcomes; any held-out
   backtest.
4. **The gap.** What this call cannot lean on. There is always one, and naming it is what makes the
   rest credible.

Then say in one paragraph what the caller can lean on. What it licenses is a **stated,
falsifiable, dated** call. It does not license a confident one.

If the standing for a call is thin, the briefing says the call is a guess and the register records
it as one. A low-confidence call that resolves is worth more to a calibration curve than a hedged
one that cannot be scored.

## Step 2: The call itself

Elicit and sharpen. Most first drafts of a forecast cannot be wrong; push until every field below
has an answer.

| Field | Rule |
| --- | --- |
| `claim` | One sentence, in the affirmative. No "may", no "could", no "is likely to be a factor in". |
| `resolves_on` | An ISO date. Not "by year end", not "eventually". |
| `resolution_criterion` | **The thing a stranger checks.** Name the source and the threshold. If nobody but the caller could adjudicate it, rewrite it. |
| `confidence` | An integer 50-99. Below 50 means the negation is the call; state that instead. |
| `falsifier` | What observation would make this wrong. If nothing would, stop: there is no call here. |
| `standing` | One line: which instruments and how many rows this rests on, copied from step 1. |
| `mechanism` | Why the caller believes it. This part gets graded even when the call resolves right for the wrong reason. |
| `rival` | The best competing explanation, stated fairly. |

Two rules that are easy to skip:

- **A call about a live subject is sealed before the second half of the analysis runs.** Sealed
  after, it is a retrodiction.
- **The register takes negative results.** A wrong call, left in place, is the most valuable row the
  file will hold. Removing one destroys the meaning of every other row.

## Step 3: Seal it

Append one object to the register. Create the file as `[]` if it does not exist.

```json
{
  "id": "fc-0001",
  "sealed_at": "2026-01-15",
  "subject": "",
  "claim": "",
  "resolves_on": "",
  "resolution_criterion": "",
  "confidence": 0,
  "falsifier": "",
  "standing": "",
  "mechanism": "",
  "rival": "",
  "outcome": null,
  "resolved_at": null,
  "scored_note": null
}
```

`outcome`, `resolved_at` and `scored_note` are the only fields a later invocation may write, and
only on resolution. Everything else is immutable once written. Commit the append on its own: the
seal's credibility is the git timestamp, so it must not ride inside a commit doing something else.

## Step 4: Resolution, when the date arrives

Set `outcome` to `right`, `wrong`, or `unresolvable`, with `resolved_at` and a `scored_note` that
says why, including the case where it resolved right for the wrong reason, which is a different
finding from a clean hit.

`unresolvable` means the criterion was written badly. Record it as a lesson about the caller's own
forecasting.

## Where calls come from

A call should already be implied by something the caller was about to say: a forward claim in an
essay or post, a pitch that cites a method, a live case where two explanations predict different
data. A public forward claim that is not in the register is what this skill exists to prevent.

## What this skill must not do

- **Never file a call the caller has not said out loud.** This skill sharpens and seals. It does
  not author the position.
- **Never quote or profile a private individual** in a call or its notes.
- **Never present a forecast as product copy.** A forecast is a stated position by a named person in
  a register.
