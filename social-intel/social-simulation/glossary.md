# Glossary: social-simulation shelf

Merged alphabetical terms across all eleven chapters. Each entry names its source chapter slug; entries appearing in multiple chapters list every source.

**Algorithmic fidelity** (out-of-one-many, synthetic-survey-data): the degree to which a model's internal associations among ideas, attitudes, and contexts mirror those of specific human subpopulations. Argyle et al. define and defend it with four criteria; Bisbee et al. undercut it on variance and covariance structure.

**ANES** (synthetic-survey-data, out-of-one-many): American National Election Studies, the human benchmark dataset both silicon-sampling papers validate against (2012-2020 waves).

**Bass coefficients p and q** (model-thinker): innovation (broadcast) and imitation (social) forces in an adoption curve; meta-analytic values near p = 0.03 and q = 0.38 for consumer products. The fitted ratio tells you whether media push or social copying carries a trend.

**Believability** (generative-agents-park): the evaluation target for generative agents, measured by interview coherence, not task success.

**Bounded-neighborhood model** (dynamic-models-of-segregation, micromotives-macrobehavior): the shared-area model where everyone evaluates one aggregate composition; tolerance distributions determine whether mixing survives.

**Carrying capacity** (growing-artificial-societies): the population a landscape sustains given the endowment distribution; frames attention-economy crowding and platform migrations.

**Cellular automaton** (a-new-kind-of-science, complexity-mitchell, self-reproducing-automata): a grid of cells updating in parallel by a fixed local rule over a neighborhood; the ancestor formalism of every agent-based model on the shelf.

**Class 1 to 4 behavior** (a-new-kind-of-science): the four regimes any run system lands in: uniform (1), periodic or nested (2), chaotic and statistically random (3), localized interacting structures (4). Class 4 is where computation and interesting transmission live.

**Computational irreducibility** (a-new-kind-of-science): no shortcut to the outcome exists; prediction requires running the system. The deep justification for simulation as method.

**Conditioning** (out-of-one-many): steering model output through prompt context alone, with no parameter updates.

**Contingent behavior** (micromotives-macrobehavior): behavior whose payoff depends on how many others are doing it; the source of equilibria, tipping points, and multiple stable states.

**Critical mass** (micromotives-macrobehavior): the adoption level above which a process becomes self-sustaining.

**Distortion audit** (llms-simulate-humans): the required check on any synthetic panel: replicate a known result in the same task family, then test error realism before trusting a novel readout.

**Distributional fidelity** (llms-simulate-humans): matching the spread and shape of human responses, not just the mean or a single plausible answer.

**Diversity prediction theorem** (model-thinker): crowd squared error equals average squared error minus prediction diversity; the math behind ensemble forecasting.

**Elementary cellular automaton** (a-new-kind-of-science, complexity-mitchell): the 256-rule family with 2 states and radius 1, each rule named by its 8-bit Wolfram code.

**Emergence** (complexity-mitchell): collective order nobody planned, produced by local interaction rules.

**Equifinality** (growing-artificial-societies): multiple distinct rule sets generating the same macro outcome; a sim matching the data identifies a regime, not the one true mechanism.

**Feeling thermometer** (synthetic-survey-data): 0-100 survey scale of warmth toward a group; Bisbee's outcome measure across 11 sociopolitical groups.

**Garden-path sentence** (llms-simulate-humans): a grammatical sentence that induces a predictable misparse, used to test human-like comprehension failure with novel stimuli that dodge memorization.

**Generative agent** (generative-agents-park): an LLM-driven agent wrapped in memory, retrieval, reflection, and planning to simulate believable human behavior.

**Generative explanation** (growing-artificial-societies): demonstrating that a macro pattern emerges from specified micro rules; the book's test of social theory.

**Genetic algorithm** (complexity-mitchell): population, fitness, crossover, mutation; search that beats design on rule sets too large to reason about.

**Growback G_alpha** (growing-artificial-societies): Sugarscape resource regeneration at alpha units per tick.

