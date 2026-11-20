---
title: Dynamic Models of Segregation
author: Thomas Schelling
year: 1971
kind: paper
theme: simulation
shelf: social-simulation
slug: dynamic-models-of-segregation
---

# Dynamic Models of Segregation

## The claim

Mild individual preferences about who your neighbors are, none of them a preference for segregation, can aggregate into near total segregation. Schelling shows this with hand-run agent models (coins on a grid, predating cheap computing) in the Journal of Mathematical Sociology, 1971. The macro outcome is not a scaled-up copy of the micro motive: collective results cannot be read off individual intent, in either direction.

## Core claims

- Extreme macro sorting emerges from mild micro preferences. Agents content to be a local minority (wanting only one third of neighbors like themselves) still produce heavily segregated maps.
- The mechanism is a cascade: each departure worsens the ratio for those who stay, pushing the next most sensitive person past threshold. Unraveling is sequential, not simultaneous.
- Mixed states are typically unstable equilibria. Fully sorted states are the attractors. A mix persists only under special conditions (caps, quotas, matched tolerance distributions), not by default.
- Tipping is real and asymmetric: out-group entry past some threshold triggers cascading in-group exit, and the process does not reverse by running it backward.
- Observed segregation is therefore weak evidence about preferences. A 90 percent sorted system is compatible with a population that mostly wanted mixing.
- The method itself is a claim: grow the phenomenon from local rules and see if the output matches reality. This is the founding move of agent-based social simulation.

## Frameworks and models

**Spatial proximity model (line and checkerboard).** Two agent types on a line (about 70 agents, each attending to the 4 nearest on each side) or on a grid of roughly 200 cells with 25 to 30 percent vacancies, each cell's neighborhood being the 8 surrounding cells. Parameters: neighborhood size n, tolerance threshold F (minimum fraction of like neighbors required to stay; Schelling ran F = 1/3 and F = 1/2 among others), vacancy rate, and a movement rule (a discontented agent moves to the nearest vacant position satisfying its demand). Result: final like-neighbor shares far exceed any individual's demand; with F = 1/2 the typical final neighborhood is around 4:1 like to unlike. Lowering F softens but does not eliminate sorting.

**Bounded-neighborhood model.** One shared area (a neighborhood, a school, a scene) rather than a grid. Each person has a tolerance ratio: the maximum other-to-own ratio they accept before leaving. Tolerance is distributed across the population; Schelling uses a linear schedule (the most tolerant member accepts 2:1, declining linearly to zero). Plotting each group's tolerated presence of the other yields overlapping parabolas whose intersections are the equilibria. Mixed equilibria exist but are unstable; the stable equilibria are all-one-group. Capacity limits or quotas can create a stable mixed point by cutting the cascade short.

**Tipping.** Extends Grodzins' tipping-point observation: once out-group presence crosses the tolerance of the least tolerant members, their exit degrades the ratio for the next tier, and the area flips. The tipping threshold is a property of the tolerance distribution, not of any individual.

## Decision rules

- If a scene, platform, or audience looks sharply sorted, do not infer strong exclusionary preferences. First test whether mild thresholds plus exit options explain it.
- If you observe a mixed community, treat it as unstable by default. Ask what cap, cost, or institution is holding it, and watch that mechanism, not the mix.
- If churn starts among a community's most sensitive members, read it as a possible cascade front, not noise. The tolerance distribution predicts who leaves next.
- If you want to preserve a mix, act on thresholds and caps, not average sentiment. Persuading the median member does nothing if the tail tips first.
- If simulating an audience, sweep threshold F and vacancy rate before adding richer psychology. Most sorting behavior lives in those two parameters.

## Key terms

- **Tipping point**: the composition level past which cascading exit becomes self-sustaining; set by the tolerance distribution, not any individual.
- **Tolerance schedule**: the distribution across a population of the maximum other-to-own ratio each member will accept.
- **Unraveling**: the sequential cascade where each departure pushes the next most sensitive member past threshold.
- **Unstable equilibrium**: a mixed state that satisfies everyone but collapses under any small perturbation.
- **Spatial proximity model**: the grid model where each agent evaluates only its adjacent cells.
- **Bounded-neighborhood model**: the shared-area model where everyone evaluates one aggregate composition.
- **Micromotives vs macrobehavior**: Schelling's later name for the core lesson; macro outcomes are not readable from micro intent in either direction.
