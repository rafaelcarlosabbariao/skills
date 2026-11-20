---
title: A New Kind of Science
author: Stephen Wolfram
year: 2002
kind: book
theme: simulation
shelf: social-simulation
slug: a-new-kind-of-science
---

# A New Kind of Science

## The claim

Extremely simple programs, run forward, generate behavior as complex as anything in nature, and for a large class of systems that behavior is computationally irreducible: no formula jumps to the answer, you can only run the system and watch. This makes step-by-step simulation, not equation-solving, the primary instrument for complex systems. It is the minimal proof behind the whole simulation shelf: local rules produce emergent worlds.

## Core claims

- Complexity does not require complex causes. Rule 30, an elementary cellular automaton definable in one line, produces output that passes statistical randomness tests from a single black cell.
- There is a low threshold of complexity. Once a system crosses it, adding sophistication to the rules does not add sophistication to the behavior. Rule 110 is Turing-universal (proof by Matthew Cook), meaning a near-trivial local rule can compute anything computable.
- Principle of Computational Equivalence: almost all processes that are not obviously simple are of equivalent computational sophistication. Universality is common, not exotic. A crowd, a market, and a cellular automaton can be computational peers.
- Computational irreducibility: for such systems, prediction cannot shortcut the computation. The fastest way to know the future state is to run it. This is the deep justification for simulation as method.
- Intrinsic randomness generation: apparent randomness can be produced internally by deterministic rules. It does not have to come from outside shocks or noisy initial conditions.
- Method over theorem: enumerate the space of simple programs and observe, rather than derive. Wolfram surveys all 256 elementary rules exhaustively before generalizing.

## Frameworks and models

**Elementary cellular automata.** One dimensional row of cells, k = 2 states, neighborhood radius r = 1. Each cell updates from its own state and its two neighbors, giving 2^3 = 8 input configurations and 2^8 = 256 possible rules. The Wolfram code names each rule by the 8-bit output string read as a number (rule 30 = 00011110, rule 110 = 01101110). The entire model space is small enough to search completely, which is the point.

**The four classes of behavior.** Run any rule from random initial conditions and it lands in one of four regimes. Class 1: everything dies to a uniform state. Class 2: periodic or nested structures, locally stable. Class 3: aperiodic, chaotic, statistically random (rule 30). Class 4: localized structures that move, collide, and interact against a stable background (rule 110). Class 4 is where computation, memory, and interesting transmission live.

**Computational irreducibility and the PCE.** If a system is computationally equivalent to a universal machine, general shortcut prediction is impossible in principle. Reducible pockets exist (traditional science lives in them), but they are islands.

**Intrinsic randomness generation.** Three sources of observed randomness: environmental noise, sensitivity to initial conditions, and generation by the rule itself. Only the third needs no external input, and it is the one analysts forget to test for.

## Decision rules

- If a cultural pattern looks random, do not default to external-shock explanations. First ask whether a simple internal rule of the community could generate that texture on its own.
- If a phenomenon resists a clean closed-form story, stop regressing and start simulating: encode candidate local rules, run them, compare output texture to the observed signal.
- If you can classify a scene's regime, forecast accordingly. Class 1 or 2 (stable or cyclic): trend extrapolation is fine. Class 3 (chaotic churn): forecast distributions, never trajectories. Class 4 (discrete memes and factions colliding): simulate interactions, this is where lead time exists.
- If a tiny rule set reproduces the macro pattern, resist adding parameters. Enumerate the small rule space exhaustively before enriching the model.
- If your sim matches the data, hold the claim loosely: many distinct rules produce the same class of texture, so a match identifies a regime, not the one true mechanism.

## Key terms

- Cellular automaton: grid of cells updating in parallel from a fixed local neighbor rule.
- Elementary CA: the 256-rule family with 2 states and radius 1, named by Wolfram code.
- Rule 30: class 3 elementary rule producing high-quality pseudo-randomness from one cell.
- Rule 110: class 4 elementary rule proven Turing-universal by Matthew Cook.
- Class 1 to 4 behavior: uniform, periodic, chaotic, and complex-interacting regimes of any run system.
- Computational irreducibility: no shortcut to the outcome exists, prediction requires running the system.
- Principle of Computational Equivalence: nearly all non-trivial processes are computationally equivalent in sophistication.
- Intrinsic randomness generation: deterministic rules producing randomness with no external noise.
