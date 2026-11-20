---
name: virality-attention
description: "Reference shelf: Dawkins' The Selfish Gene (1976), Berger and Milkman's What Makes Online Content Viral? (2012), Berger's Contagious (2013), Weng, Menczer and Ahn's Predicting Successful Memes Using Network and Community Structure (2014), and Vosoughi, Roy and Aral's The Spread of True and False News Online (2018). Load this shelf when a cultural-analysis question is really a transmission question: 'is this a wave or a pocket', 'why did this spread', 'will this trend persist or fizzle', 'is this spike real or is it just loud', 'should the dial headline this number', 'why is this domain quiet', 'which framing will travel further', 'is this moving because it is true or because it is novel', 'what makes this shareable', 'how long is the half-life', 'why do the views not convert into shares', 'should I trust this claim that is going around', 'what transmission parameters go into the audience sim', 'which feature belongs in the forecast ensemble'. Also load it before writing any trend reading that quotes volume, before assigning per-agent share probabilities in audience simulation, and before treating a most-shared or most-emailed list as a measure of what people actually believe."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# Virality and attention: why content spreads

## What this shelf is for

Five works, one question: given that attention is scarce and most things die, what decides which cultural units get copied. The shelf spans forty-two years and three disciplines (evolutionary biology, consumer psychology, network science) and it does not agree with itself. That disagreement is the useful part. Each work answers a different sub-question well and fails at the others, so the practitioner's job is to know which one you are actually asking.

Used correctly, this shelf gives the trend read a grammar for reading any dial move, gives audience simulation its transmission parameters, and gives forecast ensembles their leading-indicator features.

## The unified model: five questions, in order

Every read on this shelf runs the same spine. Answer the questions in order; skipping one is where bad calls come from.

**1. What exactly is being copied?** Dawkins' replicator-and-vehicle split is the first cut. The replicator is the thing that makes copies (a phrase, a silhouette, a sound, a recipe, a claim). The vehicle is whatever carries it (a person, a creator, a feed, a brand). Confusing them produces the most common analytic error in cultural work: reading a trend as a statement about the creator who happens to be the current vehicle. Name the unit before you measure anything.

**2. What makes an individual pass it on?** This is the psychology layer and it splits into two channels. Channel one is arousal: Berger and Milkman show that physiologically activating emotions (awe, anger, anxiety, amusement) raise sharing and deactivating ones (sadness, contentment) suppress it, regardless of whether the content feels good. Channel two is exchange: practical utility, surprise, and status signaling drive sharing without any emotional charge. Berger's STEPPS is the operational version of both channels: Social Currency, Triggers, Emotion, Public, Practical Value, Stories.

**3. Where did the first copies land?** Weng, Menczer and Ahn show that the structure of the earliest spread predicts final popularity better than either content or early volume. First adopters concentrated in one network community means the thing is held there by reinforcement and will fizzle. Early adoption already crossing several structurally distant communities marks a real viral candidate even at small absolute counts.

**4. What shape did the spread take?** Vosoughi, Roy and Aral give the measurement kit: cascade depth, size, maximum breadth, and structural virality. Low structural virality is one broadcast hub; high is genuine peer-to-peer diffusion. A view count cannot tell these apart, and only one of them is spread.

**5. What is the selection environment?** All five works sit on the same substrate: a limited attention economy where units compete for bandwidth that does not grow. Dawkins names it the meme pool, Weng et al. make it the paper's premise, Vosoughi et al. make novelty the currency inside it. Change the ranking function and you have changed the fitness function, not people's taste.

## Through-lines

**Quality is not the fitness function.** Dawkins states it flatly: meme fitness is independent of truth and of benefit to the host. Weng et al. demonstrate it structurally (community features beat content-based baselines). Vosoughi et al. demonstrate it empirically in the hardest case: falsehood beat truth on depth, size, breadth, and structural virality, with a 1.7 odds ratio on retweeting after controlling for follower count, account age, activity, and verification. If your explanation for why something spread is that it was good or that it was true, you have not explained anything.

**Counts lie; structure tells.** Weng et al. show early popularity is a weak predictor of final popularity. Vosoughi et al. insist on reporting depth, breadth, and structural virality rather than a single number. Berger separates immediate from ongoing word of mouth as different outcome variables. All three converge on the same operating rule for the trend read: a dial read should name the regime a trend is in, not quote its raw volume.

**The sharer is acting in self-interest.** Sharing is a status and relationship move. Berger's social currency lever, the exchange channel in Berger and Milkman, and the insider status that novelty confers in Vosoughi et al. are three descriptions of one thing. This is why the share layer and the view layer diverge, and why the divergence is diagnostic.

**Both the person and the platform are downstream of an older bias.** The falsehood advantage in Vosoughi et al. was measured largely before heavy algorithmic ranking, and removing bot traffic did not change the result. Humans produced the differential. Algorithms amplify a preference people already had.

**Measurement surfaces are biased samples.** Most-shared and most-emailed lists over-represent arousing content, so they measure activation, not prevalence or agreement. Berger's other correction runs the same way: roughly 7 percent of word of mouth happens online, so platform-only measurement systematically misses the channel that carries most adoption.

## Where the works disagree

**Content design versus network structure.** Berger's whole thesis is that contagious content is made, not born, and that message design beats messenger selection. Weng et al. run the opposite experiment and find that content-based baselines lose to community-structure features computed from the first fifty tweets. These are not reconcilable as stated. The working resolution: content properties set a unit's transmission probability per exposure, structure decides how many independent exposure opportunities that unit ever gets. Berger tells you what to build. Weng et al. tell you whether it escaped. Do not use Berger to predict ceiling and do not use Weng et al. to write a brief.

