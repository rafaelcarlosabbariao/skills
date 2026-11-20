---
title: Social Influence Leads to the Formation of Diverse Local Trends
author: Ziv Epstein, Matt Groh, Abhimanyu Dubey & Alex Pentland
year: 2021
kind: paper
theme: cultural-markets
shelf: status-taste-markets
slug: diverse-local-trends
---

# Social Influence Leads to the Formation of Diverse Local Trends

## The claim

The MusicLab sequel, run on AI-generated images instead of songs (Proc. ACM HCI, CSCW 2021). Social influence again produces unequal, unpredictable, winner-take-all markets, but with content embedded in a measurable feature space the authors can see what MusicLab could not: within each market, influence pulls the winners together into a coherent local trend, while parallel markets drift apart. Influence homogenizes each market internally and spawns divergent local trends across markets: global diversity survives as an archipelago of local monocultures.

## Core claims

- MusicLab replicates outside music. On a platform where participants discover and curate GAN-generated hybrid animals ("ganimals"), exposing popularity signals increases inequality of success and makes winners unpredictable across otherwise identical worlds.
- Presentation matters, not just information. The presence of social signals and their visual salience (how prominently popularity is displayed and used to order content) were randomized separately; more salient signals push the market further toward winner-take-all.
- Winners inside an influence world are morphologically similar. Popular items cluster in the generative model's feature space, which makes them a trend rather than a bag of unrelated hits.
- Parallel influence worlds diverge in feature space over time. Different worlds lock onto different regions, so the mechanism that narrows taste locally diversifies it globally.
- Trend content is path dependent. Early random fluctuations, amplified by cumulative advantage, decide not just which item wins but what kind of item wins in a given world.
- A trend is a property of a community, not of the culture. Observing one market tells you little about which trend a sibling market has formed.

## Frameworks and models

**Parallel-worlds experiment (Salganik, Dodds & Watts 2006, re-adapted).** Multiple identical markets seeded with the same items; participants randomly assigned to one world; influence worlds show others' behavior, the independent condition does not. Original MusicLab: 14,341 participants, 48 songs, 8 influence worlds plus 1 independent world. This paper ports the design to the Meet the Ganimals platform and adds a second randomized factor: the visual salience of the social signal.

**Inequality and unpredictability metrics.** Inequality of success is the Gini coefficient G over items' market shares. Unpredictability U is the mean absolute difference in an item's market share across pairs of worlds, averaged over items: high U means identical initial conditions yield different winners.

**Morphological embeddings.** Each ganimal is a point in the generative model's latent space, so "what the trend looks like" is quantifiable. Local trend formation: mean pairwise similarity of a world's popular items rises over time under influence. Divergence: distance between the popularity-weighted centroids of different worlds grows over time. This is the paper's methodological contribution: trends measured as regions of feature space, not ranked lists.

**Cumulative advantage.** Rich-get-richer feedback on early popularity decouples outcomes from intrinsic appeal between a quality floor and ceiling; here it operates on features, not just items, seeding each world's distinct trend.

## Decision rules

- If a trend is surging inside one community, then check sibling communities before calling it macro. The same dynamics predict different winners elsewhere. One world is a finding, all worlds is a shift.
- If a platform makes popularity signals salient (ranked feeds, visible counts), then expect higher inequality and unpredictability there; discount early leaderboard position as evidence of quality or durability.
- If you need to compare trends across communities, then embed the content and compare centroids over time, not item rankings. Two communities can share zero items and still share a trend region, or share items and be diverging.
- If within-community similarity of winners is rising, then a local trend is locking in; forecast within that community and treat cross-community extrapolation as unsupported.
- If a platform hides or removes social signals, then expect flatter success distributions that track quality more closely, and more stable predictions.

## Key terms

- **Parallel-worlds design**: identical markets run simultaneously so divergence can only come from social dynamics, not content or population differences.
- **Social influence condition**: participants see others' behavior (popularity counts, orderings); the independent condition hides it.
- **Signal salience**: how prominently popularity information is displayed and used to arrange content; a separate causal lever from its mere availability.
- **Gini coefficient (G)**: inequality of market share across items; higher under influence.
- **Unpredictability (U)**: mean absolute market-share difference for the same item across worlds; the measure of how little initial conditions determine winners.
- **Morphological embedding**: an item's coordinates in the generative model's feature space, letting trend content be measured directly.
- **Local trend**: a region of feature space a single world's winners converge on; coherent within, divergent across worlds.
- **Cumulative advantage**: early random popularity compounding into winner-take-all outcomes decoupled from quality.
