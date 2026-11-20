---
title: "Complexity: A Guided Tour"
author: Melanie Mitchell
year: 2009
kind: book
theme: simulation
shelf: social-simulation
slug: complexity-mitchell
---

# Complexity: A Guided Tour

## The claim

Complex systems are large networks of simple components with no central control, whose local rules produce collective behavior, information processing, and adaptation nobody intended. Mitchell treats dynamics, information theory, computation, and evolution as four views of one object, and insists the useful question is never "is this complex" but "which measure, on which variable, at which scale." She hands you instruments, not a unified theory.

## Core claims

- Deterministic does not mean predictable. Simple rules generate chaos, so long-horizon point forecasts are a category error even when the rules are known exactly.
- Simple local rules suffice for unbounded complexity. Rule 110 is Turing-universal: two states, one dimension, anything computable.
- No single measure of complexity exists. Roughly forty candidates disagree with each other, so the choice of measure is a modeling decision you must defend.
- Decentralized systems process information statistically: cheap noisy samples, parallelism, randomness as a feature, exploration traded against exploitation.
- Topology dominates content. Whether a thing spreads is set by degree distribution and path length.
- Evolution is a search algorithm, and search beats design on rule sets too large to reason about.

## Frameworks and models

**Logistic map.** x(t+1) = R x(t)(1 - x(t)). Fixed point below R = 3, period doubling above, doublings accumulating near R = 3.5699, chaos beyond, the cascade converging at the Feigenbaum constant 4.6692. One parameter drifting slowly flips a stable system aperiodic with no change in the rule.

**Cellular automata.** Cells update from their own and their neighbors' states via a lookup table. Elementary CA: two states, radius one, 256 rules. Wolfram's classes run uniform, periodic, chaotic, complex. Rule 110 is class four and universal.

**Genetic algorithms.** Population of rule strings, fitness function, elite selection, single-point crossover, per-locus mutation of order 0.005. Robby the Robot encodes strategy as a 243-locus string, one locus per sensory situation. The evolved strategy beat Mitchell's hand-designed one by finding a move she would not have written: leaving a can uncollected as a positional marker.

**Small-world networks.** Watts and Strogatz: ring lattice, k neighbors, rewire each edge with probability p. At p = 0 clustering is high and paths long; at p = 1 both collapse. Around p = 0.01 to 0.1 path length collapses while clustering holds, where contagion runs fast without community structure dissolving.

**Scale-free networks.** Barabasi and Albert: grow the graph, attach new nodes with probability proportional to degree. P(k) goes as k to the minus gamma, gamma typically 2 to 3. Hubs, robustness to random removal, fragility to targeted removal, epidemic threshold near zero.

**Complexity measures.** Shannon entropy, algorithmic information content, logical depth. Noise maximizes the first two and minimizes the third.

## Decision rules

- If a novelty metric is entropy-based, do not point it at AI slop. Slop is high-entropy and low-depth, so the metric ranks it most novel. Score process depth and provenance instead.
- If a domain's attention distribution steepens toward lower gamma, the algorithm is winning it; if the middle fattens, taste is.
- If a signal moves in all eight domains at once, suspect the instrument. Systems with no central control rarely move in lockstep, so corpus-wide simultaneity is a plumbing hypothesis.
- If you forecast past the horizon where input error doubles, report a distribution and a condition word, never a point number.
- If a rule set has more free parameters than you can reason about, fit it by search, then read the winner for the move you would not have written.
- If you need to slow a contagion on a scale-free graph, act on hubs; random intervention barely moves it.
- If a stated rule and the emergent output disagree, the gap is the finding.

## Key terms

- **Emergence**: collective order nobody planned, produced by local interaction rules.
- **Cellular automaton**: lattice of cells updated by a neighbor lookup table.
- **Rule 110**: elementary CA rule proven Turing-universal.
- **Sensitive dependence**: tiny differences in starting state grow exponentially, capping the forecast horizon.
- **Genetic algorithm**: population, fitness, crossover, mutation, searching rule spaces too large to design in.
- **Small-world network**: high clustering with short paths, from rewiring a small fraction of lattice edges.
- **Preferential attachment**: new links go to popular nodes, producing a power-law degree distribution.
- **Logical depth**: runtime of the shortest program that outputs an object; how much process is baked in.
