#!/usr/bin/env python3
"""media-create: public-domain art, edited where a research finding says, with every step on record.

usage: python3 -I media.py <command> ...
  source "<query>" [--museum aic,met,cma,commons] [--limit 6]   list public-domain candidates (cached for take)
  take <cand> --topic T --finding "..." [--approach N]          download one into the library and open its record
  detect <asset> "<what>" [--tiles 4x3]                         Gemini boxes for every <what>; preview image
  plan <asset> --of <what> --share 0.4 [--seed N|--pick 1,4,9]  choose which detections change; preview for the author
  edit <asset> --prompt "..." [--boxes plan|1,4|y0,x0,y1,x1] [--variants 2] [--from vNN]
                                                                region edits; the mask is enforced in code
  paste <asset> --text "..." --box y0,x0,y1,x1 [--angle -2] [--from vNN]
                                                                exact words on a torn paper scrap, no model
  pick <asset> <variant> --note "..."                           record the author's choice
  export <asset> [--variant vNN]                                email, 4:5 social, wide share, credit line
  index                                                         rebuild library.json
  check                                                         key, models and library reachable
  setkey                                                        save the key on the clipboard, then clear it

Boxes are Gemini's convention throughout: [ymin, xmin, ymax, xmax], normalised to 0-1000.
Every command that changes an asset appends a step to its record.json, with who decided it.
"""
import base64, io, json, math, os, random, re, sys, time, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "config.json").read_text())
if (HERE / "config.local.json").exists():   # personal values, gitignored
    CFG.update(json.loads((HERE / "config.local.json").read_text()))
LIB = Path(os.path.expanduser(os.environ.get("MEDIA_LIBRARY") or CFG["library"]))   # MEDIA_LIBRARY: a scratch library for tests
UA = "Mozilla/5.0 (compatible; media-sourcing-script/0.1)"   # generic on purpose: no names in outside requests
AUTHOR = CFG.get("author") or "the author"   # the human who decides: approves the plan, picks the variant
PAPER, INK = (236, 234, 228), (22, 21, 27)
ITALIAN = re.compile(r"Uffizi|Accademia|Firenze|Florence|Brera|Capodimonte|Borghese|Vatican|Vaticani|Venezia|Venice|"
                     r"Bargello|Pitti|Pinacoteca|Museo Nazionale|Galleria Nazionale|Gallerie", re.I)
THREE_D = re.compile(r"sculpt|statue|bust|relief|figure \(|bronze|marble", re.I)


# ---------- plumbing ----------
def now(): return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def die(msg): print("error: " + msg, file=sys.stderr); sys.exit(1)

def http(url, data=None, headers=None, timeout=60, tries=3):
    h = {"User-Agent": UA, **(headers or {})}
    body = json.dumps(data).encode() if data is not None else None
    if body: h["Content-Type"] = "application/json"
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=h), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:400]
            if e.code in (429, 500, 502, 503, 504) and k < tries - 1: time.sleep(2 * (k + 1)); continue
            raise SystemExit(f"error: HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}: {msg}")
        except urllib.error.URLError as e:
            if k < tries - 1: time.sleep(2); continue
            raise SystemExit(f"error: {urllib.parse.urlsplit(url).netloc} unreachable: {e.reason}")

def getj(url, **kw): return json.loads(http(url, **kw))

def key():
    k = os.environ.get("GEMINI_API_KEY") or ""
    f = Path(os.path.expanduser(CFG["key_file"]))
    if not k and f.exists(): k = f.read_text().strip()
    if not k: die(f"no Gemini API key: put it in {CFG['key_file']} (never in the repo)")
    return k

def gemini(model, parts, config=None):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = {"contents": [{"parts": parts}]}
    if config: body["generationConfig"] = config
    out = getj(url, data=body, headers={"x-goog-api-key": key()}, timeout=240)
    cands = out.get("candidates") or []
    if not cands: die("Gemini returned no candidates: " + json.dumps(out.get("promptFeedback", out))[:300])
    return cands[0].get("content", {}).get("parts", []), out.get("usageMetadata", {})

def img_part(im, fmt="PNG", long=1600):
    im = im.convert("RGB"); s = long / max(im.size)
    if s < 1: im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, fmt, quality=92)
    return {"inline_data": {"mime_type": "image/png" if fmt == "PNG" else "image/jpeg", "data": base64.b64encode(b.getvalue()).decode()}}

def font(name, size, weight=None):
    f = ImageFont.truetype(str(HERE / "fonts" / name), size)
    if weight:
        try: f.set_variation_by_axes([weight])
        except Exception: pass
    return f


