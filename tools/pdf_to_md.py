#!/usr/bin/env python3
"""Extract a PDF to markdown-ish text, page by page, preserving column reading order.

Usage: pdf_to_md.py <input.pdf> <output.md>

Method
- pdftotext -bbox-layout gives every text block with its bounding box.
- Per page, blocks are classed as left column, right column or full width
  relative to the page midline.
- The page is cut into horizontal bands: a full-width block forms a band;
  the gaps between are two-column bands. Each band is extracted with
  pdftotext -layout on a crop box (left crop + right crop for two-column
  bands), so tables keep their alignment and columns read in order.
- Output carries a marker per page with the PDF page index and the printed
  page label read from the page corner.
- Chapter thumb tabs in the right margin are cropped away. Pages whose text
  is mostly whitespace (board layouts, wiring, dimension drawings) are
  flagged as drawings and their labels listed without positions.
- Figures (raster or vector) are located by rendering the page and looking
  at the ink left after masking the text (see figures.py). Each gets a
  marker after the page text with a reference (figure number on the page,
  position in points), its caption when one stands next to it, and the short
  text-layer labels it contains. When tesseract is installed the figure is
  OCR'd and the recognised text follows the marker, flagged as OCR; a figure
  is never described and never saved as an image.
- A page without a text layer is OCR'd whole when tesseract is installed.
- Page furniture (running headers, footers, page numbers: text repeated at
  the same position on three or more pages, in the top or bottom zone) is
  cropped out of the body; the header/footer text goes into the page marker.
- A font report at the top of the file lists fonts that are not standard
  text faces, with the glyphs they produce and the pages they occur on, and
  fonts without a ToUnicode map. Those glyphs must be verified against the
  rendered page before they are trusted or mapped.
- Evidence from the rendered page, recorded as page notes and applied by
  stage 2 (the body text stays verbatim):
  * ligatures: on a page set in a font without a ToUnicode map, the page is
    OCR'd and a text-layer word is noted as restored when the OCR word is the
    same word with an "f" inserted before i, l or f (the fi/fl/ff ligature
    glyph that the text layer dropped) and nothing else differs;
  * drawn list markers: a small ink mark just left of a text line, outside
    every text box, is a bullet the text layer does not carry; the line is
    noted so stage 2 can render the list.
- Text is otherwise verbatim from the text layer: symbol-font glyphs that
  map to wrong characters are NOT repaired here.

Limits
- Assumes one or two text columns per band; three-column pages are not split.
- Symbol-font glyphs are passed through unrepaired (stage 2 maps them from a
  verified table).

Requires poppler-utils (pdftotext, pdfinfo, pdftoppm, pdftohtml, pdffonts);
tesseract for OCR.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True   # no __pycache__ in the repository
import figures  # noqa: E402

NS = "{http://www.w3.org/1999/xhtml}"
TOL = 8.0          # pt tolerance around the midline
SPAN_SHARE = 0.20  # share of midline-straddling blocks above which a page is one flow
MIN_GUTTER = 6.0   # pt of clear space needed between the two columns of a band
TABLE_SHARE = 0.5  # share of blocks in baseline-aligned single-line pairs that marks a table
CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
PAGE_LABEL = re.compile(r"^(?:page\s+)?(\d{1,3}(?:\s*/\s*\d{1,3})?|\d{1,2}\s*-\s*\d{1,2}|[ivx]{1,4})$", re.I)   # 83, 50/163, Page 3/5, 4 - 5, iv
SPARSE = 0.80      # whitespace share above which a page is treated as a drawing
TOP_ZONE = 0.20    # share of page height where a repeated block counts as a header
BOTTOM_ZONE = 0.15 # share of page height where a repeated block counts as a footer
REPEATS = 3        # pages a block must repeat on, at the same place, to be furniture
CAPTION = re.compile(r"^(fig(ure|\.)?|abb\.?|bild|diagram|drawing|photo|illustration|image)\s*\d", re.I)
OCR_DPI = 300      # render resolution for tesseract (600 read an LCD screenshot worse, not better)
OCR_CONF = 60      # tesseract word confidence below which a word is dropped
LIG_CONF = 80      # confidence an OCR word needs to restore a dropped ligature glyph
LIG = re.compile(r"f(?=[ilf])")   # a dropped fi/fl/ff ligature leaves the word missing an f before i, l or f
MARK_DPI = 72      # render resolution for the left-margin mark check (1 px = 1 pt)
MARK_REACH = 16.0  # pt left of a line start searched for a drawn list marker
MARK_DARK = 160    # grey level below which a pixel is ink
MARK_SIZE = 0.75   # largest side of a list marker, as a share of the line height (an inline icon fills the line)
TEXT_FACE = re.compile(r"(helvetica|arial|times|courier|calibri|cambria|verdana|tahoma|georgia|"
                       r"segoe|frutiger|univers|myriad|minion|futura|gill|franklin|garamond|"
                       r"roboto|open ?sans|source|noto|dejavu|liberation|palatino|book|century|"
                       r"trebuchet|optima|avenir|lato|ubuntu|meta|din|swiss|dutch|nimbus|proxima|"
                       r"industry|qtype|rockwell|aptos|yahei|simsun|malgun|gothic|mincho|kozgo|kozmin|"
                       r"humanist|zurich|akzidenz|neue|sans|serif|mono|text|eurotechnic|"
                       r"(?:std|pro|lt|mt)(?![a-z]))", re.I)   # foundry suffixes only as name endings: "Product" is not "Pro"
SYMBOL_FACE = re.compile(r"(dingbat|symbol|wingding|webding|pict|icon|glyph|marlett|bullet|math|cmsy|cmex|msam|msbm)", re.I)


def is_text_face(family):
    return bool(TEXT_FACE.search(family)) and not SYMBOL_FACE.search(family)


def run(args):
    return subprocess.run(args, check=True, capture_output=True).stdout


OCR_TIMEOUT = 300   # s per tesseract call; a page that takes longer is reported, not read


def run_ocr(args):
    """Tesseract on one thread (several OCR processes side by side spin-wait
    each other to a crawl when each takes all cores) with a time limit.
    Returns None on timeout."""
    env = dict(os.environ, OMP_THREAD_LIMIT="1")
    try:
        return subprocess.run(args, check=True, capture_output=True, timeout=OCR_TIMEOUT, env=env).stdout
    except subprocess.TimeoutExpired:
        return None


def page_count(pdf):
    info = run(["pdfinfo", pdf]).decode("utf-8", "replace")
    return int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))


def blocks_by_page(pdf):
    """One bbox pass over the whole document: {page: (W, H, [blocks])}."""
    raw = run(["pdftotext", "-bbox-layout", pdf, "-"])
    xml = CTRL.sub("", raw.decode("utf-8", "replace"))
    root = ET.fromstring(xml)
    pages = {}
    for pno, page in enumerate(root.iter(f"{NS}page"), start=1):
        W, H = float(page.get("width")), float(page.get("height"))
        out = []
        for b in page.iter(f"{NS}block"):
            words = [w.text or "" for w in b.iter(f"{NS}word")]
            txt = " ".join(words).strip()
            if not txt:
                continue
            box = lambda e: (float(e.get("xMin")), float(e.get("yMin")), float(e.get("xMax")), float(e.get("yMax")))
            lines = []
            for ln in b.iter(f"{NS}line"):
                lt = " ".join(w.text or "" for w in ln.iter(f"{NS}word")).strip()
                if lt:
                    lines.append(box(ln) + (lt,))
            out.append(dict(x0=float(b.get("xMin")), y0=float(b.get("yMin")),
                            x1=float(b.get("xMax")), y1=float(b.get("yMax")), text=txt,
                            nlines=len(lines) or 1, lines=lines,
                            words=[box(w) + (w.text or "",) for w in b.iter(f"{NS}word") if (w.text or "").strip()]))
        pages[pno] = (W, H, out)
    return pages


def crop_text(pdf, pno, x, y, w, h):
    if w <= 1 or h <= 1:
        return ""
    raw = run(["pdftotext", "-layout", "-f", str(pno), "-l", str(pno),
               "-x", str(int(x)), "-y", str(int(y)), "-W", str(int(w) + 1), "-H", str(int(h) + 1),
               pdf, "-"])
    return CTRL.sub("", raw.decode("utf-8", "replace"))


def tidy(txt):
    lines = [l.rstrip() for l in txt.split("\n")]
    nonblank = [l for l in lines if l.strip()]
    if not nonblank:
        return ""
    indent = min(len(l) - len(l.lstrip(" ")) for l in nonblank)
    lines = [l[indent:] if l.strip() else "" for l in lines]
    out, blank = [], 0
    for l in lines:
        if l == "":
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(l)
    return "\n".join(out).strip("\n")


def furniture_key(b, H):
    # Same text (digits wildcarded) in the same zone; headers may alternate left/right.
    return (re.sub(r"\d+", "#", b["text"])[:60], in_zone(b, H))


def in_zone(b, H):
    return "top" if b["y1"] < H * TOP_ZONE else ("bottom" if b["y0"] > H * (1 - BOTTOM_ZONE) else None)


def is_outermost(b, blocks, zone):
    """Nothing lies entirely above a header block or entirely below a footer block."""
    if zone == "top":
        return not any(o["y1"] <= b["y0"] for o in blocks if o is not b)
    return not any(o["y0"] >= b["y1"] for o in blocks if o is not b)


def furniture_candidates(blocks, H):
    for b in blocks:
        zone = in_zone(b, H)
        if zone and len(b["text"]) <= 160 and is_outermost(b, blocks, zone):
            yield b


def furniture_keys(pages):
    """Outermost header/footer blocks whose text repeats on REPEATS pages or more."""
    from collections import Counter
    cnt = Counter()
    for W, H, blocks in pages.values():
        if W:
            cnt.update({furniture_key(b, H) for b in furniture_candidates(blocks, H)})
    return {k for k, c in cnt.items() if c >= REPEATS}


def split_furniture(blocks, W, H, keys):
    """Return (body blocks, header texts, footer texts, y_top, y_bottom)."""
    furn = {id(b) for b in furniture_candidates(blocks, H) if furniture_key(b, H) in keys}
    body, head, foot = [], [], []
    for b in blocks:
        if id(b) in furn:
            (head if in_zone(b, H) == "top" else foot).append(b)
        else:
            body.append(b)
    y_top = max((b["y1"] for b in head), default=0.0)
    y_bottom = min((b["y0"] for b in foot), default=H)
    # Never crop through body text: if a body block reaches into the zone, keep the zone.
    if any(b["y0"] < y_top for b in body):
        y_top = 0.0
    if any(b["y1"] > y_bottom for b in body):
        y_bottom = H
    texts = lambda bl: [b["text"] for b in sorted(bl, key=lambda b: (round(b["y0"]), b["x0"]))
                        if not PAGE_LABEL.match(b["text"])]
    return body, texts(head), texts(foot), y_top, y_bottom


def printed_label(blocks, W, H, keys=frozenset()):
    # Short page-number token in the bottom 10 % of the page with nothing but
    # furniture below it; take the lowest.
    rest = [b for b in blocks if furniture_key(b, H) not in keys]
    cands = [b for b in blocks if b["y1"] > H * 0.90 and PAGE_LABEL.match(b["text"])
             and is_outermost(b, rest, "bottom")]
    if not cands:
        return None
    cands.sort(key=lambda b: -b["y1"])
    label = PAGE_LABEL.match(cands[0]["text"]).group(1)
    return re.sub(r"\s*-\s*", "-", label.split("/")[0].strip())


def tab_limit(blocks, W):
    """Right-edge chapter thumb tabs (short numbers stacked in the margin).
    Returns the x where the text area ends, or W if no tabs are present."""
    tabs = [b for b in blocks
            if b["x0"] > W - 40 and re.fullmatch(r"\d{1,2}(\s+\d{1,2})*", b["text"])]
    if sum(len(b["text"].split()) for b in tabs) < 5:
        return W
    return min(b["x0"] for b in tabs) - 2


def table_rows(left, right):
    """Rows where a single-line left block and a single-line right block share
    a baseline: the signature of a table whose columns fall either side of
    the midline. Two-column prose is made of multi-line paragraph blocks."""
    n = 0
    for a in left:
        if a["nlines"] > 1:
            continue
        for b in right:
            if b["nlines"] > 1:
                continue
            ov = min(a["y1"], b["y1"]) - max(a["y0"], b["y0"])
            if ov > 0.5 * min(a["y1"] - a["y0"], b["y1"] - b["y0"]):
                n += 1
                break
    return n


def bands_for(blocks, W, H):
    """Cut the page into (kind, y0, y1, xsplit) bands. kind is "full" or "two";
    xsplit is the x of the column gutter for a "two" band."""
    mid = W / 2
    left = [b for b in blocks if b["x1"] <= mid + TOL]
    right = [b for b in blocks if b["x0"] >= mid - TOL]
    span = [b for b in blocks if b not in left and b not in right]
    # A full-width table also has cells left and right of the midline, but
    # many of its cells straddle it. Real two-column text almost never does.
    if not left or not right or len(span) > SPAN_SHARE * len(blocks):
        return [("full", 0.0, H, None)]
    # Merge overlapping full-width blocks into bands, then grow each band to
    # cover any column block that overlaps it vertically (a footer such as
    # "docno | legal line | url" is three blocks on one line), so that no
    # block is cut by a band edge and extracted twice.
    span.sort(key=lambda b: b["y0"])
    merged = []
    for b in span:
        if merged and b["y0"] <= merged[-1][1] + 2:
            merged[-1][1] = max(merged[-1][1], b["y1"])
        else:
            merged.append([b["y0"], b["y1"]])
    others = left + right
    changed = True
    while changed:
        changed = False
        for band in merged:
            for b in others:
                if b["y0"] < band[1] and b["y1"] > band[0] and (b["y0"] < band[0] or b["y1"] > band[1]):
                    band[0], band[1] = min(band[0], b["y0"]), max(band[1], b["y1"])
                    changed = True
        merged.sort()
        i = 0
        while i + 1 < len(merged):
            if merged[i + 1][0] <= merged[i][1] + 2:
                merged[i][1] = max(merged[i][1], merged[i + 1][1])
                del merged[i + 1]
                changed = True
            else:
                i += 1
    bands, cur = [], 0.0
    for y0, y1 in merged:
        if y0 - cur > 2:
            bands.append(["two", cur, y0, None])
        bands.append(["full", y0, y1, None])
        cur = y1
    if H - cur > 2:
        bands.append(["two", cur, H, None])
    # Decide each candidate two-column band on its own blocks. A table whose
    # columns happen to avoid the midline, or a band with no real gutter, is
    # extracted full width: an interleaved column is readable, a cut table is not.
    for band in bands:
        if band[0] != "two":
            continue
        y0, y1 = band[1], band[2]
        L = [b for b in left if b["y0"] < y1 and b["y1"] > y0]
        R = [b for b in right if b["y0"] < y1 and b["y1"] > y0]
        if not L or not R:
            band[0] = "full"
            continue
        gutter_l, gutter_r = max(b["x1"] for b in L), min(b["x0"] for b in R)
        rows = table_rows(L, R)
        if gutter_r - gutter_l < MIN_GUTTER or (rows >= 3 and rows >= TABLE_SHARE * min(len(L), len(R))):
            band[0] = "full"
        else:
            band[3] = (gutter_l + gutter_r) / 2
    # Merge neighbouring full bands.
    out = []
    for band in bands:
        if out and out[-1][0] == "full" and band[0] == "full":
            out[-1][2] = band[2]
        else:
            out.append(band)
    return [tuple(b) for b in out]


def collapse(txt):
    """Drawing page: keep the labels, drop the positional whitespace."""
    lines = [" ".join(l.split()) for l in txt.split("\n")]
    return "\n".join(l for l in lines if l)


def caption_for(region, blocks):
    """(kind, text): kind 0 is a 'Figure N' block touching the region (a caption);
    kind 1 is a short block centred just under it, which may or may not be one."""
    x0, y0, x1, y1 = region[:4]
    cands = []
    for b in blocks:
        if b["nlines"] > 3 or len(b["text"]) > 200:
            continue
        if b["x1"] < x0 - 10 or b["x0"] > x1 + 10:
            continue
        inside = b["y0"] >= y0 - 2 and b["y1"] <= y1 + 2
        gap = 0 if inside else (b["y0"] - y1 if b["y0"] >= y1 else y0 - b["y1"])
        if gap < 0 or gap > 40:
            continue
        if CAPTION.match(b["text"]):
            cands.append((0, gap, b["text"]))
        elif (not inside and b["y0"] >= y1 and gap <= 25 and len(b["text"]) <= 100
              and not b["text"].endswith(".") and abs((b["x0"] + b["x1"]) / 2 - (x0 + x1) / 2) < 0.15 * (x1 - x0)):
            cands.append((1, gap, b["text"]))
    cands.sort()
    return (cands[0][0], cands[0][2]) if cands else None


def ocr_words(png, psm="11"):
    """Tesseract words: [(line key, left, top, width, height, word, conf)] in
    pixels of the given image, words holding at least one alphanumeric."""
    raw = run_ocr(["tesseract", png, "-", "--psm", psm, "tsv"])
    if raw is None:
        return None
    out = []
    for row in raw.decode("utf-8", "replace").splitlines()[1:]:
        f = row.split("\t")
        if len(f) < 12 or f[0] != "5":
            continue
        try:
            conf = float(f[10])
        except ValueError:
            continue
        word = f[11].strip()
        if not any(c.isalnum() for c in word):
            continue
        out.append(((int(f[2]), int(f[3]), int(f[4])), int(f[6]), int(f[7]), int(f[8]), int(f[9]), word, conf))
    return out


def ocr_lines(png, is_text=None):
    """(lines of words with confidence >= OCR_CONF, words kept, words seen, mean
    confidence of all words seen), or None if tesseract is not installed.
    is_text(left, top, width, height) tells whether an OCR word (image pixels)
    lies on a text-layer word: that word is the text layer seen again, not
    figure content, and is left out."""
    if not shutil.which("tesseract"):
        return None
    words = ocr_words(png)
    if words is None:
        return [], 0, 0, -1.0   # timed out; the marker reports the mean as -1
    if is_text:
        words = [w for w in words if not is_text(w[1], w[2], w[3], w[4])]
    lines = {}
    for key, left, top, _, _, word, conf in words:
        if conf >= OCR_CONF:
            lines.setdefault(key, []).append((left, top, word))
    out = []
    for key in sorted(lines, key=lambda k: min(t for _, t, _ in lines[k])):
        out.append(" ".join(w for _, _, w in sorted(lines[key])))
    kept = sum(len(v) for v in lines.values())
    mean = sum(w[6] for w in words) / len(words) if words else 0.0
    return out, kept, len(words), mean


def ocr_stat(kept, seen, mean):
    if mean < 0:
        return f"tesseract timed out after {OCR_TIMEOUT} s"
    return f"{kept}/{seen} words >= {OCR_CONF}, mean confidence {mean:.0f}"


def ocr_region(pdf, pno, x0, y0, x1, y1, words=()):
    """OCR of a page region; words are the page's text-layer word boxes (pt),
    whose OCR readings are left out."""
    if not shutil.which("tesseract"):
        return None
    dpi = OCR_DPI
    sc = dpi / 72.0
    ox, oy = int(x0 * sc), int(y0 * sc)

    def is_text(l, t, w, h):
        wx0, wy0, wx1, wy1 = (ox + l) / sc, (oy + t) / sc, (ox + l + w) / sc, (oy + t + h) / sc
        area = max(1e-6, (wx1 - wx0) * (wy1 - wy0))
        for tx0, ty0, tx1, ty1, _ in words:
            ov = max(0.0, min(wx1, tx1) - max(wx0, tx0)) * max(0.0, min(wy1, ty1) - max(wy0, ty0))
            if ov >= 0.5 * area:
                return True
        return False
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, "r")
        run(["pdftoppm", "-r", str(dpi), "-f", str(pno), "-l", str(pno),
             "-x", str(ox), "-y", str(oy), "-W", str(int((x1 - x0) * sc) + 1), "-H", str(int((y1 - y0) * sc) + 1),
             "-png", "-singlefile", pdf, base])
        return ocr_lines(base + ".png", is_text if words else None)


def ocr_page(pdf, pno):
    if not shutil.which("tesseract"):
        return None
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, "p")
        run(["pdftoppm", "-r", str(OCR_DPI), "-f", str(pno), "-l", str(pno), "-png", "-singlefile", pdf, base])
        return ocr_lines(base + ".png")


def figure_markers(pdf, pno, regions, blocks):
    out = []
    for i, region in enumerate(regions, start=1):
        x0, y0, x1, y1, dens, labels, nearby = region
        ref = f"figure {i} on pdf page {pno} at {x0:.0f},{y0:.0f}-{x1:.0f},{y1:.0f} pt"
        cap = caption_for(region, blocks)
        if cap is None:
            cap = "caption: none"
        elif cap[0] == 0:
            cap = f'caption: "{cap[1]}"'
        else:
            cap = f'caption: none; nearest centred text below: "{cap[1]}"'
        lab = "text-layer labels: " + (" | ".join(labels) if labels else "none")
        if nearby:
            lab += " | nearby labels: " + " | ".join(nearby)
        ocr = ocr_region(pdf, pno, x0, y0, x1, y1, [wd for b in blocks for wd in b["words"]])
        if ocr is None:
            out.append(f"<!-- {ref} | {cap} | {lab} | OCR: tesseract not installed -->")
        elif not ocr[0]:
            out.append(f"<!-- {ref} | {cap} | {lab} | OCR: no legible text ({ocr_stat(*ocr[1:])}) -->")
        else:
            out.append(f"<!-- {ref} | {cap} | {lab} | OCR text follows (tesseract, unverified; {ocr_stat(*ocr[1:])}) -->")
            out.extend(ocr[0])
            out.append(f"<!-- end of figure {i} -->")
    return out


def render_page_png(pdf, pno, dpi, td, name):
    base = os.path.join(td, name)
    run(["pdftoppm", "-r", str(dpi), "-f", str(pno), "-l", str(pno), "-png", "-singlefile", pdf, base])
    return base + ".png"


def strip_word(w):
    return re.sub(r"^[^\w]+|[^\w]+$", "", w)


def ligature_notes(pdf, pno, blocks):
    """Text-layer words whose OCR reading is the same word with the f of a
    fi/fl/ff ligature restored. Returns [(text-layer word, restored word)]."""
    if not shutil.which("tesseract"):
        return []
    with tempfile.TemporaryDirectory() as td:
        words = ocr_words(render_page_png(pdf, pno, OCR_DPI, td, "l"))
    if words is None:
        return []
    sc = 72.0 / OCR_DPI
    ocr = [(l * sc, t * sc, (l + w) * sc, (t + h) * sc, strip_word(word), conf) for _, l, t, w, h, word, conf in words]
    readings = {}
    for b in blocks:
        for x0, y0, x1, y1, text in b["words"]:
            tw = strip_word(text)
            if len(tw) < 3 or not tw.isalpha() or "-" in text:
                continue
            for ox0, oy0, ox1, oy1, ow, conf in ocr:
                ov = max(0.0, min(x1, ox1) - max(x0, ox0)) * max(0.0, min(y1, oy1) - max(y0, oy0))
                if ov >= 0.5 * min((x1 - x0) * (y1 - y0), (ox1 - ox0) * (oy1 - oy0)):
                    readings.setdefault(tw, []).append((ow, conf))
                    break
    out = []
    for tw, reads in readings.items():
        fixed = {ow for ow, conf in reads if conf >= LIG_CONF and ow != tw and len(ow) > len(tw)
                 and LIG.sub("", ow) == LIG.sub("", tw) and ow.count("f") > tw.count("f")}
        if len(fixed) == 1 and not any(ow == tw for ow, _ in reads):
            out.append((tw, fixed.pop()))
    return sorted(out)


def drawn_marker_lines(pdf, pno, W, H, blocks, regions):
    """Text lines that have a small ink mark just left of their start, outside
    every text box and every figure region: a bullet the text layer lost."""
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, "m")
        run(["pdftoppm", "-gray", "-r", str(MARK_DPI), "-f", str(pno), "-l", str(pno), "-singlefile", pdf, base])
        w, h, px = figures.read_pgm(base + ".pgm")
    sx, sy = w / W, h / H
    ink = bytearray(1 if v < MARK_DARK else 0 for v in px)
    for b in blocks:
        for x0, y0, x1, y1, _ in b["words"]:
            X0, X1 = max(0, int(x0 * sx) - 1), min(w, int(x1 * sx) + 2)
            if X1 <= X0:
                continue
            for y in range(max(0, int(y0 * sy) - 1), min(h, int(y1 * sy) + 2)):
                ink[y * w + X0:y * w + X1] = bytes(X1 - X0)
    words = [wd for b in blocks for wd in b["words"]]
    out = []
    for b in blocks:
        for x0, y0, x1, y1, text in b["lines"]:
            if not re.search(r"[A-Za-z0-9]", text):
                continue
            if any(x0 < r[2] and x1 > r[0] and y0 < r[3] and y1 > r[1] for r in regions):
                continue
            # A list marker is the leftmost thing on its row; a mark with text
            # further left on the same row is an inline icon inside a sentence.
            if any(wx1 <= x0 and min(y1, wy1) - max(y0, wy0) > 0.5 * (y1 - y0) for wx0, wy0, wx1, wy1, _ in words):
                continue
            X0, X1 = int((x0 - MARK_REACH) * sx), int((x0 - 1.5) * sx)
            Y0, Y1 = int(y0 * sy) - 2, int(y1 * sy) + 3
            if X0 < 0 or Y0 < 0 or Y1 > h or X1 - X0 < 3:
                continue
            lh = (y1 - y0) * sy
            marks, seen, reject = 0, set(), False
            for yy in range(Y0, Y1):
                for xx in range(X0, X1):
                    i = yy * w + xx
                    if not ink[i] or i in seen:
                        continue
                    # Grow the component inside the strip's x-range but freely in y
                    # (within two line heights): a bullet stays small, a bar, box
                    # border or hatch stripe runs on.
                    comp, stack = [], [i]
                    seen.add(i)
                    lo, hi = max(0, int(Y0 - 2 * lh)), min(h, int(Y1 + 2 * lh))
                    while stack:
                        j = stack.pop()
                        comp.append(j)
                        jy, jx = divmod(j, w)
                        for dy in (-1, 0, 1):
                            for dx in (-1, 0, 1):
                                ny, nx = jy + dy, jx + dx
                                if lo <= ny < hi and X0 <= nx < X1:
                                    k = ny * w + nx
                                    if ink[k] and k not in seen:
                                        seen.add(k)
                                        stack.append(k)
                    xs = [j % w for j in comp]
                    ys = [j // w for j in comp]
                    cw, ch = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
                    if ch > lh * MARK_SIZE + 1 or min(xs) == X0 or cw > lh * MARK_SIZE + 1:
                        reject = True
                    elif cw >= 2 and y0 * sy <= (min(ys) + max(ys)) / 2 <= y1 * sy:
                        marks += 1
            if reject or marks != 1:
                continue
            # An enclosure (circle, box) around a label has ink right of the line too;
            # a drawing beside the line has ink further left on the same row. A bullet
            # has neither.
            ys = range(int(y0 * sy), int(y1 * sy) + 1)
            R0, R1 = int((x1 + 1.5) * sx), min(w, int((x1 + MARK_REACH) * sx))
            L0, L1 = max(0, int((x0 - 3 * MARK_REACH) * sx)), X0
            if any(ink[yy * w + xx] for yy in ys for xx in range(R0, R1)) or any(ink[yy * w + xx] for yy in ys for xx in range(L0, L1)):
                continue
            out.append(text)
    return out


def extract_page(pdf, pno, geometry, pgm=None, keys=frozenset(), nouni=False):
    """Return (printed label, header texts, footer texts, markdown text).
    With nouni (a font without a ToUnicode map is used on the page) the page
    is OCR'd for dropped ligature glyphs."""
    W, H, blocks = geometry
    if not blocks:
        ocr = ocr_page(pdf, pno)
        parts = []
        if ocr and ocr[0]:
            parts.append(f"<!-- no text layer; page OCR text follows (tesseract, unverified; {ocr_stat(*ocr[1:])}) -->\n" + "\n".join(ocr[0]))
        if pgm:
            Wp, Hp = figures_page_size(pgm)
            parts.extend(figure_markers(pdf, pno, figures.regions(pgm, Wp, Hp, []), []))
        return None, [], [], "\n\n".join(parts)
    label = printed_label(blocks, W, H, keys)
    parts = []
    xlim = tab_limit(blocks, W)
    blocks = [b for b in blocks if b["x0"] < xlim]
    blocks, head, foot, y_top, y_bottom = split_furniture(blocks, W, H, keys)
    regions = figures.regions(pgm, W, H, blocks) if pgm else []
    notes = []
    if nouni:
        ligs = ligature_notes(pdf, pno, blocks)
        if ligs:
            notes.append("<!-- ligatures: a font without a ToUnicode map dropped a glyph; words restored from the rendered page "
                         f"(tesseract, confidence >= {LIG_CONF}): " + ", ".join(f"{a}->{b}" for a, b in ligs) + " -->")
    marks = drawn_marker_lines(pdf, pno, W, H, blocks, regions)
    if marks:
        notes.append("<!-- list markers drawn on the page, not in the text layer (from the rendered page): "
                     + " | ".join('"' + m[:60].replace('"', "'") + '"' for m in marks) + " -->")
    for kind, y0, y1, xsplit in bands_for(blocks, W, H):
        # Stay inside the body zone; pad slightly so glyph edges are not clipped.
        yy0, yy1 = max(y_top, y0 - 0.5), min(y_bottom, y1 + 0.5)
        if yy1 - yy0 < 1:
            continue
        if kind == "full":
            t = tidy(crop_text(pdf, pno, 0, yy0, xlim, yy1 - yy0))
            if t:
                parts.append(t)
        else:
            l = tidy(crop_text(pdf, pno, 0, yy0, xsplit, yy1 - yy0))
            r = tidy(crop_text(pdf, pno, xsplit, yy0, xlim - xsplit, yy1 - yy0))
            for t in (l, r):
                if t:
                    parts.append(t)
    text = "\n\n".join(parts)
    body = text.replace("\n", "")
    if body and sum(c == " " for c in body) / len(body) > SPARSE:
        text = "<!-- drawing page: text layer holds figure labels only; positions dropped -->\n" + collapse(text)
    if regions:
        text = text + "\n\n" + "\n".join(figure_markers(pdf, pno, regions, blocks))
    if notes:
        text = "\n".join(notes) + "\n\n" + text
    return label, head, foot, text


