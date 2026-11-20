# Patterns: diffusion-contagion shelf

Reusable recipes assembled across the eight works. Each pattern names when to use it, the steps, and its source works. Run the contagion classification pre-pass first; every other pattern depends on its answer.

## 1. Contagion classification pre-pass

**When to use:** before applying any model on this shelf. Every result here silently assumes simple or complex spread, and the two obey different physics.

**Steps:**
1. Name the exact behavior spreading. "Awareness of X" and "doing X in public" are different contagions of the same trend.
2. Price the adoption: money, effort, time, identity risk, social sanction. Free and private means simple; costly or visible means complex.
3. Check the four complexity mechanisms: strategic complementarity (only worth doing if others do), credibility (claims need corroboration), legitimacy (acting alone is deviant), emotional contagion (intensity needs dense company). Any one present pushes toward complex.
4. Assign a threshold: T = 1 for simple, T >= 2 for complex. Follows and views are T = 1; buying, posting, and identity adoption are T >= 2.
5. Route: simple contagions get small-world and weak-tie logic (speed, shortcuts, days-scale forecasts). Complex contagions get wide-bridge and local-density logic (redundancy, concentrated seeding, cluster reads).

**Source works:** complex-contagions, small-world-networks, strength-of-weak-ties.

## 2. Bass curve fit and lifecycle read

**When to use:** you have a first-adoption time series (or a defensible proxy) and need lifecycle position, mechanism decomposition, or a peak forecast.

**Steps:**
1. Assemble period adoptions S(t) and cumulative Y(t). First adoptions only; strip repeat behavior.
2. Regress S on Y and Y squared: S = a + bY + cY^2. Recover m as the positive root of cm^2 + bm + a = 0, then p = a/m and q = -cm. Use nonlinear least squares on the closed form when data is noisy.
3. Sanity-check against durables norms: p around 0.01 to 0.03, q around 0.3 to 0.5. A wildly high p with negligible q is a push, not a wave.
4. Diagnose mechanism: q > p with a slow trickle then acceleration means word of mouth is working, so fit and forecast the peak at t* = ln(q/p)/(p+q) instead of extrapolating the ramp. Deceleration from day one with no inflection means p-driven media or algorithm push; expect decay.
5. Check penetration: near half of m means peak velocity is now. Post-peak decline with a plausible m is pool exhaustion, not death.
6. If accelerating the trend: seed connected adopters for q-driven waves, buy reach for p-driven ones, never media money on an imitation wave.

**Source works:** bass-new-product-growth, diffusion-of-innovations.

## 3. Threshold cascade check

**When to use:** forecasting whether a spread can go global, or auditing a claim that something is about to tip. Also the standing corrective for influencer-credit stories.

**Steps:**
1. Model each member as binary with threshold phi (fraction of active neighbors needed to activate). Estimate the threshold distribution from behavior cost (pattern 1) and audience temperament.
2. Estimate the degree distribution or average degree z of the relevant network.
3. Locate the system in the cascade window: vulnerable nodes are those with degree k <= 1/phi; cascades require them to form a percolating cluster. Too sparse and nothing travels; too dense and no single activation matters.
4. If outside the window, report that no seed works, however famous, and stop.
5. If inside, run seeded simulations and report a distribution of outcomes, never a point estimate keyed to who launched it. Identical systems seeded identically produce duds and wildfires.
6. When two near-identical trends had opposite fates, resist content explanations; expect structural variance and say so.

**Source works:** influentials-watts-dodds, tipping-point (the Watts correction), complex-contagions.

## 4. Bridge audit for crossover

**When to use:** the question is whether a trend jumps from one scene to another: subculture to mainstream, one platform to another, one trend domain to another.

**Steps:**
1. Identify the two clusters and classify the contagion (pattern 1).
2. For awareness (simple): find the bridging weak ties at cluster edges. One local bridge of high degree beats a thousand in-cluster fans. If bridges exist, expect fast traversal; start the clock.
3. For behavior (complex): count the nonredundant overlapping ties between the two clusters. The bridge must be at least as wide as the threshold T. Thin celebrity or press ties predict awareness without adoption.
4. If a trend circulates only inside one tight cluster, log it as redundant chatter. If it surfaces in a structurally distant cluster, a bridge fired.
5. If an intense community fails to export its trend or mobilize, diagnose missing bridges between cliques before blaming the content.

**Source works:** strength-of-weak-ties, complex-contagions, small-world-networks.

## 5. Three-explanation spread test

**When to use:** before writing "X is spreading" about any observed cluster. Clustering has three rival explanations and only one of them is spread.

**Steps:**
1. State the three candidates: contagion (induction), homophily (like chose like), shared environment (common exposure).
2. Check longitudinal ordering: whose change came first? No ordering, no contagion claim.
3. Check directionality: named friends should influence namers; if one-way ties show the effect as strongly as mutual ties, suspect homophily.
4. Check geography and shared context for environmental confounds.
5. Even after passing, treat effect sizes as directional, not precise: homophily and contagion are generically confounded in observational network data (Shalizi and Thomas 2011, Lyons 2011).
6. For "X is everywhere suddenly" reads, add the seed-count question: one seed at degree two, or many independent seeds?

**Source works:** connected.

## 6. Seeding strategy selection

**When to use:** deciding how to launch or accelerate something: one big influencer, many small accounts, or a concentrated cluster.

