# Graph-engineering cheatsheet

Quick routing: situation, which level or model applies, what to check first. Full procedures in patterns.md; full arguments in chapters/graph-engineering-karpathy-loop.md (architecture) and chapters/mempalace.md (memory and retrieval).

## Choosing the architecture level

| Situation | Level | Check first |
|---|---|---|
| Simple, low-risk question | Zero-shot | Lowest latency wins. Do not add architecture to a question that does not have a failure mode |
| Output can be checked | Loop | Is there a cheap honest number, and is the action reversible? Repeated feedback improves the artifact only if both hold |
| Stable sequence of steps | Chain | Are the stages predictable and testable? If the path varies between runs, this is the wrong level |
| Clear input categories | Router | Does routing separate genuinely different policies or models, or is it one prompt with branches? |
| Independent units of work | Parallel | Is the reducer defined? No reducer means no fan-out |
| Decomposition varies per task | Orchestrator-workers | Does the specialization add signal, or just headcount? |
| Alternatives must stay alive | Commit DAG | Will most results never merge, and does a failed run still carry evidence? If yes, stop forcing one branch |
| Facts must survive the session | Knowledge graph | Run the earns-its-cost test before building. Having agents is not a reason |
| Very large parallel work | Dynamic workflow | Concurrency cap, worker cap, token budget, timeout, retry policy, dedup policy, evaluation gate. All of them, before launch |

## The six selection questions

| Question | If yes | If no |
|---|---|---|
| Can success be verified? | Proceed | **Stop.** Do not begin with autonomy. Define a test, rubric, source requirement, or human decision |
| Are the steps stable? | Chain | Planning or an orchestrator |
| Are subtasks independent? | Parallelize | Model dependencies explicitly, limit concurrent writes |
| Must alternative lineages remain? | DAG | A single branch is fine |
| Must facts survive the run? | Persist artifacts and graph state | Transcript is acceptable |
| Affordable in cost and latency? | Proceed | Set budgets before adding workers, not after |

## Autonomy triage

| Situation | Model | Check first |
|---|---|---|
| About to start an unattended run | The four conditions | Verifiable output, reversible action, short horizon, bounded environment. Any gap means autonomy on credit |
| Writing the brief for an unattended agent | program.md contract | Mutable vs protected files, metric and direction, budget, run command, output parsing, crash handling, commit/revert rules, logging, escalation, exhaustion criteria |
| Picking the metric | Metric-gaming check | What could you change that moves this number without improving anything? If there is an answer, the metric is wrong |
| Metric is improving but something feels off | Ratchet blindness | A ratchet improves only the metric it can see. Retain constraints: memory, throughput, stability, generalization, cost, latency |
| Agent hit the budget ceiling | Complexity budget | Return best artifact, completed work, unresolved issues, and the reason for stopping. Never a fluent summary that hides partial failure |
| Tempted to let a loop self-modify production | Limitation IX-A | A loop that works on one bounded repo does not prove safe self-modification of a production platform. Transfer the architecture, not the autonomy level |

## Multi-agent triage

| Situation | Model | Check first |
|---|---|---|
| Considering a swarm | Fragmentation check | Does this task need one coherent context? Architecture design, narrative writing, tightly coupled refactors, and subtle product decisions degrade when split |
| Swarm is busy, value is unclear | Workflow metric misreading | Task success and cost, not activity. More agents can increase activity without increasing value |
| Parallel workers all agreed | Correlated error | Identical workers reproduce the same mistake. A verification wave helps only if reviewers have a different prompt, evidence set, or role |
| Adding a review stage | Refutation framing | Instruct reviewers to refute the finding, not to assess it. Reviewers return criterion-level defects, never "looks good" |
| Multiple coding agents, one repo | Worktree isolation | Are they going to write over each other? Isolate before, not after |
| Large fan-out proposed | Cost | A 1,000-sub-agent run at high effort can cost tens of dollars. Price it before launching it |
| Claude is writing the orchestration | Retained responsibility | You still own: objective, files in scope, output contract, permissions, verification policy, concurrency and token budget, rollback rule, evidence required for synthesis |

## Graph triage

