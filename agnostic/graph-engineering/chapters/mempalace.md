---
title: "MemPalace"
author: "MemPalace project (MISSION.md bylined Milla Jovovich; backend co-founder credited as @bensig)"
year: 2026
kind: repository
theme: practice
shelf: graph-engineering
slug: mempalace
source: "https://github.com/mempalace/mempalace (MIT). Read at README badge v3.7.0, repo created 2026-04-05, last push 2026-08-07, 58.2k stars, Python."
read_on: 2026-08-08
---

# MemPalace (2026)

## The claim

Memory belongs outside the context window, and the thing you put there should be **the original text, not a summary of it**. MemPalace stores conversation history verbatim, indexes it in a spatial hierarchy borrowed from the Zettelkasten (wings for people and projects, rooms for topics, closets for compressed pointers, drawers for the original content), and retrieves it by scoped semantic search. Its README states the position plainly: conversation history is stored as verbatim text and retrieved by semantic search, and the system says it does not "summarize, extract, or paraphrase."

The stated origin is a working complaint rather than a research program: an agent that "kept waking up like 'hey what are we doing today'" after hours of prior work, and existing memory systems that "felt like large empty warehouses where you just dump huge amounts of info." The design goal that follows is unusual and worth quoting, because it is the axis on which this work parts company with the graph-engineering paper: store information in a highly structured way, **"But also RETRIEVING it in a highly UNSTRUCTURED way."**

Local-first throughout. The headline retrieval number requires no API key, no cloud, and no LLM at any stage.

## Core claims

- Verbatim storage is the default, and lossy transformation of the payload is the failure mode to avoid. Summaries are what other systems store; drawers hold the original.
- Structure exists to make retrieval **scopable**, not to compress the content. Searching a wing or a room beats searching a flat corpus.
- Retrieval should work from vague, half-remembered angles ("remember when we talked about that idea"), which keyword search cannot serve. The Zettelkasten inheritance is cross-referencing so material is findable "from any angle, not just the one you filed them under."
- The retrieval layer is a contract, not a vendor. The backend interface is exercised across deliberately different substrates "so the contract is never accidentally shaped around one vendor." ChromaDB is default; `sqlite_exact`, Milvus, Qdrant, and pgvector are opt-in.
- Memory work should not happen in the chat window. Moving diary writes, palace filing, and timestamp injection into background hooks and a subagent removed the token cost of re-transmitting them, reported as roughly $1.13 per session falling to zero.
- Agent context should be discovered at runtime, not preloaded. Each specialist agent gets its own wing and diary, listed on demand, with "no bloat in your system prompt."
- A knowledge graph is included but is not the primary store: a temporal entity-relationship graph with validity windows (add, query, invalidate, timeline) on local SQLite, sitting beside the verbatim layer rather than replacing it.
- Benchmarks should be reported at the number that generalizes. The held-out 450-question figure is named as "the honest generalisable figure," and the project declines to headline a higher number because reaching the last fraction involved inspecting specific wrong answers, which its own methodology file flags as **teaching to the test**.
- Cross-project comparison is declined on methodological grounds: placing retrieval recall next to end-to-end QA accuracy "is not an honest comparison."

## Frameworks and models

**The palace hierarchy.** Wings scope people and projects. Rooms hold topics. Drawers hold the original verbatim content. Closets hold compressed pointers. The stated inheritance is Luhmann's Zettelkasten: small cross-referenced cards that point at each other, so an item is reachable from more than the one axis it was filed under.

**Two-tier memory, and the honest reading of "verbatim."** The closet layer uses a compression scheme the project calls AAAK, which reduces names, repeated words, concepts, and key moments to AI-readable shorthand. The described flow is: the closet tells the model *where* to look, then the full content is pulled from the drawer. So the system is not free of lossy compression. It has confined it to the **index**, leaving the **payload** untouched. That distinction is the actual design claim, and it is stronger than the flat slogan.

