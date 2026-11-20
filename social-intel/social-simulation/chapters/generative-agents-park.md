---
title: "Generative Agents: Interactive Simulacra of Human Behavior"
author: "Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein"
year: 2023
kind: paper
theme: simulation
shelf: social-simulation
slug: generative-agents-park
---

# Generative Agents (Park et al., UIST 2023)

## The claim

Twenty-five LLM-driven agents, each equipped with a memory stream, a retrieval function, periodic reflection, and recursive planning, produce believable individual and emergent social behavior in a sandbox town (Smallville): information diffuses, relationships form, and agents coordinate a party none of them was scripted to hold. The architecture, not the raw model, is what makes long-horizon believability possible. Foundational paper of the LLM agent-society lane and the direct ancestor of LLM-driven audience simulation.

## Core claims

- An LLM alone drifts and flattens over long horizons. Believability requires an agent architecture around the model: record everything, retrieve selectively, synthesize periodically, plan recursively.
- Memory is the load-bearing component. A natural-language memory stream plus a scoring function for what to surface beats stuffing context or fine-tuning a persona.
- Reflection turns logs into identity. Agents that periodically abstract higher-level inferences from raw observations answer questions about themselves more coherently and act more consistently.
- Social macro-behavior emerges from micro-architecture. With no diffusion mechanic coded, news of a mayoral candidacy spread from 1 agent (4 percent) to 8 (32 percent), and a Valentine's Day party invitation from 1 (4 percent) to 13 (52 percent), across two game days. Relationship network density rose from 0.167 to 0.74.
- Evaluation is by interview and ablation. Human judges rated interview responses; the full architecture beat every ablated version (no reflection, no planning, no observation memory) and beat a human-crowdworker roleplay baseline on believability.
- Known failure modes: retrieval misses, embellishment (agents confabulate detail), and overly formal, overly cooperative dialogue inherited from instruction tuning. Treat these as artifacts, never as findings.

## Frameworks and models

**Memory stream.** A time-stamped list of every observation in natural language. Nothing is discarded; salience is handled at retrieval, not at write time.

**Retrieval function.** For each candidate memory, score = alpha_recency * recency + alpha_importance * importance + alpha_relevance * relevance, with all three alphas set to 1 in the paper. Recency is an exponential decay over sandbox time with decay factor 0.995. Importance is a model-assigned poignancy rating on a 1 to 10 scale at write time. Relevance is embedding cosine similarity to the current query. Top-scoring memories fill the context window.

**Reflection.** When the sum of importance scores of recent events crosses a threshold (150 in the implementation, firing roughly two to three times per game day), the agent generates salient questions about its recent memories, answers them, and writes the answers back as new higher-level memories citing their evidence. Reflections can cite other reflections, building a tree from observation to self-concept.

**Recursive planning and reacting.** Each agent drafts a day plan in broad strokes, then recursively decomposes it into hour-scale chunks and then 5 to 15 minute actions. Incoming observations can trigger a reaction that replans the remainder of the day. Dialogue is generated conditioned on both agents' retrieved memories of each other.

**Believability evaluation.** Structured interviews probing five areas: self-knowledge, memory, plans, reactions, reflections. Responses ranked by human evaluators across conditions; ablations isolate each component's contribution.

## Decision rules

- If you are building an audience agent, then give it a memory stream and recency-importance-relevance retrieval; a static persona prompt will not hold a rule set stable across a long simulation.
- If a simulation runs past a few dozen interactions, then add reflection; without it agents lose coherence and the run measures drift, not culture.
- If you want a diffusion estimate from a sim, then seed exactly one agent and count who can recall the item unprompted at interview time; do not read message logs as adoption.
- If agent dialogue reads polite, agreeable, and formal, then discount it as an instruction-tuning artifact before reporting any consensus or sentiment finding.
- If you claim a simulated behavior is emergent, then run the ablation: remove the component and show the behavior disappears. Otherwise you scripted it.
- If validating a sim, then benchmark against a human-roleplay baseline, not against intuition; Park's crowdworker condition losing to the full architecture is the precedent.

## Key terms

- **Generative agent**: an LLM-driven agent wrapped in memory, retrieval, reflection, and planning to simulate believable human behavior.
- **Memory stream**: the append-only natural-language record of everything an agent experiences.
- **Retrieval function**: the recency, importance, relevance scoring that decides which memories enter context.
- **Reflection**: periodic synthesis of higher-level inferences from accumulated memories, triggered by an importance-sum threshold.
- **Recursive planning**: decomposing a day plan into progressively finer actions, replanned on reaction.
- **Believability**: the evaluation target, measured by interview coherence, not task success.
- **Smallville**: the 25-agent sandbox town where the emergent behaviors were observed.
- **Silicon sampling**: using model-generated respondents in place of human survey data; the adjacent method this paper legitimized.
