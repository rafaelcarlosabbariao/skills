#!/usr/bin/env python3
"""Writes the storytelling repertoire as diagrams: one overview (the reader's four questions) and one detail per
family (job -> how to tell and show it). Usage: python3 this.py <out.html>"""
import sys, html

INK, MUTED, SOFT, PAPER, PAPER2, RULE = "#1a1813", "#6e6759", "#6a5f52", "#f2eee4", "#e5dfd1", "#ded8c9"
ACC, TINT = "#2f6b5b", "#dfe7e2"
SANS = "Geist, 'Helvetica Neue', system-ui, sans-serif"
MONO = "'JetBrains Mono', Menlo, monospace"
e = html.escape

def t(x, y, s, size=12, fill=INK, weight=None, fam=SANS, anchor=None, ls=None):
    a = f' font-weight="{weight}"' if weight else ""
    a += f' text-anchor="{anchor}"' if anchor else ""
    a += f' letter-spacing="{ls}"' if ls else ""
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="{fam}"{a}>{e(s)}</text>'

def defs(p):
    return (f'<defs><marker id="{p}-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
            f'<polygon points="0 0, 8 3, 0 6" fill="{MUTED}"/></marker></defs>')

def svg(slug, w, h, title, desc, body):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-labelledby="{slug}-title {slug}-desc"><title id="{slug}-title">{e(title)}</title>'
            f'<desc id="{slug}-desc">{e(desc)}</desc>{defs(slug)}<rect width="100%" height="100%" fill="{PAPER}"/>'
            + "".join(body) + "</svg>")

SPINE = {1: "cover", 2: "precedent", 3: "method", 4: "what we saw", 5: "limits", 6: "scaffold"}

FAMILIES = [
    ("size", "SIZE", "How big is it?", [
        ("Scale or magnitude", [1, 4], "A concrete unit (Heath 2007)", "Unit chart or icon array; scroll at true scale",
         "Korostoff, 1-pixel wealth", "A big number in no familiar unit; area or radius exaggeration", False),
        ("Distribution or inequality", [4], "Reveal the spread, then the case", "Strip or beeswarm, histogram, percentile chart",
         "Upshot, top 1% vs bottom 60% (2017)", "An average that hides the tails", False),
        ("The sample, part of a whole", [3, 4], "Nest from whole to part", "Icon array or waffle; nested areas for the sample",
         "Galesic et al. (2009); Artsy (2021) sample", "More than five parts; a pie of many slices", False)]),
    ("change", "CHANGE", "What changed, against what?", [
        ("Change over time", [2, 4], "ABT: it was, and, but, therefore",
         "Slope or linked bars for two points; annotated line; small multiples for many series",
         "Upshot, 255 Charts (2014); Rosling, 200 Countries (2010)",
         "Two big numbers with no path; truncated axis; animation with no pause to compare", False),
        ("Comparison", [4], "Answer first; compared to what?", "Dot plot or linked bars on one shared scale; small multiples",
         "The Pudding, Film Dialogue (2016)", "Unequal bases; dual axes; a comparator picked to flatter", False),
        ("Precedent, the past rhymes", [2], "Then and now, the difference named", "Paired timeline; the old record redrawn beside the new",
         "Du Bois, data portraits (1900)", "An analogy with the difference left out", False)]),
    ("why", "WHY", "Why does it happen?", [
        ("Cause or mechanism", [4], "SCQA; rule out the rivals one by one", "Candidate causes revealed in turn against what was observed",
         "Bloomberg, What's Really Warming the World (2015); Snow (1854)", "Correlation drawn as cause; rivals left out", False),
        ("Hidden system or rule set", [4, 6], "Local rules, then interactions, then the output nobody planned",
         "Explorable simulation; stepped diagram of the rules", "Parable of the Polygons (2014), after Schelling (1971)",
         "A toy model read as data; the reader not told which knob matters", True),
        ("Network or flow", [4], "Follow one thread through the whole", "Flow map, Sankey, two-mode network",
         "Minard (1869); Healy, Paul Revere (2013)", "Hairball; flows with no totals", False)]),
    ("weigh", "WEIGH", "What should the reader weigh?", [
        ("Surprise against expectation", [1, 4], "Information gap (Loewenstein 1994): predict, then reveal",
         "“You draw it”; a guess slide, then the answer slide", "Upshot, You Draw It (2015)",
         "The truth is unsurprising; the gap too wide to guess at", True),
        ("Uncertainty", [4, 5], "Several outcomes shown side by side", "Hypothetical outcome plots; ranges; per-case needles",
         "Hullman et al. (2015); NYT needle (2016) and its lesson", "A point estimate read as a promise", False),
        ("One room standing for many", [1, 4], "Anecdotal lede, nut graf; anecdote, then reflection (Glass)",
         "The room as one marked dot inside the distribution", "Geertz, Deep Play (1972); Snow Fall (2012)",
         "The identifiable-victim effect: the one swamps the many", True),
        ("A proposal the reader|may decline", [6], "What is, what could be (Duarte 2010); the case method",
         "One diagram of the scaffold: gap, translator, shared goal, past, tower",
         "Duarte's sparkline of I Have a Dream; HBS cases (1920s)", "It turns into an instruction or a call to action", False)]),
]

