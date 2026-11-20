# Patterns: virality and attention

Reusable procedures assembled from the five chapters on this shelf. Each one is stated as name, when to use, steps, and source works. Run them in roughly the order given when you are working a trend cold: name the unit, classify the psychology, test the structure, then measure the spread.

---

## 1. Replicator readout

**When to use.** First move on any trend, spike, or client brief. Also whenever a conversation keeps naming a creator or a brand rather than a thing that copies.

**Steps.**
1. Write one sentence: "the thing being copied is X." X must be a unit that can be reproduced by someone who has seen it once (a phrase, a silhouette, a sound, a template, a recipe, a claim, a protocol).
2. Separately list the vehicles currently carrying it (people, accounts, feeds, brands, publications).
3. Check the divergence: is the vehicle's interest the same as the replicator's? If a creator is being amplified while the unit itself is not being reproduced, you have a vehicle story, not a trend.
4. If you cannot state X in one sentence, the trend is not yet a trend. Say so instead of forecasting it.

**Source works.** selfish-gene.

---

## 2. Replicator triad score

**When to use.** When you need curve shape or half-life rather than a yes-or-no on spread. Standard input to any forecast run.

**Steps.**
1. Score longevity: how long does one copy survive in the wild before it stops being intelligible or usable?
2. Score fecundity: how many copies per unit time does one exposure generate?
3. Score copying-fidelity: retell it casually and see what survives. Does the unit come through intact, or does it degrade?
4. Read the combination. High fecundity with low fidelity is churn, so expect a spike and a fast decay. High fidelity with low fecundity is a slow burn. Both high is regime change. Never collapse the three into a single "momentum" number.
5. Use fidelity, not volume, as the half-life feature.

**Source works.** selfish-gene.

---

## 3. Wave-or-pocket entropy check

**When to use.** Any time someone asks whether a rising thing is real or local. The single highest-value test on this shelf, and the standing structural test behind trend calls.

**Steps.**
1. Take the earliest adopters, roughly the first 50 adoption events, not the current total.
2. Assign each adopter to a community. On a follower or interaction graph, detect communities (Infomap in the paper, and the result is robust to method). Where you lack a graph, use the audience clusters you already hold: for an audience simulation, the segment map; for the trend read, domain and venue.
3. Compute the three concentration measures: number of infected communities, usage entropy H = -sum over communities c of p(c) log p(c), and the fraction of early interactions that stayed inside a community.
4. Call the regime. Low entropy and high intra-community share means a pocket, so expect a fizzle no matter how loud that community is. High entropy across structurally distant communities means a viral candidate, even at low absolute volume.
5. Explicitly refuse to rank on early counts. If you can afford only one number, publish the entropy, not the total.

**Source works.** predicting-successful-memes.

---

## 4. Simple versus complex contagion regime call

**When to use.** Before extrapolating any scene, subculture, or niche behavior to the mainstream. Especially for identity-heavy or costly behaviors.