**Steps:**
1. Classify the contagion (pattern 1).
2. Simple contagion, awareness goal: buy bridges. Seed accounts embedded in multiple scenes; weak-tie traversal does the rest.
3. Complex contagion, adoption goal: concentrate seeds in one neighborhood so local thresholds get crossed, rather than scattering for reach.
4. Influencer versus many-seeds: default to many ordinary seeds (big-seed logic) unless there is direct evidence the audience network sits near the sparse edge of the cascade window, the one region where connected seeds help.
5. Pick individual seeds by centrality and mutual ties, not audience size: a mutual tie carries roughly three times the influence of a one-way tie.
6. Cap expected organic reach at about three degrees per seed; sustained diffusion needs re-seeding, not momentum.

**Source works:** influentials-watts-dodds, complex-contagions, connected, strength-of-weak-ties.

## 7. Five-attribute adoption score

**When to use:** explaining why adoption is fast or slow, or stress-testing hype about a new tool, practice, or aesthetic.

**Steps:**
1. Score the innovation as its adopters perceive it, not as it objectively is, on: relative advantage, compatibility, complexity (inverted), trialability, observability.
2. Discount hype for anything scoring low on compatibility or observability regardless of relative advantage.
3. For value-laden practices, compatibility is the usual failure point; for visible aesthetics and AI tools, observability is the usual win.
4. Recheck at each curve stage: reinvention means the late majority is adopting a different meaning than the innovators did.

**Source works:** diffusion-of-innovations.

## 8. Curve-position and carrier read

**When to use:** any trend signal that needs a lifecycle location: who is carrying this, and what happens next.

**Steps:**
1. Profile the visible discussants into adopter categories. Only innovators (niche forums, no local credibility) means do not forecast take-off. Early adopters and local opinion leaders carrying it means forecast the curve.
2. Check the channel mix: media dominates awareness, peers dominate persuasion. Media coverage with no peer conversation is high p, low q: fast rise, fragile.
3. Take-off test: past roughly 10 to 20 percent of the relevant population, growth self-sustains; shift the question to ceiling and consequences.
4. For interactive behaviors (value grows with users), check critical mass: stalled below it predicts abandonment, not slow growth.
5. Flag algorithmic contamination: when the feed simulates peer persuasion, apparent q is inflated; note it in the read.

**Source works:** diffusion-of-innovations, bass-new-product-growth.

## 9. Shortcut check for cross-domain echo

**When to use:** the same term, sound, or aesthetic surfaces in two unconnected scenes or trend domains within a day or so.

**Steps:**
1. Treat simultaneity as shortcut transmission, not simultaneous invention. Find the bridging account or event before writing a zeitgeist story.
2. Language shows bridge traffic first, because words are the cheapest cargo a bridge can carry. Tech, music, and food are the usual bridging domains.
3. Do not forecast containment for any scene: containment fails at very low rewiring, and a sealed-feeling scene is two shortcuts from anything.
4. When a platform change raises random exposure (recommendation, cross-posting, discovery), model it as raising p in the Watts-Strogatz sense: faster diffusion, flatter geography, clustering intact.

**Source works:** small-world-networks, strength-of-weak-ties.

## 10. Stickiness and context audit

**When to use:** a message is reaching people but not converting, or behavior shifted with no new message in sight.

**Steps:**
1. Reach without conversion: treat as stickiness failure. Edit the message structure and lower the action cost (the tetanus-map move: practical, personal, small action gap) before buying more reach.
2. Behavior shift without a new message: audit context first: environment cues, defaults, group size.
3. Broken Windows generalization: visible low-grade disorder (including slop in a feed) licenses more of it; small visible cleanups can tip the other way.
4. Community past roughly 150 active members: expect norm self-enforcement to weaken and factions or moderation needs to appear.

**Source works:** tipping-point.

## 11. Audience sim parameterization

**When to use:** building or calibrating an agent-based audience simulation from a decoded rule set.

**Steps:**
1. Graph: build the audience as a Watts-Strogatz lattice with an estimated rewiring p, never a random graph (random graphs understate clustering and spread everything too evenly). Report L and C per audience.
2. Agents: give each agent an activation threshold keyed to behavior cost (T = 1 for follows and views, T >= 2 for buying, posting, identity adoption), drawn per segment. Give each agent the Bass hazard p + qF with segment-calibrated p and q, and adopter-category-specific thresholds instead of one average consumer.
3. Influence: encode hyperdyadic decay per hop (roughly 0.57, 0.20, 0.10 as a starting schedule) and weight mutual ties about 3x one-way ties.
4. Bridges: flag members embedded in multiple scenes as bridge nodes; route simulated information events through them, and audit bridge width between segments before predicting crossover.
5. Experiments: run top-degree seeding against random big-seed to tell a creator whether influencer collabs or wide shallow seeding fits their audience.

**Source works:** small-world-networks, complex-contagions, bass-new-product-growth, connected, influentials-watts-dodds, diffusion-of-innovations, strength-of-weak-ties.

## 12. Forecast ensemble construction

**When to use:** building an ensemble cultural forecast where diffusion is the mechanism.

**Steps:**
1. Include Bass members: fit p, q, m on early trend data, propagate parameter uncertainty, forecast peak timing as a distribution.
2. Sweep rewiring p wide: L(p) is steep at low p, so small uncertainty in shortcut count is large uncertainty in arrival time.
3. Sweep threshold distributions: a forecast that a costly behavior jumps communities is only credible if the scenario contains a wide bridge.
4. Bound per-seed organic reach at three degrees; treat seed centrality, not seed count, as the sensitive parameter.
5. Include tipping scenarios where small context changes flip outcomes; report tipping conditions and outcome distributions, never single-trigger point predictions.

**Source works:** bass-new-product-growth, small-world-networks, complex-contagions, connected, influentials-watts-dodds, tipping-point.
