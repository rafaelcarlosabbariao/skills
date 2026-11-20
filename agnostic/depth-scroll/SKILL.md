---
name: depth-scroll
description: "Build a depth-scroll page: a sequence of panels (drawings, one-idea cards, stages) set as stations on a depth axis that the scroll travels down, each one coming out of the distance, resting sharp at the screen plane and passing the viewer, with a stream of cards flying toward the viewer behind them, after the landing field of WhatTheFad (whatthefad.netlify.app). Trigger on 'a UI that scrolls towards the user', 'like whatthefad', 'make this fly toward me', 'depth scroll', 'scroll into the screen', 'a tunnel of these', or any ask to turn a flat page of figures into one the reader travels through."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# Depth scroll

A page format for a set of figures the reader travels through, one at a time. The first build
turned a set of explanatory drawings into a scroll toward the viewer, modeled on the landing page of
WhatTheFad ([whatthefad.netlify.app](https://whatthefad.netlify.app), source at
[github.com/rafaelcarlosabbariao/cultural-archaeology](https://github.com/rafaelcarlosabbariao/cultural-archaeology)).

The skill holds four files:

| File | What it is |
| --- | --- |
| `template.html` | The page: station chrome, the stream, the rail, and the script that runs them |
| `build.py` | Fills the template from a spec, as a command or as a module |
| `capture.mjs` | Real-time headless captures and navigation checks over the DevTools protocol |
| `SKILL.md` | This file |

## When it fits

- **It fits** four to twelve self-contained panels read one at a time, each fitting a screen:
  drawings, one-idea cards, the stages of a sequence.
- **It does not fit** long prose, tables, or anything a reader compares side by side or scans back
  and forth through. Build a flat page for those.
- **Output.** The page is one self-contained `.html` file, with no external scripts and no WebGL.
  The template ships with a warm cream and ink palette in `:root` tokens; restyle them to taste.

## How it works

### WhatTheFad's field, the source

Read from WhatTheFad's `index.html` (`#landing-trendfield` CSS, and the `renderTrendField`
function).

- **Projection.** The field is a container with `perspective: 900px`, and each chip is placed with
  `translate3d(x, y, z)`. The browser draws a chip at scale 900 / (900 − z): 0.24 at z = −2800, 1
  at the screen plane and 1.3 at z = 220.
- **A clock drives the motion.** A `requestAnimationFrame` loop moves each chip toward the viewer
  at 150 px/s times a per-chip factor of 0.75 to 1.25. Past z = 220 it respawns on an elliptical
  ring at z = −2800.
- **Fades and paint order.** A chip fades in over the first quarter of its depth and out between z = 60
  and 220. The field never uses `preserve-3d`, so each chip's `z-index` is set from its depth to
  make the nearer one paint on top.
- **The quiet center.** A radial `mask-image` hides the middle, where far chips gather at the
  vanishing point.
- **Catching a chip.** The browser re-checks `:hover` only when the pointer moves, so a chip
  drifting under a still cursor never lights. WhatTheFad tests the pointer against each chip's
  projected rectangle every frame, and a caught chip slows the field to 8%.

### What this format adds

- **The scroll is the camera.**
  - A tall track (`main.depth`) holds one stop per station, one stage height apart, with
    `scroll-snap-type: y proximity`.
  - A sticky stage under the pinned header holds the scene.
  - The scroll position becomes a station index, whole at each stop. A camera eases toward it
    (rate 9 per second), and station `i` is drawn at z = (camera − i) × 1400.
- **A station's passage.**
  - The station waiting behind is dim and sits a little low, so it rises into place as it comes
    forward.
  - At rest it is at z = 0 and scale 1, on whole pixels, so its text is as sharp as a flat page.
  - Passing the viewer, it fades out by z = 300, at 1.5×.
  - A station taller than the stage is scaled to fit.
- **The stream.** WhatTheFad's field, mask included. The cards' speed is a base of 46 plus 0.9 of
  the camera's speed, so scrolling forward rushes them past and scrolling back sends them away. A
  station names the card groups it draws on (`lit`), and those cards light up while it is in front.
- **Input.**
  - Wheel, trackpad, touch, the arrow keys, the rail and the header's contents all move the one
    native scroll, so every input lands on the same stops.
  - Focus entering a station that is not in front scrolls to it.
  - The stream is decorative, and only the station at rest takes pointer events, so no per-frame
    hit test is needed.
- **Fallback.** Without JavaScript, or with `prefers-reduced-motion: reduce`, the page is the
  stations stacked flat. The depth is switched on by a `deep` class the script adds. In flat mode
  the contents' anchors move onto the stations.

## Building one

`SK` below is wherever you installed this skill, for example `~/.claude/skills/depth-scroll`.

1. **Content first.** Put each panel on a flat page as `<figure class="fig">` holding a `.plate`
   (the drawing) and a `figcaption`. The flat page is also the reading copy. A station can instead
   carry raw `html`.
2. **Write a spec** (below), as a JSON file or as a dict in the project's own build script when
   values are computed (for example, card names read from a data file).
3. **Build it.**
   ```sh
   python3 -I $SK/build.py spec.json
   ```
   or, from a script:
   ```python
   sys.path.insert(0, str(Path.home() / '.claude/skills/depth-scroll'))
   import build
   build.write(spec, base=HERE)
   ```
4. **Optional header.** The template leaves room for a pinned header (`--pin-h`, `header.pin`,
   `nav.pin-toc`). Without one, the stage starts at the top of the window.
5. **Check it** with `capture.mjs` (below), then commit.

### The spec

Paths are relative to `base`: the spec file's folder, or the folder passed to `write`. Image
paths are written into the page as given, so give them relative to the output page.

| Field | What it holds |
| --- | --- |
| `out` | The page to write |
| `title` | The `<title>`, named by kind (`<Subject> <kind noun>`) |
| `source` | Optional flat page. Its `figure.fig` blocks become `fig: n`, and its style blocks (not the header's) are copied in so the drawings keep their classes |
| `kicker` | The small label over a section-level station; a subsection's kicker is its section's name |
| `door` | HTML of the first station: a standfirst, a note, a link to the flat page |
| `stations[]` | `id`; `sec` and/or `sub` (the contents lines; `sec` alone is a section, `sub` alone a subsection, both opens a section on this station); `title` (defaults to `sub`, then `sec`); `lead` (HTML, one or two sentences); `fig` or `html`; `cards` (`[{img, label}]`, a small image row); `lit` (stream groups to light) |
| `cards_label` | The label at the end of a station's image row |
| `close` | `{title, kicker, html}` for the last station, usually the sources |
| `stream[]` | `{label, img, group}` per card. Forty to eighty reads as a stream |
| `css` | Optional extra CSS, appended last |

### Checking

```sh
K=$SK/capture.mjs
node $K file:///path/page.html at-2.png 2                  # a station at rest
node $K file:///path/page.html transit.png 4.4 --wait=900  # between two stations, snapping off
node $K file:///path/page.html last.png 9                  # the last stop is reachable
node $K file:///path/page.html light.png 5 --light         # the daylight ground
node $K file:///path/page.html phone.png 3 375 700         # phone width
node $K file:///path/page.html flat.png 0 --reduce         # the reduced-motion page
node $K "file:///path/page.html#st-model" hash.png -       # a link to a stop, on load
node $K file:///path/page.html nav.png 0 --nav             # arrows, the last contents link, the rail
```

Each run prints the stops and, per step, `y`, `front` (the station taking pointer events),
`rail`, `cardsShown`, `cardsLit`, `deep` and `pageWidth`. A station at rest has `front` equal to
its index; `pageWidth` must read the viewport width (no sideways page scroll). Look at every
image, in both grounds and at phone width, before calling it done. For pages whose images sit
outside the folder, copy the page to the scratchpad with absolute image paths first.

Do not check with `chrome --headless --screenshot`. Under `--virtual-time-budget`, animation frames
barely advance, so the eased camera never arrives, and a screenshot of a scrolled window can come
back blank. `capture.mjs` drives a real-time headless Chrome, where frames run at their real rate.

## Tuning

The constants sit at the head of the script in `template.html`.

| Constant | Value | What it moves |
| --- | --- | --- |
| `PERSP` | 900 | Must match the CSS `perspective` on `.stations` and `.field` |
| `GAP` | 1400 | World depth between two stations |
| `AHEAD` | 2.2 × GAP | How far ahead a station is drawn at all |
| `PASS` | 300 | Where a passing station has faded out (scale 1.5) |
| `LIFT` | 36 | Pixels a waiting station sits low per GAP of distance |
| `DEPTH`, `NEAR` | 2800, 220 | The stream's spawn depth and the depth where a card has flown past |
| `BASE` | 46 | The stream's speed at rest, px/s |
| camera ease | 9 per second | How quickly the camera catches the scroll |

## What went wrong on the first build

Each of these was found by looking, and each is fixed in the template.

- **The header's scroll margin.** The pinned header gives every `[id]` a `scroll-margin-top`, so
  anchors land below it. Jumps landed 126px short of each stop until the stops were set to zero.
- **The track was one header short.** The page ended before the last stop could reach the top.
  The track's height uses the window height, not the stage's.
- **Cards flew behind the contents column.** That column is fixed and transparent, so cards
  showed through its text. When the column is fixed, the stage starts to its right.
- **Far cards gathered at the vanishing point.** WhatTheFad's mask fixed it.
- **The passing station lingered as a large blur.** The fix was a shorter `PASS` and a squared fade.
- **The waiting station showed under short stations.** It is drawn dim (squared).
- **The flat mode's contents pointed at hidden stops.** The stops move onto the stations.
- **A scroll that landed before the load event hit a short page.** The track is laid out as soon
  as the document is parsed, and again once fonts and images settle, so a restored scroll and a
  `#st-<id>` link both land.
- **On a phone** the wide drawings pan sideways inside their plate, the image row is hidden, and the
  station is narrowed so the rail keeps the right edge.

## Open

- **Catching a card.** In WhatTheFad a caught chip opens an excavation. Here a card could open
  its record, which needs the target page to take an id in its URL and the projected hit test
  above.
- **A pause control.** The stream moves for as long as the page is open. Reduced motion stops
  it, but there is no pause button, which WCAG 2.2.2 asks of motion that lasts more than five
  seconds alongside other content.
- **The feel on a real trackpad and phone, and the frame rate,** have not been judged by a person.