# ---------- the record ----------
def adir(a):
    d = LIB / "assets" / a
    if not (d / "record.json").exists(): die(f"no asset {a} in {LIB}/assets")
    return d

def load(a): return json.loads((adir(a) / "record.json").read_text())

def save(rec):
    d = LIB / "assets" / rec["id"]; d.mkdir(parents=True, exist_ok=True)
    (d / "record.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n")

def step(rec, cmd, by, **detail):
    rec.setdefault("steps", []).append({"at": now(), "cmd": cmd, "by": by, **detail})

def box_px(b, w, h):
    y0, x0, y1, x1 = b
    return (round(x0 / 1000 * w), round(y0 / 1000 * h), round(x1 / 1000 * w), round(y1 / 1000 * h))

def parse_box(s):
    v = [float(x) for x in s.split(",")]
    if len(v) != 4 or not all(0 <= x <= 1000 for x in v) or v[0] >= v[2] or v[1] >= v[3]:
        die("a box is y0,x0,y1,x1 in 0-1000 with y0<y1 and x0<x1")
    return v

def base_image(a, rec, frm=None):
    d = adir(a)
    if frm:
        v = rec.get("variants", {}).get(frm) or die(f"no variant {frm}")
        return Image.open(d / v["path"]).convert("RGB")
    return Image.open(d / "source.jpg").convert("RGB")

def next_variant(rec):
    n = 1 + max([int(k[1:]) for k in rec.get("variants", {})] or [0])
    return f"v{n:02d}"


# ---------- source ----------
def src_aic(q, n):
    f = "id,title,artist_title,date_display,image_id,is_public_domain,classification_title,artwork_type_title,credit_line,place_of_origin"
    j = getj(f"https://api.artic.edu/api/v1/artworks/search?q={urllib.parse.quote(q)}&limit={n*2}&fields={f}"
             "&query[term][is_public_domain]=true", headers={"AIC-User-Agent": "media-sourcing-script"})
    for o in j.get("data", []):
        if not (o.get("is_public_domain") and o.get("image_id")): continue
        yield {"cid": f"aic:{o['id']}", "holder": "Art Institute of Chicago", "title": o.get("title"), "artist": o.get("artist_title"),
               "date": o.get("date_display"), "kind": o.get("artwork_type_title") or o.get("classification_title") or "",
               "image": f"https://www.artic.edu/iiif/2/{o['image_id']}/full/1686,/0/default.jpg",
               "page": f"https://www.artic.edu/artworks/{o['id']}", "license": "Public domain (CC0), is_public_domain=true",
               "credit_raw": o.get("credit_line") or ""}

def src_met(q, n):
    # v1/search was retired 2026-10-01; v1.1 is paginated
    ids = getj(f"https://collectionapi.metmuseum.org/public/collection/v1.1/search?hasImages=true&limit={n * 4}&offset=0&q={urllib.parse.quote(q)}").get("objectIDs") or []
    got = 0
    for i in ids:
        o = getj(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}")
        if not (o.get("isPublicDomain") and o.get("primaryImage")): continue
        got += 1
        yield {"cid": f"met:{i}", "holder": "The Metropolitan Museum of Art", "title": o.get("title"), "artist": o.get("artistDisplayName"),
               "date": o.get("objectDate"), "kind": o.get("classification") or o.get("objectName") or "", "image": o["primaryImage"],
               "page": o.get("objectURL"), "license": "Public domain (CC0), isPublicDomain=true", "credit_raw": o.get("creditLine") or ""}
        if got >= n: break

def src_cma(q, n):
    j = getj(f"https://openaccess-api.clevelandart.org/api/artworks/?q={urllib.parse.quote(q)}&cc0=1&has_image=1&limit={n}")
    for o in j.get("data", []):
        im = (o.get("images") or {}); u = (im.get("print") or im.get("web") or {}).get("url")
        if o.get("share_license_status") != "CC0" or not u: continue
        cr = (o.get("creators") or [{}])[0].get("description") or ""
        yield {"cid": f"cma:{o['id']}", "holder": "Cleveland Museum of Art", "title": o.get("title"), "artist": cr,
               "date": o.get("creation_date"), "kind": o.get("type") or "", "image": u, "page": o.get("url"),
               "license": "CC0, share_license_status=CC0", "credit_raw": o.get("creditline") or ""}

