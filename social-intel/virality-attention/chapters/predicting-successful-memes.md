---
title: "Predicting Successful Memes Using Network and Community Structure"
author: "Lilian Weng, Filippo Menczer, Yong-Yeol Ahn"
year: 2014
kind: paper
theme: virality
shelf: virality-attention
slug: predicting-successful-memes
---

# Predicting Successful Memes Using Network and Community Structure

ICWSM 2014, pp. 535-544; companion study in Scientific Reports, 2013. In one line: meme virality is predictable from network and community structure, not content quality; community concentration signals fizzle vs spread.

## The claim

The future popularity of a meme is predictable from the structure of its earliest spread, not from its content. First adopters concentrated inside one community mean the meme is held there by social reinforcement and will likely fizzle. Early adoption that already crosses many communities marks a genuine viral candidate, even when raw counts are small.

## Core claims

- Memes (operationalized as new Twitter hashtags on a reciprocal-follow network of hundreds of thousands of users) compete for finite collective attention; most die, a few dominate, and structure decides which.
- Community concentration of early adopters is the strongest predictor of final popularity. The more communities a meme permeates early, the more viral it becomes.
- Early popularity is a poor predictor of future popularity. Raw early volume misleads; where the volume sits in the network is what carries signal.
- Viral memes spread like simple contagion, crossing community boundaries on single exposures, like a disease. Niche memes spread like complex contagion, needing repeated reinforcement, which traps them inside dense communities.
- A machine learning model (random forests) fed community-structure features from only the first ~50 tweets of a hashtag identifies future top-percentile memes far better than content-based or early-popularity baselines. Community features alone perform nearly as well as the full feature set.

## Frameworks and models

**Community concentration measures.** Detect communities on the follower graph (the authors use Infomap; the finding is robust to the detection method), then score a meme's first N adopters (N around 50) on three quantities: (1) the number of infected communities, the count of distinct communities among early adopters; (2) usage entropy, H = -sum over communities c of p(c) log p(c), where p(c) is the fraction of early tweets or adopters in community c, so low entropy means concentrated and high entropy means dispersed; (3) the fraction of intra-community interactions, the share of early adoption edges (retweets, mentions, follows) that stay inside a community rather than bridging out.

**Simple vs complex contagion as a diagnostic.** Complex contagion (Centola and Macy) requires multiple reinforcing exposures, and dense within-community ties supply exactly that, so reinforcement-dependent memes get structurally trapped. Simple contagion needs one exposure, so it leaks across weak ties between communities. The paper turns this theory into a measurement: a meme's early community footprint reveals which regime it is in, and therefore its ceiling.

**Prediction pipeline.** Task: after observing the first ~50 tweets of a new hashtag, classify whether its final popularity lands in a top percentile bracket (for example top 5% or 10% of all memes). Features come in three groups: influence of early adopters (follower counts, activity), community concentration (the three measures above), and adoption time-series shape (growth rate, inter-adoption timing). Classifier: random forests. Community features dominate.

## Decision rules

- If a rising trend's early adopters sit in one community, then call it niche and expect a fizzle, no matter how loud that community is.
- If early adoption spans several structurally distant communities, then flag a viral candidate even while absolute volume is still small.
- If ranking candidate trends, then weight community dispersion over early counts; never headline on early volume alone.
- If a behavior is identity-heavy or costly (adoption needs social cover), then treat it as complex contagion: expect it to stay community-bound and discount extrapolations to the mainstream.
- If you can only afford one metric, then compute adopter entropy across communities, not adopter totals.

## Key terms

- meme: a unit of transmissible culture; operationalized here as a new hashtag.
- community concentration: the degree to which a meme's early adopters cluster inside few network communities.
- usage entropy: Shannon entropy of a meme's early adoption across communities; high entropy signals viral potential.
- infected communities: the count of distinct communities containing at least one early adopter.
- simple contagion: spread requiring a single exposure; crosses community boundaries easily.
- complex contagion: spread requiring reinforcement from multiple contacts; gets trapped in dense communities.
- structural trapping: the confinement of a reinforcement-dependent meme inside the community that incubated it.
- limited attention economy: the regime where ideas exceed cognitive bandwidth, so attention scarcity, not idea supply, determines survival.
