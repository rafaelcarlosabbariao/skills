# Cheatsheet: diffusion-contagion shelf

Decision tables and quick rules. Open this first under time pressure; each row points to the chapter or pattern with the full mechanics.

## Master fork: what kind of spread is this

| Situation | Which model applies | What to check first |
|---|---|---|
| The thing spreads on one exposure (a link, a meme, news, a term) | Simple contagion: weak ties + small worlds (strength-of-weak-ties, small-world-networks) | Are there bridges out of the origin cluster? If yes, forecast in days |
| Adoption costs something: money, effort, identity risk, sanction | Complex contagion, T >= 2 (complex-contagions) | Bridge width between clusters, not path length or follower counts |
| You have an adoption time series and need a peak call | Bass model (bass-new-product-growth) | Curve shape: inflection present (q-driven) or deceleration from day one (p-driven) |
| You need to know who carries the trend and who adopts next | Adopter categories + five attributes (diffusion-of-innovations) | Which category the visible discussants belong to; media vs peer channel mix |
| Someone credits a cascade to an influencer or tastemaker | Threshold cascade model (influentials-watts-dodds) | The susceptibility side: thresholds, connectivity, cascade window. Seed identity is narrative until checked |
| A behavior clusters in a scene and looks like it is spreading | Three-explanation test (connected) | Whose change came first; do one-way ties show the effect too (homophily flag) |
| A message reaches people but nobody acts | Stickiness Factor (tipping-point) | Message structure and action cost, before buying reach |
| Behavior shifted with no new message | Power of Context (tipping-point) | Environment cues, defaults, group size (Rule of 150) |

## Curve diagnostics

| Observation | Reading | Rule |
|---|---|---|
| Slow trickle, then acceleration, then inflection | q > p: word of mouth is doing the work | Fit the curve; forecast the peak at t* = ln(q/p)/(p+q); do not extrapolate the ramp |
| Decelerating from day one, no inflection | p-driven: media or algorithm push | Expect decay, not a mainstream wave; do not spend on reach it already has |
| Penetration approaching half the plausible pool | Peak velocity is now (peak lands just under half of m) | Call the top while others draw straight lines through the ramp |
| Metric declining after a peak | Possibly pool exhaustion, not death | Check m before writing an obituary; finite pools always decline |
| Adoption crossed 10 to 20 percent of the relevant population | Take-off: interpersonal networks activated | Treat growth as self-sustaining; shift to ceiling and consequences |
| Interactive behavior stalled below critical mass | Pre-critical-mass failure mode | Predict abandonment, not slow growth |
| Repeated behavior (slang use, posting style, listening) | Bass covers only the first-adoption layer | Model repetition separately |

## Crossover: will it jump scenes

| Situation | Which lens | First check |
|---|---|---|
| Trend saturates one community, stalls corpus-wide | Wide bridges (complex-contagions) | Any cluster of people embedded in both sides? Thin press or celebrity ties give awareness without adoption |
| Same term in two unconnected scenes within a day | Shortcut transmission (small-world-networks) | Find the bridging account before writing a zeitgeist story; it is one shortcut event, not two domain moves |
| Term circulating only inside one tight cluster | Redundant chatter (strength-of-weak-ties) | Log it; start the clock only when it surfaces in a structurally distant cluster |
| A scene looks sealed and insulated | Small-world regime | Do not forecast containment; containment fails at very low rewiring |
| Costly norm spreading fast through a sparse broadcast network | Suspicion rule (complex-contagions) | Either it is actually cheap to adopt, or the spread is astroturfed |
| Trend jumps subcultures fast and intact vs deepening in one scene | Connector vs maven signature (tipping-point) | Bridges for jumps, information specialists for deepening |

## Seeding decisions

