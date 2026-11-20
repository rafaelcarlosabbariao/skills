---
title: Wide Social Influence and the Emergence of the Unexpected
author: Arvidsson, Hedström & Keuschnigg
year: 2021
kind: paper
theme: cultural-markets
shelf: status-taste-markets
slug: wide-social-influence
---

# Wide Social Influence and the Emergence of the Unexpected

Analytical sociology from the Linköping IAS group. Circulated from 2021; the peer-reviewed version, subtitled "An Empirical Test Using Spotify Data," appears in Sociological Science 12: 715-742.

## The claim

Social influence does not merely amplify what people already want. When influence is wide, flowing from peers who are similar enough to persuade but different enough to carry unfamiliar content, adoption decouples from preference, and collective outcomes emerge that no census of initial tastes could predict. The paper formalizes this mechanism and tests it on large-scale Spotify listening data.

## Core claims

- Homophily carries a built-in trade-off. Very similar peers are credible but redundant: they recommend what you would have found anyway. Very dissimilar peers carry novelty but lack persuasive force. Neither extreme produces surprise.
- Influence on novel adoption is non-monotonic in peer similarity: an inverted-U. The peak sits at intermediate similarity, the zone of partial homophily.
- Partial homophily is the generative zone of culture. It is where items jump preference neighborhoods, where adoption stops being a readout of prior taste, and where the unexpected enters.
- Decoupling scales up. Once choices stop mirroring preferences, aggregate popularity stops mirroring the preference distribution. Which item wins becomes structurally unpredictable, echoing Salganik-Dodds-Watts but locating the cause in network composition, not cumulative advantage alone.
- Divergent local subcultures follow. Populations with near-identical preference distributions can settle into different cultural equilibria because early adoption paths ran through different partially similar peers. Difference between scenes is not evidence of different tastes.
- The Spotify test operationalizes this: listening histories are compressed into preference profiles via topic modeling, influence is identified with statistical matching of comparable users, and adoption of music outside a user's prior profile is traced to partially similar peers.

## Frameworks and models

**The similarity-influence curve (wide social influence).** Represent each person's taste as a vector in preference space, in the empirical test a topic-model distribution over listened music. For a focal person and peer, compute similarity s in [0,1]. The probability that peer adoption converts into focal adoption of an item outside the focal profile is a function w(s): low at s near 0 (no persuasion), low at s near 1 (persuasion without novelty), maximal at intermediate s. There are no canonical fitted constants like Bass p and q; the working objects are the preference vectors, the similarity measure, and the inverted-U shape of w(s). What you estimate in a new dataset is where the peak sits.

**Preference-adoption decoupling.** Two ledgers per population: the preference distribution (what people would choose in isolation) and the adoption distribution (what they take up under influence). Narrow influence keeps the ledgers aligned and outcomes forecastable from surveys. Wide influence drives a wedge between them; the wedge, not noise, is where hits and subcultures come from.

**Distinguish from wide bridges.** Centola's wide bridges concern tie redundancy needed for complex contagion. Wide social influence concerns peer composition in taste space. A network can have wide bridges and still be narrow in this paper's sense if everyone in it likes the same things.

## Decision rules

- If a trend surfaces in a community with no visible preference basis there, then look for adjacent, partially similar communities feeding it. Trace the bridge population before theorizing a taste shift.
- If two structurally similar scenes diverge culturally, then do not hunt for underlying preference differences. Attribute to path-dependent influence first, and say so in the read.
- If a platform's recommender tightens exposure toward high-similarity peers and items, then expect fewer unexpected hits and consumption that mirrors stated preference. Watch for humans reintroducing surprise through group chats, curators, and scenes.
- If forecasting a cultural market, then forecast the distribution of outcomes, never the winner. Point predictions of hit identity are structurally unsound in wide-influence regimes.
- If measuring influence in any dataset, then bin peers by taste similarity and test for the inverted-U before assuming closest peers matter most.

## Key terms

- **Wide social influence**: influence arriving from a peer set that spans beyond one's own preference neighborhood.
- **Partial homophily**: peer similarity high enough to persuade, low enough to carry novelty; the generative zone.
- **Preference-adoption decoupling**: the gap between what a population would choose in isolation and what it adopts under influence.
- **Inverted-U influence curve**: influence on novel adoption peaking at intermediate peer similarity.
- **Divergent local subcultures**: different cultural equilibria in populations with near-identical preferences, produced by path-dependent influence.
- **Unpredictability paradox**: in influence-driven markets, winners between a quality floor and ceiling cannot be forecast from preferences or quality.
- **Wide bridges**: Centola's redundancy condition for complex contagion; related but distinct, about tie structure rather than taste composition.