**Mining, sweeping, waking.** `mempalace mine` ingests project files or Claude Code sessions (`--mode convos`, scoped per project with `--wing`). `mempalace sweep` stores one verbatim drawer per user or assistant message for per-message recall, described as idempotent and resume-safe. `mempalace search` queries. `mempalace wake-up` loads context into a new session, which is the operation the whole system exists to make possible.

**The pluggable backend contract.** Defined in `mempalace/backends/base.py`. Backends differ in mode (local embedded, local exact, server), namespace support, and lexical search support, and every non-default one is opt-in. Selection by `--backend`, `MEMPALACE_BACKEND`, or `config.json`. The contract is validated across substrates specifically to prevent it calcifying around one implementation.

**The retrieval ladder.** Raw semantic search with no heuristics and no LLM reaches 96.6% R@5 on LongMemEval (500 questions). A hybrid pipeline adding keyword boosting, temporal-proximity boosting, and preference-pattern extraction reaches 98.4% on a held-out 450 questions tuned on a 50-question dev split. An LLM reranker promoting the best of the top 20 reaches at least 99%, and is reported as model-agnostic, reproduced with Claude Haiku, Claude Sonnet, and a local model via Ollama. Other results: LoCoMo 60.3% R@10 raw and 88.9% hybrid, ConvoMem 92.9% average recall, MemBench 80.3% R@5.

**Background hooks as the delivery mechanism.** Auto-save hooks for Claude Code, Codex CLI, and Cursor save periodically and before context compression. The v4 redesign moved this work off the chat surface entirely after the author noticed the agent "literally writing the same info down over and over again" when hooks fired inline.

**The temporal knowledge graph.** Entity-relationship, with validity windows and an explicit invalidate operation plus a timeline query. Time-bounded facts are first-class rather than a modeling afterthought.

## Decision rules

- If the payload can be stored whole, store it whole. Compress the index, not the content.
- If retrieval has to serve vague recall, semantic search over original text beats keyword search over summaries.
- If memory writes are happening inside the chat window, move them to background hooks. They are costing tokens on every turn and producing duplicate work.
- If an agent needs specialist context, make it discoverable at runtime rather than resident in the system prompt.
- If a storage layer might ever be swapped, define the contract first and validate it against a deliberately different substrate. A contract tested against one backend is a description of that backend.
- If a fact has a validity window, model the window. Invalidation is an operation, not a delete.
- If a benchmark number was reached by inspecting specific wrong answers, it is not the number to publish. Publish the held-out figure.
- If two projects report different metrics on different splits, do not place them side by side.
- If ingesting an existing transcript archive, back it up before backfilling.
- If testing a new memory tool, do not point it at critical files first. The project says this in its own mission document.

## Where it stands against the paper

Read this chapter against `graph-engineering-karpathy-loop`. They agree on the premise and split on the method.

**Agreement, arrived at independently: memory goes outside the context window, and the working context stays small.** The paper's §V-B insists each worker gets a task-specific subgraph rather than a serialized graph, and warns that a graph "should not become a new form of context dumping." MemPalace's runtime-discoverable agent wings ("no bloat in your system prompt") and its move of hook writes off the chat surface are the same instinct reached from a token bill rather than from architecture. Two independent derivations of one rule is the strongest evidence this shelf carries for it.

**Disagreement one, and the important one: canonical resolution versus verbatim retention.** The paper's pipeline is extraction, then resolution of surface forms into canonical entities, then reasoning over a typed graph. It accepts that the graph is a lossy derivative of the corpus, and manages the risk procedurally: keep merges additive, inspectable, and reversible, because §IX-G says a false merge contaminates every downstream traversal. MemPalace takes the other bet. It does not make the payload depend on resolution at all, so a resolution error degrades *findability* rather than corrupting *content*. The paper's graph can answer "which claims conflict" in a way MemPalace cannot; MemPalace can always return what was actually said, which a resolved graph cannot reconstruct once it has collapsed the surface forms. Neither is free. Choose by asking whether your downstream failure is worse when an answer is unfindable or when it is confidently wrong.