**Valence.** Berger and Milkman report that positive content is more viral than negative on average once arousal and everything else is controlled. Vosoughi et al. find falsehood's winning emotional signature is surprise plus disgust, which is neither positive nor merely aroused. The reconciliation the chapters themselves offer: the arousal that powers falsehood is specifically novelty-linked surprise. Treat surprise as a distinct engine, not as generic high arousal, whenever you are dealing with a contested claim.

**Simple versus complex contagion.** Weng et al. make regime a property of the meme, diagnosed from its early footprint: viral memes travel like a disease on single exposures, niche memes need reinforcement and get structurally trapped. Berger's Public lever implies the same thing from the content side, since observable behaviors get imitated and private ones stall. The tension is about which side you can intervene on. In practice, run the structural diagnostic first, then ask whether a Public or Trigger intervention could move it, and be honest that identity-heavy or costly behaviors usually stay community-bound regardless.

**Agency.** Berger's book is an engineering manual. Dawkins' frame is that the replicator's interest and the host's interest are different questions, and a meme can spread while damaging its carriers. When a client asks how to make something spread, Berger is the right register. When you are reading culture rather than building in it, Dawkins is the corrective, and it is the sharper tool for the slop system in particular.

**Three different dependent variables.** Berger: immediate versus ongoing word of mouth. Weng et al.: whether final popularity lands in a top percentile. Vosoughi et al.: cascade geometry. These are not interchangeable, and most sloppy virality arguments come from swapping them mid-sentence. Pick the outcome variable before you pick the model.

## When each work is the right tool

**selfish-gene** when you need to know what unit you are tracking, when a format is degrading on each retelling, when a belief arrives bundled with three others, when two behaviors have coexisted at a steady ratio and someone keeps predicting a winner, or when you need half-life intuition (fidelity predicts persistence, fecundity predicts amplitude).

**what-makes-content-viral** when a spike needs to be classified before it is interpreted, when you are choosing between candidate framings, when a domain has gone quiet and you need to know whether that means absence of feeling or just sad-coded coverage, or when you are setting per-agent share probabilities in a simulation.

**contagious-berger** when the question is design or persistence rather than measurement: which lever is carrying a spike, whether ongoing word of mouth has any trigger to hang on, whether a widely seen thing is share-negative on status, whether a story is carrying its subject or detaching from it.

**predicting-successful-memes** when the question is wave or pocket. This is the ranking test for any candidate trend and the strongest single-metric answer on the shelf: adopter entropy across communities, not adopter totals.

**true-false-news** when a claim rather than a taste is moving, when velocity looks anomalous, when the content is political or culture-war shaped, or when you need a defensible measurement vocabulary for the word "spread" in client-facing work.

## Chapter index

| slug | work (author, year) | one-line | when to load |
| --- | --- | --- | --- |
| `selfish-gene` | The Selfish Gene (Dawkins, 1976) | Replicators are selected on longevity, fecundity, and copying-fidelity, and meme fitness is independent of truth or benefit to the carrier. | Read `chapters/selfish-gene.md` when you need to name the replicating unit, forecast curve shape or half-life, trace a bundled belief complex, or explain spread that visibly costs its carriers. |
| `what-makes-content-viral` | What Makes Online Content Viral? (Berger and Milkman, 2012) | Arousal, not valence, drives sharing: anger, awe, and anxiety lift transmission while sadness suppresses it, with utility and surprise on a separate channel. | Read `chapters/what-makes-content-viral.md` when classifying a spike's fueling emotion, comparing candidate framings, correcting a share-based sample, or setting agent share probabilities. |
| `contagious-berger` | Contagious: Why Things Catch On (Berger, 2013) | Six designable drivers (STEPPS) govern word of mouth, and triggers rather than interest govern whether talk persists. | Read `chapters/contagious-berger.md` when diagnosing which lever carries a move, forecasting persistence from trigger habitat, or auditing why a widely seen thing is not being passed on. |
| `predicting-successful-memes` | Predicting Successful Memes Using Network and Community Structure (Weng, Menczer and Ahn, 2014) | Community concentration of the earliest adopters predicts final popularity; early volume does not. | Read `chapters/predicting-successful-memes.md` on any wave-or-pocket call, any ranking of candidate trends, and before extrapolating a scene to the mainstream. |
| `true-false-news` | The Spread of True and False News Online (Vosoughi, Roy and Aral, 2018) | Falsehood travels farther, faster, deeper, and more broadly than truth, driven by novelty and by humans rather than bots. | Read `chapters/true-false-news.md` when a claim is moving unusually fast, when content is political, when you need cascade metrics instead of view counts, or when someone blames bots. |

## Companion files

- **`glossary.md`** when a term from any chapter needs a precise definition, when you are writing client-facing copy and want the shelf's vocabulary used correctly, or when two works appear to use the same word (meme, contagion, arousal) for different things.
- **`patterns.md`** when you have a live artifact or trend in hand and need a procedure: the entropy check, the cascade anatomy readout, the STEPPS diagnosis, the novelty score, the replicator triad, the audience transmission rule set.
- **`cheatsheet.md`** when you are mid-read and need the fast answer: which model applies to this situation, what to check first, which domain runs on which mechanism, and which numbers from these papers are portable versus rank-order only.

Cross-shelf: threshold cascades, Bass curves, and weak-tie diffusion live on `diffusion-contagion`. Artificial-market and social-influence experiments live on `status-taste-markets`. Agent-based implementation lives on `social-simulation`. This shelf answers why a unit is transmissible; those answer how a population converts.
