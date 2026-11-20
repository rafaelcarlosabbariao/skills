---
title: Growing Artificial Societies
author: Epstein & Axtell
year: 1996
kind: book
theme: simulation
shelf: social-simulation
slug: growing-artificial-societies
---

# Growing Artificial Societies (Epstein & Axtell, 1996)

## The claim

Social science should be generative: to explain a macro pattern (inequality, migration, war, trade, cultural groups), you must grow it in a population of simple agents following local rules. If you did not grow it, you did not explain it. The Sugarscape model demonstrates the method: from a handful of movement, metabolism, and interaction rules, recognizably social history emerges without any agent intending it.

## Core claims

- Macro social order needs no macro designer. Skewed wealth distributions, migration waves, tribes, trade networks, and war all emerge from local agent rules on a resource landscape.
- Uniform inputs produce skewed outputs. Agent endowments (vision, metabolism) are drawn from uniform distributions, yet wealth ends up heavily right-skewed with a Pareto-like tail. Inequality is a structural product of interaction, not proof of unequal talent.
- Explanation equals generation. A theory of a social phenomenon is a rule set that, when run, reproduces the phenomenon. Statistical fit without a generating mechanism is description, not explanation.
- Institutions are grown, not assumed. Markets, cultural groups, and even combat coalitions appear when the relevant rules are switched on, letting you watch institutions form rather than positing them.
- Decentralized trade approaches but never reaches textbook equilibrium. Bilateral bargaining moves prices toward the market-clearing level, raises welfare and carrying capacity, and simultaneously increases wealth inequality.
- The model is a laboratory. Toggle one rule, hold everything else fixed, rerun, and you get causal attribution that observational culture data cannot give you.

## Frameworks and models

**Sugarscape.** A 50x50 lattice with sugar in two peaks (site capacity 0 to 4). Roughly 250 agents, each with vision v drawn uniformly from 1 to 6, metabolism m drawn uniformly from 1 to 4, and a sugar store. Movement rule M: look out to distance v in the four lattice directions, move to the nearest unoccupied site with the most sugar, harvest it, burn m per tick, die at zero. Growback rule G_alpha: each site regrows alpha units per tick (G_1 is the standard run; G_infinity is instant). Population settles at a carrying capacity set by the landscape and the endowment distribution, and wealth becomes strongly skewed (Gini around 0.5 in the canonical runs).

**Cultural transmission, rule K.** Each agent carries a binary tag string. On contact, an agent flips one of a neighbor's tags toward its own. Group membership is the tag-string majority (red vs blue). Stable cultural regions form and drift with zero coordination. This is the minimal model of how a slang term, aesthetic, or stance spreads by adjacency.

**Combat, rule C_alpha.** Agents may attack poorer members of the other cultural group; reward is the victim's wealth capped at alpha. Group tags plus resource scarcity generate raiding fronts and ethnocentric conflict from tags that mean nothing in themselves.

**Trade, rule T.** Add a second commodity, spice. Agent welfare is Cobb-Douglas: W(w1, w2) = w1^(m1/mT) * w2^(m2/mT), with mT = m1 + m2. Neighbors compute marginal rates of substitution and trade at the geometric mean of their MRSs whenever both gain. Result: an emergent market with prices converging toward, but fluctuating around, the neoclassical equilibrium. With finite lives and evolving preferences, convergence fails, a standing warning against equilibrium assumptions in culture.

**Demography and inheritance.** Reproduction rule S passes genetics and half of each parent's wealth to offspring; inheritance flattens selection pressure and entrenches inequality. Disease is modeled as bit strings matched against an immune string, spreading by contact.

## Decision rules

- If you see a skewed cultural outcome (attention, follower counts, streaming revenue), do not infer skewed underlying merit. Check whether uniform inputs plus interaction structure would grow the same skew.
- If an explanation of a trend cannot be stated as agent-level rules that generate the macro curve, treat it as narrative, not explanation. Demote it in the read.
- If two different rule sets grow the same observed pattern, withhold confidence in both and look for data that discriminates (the equifinality check).
- If group conflict appears, look for the tag plus scarcity combination before assuming deep ideological cause. Arbitrary markers become battle lines when resources tighten.
- When testing a mechanism, change one rule per run. Never vary two rules between simulation runs you intend to compare.

## Key terms

- **Generative explanation**: demonstrating that a macro pattern emerges from specified micro rules; the book's test of social theory.
- **Sugarscape**: the lattice resource landscape plus agent population that serves as the laboratory.
- **Rule M**: movement rule, go to the best visible unoccupied site within vision range.
- **Growback G_alpha**: resource regeneration at alpha units per tick.
- **Rule K**: cultural tag-flipping transmission producing emergent groups.
- **Rule C_alpha**: combat against out-group agents with reward capped at alpha.
- **Carrying capacity**: the population a landscape sustains given the endowment distribution.
- **Equifinality**: multiple distinct rule sets generating the same macro outcome.
