# Patterns: social-simulation shelf

Reusable techniques that emerge across the shelf. Each pattern gives when to use it, the steps, and the source works. These are procedures, not citations: run them.

## 1. Regime classification before forecasting

**When to use:** before any ensemble forecast or trend call, to decide what kind of prediction is even honest.

**Steps:**
1. Watch the scene's recent behavior and classify it: settles to one state (class 1), cycles or holds a stable structure (class 2), churns aperiodically with no persistent structures (class 3), or shows discrete memes and factions that move, collide, and interact (class 4).
2. Class 1 or 2: trend extrapolation is fine.
3. Class 3: forecast distributions and condition words only, never trajectories or point numbers past the horizon where input error doubles.
4. Class 4: simulate the interactions; this is where lead time exists.
5. Report the regime class alongside the forecast.

**Source works:** a-new-kind-of-science, complexity-mitchell.

## 2. Threshold cascade check

**When to use:** a scene, feed, or audience looks sharply sorted, flipped fast, or is unraveling, and you are tempted to explain it with strong preferences or extremism.

**Steps:**
1. Model mild preferences plus interaction first; escalate the motive story only if the mild model fails to reproduce the pattern.
2. Map the threshold or tolerance distribution across the population, as a distribution, never a point value or a mean.
3. Plot cumulative thresholds against the 45 degree line: crossings from above are stable equilibria, crossings from below are tipping points.
4. Report which side of critical mass the scene sits on, and its distance to tip, not a trend line.
5. Watch the most sensitive members: churn starting there is a possible cascade front, and the tolerance distribution predicts who leaves next.
6. If a mix is holding, find the cap, cost, or institution holding it and watch that mechanism, not the mix.
7. In an audience sim, sweep threshold F and vacancy rate before adding richer psychology; most sorting behavior lives in those two parameters.

**Source works:** dynamic-models-of-segregation, micromotives-macrobehavior, model-thinker.

## 3. Adoption curve fit (Bass r-versus-S check)

**When to use:** any rising trend in fashion, music, language, or food, before writing an origin story into a brief; the taste-versus-algorithm dial.

**Steps:**
1. Fit the Bass model dA = p(N - A) + qA(N - A)/N to the adoption series.
2. Read the shape first: r-shaped (fast rise then flatten) credits broadcast, meaning media or algorithmic push; S-shaped credits social copying.
3. Read the fitted p to q ratio: high p with low q reads as algorithm-fed, high q reads as genuinely social. Benchmarks: p near 0.03, q near 0.38 for consumer products.
4. Ship the fitted ratio as a condition-first dial read; do not name a driver before fitting.

**Source works:** model-thinker.

## 4. Grow-it validation (generative check on a mechanism claim)

**When to use:** anyone, including you, claims "X caused this cultural pattern"; also the standing validation gate for every audience simulation.

**Steps:**
1. State the explanation as agent-level local rules. If it cannot be stated as rules, demote it to narrative.
2. Implement and run the rules; check whether the grown macro pattern matches the observed curve or clustering.
3. Change one rule per run, never two, so causal attribution holds between compared runs.
4. If a tiny rule set reproduces the pattern, resist adding parameters; enumerate the small rule space before enriching.
5. Run the equifinality check: if two distinct rule sets grow the same pattern, withhold confidence in both and hunt for data that discriminates.
6. Hold the final claim loosely: a match identifies a regime, not the one true mechanism.

**Source works:** growing-artificial-societies, a-new-kind-of-science, self-reproducing-automata, dynamic-models-of-segregation.

## 5. Distribution and tail diagnosis

**When to use:** any metric before you trust its average; any attention, reach, or engagement read.

