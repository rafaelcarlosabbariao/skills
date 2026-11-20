# Graph-engineering patterns

Reusable recipes drawn across the shelf. Each pattern: when to use, steps, source. Roman-numeral sources are sections of the paper (chapters/graph-engineering-karpathy-loop.md); patterns 14 to 18 come from MemPalace (chapters/mempalace.md). Details and caveats live in the chapters.

Patterns 1 to 13 are about **how much architecture**. Patterns 14 to 18 are about **what to keep, and in what form**. Where they conflict, the split is deliberate and the two chapters argue it out.

## 1. The ratchet loop

**When to use:** any search where a cheap, honest number can be produced on demand and a bad step can be undone. This is stage one of the build path and the general form of autoresearch.

**Steps:**
1. Confirm the four autonomy conditions hold: the output is verifiable, the action is reversible, the horizon is short, the environment is bounded. If any fails, stop and fix that first.
2. Inspect current state and recent history.
3. Propose exactly one motivated change. One change per trial is what makes the history readable.
4. Apply and commit the candidate before evaluating, so the revert target is unambiguous.
5. Evaluate. On a crash, inspect and fix only if the failure is mechanical, otherwise revert.
6. Keep the commit if the metric improved, otherwise reset to the previous retained commit.
7. Append a trial record either way, including crashes and reverts. The discarded trials are the point: they are the machine-readable form of what a human researcher holds in working memory.

