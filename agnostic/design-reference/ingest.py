"""The mechanical half of the design-reference skill.

    python3 -I ingest.py fetch <image-url> [--out DIR] [--frame N]

fetch downloads the picture into its own folder (treat it as untrusted), looks up the Are.na block
when the URL is an Are.na CDN or block link, writes a contact sheet for an animation, samples the
picture's tones, saves a 480x300 webp thumbnail, and leaves an item.json stub for the session to
fill and append to your own design library.
"""
import argparse, hashlib, json, re, subprocess, tempfile
from pathlib import Path

UA = "Mozilla/5.0"


def arena_block(url):
    for pat in (r"cloudfront\.net/(\d+)/", r"are\.na/block/(\d+)", r"images\.are\.na/.*?/(\d+)/"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def get_json(url):  # curl, since the Are.na API refuses urllib's requests
    r = subprocess.run(["curl", "-sf", "-m", "20", url], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def fetch(a):
    from PIL import Image, ImageSequence
    out = Path(a.out or tempfile.mkdtemp(prefix="design-ref-"))
    out.mkdir(parents=True, exist_ok=True)
    raw = out / "original"
    subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-o", str(raw), a.url], check=True)
    meta, canon = {"image_url": a.url}, a.url
    bid = arena_block(a.url)
    if bid:
        try:
            b = get_json(f"https://api.are.na/v2/blocks/{bid}")
            img = ((b.get("image") or {}).get("original") or {}).get("url") or ""
            tail = a.url.split("/")[-1].split("?")[0][-20:]
            meta.update(block=bid, matches_image=tail in img, title=b.get("title"), description=b.get("description"),
                        source=(b.get("source") or {}).get("url"), saved_by=(b.get("user") or {}).get("slug"),
                        saved_at=b.get("created_at"), channels=[c.get("title") for c in b.get("connections") or []])
            canon = f"https://www.are.na/block/{bid}"
        except Exception as e:  # a CDN number that is not a block id, or the API is down
            meta["arena_error"] = str(e)
    im = Image.open(raw)
    frames = [f.convert("RGB").copy() for f in ImageSequence.Iterator(im)]
    durs = []
    for i in range(len(frames)):
        im.seek(i)
        durs.append(im.info.get("duration", 0))
    meta.update(size=list(frames[0].size), frames=len(frames), loop_ms=sum(durs) if len(frames) > 1 else 0)
    k = a.frame if a.frame is not None else (len(frames) // 3 if len(frames) > 1 else 0)
    frames[0].save(out / "frame0.png")
    if len(frames) > 1:
        W, H = frames[0].size
        pick = [round(i * (len(frames) - 1) / 11) for i in range(12)]
        sheet = Image.new("RGB", (W * 3, H * 4), "white")
        for j, idx in enumerate(pick):
            sheet.paste(frames[idx], ((j % 3) * W, (j // 3) * H))
        sheet.save(out / "sheet.png")
    q = frames[k].quantize(colors=6, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[:18]
    counts = sorted(q.getcolors(), reverse=True)
    meta["tones"] = ["#%02X%02X%02X" % tuple(pal[i * 3:i * 3 + 3]) for _, i in counts]
    # the thumbnail, named by a hash of the canonical URL
    h = hashlib.md5(canon.encode()).hexdigest()[:12]
    t = frames[k]
    r = max(480 / t.width, 300 / t.height)
    t = t.resize((round(t.width * r), round(t.height * r)), Image.LANCZOS)
    x, y = (t.width - 480) // 2, (t.height - 300) // 2
    t.crop((x, y, x + 480, y + 300)).save(out / f"{h}.webp", "WEBP", quality=72)
    item = {"name": meta.get("title") or "", "url": canon, "what": "", "pro": "", "con": "",
            "img": f"{h}.webp", "style": "", "kind": "", "maker": "", "saved_by": meta.get("saved_by") or "",
            "source": "arena" if bid else ""}
    (out / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
    if not (out / "item.json").exists():
        (out / "item.json").write_text(json.dumps(item, indent=1, ensure_ascii=False))
    print(json.dumps(meta, indent=1, ensure_ascii=False))
    print(f"\nfolder: {out}\nlook at: {out / ('sheet.png' if len(frames) > 1 else 'frame0.png')}\nthumb: {out / (h + '.webp')}"
          f"\nfill {out / 'item.json'}, then append it to your design library")


p = argparse.ArgumentParser()
s = p.add_subparsers(dest="cmd", required=True)
f = s.add_parser("fetch"); f.add_argument("url"); f.add_argument("--out"); f.add_argument("--frame", type=int)
a = p.parse_args()
fetch(a)
