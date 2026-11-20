---
name: todo
description: "Show the open to-do list for a project, or across every project at once, read from a To Do register (a root TODO.md per repo, overridden only by a '## Task system of record' heading in that repo's CLAUDE.md). Trigger on '/todo', 'what's on the list', 'show me the todos', 'what's open here', 'what's open across everything', 'what am I working on', 'show open work for <project>', or any ask for the current state of a project's task list."
---

If `SKILL.local.md` exists in this folder, read it first; it holds your paths, data and house rules.

# /todo: read the To Do register

One command that answers "what is open?" from inside any repo, for that repo or for all of them.

## The register

- Every project is a git repo under one root folder (`$TODO_ROOT`, or your home directory) with a
  root `TODO.md`. Adding that file is the whole of opting a repo in; there is no list to keep current.
- Items are markdown checkboxes (`- [ ]`, `- [x]`) grouped under `##` headings. A `path:line` in
  backticks inside an item is reported as a citation.
- A repo may move its task list elsewhere (for example, a Notion board) by adding a
  `## Task system of record` heading to its own `CLAUDE.md`. The words `notion-first` or
  `companion` in that section set the shape. Nothing else is consulted.

**This is a read, not the record.** Nothing here checks anything off. Items are ticked at the
source: the repo's own `TODO.md`, or the board for a Notion-first repo. Do not offer to tick a box
as part of running this.

## Run it

`SK` is wherever you installed this skill, for example `~/.claude/skills/todo`.

```
python3 $SK/todo.py              # the repo you are standing in
python3 $SK/todo.py <project>    # a named repo, from anywhere
python3 $SK/todo.py all          # every repo, with a total
python3 $SK/todo.py all --done   # include completed items
python3 $SK/todo.py all --json   # same data, machine-readable
```

Show the output as it comes. It is already grouped by section, carries `TODO.md:<line>` for every
item and any `path:line` sources the item cites, and reports unpushed commits per repo. Do not
re-read the `TODO.md` files yourself to reformat it: the script exists so a session does not pay
for ten file reads to answer this.

## Notion-first repos

The script holds no Notion credentials on purpose, so a Notion-first repo prints a pointer. When
the rows matter, query the board directly with the Notion tools, never from a doc line, a frozen
snapshot or a filtered view.

**A Notion companion is never a task source.** Read it for context; if something there turns out
to be work, write it into `TODO.md` before it counts.

## When someone asks for more than a list

The `--json` output is shaped for a richer, linked, sortable view (a dashboard or a nightly mirror
into a notes vault). Build that as its own surface that reads the JSON; this skill stays the cheap
read.
