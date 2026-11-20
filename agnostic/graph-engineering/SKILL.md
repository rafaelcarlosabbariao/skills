---
name: graph-engineering
description: "Practice shelf on agent architecture and durable memory, compiled from two works: Graph Engineering: The Karpathy Loop, Improved 1000x by Itself (independent compilation, 2026), which maps autoresearch and AgentHub onto Anthropic's workflow patterns, Dynamic Workflows, and the Knowledge Graph Cookbook; and MemPalace (2026), a local-first verbatim memory system that takes the opposite bet on what to store. Load this shelf for two families of question. Architecture: 'should this be a loop, a chain, a swarm, or a graph', 'how many sub-agents and what is the budget', 'our multi-agent run produced confident nonsense', 'the swarm is busy but is it producing value', 'how do we keep experiment lineage instead of one main branch', 'when do we stop and hand back partial work'. Memory and retrieval: 'the agent forgets everything between sessions', 'do we actually need a knowledge graph here', 'should we store summaries or the original text', 'why did entity resolution merge two different people', 'how do we evaluate an extraction or retrieval pipeline', 'how do we mark a fact that used to be true', 'how do we stop memory writes eating the context window', 'is this benchmark number honest'."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# Graph engineering: from one measured loop to a durable graph

Two works, one job: deciding how much system architecture to place around a model call, and what to keep when the context window closes.

**The paper** (`graph-engineering-karpathy-loop`) maps Karpathy's progression, autoresearch then AgentHub, onto Anthropic's workflow infrastructure of five composable patterns, Dynamic Workflows, and the Knowledge Graph Construction Cookbook, and turns the overlap into a staged build path with exit criteria at every stage. It is a practice document, not a theory: its claims are about where to put memory and evaluation, and its warnings are about what automation does to a mistake.

**MemPalace** (`mempalace`) is a shipped local-first memory system that agrees with the paper's premise and inverts its method. Both put memory outside the context window. The paper extracts, resolves surface forms into canonical entities, and reasons over a typed graph. MemPalace stores the original text verbatim, compresses only the index, and retrieves by scoped semantic search. It is the shelf's working counterexample, and it is also the clearest case of the paper's own evaluation discipline being practiced by someone with an incentive not to.

Read the paper for **how much architecture**. Read MemPalace for **what to keep, and in what form**.

## The unified mental model

### 1. Each architecture externalizes exactly one bottleneck

This is the paper's spine, and it is what makes the rest of the shelf usable. Every level of agent architecture takes one thing that was previously trapped in a human head or a chat transcript and puts it somewhere durable and queryable:

- A **loop** externalizes iteration and evaluation.
- A **chain** externalizes task order.
- A **swarm** externalizes parallel search and role specialization.
- A **DAG** externalizes experiment lineage.
- A **knowledge graph** externalizes shared facts, provenance, and cross-session memory.

The operational consequence: never choose an architecture by how sophisticated it sounds. Name the bottleneck first, then take the level that externalizes it, and no more. Each pattern addresses a specific limitation of the previous stage (the loop addresses single-pass errors, tools address knowledge gaps, planning addresses complexity, multi-agent addresses perspective limits, the DAG addresses lineage tracking, the graph addresses persistent shared memory). The progression is not mandatory, but it is directional: skipping stages means adding a solution to a bottleneck you have not yet demonstrated you have.

### 2. The bottleneck is rarely the next model call

The paper's own summary of its most important insight: the constraint is usually not model capability but **the placement of memory and evaluation**. A loop can remember the current code and a local experiment log. A swarm creates many independent contexts and remembers nothing across them. A commit DAG remembers which work descends from which experiment. A knowledge graph remembers which claims connect to which entities and sources. The phrase that carries it: **the agent forgets, the graph does not.**

This reframes almost every "the agent is not good enough" complaint into a question about where state lives. Before reaching for a stronger model or more workers, ask what the system is being forced to rebuild from scratch in every context window.

### 3. Autonomy is licensed by four conditions, not by ambition

Autoresearch works (roughly 700 experiments in two days, about 20 retained optimizations) because four conditions hold, and the paper is explicit that they are the license:

1. **The output is verifiable.** Training produces a measurable validation result.
2. **The action is reversible.** Git reset returns to the last retained state.
3. **The horizon is short.** Five-minute runs create frequent feedback.
4. **The environment is bounded.** The repository narrows the action space.

Where all four hold, an agent can run unattended and record results without asking a human. Where any one fails, autonomy is being granted on credit. The first selection question in the decision framework is the hard gate: if success cannot be verified, do not begin with autonomy at all. Define a test, a rubric, a source requirement, or a human decision first.

### 4. The human's artifact moves up a level, and the responsibility does not move at all

Karpathy's "programming the program": in Software 1.0 the developer writes instructions, in 2.0 shapes behavior through data and training, in 3.0 prompts become the programmable interface. Autoresearch adds another layer, where natural-language instructions (`program.md`) configure an autonomous research organization. The human stops editing the work product and starts editing the brief.

Anthropic's Dynamic Workflows make the same move at the orchestration layer: instead of a developer writing a static fan-out script, the model writes the orchestration program for the current task. The paper is firm that this **changes the abstraction boundary but does not remove engineering responsibility.** The human still defines the objective, the files in scope, the output contract, the permissions, the verification policy, the concurrency and token budget, the rollback rule, and the evidence required for synthesis. Anything on that list you have not defined, you have delegated by accident.

### 5. Work lineage and domain knowledge are two graphs, and collapsing them loses both

The commit DAG answers: what changed, which experiment is the parent, which agent produced the change, which lineages remain active. The knowledge graph answers: which entities exist, how they relate, which sources support the relation, which claims conflict. They are complementary and should not be collapsed into one structure. A production platform connects them (an agent run produced a claim, modified a commit, was evaluated by an evaluation; the claim is about an entity, supported by a source, and supersedes an earlier claim) without merging them.

The five-plane reference architecture exists for the same reason: control, execution, artifact, graph, and evaluation planes are separated specifically so that **one chat transcript does not become the database, the workflow engine, and the audit log.**

### 6. A graph is not a place to dump context

The failure mode the paper flags hardest for anyone who has just built a graph: using it as a bigger context window. Retrieval must be a bounded construction, not a replay. A context builder resolves the entities mentioned in the task, expands one or two hops over allowed edge types, includes current artifact versions, prioritizes recent verified claims, includes conflicts and uncertainty, serializes within a token budget, and attaches stable edge identifiers so the answer can cite them. Multi-hop querying that serializes the whole graph has reproduced the problem it was built to solve.

Both works reach this rule independently, which is the strongest evidence on the shelf for any single claim. MemPalace arrives from the token bill rather than from architecture: it moved diary writes, filing, and timestamp injection out of the chat window into background hooks after watching an agent rewrite the same block every turn, and it makes specialist agent context discoverable at runtime so nothing resident sits in the system prompt.

### 7. Compress the index, not the payload

The shelf's second axis, and the one the two works split on. Every memory system loses something; the design question is **where** the loss is allowed to happen.

The paper puts it in the payload. Extraction produces typed entities, resolution collapses surface forms into canonical ones, and the graph you reason over is a lossy derivative of the corpus. It manages the cost procedurally: keep merges additive, inspectable, and reversible, because a false merge contaminates every traversal that touches it.

MemPalace puts it in the index. Drawers hold the original text untouched; the closet layer holds compressed shorthand whose only job is to say which drawer to open. A resolution error there degrades findability rather than corrupting content.

Neither is free, and the choice is not a matter of taste. Ask which failure is worse in your setting: an answer that cannot be found, or an answer that is confidently wrong. Ask also whether anything downstream needs the exact words, because a resolved graph cannot reconstruct them once the surface forms are gone.

## Where the works disagree

The shelf is not unanimous, and the disagreements are load-bearing. They run in two directions: between the two works, and inside the paper, between its build path and its own limitations section.

### Between the works

**Canonical resolution versus verbatim retention.** The central split, treated at length in the MemPalace chapter. The paper accepts a lossy derivative and manages the risk with reversible merges; MemPalace refuses to let the payload depend on resolution at all. The paper's graph can answer "which claims conflict" in a way MemPalace cannot. MemPalace can always return what was actually said, which a resolved graph cannot reconstruct. Choose by naming your worse failure.