**Steps.**
1. Ask whether adoption requires social cover. Does someone need to see several trusted people do it before they will, or does one exposure suffice?
2. Cross-check against the structural evidence from pattern 3. Reinforcement-dependent units show high intra-community interaction and low entropy; single-exposure units leak across weak ties early.
3. If complex, state structural trapping in the read and discount the mainstream extrapolation. If simple, the ceiling is genuinely open.
4. Optional intervention check from the content side: could making the behavior observable (Berger's Public lever) or attaching it to a frequent cue (Triggers) shift it toward single-exposure spread? Be honest that costly and identity-heavy behaviors usually stay bound regardless.

**Source works.** predicting-successful-memes; contagious-berger.

---

## 5. Cascade anatomy readout

**When to use.** Whenever you are about to write the word "spread," "went viral," or "blew up" in client-facing or published work. Replaces view counts.

**Steps.**
1. Define the cascade: one origin assertion plus its unbroken reshare chain.
2. Measure four quantities, not one: depth (hops from origin), size (unique users), maximum breadth (most users at any single depth), and structural virality (mean shortest-path distance between all node pairs).
3. Read the shape. Low structural virality with high breadth is one broadcast hub amplifying, which is reach and not diffusion. High structural virality with real depth is person-to-person spread.
4. Report all four, or say plainly which one you have. Never headline a single count.

**Source works.** true-false-news.

---

## 6. Two-step velocity gate

**When to use.** Before any fast-moving claim enters a trend reading, a brief, or a client deck. Mandatory when the content is political or culture-war shaped.

**Steps.**
1. Step one, velocity and depth anomaly. Is this moving faster and deeper than comparable items in the same domain? Treat unusual speed as a falsehood risk flag, not as evidence of importance. The benchmark from the paper: truth took roughly six times as long as falsehood to reach 1,500 people and about twenty times as long to reach depth 10.
2. Step two, reply-emotion signature. Score reply text for emotion. Surprise plus disgust raises the false-claim prior; sadness, trust, anticipation, and joy lower it.
3. Do not discount a cascade because its carriers are small, new, and unverified. That is the normal profile of a false cascade; falsehood spread despite its carriers, not because of them.
4. If someone attributes the spread to bots, ask for the human-only rerun. Expect bots to explain volume, not a true-false gap.
5. Apply the largest falsehood premium to political and culture-war content, which traveled fastest and deepest of all categories.
6. Verify before quoting. Define veracity exogenously (independent fact-checkers) and then measure diffusion, never the reverse.

**Source works.** true-false-news.

---

## 7. Novelty score against the audience's baseline

**When to use.** Forecasting whether a specific claim or piece will travel with a specific audience. Also for diagnosing why something that worked once stopped working.

**Steps.**
1. Fix the audience. Novelty is relative to what that audience has recently seen, not to what you have seen.
2. Build the exposure baseline: the topic mix that audience encountered over a recent window (60 days in the paper).
3. Represent the candidate item's topic mix the same way (LDA in the paper) and compute distance from the baseline. The paper uses information uniqueness, KL divergence, and Bhattacharyya distance.
4. High distance predicts sharing. Also note the status payoff: passing on novel information confers insider standing on the sharer.
5. Model decay. Novelty falls as exposure accumulates, so the same item scores lower each week. When everything in a domain is novel, nothing is, and the advantage flattens.

**Source works.** true-false-news; predicting-successful-memes (limited attention economy as the substrate).

---

## 8. Arousal-valence pre-pass

**When to use.** On every spike, before interpretation. The standing correction layer for the dial across all 8 domains.

**Steps.**
1. Place the content on the grid. Valence positive or negative, arousal activating or deactivating.
2. Name the fueling emotion in words: anger spike, anxiety spike, awe wave, amusement wave. Do not write "engagement."
3. Apply the direction of effect. Activating emotions raise sharing regardless of valence; sadness and contentment suppress it. From the NYT field model, per one standard deviation increase in the rated dimension: anger about +34 percent on the odds of making the most-emailed list, awe about +30 percent, anxiety about +21 percent, sadness about -16 percent. Treat these as rank-order anchors, not portable constants.
4. Convert to an interpretation rule: anger-fueled volume is activation, not consensus. Do not read a share spike as a change in what people believe.
5. Run the quiet case in reverse. If a domain has gone quiet on a grief-heavy topic, check whether coverage went sad-coded and low arousal before concluding that interest died.

**Source works.** what-makes-content-viral; contagious-berger; true-false-news (surprise as the specific arousal behind false claims).

---

## 9. Two-channel score

**When to use.** When something is spreading with no obvious emotional charge, or when a piece is emotionally hot but is not converting into adoption.

**Steps.**
1. Score channel one, emotional broadcasting: what arousal is discharging into the share?
2. Score channel two, social exchange: what does passing this on do for the sharer or the recipient? Practical usefulness, surprise or interestingness, help, signalling, bonding.
3. Emotionally flat items can still spread hard on channel two. Practical utility carried an effect of comparable magnitude to the emotion terms (roughly +30 percent), and surprise around +14 percent.
4. If both channels are empty and the thing is still moving, go back to pattern 3, because you are probably looking at structure or paid amplification rather than transmission.

**Source works.** what-makes-content-viral; contagious-berger.

---

## 10. STEPPS diagnosis of a dial move

**When to use.** When a domain moves and you need to say why in one line, and when a client asks how to build something that gets talked about.

**Steps.**
1. Walk the six levers and mark which are present: Social Currency, Triggers, Emotion, Public, Practical Value, Stories.
2. Identify the carrying lever, the one doing the work. A thing does not need all six.
3. Forecast from the carrier. Arousal-driven spikes decay fast; trigger-driven ones persist.
4. Run the negative checks. If widely seen but rarely shared, audit social currency: does passing it on raise or lower the sharer's status? If the story is huge but the subject detaches from it, discount the adoption effect, because that is virality without value.
5. If the behavior lives in a private domain, expect slower spread than an observable domain at equal interest, and watch for public proxies to appear before calling a takeoff.

**Source works.** contagious-berger.

---

## 11. Trigger-habitat count

**When to use.** Forecasting persistence rather than amplitude. The concrete answer to "how long will this last."

**Steps.**
1. Describe the audience's daily habitat: the cues they actually encounter, at what frequency.
2. Count how many of those cues are linked to the unit. A phrase anchored to a daily cue persists; an orphaned coinage dies.
3. Score trigger frequency and habitat fit rather than cleverness or launch buzz.
4. Combine with pattern 2. Trigger-poor and arousal-rich means a short half-life. Trigger-rich means ongoing word of mouth even at modest interest.
5. Separate the outcome variables explicitly in the writeup: immediate word of mouth and ongoing word of mouth are different lines.

**Source works.** contagious-berger.

---

## 12. Share-layer versus view-layer split

**When to use.** Slop reads, taste-versus-the-algorithm reads, and any case where impressions and transmission disagree.

**Steps.**
1. Pull the two layers separately: views or impressions on one side, shares or reshares or reproductions on the other.
2. Ask the status question on the share layer. Sharing AI slop costs status, so the predicted equilibrium is slop winning views while human work wins transmission.
3. Watch transmission over production. Generative systems push fecundity and fidelity toward the limit while decoupling the unit from any benefit to its host, so raw output volume stops being informative.
4. Note the selection environment. The recommender is the environment and ranking is the fitness function, so a change in ranking is a change in selection pressure, not a change in taste.
5. Report the divergence itself as the finding.

**Source works.** contagious-berger; selfish-gene; predicting-successful-memes.

---

## 13. Co-adapted complex trace

**When to use.** Values, gender, and any belief-shaped signal. Whenever a position seems to arrive prepackaged with other positions.

**Steps.**
1. List the items that co-occur in carriers of the focal belief.
2. Test mutual reinforcement: does holding one raise the survival odds of the others inside the same host?
3. If yes, name the complex and track it as the unit, not the item.
4. Set expectations accordingly. Refuting one item leaves the complex intact, so do not forecast collapse from a single debunk.

**Source works.** selfish-gene.

---

## 14. Frequency-dependent equilibrium read

**When to use.** When two behaviors, aesthetics, or positions have coexisted at a steady ratio and everyone keeps predicting one will win.

**Steps.**
1. Plot the ratio over time rather than each side's level.
2. If the ratio is stable, stop hunting for a winner and report the ratio as the finding.
3. Check invadability. An outcome that is better for everyone can still be unstable if a single alternative strategy can invade it, which is why the collectively better state is not the prediction.
4. In an audience simulation, use this to call a segment mix stable rather than transitional. In a forecast ensemble, land the forecast on a ratio band rather than a point.

**Source works.** selfish-gene.

---

## 15. Audience transmission rule set

**When to use.** Building or revising an audience rule set for agent-based simulation. This is the composite recipe that turns the shelf into parameters.

**Steps.**
1. Per segment, encode sharing behavior as STEPPS weights: which of the six levers this audience actually responds to.
2. Give each agent a share probability that is a function of arousal, with sadness as an explicit suppressor, and specify which arousal emotions this audience discharges into sharing.
3. Add a transmission multiplier of 1.7 for high-novelty claims, and emotion-conditioned share rules where surprise and disgust boost spread and sadness dampens it.
4. Modify per-agent transmission probability by arousal level and by trigger frequency in that agent's habitat.
5. Implement transmission as imitation with an explicit mutation rate, which is the operational form of copying-fidelity.
6. Assign agents to communities and score any candidate message on predicted concentration. Content whose early resonance stays inside one cluster is retention material; content that bridges clusters is growth material.
7. Where two strategies coexist, use the hawk-dove style equilibrium to declare a segment mix stable rather than mid-transition.

**Source works.** contagious-berger; what-makes-content-viral; true-false-news; predicting-successful-memes; selfish-gene.

---

## 16. Forecast feature pack

**When to use.** Specifying features for an ensemble cultural forecast.

**Steps.**
1. Amplitude features: the arousal profile of coverage predicts spike amplitude; weight candidate framings by arousal class, giving anger and awe framings higher transmissibility priors than sad or content ones.
2. Persistence features: trigger habitat density and copying-fidelity predict half-life. Trigger-poor and arousal-rich signals get short half-lives.
3. Leading indicator: adopter-community entropy at first observation.
4. Explicit exclusion: do not use early popularity as a headline predictor, because it is a weak predictor of final popularity.
5. Contested-claim adjustment: assume the false variant reaches audiences roughly six times faster, give political variants the largest premium, and decay the novelty term as exposure accumulates.
6. Scenario attractors: use frequency-dependent equilibria so forecasts land on a ratio band rather than a point.

**Source works.** contagious-berger; what-makes-content-viral; predicting-successful-memes; true-false-news; selfish-gene.

---

## 17. De-bias a most-shared sample

**When to use.** Any time a share chart, most-emailed list, or reshare ranking is about to be read as evidence of what people believe or how common something is.

**Steps.**
1. State the bias out loud: what tops sharing charts is a biased sample of culture, over-representing arousing content.
2. Reclassify the top items by arousal (pattern 8). If the list is anger-heavy or awe-heavy, the list is measuring activation.
3. Correct before inferring prevalence or agreement. Expect the share of voice on high-arousal pressure systems to overstate real-world division.
4. Add the offline correction where adoption is the real question. Roughly 7 percent of word of mouth happens online, so platform-only measurement misses the dominant channel.

**Source works.** what-makes-content-viral; contagious-berger.
