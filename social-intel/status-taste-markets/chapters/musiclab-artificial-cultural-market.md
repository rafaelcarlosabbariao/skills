---
title: "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market"
author: "Matthew J. Salganik, Peter Sheridan Dodds, Duncan J. Watts"
year: 2006
kind: paper
theme: cultural-markets
shelf: status-taste-markets
slug: musiclab-artificial-cultural-market
---

# MusicLab: the artificial cultural market

## The claim

Social influence, not quality, decides winners in cultural markets. In a controlled web experiment (Science, 2006), showing people what others downloaded made hit distributions more unequal and, at the same time, less predictable: the same 48 songs produced different winners in parallel worlds that started identically. Quality only sets a floor and a ceiling; between them, history is an accident that compounds.

## Core claims

- 14,341 participants listened to 48 songs by unknown bands and chose downloads either independently (no popularity info) or inside one of 8 social influence "worlds" showing download counts.
- Social influence increased inequality of success: download share concentrated on fewer songs, with the Gini coefficient roughly doubling under strong influence (0.45+ in the ranked-list condition, per the paper's figure).
- Social influence increased unpredictability: the same song landed at very different ranks across the 8 worlds. The canonical case: "Lockdown" by 52metro was 26th on appeal, finished 1st in one world and 40th in another.
- Strength of the signal matters. Experiment 1 showed counts beside a random grid; Experiment 2 sorted the list by downloads. The ranked list produced more inequality and more unpredictability than the grid.
- Quality is a bound, not a driver: the best songs (by independent-condition appeal) rarely failed and the worst rarely won, but everything in the middle could go anywhere.
- Consequence: expert prediction of specific hits fails structurally. No information about the songs recovers what depends on the market's own early history.

## Frameworks and models

**Parallel worlds design.** Randomize an incoming population into one independent world plus k identical influence worlds (here k = 8). Each world evolves on its own history; cross-world divergence isolates social influence from the object itself. The template for any counterfactual read of a hit.

**Cumulative advantage (Matthew effect).** Early, essentially random download differences get amplified because people preferentially sample what is already popular. Success breeds success. The tunable parameter is signal strength: how visible and how ordered the popularity information is. Ranked feeds are the high-signal condition.

**The two measures.** Inequality: Gini coefficient G over songs' market shares m_i (share of all downloads in a world). Unpredictability: u_i, the average absolute difference in a song's market share across all pairs of worlds, averaged over songs. Social influence pushed both up together, which is the paper's punchline: markets can be simultaneously more winner-take-all and less forecastable.

**Quality floor and ceiling.** Appeal = a song's market share in the independent condition. Appeal correlates with success only at the extremes. Practically: quality screens out losers, it does not pick winners.

**Self-fulfilling prophecy (follow-up, Salganik and Watts 2008).** Inverting the displayed rankings mid-market made false hits partly stick; the best songs slowly recovered. Perceived popularity is itself a causal force, but quality reasserts at the extremes over time.

## Decision rules

- If a hit is running away with a market, do not read its rank as a quality measurement. Rank encodes frozen early accidents plus a quality bound.
- If you must forecast, forecast the distribution, not the winner: level of inequality, share of the top slot, spread of plausible winners. Never a single name with confidence.
- If a platform makes popularity more visible or sorts by it (ranked feeds, trending tabs, view counts), expect more concentration and less predictability, not better sorting by quality.
- If you can observe the same object across quasi-independent populations (platforms, geos, subcultures), treat them as parallel worlds: convergence across worlds signals appeal, divergence signals cascade.
- If something is bottom-decile on independent appeal, bet against it regardless of early heat; if top-decile, bet against total failure. Refuse point predictions for the middle.

## Key terms

- **MusicLab:** the web-based experimental platform behind the study.
- **Independent condition:** participants choose with no popularity information; yields the appeal baseline.
- **Social influence world:** one of 8 identical markets whose participants see that world's download counts.
- **Appeal:** a song's market share in the independent condition; the quality proxy.
- **Market share (m_i):** fraction of a world's total downloads going to song i.
- **Gini coefficient (G):** inequality of market shares within a world.
- **Unpredictability (u_i):** average pairwise difference in a song's market share across worlds.
- **Cumulative advantage:** popularity feeding on itself, decoupling outcomes from intrinsic quality.
- **Quality floor and ceiling:** the bounds appeal places on outcomes; everything between is path-dependent.
