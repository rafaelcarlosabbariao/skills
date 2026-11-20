# Graph-engineering glossary

Merged terms from both chapters, alphabetical. Entries marked with a section sign (§) source to the paper, chapters/graph-engineering-karpathy-loop.md, and name the section where it helps. Entries marked *(mempalace)* source to chapters/mempalace.md. Read the chapters for full context.

Where the two works use the same word differently, both senses are given in one entry and the difference is the point.

**AAAK** *(mempalace)*: MemPalace's compression scheme for closet entries, reducing names, repeated words, concepts, and key moments to model-readable shorthand. Deliberately not an acronym. Lossy by design, and confined to the index so the drawer stays whole.

**AgentHub** (§III): Karpathy's sketch of an agent-first collaboration platform, a bare Git repository plus a message board, whose slogan is "GitHub is for humans. AgentHub is for agents." Explicitly a work in progress, not production software.

**agentic engineering** (§X): the middle stage of the progression, where the human specifies, orchestrates, verifies, and remains responsible for quality, rather than expressing intent and letting the model write (vibe coding) or sharing durable typed state between agents (graph engineering).

**artifact contract** (§VI-D): the typed handoff between agent roles. A reviewer under an artifact contract returns criterion-level defects rather than an approval verdict.

**artifact plane** (§VI-G): the plane of the reference architecture storing plans, drafts, code changes, reports, metrics, and evaluations as immutable versions.

**autoresearch** (§II): Karpathy's single-agent loop placing an agent in an executable research harness with a mutable training program, a fixed metric, a time budget, Git history, and instructions. Roughly 700 experiments in two days, about 20 retained optimizations.

**backend contract** *(mempalace)*: the storage interface in `mempalace/backends/base.py`, deliberately exercised across different substrates (embedded, exact, server) so it is never shaped around one vendor. A contract tested against a single backend is a description of that backend.

**blocking signal** (§IV-D): a cheap filter that narrows the candidate set before a model arbitrates entity resolution, needed once resolution runs at scale.

**bounded context construction** (§V-B): building each worker a task-specific subgraph (resolve entities, expand one or two hops, include current versions, prioritize recent verified claims, include conflicts, fit a token budget, attach edge ids) instead of serializing the graph.

**closet** *(mempalace)*: the compressed pointer layer holding AAAK shorthand. Its only job is to tell a model which drawer to open. Compare **bounded context construction** (§V-B), which solves the same problem by traversal rather than by index.

**commit DAG** (§III-D, §V-A): the work-lineage graph where commits are nodes and parent links directed edges, and a node can carry hypothesis, diff, metric, runtime, memory, environment, keep-or-discard status, and links to discussion. Answers what changed and what descends from what.

**complexity budget** (§VIII-B): the declared ceilings for a run (model calls, sub-agents, concurrent workers, tool calls, wall-clock time, tokens, cost, retries, graph writes) plus the minimum evidence required to finalize.

**compression ratio** (§VII-B): raw surface forms divided by canonical entities. A high ratio is not automatically good, because over-merging produces a connected but false graph. Note the two works compress different things: this ratio measures loss in the *payload*, whereas MemPalace's AAAK compresses only the *index*. See **payload versus index**.

**control plane** (§VI-G): the plane that receives objectives, creates plans, allocates budgets, starts workflows, and decides when to stop.

**decision scenario for architecture**, see **six selection questions**.

**drawer** *(mempalace)*: where original verbatim content lives; MemPalace's unit of evidence. The counterpart to the paper's cited edge, and the two works disagree about which is the better citation.

**Dynamic Workflows** (§IV-B): Anthropic's feature where the model writes a JavaScript orchestration program for the current task. Up to 16 concurrent sub-agents, a hard cap of 1,000 per workflow, fresh context per sub-agent, intermediate state in script variables.

**evaluation plane** (§VI-G): the plane running deterministic checks, model evaluators, statistical scorers, and human review.

**evaluator-optimizer** (§IV-A): the workflow pattern where one role generates and another evaluates against criteria in a loop. Its graph role is the grounding layer.

**execution plane** (§VI-G): the plane running tools, tests, training jobs, code modifications, and sub-agents in isolated environments.

**externalized bottleneck** (§I): the one thing each architecture level moves out of volatile memory into durable, queryable state. Loop: iteration and evaluation. Chain: task order. Swarm: parallel search and role specialization. DAG: experiment lineage. Knowledge graph: shared facts, provenance, cross-session memory.

**false merge** (§IX-G): collapsing two distinct entities into one node. Contaminates every downstream traversal, since queries then combine both entities' employers, projects, dates, and actions.

**four conditions** (§II-D): what makes a task compatible with autonomy. The output is verifiable, the action is reversible, the horizon is short, the environment is bounded.

**fragmentation** (§IX-E): the quality loss when work that needs one coherent context is divided into isolated units. Named risks: architecture design, narrative writing, tightly coupled refactors, subtle product decisions.

**frontier** (§III-C): the set of commits with no children (`ah leaves`), the unexplored edge of the search DAG.

**graph autoresearch** (§VII-A): the ratchet loop applied to the extraction prompt, ontology, resolution policy, or query serializer rather than to model code.

**graph plane** (§VI-G): the plane storing entities, claims, relations, provenance, experiment lineage, and task dependencies.

