---
title: The Spread of True and False News Online
author: Vosoughi, Roy & Aral
year: 2018
kind: paper
theme: virality
shelf: virality-attention
slug: true-false-news
---

# The Spread of True and False News Online

## The claim

Falsehood diffuses significantly farther, faster, deeper, and more broadly than truth, and the gap is widest for political news. The engine is novelty: false claims are measurably more novel than true ones relative to what a user has recently seen, and novelty wins attention and sharing. Humans, not bots, produce the differential.

## Core claims

- Across roughly 126,000 verified rumor cascades on Twitter (2006 to 2017, about 3 million people, 4.5 million tweets), false news beat true news on every diffusion metric: depth, size, breadth, and structural virality.
- The top 1 percent of false cascades routinely reached 1,000 to 100,000 people; true cascades rarely reached more than 1,000. Truth took about six times as long as falsehood to reach 1,500 people and about twenty times as long to reach cascade depth 10.
- Falsehood was 70 percent more likely to be retweeted than truth (odds ratio 1.7), after controlling for follower count, followees, account age, activity, and verification.
- The spreaders of false news had fewer followers, followed fewer people, were less active, less often verified, and newer to the platform. Falsehood spread despite its carriers, not because of them.
- False news was more novel than true news against each user's prior 60 days of exposure, and novelty predicted sharing. Replies to false news carried more surprise and disgust; replies to truth carried more sadness, anticipation, joy, and trust.
- Removing bot traffic (bot-detection filtering) did not change any conclusion. Bots accelerated true and false news at roughly the same rate.
- Political false news traveled fastest and deepest of all categories, ahead of terrorism, disasters, science, urban legends, and finance.

## Frameworks and models

**Cascade anatomy.** A rumor cascade is one origin tweet plus its unbroken retweet chain. Four measurements: depth (retweet hops from origin), size (unique users), maximum breadth (most users at any single depth), and structural virality (mean shortest-path distance between all node pairs, from Goel, Anderson, Hofman, and Watts). Low structural virality means one broadcast hub; high means true peer-to-peer diffusion. False cascades scored higher on all four. Use these, never raw view counts, when judging whether something actually spread.

**Ground truth by fact-checker consensus.** Veracity came from six independent fact-checking organizations agreeing 95 to 98 percent of the time, with a hand-coded robustness sample. The design pattern: define truth exogenously, then measure diffusion, never the reverse.

**The novelty hypothesis.** For each retweet decision, compare the tweet's topic distribution (latent Dirichlet allocation) to what that user saw in the prior 60 days, using three distances: information uniqueness, KL divergence, Bhattacharyya distance. False rumors scored higher on all three, and users preferentially shared what scored novel. Novelty earns attention in a limited-attention economy and confers insider status on the sharer.

**Emotional signature.** Reply text scored against the NRC emotion lexicon. Falsehood's profile is surprise plus disgust; truth's is sadness, anticipation, joy, trust. This refines the high-arousal virality account (Berger): the arousal that powers falsehood is specifically novelty-linked surprise.

**The 70 percent edge.** Logistic regression on retweet probability with user covariates held fixed gives falsehood a 1.7 odds ratio. That is the single most portable parameter in the paper: a fixed multiplier on transmission probability for novel-surprising claims.

## Decision rules

- If a claim is moving unusually fast and deep, treat velocity as a falsehood risk flag, not as evidence of importance. Verify before it enters a reading.
- If reply sentiment runs surprise plus disgust, raise the false-claim prior. If it runs sadness, trust, anticipation, or joy, lower it.
- If the accounts spreading a story are small, new, and unverified, do not discount the cascade. Weak carriers are the normal profile of a false cascade.
- If someone blames bots for a spread differential, demand the human-only rerun. Expect bots to explain volume, not the true-false gap.
- If the content is political or culture-war shaped, apply the largest falsehood premium.
- If measuring spread, report depth, breadth, and structural virality, never a single count.
- If forecasting whether a claim will travel, score its novelty against the target audience's recent exposure baseline, not against your own.

## Key terms

- **Rumor cascade**: one origin assertion plus its unbroken retweet chain; the unit of diffusion analysis.
- **Structural virality**: mean distance between all node pairs in a cascade; separates broadcast from person-to-person spread.
- **Cascade depth**: number of retweet hops from the origin tweet.
- **Novelty (information uniqueness)**: distance between a tweet's topic mix and the sharer's prior 60-day exposure.
- **Odds ratio 1.7**: falsehood's 70 percent retweet advantage over truth with user covariates controlled.
- **Bot null result**: removing automated accounts leaves the true-false gap intact; humans drive the differential.
- **Emotional signature**: the reply-emotion profile of a claim; surprise-disgust for false, sadness-trust for true.
