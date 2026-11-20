# Cheatsheet: social-simulation shelf

Decision tables for live analysis. Situation in, model out, first check named. Details and steps live in patterns.md; definitions in glossary.md.

## Situation to model

| Situation | Which model applies | Check first |
|---|---|---|
| A scene, feed, or audience looks sharply sorted | Schelling spatial proximity / checkerboard (dynamic-models-of-segregation) | Whether mild thresholds plus exit options explain it before inferring strong preferences; sweep threshold F and vacancy rate |
| A mixed community is holding | Bounded-neighborhood model (dynamic-models-of-segregation) | What cap, quota, or institution is cutting the cascade short; watch that mechanism, not the mix |
| A collective outcome flipped fast | Threshold / critical mass (micromotives-macrobehavior, model-thinker) | The threshold distribution and which side of critical mass the scene sits on, before inferring a preference shift |
| A scene, seminar, or group chat is fading | Dying seminar / unstable equilibrium (micromotives-macrobehavior) | Distance to the unstable point; near it, small shocks decide everything, so widen the ensemble |
| Everyone complains but nobody deviates | Multi-person prisoner's dilemma (micromotives-macrobehavior) | The minimum coalition size k; look for the binding rule, not the persuasion campaign |
| Quality is unverifiable in a market (human vs slop) | Lemons market (micromotives-macrobehavior) | Provenance signals, certification, signaling: the counter-moves adverse selection predicts |
| Attention, reach, or wealth looks skewed | Preferential attachment / Sugarscape (model-thinker, growing-artificial-societies) | The tail exponent, and whether uniform inputs plus interaction would grow the same skew before crediting merit |
| An adoption curve is rising | Bass model (model-thinker) | r-shaped vs S-shaped; fit p and q before naming media push or social copying as the driver |
| A trend persists despite churn | SIR contagion (model-thinker) | R0 and the reinfection or superspreader mechanism; fads have recovery too |
| An intervention produced a visible change | Markov model (model-thinker) | Whether it changed transition probabilities or just the state; state-only changes revert |
| Group conflict is escalating | Rule K plus C_alpha, tags plus scarcity (growing-artificial-societies) | Tag consolidation and resource tightening before assuming deep ideological cause |
| A format or meme is spreading | Universal constructor / tape (self-reproducing-automata) | Whether it ships its own build instructions (template, tutorial, recipe, prompt) or is copied only as data |
| A pattern looks random | Intrinsic randomness generation (a-new-kind-of-science) | Whether a simple internal rule of the community or platform could generate the texture before crediting an outside shock |
| A signal moves in all eight domains at once | Instrument check (complexity-mitchell) | The plumbing; decentralized systems rarely move in lockstep, so verify sibling systems and overall volume same run |
| Fragmentation in values or gender discourse | Bridge nodes on the network (complexity-mitchell) | Whether accounts connecting two clusters still post into both |
| Loneliness read in relationships, work, body | Clustering vs path length (complexity-mitchell) | Which failure mode: all weak ties with no clustering, or high clustering with no bridges |
| Need to slow or speed a contagion | Scale-free network (complexity-mitchell) | Hubs; random intervention barely moves a scale-free graph |
| Stated rules and observed output disagree | Emergence (complexity-mitchell, growing-artificial-societies) | Nothing; the gap is the finding |

## Forecast posture by regime

| Regime observed | Posture | Rule |
|---|---|---|
| Stable or cyclic (class 1 or 2) | Extrapolate | Trend lines are honest here |
| Chaotic churn (class 3) | Distributions only | Condition word plus spread; no point numbers past the horizon where input error doubles |
| Discrete memes and factions interacting (class 4) | Simulate | This is where lead time exists; run the interactions |
| Near an unstable equilibrium or tipping point | Widen the ensemble | Report distance to tip and the tipping basin, not a trajectory |
| Fixed transition structure, one-shot shock | Expect reversion | Only a changed matrix moves the long run |
| Any regime, any forecast | Ensemble | At least three structurally different models; spread is the confidence statement; disagreement is information |

## Synthetic panel trust ladder

| What you want from the panel | Verdict | Required gate |
|---|---|---|
| Hypothesis generation, message piloting | Allowed | Full covariate backstories, many samples per persona, distributions not single completions |
| Group-level averages for a strong-identity segment | Allowed with caution | Four-criteria audit against real data in that domain; pattern correspondence, not just marginals |
| Variance, spread, or disagreement claims | Refuse | Variance compression is systematic; real crowds always carry more disagreement than the model returns |
| Regression, segment comparison, significance | Refuse | Synthetic standard errors are fiction; coefficients move and intervals collapse |
| Minority or cross-pressured segment claims | Refuse; require human data | The model erases atypical members of groups, exactly the people who change a cultural read |
| Weak-identity segment (the pure-independent case) | Downgrade | Too little to condition on; human confirmation required |
| Novel question in a new task family | Gate first | Turing Experiment: replicate a known human result in the same family first; no replication, no trust |
| Famous scenario | Gate first | Assume contamination; build novel stimuli before crediting the match |
| Post-training-cutoff phenomenon | Gate first | Inject live trend signal into the conditioning context; conditioning alone will not reach it |
| Anything shipping to a client | Label and pin | Pin model version, log prompts, rerun under paraphrase; label pilot or hypothesis, never measurement |

## Slop signatures (human vs machine read)

| Signal | Reading | Source |
|---|---|---|
| High entropy, low logical depth, volume up with depth flat | Slop, not culture | complexity-mitchell |
| Answers too correct, too central, no human spread | Hyper-accuracy distortion, machine text | llms-simulate-humans |
| Near-unanimous simulated or summarized opinion | Model artifact, not consensus | synthetic-survey-data |
| Over-cooperative, formal, low-variance politeness | Instruction-tuning artifact | generative-agents-park |
| Copying loop that degrades per generation (screenshots of screenshots) | Below the reproduction threshold; expect decay | self-reproducing-automata |
| Format shipping its own instructions | Above threshold; expect self-sustaining spread and mutation | self-reproducing-automata |
| Rich, organic-seeming texture | Not evidence of human depth; rule 30 comes from one line | a-new-kind-of-science |
| Unverifiable origin plus flight to certified spaces | Lemons dynamics running; track provenance counter-moves | micromotives-macrobehavior |

## Quick rules

- Never infer preferences from sorted outcomes, and never infer outcomes from polled preferences. Model the interaction.
- Never ship a single-model number. Three structurally different models minimum; report the spread.
- One rule change per run. Two changed rules between compared runs voids the comparison.
- A sim that matches the data identifies a regime, not the mechanism. Run the equifinality check.
- Thresholds enter as distributions, never point values. The tail tips before the median moves.
- Simulation output is never read back as member intent.
- Emergence claims require ablation: remove the component, show the behavior disappears.
- Diffusion in a sim is measured by unprompted recall at interview, never by message logs.
- Matching the mean is not matching the population. Demand the variance and the subgroups.
- Before a behavioral claim, run the musical-chairs check: choice pattern or closed-system identity?
- If a shock moved the state but not the matrix, say reversion in the read.
- Fat tail: drop the average, report the tail, hunt the feedback loop.
- Corpus-wide simultaneity is a plumbing hypothesis before it is a finding.
- Pin model versions and log prompts, or the synthetic result is not a finding.