def src_commons(q, n):
    p = {"action": "query", "format": "json", "generator": "search", "gsrsearch": q, "gsrnamespace": "6", "gsrlimit": str(n * 2),
         "prop": "imageinfo", "iiprop": "url|extmetadata|size", "iiurlwidth": "3840"}  # a standard thumbnail width; Wikimedia answers 429 to others (2400 failed 2026-11-19)
    j = getj("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p))
    for pg in (j.get("query", {}).get("pages") or {}).values():
        ii = (pg.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata") or {}
        val = lambda k: clean_wiki(re.sub(r"<[^>]+>", " ", (md.get(k) or {}).get("value", "")))
        lic = val("LicenseShortName")
        if not re.search(r"public domain|\bPD\b|CC0", lic, re.I): continue
        if not ii.get("thumburl"): continue
        if "thumbnail_unscaled" in ii["thumburl"] or "/thumb/" not in ii["thumburl"]:
            # Smaller than 3840: the API hands back the original on upload.wikimedia.org, which answers 429 to scripts.
            # Ask for the largest standard thumbnail under the original's width (thumb.wikimedia.org serves those).
            want = next((s for s in (1920, 1280, 960, 500, 330, 250) if s < (ii.get("width") or 0)), None)
            if want:
                t = getj("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({"action": "query", "format": "json",
                         "pageids": pg["pageid"], "prop": "imageinfo", "iiprop": "url", "iiurlwidth": str(want)}))
                ii["thumburl"] = next(iter(t["query"]["pages"].values()))["imageinfo"][0].get("thumburl") or ii["thumburl"]
        yield {"cid": f"commons:{pg['pageid']}", "holder": "Wikimedia Commons", "title": val("ObjectName") or pg.get("title", "").removeprefix("File:"),
               "artist": val("Artist"), "date": val("DateTimeOriginal"), "kind": "", "image": ii["thumburl"],
               "page": ii.get("descriptionurl"), "license": f"{lic} (Wikimedia Commons)",
               "credit_raw": " ".join([val("Credit"), val("ImageDescription")])[:600]}

def clean_wiki(s):
    """Commons metadata carries Wikidata template text: 'Children's Games title QS:P1476,en:"..."'."""
    s = re.sub(r"\s+", " ", s).strip()
    m = re.search(r'QS:P1476,\w+:"([^"]+)"', s)
    if m: return m.group(1)
    s = re.split(r"\s*(?:title|date) QS:|date QS:|QS:P", s)[0]
    return s.strip(" .")

SOURCES = {"aic": src_aic, "met": src_met, "cma": src_cma, "commons": src_commons}

def flags_for(c):
    f, blob = [], " ".join(str(c.get(k) or "") for k in ("holder", "credit_raw", "title", "page"))
    if ITALIAN.search(blob): f.append("italian-holder?: commercial reproduction may need permission")
    if c["holder"] == "Wikimedia Commons" and THREE_D.search(blob + " " + (c.get("kind") or "")) and "CC0" not in c["license"]:
        f.append("3d-photo?: a photo of a 3D work can carry the photographer's copyright")
    return f

def cmd_source(args):
    q = args[0] if args else die('source "<query>"')
    museums = (opt(args, "--museum") or "aic,met,cma,commons").split(","); n = int(opt(args, "--limit") or 6)
    cache, rows = {}, []
    for m in museums:
        try:
            for c in SOURCES[m](q, n): c["flags"] = flags_for(c); cache[c["cid"]] = c; rows.append(c)
        except SystemExit as e: print(f"  {m}: {e}", file=sys.stderr)
    LIB.mkdir(parents=True, exist_ok=True)
    old = json.loads((LIB / "_candidates.json").read_text()) if (LIB / "_candidates.json").exists() else {}
    (LIB / "_candidates.json").write_text(json.dumps({**old, **cache}, indent=1, ensure_ascii=False))
    for c in rows:
        print(f"{c['cid']:18} {(c['artist'] or '?')[:28]:28} {(c['title'] or '?')[:48]:48} {(c['date'] or '')[:14]:14} "
              f"{(c['kind'] or '')[:12]:12}{'  FLAG ' + '; '.join(c['flags']) if c['flags'] else ''}")
    if not rows: print("no public-domain matches")


