---
title: Complex Contagions and the Weakness of Long Ties
author: Centola & Macy
year: 2007
kind: paper
theme: diffusion
shelf: diffusion-contagion
slug: complex-contagions
---

# Complex Contagions and the Weakness of Long Ties

## The claim

Information spreads like a disease: one exposure can be enough, so the long random ties of a small-world network accelerate it. Behavior that carries cost or risk needs multiple reinforcing exposures, and the same long ties that speed information are too narrow to deliver reinforcement, so they are weak for behavior. What carries behavior across communities is a wide bridge: multiple overlapping ties between the same two clusters.

## Core claims

- Contagions divide into simple (one exposure can suffice: news, a job lead, a virus) and complex (adoption requires confirmation from two or more independent sources).
- Four mechanisms make a contagion complex: strategic complementarity (the thing is only worth doing if others do it), credibility (claims need corroboration), legitimacy (acting alone is deviant, acting with others is normal), and emotional contagion (intensity builds in dense company).
- Granovetter's weak-tie result and the Watts-Strogatz small-world result hold only for simple contagions. For complex contagions the finding inverts: randomly rewired long ties slow or kill diffusion. Hence "the weakness of long ties."
- Bridge width, not path length, governs whether behavior crosses between communities. A bridge of one tie carries information; a complex contagion needs a bridge at least as wide as its threshold.
- Clustered, redundant, locally dense networks, the ones network theory had written off as inefficient, are the efficient topology for spreading costly behavior.
- The paper separates tie strength (Granovetter's relational intimacy) from tie range (topological distance spanned). The topological variable is what does the causal work here.

## Frameworks and models

**Simple vs. complex contagion.** Formalized as an activation threshold. Each node activates when the number of active neighbors reaches a threshold T (or a fraction a of its z neighbors). T = 1 defines a simple contagion. T >= 2, even just 2, defines a complex one, and 2 is enough to flip every headline small-world result.

**The perturbed lattice experiment.** Agents sit on a regular ring lattice with degree z (Moore-style neighborhoods). Following Watts and Strogatz, ties are randomly rewired with probability p, sweeping from p = 0 (pure lattice, high clustering, long paths) to p = 1 (random graph, short paths, no clustering). For T = 1, rewiring monotonically speeds diffusion. For T >= 2, moderate p already slows spread and beyond a critical p* the cascade fails outright: rewiring removes the redundant local ties that delivered the second exposure, and the new long ties arrive alone at their far end, below threshold. Shortcuts for information are dead ends for behavior.

**Wide bridges.** Bridge width is the number of nonredundant ties linking two neighborhoods. A complex contagion with threshold T crosses only bridges of width >= T. This is the operational replacement for "influencer reach": count overlapping ties between communities, not follower counts across them.

## Decision rules

- If you are asked why something "went viral" here but a costlier cousin did not, first classify each as simple or complex. Awareness and behavior obey different physics.
- If a practice must cross from one scene to another (a subculture to the mainstream, one platform to another), look for wide bridges: clusters of people embedded in both. If only thin celebrity or press ties connect them, expect awareness without adoption.
- If a costly norm is spreading fast through a sparse, broadcast-shaped network, be suspicious: either it is actually a simple contagion (cheap to adopt, low identity cost) or the spread is astroturfed.
- If you want to forecast whether a behavior sustains, estimate its threshold from its cost: identity risk, money, effort, social sanction. Higher cost means it lives or dies on local redundancy, so read the dense clusters, not the feed.
- If seeding adoption, concentrate seeds in one neighborhood to cross local thresholds, rather than scattering them for maximum reach.

## Key terms

- Complex contagion: a behavior whose adoption requires reinforcement from multiple sources, not one exposure.
- Simple contagion: spread where a single contact can transmit, as with information or disease.
- Threshold (T): the number of activated neighbors a node needs before it activates.
- Wide bridge: multiple overlapping ties between two clusters, wide enough to deliver T exposures across the gap.
- Tie range: the topological distance a tie spans, distinct from its relational strength.
- Rewiring probability (p): the Watts-Strogatz parameter converting a clustered lattice toward a random graph.
- Strategic complementarity: payoff to adopting rises with the number of prior adopters.