| Goal | Strategy | Source |
|---|---|---|
| Spread awareness of something cheap to adopt | Buy bridges: seed accounts embedded in multiple scenes | strength-of-weak-ties |
| Spread adoption of something costly | Concentrate seeds in one neighborhood to cross local thresholds; do not scatter for reach | complex-contagions |
| One big influencer vs many small accounts | Default to many seeds (big-seed) unless the network sits near the sparse edge of the cascade window | influentials-watts-dodds |
| Choosing individual seeds | Centrality and mutual ties, not audience size; mutual ties carry about 3x one-way influence | connected |
| Forecasting per-seed reach | Cap organic spread at about three degrees; plan re-seeding, not momentum | connected |
| Accelerating a q-driven wave | Seed connected adopters; media money is wasted on an imitation wave | bass-new-product-growth |
| Working through institutions | Change agents succeed through opinion leaders, not around them | diffusion-of-innovations |

## Anti-narrative rules (apply before publishing any read)

| Claim on the table | Required check |
|---|---|
| "X made it blow up" | Was the population primed: thresholds low, connectivity in-window? Influencer credit is post-hoc narrative until the susceptibility side is checked |
| "X is spreading through the scene" | Three-explanation test: contagion vs homophily vs shared environment; longitudinal ordering and tie directionality |
| "X is everywhere suddenly" | One seed at degree two, or many independent seeds? Plus the sibling-system and volume check before calling anything corpus-wide |
| "These two trends were identical, one won" | Expect structural variance, not content explanations; identical systems produce duds and wildfires |
| "This scene will keep it contained" | Two shortcuts from anything; containment fails at low p |
| "It went viral here, so the behavior will follow" | Awareness and behavior obey different physics; classify simple vs complex first |
| "The algorithm proves people love it" | p vs q decomposition: algorithmic push is external influence; only a real q term is people choosing it |

## Pressure-system quick map

| System | Shelf read |
|---|---|
| slop | AI slop floods are p-shaped by construction: pure external supply. A slop wave that develops a real q term has crossed into culture. Visible low-grade slop licenses more (Broken Windows) |
| lonely | Loneliness spreads to three degrees and pushes carriers to the network edge, a self-reinforcing spiral; the loneliness economy is largely a weak-tie deficit. High C with short L is the shape of connected-but-lonely |
| taste | p vs q is the cleanest algorithm-vs-taste operationalization. Feeds are rewiring machines and impersonate weak ties while serving in-cluster redundancy; when the algorithm simulates peer persuasion, apparent q is inflated |
| values, gender | Positions carrying sanction are complex contagions: they harden in reinforcing enclaves before moving globally. Camps are high C, two hops apart: cross-camp outrage transmits instantly with zero persuasion |

## Quick numbers

| Number | Meaning | Source |
|---|---|---|
| p about 0.01 to 0.03, q about 0.3 to 0.5 | Typical Bass fits for durables (meta-analytic averages near p 0.03, q 0.38) | bass-new-product-growth |
| t* = ln(q/p)/(p+q) | Peak time of new adoptions | bass-new-product-growth |
| Just under half of m | Penetration at peak velocity, F* = 1/2 - p/(2q) | bass-new-product-growth |
| 10 to 20 percent | Adoption level at take-off | diffusion-of-innovations |
| 2.5 / 13.5 / 34 / 34 / 16 | Adopter category shares in percent | diffusion-of-innovations |
| 49 to 87 percent | Adoption-rate variance explained by the five perceived attributes | diffusion-of-innovations |
| T = 1 vs T >= 2 | Simple vs complex contagion; 2 is enough to flip every headline small-world result | complex-contagions |
| Bridge width >= T | Condition for a complex contagion to cross clusters | complex-contagions |
| k <= 1/phi | Vulnerable-node condition; cascades need these to percolate | influentials-watts-dodds |
| 3 degrees | Default organic influence horizon | connected |
| 0.57 / 0.20 / 0.10 | Per-hop influence decay starting schedule (obesity magnitudes) | connected |
| about 3x | Mutual-tie influence vs one-way tie | connected |
| 16.7 / 55.6 / 27.8 percent | Job leads via contacts seen often / occasionally / rarely | strength-of-weak-ties |
| 150 | Group size cap for self-enforcing norms | tipping-point |