**Disagreement two: cited edges versus original text as the unit of evidence.** The paper's grounding layer decomposes a claim into the specific edges that would support it and names the missing ones. That requires a typed graph and gives edge-level citation. MemPalace's evidence is the drawer, which is the original passage. It cannot tell you which relation is missing, but its citation cannot be an artifact of extraction either. The paper's §IX-F caveat cuts toward MemPalace here: a graph keeps claims, sources and relationships inspectable, but "it does not convert claims into truth." Verbatim text is the least processed form of that inspection.

**Disagreement three, softer: does the graph earn its cost.** The paper's §VIII-C test says do not add a knowledge graph merely because the system has agents, and reserves it for connected queries, evolving relations, provenance, and shared world state. MemPalace ships a graph but subordinates it to semantic search, which is arguably the paper's own test applied honestly: most recall questions do not need traversal, so traversal is not the primary path.

**Where MemPalace practises what the paper preaches.** The paper warns in §IX-B that a ratchet improves only the metric it can see, and that an evaluation set can be overfit. MemPalace names that exact failure in its own results, calls it teaching to the test, and publishes the held-out number instead of the flattering one. It is the clearest worked example on this shelf of the paper's evaluation discipline being followed by someone with an incentive not to.

**Where the slogan overstates.** "It does not summarize, extract, or paraphrase" is true of drawers and not of closets, since AAAK compression is by construction lossy. The system's real claim is the layered one, and the layered one is the defensible one.

## Applications

- **Corpora of quoted talk** (community posts, interviews, field notes) are the direct application. A read that quotes a person needs the original text, not a paraphrase of it, both for any decision about anonymizing it and because the unguarded register is the evidence.
- **A derived graph over stored observations** splits the same way MemPalace does: store the observations, compute co-presence or similarity at query time, and treat derived structure as disposable.
- **Validity windows** are the piece worth taking outright. Rules, codes and lexicons drift, and most note systems have no way to say a claim was true for a window and is now invalid without deleting it. `invalidate` plus `timeline` is a better shape than an edit.
- **Cross-session continuity for long engagements.** Work that runs for weeks across many sessions is the wake-up problem; ask whether the constraint is model capability or the absence of a place to put durable state.
- **Before adopting it as software**, note what installation entails: a Python toolchain, roughly 300 MB of embedding model, a vector-store backend, an MCP server exposing 36 tools, and hooks that capture session content to local storage. Nothing leaves the machine unless opted in, but mining a whole directory of session transcripts sweeps across every project, including confidential client work. Scope by wing before mining, not after.

## Key terms

- **Wing**: the top-level scope in the palace, one per person or project.
- **Room**: a topic container inside a wing.
- **Drawer**: where original verbatim content lives; the unit of evidence.
- **Closet**: a compressed pointer layer holding AAAK shorthand for names, repeated words, concepts, and key moments, which tells a model where to look before it pulls the drawer.
- **AAAK**: the project's compression scheme for closet entries, deliberately not an acronym. Lossy by design, and confined to the index rather than the payload.
- **Mine**: ingest files or session transcripts into the palace.
- **Sweep**: store one verbatim drawer per message for per-message recall; idempotent and resume-safe.
- **Wake-up**: load relevant context into a new session, the operation the system exists to make possible.
- **Backend contract**: the storage interface in `mempalace/backends/base.py`, validated across deliberately different substrates so it is not shaped around one vendor.
- **Validity window**: the time bounds on a knowledge-graph fact, with invalidation as an operation distinct from deletion.
- **Teaching to the test**: the project's own name for improving a benchmark number by inspecting specific wrong answers; the reason it publishes the held-out figure instead.
- **Held-out figure**: the number measured on questions not seen during tuning, named as the honest generalisable one.
