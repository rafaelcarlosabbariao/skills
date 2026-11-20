---
title: "Graph Engineering: The Karpathy Loop, Improved 1000x by Itself"
author: uncredited (independent compilation, not affiliated with or endorsed by Andrej Karpathy or Anthropic)
year: 2026
kind: paper
theme: practice
shelf: graph-engineering
slug: graph-engineering-karpathy-loop
source: "PDF, author uncredited; not linked publicly"
based_on: "Anthropic Knowledge Graph Construction Cookbook; Andrej Karpathy courses and presentations in the public domain; karpathy/autoresearch; AgentHub"
---

# Graph Engineering: The Karpathy Loop, Improved 1000x by Itself (2026)

## The claim

The progression from vibe coding to agentic engineering to graph engineering is a progression in where state lives. Karpathy built autoresearch, a single-agent loop that ran roughly 700 ML experiments in two days and retained about 20 training optimizations autonomously, then argued the next step was collaboration and sketched AgentHub, where agent swarms coordinate through a shared commit DAG instead of a main branch. Anthropic shipped a parallel progression in production: five composable workflow patterns, Dynamic Workflows that spawn up to 1,000 fresh-context sub-agents from a single prompt, and a Knowledge Graph Construction Cookbook that replaces trained NLP pipelines with structured-output prompts. The synthesis is that **each architecture externalizes a different bottleneck**, and the practical work is choosing the lowest level that externalizes the bottleneck you actually have.

Its audience is engineers who already know how to call an LLM and now need to decide how much system architecture to place around it.

## Core claims

- Each level externalizes one thing: a loop externalizes iteration and evaluation, a chain task order, a swarm parallel search and role specialization, a DAG experiment lineage, a knowledge graph shared facts, provenance, and cross-session memory.
- The bottleneck is often not the next model call. It is the placement of memory and evaluation.
- Autonomy is licensed by four conditions: verifiable output, reversible action, short horizon, bounded environment. Autoresearch satisfies all four, which is why it works unattended.
- `program.md` is "programming the program." The human's artifact becomes the brief, not the code. If the human wants better results they revise the instructions, not `train.py`.
- The architectural lesson is more reliable than any single optimization discovered. A human researcher carries hypotheses, failed attempts, and parameter interactions in working memory; the loop converts them into machine-readable history where every experiment has a parent state, a code diff, a metric, and a keep-or-discard decision.
- Agent research inverts human Git assumptions. Thousands of agents explore simultaneously, most results may never merge, and a failed experiment still contains useful evidence. The primary operation is no longer "merge this into main," it is "traverse the search graph."
- The DAG is the graph, literally: commits are nodes, parent links are directed edges, and a commit node can carry hypothesis, diff, metric, runtime, memory, environment, keep-or-discard status, and links to discussion.
- The commit DAG (work lineage) and the knowledge graph (domain knowledge) are complementary and must not be collapsed.
- Claude writing the workflow changes the abstraction boundary but does not remove engineering responsibility. Objective, scope, output contract, permissions, verification policy, budget, rollback rule, and evidence requirement remain human.
- The graph does not convert claims into truth. It preserves claims, sources, and relationships so they can be inspected.
- The reliability test: every important output can be traced to an objective, a plan, an artifact, a source, a graph path, an evaluator decision, and a bounded execution record. When that is false, adding more agents usually increases opacity.

## Frameworks and models

**The autoresearch harness.** The agent is placed inside an executable research harness exposing a mutable training program, a fixed evaluation metric, a time budget, Git history, and instructions. Three files are central: `prepare.py` (fixed data preparation and evaluation utilities, never modified by the agent), `train.py` (the model, optimizer, hyperparameters, and training loop, which is the experimental surface the agent edits), and `program.md` (the research process, constraints, metric, logging rules, and autonomy policy). The loop: read current `train.py` and recent history, propose one motivated change, commit the candidate, run training for about five minutes, measure the metric and peak memory, on crash inspect and fix if mechanical else revert, keep the commit if the metric improves else reset to the previous retained commit, record the result and continue without asking a human.

**The ratchet loop.** The reusable template underneath autoresearch: inspect, propose, apply, evaluate, then keep or revert, appending a trial record either way, including for crashes. The ratchet is the general form; the ML training case is one instance. It applies to any search where a cheap honest number can be produced on demand.

**What `program.md` must establish.** Mutable and protected files, the metric and its direction, the experiment budget, the run command, output parsing, crash handling, commit and revert rules, logging, the human escalation policy, and exhaustion criteria.