def overview():
    b = []
    # arrows first: root bottom edge, fanned attach points, orthogonal elbows (r=8), outer connectors bend higher
    paths = ["M512,96 V112 A8,8 0 0 1 504,120 H176 A8,8 0 0 0 168,128 V168",
             "M568,96 V132 A8,8 0 0 1 560,140 H464 A8,8 0 0 0 456,148 V168",
             "M632,96 V132 A8,8 0 0 0 640,140 H736 A8,8 0 0 1 744,148 V168",
             "M688,96 V112 A8,8 0 0 0 696,120 H1024 A8,8 0 0 1 1032,128 V168"]
    for p in paths:
        b.append(f'<path d="{p}" fill="none" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#ov-arrow)"/>')
    # root (focal)
    b.append(f'<rect x="456" y="40" width="288" height="56" rx="28" fill="{PAPER}"/>')
    b.append(f'<rect x="456" y="40" width="288" height="56" rx="28" fill="{TINT}" stroke="{ACC}" stroke-width="1.2"/>')
    b.append(t(600, 64, "What must the reader see?", 12, INK, 600, anchor="middle"))
    b.append(t(600, 80, "one job per slide or section", 9, SOFT, fam=MONO, anchor="middle"))
    for i, (slug, tag, q, jobs) in enumerate(FAMILIES):
        x = 40 + i * 288
        b.append(f'<rect x="{x}" y="168" width="256" height="144" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>')
        tw = 12 + 6 * len(tag)
        tw += (4 - tw % 4) % 4
        b.append(f'<rect x="{x+8}" y="176" width="{tw}" height="12" rx="2" fill="transparent" stroke="rgba(26,24,19,0.40)" stroke-width="0.8"/>')
        b.append(t(x + 8 + tw // 2, 185, tag, 8, "rgba(26,24,19,0.80)", fam=MONO, anchor="middle", ls="0.08em"))
        b.append(t(x + 16, 212, q, 12, INK, 600))
        for j, job in enumerate(jobs):
            b.append(t(x + 16, 236 + j * 16, job[0].replace("|", " "), 12, MUTED))
    b.append(f'<line x1="40" y1="344" x2="1160" y2="344" stroke="rgba(26,24,19,0.10)" stroke-width="0.8"/>')
    b.append(t(40, 360, "LEGEND", 8, MUTED, fam=MONO, ls="0.18em"))
    b.append(f'<rect x="40" y="376" width="24" height="12" rx="6" fill="{TINT}" stroke="{ACC}" stroke-width="1"/>')
    b.append(t(72, 386, "Start here", 8, MUTED))
    b.append(f'<rect x="200" y="376" width="24" height="12" rx="2" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>')
    b.append(t(232, 386, "The reader's question, with its jobs; each is detailed below", 8, MUTED))
    return svg("ov", 1200, 404, "Storytelling repertoire: the reader's four questions",
               "Overview of the storytelling repertoire: the starting question, what must the reader see, branches into four "
               "families of jobs: how big is it, what changed against what, why does it happen, and what should the reader weigh.",
               b)

def detail(slug, tag, q, jobs):
    b = [t(40, 44, "THE JOB", 8, SOFT, fam=MONO, ls="0.18em"), t(320, 44, "HOW TO TELL IT AND SHOW IT", 8, SOFT, fam=MONO, ls="0.18em")]
    rows = len(jobs)
    for i, (name, spine, tell, show, copy, fails, best) in enumerate(jobs):
        y = 64 + i * 120
        cy = y + 48
        b.append(f'<line x1="280" y1="{cy}" x2="320" y2="{cy}" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{slug}-arrow)"/>')
    for i, (name, spine, tell, show, copy, fails, best) in enumerate(jobs):
        y = 64 + i * 120
        fill, stroke, sw = (TINT, ACC, "1.2") if best else (PAPER, INK, "1")
        b.append(f'<rect x="40" y="{y}" width="240" height="96" rx="6" fill="{PAPER}"/>')
        b.append(f'<rect x="40" y="{y}" width="240" height="96" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        lines = name.split("|")
        for k, ln in enumerate(lines):
            b.append(t(56, y + 32 + k * 16, ln, 12, INK, 600))
        b.append(t(56, y + 80, "spine · " + ", ".join(SPINE[s] for s in spine), 9, SOFT, fam=MONO))
        b.append(f'<rect x="320" y="{y}" width="840" height="96" rx="6" fill="{PAPER}" stroke="rgba(26,24,19,0.30)" stroke-width="1"/>')
        for k, (lab, val, size, col, wt, fam) in enumerate([
                ("TELL", tell, 12, INK, 600, SANS), ("SHOW", show, 12, MUTED, None, SANS),
                ("COPY", copy, 9, SOFT, None, MONO), ("FAILS", fails, 9, SOFT, None, MONO)]):
            yy = y + 24 + k * 20 - (2 if k > 1 else 0)
            b.append(t(336, yy, lab, 8, SOFT, fam=MONO, ls="0.12em"))
            b.append(t(392, yy, val, size, col, wt, fam=fam))
    ly = 64 + rows * 120 + 8
    b.append(f'<line x1="40" y1="{ly}" x2="1160" y2="{ly}" stroke="rgba(26,24,19,0.10)" stroke-width="0.8"/>')
    b.append(t(40, ly + 16, "LEGEND", 8, MUTED, fam=MONO, ls="0.18em"))
    b.append(f'<rect x="40" y="{ly+32}" width="24" height="12" rx="2" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>')
    b.append(t(72, ly + 42, "The job, and where it sits in the report spine", 8, MUTED))
    b.append(f'<rect x="320" y="{ly+32}" width="24" height="12" rx="2" fill="{PAPER}" stroke="rgba(26,24,19,0.30)" stroke-width="1"/>')
    b.append(t(352, ly + 42, "Story structure, visual form, the exemplar to copy, how it fails", 8, MUTED))
    if any(j[6] for j in jobs):
        b.append(f'<rect x="720" y="{ly+32}" width="24" height="12" rx="2" fill="{TINT}" stroke="{ACC}" stroke-width="1"/>')
        b.append(t(752, ly + 42, "Marked as a frequent fit", 8, MUTED))
    h = ly + 60
    names = ", ".join(j[0].replace("|", " ").lower() for j in jobs)
    return svg(slug, 1200, h, f"{q} The jobs and how to tell them",
               f"Detail of the storytelling repertoire for the question {q.lower()} Each job ({names}) is paired with its story "
               "structure, its visual form, the exemplar to copy and how it fails.", b)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Storytelling repertoire map</title>
<!-- The master table of the storytelling-repertoire skill (SKILL.md), drawn as an overview of the
     reader's four questions and one detail per question, to stay inside the Diagram Design budget of nine nodes.
     Generated by scripts/draw-map.py; edit the table there and in SKILL.md, then redraw. -->
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--paper:{PAPER};--ink:{INK};--muted:{MUTED};--rule:{RULE};
--serif:"Instrument Serif","Didot","Bodoni 72","Baskerville",serif;--body:"Geist","Helvetica Neue",system-ui,sans-serif;--mono:"JetBrains Mono","Menlo",monospace}}
body{{font-family:var(--body);background:var(--paper);color:var(--ink);padding:3rem 2rem}}
.frame{{max-width:1200px;margin:0 auto}}
.eyebrow{{font-family:var(--mono);font-size:.66rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:.5rem}}
h1{{font-family:var(--serif);font-size:clamp(1.5rem,2.4vw + .75rem,2rem);font-weight:400;letter-spacing:-.02em;line-height:1.15;margin-bottom:1.5rem}}
h2{{font-family:var(--serif);font-size:1.4rem;font-weight:400;margin:3rem 0 1rem}}
svg{{width:100%;min-width:900px;display:block}}
.colophon{{font-family:var(--mono);font-size:.66rem;color:var(--muted);border-top:1px solid var(--rule);margin-top:2rem;padding-top:.75rem}}
</style>
</head>
<body><div class="frame">
<p class="eyebrow">Overview and four details</p>
<h1>Storytelling repertoire: pick the form by the job</h1>
{overview()}
''' + "".join(f'<h2>{e(q)}</h2>\n{detail(s, tg, q, jobs)}\n' for s, tg, q, jobs in FAMILIES) + '''
<p class="colophon">Source: the storytelling-repertoire skill (SKILL.md), names and dates checked by web search 18 November 2026</p>
</div></body></html>
'''
open(sys.argv[1], "w").write(page)
print("written")