**graph-grounded evaluator** (§V): an evaluator that decomposes a claim into the edges that would support it, checks the graph, and returns structured feedback naming the decision, the reason, and the required evidence.

**held-out figure** *(mempalace)*: a score measured on items not seen during tuning, named by the project as the honest generalisable number and published as the headline in place of a higher tuned one.

**knowledge graph** (§IV-C, §V-A): the domain-knowledge graph answering which entities exist, how they relate, which sources support a relation, and which claims conflict. Complementary to the commit DAG and not to be collapsed with it.

**lineage** (§III-C): the ancestry path from a commit back to the root, reconstructing what produced an outcome.

**mechanism versus culture** (§III-B): the deliberate separation where the platform supplies storage and traversal while prompts and project instructions define what agents post, how they describe results, and which experiments they attempt.

**mine** *(mempalace)*: ingest files or session transcripts into the palace. Scope with a wing before mining a mixed corpus.

**orchestrator-workers** (§IV-A): the workflow pattern where a central model dynamically decomposes, assigns, and synthesizes. Its graph role is shared memory: workers read and write the graph while the orchestrator's context stays clean.

**parallelization** (§IV-A): the workflow pattern running independent calls concurrently, by sectioning or by voting. Its graph role is a shared surface where workers publish non-overlapping findings.

**payload versus index** *(mempalace)*: the shelf's second axis. The payload is what a future reader must see and is kept whole; the index is what helps find it and absorbs all lossy compression. The index is rebuildable, the payload is not.

**persistent world model** (§V): graph state that outlives any single run, enabling long-running investigations, cross-session planning, incremental ingestion, contradiction tracking, temporal facts, versioned decisions, audit trails, model handoff, and recovery after a failed run. Slogan: the agent forgets, the graph does not.

**program.md** (§II-A, §II-B): the human's artifact in autoresearch, describing the research process, constraints, metric, logging rules, and autonomy policy. The instrument of "programming the program."

**programming the program** (§II-B): configuring an autonomous process through a natural-language brief, so improving results means revising the instructions rather than the work product.

**prompt chaining** (§IV-A): the workflow pattern where one model call produces an artifact for the next in a fixed sequence. Its graph role is validation: check entities against the current graph.

**ratchet loop** (§II-D): the reusable template underneath autoresearch. Inspect, propose, apply, evaluate, then keep or revert, appending a trial record either way, crashes included.

**reducer** (§VI-F): the defined combination step for parallel results. Must be specified before fan-out.

**reflective loop** (§VI-A): stage one of the build path. A stored first draft, an evaluator with explicit criteria, a revision step, a stopping rule, and every artifact stored.

**resolution** (§IV-D): mapping extracted surface forms to canonical entities by grouping candidates by type and using descriptions as contextual evidence. Should be additive and inspectable so incorrect merges are reversible.

**room** *(mempalace)*: a topic container inside a wing.

**routing** (§IV-A): the workflow pattern where a classifier sends input to a specialized prompt, model, or tool set. Its graph role is classifier input: entity type and degree route queries.

**scoped retrieval** *(mempalace)*: narrowing to a wing or room before searching, rather than ranking a flat corpus. Filing decisions must not become retrieval limits, which is what the cross-referencing is for.

**six selection questions** (§VIII-A): the design gate. Can success be verified; are the steps stable; are subtasks independent; must alternative lineages remain available; must facts survive the run; can the organization afford the cost and latency.

**staged build path** (§VI, Table II): reflective loop (day 1), tool use (day 2), planning (week 1), multi-agent (week 2), persistent graph (month 1), swarm workflow (month 2), each with an exit criterion.

**surface form** (§IV-D): an extracted entity label before resolution. May be an abbreviation, alias, former name, spelling variant, or partial name.

**sweep** *(mempalace)*: storing one verbatim drawer per user or assistant message for per-message recall; idempotent and resume-safe.

**teaching to the test** *(mempalace)*: the project's own name for improving a benchmark by inspecting specific wrong answers, and its stated reason for not headlining the resulting number. The paper states the same hazard abstractly in §IX-B; this is it practiced.

**traverse the search graph** (§III-A): the primary operation in agent-first collaboration, replacing "merge this into main," on the premise that most results never merge and a failed experiment still contains evidence.

**validity window** *(mempalace)*: the time bounds on a knowledge-graph fact, with invalidation as an operation distinct from deletion, plus a timeline query. Fills the gap the paper leaves when it lists temporal facts in §V without a mechanism.

**verbatim storage** *(mempalace)*: keeping the original text unsummarized, unextracted, and unparaphrased. True of drawers and not of closets, so the defensible form of the claim is the layered one, not the slogan.

**vibe coding** (§X): the first stage of the progression, where the human expresses intent and the model writes.

**wake-up** *(mempalace)*: loading relevant context into a new session. The operation the whole system exists to make possible, and the direct answer to "the agent forgets."

**wing** *(mempalace)*: the top-level scope in the palace, one per person or project. The unit you scope a search to.

**worktree isolation** (§VI-D): giving each coding agent its own working copy when several modify the same repository in parallel.

**Zettelkasten** *(mempalace)*: Luhmann's method of small cross-referenced index cards pointing at each other, named as the architecture behind wings, rooms, closets, and drawers. The inherited property is reachability from more than one axis.