**Steps:**
1. Check the tail. Normal implies many independent additive causes; power law implies feedback, usually preferential attachment or self-organized criticality.
2. If the tail is fat, drop averages and normal anomaly bands; report tail behavior and hunt for the feedback loop.
3. For taste reads, track the exponent gamma of the attention distribution over time: steepening toward lower gamma means the algorithm is winning the domain; a fattening middle means taste is.
4. If a skewed outcome tempts a merit story, remember Sugarscape: uniform inputs plus interaction structure grow Pareto tails on their own.

**Source works:** model-thinker, complexity-mitchell, growing-artificial-societies.

## 6. Network topology read

**When to use:** contagion, fragmentation, or community-health questions in any domain; the lonely and values dials.

**Steps:**
1. Estimate clustering coefficient and mean path length. All weak ties with no clustering is one loneliness failure mode; high clustering with no bridges is the other.
2. For fragmentation (values, gender), watch bridge nodes: whether accounts connecting two clusters still post into both.
3. To slow a contagion on a scale-free graph, act on hubs; random intervention barely moves it.
4. Remember topology dominates content: whether a thing spreads is set by degree distribution and path length before anything about the thing itself.

**Source works:** complexity-mitchell, model-thinker.

## 7. Markov state-versus-matrix check

**When to use:** a shock or intervention produced a visible change and you must forecast whether it sticks; loneliness interventions especially.

**Steps:**
1. Ask whether the event changed the transition probabilities (habits, defaults, venues) or just the current state.
2. State-only changes revert to the old equilibrium; say so in the read.
3. Only a changed matrix moves the long run; look for structural evidence before crediting persistence.

**Source works:** model-thinker.

## 8. Silicon panel build with the four-criteria audit

**When to use:** you need a fast read on how a defined audience would respond to a message, before committing to human research.

**Steps:**
1. Build one first-person conditioning backstory per real or archetypal respondent from full covariates, one silicon individual per person, not one generic persona.
2. Sample many completions per persona; read distributions, never a single completion.
3. Before trusting the panel in a new domain, run the four-criteria audit against a slice of real data from that domain: Social Science Turing Test, backward continuity, forward continuity, pattern correspondence.
4. Check pattern correspondence even when marginals look right; matching averages with broken inter-item structure is a failed simulation.
5. Downgrade confidence for segments with weak or crosscutting identity anchors, and require human confirmation there.
6. If the phenomenon post-dates training data, inject live signal (live trend feeds) into the conditioning context.
7. Reject any "what Gen Z thinks" built from one prompt and one completion: no persona depth, no distribution, no audit.

**Source works:** out-of-one-many, synthetic-survey-data, generative-agents-park.

## 9. Three-moment audit of any synthetic sample

**When to use:** any synthetic panel, simulated audience, or LLM-summarized opinion set is about to feed a claim; the mandatory skeptic pass after pattern 8.

**Steps:**
1. First moment: do synthetic means match real means? Usually yes; this alone proves nothing.
2. Second moment: does synthetic variance match real variance? Expect compression; demand subgroup breakdowns.
3. Covariance: do regressions on synthetic data recover real coefficients with honest uncertainty? Treat synthetic standard errors as fiction and refuse to report significance from them.
4. If the panel is unanimous or near-unanimous, read model artifact, not consensus.
5. If the claim rests on minority or cross-pressured segments, require human data; that is exactly where synthetic fails.
6. Pin the model version, log prompts, rerun under paraphrase, and label output as pilot or hypothesis, never measurement.

**Source works:** synthetic-survey-data, llms-simulate-humans.

## 10. Turing Experiment replication gate

**When to use:** before any synthetic panel or agent sim answers a novel question; the validation protocol for audience simulations.

**Steps:**
1. Make the panel replicate a known human result in the same task family first. No replication, no trust.
2. If the scenario is famous, assume training-data contamination and build novel stimuli before crediting the match.
3. Run the distortion audit: if the simulated crowd is more accurate or more uniform than any real crowd would plausibly be, read hyper-accuracy distortion, not insight.
4. Vary demographics cheaply by names, but validate subgroup effect direction against human data before reporting it.
5. Log refusals, moralizing, or mid-simulation corrections as alignment artifacts, never as participant behavior.
6. Benchmark against a human-roleplay baseline, not against intuition.