def cmd_take(args):
    cid = args[0] if args else die("take <candidate-id>")
    cache = json.loads((LIB / "_candidates.json").read_text()) if (LIB / "_candidates.json").exists() else {}
    c = cache.get(cid) or die(f"{cid} not in the candidate cache; run source first")
    allow = opt(args, "--allow-flag")
    if c["flags"] and not allow: die("flagged: " + "; ".join(c["flags"]) + '. Pass --allow-flag "<reason>" after checking.')
    aid = cid.replace(":", "-")
    if (LIB / "assets" / aid / "record.json").exists(): die(f"{aid} is already in the library")
    im = Image.open(io.BytesIO(http(c["image"], timeout=120))).convert("RGB")
    s = CFG["source_long_edge"] / max(im.size)
    if s < 1: im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    d = LIB / "assets" / aid; (d / "work").mkdir(parents=True, exist_ok=True); (d / "out").mkdir(exist_ok=True)
    im.save(d / "source.jpg", quality=90)
    # --title/--artist/--date/--holder correct the source's metadata by hand (Commons names itself, not the museum)
    fix = {k: opt(args, "--" + k) for k in ("title", "artist", "date", "holder")}
    rec = {"id": aid, "title": (fix["title"] or c["title"] or "").strip(), "artist": fix["artist"] or c["artist"], "date": fix["date"] or c["date"],
           "holder": fix["holder"] or c["holder"], "image_site": c["holder"], "kind": c["kind"], "metadata_fixed": {k: v for k, v in fix.items() if v},
           "page": c["page"], "image_url": c["image"], "license": c["license"], "flags": c["flags"], "flag_override": allow,
           "pulled": now()[:10], "size": list(im.size), "topic": opt(args, "--topic") or "", "finding": opt(args, "--finding") or "",
           "approach": opt(args, "--approach") or "", "detections": {}, "plan": None, "variants": {}, "picked": None, "steps": []}
    step(rec, "take", opt(args, "--by") or "Claude", candidate=cid)
    save(rec); index(quiet=True)
    print(f"{aid}: {im.width}x{im.height} -> {d}/source.jpg")


