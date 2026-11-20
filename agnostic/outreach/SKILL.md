---
name: outreach
description: "Write a tailored cold outreach DM or email from you, given a link (LinkedIn profile, company site, article) and the recipient's job title. Also holds your control brief (the untailored self-introduction) and your verified fact record. Trigger on 'outreach', 'write a DM to', 'cold email this person', 'reach out to', pasting a profile or company link with a job title, or asking for your intro blurb."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# Outreach

Given **a link and a job title**, produce a short outreach message from you that a busy person
will answer.

## Set up once

Two files carry the substance. Copy the examples and fill them with your own facts:

- `references/facts.md` (from `facts.example.md`): **the verified facts.** Every claim in a
  message comes from here. Read it before drafting, every time.
- `references/control-brief.md` (from `control-brief.example.md`): **the control.** Your
  untailored intro at three lengths. Use it verbatim when there is no link or the role is unknown;
  it is also the baseline any tailored draft has to beat.

Both are personal. `*.local.md` is gitignored if you prefer `facts.local.md` and
`control-brief.local.md`; the skill reads whichever exists.

## The job

Most records have two or three halves that rarely appear together in one person (for example, a
technical credential and a community or creative practice). Tailoring is mostly deciding which half
leads, and what the single ask is. List your halves in `facts.md` under **Halves**.

The message is one recognizable person reaching one other.

## Procedure

**1. Read the link.** Fetch it (WebFetch, or browser tools if it is gated). Find at least one
specific, recent, non-obvious thing: a project they shipped, a venue's programming, a line from
something they wrote. Generic flattery ("love what you're doing at X") is the tell of a mass send.

If the link cannot be fetched, say so and draft from the job title alone, flagging that the opener
is unanchored and needs a specific detail before sending.

**2. Read `facts.md`.** Every time. Numbers drift and some are embargoed.

**3. Pick the lane** from the job title, using the **Lanes** table in `facts.md`. A lane maps a
kind of recipient to the half of your record that leads and the angle. A starting shape:

| Recipient | Leads with | The angle |
|---|---|---|
| Hiring manager, recruiter | Your strongest credential | Hard numbers first; side projects as closing color |
| Founder, product, community | Peer register | Shortest message; lead with a published lesson or failure |
| Press, editor, journalist | The story and its numbers | The surprising figure is the hook |
| Research, insights, strategy | The credential plus your field access | What you see that a panel does not |
| Venue, events, partnerships | The practice | What you bring to their room, with proof you have done it |

If the title does not fit a row, ask which lane before guessing. A message aimed at the wrong half
of the record is worse than a late one.

**4. Draft.** Structure, in order:

1. **The anchor:** the specific thing from step 1. One sentence. Proves it was read.
2. **Who you are:** one or two sentences from the lane's half of the record.
3. **The bridge:** why *them*. This is the sentence that earns the reply.
4. **One ask:** small, concrete, easy to say yes to. A 15-minute call, a reply, a date. Never two.

**5. Check it** against the rules below, then output.

## Format and length

| Surface | Limit | Notes |
|---|---|---|
| LinkedIn connection note | **300 characters, hard** | One line plus one ask. Count them. |
| LinkedIn DM / InMail | 600-900 chars | Under 150 words. InMail subject line 200 chars or fewer. |
| Instagram DM | 2-4 sentences | Most casual register. No credential dump. |
| Cold email | 120-150 words | Specific subject line. Close with the signature block in `facts.md`. |

Default to DM length unless told otherwise. State which surface the draft is for, and give the
character count for a connection note.

## Rules

- **Never invent a fact.** Not a number, not a date, not a mutual connection, not a claim about
  their company. If a draft would be stronger with something not in `facts.md`, ask.
- **Respect the embargo list** in `facts.md` (unannounced names, unresolved dates, figures you do
  not cite publicly).
- **One ask.** Two asks get zero replies.
- **Earnest, direct, plain.** No hype adjectives, no "quick question", no fake urgency, no "I'll keep
  this brief" (be brief), no double-negative understatement ("not the worst"); say the plain positive.
- **Keep a published failure or lesson** when there is room. Builders trust a stated loss.
- **No signature block in DMs**, email only.

## Output

Give the draft in a copy-pasteable block, then briefly:

- which lane was picked and why
- the one detail used as the anchor, and where it came from
- anything you must fill in or verify before sending

If the tailored draft is not clearly better than the control brief for this recipient, say so and
send the control. That is a real outcome.