**Source works:** llms-simulate-humans, generative-agents-park, synthetic-survey-data.

## 11. Generative-agent society build and ablation

**When to use:** building audience agents or any sim that runs past a few dozen interactions.

**Steps:**
1. Give each agent a memory stream (append-only, natural language) and recency-importance-relevance retrieval; a static persona prompt will not hold a rule set stable over a long run.
2. Add reflection triggered by an importance-sum threshold; without it the run measures drift, not culture.
3. Use recursive planning: day plan, hour chunks, 5 to 15 minute actions, with reaction-triggered replanning.
4. To measure diffusion, seed exactly one agent and count who can recall the item unprompted at interview time; never read message logs as adoption.
5. To claim emergence, run the ablation: remove the component and show the behavior disappears. Otherwise you scripted it.
6. Discount polite, agreeable, formal dialogue as instruction-tuning artifact before reporting consensus or sentiment.

**Source works:** generative-agents-park, llms-simulate-humans.

## 12. Slop signature scan

**When to use:** the trend read's human-versus-AI-slop read, in any domain; judging whether a discourse pattern is human crowds or machine output.

**Steps:**
1. Never use an entropy-based novelty metric alone: slop is high-entropy and low-depth, so the metric ranks it most novel. Score logical depth and provenance instead. Volume up with depth flat is slop, not culture.
2. Check variance: too correct, too central, no human spread is the hyper-accuracy fingerprint of machine text; real crowds always carry more disagreement.
3. Check dialogue texture: consistent memory citation, over-cooperative tone, and low-variance politeness are the detection profile for believable synthetic humans.
4. Classify the copying loop: content re-interpreted as instructions (templates, tutorials, recipes, prompts) is above the reproduction threshold and will self-sustain and mutate; content only copied as data (screenshots of screenshots) copies degeneratively and decays.
5. Remember rule 30: rich, organic-seeming output can come from a trivial deterministic generator. Apparent complexity is not evidence of human depth.
6. Expect lemons dynamics: when readers cannot verify human origin, adverse selection predicts flight to certified-human spaces. Track provenance signals as the counter-move.

**Source works:** complexity-mitchell, llms-simulate-humans, synthetic-survey-data, self-reproducing-automata, a-new-kind-of-science, micromotives-macrobehavior, generative-agents-park.

## 13. Ensemble forecast assembly

**When to use:** every forecast run; any cultural quantity anyone wants a number for.

**Steps:**
1. Never ship a single-model number. Run at least three structurally different models against the question.
2. Log each member model's error and the ensemble's diversity separately, so both terms of the diversity prediction theorem stay visible.
3. Vary seeds and rule sets; treat spread across runs as the confidence statement.
4. Where the system sits near an unstable equilibrium, widen the ensemble: small shocks decide everything there.
5. Map the tipping basin and report distance to tip, not just point forecasts, wherever thresholds govern.
6. Treat disagreement between good models as information about the phenomenon, not a defect to resolve.
7. Silicon-sampled opinion may seed scenario branches, but ensemble weight belongs to observed data, and every silicon member needs the distortion audit first.

**Source works:** model-thinker, complexity-mitchell, growing-artificial-societies, micromotives-macrobehavior, llms-simulate-humans, synthetic-survey-data.

## 14. Instrument check on corpus-wide moves

**When to use:** a signal moves in all eight domains at once.

**Steps:**
1. Suspect the instrument first: systems with no central control rarely move in lockstep, so corpus-wide simultaneity is a plumbing hypothesis before it is a finding.
2. Verify sibling systems and overall volume from the same run before claiming a cultural event.
3. Only after plumbing is cleared, look for a genuine shared driver.

**Source works:** complexity-mitchell.