def figures_page_size(pgm):
    w, h, _ = figures.read_pgm(pgm)
    return w * 72.0 / figures.DPI, h * 72.0 / figures.DPI


def page_ranges(nums):
    nums = sorted(set(nums))
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:] + [None]:
        if n is not None and n == prev + 1:
            prev = n
            continue
        out.append(f"{start}" if start == prev else f"{start}-{prev}")
        if n is not None:
            start = prev = n
    return ", ".join(out)


def nouni_fonts(pdf):
    """Families of fonts without a ToUnicode map (pdffonts)."""
    info = run(["pdffonts", pdf]).decode("utf-8", "replace").splitlines()
    if len(info) <= 2:
        return set()
    c_type, c_uni = info[0].index("type"), info[0].index("uni")
    return {re.sub(r"^[A-Z]{6}\+", "", r[:c_type].strip()) for r in info[2:] if len(r) > c_uni and r[c_uni:c_uni + 3].strip() == "no"}


def font_report(pdf):
    """(report lines, pages using a font without a ToUnicode map). The report
    lists fonts that are not standard text faces, with the glyphs they produce
    and the pages they occur on, and fonts without a ToUnicode map."""
    lines = []
    try:
        raw = run(["pdftohtml", "-xml", "-i", "-stdout", pdf])
        root = ET.fromstring(CTRL.sub("", raw.decode("utf-8", "replace")))
    except Exception:
        return ["<!-- font check: pdftohtml -xml failed; fonts not inspected -->"], set()
    nouni = nouni_fonts(pdf)
    nouni_pages = set()
    fam_of, glyphs, pages, unmapped = {}, {}, {}, {}
    for pno, page in enumerate(root.iter("page"), start=1):
        for fs in page.iter("fontspec"):
            fam_of[fs.get("id")] = re.sub(r"^[A-Z]{6}\+", "", fs.get("family", ""))
        for t in page.iter("text"):
            fam = fam_of.get(t.get("font"), "?")
            txt = "".join(t.itertext())
            if fam in nouni and txt.strip():
                nouni_pages.add(pno)
            for c in txt:
                if c == "\ufffd":
                    unmapped.setdefault("U+FFFD (glyph with no Unicode mapping)", set()).add(pno)
                elif 0xE000 <= ord(c) <= 0xF8FF:
                    unmapped.setdefault(f"U+{ord(c):04X} (private-use code from {fam})", set()).add(pno)
            if is_text_face(fam):
                continue
            chars = {c for c in txt if not c.isspace()}
            if not chars:
                continue
            glyphs.setdefault(fam, set()).update(chars)
            pages.setdefault(fam, set()).add(pno)
    for fam in sorted(glyphs):
        g = "".join(sorted(glyphs[fam]))
        g = g if len(g) <= 60 else g[:60] + "…"
        lines.append(f'<!-- font check: {fam} is not a standard text face; glyphs "{g}" on pages {page_ranges(pages[fam])}. Verify against the rendered page before trusting or mapping. -->')
    for code in sorted(unmapped):
        lines.append(f"<!-- font check: {code} on pages {page_ranges(unmapped[code])}; the character carries no meaning as text, read the rendered page -->")
    if nouni:
        lines.append(f"<!-- font check: no ToUnicode map in {', '.join(sorted(nouni))}; ligatures (fi, fl) or special glyphs may be missing from the text"
                     f" (pages {page_ranges(nouni_pages) if nouni_pages else 'none'} checked against the rendered page) -->")
    return lines, nouni_pages


def main(pdf, out):
    n = page_count(pdf)
    pages = blocks_by_page(pdf)
    keys = furniture_keys(pages)
    chunks, nouni_pages = font_report(pdf)
    with tempfile.TemporaryDirectory() as td:
        pgms = figures.render(pdf, td)
        for pno in range(1, n + 1):
            label, head, foot, text = extract_page(pdf, pno, pages.get(pno, (0.0, 0.0, [])), pgms.get(pno), keys,
                                                   nouni=pno in nouni_pages)
            marker = f"<!-- pdf page {pno}"
            if label:
                marker += f" | printed page {label}"
            if head:
                marker += " | header: " + " / ".join(head)
            if foot:
                marker += " | footer: " + " / ".join(foot)
            chunks.append(marker + " -->\n\n" + (text if text else "(no text layer on this page)"))
            print(f"page {pno}/{n}", file=sys.stderr, end="\r")
    print(file=sys.stderr)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n\n".join(chunks) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