| Situation | Model | Check first |
|---|---|---|
| Someone proposes a knowledge graph | Earns-its-cost test | Independent tasks, no cross-session state, single-document answers, fixed simple relations, a table would do, no provenance need, or extraction error exceeding traversal value: any of these and the graph is probably unnecessary |
| Building extraction | Schema-first | The schema is the only training data. One structured-output call per document replaces the NER and relation classifier |
| Two labels, same entity | Resolution as reasoning | String similarity misses zero-overlap aliases and merges distinct people who share names. Group by type, use descriptions as evidence, let a stronger model arbitrate |
| A merge was made | Reversibility | Did it retain aliases, source documents, rationale, confidence, and the run id? If not, it cannot be undone without rebuilding |
| Compression ratio looks great | Over-merging | High compression is not automatically good. Check false merge rate and missed merge rate |
| Isolated nodes spiked | Resolution regression | Sudden increase suggests resolution broke. Sudden decrease suggests over-merging |
| Query returns a fluent answer | Path evaluation | Evaluate the path, not just the answer. Fluent answers can cite irrelevant edges |
| Serializing graph state for a worker | Bounded context construction | Resolve entities, expand one or two hops, current versions, recent verified claims, include conflicts, fit the token budget, attach edge ids. Never dump the graph |
| Checking a claim | Grounding layer | Name the specific missing edges and the required evidence. Structured feedback beats free-form critique |
| Graph says a claim is supported | IX-F | Sourced is not verified. The graph preserves claims for inspection; it does not make them true |
| Work lineage and domain facts in one store | Do not collapse | The commit DAG answers what changed and what descends from what. The knowledge graph answers which entities exist and which sources support the relation. Connect them, keep them separate |

## Memory triage

| Situation | Model | Check first |
|---|---|---|
| Choosing what a memory layer stores | Verbatim payload split | Payload whole, compression in the index. Which failure is worse here: unfindable, or confidently wrong? |
| About to store a summary as the record | Stop | A summary is an index entry, not evidence. Store the original alongside it or you cannot recover the words |
| Anything downstream needs exact wording | Verbatim only | Quotation, cloaking decisions, authenticity reads, client deliverables. A resolved graph cannot reconstruct surface forms once collapsed |
| Index is corrupt or the schema changed | Rebuildability test | Can you rebuild the index from the payload? If not, the split was never real |
| Flat search returning plausible-but-wrong hits | Scoped retrieval | Scope by wing or project first, then search. Ranking a whole corpus is not the same as searching the right part of it |
| Query names a specific term and misses | Lexical path | Semantic similarity alone misses exact terms. Keep a keyword or exact-match route beside it |
| Recall requests are vague by nature | Unstructured retrieval | "That thing we discussed once" is the real query shape. Cross-reference so filing decisions are not retrieval limits |
| A stored fact has stopped being true | Validity windows | Invalidate, do not delete, and never silently overwrite. Overwriting destroys the only evidence of drift |
| Asking what we believed and when | Timeline query | If this needs reconstructing from diffs, the facts were stored as current state and should not have been |
| Agent starts each session from nothing | Wake-up path | Is there a place to put durable state, or is this being blamed on model capability? |
| Memory writes appearing in the chat window | Move to hooks | Duplicate blocks each turn is the symptom. Measure tokens per session before and after |
| Specialist context sitting in the system prompt | Runtime discovery | List it on demand instead. Resident context is paid for on every turn |
| Reporting a retrieval or extraction number | Honest benchmark | Held-out figure as the headline. If the last increment came from inspecting wrong answers, that is teaching to the test |
| Comparing two memory systems | Refuse the wrong comparison | Retrieval recall against end-to-end QA accuracy is not a comparison. Different metrics on different splits do not go side by side |
| Adopting a memory tool over a mixed corpus | Scope before mining | Mining a whole projects directory sweeps every project at once. Client-confidential material has a boundary; scope by wing first |

## Metric misreadings, by layer

| Layer | Metric | The misreading |
|---|---|---|
| Extraction | Entity and relation F1 | High precision hides missing entities |
| Resolution | Pairwise precision and recall | Compression alone rewards over-merging |
| Graph | Components, density | One connected component is not always desirable |
| Query | Accuracy, cited paths | Fluent answers can cite irrelevant edges |
| Workflow | Task success, cost | More agents can increase activity without value |
| Operations | Recovery, corrections | Average success hides catastrophic cases |

## Quick rules

- Name the bottleneck first, then take the lowest level that externalizes it.
- The bottleneck is rarely the next model call. It is where memory and evaluation live.
- If success cannot be verified, autonomy does not start.
- One motivated change per trial, and record the reverts too.
- Define the reducer before the fan-out.
- Store artifacts before storing conversations.
- Use a DAG when alternatives should stay alive; use a graph when relationships and persistence matter; use a swarm only when the task is parallel and the reducer is defined.
- The agent forgets, the graph does not. That is the point of the graph and the limit of the swarm.
- A graph preserves claims for inspection. It does not convert them into truth.
- A loop amplifies your objective; a graph amplifies your ontology. Both amplify a specification mistake.
- Compress the index, never the payload. The index is rebuildable; the original words are not.
- Scope the query before you run it. A wing beats a corpus.
- Invalidate, do not delete. Overwrite is how drift becomes invisible.
- Memory writes belong in background hooks, not in the turn.
- Publish the held-out number. If the last increment came from reading the wrong answers, it is teaching to the test.
- The reliability test: every important output traces to an objective, a plan, an artifact, a source, a graph path, an evaluator decision, and a bounded execution record. When that is false, more agents means more opacity.
