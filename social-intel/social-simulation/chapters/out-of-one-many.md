---
title: "Out of One, Many: Using Language Models to Simulate Human Samples"
author: "Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, David Wingate"
year: 2023
kind: paper
theme: simulation
shelf: social-simulation
slug: out-of-one-many
---

# Out of One, Many (Argyle et al., 2023)

## The claim

A large language model's biases are not one monolithic distortion. They are fine-grained and demographically correlated, so if you condition the model on a rich first-person backstory built from a real person's covariates, it will emulate the response distribution of that person's subgroup. The paper names this property algorithmic fidelity and shows GPT-3 passing hard empirical tests of it against American National Election Studies (ANES) data.

## Core claims

- Silicon sampling works: feed the model a demographic backstory, sample completions, and the output distribution tracks the matching human subgroup, not a generic average human.
- Fidelity is measurable. The paper defines four criteria (below) and insists fidelity be demonstrated per task and per domain, never assumed.
- Study 1: GPT-3 conditioned as partisans produced word lists describing the other party that human raters could not reliably distinguish from lists written by real partisans.
- Study 2: conditioned on ANES respondents' covariate profiles, GPT-3's reported vote matched actual reported vote with tetrachoric correlations of 0.90 (2012), 0.92 (2016), and 0.94 (2020).
- The known failure case: pure independents, especially in 2020. Subgroups with weak identity anchors give the model too little to condition on.
- Study 3: the model reproduces the pattern of correlations among attitude items, not just marginal frequencies. Structure, not just averages.
- Bias becomes a feature: because the distortions are demographically patterned, proper conditioning turns them into signal about subpopulations.

## Frameworks and models

**Silicon sampling.** Build a first-person conditioning template from a real respondent's covariates (party ID, ideology, race, gender, age, religiosity, political interest, and so on), one silicon individual per real individual. Prompt the model to complete the survey response, sample many completions, and read the resulting distribution as a synthetic subgroup sample. No fine-tuning, only conditioning.

**Algorithmic fidelity, four criteria.** 1) Social Science Turing Test: humans cannot distinguish generated responses from human ones. 2) Backward Continuity: a reader can recover the persona's attitudes and demographics from the output. 3) Forward Continuity: responses proceed naturally from the conditioning context. 4) Pattern Correspondence: generated data reproduces the relationships among ideas, demographics, and behavior found in human data. All four are audits you run, not properties you assume.

**Key parameters.** Model: GPT-3 davinci, 175B parameters. Benchmark: ANES 2012, 2016, 2020. Vote-choice tetrachoric correlations: 0.90, 0.92, 0.94. Distributions come from repeated sampling per persona, never a single completion.

## Decision rules

- If you need a fast read on how a defined audience would respond to a message, then run a silicon panel first: full covariate backstories, many samples per persona, read distributions.
- If a segment has weak or crosscutting identity anchors (the pure-independent case), then downgrade confidence in the silicon read and require human confirmation.
- If you are about to trust synthetic respondents in a new domain, then run the four-criteria audit against a slice of real data from that domain before shipping anything.
- If synthetic marginals look right, then still check pattern correspondence: matching averages with broken inter-item structure is a failed simulation.
- If the phenomenon post-dates the model's training data, then do not expect fidelity from conditioning alone; inject current context (live signal) into the prompt.
- If someone hands you "what Gen Z thinks" from one prompt and one completion, then reject it: no persona depth, no distribution, no audit.

## Key terms

- Silicon sampling: conditioning a language model on demographic backstories so its outputs stand in for human survey respondents.
- Algorithmic fidelity: the degree to which the model's internal associations among ideas, attitudes, and contexts mirror those of specific human subpopulations.
- Silicon individual: one synthetic respondent built from one real respondent's covariate profile.
- Social Science Turing Test: generated responses that human judges cannot distinguish from human ones.
- Pattern correspondence: synthetic data reproducing the correlational structure among variables, not just their marginals.
- Tetrachoric correlation: correlation between two binary variables assuming latent continuous traits; the paper's vote-match metric.
- Conditioning: steering model output through prompt context alone, with no parameter updates.
