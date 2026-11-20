---
title: A New Product Growth Model for Consumer Durables
author: Frank M. Bass
year: 1969
kind: paper
theme: diffusion
shelf: diffusion-contagion
slug: bass-new-product-growth
---

# A New Product Growth Model for Consumer Durables

Published in Management Science, January 1969, under a typesetter's scrambled title ("A New Product Growth for Model Consumer Durables") that stuck to one of the most cited papers in marketing science. In one line: the mathematical S-curve, innovation (p) and imitation (q) coefficients, fit it in code.

## The claim

Adoption of a new durable is driven by two forces that can be separated mathematically: external influence (media, advertising, anything that reaches people independent of other adopters) and internal influence (imitation, word of mouth, social pressure from prior adopters). One two-parameter hazard function captures both, reproduces the empirical S-curve of every major consumer durable, and, fitted to early data, forecasts the timing and height of the sales peak.

## Core claims

- The probability that a non-adopter adopts at time t is a linear function of how many people have already adopted: pressure to adopt grows with cumulative adoption.
- Two coefficients decompose any adoption wave: p, the coefficient of innovation (external push), and q, the coefficient of imitation (social pull). They are estimable from sales data alone.
- If q > p, the curve is an S: slow start, acceleration, inflection, peak, decline. If q <= p, there is no inflection; adoption starts at its maximum and decays. The shape of early growth is diagnostic of the mechanism.
- The market potential m is finite. Decline after the peak is arithmetic, not failure: the pool of never-adopters is running out.
- Fitted to annual first-purchase data for eleven consumer durables (refrigerators, freezers, TVs, room air conditioners, clothes dryers, and others), the model fit closely and, most famously, called the late-1960s peak in color television sales while industry projections still pointed up. Bass was right.
- The model covers first purchases only. Repeat buying and replacement are out of scope.

## Frameworks and models

**The Bass model.** Let F(t) be the cumulative fraction of eventual adopters who have adopted by t, and f(t) its density. The core assumption is the hazard:

    f(t) / (1 - F(t)) = p + q F(t)

With market potential m and cumulative adopters Y(t) = m F(t), adoptions per period are:

    S(t) = p m + (q - p) Y(t) - (q / m) Y(t)^2

Closed form:

    F(t) = (1 - e^(-(p+q)t)) / (1 + (q/p) e^(-(p+q)t))

Peak of the noncumulative curve arrives at t* = ln(q/p) / (p + q), with height m (p + q)^2 / (4q), reached when penetration hits F* = 1/2 - p/(2q), always just under half of potential. Typical fitted magnitudes for durables: p around 0.01 to 0.03, q around 0.3 to 0.5 (later meta-analyses average p near 0.03, q near 0.38).

**Estimation from data.** Regress period adoptions S on cumulative Y and Y^2: S = a + bY + cY^2. Then m is the positive root of c m^2 + b m + a = 0, p = a/m, q = -c m. Three regression coefficients recover all three structural parameters. In code: OLS on the quadratic, or nonlinear least squares on the closed form when data is noisy.

**Position in the shelf.** Bass is the aggregate, differential-equation face of what Rogers describes verbally (adopter categories) and what Granovetter-style threshold models describe at the individual level. p-driven adoption is simple external exposure; q-driven adoption is the aggregate shadow of peer thresholds.

## Decision rules

- If a trend's early growth decelerates from day one, with no inflection, then it is p-driven: a media or algorithm push. Expect decay, not a mainstream wave.
- If growth accelerates after a slow trickle, then q dominates: word of mouth is doing the work. Fit the curve and forecast the peak instead of extrapolating the ramp.
- If penetration of the plausible pool is approaching half, then you are near peak velocity: call the top while everyone else draws straight lines through the ramp.
- If a metric declines after its peak, then check m before declaring death: finite pools always produce declines.
- If you want to accelerate a q-driven trend, seed connected adopters; if p-driven, buy reach. Do not spend media money on an imitation-driven wave.
- If the behavior is repeated (posting styles, slang use, listening), then Bass covers only the first-adoption layer; model repetition separately.

## Key terms

- **Coefficient of innovation (p):** per-period adoption probability from external influence alone; the intercept of the hazard.
- **Coefficient of imitation (q):** strength of social influence; how much each prior adopter raises the hazard for the rest.
- **Market potential (m):** the finite pool of eventual adopters; everything saturates against it.
- **Hazard rate:** probability of adopting now given you have not yet; Bass makes it linear in cumulative adoption.
- **S-curve:** the cumulative adoption shape produced whenever q > p.
- **Peak time t*:** ln(q/p) / (p + q); when new adoptions top out.
- **First purchase:** the only event the model counts; replacement and repeat buying are excluded.