**Cited edges versus original text as the unit of evidence.** The paper's grounding layer decomposes a claim into the edges that would support it and names the missing ones, which requires a typed graph and yields edge-level citation. MemPalace's citation is the passage itself: it cannot tell you which relation is missing, but it cannot be an artifact of extraction either. The paper's own §IX-F cuts toward MemPalace here, since a graph preserves claims for inspection rather than converting them into truth.

**Structured filing versus unstructured retrieval.** MemPalace's stated goal is storing in a highly structured way and retrieving in a highly unstructured one, so that half-remembered questions still land. The paper's query layer is bounded traversal with typed edges and filters. The working resolution is that they serve different questions: traversal answers "what connects these two things," semantic search answers "what was that thing we said once."

**Whether the graph earns its cost.** The paper reserves a knowledge graph for connected queries, evolving relations, provenance, and shared world state, and warns against adding one merely because the system has agents. MemPalace ships a graph but subordinates it to semantic search, which is arguably the paper's own test applied honestly rather than a disagreement with it.

### Inside the paper

The tension between the paper's build path and its own limitations section. These are the load-bearing contradictions, and the limitations generally win.

**The staged path versus "fragmentation can reduce quality."** Sections VI is a ladder that ends in a swarm, and the implicit reward for climbing is throughput. Section IX-E says some tasks require one coherent context, and names architecture design, narrative writing, tightly coupled refactors, and subtle product decisions as work that degrades when divided into isolated units. The ladder is not universal. Read the swarm stage as available, not as the destination, and check whether the task is genuinely decomposable before fanning out.

**Measured autonomy versus "metrics can be gamed."** The ratchet loop is the paper's most transferable object, and section IX-B undercuts it directly: a ratchet improves only the metric it can see, and may reduce validation loss while increasing inference cost, decreasing robustness, or overfitting the evaluation set. The resolution is constraints alongside the objective (memory, throughput, stability, generalization for training; resolution precision and query latency for graphs), not a better single number. The same applies at the graph layer: compression ratio rewards over-merging if optimized alone.

**"Improved 1000x by itself" versus "autoresearch does not equal frontier research."** The subtitle and abstract lean on scale (700 experiments, 1,000 sub-agents, 86,000 stars), and section IX-A retracts the implication: a loop that works on one GPU does not prove an agent can safely self-modify a production training platform, and repository popularity is not a scientific performance measure. The paper itself offers the better reading of the star count, that it is evidence the pattern is easy to reproduce because the code is small, the metric visible, and the loop legible. **The correct transfer is the architecture, not the numbers:** bounded changes, measurable evaluation, reversibility, durable history.

**Graph as grounding versus "knowledge graphs reflect their corpus."** Section V sells the graph as the grounding layer where an evaluator checks claims against edges and returns structured feedback naming the missing evidence. Section IX-F is the caveat that matters most for anything downstream of a corpus: a biased corpus produces a biased graph, missing documents produce missing edges, and the graph **preserves claims, sources, and relationships so they can be inspected, it does not convert claims into truth.** A grounded claim is a sourced claim, not a verified one.

**Automation as leverage versus "the graph amplifies builder judgment."** The whole document is an argument for more architecture, and section IX-H names the cost: a loop amplifies the objective and evaluator the builder chose, a graph amplifies the ontology and source policy. If the system is told to optimize the wrong thing or to represent the world incorrectly, automation increases the scale of the error rather than surfacing it. Every stage on the ladder therefore raises the price of a specification mistake.

## Which stage is the right tool

