---
title: The Model Thinker
author: Scott Page
year: 2018
kind: book
theme: simulation
shelf: social-simulation
slug: model-thinker
---

# The Model Thinker

## The claim

Every model is a deliberate simplification that gets some things right by ignoring others. Page's argument is that ensembles of simple formal models, run against the same question, beat both any one model and unaided intuition, and he proves the mathematical version of that claim. The book is a working catalog: a few dozen models with their parameters, each earning a place in the ensemble.

## Core claims

- Many-model thinking is a method, not a metaphor. Apply several structurally different models to one phenomenon and read the agreements and disagreements as the finding.
- The diversity prediction theorem makes ensemble accuracy arithmetic: many-model error equals average model error minus the diversity of the models' predictions. Diversity counts one for one with accuracy.
- Models serve seven distinct uses, REDCAPE: reason, explain, design, communicate, act, predict, explore. A model good for one use can be wrong for another; name the use before choosing the model.
- The shape of a distribution is a diagnosis of its generating process. Normal implies many independent additive causes; power law implies feedback (preferential attachment, self-organized criticality). Check the tail before trusting an average.
- Markov systems with fixed transition probabilities converge to a unique statistical equilibrium regardless of starting point. One-shot shocks wash out; only changing the transition probabilities changes the long run.
- Macro patterns grow from micro rules. Threshold, network, and contagion models turn individual rules into collective curves fit against data.

## Frameworks and models

**Diversity prediction theorem.** For N models predicting value V: (M-bar minus V)^2 = average of (Mi minus V)^2 minus average of (Mi minus M-bar)^2. Crowd squared error = average squared error minus predictive diversity. A mediocre but diverse ensemble can beat a good single model; a redundant ensemble cannot.

**Broadcast, diffusion, Bass.** Broadcast: adopters grow by p times the remaining pool, giving an r-shaped curve that rises fast then flattens. Diffusion: growth is q times adopters times remaining pool over N, giving an S-curve. Bass combines them: dA = p(N - A) + qA(N - A)/N. Meta-analyses put p near 0.03 and q near 0.38 for consumer products. The fitted p to q ratio tells you whether media push or social copying is carrying a trend.

**SIR contagion and R0.** R0 = contact rate times transmission probability divided by recovery rate. Above 1 the thing spreads, below 1 it dies; the immunity threshold is 1 minus 1/R0. Cultural fads have recovery too: people quit. A trend that persists despite churn needs reinfection or superspreaders.

**Markov models.** Finite states, fixed positive transition probabilities, unique equilibrium independent of initial conditions. The practical teeth: interventions that move the state but not the matrix decay back to baseline.

**Power laws via preferential attachment.** New nodes link to existing nodes in proportion to current degree, producing Zipf-like tails where a few items absorb most attention. Self-organized criticality generates the same signature from accumulated stress plus cascades.

**Threshold and local-interaction models.** Granovetter riots, standing ovations, Schelling sorting: each agent acts when participation crosses a personal threshold, and the distribution of thresholds, not the average preference, decides whether a cascade runs.

**Rugged landscapes.** Multi-peaked problems reward diverse heuristics; hill-climbing from one start finds one local peak. Many models are many starting points.

## Decision rules

- If forecasting any cultural quantity, never ship a single-model number. Run at least three structurally different models and report the spread as part of the answer.
- If an adoption curve is r-shaped, credit broadcast (media, algorithmic push). If S-shaped, credit social copying. Fit p and q before naming the driver.
- If a metric has a fat tail, drop averages and normal anomaly bands; hunt for the feedback loop and report the tail behavior instead.
- If a shock produced a visible change, ask whether it altered transition probabilities or just the state. State-only changes will revert; say so in the read.
- If a collective outcome flipped fast, model the threshold distribution before inferring a preference shift.
- If two good models disagree, treat the disagreement as information about the phenomenon, not as a defect to resolve.

## Key terms

- **Many-model thinking:** applying several simple formal models to one phenomenon and reading the ensemble.
- **Diversity prediction theorem:** crowd squared error equals average squared error minus prediction diversity.
- **REDCAPE:** the seven uses of models: reason, explain, design, communicate, act, predict, explore.
- **Bass coefficients p and q:** innovation (broadcast) and imitation (social) forces in an adoption curve.
- **R0:** contacts times transmission over recovery; spread requires R0 above 1.
- **Markov equilibrium:** the unique long-run distribution of a fixed-transition system, independent of history.
- **Preferential attachment:** growth proportional to current size, the standard generator of power-law tails.
- **Rugged landscape:** a multi-peaked problem where local search stalls and diverse heuristics pay.