# ---------- detect, plan ----------
def detect_once(im, what, isface):
    hint = (" A face box runs from the top of the forehead to the chin and from ear to ear. Include every face: people, angels,"
            " figures in windows, murals, sculpture and tiny background figures. Never box a whole body or an object.") if isface else ""
    prompt = (f"Find only this target in the image: {what}. Box nothing else, however prominent. Each box tightly encloses one"
              f" instance.{hint} Return a JSON list of at most 80 items, each "
              '{"box_2d": [ymin, xmin, ymax, xmax] normalised to 0-1000, "label": "<a few words>"}. If there are none, return []. Never return masks.')
    m = CFG["detect_model"]
    think = {"thinkingBudget": 0} if m.startswith("gemini-2") else {"thinkingLevel": "low"}
    schema = {"type": "ARRAY", "items": {"type": "OBJECT", "required": ["box_2d", "label"], "properties": {
        "box_2d": {"type": "ARRAY", "items": {"type": "INTEGER"}}, "label": {"type": "STRING"}}}}
    parts, use = gemini(m, [img_part(im), {"text": prompt}],
                        {"responseMimeType": "application/json", "responseSchema": schema, "thinkingConfig": think})
    txt = "".join(p.get("text", "") for p in parts if not p.get("thought")).strip()
    if os.environ.get("MEDIA_DEBUG"): print(txt[:3000], file=sys.stderr)
    try: boxes = json.loads(re.sub(r"^```(json)?|```$", "", txt).strip())
    except json.JSONDecodeError: die("detection did not return JSON: " + txt[:200])
    for b in boxes:
        if isinstance(b, dict) and "box_2d" not in b and "box" in b: b["box_2d"] = b.pop("box")
    boxes = [b for b in boxes if isinstance(b, dict) and len(b.get("box_2d", [])) == 4]
    if isface:  # the face guard rests on this, so a "face" shaped like a body fails the run instead of passing it
        big = [b["label"] for b in boxes if (b["box_2d"][2] - b["box_2d"][0]) * (b["box_2d"][3] - b["box_2d"][1]) > 120000]
        # 2026-11-19: on Bruegel's Children's Games every box was a whole small figure, far under the area limit, so
        # shape is checked too: a face is about as tall as it is wide, a standing figure two to three times taller.
        asp = sorted(((b["box_2d"][2] - b["box_2d"][0]) * im.height) / max(1, (b["box_2d"][3] - b["box_2d"][1]) * im.width) for b in boxes)
        tall = sum(1 for x in asp if x > 2.2)
        if big: die(f"face detection returned body-sized boxes ({'; '.join(big)[:200]}); nothing saved. Rerun, or check the prompt.")
        if asp and (tall or asp[len(asp) // 2] > 1.45):
            die(f"face detection returned body-shaped boxes (median height/width {asp[len(asp) // 2]:.2f}, {tall} over 2.2); "
                "nothing saved. Small figures need --tiles, e.g. --tiles 4x3.")
    return boxes, use.get("totalTokenCount") or 0

def iou(a, b):
    y0, x0, y1, x1 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, y1 - y0) * max(0, x1 - x0)
    return inter / ((a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter or 1)

def cmd_detect(args):
    a, what = (args[0], args[1]) if len(args) > 1 else die('detect <asset> "<what>" [--tiles 4x3]')
    rec = load(a); im = base_image(a, rec); W, H = im.size
    isface = what.strip().lower() in ("face", "faces")
    cols, rows = [int(x) for x in (opt(args, "--tiles") or "1x1").lower().split("x")]
    # Tiles overlap by 12% so a figure on a seam is whole in one of them; duplicates from the overlap merge into one box,
    # the union of the two, so a face guard only ever grows.
    boxes, tokens, ov = [], 0, 0.12
    for r in range(rows):
        for c in range(cols):
            tw, th = W / cols, H / rows
            x0, y0 = int(max(0, (c - ov) * tw)), int(max(0, (r - ov) * th))
            x1, y1 = int(min(W, (c + 1 + ov) * tw)), int(min(H, (r + 1 + ov) * th))
            got, t = detect_once(im.crop((x0, y0, x1, y1)), what, isface); tokens += t
            for b in got:
                by0, bx0, by1, bx1 = b["box_2d"]
                b["box_2d"] = [round((y0 + by0 / 1000 * (y1 - y0)) / H * 1000), round((x0 + bx0 / 1000 * (x1 - x0)) / W * 1000),
                               round((y0 + by1 / 1000 * (y1 - y0)) / H * 1000), round((x0 + bx1 / 1000 * (x1 - x0)) / W * 1000)]
                dup = next((k for k in boxes if iou(k["box_2d"], b["box_2d"]) > 0.4), None)
                if dup: dup["box_2d"] = [min(dup["box_2d"][0], b["box_2d"][0]), min(dup["box_2d"][1], b["box_2d"][1]),
                                         max(dup["box_2d"][2], b["box_2d"][2]), max(dup["box_2d"][3], b["box_2d"][3])]
                else: boxes.append(b)
    rec["detections"][what] = boxes
    step(rec, "detect", "Claude", what=what, n=len(boxes), tiles=f"{cols}x{rows}", model=CFG["detect_model"], tokens=tokens)
    save(rec); preview(a, rec, what, [], f"detect-{slug(what)}.jpg")
    print(f"{len(boxes)} x {what}; preview {adir(a)}/work/detect-{slug(what)}.jpg")

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]

def preview(a, rec, what, chosen, name):
    im = base_image(a, rec); dr = ImageDraw.Draw(im); w, h = im.size; f = font("SchibstedGrotesk.ttf", max(14, w // 70), 700)
    for i, b in enumerate(rec["detections"].get(what, []), 1):
        x0, y0, x1, y1 = box_px(b["box_2d"], w, h); on = i in chosen
        dr.rectangle((x0, y0, x1, y1), outline=(217, 65, 43) if on else (240, 240, 240), width=max(2, w // (300 if on else 600)))
        dr.text((x0 + 4, y0 + 2), str(i), fill=(217, 65, 43) if on else (255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
    im.save(adir(a) / "work" / name, quality=85)

def cmd_plan(args):
    a = args[0] if args else die("plan <asset> --of <what> --share 0.4")
    rec = load(a); what = opt(args, "--of") or die("--of <what>, a detection already run")
    boxes = rec["detections"].get(what) or die(f"no detections for {what!r}; run detect first")
    n = len(boxes)
    if opt(args, "--pick"):
        chosen = sorted({int(x) for x in opt(args, "--pick").split(",")}); by = opt(args, "--by") or AUTHOR
        if not all(1 <= c <= n for c in chosen): die(f"picks run 1..{n}")
    else:
        share = float(opt(args, "--share") or die("--share or --pick")); k = round(share * n)
        seed = int(opt(args, "--seed") or 1); chosen = sorted(random.Random(seed).sample(range(1, n + 1), k)); by = "Claude"
    share_txt = f"{len(chosen)} of {n} ({len(chosen) / n:.0%})"
    rec["plan"] = {"of": what, "chosen": chosen, "n": n, "share": share_txt}
    step(rec, "plan", by, of=what, chosen=chosen, share=share_txt, finding_share=opt(args, "--share"))
    save(rec); preview(a, rec, what, chosen, "plan.jpg")
    print(f"plan: {share_txt}; preview {adir(a)}/work/plan.jpg (red = will change)")


# ---------- edit ----------
WRAP = ("This is a detail of a public-domain painting. {prompt} Change only that. Paint the change in the same hand: the "
        "artist's brushwork, palette, lighting, varnish and craquelure. Leave every face, hand and the framing exactly as "
        "they are. Return the whole detail at the same framing and aspect ratio.")

def feather_mask(size, inner, faces, rad):
    def grow(b, k, extra=0):  # detections run loose, so pad each face before protecting it
        x0, y0, x1, y1 = b; px, py = (x1 - x0) * k + extra, (y1 - y0) * k + extra
        return (x0 - px, y0 - py, x1 + px, y1 + py)
    m = Image.new("L", size, 0); d = ImageDraw.Draw(m); d.rectangle(inner, fill=255)
    for fb in faces: d.rectangle(grow(fb, 0.25, rad), fill=0)   # the fade happens outside the face
    m = m.filter(ImageFilter.GaussianBlur(rad)); d = ImageDraw.Draw(m)
    for fb in faces: d.rectangle(grow(fb, 0.15), fill=0)        # faces always keep the original pixels
    return m

def regions(rec, spec, w, h):
    if spec in (None, "plan"):
        p = rec.get("plan") or die("no plan; run plan, or pass --boxes")
        dets = rec["detections"][p["of"]]; return [dets[i - 1]["box_2d"] for i in p["chosen"]]
    if re.fullmatch(r"[\d,]+", spec) and "detections" in rec and rec.get("plan"):
        dets = rec["detections"][rec["plan"]["of"]]; return [dets[int(i) - 1]["box_2d"] for i in spec.split(",")]
    return [parse_box(s) for s in spec.split(";")]

def cmd_edit(args):
    a = args[0] if args else die('edit <asset> --prompt "..."')
    rec = load(a); prompt = opt(args, "--prompt") or die("--prompt"); frm = opt(args, "--from")
    base = base_image(a, rec, frm); w, h = base.size
    regs = regions(rec, opt(args, "--boxes"), w, h)
    faces = [box_px(b["box_2d"], w, h) for b in rec["detections"].get("faces", [])]
    if not faces and "--no-face-check" not in args:
        print("no face detections yet; run: detect <asset> faces   (or pass --no-face-check for a work with none)"); sys.exit(1)
    nvar = int(opt(args, "--variants") or 1); made = []
    for _ in range(nvar):
        out = base.copy(); vid = next_variant(rec); log = []
        for r in regs:
            x0, y0, x1, y1 = box_px(r, w, h); pw, ph = (x1 - x0) * 0.18, (y1 - y0) * 0.18
            cx0, cy0, cx1, cy1 = max(0, int(x0 - pw)), max(0, int(y0 - ph)), min(w, int(x1 + pw)), min(h, int(y1 + ph))
            crop = base.crop((cx0, cy0, cx1, cy1))
            parts, use = gemini(CFG["edit_model"], [{"text": WRAP.format(prompt=prompt)}, img_part(crop, long=1536)],
                                {"responseModalities": ["TEXT", "IMAGE"]})
            data = next((p.get("inlineData") or p.get("inline_data") for p in parts if (p.get("inlineData") or p.get("inline_data"))), None)
            if not data: die("the model returned no image: " + " ".join(p.get("text", "") for p in parts)[:300])
            ed = Image.open(io.BytesIO(base64.b64decode(data["data"]))).convert("RGB")
            ar_in, ar_out = crop.width / crop.height, ed.width / ed.height
            ed.save(adir(a) / "work" / f"{vid}-raw-{len(log) + 1}.png")
            ed = ed.resize(crop.size, Image.LANCZOS)
            inner = (x0 - cx0, y0 - cy0, x1 - cx0, y1 - cy0)
            fl = [(max(0, fx0 - cx0), max(0, fy0 - cy0), fx1 - cx0, fy1 - cy0) for fx0, fy0, fx1, fy1 in faces
                  if fx1 > cx0 and fx0 < cx1 and fy1 > cy0 and fy0 < cy1]
            m = feather_mask(crop.size, inner, fl, max(2, min(crop.size) * 0.03))
            out.paste(Image.composite(ed, crop, m), (cx0, cy0))
            log.append({"box": r, "aspect_drift": round(abs(ar_in - ar_out) / ar_in, 3), "tokens": use.get("totalTokenCount")})
        out.save(adir(a) / "out" / f"{vid}.jpg", quality=92)
        rec.setdefault("variants", {})[vid] = {"path": f"out/{vid}.jpg", "kind": "edit", "prompt": prompt, "model": CFG["edit_model"],
                                              "from": frm, "regions": log, "faces_protected": len(faces), "at": now()}
        step(rec, "edit", "Claude", variant=vid, regions=len(regs), prompt=prompt, prompt_by=opt(args, "--prompt-by") or "Claude")
        save(rec); made.append(vid)
    print("made " + ", ".join(f"{adir(a)}/out/{v}.jpg" for v in made))


# ---------- paste (no model) ----------
def torn(size, rng):
    w, h = size; j = max(2, min(w, h) // 40); pts = []
    for x in range(0, w + 1, max(6, w // 30)): pts.append((x, rng.randint(0, j)))
    for y in range(0, h + 1, max(6, h // 12)): pts.append((w - rng.randint(0, j), y))
    for x in range(w, -1, -max(6, w // 30)): pts.append((x, h - rng.randint(0, j)))
    for y in range(h, -1, -max(6, h // 12)): pts.append((rng.randint(0, j), y))
    m = Image.new("L", size, 0); ImageDraw.Draw(m).polygon(pts, fill=255); return m

def fit_text(text, box_w, box_h, italic):
    name = "EBGaramond-Italic.ttf" if italic else "EBGaramond.ttf"
    for size in range(int(box_h * 0.6), 9, -1):
        f = font(name, size, 500); words, lines, cur = text.split(), [], ""
        for wd in words:
            t = (cur + " " + wd).strip()
            if f.getlength(t) <= box_w * 0.9: cur = t
            else: lines.append(cur); cur = wd
        lines.append(cur); lh = size * 1.18
        if len(lines) * lh <= box_h * 0.86 and all(f.getlength(l) <= box_w * 0.9 for l in lines): return f, lines, lh
    die("the text does not fit that box; make the box bigger or the text shorter")

def cmd_paste(args):
    a = args[0] if args else die('paste <asset> --text "..." --box y0,x0,y1,x1')
    rec = load(a); text = opt(args, "--text") or die("--text"); frm = opt(args, "--from")
    base = base_image(a, rec, frm).convert("RGBA"); w, h = base.size
    x0, y0, x1, y1 = box_px(parse_box(opt(args, "--box") or die("--box")), w, h); bw, bh = x1 - x0, y1 - y0
    faces = [box_px(b["box_2d"], w, h) for b in rec["detections"].get("faces", [])]
    if not faces and "--no-face-check" not in args: die("no face detections yet; run: detect <asset> faces   (or --no-face-check)")
    faces = [(f[0] - (f[2] - f[0]) * .15, f[1] - (f[3] - f[1]) * .15, f[2] + (f[2] - f[0]) * .15, f[3] + (f[3] - f[1]) * .15) for f in faces]
    hit =[f for f in faces if f[2] > x0 and f[0] < x1 and f[3] > y0 and f[1] < y1]
    if hit: die(f"that box covers {len(hit)} face(s); faces stay as painted. Move the box.")
    f, lines, lh = fit_text(text, bw, bh, "--italic" in args)
    scrap = Image.new("RGBA", (bw, bh), PAPER + (255,)); d = ImageDraw.Draw(scrap)
    ty = (bh - len(lines) * lh) / 2
    for i, l in enumerate(lines): d.text(((bw - f.getlength(l)) / 2, ty + i * lh), l, font=f, fill=INK)
    rng = random.Random(len(text)); scrap.putalpha(torn((bw, bh), rng))
    ang = float(opt(args, "--angle") or -1.5); scrap = scrap.rotate(ang, resample=Image.BICUBIC, expand=True)
    sh = Image.new("RGBA", scrap.size, (0, 0, 0, 0)); sh.putalpha(scrap.getchannel("A").point(lambda v: v * 0.35))
    sh = sh.filter(ImageFilter.GaussianBlur(max(2, bw // 120)))
    ox, oy = x0 - (scrap.width - bw) // 2, y0 - (scrap.height - bh) // 2
    base.alpha_composite(sh, (max(0, ox + 3), max(0, oy + 4))); base.alpha_composite(scrap, (max(0, ox), max(0, oy)))
    vid = next_variant(rec); base.convert("RGB").save(adir(a) / "out" / f"{vid}.jpg", quality=92)
    rec.setdefault("variants", {})[vid] = {"path": f"out/{vid}.jpg", "kind": "paste", "text": text, "box": parse_box(opt(args, "--box")),
                                          "angle": ang, "from": frm, "model": None, "at": now()}
    step(rec, "paste", opt(args, "--by") or "Claude", variant=vid, text=text, text_by=opt(args, "--text-by") or f"{AUTHOR}'s finding")
    save(rec); print(f"made {adir(a)}/out/{vid}.jpg")


# ---------- pick, export, index ----------
def cmd_pick(args):
    a, v = (args[0], args[1]) if len(args) > 1 else die("pick <asset> <variant>")
    rec = load(a); rec["variants"].get(v) or die(f"no variant {v}")
    rec["picked"] = v; step(rec, "pick", AUTHOR, variant=v, note=opt(args, "--note") or "")
    save(rec); index(quiet=True); print(f"{a}: {v} picked")

def credit(rec):
    who = re.sub(r"\s*\(.*?\)\s*", " ", rec.get("artist") or "Unknown artist").strip()
    title = (rec.get("title") or "Untitled").strip(" ,")
    by = f" Edited by {CFG['credit_by']}." if CFG.get("credit_by") else ""
    return f"After {who}, {title}, {rec.get('date') or 'n.d.'}. {rec['holder']}, public domain.{by}"

def framed(im, W, H, cap, margin):
    cv = Image.new("RGB", (W, H), PAPER); capf = font("SchibstedGrotesk.ttf", max(14, W // 54), 500)
    cap_h = int(capf.size * 2.6); s = min((W - 2 * margin) / im.width, (H - 2 * margin - cap_h) / im.height)
    r = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (W - r.width) // 2, margin + (H - 2 * margin - cap_h - r.height) // 2; cv.paste(r, (x, y))
    d = ImageDraw.Draw(cv); words, lines, cur = cap.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if capf.getlength(t) <= W - 2 * margin: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur)
    for i, l in enumerate(lines[:2]): d.text((margin, y + r.height + capf.size * (0.7 + 1.25 * i)), l, font=capf, fill=(92, 91, 98))
    return cv

def cmd_export(args):
    a = args[0] if args else die("export <asset>")
    rec = load(a); v = opt(args, "--variant") or rec.get("picked") or die("no picked variant; pick one or pass --variant")
    im = base_image(a, rec, v); d = adir(a) / "out" / f"{v}-export"; d.mkdir(exist_ok=True); cap = credit(rec)
    e = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS) if im.width > 1200 else im
    e.save(d / "email-1200.jpg", quality=88)
    framed(im, 1080, 1350, cap, 64).save(d / "social-1080x1350.jpg", quality=90)
    framed(im, 1200, 630, cap, 36).save(d / "share-1200x630.jpg", quality=90)
    (d / "credit.txt").write_text(cap + "\n")
    step(rec, "export", "Claude", variant=v); save(rec)
    print(f"{d}/ email-1200.jpg social-1080x1350.jpg share-1200x630.jpg credit.txt\n{cap}")

def index(quiet=False):
    rows = []
    for f in sorted((LIB / "assets").glob("*/record.json")):
        r = json.loads(f.read_text())
        rows.append({k: r.get(k) for k in ("id", "title", "artist", "date", "holder", "license", "flags", "topic", "finding", "approach", "picked")}
                    | {"variants": len(r.get("variants", {})), "human_steps": sum(1 for s in r.get("steps", []) if s["by"] == AUTHOR)})
    (LIB / "library.json").write_text(json.dumps({"updated": now(), "assets": rows}, indent=1, ensure_ascii=False) + "\n")
    if not quiet: print(f"{len(rows)} assets -> {LIB}/library.json")

def cmd_check(args):
    print("library:", LIB, "ok" if LIB.exists() else "missing")
    ms = getj("https://generativelanguage.googleapis.com/v1beta/models?pageSize=200", headers={"x-goog-api-key": key()})
    names = {m["name"].split("/")[-1] for m in ms.get("models", [])}
    for m in (CFG["detect_model"], CFG["edit_model"]):
        if m not in names: print(f"{m}: NOT LISTED for this key"); continue
        try:  # a listed model can still refuse new keys, so ping it
            gemini(m, [{"text": "Reply with the single word ok."}], {"responseModalities": ["TEXT"]} if m == CFG["edit_model"] else None)
            print(f"{m}: ok")
        except SystemExit: print(f"{m}: listed but refused a call (see error above)")

def cmd_setkey(args):
    import subprocess
    k = subprocess.run(["pbpaste"], capture_output=True, text=True).stdout.strip()
    if not (k.startswith("AIza") and 30 <= len(k) <= 60 and not any(c.isspace() for c in k)):
        die(f"clipboard holds {len(k)} chars that do not look like a Gemini key (AIza...); copy the key and run again. Nothing saved.")
    f = Path(os.path.expanduser(CFG["key_file"])); f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(k + "\n"); f.chmod(0o600)
    subprocess.run(["pbcopy"], input="", text=True)
    print(f"saved {len(k)}-char key to {CFG['key_file']} (0600); clipboard cleared")

def opt(args, name):
    return args[args.index(name) + 1] if name in args and args.index(name) + 1 < len(args) else None

CMDS = {"source": cmd_source, "take": cmd_take, "detect": cmd_detect, "plan": cmd_plan, "edit": cmd_edit, "paste": cmd_paste,
        "pick": cmd_pick, "export": cmd_export, "index": lambda a: index(), "check": cmd_check, "setkey": cmd_setkey}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS: print(__doc__); sys.exit(0 if len(sys.argv) < 2 else 1)
    CMDS[sys.argv[1]](sys.argv[2:])
