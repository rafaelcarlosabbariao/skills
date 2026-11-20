# Patterns: status-taste-markets shelf

Reusable techniques that emerge across the shelf. Each pattern: name, when to use, steps, source works. These are built strictly from what the chapters support; no imported frameworks.

## 1. Sibling-worlds check (cascade vs appeal)

**When to use:** any time a trend, sound, phrase, or aesthetic is surging and you are tempted to call it a real shift. This is the theory behind the standing rule to check sibling systems before claiming a corpus-wide move.

**Steps:**
1. Identify quasi-independent populations that could each have adopted the item: other platforms, other geos, other communities, other trend domains.
2. Check whether the item is rising in each of them, in the same run, alongside overall volume.
3. Convergence across independent surfaces signals appeal; movement in one world only signals a local cascade, which is expected behavior of influence markets, not noise.
4. Write the read naming the world the trend is local to. One world is a finding; all worlds is a shift.

**Source works:** MusicLab (Salganik, Dodds and Watts 2006); Diverse Local Trends (Epstein et al. 2021).

## 2. Leaderboard discount (MusicLab-style popularity read)

**When to use:** reading any chart, trending tab, ranked feed, or view-count race.

**Steps:**
1. Refuse the default reading that rank measures quality. Rank encodes frozen early accidents plus a quality bound.
2. Look for an independent-appeal proxy: performance in a context without visible popularity signals, or convergence across worlds (pattern 1).
3. Apply the floor and ceiling: bottom-decile appeal items, bet against regardless of early heat; top-decile items, bet against total failure. Refuse point predictions for the middle.
4. Never write "this won because it was best." Write condition-first: what the market's early history and display architecture did.

**Source works:** MusicLab; Diverse Local Trends.

## 3. Replicate-worlds simulation protocol

**When to use:** any agent-based audience simulation or forecast ensemble run.

**Steps:**
1. Expose social-signal strength (visibility and ordering of popularity information) as an explicit parameter, not a hidden assumption.
2. Run 8 or more replicate worlds per scenario: same agents, same content pool, different seeds.
3. Report the distribution of winners, the spread across worlds, and the floor/ceiling read on the material. The spread is the product, not a residual to shrink.
4. Where partial-homophily bridges between audience segments are dense, widen outcome variance and report divergent-subculture branches as legitimate scenario forks, not model error.

**Source works:** MusicLab; Diverse Local Trends; Wide Social Influence (Arvidsson, Hedstrom and Keuschnigg 2021).

## 4. Trend-region embedding comparison

**When to use:** comparing what two or more communities are actually into, or measuring whether a local trend is locking in.

**Steps:**
1. Embed the content items in a shared feature space (the Diverse Local Trends move: measure trend content directly, not ranked lists).
2. Within a community: track mean pairwise similarity of its popular items over time. Rising similarity means a local trend is locking in; forecast within that community and treat cross-community extrapolation as unsupported.
3. Across communities: compare popularity-weighted centroids over time, not item overlap. Two communities can share zero items and still share a trend region, or share items while diverging.

**Source works:** Diverse Local Trends.

## 5. Signal-salience audit

**When to use:** a platform changes its interface (adds or removes ranked feeds, visible counts, trending modules), or you need to compare taste dynamics across platforms.

**Steps:**
1. Score how visible popularity information is and how strongly it orders what users see. Availability and salience are separate levers.
2. High salience: expect more concentration (higher Gini) and more unpredictability together, not better sorting by quality. Discount leaderboard position as evidence of quality or durability.
3. Hidden or removed signals: expect flatter success distributions that track quality more closely, and more stable predictions.

**Source works:** MusicLab (grid vs ranked list); Diverse Local Trends (salience randomized separately).

## 6. Cycle-stage diagnosis

**When to use:** any emerging convention in fashion, music, food, or language; any "is this over?" question.

**Steps:**
1. Ask three questions: who originated it, who holds it now, has it crossed out of its originating tier.
2. Check the signaling-cost trajectory. Rising volume plus falling cost equals late cycle; mark cachet as depreciating no matter how loud current volume is.
3. If it has crossed into mass adoption, forecast elite abandonment and scan the originators, not the adopters, for the replacement.
4. Check for patina: novelty cachet with no accruing historical value classifies as a fad with a short half-life; patina separates classics.