**Hyper-accuracy distortion** (llms-simulate-humans): simulated humans answering more correctly than real humans, an artifact of scale and instruction tuning; the diagnostic failure of the wisdom-of-crowds Turing Experiment.

**Intrinsic randomness generation** (a-new-kind-of-science): deterministic rules producing randomness with no external noise; the source analysts forget to test for.

**Kinematic model** (self-reproducing-automata): self-reproduction with physical parts in a reservoir, the pre-cellular thought experiment.

**Lemons market** (micromotives-macrobehavior): unverifiable quality lets bad goods drive out good through adverse selection; the model under the human-versus-slop pressure.

**Logical depth** (complexity-mitchell): runtime of the shortest program that outputs an object; how much process is baked in. High entropy with low depth is the slop signature.

**Logistic map** (complexity-mitchell): x(t+1) = R x(t)(1 - x(t)); one slowly drifting parameter flips a stable system aperiodic with no change in the rule.

**Many-model thinking** (model-thinker): applying several simple formal models to one phenomenon and reading the ensemble's agreements and disagreements as the finding.

**Markov equilibrium** (model-thinker): the unique long-run distribution of a fixed-transition system, independent of history; interventions that move the state but not the matrix decay back to baseline.

**Memory stream** (generative-agents-park): the append-only natural-language record of everything an agent experiences; salience is handled at retrieval, not at write time.

**Micromotives versus macrobehavior** (dynamic-models-of-segregation, micromotives-macrobehavior): macro outcomes are not readable from micro intent in either direction; Schelling's core lesson.

**Multi-person prisoner's dilemma** (micromotives-macrobehavior): all prefer universal cooperation, each prefers to defect unilaterally; the fix is a binding rule, not persuasion.

**Multiple equilibria** (micromotives-macrobehavior): distinct stable states available to one system; history and shocks pick among them.

**Musical-chairs mathematics** (micromotives-macrobehavior): closed-system identities that make some aggregate patterns arithmetically necessary, not behavioral news.

**Name-based persona seeding** (llms-simulate-humans): varying simulated demographics by inserting different names into the prompt template; cheap, but subgroup effects need validation against human data.

**Pattern correspondence** (out-of-one-many): synthetic data reproducing the correlational structure among variables, not just their marginals; the hardest of the four fidelity criteria.

**Persona prompt** (synthetic-survey-data): first-person prompt built from a real respondent's covariates to condition the model.

**Preferential attachment** (complexity-mitchell, model-thinker): new links go to popular nodes in proportion to current degree, producing power-law tails; a recommender is a preferential attachment machine.

**Principle of Computational Equivalence** (a-new-kind-of-science): nearly all non-trivial processes are computationally equivalent in sophistication; universality is common, not exotic.

**R0** (model-thinker): contact rate times transmission probability over recovery rate; spread requires R0 above 1, and the immunity threshold is 1 minus 1/R0.

**Recursive planning** (generative-agents-park): decomposing a day plan into progressively finer actions, replanned on reaction.

**REDCAPE** (model-thinker): the seven uses of models: reason, explain, design, communicate, act, predict, explore. Name the use before choosing the model.

**Reflection** (generative-agents-park): periodic synthesis of higher-level inferences from accumulated memories, triggered by an importance-sum threshold; turns logs into identity.

**Retrieval function** (generative-agents-park): the recency, importance, relevance scoring that decides which memories enter an agent's context.

**Rugged landscape** (model-thinker): a multi-peaked problem where local search stalls and diverse heuristics pay.

**Rule 30** (a-new-kind-of-science): class 3 elementary rule producing high-quality pseudo-randomness from one black cell; proof that rich output does not imply a rich generator.

**Rule 110** (a-new-kind-of-science, complexity-mitchell): class 4 elementary rule proven Turing-universal by Matthew Cook; two states, one dimension, anything computable.

**Rule C_alpha** (growing-artificial-societies): Sugarscape combat against out-group agents with reward capped at alpha; tags plus scarcity generate ethnocentric conflict.

