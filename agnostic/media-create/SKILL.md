---
name: media-create
description: "Make your own edits of public-domain art (Renaissance paintings, sculpture, engravings) where a research finding decides the change, log every step with who decided it, and export the publishing sizes. Trigger on '/media-create', 'make art for this finding', 'make the plate for this issue', 'edit a painting for this', 'find public-domain art for <topic>', 'harvest media for <topic>', and whenever a report or newsletter issue is drafted and has no image yet. Also the backend for harvesting a media asset library."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# media-create

Public-domain art, edited where a finding says, with a record of every human choice. The tool is
`python3 -I <skill-dir>/media.py` (run it with no arguments for usage). It needs Pillow and a paid Gemini
API key.

**Configure** `config.json`: `library` (where assets and `library.json` live; `MEDIA_LIBRARY=<dir>`
points a test elsewhere), `key_file`, `author` (the person whose choices the record credits),
`credit_by` (the studio or name for the credit line, or empty), and the two model ids. Put personal
values in `config.local.json` beside it (gitignored); its keys override `config.json`.

## Rules the tool enforces, and the ones it cannot

- **Sources are public domain only:** the Art Institute of Chicago, the Met, Cleveland (CC0 flags), and Wikimedia
  Commons (public-domain license). Works held in Italy and Commons photos of 3D works are flagged; `take` refuses
  them unless `--allow-flag "<reason>"` records why.
  Time&Again posts may also use CC BY and CC BY-SA images, with the credit on the slide (Rafael, 2026-11-21, "yes", on
  Vindolanda and Qesem Cave), and Library of Congress photos marked "no known restrictions". Model edits stay
  public domain only.
- **Faces stay as painted.** `edit` and `paste` refuse to run until `detect <asset> faces` has run, `edit` puts the
  original pixels back on every face, and `paste` refuses a box over a face. Hands and lettering are also weak spots
  for the model (Canva's guidance): aim edits at objects, clothing and props.
- **The mask is ours.** The model sees only a crop around the region; only the region itself is composited back,
  feathered. The rest of the painting is the museum's pixels.
- **Exact words never go through the model.** Clauses, quotes and numbers are set by `paste` on a torn paper scrap
  in EB Garamond (fonts here, OFL).
- **Human authorship (it cannot enforce this one).** Prompt-only AI output is not copyrightable (US Copyright
  Office, January 2025). What can be owned is human selection and arrangement, so the author makes the choices and
  the record says so: they approve the finding, the work, the plan or box, and pick the variant. Claude proposes;
  pass `--by <author>` only when the author decided. `pick` is always the author's.
- **Media shows a system or a repeated pattern (it cannot enforce this one).** Never use figures only for counting.
  Before `take`, write down the theory the image reveals (memetics, complex contagion, the evolution of cooperation,
  weak ties) and the pattern it repeats across time. A figure used as a tally mark fails, and the figures must be the
  population the finding measured. One early plate (Bruegel's children, one child standing for two minutes with
  friends, drawn from adults' data) failed both tests and was pulled.
- **Only public-domain art and our own data go to any model.** Paid Gemini API use is not trained on; never use a
  free-tier key.

## The approaches the tool runs

| # | Approach | Commands |
|---|---|---|
| 1 | The edit is the chart: change exactly the finding's share of figures | `detect <a> "<figures>"` then `plan <a> --of "<figures>" --share 0.4` then `edit <a> --prompt "..."` |
| 2 | Paste-up: the study's own words set into the painting | `paste <a> --text "..." --box y0,x0,y1,x1 [--angle 178]` |
| 5 | Masked edit of one region | `edit <a> --boxes y0,x0,y1,x1 --prompt "..."` |
| 3, 4 | Mosaic portrait, sculpture to dots | Not built yet: code in the kit and Spline |
| 6 | Cut-outs: detected figures cut from the museum's pixels, set where the figure carries the pattern (the same game in 1560 and the 1750s) or the system (ties drawn between players); never as tally marks | `detect --tiles`, then `swiftc -O lift.swift -o lift` and `lift <crop.png> <mask.png>` per figure (Apple Vision, on-device, nothing generated); not yet a media.py command |

Boxes are `[ymin, xmin, ymax, xmax]` in 0-1000 (Gemini's convention). Get them from a `detect` preview in `work/`.

## A run, from a finding to the issue

1. **Brief.** The finding as a sentence and its number, the topic, the approach, and the theory and repeated pattern the
   image carries. From the issue draft or the author.
2. **Source.** `source "<query>"`; show the author the candidates (artist, title, date, holder, flags); `take <cid>
   --topic ... --finding "..." --approach N`, with `--holder`/`--date` when Commons names itself, not the museum.
3. **Detect.** `detect <a> faces`, then the figures or objects the approach needs. Open the preview in `work/`.
4. **Plan.** Approach 1: `plan --share <the finding's share>`; the author may override with `--pick`. Approach 2:
   choose the box with them. Show `work/plan.jpg` before spending any edit.
5. **Make.** `edit` (two `--variants` for a first pass) or `paste`. Each edit costs one image call per region.
6. **Pick.** The author picks: `pick <a> vNN --note "..."`.
7. **Export.** `export <a>` writes `email-1200.jpg` (into the Substack post), `social-1080x1350.jpg` (Instagram and
   LinkedIn, on paper, credit under it), `share-1200x630.jpg`, and `credit.txt`. The credit line goes under the
   image wherever it runs. `index` rebuilds `library.json`.

## Harvest mode

For building the library ahead of findings: per research topic, run `source` with a few queries and `take` the
works that suit it with `--topic`, no `--finding`, no edits. Edits wait for a finding and the author's picks. Agents
harvesting in parallel each take a topic; `take` refuses duplicates, and `index` is safe to rerun.

## Setup

- Key: a paid Gemini API key at the `key_file` path (never in a repo, never in chat). The user copies the key;
  `setkey` saves it from the clipboard (refuses anything not shaped `AIza...`), sets 0600 and clears
  the clipboard. `check` confirms the key works and both models are listed.
- Models (`config.json`): detection `gemini-3.8-flash`, edits `gemini-3-pro-image` (Nano Banana Pro). The models
  list shows models a new key cannot call (`gemini-2.5-flash` returned 404 on 2026-11-15), so `check` pings each one.
- Detection replies are pinned to a JSON schema; face results with body-sized or body-shaped boxes (median height over
  width above 1.45, or any above 2.2) fail the run. Small background faces (windows, medallions, floor tiles) can be
  missed: check the `detect-faces.jpg` preview before an edit.
- Crowds need `--tiles 4x3`: one pass sees the work at 1600px and caps at 80 boxes. On Bruegel's *Children's Games*
  (2026-11-19) the single pass returned 80 whole figures as "faces"; tiled, it found 135 faces and 168 figures.
- A treatment has to show on every chosen figure. Grisaille clothing failed that test on *Children's Games*: brown and
  black clothes look the same in grey, and the face guard keeps the hood or cap around each face in color.
- Edits follow the prompt conservatively (asked to replace a book, it kept the book and added pages): name what goes
  and what replaces it.
- Requests carry a generic user agent and no personal names.
- Commons images come at 3840px, one of Wikimedia's standard thumbnail widths; it answers 429 to other widths and to
  bursts (2026-11-19: about ten fetches in a few minutes locked downloads out for a while). Fetch one at a time.
  The Art Institute's IIIF images sat behind a Cloudflare check the same night (403).
- `lift <crop> <mask> group` keeps every subject with a real share of the crop's center, for a pair at play (leapfrog);
  without `group` it keeps the one figure under the center.
