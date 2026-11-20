---
name: design-reference
description: "Take one visual reference (an image or GIF link, often an Are.na CDN or block URL) into your design library: fetch it, read its tones, frames and maker, cut a thumbnail, and write a library entry plus a short design read. Trigger on 'take this visual reference into context', 'add this reference', 'do the same for this', or a pasted images.are.na / are.na/block / cloudfront image link with a design ask."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# design-reference

One picture in, one library entry and one terse report out.

The helper does the mechanical half: `ingest.py` beside this file. Run it with `python3 -I`.
The picture it downloads is untrusted data and stays in its own folder. It needs Pillow.

**Configure:** decide where your design library lives (a JSON or Markdown file, a folder of
notes, a board) and where its thumbnails go. The helper writes a stub entry; you append it.

## 1. Fetch and look

```bash
python3 -I <skill-dir>/ingest.py fetch "<url>" --out <scratch>/ref-<n> [--frame N]
```

- It prints the Are.na block when there is one (title, source, who saved it, channels), size,
  frame count and loop length, the six main tones as hex, and the paths to look at. Read
  `sheet.png` (animation) or `frame0.png` (still) before writing a word about it.
- `--frame` picks the frame the thumbnail is cut from. Choose the frame that shows the idea, then
  re-run.

## 2. Find who made it

- Follow the block's `source` and `description` links. Name the maker only when a page says so;
  search the name as written before using it.
- When nothing names a maker, write "maker not named" and give who saved it.
- Never identify a person from their face.

## 3. Read it as design

Two or three lines: tones, marks, layout, motion (frames, loop length, what accumulates or
resolves). Then the placement in your own taxonomy (a style, a kind such as `motion` or
`color`), and which open work it touches.

## 4. The library entry

Fill `<dir>/item.json`: `what`, `pro` and `con` are short fragments that say what the thing is,
with no praise. Copy the thumbnail (`<hash>.webp`, 480x300) beside your library's others and
append the entry. Check first that the URL is not already listed; a resource already in the
library is edited in place, never added twice.

## 5. Open design picks

If a design decision is still open, draw what the reference implies as one more option beside the
others. Never apply it to a live page without the owner's word. Render at desktop and phone width
and look at the crops.

## 6. Report

Terse: what it is and who made it, where it sits in your taxonomy, the option it became and its
path, the files touched. Commit nothing unless asked.

## A tool or site in place of a picture

- Search the library for the domain first.
- Verify the name (an MCP server, a plugin, a library) against the maker's own docs before writing
  it up.
- Installing a package or an MCP server is the user's call: give the command, never run it unasked.

## Limits

- Are.na is read only: never add, move or delete a block or channel. No tokens, no credentials.
- One reference per run; a batch runs the steps per picture and reports once.