**Source works:** Status and Culture (Marx 2022).

## 7. Disgust-boundary mapping

**When to use:** decoding an audience or scene; the first move of any audience rule-set build.

**Steps:**
1. Map what the group performs contempt for before mapping what it loves. Performed contempt locates a status economy more reliably than stated loves.
2. Treat the despised "mainstream" (or "the algorithm") as identity work: model the boundary drawing, not the described mainstream as a real segment.
3. Note what the scene feminizes in order to dismiss; that is usually the commercially larger market, and it predicts how taste and gender discourse braid.
4. When someone explains a taste as pure preference, ask which status strategy it serves before asking whether it is sincere.

**Source works:** Club Cultures (Thornton 1995); Status and Culture.

## 8. Media-tier tagging

**When to use:** every daily trend read; any signal about a scene arriving through coverage.

**Steps:**
1. Before scoring a signal, classify its carrier: micro-media (flyers, small accounts, group chats: assembles the crowd), niche media (music and style press: names and constructs the scene), mass media (tabloids, national coverage: condemns).
2. Apply the tier's effect. Mass condemnation is a growth signal: forecast hardened insider identity and recruitment, not decline. A friendly mainstream embrace forecasts capital flight and forking into new micro-scenes.
3. Date a scene's public life from the niche-media naming event, not from the practice's origin.

**Source works:** Club Cultures.

## 9. Inverted-U peer-similarity test

**When to use:** measuring influence in any dataset with taste profiles; building audience influence weights.

**Steps:**
1. Represent each person's taste as a vector (the Spotify test used topic-model distributions over listening).
2. Bin peers by taste similarity to the focal person.
3. Test where influence on adoption of novel items (outside the focal profile) peaks. Do not assume closest peers matter most; the shelf's finding is a peak at intermediate similarity.
4. In simulations, weight intermediate-similarity peers highest for novel adoption; estimate where the peak sits in your data rather than importing constants.

**Source works:** Wide Social Influence.

## 10. Bridge-population trace

**When to use:** a trend surfaces in a community with no visible preference basis there.

**Steps:**
1. Do not theorize a taste shift first. Look for adjacent, partially similar communities feeding the adoption.
2. Trace the bridge population the item traveled through before writing the read.
3. If two structurally similar scenes have diverged culturally, attribute to path-dependent influence first, not underlying preference differences, and say so explicitly.
4. Score a creator's crossover potential by the density of partially homophilous bridges between their audience segments.

**Source works:** Wide Social Influence; Diverse Local Trends.

## 11. Status-strategy segmentation

**When to use:** building audience rule sets; simulating how an audience reacts when a creator goes mass.

**Steps:**
1. Segment audience clusters by the taste strategy each runs: emulator (copying up), distinguisher, counter-signaler (secure, understated), professional-class rationalizer (best-reviewed, optimized), subcultural (inverted criteria), avant-garde negation.
2. Give each cluster a subcultural-capital variable, a disgust-boundary list, and a constructed mainstream-other.
3. Simulate abandonment cascades for the moment the creator's signal crosses tiers: agents defend capital when diffusion threatens it; counter-signalers exit first when the signal goes mass.

**Source works:** Status and Culture; Club Cultures.

## 12. Crossover-timing read

**When to use:** judging how close a scene or aesthetic is to mainstream crossover, for forecast leads.

**Steps:**
1. Watch for insiders policing sell-outs: that marks subcultural capital near peak valuation and crossover close. Expect early holders to exit into new undergrounds.
2. Watch for moral panic: mass condemnation certifies transgression and extends scene life; treat panic coverage as an input to growth, not a symptom of death.
3. Cross-check with cycle stage (pattern 6): saturation, not time, is the trigger for elite abandonment.
4. Use these as leading indicators in ensembles: sell-out policing and panic events time the crossover; shortening cycle length and nostalgia recycling are standing priors.

**Source works:** Club Cultures; Status and Culture.