**AgentHub's CLI as a graph interface.** `ah push`, `ah fetch <hash>`, `ah log [-agent X]`, `ah children <hash>` (what was tried above this), `ah leaves` (the frontier, commits with no children), `ah lineage <hash>` (ancestry path to root), `ah diff <hash-a> <hash-b>`. These encode a different unit of collaboration: the questions are about descent and frontier rather than merge readiness. Minimal architecture: one Go server binary, one SQLite database, one bare Git repo on disk, one API key per agent, rate limiting and bundle-size limits, a thin CLI. The design deliberately separates **mechanism from culture**: the platform does not know whether agents are tuning models, fixing tests, hunting vulnerabilities, or designing APIs, because prompts and project instructions define that.

**The five workflow patterns.** Prompt chaining (one call's output is the next call's artifact, fixed sequence). Routing (a classifier sends input to a specialized prompt, model, or tool set). Parallelization (independent calls run concurrently, by sectioning or voting). Orchestrator-workers (a central model dynamically decomposes, assigns, and synthesizes). Evaluator-optimizer (one role generates, another evaluates against criteria in a loop). Anthropic's guidance is to begin with the simplest composable pattern.

**Dynamic Workflows.** The model writes a JavaScript orchestration program for the current task rather than the developer writing a static fan-out script. Key specifications: up to 16 concurrent sub-agents, a hard cap of 1,000 per workflow, fresh context for each sub-agent, intermediate state held in script variables. The worked example fans out auditors over globbed files at concurrency 16, filters findings by confidence threshold, spawns reviewers instructed to *refute* each surviving finding, and ends at a single synthesizer producing one cited report.

**The four-stage knowledge graph pipeline.** Extraction (a cheap model makes a schema-constrained call producing typed entities and subject-predicate-object relations). Resolution (a stronger model clusters candidates by type and context, mapping surface forms to canonical entities). Assembly (a MultiDiGraph where nodes carry type, source, and count, and edges carry predicate and provenance). Querying (serialize a bounded subgraph as triples so the model reasons with edge-level citations). The Pydantic schema is the only "training data": a trained NER model and relation classifier collapse into one structured-output prompt per document.

