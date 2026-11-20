"""Build a depth-scroll page from a spec: stations on a depth axis that the scroll travels down,
with a stream of cards flying toward the viewer behind them (after WhatTheFad's landing field).

    python3 -I build.py spec.json

or from a project's own build script, when the spec is computed:

    sys.path.insert(0, str(Path.home() / '.claude/skills/depth-scroll'))
    import build
    build.write(spec, base=Path(__file__).parent)

Every path in the spec is relative to `base` (the spec file's folder on the command line), and
image paths are written into the page as given, so give them relative to the output page. The
spec's fields are documented in SKILL.md.
"""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = re.compile(r'<figure class="fig">\s*(.*?)\s*</figure>', re.S)
# the source page's own style blocks, skipping any pinned-header styles (id="pin-...")
CSS = re.compile(r'<style(?![^>]*\bid="pin-)[^>]*>(.*?)</style>', re.S)


def esc(s):
    return html.escape(s or '', quote=True)


def render(spec, base=Path('.')):
    base = Path(base)
    figs, src_css = [], ''
    if spec.get('source'):
        src = (base / spec['source']).read_text()
        figs = FIG.findall(src)
        src_css = '\n'.join(CSS.findall(src))

    stations = [dict(id='door', kind='door', html=spec.get('door', ''), title=spec.get('door_label', 'The door'))]
    stations += spec['stations']
    if spec.get('close'):
        c = spec['close']
        stations.append(dict(id='close', kind='close', sec=c.get('title', 'Sources'), title=c.get('title', 'Sources'),
                             kicker=c.get('kicker', 'The close'), html=c.get('html', '')))
    n = len(stations)
    ids = [s['id'] for s in stations]
    assert len(set(ids)) == n, f'station ids repeat: {ids}'

    def section_of(i):
        for s in reversed(stations[:i + 1]):
            if s.get('sec'):
                return s['sec']
        return ''

    marks, slots, rail = [], [], []
    for i, s in enumerate(stations):
        title = s.get('title') or s.get('sub') or s.get('sec') or ''
        # contents lines: a section line, then the station's own line when it is a subsection
        if s.get('sec') and s.get('sub'):
            marks.append(f'<div class="mark" data-at="{i}" id="sec-{esc(s["id"])}" data-toc="sec" data-title="{esc(s["sec"])}"></div>')
        toc = ''
        if s.get('sub'):
            toc = f' data-toc="sub" data-title="{esc(s["sub"])}"'
        elif s.get('sec'):
            toc = f' data-toc="sec" data-title="{esc(s["sec"])}"'
        marks.append(f'<div class="stop mark" data-at="{i}" id="st-{esc(s["id"])}"{toc}></div>')
        rail.append(f'<button type="button" data-go="{i}" aria-label="{esc(title)}"></button>')

        if s.get('kind') == 'door':
            body = s['html']
        elif s.get('kind') == 'close':
            body = f'<p class="kick">{esc(s["kicker"])}</p><h2 data-toc="skip">{esc(title)}</h2>{s["html"]}'
        else:
            kick = s.get('kicker') or (section_of(i) if s.get('sub') else spec.get('kicker', ''))
            if 'fig' in s:
                assert s['fig'] < len(figs), f'station {s["id"]}: figure {s["fig"]} not in the source ({len(figs)} found)'
                inner = f'<figure class="fig">{figs[s["fig"]]}</figure>'
            else:
                inner = s.get('html', '')
            cards = ''
            if s.get('cards'):
                cards = '<div class="cards">' + ''.join(
                    f'<figure><img src="{esc(c["img"])}" alt="" decoding="async"><figcaption>{esc(c["label"])}</figcaption></figure>'
                    for c in s['cards']) + (f'<p class="from">{esc(spec["cards_label"])}</p>' if spec.get('cards_label') else '') + '</div>'
            lead = f'<p class="lead">{s["lead"]}</p>' if s.get('lead') else ''
            body = (f'<p class="kick">{esc(kick)}</p>' if kick else '') + f'<h2 data-toc="skip">{esc(title)}</h2>{lead}{inner}{cards}'
        lit = ' '.join(s.get('lit', [])) if isinstance(s.get('lit'), list) else (s.get('lit') or '')
        slots.append(f'<div class="slot" data-i="{i}" data-lit="{esc(lit)}" style="z-index:{n - i}">'
                     f'<article class="station" aria-label="{esc(title)}">{body}</article></div>')

    chips = ''.join(
        f'<span class="ch" data-set="{esc(c.get("group", ""))}">'
        + (f'<img src="{esc(c["img"])}" alt="" decoding="async">' if c.get('img') else '')
        + f'<span>{esc(c["label"])}</span></span>'
        for c in spec.get('stream', []))

    page = (HERE / 'template.html').read_text()
    for k, v in {'/*TITLE*/': esc(spec['title']), '/*SOURCE_CSS*/': src_css, '/*EXTRA_CSS*/': spec.get('css', ''),
                 '/*MARKS*/': '\n'.join(marks), '/*SLOTS*/': '\n'.join(slots), '/*RAIL*/': ''.join(rail), '/*CHIPS*/': chips}.items():
        assert page.count(k) == 1, k
        page = page.replace(k, v)
    return page


def write(spec, base=Path('.')):
    out = Path(base) / spec['out']
    out.write_text(render(spec, base))
    print(out, out.stat().st_size // 1024, 'KB;', len(spec['stations']), 'stations,', len(spec.get('stream', [])), 'cards in the stream')
    return out


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    p = Path(sys.argv[1]).resolve()
    write(json.loads(p.read_text()), base=p.parent)