**Source sections:** II (Karpathy's loop), II-D (why the loop works).

## 2. The program.md contract

**When to use:** before starting any unattended run. This is the brief that replaces supervision.

**Steps:** pin down each of these, and treat a missing one as a reason not to start.
1. Mutable files and protected files.
2. The metric and its direction, chosen so that changes you are about to make cannot flatter it.
3. The experiment budget.
4. The run command and how its output is parsed.
5. Crash handling.
6. Commit and revert rules.
7. Logging rules.
8. The human escalation policy.
9. Exhaustion criteria: what "done" or "out of ideas" means.

**Source sections:** II-A, II-B.

## 3. The staged build path

**When to use:** deciding what to add next to a system that already works but is not good enough. Add one stage at a time and hold each exit criterion before climbing.

**Steps:**
1. **Day 1, reflective loop.** Take one existing model call whose output can be evaluated. Add a stored first draft, an evaluator with explicit criteria, a revision step, and a stopping rule. Store every artifact. Exit: measured quality improvement.
2. **Day 2, one tool.** Add a single tool addressing a measured failure, with a typed schema, permissions, and result confirmation. Exit: the tool reduces that error class.
3. **Week 1, planning.** Only if the task path varies. Require a JSON plan before execution, validate dependencies, preserve successful work during replanning, cap retries and total cost. Exit: variable tasks complete.
4. **Week 2, multi-agent.** Begin with generator and critic. Expand to planner, implementer, test author, reviewer, security reviewer, synthesizer only as specialization adds signal. Every handoff is an artifact contract; a reviewer returns criterion-level defects, not approval. Use worktree isolation when multiple coding agents modify one repository. Exit: the role split beats a single agent.
5. **Month 1, persistent graph.** Versioned JSON or relational tables storing entities, claims, sources, relations, artifacts, agent runs, evaluations, versions, aliases, and open questions. Cheap-model extraction, stronger-model resolution, provenance on every edge. Exit: cross-session queries work.
6. **Month 2, swarm.** Only for embarrassingly parallel workloads. Exit: wall-clock gain with no quality loss.

**Source sections:** VI, Table II.

## 4. The complexity budget

**When to use:** before every autonomous or fanned-out run, without exception.

**Steps:**
1. Declare ceilings: maximum model calls, sub-agents, concurrent workers, tool calls, wall-clock time, tokens, financial cost, retries, and graph writes.
2. Declare the floor: the minimum evidence required before anything may be finalized.
3. On exhaustion, return four things: the best current artifact, the work actually completed, the unresolved issues, and the reason for stopping.
4. Never hide partial failure behind a fluent final answer. A confident summary of incomplete work is the failure mode this pattern exists to prevent.

**Source section:** VIII-B.

## 5. The six selection questions

**When to use:** at the start of any design, to pick the architecture level before writing code.

**Steps:** answer in order, and stop climbing as soon as the bottleneck is externalized.
1. Can success be verified? If not, do not begin with autonomy. Define a test, rubric, source requirement, or human decision.
2. Are the steps stable? If yes, chain. If no, planning or an orchestrator.
3. Are subtasks independent? If yes, parallelize. If no, model dependencies explicitly and limit concurrent writes.
4. Must alternative lineages remain available? If yes, DAG rather than one branch.
5. Must facts survive the run? If yes, persist artifacts and graph state, not transcript summaries.
6. Can the organization afford the cost and latency? Set budgets before adding workers.

**Source section:** VIII-A.

## 6. Fan-out with a defined reducer

**When to use:** a genuinely parallel workload: auditing every file for one defect class, extracting entities from thousands of documents, generating tests for independent modules, comparing candidate configurations, investigating independent hypotheses.

**Steps:**
1. Define the reducer **before** fan-out. How results combine is a design decision, not a cleanup step.
2. Check the task is decomposable at all. Architecture design, narrative writing, tightly coupled refactors, and subtle product decisions degrade when split.
3. Set the contract: concurrency limit, total worker cap, token budget, per-worker timeout, retry policy, evidence contract, deduplication policy, final evaluation gate.
4. Give each worker fresh context and a task-specific slice, not the whole state.
5. If adding a verification wave, give reviewers a different prompt, evidence set, or role. Identical reviewers reproduce correlated errors instead of catching them. Instructing reviewers to *refute* rather than assess is the stronger form.
6. Reduce through the defined reducer, then pass the final evaluation gate.

**Source sections:** IV-B, VI-F, IX-D, IX-E.

## 7. Extraction, resolution, assembly, query

**When to use:** building a knowledge graph from unstructured documents. First confirm the graph earns its cost (pattern 8).

**Steps:**
1. **Extract** with a cheap model and a schema-constrained call producing typed entities and subject-predicate-object relations. The schema is the only training data.
2. **Resolve** with a stronger model. Narrow candidates with cheap blocking signals first, group by entity type, use descriptions as contextual evidence, then ask the model to propose canonical clusters. String similarity alone fails both directions: it misses aliases with zero character overlap and incorrectly merges people who share names.
3. Keep resolution **additive and inspectable**: the canonical entity retains aliases, source documents, resolution rationale, confidence, and the run that created the merge, so an incorrect merge can be reversed without rebuilding the pipeline.
4. **Assemble** into a multigraph where nodes carry type, source, and count, and edges carry predicate, source document, and confidence.
5. **Query** by bounded traversal, never by dumping the graph. Identify starting entities, traverse a bounded neighborhood, filter edges by type or date, serialize the result, and let the answer cite edge identifiers.

**Source sections:** IV-C, IV-D, IV-E.

## 8. The graph-earns-its-cost test

**When to use:** whenever someone proposes a knowledge graph. Having agents is not a reason to have a graph.

**Steps:** a graph is likely **unnecessary** if any of these hold:
1. Tasks are independent.
2. No cross-session state is required.
3. Answers depend on one document.
4. Relations are fixed and simple.
5. A relational table answers every query.
6. Provenance is not needed.
7. Extraction errors would outweigh traversal value.

A graph **earns its cost** when connected queries, evolving relations, provenance, or shared world state are central to the job.

**Source section:** VIII-C.

## 9. Bounded context construction

**When to use:** every time a worker is given state from a graph. This is the discipline that stops a graph from becoming a larger context window.

**Steps:**
1. Resolve the entities mentioned in the task.
2. Expand one or two hops over allowed edge types only.
3. Include current artifact versions.
4. Prioritize recent verified claims.
5. Include conflicts and uncertainty rather than silently picking a side.
6. Serialize within an explicit token budget.
7. Attach stable edge identifiers so the answer can cite them.

**Source section:** V-B.

## 10. The graph-grounded evaluator

**When to use:** checking a generated claim against evidence, in place of free-form critique.

**Steps:**
1. Decompose the claim into the specific edges that would have to exist to support it.
2. Check the graph for each.
3. Return structured feedback: the decision, the claim, the reason (name the missing or contradictory path), and `required_evidence` as a list of the specific source-backed relations needed.
4. Treat a grounded claim as sourced, not verified. The graph preserves claims so they can be inspected; it does not convert them into truth.

**Source sections:** V, IX-F.

## 11. Graph autoresearch

**When to use:** improving an extraction pipeline, ontology, resolution policy, or query serializer. It is pattern 1 applied one level up.

**Steps:**
1. Build a gold set first. Without it there is no ratchet.
2. Read the current prompt or schema and the score history.
3. Propose one prompt or schema change.
4. Run extraction on the gold set.
5. Compute precision, recall, F1, schema-valid response rate, cost, and latency. For resolution add compression ratio, pairwise precision and recall, false merge rate, missed merge rate, and manual review rate.
6. Keep if improved, revert if worse.
7. Guard against the metric you can see: never optimize compression alone, and never trade resolution precision or query latency for extraction quality without saying so.

**Source sections:** VII-A, VII-B, IX-B.

## 12. Multi-hop query evaluation

**When to use:** validating a graph query layer. Accuracy on the answer alone will pass a system that cites irrelevant edges.

**Steps:** a valid answer must do all of the following, and each is a separate check.
1. Resolve the question's entities correctly.
2. Retrieve a relevant subgraph.
3. Use supported edges.
4. Respect time and source constraints.
5. Distinguish fact from inference.
6. Cite the edges used.
7. Identify missing evidence rather than filling the gap.

Then build adversarial cases: misleading aliases, contradictory dates, disconnected paths.

**Source section:** VII-C.

## 13. Production monitoring by trend

**When to use:** once a graph is live. Track movement, not isolated scores.

**Steps:** watch extraction rate by document type, schema failure rate, resolution compression, connected-component changes, query latency, subgraph size, cited-edge validity, token cost, stale entity count, graph update failures, and agent retry rates.

Two readings to have ready:
- A sudden **increase** in isolated nodes may signal resolution regression.
- A sudden **decrease** may signal over-merging.

**Source section:** VII-D (paper).

## 14. The verbatim payload split

**When to use:** designing any memory layer, before choosing a store. This is the decision that is expensive to reverse later.

**Steps:**
1. Separate the **payload** (what a future reader will need to see) from the **index** (what helps find it). They are different artifacts with different tolerances.
2. Keep the payload whole. Store the original text, unsummarized and unparaphrased, as the unit of evidence.
3. Put all lossy compression in the index: shorthand, embeddings, extracted entities, canonical clusters. The index's job is to say which payload to open.
4. Treat the index as **rebuildable** and the payload as **irreplaceable**. If a schema change or a resolution bug means rebuilding the index, that must be an inconvenience, not a data loss.
5. Ask the qualifying question before deviating: is the worse failure an answer that cannot be found, or an answer that is confidently wrong? Findability failures are recoverable, corrupted content is not.
6. Ask whether anything downstream needs the exact words (quotation, cloaking decisions, authenticity reads, client deliverables). If yes, the payload cannot be a derivative.

**Source:** MemPalace, read against the paper's §IV-D and §IX-G.

## 15. Scoped retrieval

**When to use:** any corpus large enough that a flat search returns plausible-but-wrong neighbors.

**Steps:**
1. Give the corpus a scope hierarchy before it grows: a top-level scope per person or project, a topic level beneath it, and the original items at the leaves.
2. Cross-reference items so they are reachable from more than the one axis they were filed under. The Zettelkasten property is that filing decisions do not become retrieval limits.
3. Scope the query first, search second. Searching one wing beats searching everything and ranking.
4. Keep a lexical or exact-match path alongside the semantic one, for the queries where a specific term matters and embedding similarity will miss it.
5. Expect vague queries. The system has to serve "that thing we discussed once," not only well-formed questions.

**Source:** MemPalace.

## 16. Validity windows instead of edits

**When to use:** any fact that can stop being true: an audience rule, a price, a role, a policy, a code or lexicon that drifts.

**Steps:**
1. Store facts with time bounds rather than as current-state rows.
2. Make **invalidate** an operation distinct from delete. An invalidated fact stays queryable and keeps its window.
3. Support a timeline query, so "what did we believe, and when" is answerable without reconstructing history from diffs.
4. Never silently overwrite a fact that has changed. An overwrite destroys the one thing that makes drift visible.

**Source:** MemPalace's temporal knowledge graph, which addresses the gap the paper leaves in §V.

## 17. Keep memory work off the chat surface

**When to use:** as soon as a memory or logging layer is wired into an interactive agent.

**Steps:**
1. Move writes (filing, diaries, timestamps, summaries) into background hooks or a subagent. They should not consume turns or tokens in the main window.
2. Watch for duplicate work: an agent re-emitting the same block each time a hook fires is the symptom that the write path is running inline.
3. Make specialist context discoverable at runtime (list it on demand) rather than resident in the system prompt.
4. Save before context compression, not only on a timer.
5. Measure the change in tokens per session. The cost of an inline memory layer is real and countable.

**Source:** MemPalace, converging on the paper's §V-B bounded-context rule from the opposite direction.

## 18. The honest benchmark

**When to use:** reporting any retrieval, extraction, or evaluation number, internally or publicly.

**Steps:**
1. Hold out a split. Tune on a dev set, report on questions not seen during tuning, and say which is which.
2. Publish the **held-out** figure as the headline, not the best figure.
3. If the last increment was obtained by inspecting specific wrong answers, name that as teaching to the test and do not headline the result.
4. State what the number does and does not require: which stages need an API key, a model, or a network call.
5. Refuse side-by-side comparisons across projects measuring different things on different splits. Retrieval recall next to end-to-end accuracy is not a comparison.
6. Make results reproducible from the repository, with per-question outputs committed, so a reader can check rather than trust.

**Source:** MemPalace's benchmark methodology, which is the paper's §IX-B warning practiced rather than stated.