**Rule K** (growing-artificial-societies): cultural tag-flipping transmission producing emergent groups; the minimal model of slang and aesthetic spread by adjacency.

**Rule M** (growing-artificial-societies): Sugarscape movement rule: go to the best visible unoccupied site within vision range.

**Scale-free network** (complexity-mitchell): degree distribution P(k) proportional to k to the minus gamma (gamma typically 2 to 3); hubs, robustness to random removal, fragility to targeted removal.

**Sensitive dependence** (complexity-mitchell): tiny differences in starting state grow exponentially, capping the forecast horizon even when rules are known exactly.

**Silicon individual** (out-of-one-many): one synthetic respondent built from one real respondent's covariate profile.

**Silicon sampling** (out-of-one-many, synthetic-survey-data, generative-agents-park, llms-simulate-humans): conditioning a language model on demographic backstories so its completions stand in for human survey respondents; the method Argyle licenses, Aher validates, and Bisbee stress-tests.

**Small-world network** (complexity-mitchell): high clustering with short paths, produced by rewiring a small fraction of lattice edges; where contagion runs fast without community structure dissolving.

**Smallville** (generative-agents-park): the 25-agent sandbox town where emergent diffusion, relationship formation, and coordination were observed.

**Social Science Turing Test** (out-of-one-many): generated responses that human judges cannot distinguish from human ones; first of the four fidelity criteria.

**Spatial proximity model** (dynamic-models-of-segregation): the grid model where each agent evaluates only its adjacent cells.

**Sugarscape** (growing-artificial-societies): the lattice resource landscape plus agent population that serves as the generative laboratory.

**Tape** (self-reproducing-automata): the stored description, used once as instructions and once as copied data; the instruction-data duality behind self-sustaining replication.

**Temporal instability** (synthetic-survey-data): the same prompt returning different results after a model update, breaking reproducibility.

**Tetrachoric correlation** (out-of-one-many): correlation between two binary variables assuming latent continuous traits; the vote-match metric (0.90 to 0.94 across 2012-2020).

**Three-moment audit** (synthetic-survey-data): judge a synthetic panel on means, then variance, then covariance structure; a panel passing only the first is a caricature, not a sample.

**Threshold** (micromotives-macrobehavior): the adoption level at which a given individual joins in; distributions of thresholds, not averages, decide cascades.

**Threshold of complication** (self-reproducing-automata): the complexity level separating degenerative copying from exact or generative self-reproduction.

**Tipping point** (dynamic-models-of-segregation, micromotives-macrobehavior): the composition level past which cascading exit becomes self-sustaining; a property of the tolerance distribution, not of any individual, and not reversible by running the process backward.

**Tolerance schedule** (dynamic-models-of-segregation): the distribution across a population of the maximum other-to-own ratio each member will accept.

**Training-data contamination** (llms-simulate-humans): the model reproducing a famous study's results from memory rather than simulating behavior; countered with novel stimuli.

**Turing Experiment** (llms-simulate-humans): validation design where a model simulates many named participants of a study and the aggregate curve is compared to published human results; replaces the Turing Test's one-off impersonation with distributional fidelity.

**Universal constructor** (self-reproducing-automata): a machine that can build any machine, including itself, from a description; the frame for AI content farms in the slop read.

**Unraveling** (dynamic-models-of-segregation): the sequential cascade where each departure pushes the next most sensitive member past threshold.

**Unstable equilibrium** (dynamic-models-of-segregation, micromotives-macrobehavior): a mixed state that satisfies everyone but collapses under any small perturbation; the default fate of mixed communities absent caps or quotas.

**Variance compression** (synthetic-survey-data): synthetic responses clustering near the modal answer, understating real population spread; hits minorities and atypical group members hardest, and doubles as a slop signature.

**Von Neumann neighborhood** (self-reproducing-automata): a cell plus its 4 orthogonal neighbors, 5 cells total.
