---
title: Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies
author: Gati Aher, Rosa I. Arriaga, Adam Tauman Kalai
year: 2023
kind: paper
theme: simulation
shelf: social-simulation
slug: llms-simulate-humans
---

# Using Large Language Models to Simulate Multiple Humans

## The claim

One language model can stand in for many different people, not one clever interlocutor. The paper replaces the Turing Test with the Turing Experiment: prompt the model as each of N named participants in a classic human subject study, aggregate, and check the distribution against the published human record. Three of four replications track humans; the fourth fails diagnostically, the model is too correct to be a crowd.

## Core claims

- A Turing Experiment (TE) evaluates distributional fidelity, not one-off impersonation. No judge, no deception game: run many simulated participants, compare aggregate curves to the human literature.
- Names are a cheap persona knob. Swapping first names and surnames varies gender and ethnicity across simulated participants, and known effects (gender differences in ultimatum play) reappear in the aggregate.
- Replication fidelity generally improves with model scale. Larger GPT-3 variants reproduce ultimatum-game rejection behavior, garden-path comprehension failures, and Milgram-style obedience patterns that smaller models miss.
- The critical failure is hyper-accuracy distortion: on wisdom-of-crowds estimation questions, the largest and most instruction-tuned models answer far more accurately than any human crowd, so the simulated distribution misrepresents people.
- Fidelity to human error is part of fidelity. A model aligned to be helpful and truthful is thereby a worse simulator of ordinary humans on knowledge tasks.
- Training-data contamination is a live confound when replicating famous studies. The authors construct novel garden-path sentences precisely so the model cannot recite memorized results.

## Frameworks and models

**Turing Experiment (TE).** Mechanics: a prompt template describing the study scenario with a participant-name placeholder; sample N names spanning gender and ethnicity; run one zero-shot completion per simulated participant; aggregate; compare against published human results. The unit of validation is the curve, not the individual transcript.

**The four TEs and their outcomes.**
- Ultimatum Game TE: simulated responders accept or reject splits of a fixed sum. Acceptance rises with offer fraction and low offers get rejected, matching the behavioral-economics record that people pay to punish unfairness.
- Garden Path TE: novel garden-path sentences (built to dodge memorization) versus controls. Larger models judge the garden-path items confusing the way human readers do.
- Milgram Shock TE: the obedience setup with the standard escalating shock ladder and experimenter prods. Simulated teachers largely comply, and disobedience clusters after the learner's protests, qualitatively matching Milgram's finding that about 65 percent of subjects went to the maximum.
- Wisdom of Crowds TE: numeric estimation questions. Here the simulation breaks: hyper-accuracy distortion. The simulated crowd's answers sit near the true value instead of spreading like human guesses.

**Distortion audit.** The durable contribution is the failure taxonomy: scale fixes social-behavior fidelity but alignment tuning injects hyper-accuracy, so every synthetic-panel claim needs a known-result replication check plus an error-realism check before any novel readout is trusted.

There is no parametric model. The operative parameters are N (simulated participants), name pool composition, the model-scale ladder, ultimatum offer fractions, and the 15-volt shock increments to 450 volts in the Milgram TE.

## Decision rules

- If a synthetic panel will be used on a novel question, then first make it replicate a known human result in the same task family. No replication, no trust.
- If a simulated crowd is more accurate or more uniform than any real crowd would plausibly be, then read hyper-accuracy distortion, not insight.
- If the scenario being simulated is famous, then assume contamination and build novel stimuli before crediting the match.
- If demographic variation is needed cheaply, then vary names, but validate the subgroup effect direction against human data before reporting it.
- If an aligned model refuses, moralizes, or corrects mid-simulation, then log it as an alignment artifact, a distortion class, not participant behavior.

## Key terms

- Turing Experiment (TE): validation design where a model simulates many named participants of a study and the aggregate is compared to human results.
- Hyper-accuracy distortion: simulated humans answering more correctly than real humans, an artifact of scale and instruction tuning.
- Silicon sampling: using model completions as stand-ins for human survey respondents.
- Name-based persona seeding: varying simulated demographics by inserting different names into the prompt template.
- Distributional fidelity: matching the spread and shape of human responses, not just the mean or a single plausible answer.
- Training-data contamination: the model reproducing a famous study's results from memory rather than simulating behavior.
- Garden-path sentence: a grammatical sentence that induces a predictable misparse, used to test human-like comprehension failure.
