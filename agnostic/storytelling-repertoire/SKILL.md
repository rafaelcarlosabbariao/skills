---
name: storytelling-repertoire
description: "Pick the story structure, the visual form and the exemplar that fit one argument or insight, before building any report, deck, slide, post or chart. Indexed by the job the evidence has to do (change over time, comparison, scale, distribution, part-to-whole, cause, hidden system, network or flow, surprise, uncertainty, precedent, the scaffold proposal, one room standing for many). Trigger on 'which format for this insight', 'how should we tell this', 'how do we show this', 'pick the story structure', 'build the deck', 'build the report', 'outline the report', 'what visual for this finding', 'make this slide land', or the start of any report, deck, carousel or data post."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# Storytelling repertoire

A repertoire of story structures and visual forms, indexed by what the evidence has to do. The aim is to show
through empirics and visuals that expose the systems and social theories behind a finding.

Every name, work and date below was checked by web search on 2026-11-18; sources are in
`references/exemplars.md`. Where sources disagreed, the file says so.

## The procedure

1. **Write the insight as one ABT sentence** (Olson 2015): "X, and Y, but Z, therefore W." If it will not go into
   that shape, there is no finding yet; go back to the data.
2. **Name the job.** Pick one row of the table below as the primary job, at most one as secondary. A slide or
   section does one job.
3. **Pick the piece's arc by channel** (`references/structures.md`):
   - Report (site, newsletter): a six-step spine (1 cover, 2 precedent, 3 method, 4 what we saw, 5 limits,
     6 scaffold), opened with an anecdotal lede and nut graf, rising through the observations to one turn, ending
     on the scaffold: a proposal the reader may decline.
   - Site report: martini glass (Segel and Heer 2010): an author-driven stem, then a reader-driven explorer.
   - Deck or carousel: one claim per slide; the claims in order read as the ABT; ends on the scaffold or a
     contact slide, never a lesson. An Instagram carousel opens on a full picture with a text hook on the topic;
     the evidence starts on slide 2.
   - LinkedIn or a summary for a decider: answer first (Minto's SCQA), then the evidence.
4. **Pick the visual form from the row**, then run the evidence grammar on it (`references/visual-forms.md`):
   - **Compared to what?** Every number has a comparator: another group, another year, a threshold, a base rate.
   - **Because of what?** The theory that explains it sits on the chart, in a short ruled note, author and year.
   - **Base named.** n, dates and source on the slide; the sample and the method shown as counts (nested shapes,
     numbered stages) before any finding.
   - **A visual shows a relationship, a change or a mechanism a reader could not see in the table.** A picture
     that only depicts a count fails (crowds drawn as decoration; painted figures used as tally marks). Figures in
     a visual carry a theory or a pattern repeated over time.
5. **Read the row's "fails when" cell** and check your own rules. Suggested defaults: counts only from any social
   corpus, no user comment quoted or paraphrased; no slide whose argument is a quote of the author; nothing
   client-confidential; your style guide.
6. **Build.** Charts and diagrams: use whatever charting or diagram skill you have. Copy the exemplar's move,
   never its look. `scripts/draw-map.py <out.html>` draws the master table as an overview diagram.

## The master table

| Job | Structure | Visual form | Copy this | Fails when | Spine step |
|---|---|---|---|---|---|
| Change over time | ABT: it was, and, but, therefore | Slope or linked bars for two points; annotated line; small multiples for many series | Upshot, 255 Charts (2014); Rosling, 200 Countries (2010) | Two big numbers with no path; truncated axis; animation with no pause to compare | 2, 4 |
| Comparison | Answer first; "compared to what?" | Dot plot or linked bars on one shared scale; small multiples | The Pudding, Film Dialogue (2016) | Unequal bases; dual axes; a comparator picked to flatter | 4 |
| Scale or magnitude | Concrete unit (Heath 2007) | Unit chart or icon array; scroll at true scale | Korostoff, 1-pixel wealth | A big number in no familiar unit; area or radius exaggeration | 1, 4 |
| Distribution or inequality | Reveal the spread, then the case | Strip or beeswarm, histogram, percentile chart | Upshot, top 1% vs bottom 60% (2017) | An average that hides the tails | 4 |
| Part-to-whole, risk, the sample | Nest from whole to part | Icon array or waffle; nested areas for the sample | Galesic et al. (2009); Artsy (2021) sample | More than five parts; a pie of many slices | 3, 4 |
| Cause or mechanism | SCQA; rule out the rivals one by one | Sequenced reveal of candidate causes against the observed; cause and effect on one plane | Bloomberg, What's Really Warming the World (2015); Snow (1854) | Correlation drawn as cause; rivals left out | 4 |
| Hidden system or rule set | Local rules, interactions, the output nobody planned | Explorable simulation; stepped diagram of the rules | Parable of the Polygons (2014), after Schelling (1971) | A toy model read as data; the reader not told which knob matters | 4, 6 |
| Network or flow | Follow one thread through the whole | Flow map, Sankey, two-mode network | Minard (1869); Healy, Paul Revere (2013) | Hairball; flows with no totals | 4 |
| Surprise against expectation | Information gap (Loewenstein 1994): predict, then reveal | "You draw it"; a guess slide, then the answer slide | Upshot, You Draw It (2015) | The truth is unsurprising; the gap too wide to guess at | 1, 4 |
| Uncertainty | Show the outcomes, not one number | Hypothetical outcome plots; ranges; per-case needles | Hullman et al. (2015); NYT needle (2016) and its lesson | A point estimate read as a promise | 4, 5 |
| Precedent, the past rhymes | Then and now, the difference named | Paired timeline; the old record redrawn beside the new | Du Bois, data portraits (1900) | An analogy with the difference left out | 2 |
| A proposal the reader may decline | What is, what could be (Duarte 2010); the case method | One diagram of the scaffold: gap, translator, shared goal, past, tower | Duarte's sparkline of "I Have a Dream"; HBS cases (1920s) | It turns into an instruction or a call to action | 6 |
| One room standing for many | Anecdotal lede, nut graf; anecdote, then reflection (Glass) | The room as one marked dot inside the distribution | Geertz, Deep Play (1972); Snow Fall (2012) | The identifiable-victim effect: the one swamps the many | 1, 4 |

## Channel genre map (Segel and Heer 2010)

| Channel | Genre | Note |
|---|---|---|
| Site report | Martini glass; magazine style with live charts | The explorer is the bowl; the stem is the report |
| Newsletter | Magazine style; annotated chart stills | Same report, charts as stills |
| LinkedIn document | Slide show | One claim per page; source line on each |
| Instagram | Comic strip or slide show | Fewer words, same evidence |
| TikTok | Film, video, animation | One mechanism per clip |

## Related

- `references/structures.md`: the argument and narrative structures, each with when it fits and when it fails.
- `references/visual-forms.md`: the visual forms and the evidence grammar in depth.
- `references/exemplars.md`: every exemplar with its link and the source that verified it.
- `scripts/draw-map.py`: draws the master table as diagrams.
