---
title: "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models"
author: "Bisbee, Clinton, Dorff, Kenkel, Larson"
year: 2024
kind: paper
theme: simulation
shelf: social-simulation
slug: synthetic-survey-data
---

# Synthetic Replacements for Human Survey Data

The skeptic's chapter on the shelf. In one line: LLM samples flatten variance and misrepresent minority opinion, required reading before trusting any synthetic panel.

## The claim

LLM personas can reproduce the average opinion of a population while failing at everything a survey is actually for. Bisbee and colleagues (Political Analysis, 32(4), 401-416) prompted ChatGPT to adopt personas built from real American National Election Study respondents and asked for 0-100 feeling thermometer scores toward 11 sociopolitical groups. The synthetic means tracked the 2016-2020 ANES closely, but the distributions were badly compressed, the regression structure was wrong, and the outputs shifted with prompt wording and model version. Matching the mean is not matching the population.

## Core claims

- Persona-prompted LLMs recover group-level averages of public opinion with surprising accuracy. This is the seductive result that makes synthetic panels look viable.
- Synthetic responses have far less variance than real respondents. The model gives the modal answer for a demographic profile, not a draw from the real distribution of people with that profile.
- Regression coefficients estimated on synthetic data frequently differ significantly from the same models run on ANES data, and standard errors are much too small. Synthetic panels produce confident, wrong inference about who believes what and why.
- Variance compression hits minorities and atypical members of groups hardest. The model erases the conservative Black voter and the pro-union Republican, exactly the people whose existence changes a cultural read.
- Outputs are unstable across prompt phrasings and across model updates. The same persona asked the same question months apart returns different answers, so results are not reproducible and drift with the vendor's release cycle.
- Net position, written against the optimism of Argyle et al.'s silicon sampling: synthetic samples cannot replace human survey data for inference. They are at best a hypothesis-generation and piloting tool.

## Frameworks and models

**Silicon sampling (the method under test).** Take real respondent covariates (age, gender, race, education, partisanship, ideology, and similar), concatenate them into a first-person persona prompt, query the LLM for the survey item, and treat the completions as a synthetic panel. Argyle et al. (2023) called the match to human data "algorithmic fidelity." This paper is the stress test of that idea.

**The three-moment audit.** The paper's durable contribution is an evaluation framework: judge a synthetic panel on three levels, in order of increasing difficulty. (1) First moment: do synthetic means match real means? Usually yes. (2) Second moment: does synthetic variance match real variance? No, standard deviations shrink sharply. (3) Covariance structure: do regressions of opinion on demographics recover the real coefficients with honest uncertainty? No, coefficients move and intervals collapse. A panel that only passes level 1 is a caricature, not a sample.

**The stability tests.** Two robustness probes: perturb the prompt wording and hold everything else fixed, and rerun the identical pipeline on a later model version. Both moved the results significantly. Any synthetic-panel claim therefore needs a pinned model version and a prompt-sensitivity check, or it is not a finding.

## Decision rules

- If a synthetic panel or simulated audience is pitched on how well its averages match real data, then demand the variance and the subgroup breakdowns before believing anything downstream.
- If you run regressions or segment comparisons on LLM-generated respondents, then treat the standard errors as fiction and refuse to report significance from them.
- If a simulated audience is unanimous or near-unanimous, then read that as model artifact, not consensus. Real crowds always carry more disagreement than the model returns.
- If a claim rests on minority or cross-pressured segments (the atypical member of a demographic), then require human data. That is precisely where synthetic respondents fail.
- If you must use synthetic respondents, then pin the model version, log the prompts, rerun under paraphrase, and label the output as pilot or hypothesis, never as measurement.

## Key terms

- **Silicon sampling**: using persona-prompted LLMs as stand-ins for human survey respondents.
- **Algorithmic fidelity**: Argyle et al.'s claim that LLMs conditioned on personas mirror human response distributions; the claim this paper undercuts.
- **Feeling thermometer**: 0-100 survey scale of warmth toward a group; the paper's outcome measure across 11 sociopolitical groups.
- **Variance compression**: synthetic responses clustering near the modal answer, understating real population spread.
- **Persona prompt**: first-person prompt built from a real respondent's covariates to condition the model.
- **Temporal instability**: the same prompt returning different results after a model update, breaking reproducibility.
- **ANES**: American National Election Study, the human benchmark (2016-2020 waves here).
