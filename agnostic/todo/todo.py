#!/usr/bin/env python3
"""Open work reader for the To Do register.

The register: every project (an "arm") is a git repo under one root folder that keeps its open
work in a root TODO.md, unless the project's own CLAUDE.md moves it off that default under a
"## Task system of record" heading. That heading is the ONLY thing consulted; the shape is never
inferred from anything else.

The root folder is $TODO_ROOT, or your home directory when unset.

Read-only by design. Nothing here checks anything off. Items are ticked at the source.

Usage:
  todo.py                 open work for the arm you are standing in
  todo.py <arm>           open work for a named arm
  todo.py all             every arm, grouped
  todo.py [...] --done    include completed items
  todo.py [...] --json    machine-readable, same data
"""

import json
import os
import re
import subprocess
import sys

HOME = os.path.expanduser(os.environ.get("TODO_ROOT") or "~")
BOX = re.compile(r"^(\s*)- \[( |x|X)\]\s+(.*)$")
HEADING = re.compile(r"^##\s+(.*?)\s*$")
CITATION = re.compile(r"`([A-Za-z0-9._/~-]+\.[A-Za-z0-9]+):(\d+)`")
RECORD_HEADING = re.compile(r"^##\s+Task system of record\b.*$", re.M)


def discover_arms():
    """An arm is a git repo under the root with a root TODO.md. Adding the file is the whole of
    opting in, so discovery beats a hardcoded list that would go stale."""
    arms = {}
    if not os.path.isdir(HOME):
        return arms
    for name in sorted(os.listdir(HOME)):
        path = os.path.join(HOME, name)
        if not os.path.isdir(path) or name.startswith("."):
            continue
        if os.path.isdir(os.path.join(path, ".git")) and os.path.isfile(os.path.join(path, "TODO.md")):
            arms[name] = path
    return arms


def task_system(path):
    """Resolve the arm's declared task system. Only the CLAUDE.md heading counts."""
    claude_md = os.path.join(path, "CLAUDE.md")
    if not os.path.isfile(claude_md):
        return {"shape": "markdown", "declared": False, "note": None}
    text = open(claude_md, encoding="utf-8", errors="replace").read()
    m = RECORD_HEADING.search(text)
    if not m:
        return {"shape": "markdown", "declared": False, "note": None}
    section = text[m.end():]
    nxt = re.search(r"^## ", section, re.M)
    section = section[: nxt.start()] if nxt else section
    low = section.lower()
    if "notion-first" in low:
        shape = "notion-first"
    elif "companion" in low:
        shape = "markdown+companion"
    else:
        shape = "markdown"
    first = next((ln.strip() for ln in section.splitlines() if ln.strip()), None)
    return {"shape": shape, "declared": True, "note": first}


def parse_todo(path, arm):
    """Rows are checkbox lines; a row owns the indented lines that follow it."""
    todo = os.path.join(path, "TODO.md")
    lines = open(todo, encoding="utf-8", errors="replace").read().splitlines()
    rows, section, current = [], None, None

    def close():
        nonlocal current
        if current:
            current["text"] = re.sub(r"\s+", " ", current["text"]).strip()
            current["citations"] = [
                {"path": p, "line": int(n)} for p, n in CITATION.findall(current["text"])
            ]
            rows.append(current)
            current = None

    for i, line in enumerate(lines, 1):
        h = HEADING.match(line)
        if h:
            close()
            section = h.group(1)
            continue
        b = BOX.match(line)
        if b:
            close()
            current = {
                "arm": arm,
                "line": i,
                "section": section,
                "status": "done" if b.group(2).lower() == "x" else "open",
                "indent": len(b.group(1)),
                "text": b.group(3),
            }
            continue
        if current is not None:
            if line.strip() == "":
                close()
            elif line.startswith((" ", "\t")):
                current["text"] += " " + line.strip()
            else:
                close()
    close()
    return rows