**Graph roles across the workflow patterns.** Retrieval source for the augmented LLM (traversal for multi-hop questions), validation source for prompt chaining (check entities against the current graph), classifier input for routing (entity type and degree route queries), shared surface for parallelization (workers publish non-overlapping findings), shared memory for orchestrator-workers (workers read and write the graph while the orchestrator's context stays clean), and grounding layer for evaluator-optimizer (the evaluator checks claims against edges).

**The graph-grounded evaluator.** For a claim like "Vendor X supplied the component involved in Incident Y," the evaluator checks for the specific edges that would support it and, when one is missing, returns structured feedback naming the decision, the claim, the reason ("no supported path"), and the required evidence as a list of the specific source-backed relations needed. This is more actionable than free-form critique.

**Bounded context construction.** Each worker gets a task-specific subgraph, not the graph. Resolve entities mentioned in the task, expand one or two hops over allowed edge types, include current artifact versions, prioritize recent verified claims, include conflicts and uncertainty, serialize within a token budget, attach stable edge identifiers for citation.

**The five-plane reference architecture.** Control (receives objectives, creates plans, allocates budgets, starts workflows, decides when to stop). Execution (runs tools, tests, training jobs, code modifications, and sub-agents in isolated environments). Artifact (stores plans, drafts, code changes, reports, metrics, and evaluations as immutable versions). Graph (entities, claims, relations, provenance, experiment lineage, task dependencies). Evaluation (deterministic checks, model evaluators, statistical scorers, human review). The separation prevents one chat transcript from becoming the database, the workflow engine, and the audit log.

**The staged build path, with exit criteria.** Reflective loop (day 1, low complexity, exit on measured quality improvement). Tool use (day 2, low, exit when the tool reduces a known error class). Planning (week 1, medium, exit when variable tasks complete). Multi-agent (week 2, medium, exit when the role split beats a single agent). Persistent graph (month 1, high, exit when cross-session queries work). Swarm workflow (month 2, high, exit on wall-clock gain with no quality loss).

**The complexity budget.** Every run declares maximum model calls, sub-agents, concurrent workers, tool calls, wall-clock time, tokens, financial cost, retries, and graph writes, plus the minimum evidence required for finalization. When the budget is exhausted, return the best current artifact, the completed work, the unresolved issues, and a reason for stopping. Do not hide partial failure behind a fluent final answer.

**Graph autoresearch.** The evaluation harness has the same shape as the original loop, applied one level up: read the current extraction prompt and score history, propose one prompt or schema change, run extraction on a gold set, compute precision, recall, F1, cost, and latency, keep if improved and revert if worse. The artifact being optimized is not `train.py`, it is the extraction prompt, the ontology, the resolution policy, or the query serializer.

## Decision rules

- If success cannot be verified, do not begin with autonomy. Define a test, rubric, source requirement, or human decision first.
- If the steps are stable, use a chain. If they are not, consider planning or an orchestrator.
- If subtasks are independent, parallelize. If they are not, model the dependencies explicitly and limit concurrent writes.
- If alternative lineages must remain available, use a DAG rather than forcing every result into one branch.
- If facts must survive the run, persist artifacts and graph state. Do not rely on transcript summaries.
- If the cost and latency are not affordable, set budgets before adding workers, not after.
- If the task is not decomposable (architecture design, narrative writing, tightly coupled refactors, subtle product decisions), do not fan out. Fragmentation degrades work that needs one coherent context.
- If you are about to fan out, define the reducer first. No reducer means no fan-out.
- If a verification wave is added after parallel work, give the reviewers a different prompt, evidence set, or role. Identical reviewers reproduce correlated errors rather than catching them.
- If the compression ratio is the only resolution metric, you are rewarding over-merging. Track false merge rate and missed merge rate alongside it.
- If isolated nodes suddenly increase, suspect resolution regression. If they suddenly decrease, suspect over-merging.
- If a graph would only be introduced because the system has agents, do not introduce it. A graph earns its cost when connected queries, evolving relations, provenance, or shared world state are central, and is unnecessary when tasks are independent, answers depend on one document, relations are fixed and simple, a relational table answers every query, provenance is not needed, or extraction errors would outweigh traversal value.
- If a merge is made during entity resolution, keep it reversible: retain aliases, source documents, resolution rationale, confidence, and the run that created it.
- If the answer is fluent but the cited edges are irrelevant, the query layer is failing even though accuracy looks acceptable. Evaluate multi-hop answers against both the answer and the path.

## Applications

- **A graph you already keep** (co-occurrence edges, citation links, a people-by-groups table) is subject to the shelf's warnings. Compute derived relations at query time where you can, and key entities on stable identifiers (an account id, a DOI) before letting a model arbitrate merges.
- **Long engagements** split into domain knowledge (the rules, tensions and drift you are mapping) and work lineage (which run and which analyst produced each claim). Keep them in separate structures so either question can be asked cleanly.
- **Ensemble forecasts** are the parallelization pattern with a reducer problem: decide how scenarios combine before generating them.
- **Ingestion sources are an ontology decision.** Missing documents produce missing edges, and the graph will not announce the gap.
- **A standing build agent** should be a measured loop with a verifiable exit before it is a swarm, with an escalation policy that pauses on consequential design choices.
- **Any proposal to start at a multi-agent or graph stage** should first name which bottleneck a simpler level failed to externalize. Skipping stages means adding a solution to a bottleneck nobody has demonstrated.

## Key terms

- **Ratchet loop**: inspect, propose, apply, evaluate, keep or revert, recording a trial either way; the general form of autoresearch.
- **Programming the program**: configuring an autonomous process through a natural-language brief, so the human's artifact is the instructions rather than the work product.
- **Externalized bottleneck**: the one thing a given architecture level moves out of volatile memory and into durable, queryable state.
- **Frontier (leaves)**: commits with no children, the unexplored edge of a search DAG.
- **Lineage**: the ancestry path from a commit to the root, reconstructing what produced an outcome.
- **Mechanism versus culture**: the platform provides traversal and storage; prompts and project instructions decide what agents post and attempt.
- **Surface form**: an extracted entity label before resolution, which may be an abbreviation, alias, former name, spelling variant, or partial name.
- **Compression ratio**: raw surface forms divided by canonical entities; a high ratio is not automatically good, since over-merging creates a connected but false graph.
- **False merge**: collapsing two distinct entities into one node, contaminating every downstream traversal that touches it.
- **Grounding layer**: an evaluator that checks a claim against graph edges and names the specific missing evidence rather than critiquing freely.
- **Persistent world model**: graph state that outlives any single run, enabling cross-session planning, contradiction tracking, audit trails, and recovery after failure.
- **Complexity budget**: the declared ceilings on calls, workers, time, tokens, cost, retries, and writes, plus the minimum evidence required to finalize.
- **Artifact contract**: the typed handoff between agent roles, where a reviewer returns criterion-level defects rather than approval.
- **Graph autoresearch**: applying the ratchet loop to the extraction prompt, ontology, resolution policy, or query serializer instead of to model code.
