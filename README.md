# skills

Claude Code skills I wrote and use, with personal data removed.

## Install

```sh
git clone https://github.com/rafaelcarlosabbariao/skills.git
ln -s "$PWD/skills/agnostic/autoresearch" ~/.claude/skills/autoresearch   # or cp -R
```

One folder per skill. Fill any `config.json`, template or "Configure" note before first use. Put your own paths and rules in a `SKILL.local.md` beside a skill's `SKILL.md` (gitignored); each skill reads it first.

## Agnostic

| Skill | What it does | Trigger |
|---|---|---|
| autoresearch | Overnight one-metric experiment loop, git as judge | "run autoresearch" |
| deep-dive | 20-minute project deep-dive: prep doc and slides | "deep dive" |
| depth-scroll | Page whose panels fly toward the reader on scroll | "depth scroll" |
| design-reference | One image into your design library | "add this reference" |
| drop | Routes a pasted link to its project and logs it | "/drop" |
| forecast-call | Seals one dated, falsifiable forecast | "seal a call" |
| graph-engineering | Agent architecture and memory shelf | "loop or swarm?" |
| media-create | Public-domain art edited where a finding says | "/media-create" |
| outreach | Cold DM or email from your own fact record | "write a DM to" |
| storytelling-repertoire | Story structure and visual form by evidence job | "how should we tell this" |
| todo | Open `TODO.md` items across repos | "/todo" |

## Social intelligence

| Skill | What it does | Trigger |
|---|---|---|
| destrange | Screens a cultural claim, then validates or rebuilds it | "run the destrange" |
| diffusion-contagion | Shelf: how things spread | "will this break out" |
| gossip-reputation | Shelf: what talk about people does | "malice or maintenance?" |
| language-change | Shelf: how words survive a ranked feed | "will this slang stick" |
| semiotics-decoding | Shelf: signs and codes | "what is this signaling" |
| social-psychology | Shelf: influence, judgment, identity | "organic or manufactured?" |
| social-simulation | Shelf: agent models, synthetic panels | "trust a simulated audience?" |
| status-taste-markets | Shelf: status and cultural markets | "good, or a cascade?" |
| virality-attention | Shelf: transmission | "wave or pocket?" |
| whatthefad | Reverse cultural archaeology of a trend | "where did X come from" |

## Credits: third-party skills I use

Not included; get them upstream.

- [gstack](https://github.com/garrytan/gstack) (MIT), including its `diagram` skill
- [diagram-design](https://github.com/cathrynlavery/diagram-design) (MIT)
- [claude-drawing](https://github.com/cloveric/claude-drawing-skill) (MIT)
- [REA, reverse-engineer-anything](https://github.com/morluto/rea)
- [i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT)
- [lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) (PolyForm Noncommercial)
- [cultural-intelligence](https://github.com/coreymaypray/sloth-skill-tree)
- [Anthropic skills](https://github.com/anthropics/skills)
- autoresearch ports [karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## License

MIT. Fonts in `agnostic/media-create/fonts/` are SIL OFL (`OFL.txt`).