def unpushed(path):
    try:
        out = subprocess.run(
            ["git", "-C", path, "rev-list", "--count", "@{u}..HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        return int(out.stdout.strip()) if out.returncode == 0 else None
    except Exception:
        return None


def collect(arm, path):
    ts = task_system(path)
    rows = parse_todo(path, arm)
    return {
        "arm": arm,
        "path": path.replace(HOME, "~"),
        "taskSystem": ts,
        "unpushed": unpushed(path),
        "rows": rows,
        "open": sum(1 for r in rows if r["status"] == "open"),
        "done": sum(1 for r in rows if r["status"] == "done"),
    }


def strip_md(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"~~(.+?)~~", r"\1", s)
    return s


def render(bundle, show_done, width=96):
    a = bundle
    head = f"{a['arm']}  ({a['path']}/TODO.md)"
    print(head)
    print("-" * min(len(head), width))

    ts = a["taskSystem"]
    if ts["shape"] == "notion-first":
        print("  Task system of record: NOTION-FIRST (declared in CLAUDE.md).")
        print("  This file is a pointer. Open rows live in Notion and are not readable here:")
        print("  this script has no Notion credentials by design. Ask Claude to query the")
        print("  board directly with the Notion tools.")
        if ts["note"]:
            print(f"  {strip_md(ts['note'])[:width]}")
        print()
        return
    if ts["shape"] == "markdown+companion":
        print("  Task system of record: MARKDOWN + Notion companion (declared).")
        print("  The companion is for thinking and references. A task only counts here.")

    if not a["rows"]:
        print("  No items.")
        print()
        return

    section = object()
    for r in a["rows"]:
        if r["status"] == "done" and not show_done:
            continue
        if r["section"] != section:
            section = r["section"]
            print(f"\n  ## {section or '(no section)'}")
        mark = "x" if r["status"] == "done" else " "
        text = strip_md(r["text"])
        if len(text) > width:
            text = text[: width - 1] + "…"
        print(f"  [{mark}] {text}")
        print(f"      TODO.md:{r['line']}", end="")
        if r["citations"]:
            cites = " ".join(f"{c['path']}:{c['line']}" for c in r["citations"][:4])
            print(f"   -> {cites}", end="")
        print()

    print()
    tail = f"  {a['open']} open, {a['done']} done"
    if a["unpushed"]:
        tail += f"  |  {a['unpushed']} unpushed commit(s) in this repo"
    print(tail)
    print()


def cwd_arm(arms):
    try:
        root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
    except Exception:
        root = ""
    if root:
        name = os.path.basename(root)
        if name in arms:
            return name
    return None


def main():
    args = [a for a in sys.argv[1:]]
    show_done = "--done" in args
    as_json = "--json" in args
    targets = [a for a in args if not a.startswith("-")]

    arms = discover_arms()
    if not arms:
        print(f"No arms found: no git repo in {HOME} has a root TODO.md.", file=sys.stderr)
        return 1

    if targets and targets[0] == "all":
        chosen = list(arms)
    elif targets:
        want = targets[0]
        if want not in arms:
            print(f"Unknown arm '{want}'. Known: {', '.join(arms)}", file=sys.stderr)
            return 1
        chosen = [want]
    else:
        here = cwd_arm(arms)
        if here is None:
            print("Not standing in a registered arm. Showing every arm.\n")
            chosen = list(arms)
        else:
            chosen = [here]

    bundles = [collect(a, arms[a]) for a in chosen]

    if as_json:
        print(json.dumps({"arms": bundles}, indent=2))
        return 0

    for b in bundles:
        render(b, show_done)

    if len(bundles) > 1:
        md = [b for b in bundles if b["taskSystem"]["shape"] != "notion-first"]
        notion = [b for b in bundles if b["taskSystem"]["shape"] == "notion-first"]
        print("=" * 60)
        print(f"{sum(b['open'] for b in md)} open across {len(md)} markdown arm(s)"
              + (f", plus {len(notion)} Notion-first arm(s) not counted here" if notion else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
