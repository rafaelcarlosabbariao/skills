---
name: drop
description: "Route a dropped link (any URL, PDF, Are.na block, or local file) to the project it serves and log it as consumed knowledge in that project's drops register, with an optional write-back to a notes vault or knowledge graph. Trigger on '/drop', 'drop this', 'file this link', 'where does this link go', 'save this for <project>', or a bare pasted URL with no other ask."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# /drop: the intake for consumed knowledge

One link in, up to two writes out: a **register entry** in the project the link serves, and a
**notes write-back** when the link carries something worth a note. Never silently drop a link;
"none of the above" is a routing outcome.

## Configure once

Fill the routing table below with your own projects. Each row is a project, the folder or repo
that holds its register, and what belongs there. Keep a catch-all row for links that serve several
projects or none.

| Project | Folder | Belongs here when it is about |
|---|---|---|
| `<project-a>` | `~/<project-a>` | `<subjects>` |
| `<project-b>` | `~/<project-b>` | `<subjects>` |
| cross-project / unclear | `~/<notes-home>` | serves several projects, or no clean fit |

Optional: the path to a notes vault (Obsidian or similar) for step 4, and its folder names.

## Step 1: fetch and identify

Fetch the URL (or read a local path). Establish what it is (article, paper, tool, repo, person,
product, video, Are.na block), who made it, and one line of what it claims or does. If the fetch
fails, still route on the URL and whatever the user said when dropping it; note `unfetched` in the
entry.

## Step 2: route by project first

Ask "which project does this serve?" before "what type is this?". Whatever the user says when
dropping it beats all inference; then subject matter. When two projects both plausibly claim it,
prefer the more specific one. Torn: route to the catch-all and say so in the entry.

## Step 3: existing intakes take precedence

If a kind of drop already has a dedicated intake (a reading list, a competitor tracker, a log of
your own published work), use that one and do not double-file.

Everything else lands in the project's drops register: **`docs/drops.md`** in the project folder.
Create it on first drop with the header below; prepend under a dated heading, newest day first:

```markdown
# Drops: consumed knowledge register

Intake log written by the /drop skill. Newest first. Every entry names why it
landed here; the notes line says what note it fed, or `notes: none` and why.

## 2026-01-15
- **<title>** <url>
  what: <one factual line>. why here: <the project signal>. notes: [[<note>]] | none (<reason>). next: <read / cite in X / build / none>.
```

Entries say what the thing is, with no praise. A register may grow **standing lanes** above the
dated log when the user names one. Do not invent lanes unprompted.

## Step 4: notes write-back (optional)

If a vault is configured and the link introduces or strengthens a note (a thinker, topic,
platform, method, work), write or update it in the vault's existing style. Not every drop earns a
note; when skipped, the register entry records `notes: none` and why. Do not create new top-level
folders.

## Step 5: report back

One short confirmation: project, file written, note touched or skipped, and the `next:` you
recorded. No summary of the fetched page beyond the register line.

## Bulk drops (tab dumps, bookmark exports)

Run the same route per link but batch the writes per destination file, and show a routing table
for confirmation before writing anything when the batch exceeds about ten links.