- **Any output that can be checked:** the reflective loop. Stored first draft, evaluator with explicit criteria, revision step, stopping rule, every artifact stored. Day 1, low complexity, exit criterion is measured quality improvement.
- **A known, recurring error class:** one tool, with a typed schema, permissions, and result confirmation. Day 2. Exit criterion is that the tool reduces that error class.
- **Task paths that vary between runs:** planning. Require a JSON plan before execution, validate dependencies, preserve successful work across replanning, cap retries and total cost. Week 1. Do not add planning to a stable sequence: use a chain.
- **Perspective limits, where one reviewer misses what another catches:** multi-agent, starting with generator and critic. Every handoff is an artifact contract, and a reviewer returns criterion-level defects, never "looks good." Worktree isolation when multiple coding agents touch one repository. Week 2. Exit criterion is that the role split beats a single agent.
- **Alternatives that must stay alive:** a commit DAG, not one main branch. Use when most results will never merge and a failed experiment still carries evidence. The primary operation becomes traversing the search graph rather than merging into main.
- **Facts that must survive the run:** a knowledge graph. Entities, claims, sources, relations, artifacts, agent runs, evaluations, versions, aliases, open questions, with provenance on every edge. Month 1. Exit criterion is that cross-session queries work.
- **Genuinely parallel work with a defined reducer:** the swarm or dynamic workflow. Define the reducer before fan-out, then set concurrency limit, worker cap, token budget, per-worker timeout, retry policy, evidence contract, deduplication policy, and final evaluation gate. Month 2. Exit criterion is wall-clock gain with no quality loss.
- **A simple, low-risk question:** zero-shot. The lowest-latency answer is still an answer, and the paper's table lists it first for a reason.

## Which memory shape is the right tool

- **Recall of what was actually said, across sessions:** verbatim storage with scoped semantic search. Store the original, compress only the index, scope by project or person before searching. MemPalace's shape.
- **Questions about how things connect:** a typed graph with bounded traversal. Resolve entities, expand one or two hops, cite the edges. The paper's shape.
- **Facts that were true for a while:** validity windows with an explicit invalidate operation and a timeline query. Do not delete a fact that has expired, and do not silently edit one either.
- **Evidence that has to survive quotation:** the original passage, never a paraphrase. If a cloaking decision, an authenticity read, or a client deliverable depends on the exact words, a resolved graph has already thrown away what you need.
- **Memory writes that are costing tokens every turn:** move them off the chat surface into background hooks, and make specialist context discoverable at runtime rather than resident in the prompt.
- **Both, usually.** The two shapes are complementary rather than exclusive: keep the corpus verbatim, build the graph over it as a derived index, and treat the graph as rebuildable. What must never be derived is the source text.

## Chapter index

| slug | work (source, year) | one-line | when to load |
|---|---|---|---|
| graph-engineering-karpathy-loop | Graph Engineering: The Karpathy Loop, Improved 1000x by Itself (independent compilation, 2026) | Maps autoresearch and AgentHub onto Anthropic's workflow patterns, Dynamic Workflows, and the KG Cookbook; each architecture externalizes one bottleneck, and the build path runs loop, tools, planning, multi-agent, graph, swarm | read chapters/graph-engineering-karpathy-loop.md when designing an autonomous loop or swarm, deciding whether a knowledge graph earns its cost, setting a complexity budget, evaluating an extraction pipeline, or diagnosing a multi-agent run that is busy without producing value |
| mempalace | MemPalace (2026, MIT, github.com/mempalace/mempalace) | Local-first verbatim memory: wings, rooms, drawers, and a compressed closet index; scoped semantic search, pluggable backends, a temporal KG with validity windows, and a published refusal to headline an overfit benchmark number | read chapters/mempalace.md when deciding what to store rather than how much architecture to build, when an agent loses continuity between sessions, when choosing between summaries and original text, when a fact needs a time bound, or when judging whether a reported benchmark is honest |

## Companion files

- **glossary.md**: every key term from both chapters, merged alphabetically, each tagged with its source chapter. Open it when a term from one work appears in the other's context, or to keep vocabulary consistent across specs and build notes.
- **patterns.md**: the reusable recipes, each with when-to-use, steps, and source: the ratchet loop, the program.md contract, the staged build path, the complexity budget, the graph-grounded evaluator, entity resolution as a reasoning task, bounded context construction, the graph autoresearch loop, the swarm fan-out contract, the verbatim-payload split, scoped retrieval, validity windows, and the honest-benchmark discipline. Open it when you know the job and want the procedure, not the argument.
- **cheatsheet.md**: decision tables mapping situation to architecture level or memory shape to first check, plus the six selection questions and the metric misreadings. Open it first, mid-design, when you need to know which level applies before loading a full chapter.
