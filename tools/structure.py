#!/usr/bin/env python3
"""Turn a verbatim extraction (extracted/<case>/<name>.md) into a structured
markdown document (structured/<case>/<name>.md).

Usage: structure.py <extracted.md> <source.pdf> <out.md> [<review.md>]

What it does, all by document-independent rules
- Headings: lines whose font size is clearly above the body size, or whole
  bold lines, read from the PDF with pdftohtml -xml; levels follow size.
- Paragraphs: lines joined, end-of-line hyphenation repaired, a paragraph
  that runs over a page break joined (the page marker moves after it).
- Lists: bullet and numbered lines become markdown list items.
- Tables: blocks of lines that share column gaps become markdown tables;
  cells wrapped over several lines are merged. A block that does not split
  cleanly is kept as a fenced block with its alignment intact.
- Removed: table-of-contents lines (dot leaders to a page number) and
  lines holding a marketing or legal boilerplate phrase (listed in
  boilerplate.txt next to this script). Every removed line still exists in
  the extraction.
- Addenda: a page announcing itself as an addendum, erratum or supplement
  is moved to the top under "Addenda and corrections", with its page cite.
- Sub/superscripts: pairs seen in the font sizes are listed per page and
  applied where the flattened form occurs as a whole word on that page.
- Glyphs of fonts the font check flags are replaced from glyphs.txt (a table
  verified against the rendered page, keyed by font family); a glyph without
  an entry stays. A run of one such glyph counts as one.
- Page notes written by stage 1 from the rendered page are applied: words
  with a restored ligature replace their broken form on that page; lines
  with a drawn list marker become list items.
- OCR text of a figure is kept only when tesseract's word statistics for
  that figure pass the floor (OCR_SHARE, OCR_MEAN); the marker says so.
- Review (optional, from review.py): a figure's OCR text is replaced by the
  model's transcription, flagged as text from the page image; a verified
  reading is marked so; a table is emitted as the model re-arranged it, its
  words unchanged. Glyph candidates in the review file are not applied.
- Omitted: a section whose heading is a title in omit_sections.txt (legal,
  warranty, trademark and regulatory boilerplate), from the heading to the
  next heading of any level; a marker with the page cite stands in for it.
- Everything else, including page markers and figure markers, is kept.
  Text is never rewritten beyond joining lines.

Requires poppler-utils (pdftohtml).
"""
import fnmatch
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True   # no __pycache__ in the repository
from pdf_to_md import is_text_face  # noqa: E402
CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
PAGE_MARK = re.compile(r"^<!-- pdf page (\d+)(?: \| printed page ([^|]+?))?(?: \| header: (.*?))?(?: \| footer: (.*?))? -->$")
FIG_START = re.compile(r"^<!-- figure (\d+) on pdf page \d+ .* -->$")
FIG_END = re.compile(r"^<!-- end of figure (\d+) -->$")
BULLET = re.compile(r"^(\s*)([•●○◦❍■□▪➥➢►▶✓✔\-–—*]+|[①-⑳❶-❿⓫-⓴]|\(?\d{1,3}[.)]|[a-z][.)]|\d{1,3}\)|[ivx]{1,4}[.)])\s+(\S.*)$")
TOC_LINE = re.compile(r"\.{4,}\s*[\divx]+\s*$|(\s\.\s?){4,}\s*[\divx]+\s*$|[—–-]\s*page\s+\d+\s*$", re.I)
ADDENDUM = re.compile(r"\b(addend[au]m|errat[au]m?|supplement|additional (feature )?information|corrections?)\b", re.I)
HEAD_BIG = 1.15      # size ratio to the body size above which a line is a heading
HEAD_MAXLEN = 120
GAP = re.compile(r" {2,}")
KEYVAL = re.compile(r"^\s*[A-Za-z][^:]{1,50}:(\s|$)")
DASH_ITEM = re.compile(r"^\s*[—–](?=\S)")   # em/en dash glued to the item, common in datasheets
MARKS = "■□◇◆●•○▪▶►➥✓✔❍"                     # publisher level markers in front of headings
OCR_SHARE = 0.4   # share of a figure's OCR words that must pass the word threshold (below: callout digits, pixel fonts, textures)
OCR_MEAN = 45.0   # mean word confidence a figure's OCR must reach
OCR_STAT = re.compile(r"(\d+)/(\d+) words >= \d+, mean confidence (\d+)")
LIG_NOTE = re.compile(r"^<!-- ligatures: .*?: (.*) -->$")
MARK_NOTE = re.compile(r'^<!-- list markers drawn on the page, not in the text layer \(from the rendered page\): (.*) -->$')
OMIT_MARK = re.compile(r'^<!-- omitted: "(.*)" \(pdf pages? ([\d-]+); (\d+) lines\)')
REV_FIG = re.compile(r"^<!-- reviewed figure (\d+) on pdf page (\d+): (\w+)(.*) -->$")
REV_TABLE = re.compile(r'^<!-- reviewed table on pdf page (\d+), first row "(.*)": (\w+)(.*) -->$')


def run(args):
    return subprocess.run(args, check=True, capture_output=True).stdout


# ----------------------------------------------------------------- font info

def load_glyphs(pdf):
    """{font family: [(key, replacement)]} from glyphs.txt, longest keys first;
    entries restricted to another source file are left out."""
    path = os.path.join(HERE, "glyphs.txt")
    table = {}
    if not os.path.exists(path):
        return table
    base = os.path.basename(pdf)
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 4:
                continue
            fam, key, rep = cols[0], cols[1], cols[2]
            if len(cols) >= 5 and cols[4].strip() and cols[4].strip() != base:
                continue
            if re.fullmatch(r"U\+[0-9A-Fa-f]{4,6}", key):
                key = chr(int(key[2:], 16))
            table.setdefault(fam, []).append((key, rep))
    for fam in table:
        table[fam].sort(key=lambda kr: -len(kr[0]))
    return table


def glyph_tokens(text, entries):
    """Split a flagged-font fragment into (glyph run key, replacement) tokens,
    longest table key first; an unmapped glyph maps to itself."""
    out, i = [], 0
    while i < len(text):
        if text[i].isspace():
            i += 1
            continue
        for key, rep in entries:
            if text.startswith(key, i):
                out.append((key, rep))
                i += len(key)
                break
        else:
            out.append((text[i], text[i]))
            i += 1
    return out


def map_glyphs(text, entries):
    return "".join(rep for _, rep in glyph_tokens(text, entries))


def glyph_sub(reps):
    def sub(m):
        out, k = [], 0
        pos = m.start()
        for g in range(1, len(m.groups()) + 1):
            out.append(m.string[pos:m.start(g)])
            rep = reps[k]
            nxt = m.string[m.end(g):m.end(g) + 1]
            if rep and nxt and nxt.isalnum() and not rep[-1].isspace():
                rep += " "
            out.append(rep)
            pos = m.end(g)
            k += 1
        out.append(m.string[pos:m.end()])
        return "".join(out)
    return sub


def row_patterns(frags):
    """Regexes for the body line of a row holding flagged-font fragments, each
    with its substitution: first the whole row, then each glyph fragment with
    one neighbouring word as context (for a body line that does not hold the
    whole row). A glyph key may be repeated in the text layer (a pictogram
    drawn as a wide and a thin glyph); plain words are matched with flexible
    spacing."""
    elems = []   # ("g", [(pattern, rep)]) or ("w", [words])
    for text, fam, entries in frags:
        if entries is None:
            if text.split():
                elems.append(("w", text.split()))
        else:
            toks = [(r"(?<!\w)(" + "".join(re.escape(c) + "+" for c in key) + ")", rep) for key, rep in glyph_tokens(text, entries)]
            if toks:
                elems.append(("g", toks))
    if not any(k == "g" for k, _ in elems):
        return []
    out = []
    parts, reps = [], []
    for kind, val in elems:
        if kind == "w":
            parts.append(r"\s*".join(re.escape(w) for w in val))
        else:
            parts.extend(p for p, _ in val)
            reps.extend(r for _, r in val)
    full = r"\s*".join(parts)
    if not any(k == "w" for k, _ in elems):
        # A row of glyphs only (callouts on a drawing) must be the whole line, or a
        # token of its own between column gaps; never part of a word.
        out.append((re.compile(r"^\s*" + full + r"\s*$"), glyph_sub(reps)))
        full = r"(?:^|(?<=\s\s))" + full + r"(?=\s\s|\s*$)"
    out.append((re.compile(full), glyph_sub(reps)))
    for i, (kind, val) in enumerate(elems):
        if kind != "g":
            continue
        pats = [p for p, _ in val]
        rs = [r for _, r in val]
        if i + 1 < len(elems) and elems[i + 1][0] == "w":
            pat = r"\s*".join(pats + [re.escape(elems[i + 1][1][0])])
        elif i > 0 and elems[i - 1][0] == "w":
            pat = r"\s*".join([re.escape(elems[i - 1][1][-1])] + pats)
        else:
            continue
        out.append((re.compile(pat), glyph_sub(rs)))
    return out


def xml_pages(pdf, glyphs=None):
    """{page: [run dict(text, size, bold, top, siblings)]} from pdftohtml -xml,
    plus {page: [(pattern, sub)]} for rows holding flagged-font glyphs.
    A run is text on one row with no large gap inside it; siblings counts the
    other runs on the same row (other column, or other table cells)."""
    glyphs = glyphs or {}
    try:
        raw = run(["pdftohtml", "-xml", "-i", "-stdout", pdf])
        root = ET.fromstring(CTRL.sub("", raw.decode("utf-8", "replace")))
    except Exception:
        return {}, {}
    out, sizes, fams, patterns = {}, {}, {}, {}
    for pno, page in enumerate(root.iter("page"), start=1):
        sizes.update({fs.get("id"): float(fs.get("size", 0)) for fs in page.iter("fontspec")})
        fams.update({fs.get("id"): re.sub(r"^[A-Z]{6}\+", "", fs.get("family", "")) for fs in page.iter("fontspec")})
        frags = []
        for t in page.iter("text"):
            txt = "".join(t.itertext())
            top = float(t.get("top", 0))
            if not txt.strip() or top < 0:
                continue
            bold = t.find("b") is not None and "".join(t.find("b").itertext()).strip() == txt.strip()
            fam = fams.get(t.get("font"), "")
            entries = glyphs.get(fam, []) if fam and not is_text_face(fam) else None
            frags.append(dict(text=txt, size=sizes.get(t.get("font"), 0.0), bold=bold, top=top,
                              left=float(t.get("left", 0)), width=float(t.get("width", 0)),
                              height=float(t.get("height", 0)), fam=fam, entries=entries))
        frags.sort(key=lambda f: (f["top"], f["left"]))
        rows, cur = [], []
        for f in frags:
            if cur and abs(f["top"] - cur[-1]["top"]) > max(3, 0.4 * cur[-1]["height"]):
                rows.append(cur)
                cur = []
            cur.append(f)
        if cur:
            rows.append(cur)
        page_runs = []
        for row in rows:
            row.sort(key=lambda f: f["left"])
            runs, r = [], [row[0]]
            for a, b in zip(row, row[1:]):
                if b["left"] - (a["left"] + a["width"]) > 20:
                    runs.append(r)
                    r = []
                r.append(b)
            runs.append(r)
            for r in runs:
                shown = lambda f: map_glyphs(f["text"], f["entries"]) if f["entries"] is not None else f["text"]
                text = shown(r[0])
                for a, b in zip(r, r[1:]):
                    text += (" " if b["left"] - (a["left"] + a["width"]) > 1 else "") + shown(b)
                words = [f for f in r if len(f["text"].strip()) >= 3]
                main = words[0] if words else max(r, key=lambda f: len(f["text"].strip()))
                page_runs.append(dict(text=text.strip(), size=main["size"],
                                      bold=all(f["bold"] for f in r), top=r[0]["top"], left=r[0]["left"],
                                      siblings=len(runs) - 1))
                if any(f["entries"] is not None for f in r):
                    patterns.setdefault(pno, []).extend(row_patterns([(f["text"], f["fam"], f["entries"]) for f in r]))
        out[pno] = page_runs
    return out, patterns


def apply_glyphs(lines, patterns):
    """Substitute flagged-font glyphs in body lines, page by page."""
    if not patterns:
        return lines
    out = []
    for l in lines:
        if not l.startswith("<!--"):
            for pat, sub in patterns:
                l = pat.sub(sub, l)
        out.append(l)
    return out


def body_size(pages):
    c = Counter()
    for lines in pages.values():
        for l in lines:
            c[round(l["size"])] += len(l["text"])
    return c.most_common(1)[0][0] if c else 0


CONTENTS = re.compile(r"^(table of )?contents\b", re.I)


def continues_below(l, lines):
    """True when the next run under this one, in the same column, starts lowercase
    and is set smaller or not bold: the line is the lead-in of a paragraph, not a
    heading (a heading wrapped onto a second line keeps its size and weight)."""
    below = [o for o in lines if o["top"] > l["top"] + 2 and abs(o["left"] - l["left"]) < 40]
    if not below:
        return False
    nxt = min(below, key=lambda o: o["top"])
    if nxt["top"] - l["top"] > l["size"] * 2.2 or not re.match(r"^[a-z]", nxt["text"]):
        return False
    return nxt["size"] < l["size"] * 0.95 or (l["bold"] and not nxt["bold"])


def in_bold_block(l, lines):
    """True when the run just above, in the same column, is bold or a bullet item:
    this bold line continues a bold block rather than opening a section."""
    above = [o for o in lines if o["top"] < l["top"] - 2 and abs(o["left"] - l["left"]) < 40]
    if not above:
        return False
    prv = max(above, key=lambda o: o["top"])
    return l["top"] - prv["top"] <= l["size"] * 2.2 and (prv["bold"] or bool(BULLET.match(prv["text"])))


def heading_candidates(pages):
    """{page: [(text, level)]} with wrapped headings merged."""
    base = body_size(pages)
    if not base:
        return {}
    cands = {}
    for pno, lines in pages.items():
        margins = Counter(round(l["left"] / 5) * 5 for l in lines)
        margins = {m for m, c in margins.items() if c >= 3}
        lst = []
        for l in lines:
            t = l["text"]
            if len(t) > HEAD_MAXLEN or not re.search(r"[A-Za-z]", t) or TOC_LINE.search(t):
                continue
            bullet = BULLET.match(t) and not re.match(r"^\d{1,3}(\.\d{1,3})*[.)]?\s+[A-Z]", t)
            if continues_below(l, lines):
                continue
            if l["size"] >= base * HEAD_BIG:
                lst.append(dict(text=t, size=round(l["size"]), top=l["top"], left=l["left"], big=True))
            elif l["bold"] and not bullet and l["size"] >= base * 0.9 and not t.endswith((".", ":", "-", ",")) \
                    and 4 <= len(t) <= 100 and not l["siblings"] and not in_bold_block(l, lines) \
                    and (len(t.split()) >= 2 or re.search(r"[a-z]", t)) \
                    and any(abs(l["left"] - m) <= 8 for m in margins):
                lst.append(dict(text=t, size=round(l["size"]), top=l["top"], left=l["left"], big=False))
        # merge a heading wrapped over consecutive, left-aligned lines of the same size
        # (a heading in the other column may sit between them in reading order)
        merged = []
        for h in lst:
            prev = None
            for cand in merged[-3:]:
                if cand["size"] == h["size"] and cand["big"] == h["big"] and abs(cand["left"] - h["left"]) < 30 \
                        and h["size"] * 0.8 <= h["top"] - cand["top"] <= h["size"] * 2.2 and not re.match(r"^\d", h["text"]):
                    prev = cand
            if prev:
                prev["text"] += " " + h["text"]
                prev["top"] = h["top"]
            else:
                merged.append(dict(h))
        # a bold paragraph is not a heading: merged bold text that is long or holds a sentence break
        merged = [h for h in merged if h["big"] or (len(h["text"]) <= 80 and ". " not in h["text"])]
        merged = [h for h in merged if not CONTENTS.match(norm(h["text"]))]
        cands[pno] = merged
    # levels from the sizes used by headings on more than one page (a cover title does not set a level)
    use = {}
    for pno, lst in cands.items():
        for h in lst:
            if h["big"]:
                use.setdefault(h["size"], set()).add(pno)
    ranked = sorted((sz for sz, pp in use.items() if len(pp) >= 2), reverse=True)[:4]
    if not ranked:
        ranked = sorted(use, reverse=True)[:4]

    def level_of(size):
        for i, sz in enumerate(ranked):
            if size >= sz:
                return i + 1
        return len(ranked) + 1

    out = {}
    for pno, lst in cands.items():
        out[pno] = [(h["text"], 1 + (level_of(h["size"]) if h["big"] else len(ranked) + 1)) for h in lst]
    return out


def subsup_from_xml(pdf):
    """{page: [(flattened, marked)]} for a small span glued to a normal one, e.g. IP -> I_P."""
    try:
        raw = run(["pdftohtml", "-xml", "-i", "-stdout", pdf])
        root = ET.fromstring(CTRL.sub("", raw.decode("utf-8", "replace")))
    except Exception:
        return {}
    out = {}
    for pno, page in enumerate(root.iter("page"), start=1):
        sizes = {fs.get("id"): float(fs.get("size", 0)) for fs in page.iter("fontspec")}
        frags = []
        for t in page.iter("text"):
            txt = "".join(t.itertext())
            if not txt.strip():
                continue
            frags.append((float(t.get("top", 0)), float(t.get("left", 0)), float(t.get("width", 0)),
                          float(t.get("height", 0)), sizes.get(t.get("font"), 0.0), txt))
        frags.sort(key=lambda f: (f[0], f[1]))
        pairs = []
        for i, f in enumerate(frags):
            for g in frags[max(0, i - 6):i + 7]:
                if g is f or not g[4] or not f[4]:
                    continue
                # g is a small fragment right after f, vertically overlapping, shifted
                if g[4] <= 0.8 * f[4] and abs(g[1] - (f[1] + f[2])) <= 3 and \
                        g[0] < f[0] + f[3] and g[0] + g[3] > f[0]:
                    base = f[5].split()[-1] if f[5].split() else ""
                    small = g[5].strip()
                    if not base or not small or len(small) > 8 or " " in small or small in ("®", "™", "©"):
                        continue
                    if not re.search(r"[A-Za-z0-9]$", base):
                        continue
                    mark = "^" if g[0] + g[3] / 2 < f[0] + f[3] / 2 else "_"
                    pairs.append((base + small, f"{base}{mark}{small}"))
        if pairs:
            out[pno] = sorted(set(pairs))
    return out


# ------------------------------------------------------------- extraction md

def parse_extraction(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    notes, pages, cur = [], [], None
    for line in lines:
        m = PAGE_MARK.match(line)
        if m:
            cur = dict(pno=int(m.group(1)), printed=m.group(2), header=m.group(3), footer=m.group(4), lines=[])
            pages.append(cur)
        elif cur is None:
            if line.strip():
                notes.append(line)
        else:
            cur["lines"].append(line)
    return notes, pages


def ocr_passes(marker):
    """None when the marker carries no OCR statistics, else whether the figure's
    OCR clears the floor: enough words above the word threshold and a high
    enough mean confidence (an LCD pixel font or a low-resolution scan fails)."""
    m = OCR_STAT.search(marker)
    if not m:
        return None
    kept, seen, mean = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return seen > 0 and kept / seen >= OCR_SHARE and mean >= OCR_MEAN


def split_figures(lines):
    """Separate body lines from figure blocks. OCR text below the floor is
    left out and the marker says so."""
    body, figs, i = [], [], 0
    while i < len(lines):
        l = lines[i]
        m = FIG_START.match(l)
        if m:
            block = [l]
            if "OCR text follows" in l:
                i += 1
                while i < len(lines) and not FIG_END.match(lines[i]):
                    block.append(lines[i])
                    i += 1
                if i < len(lines):
                    block.append(lines[i])
                if ocr_passes(l) is False:
                    block = [l.replace("OCR text follows (tesseract, unverified; ", "OCR below floor, text not used (")]
            figs.append(block)
        elif l.startswith("<!-- no text layer; page OCR text follows") and ocr_passes(l) is False:
            body.append(l.replace("page OCR text follows (tesseract, unverified; ", "page OCR below floor, text not used ("))
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("<!--"):
                i += 1
            continue
        else:
            body.append(l)
        i += 1
    return body, figs


def page_notes(lines):
    """(ligature pairs, drawn-marker line prefixes) from stage 1's page notes."""
    ligs, marks = [], []
    for l in lines:
        m = LIG_NOTE.match(l)
        if m:
            ligs.extend(tuple(pair.split("->", 1)) for pair in m.group(1).split(", ") if "->" in pair)
        m = MARK_NOTE.match(l)
        if m:
            marks.extend(re.findall(r'"([^"]*)"', m.group(1)))
    return ligs, marks


def apply_ligatures(lines, ligs):
    for broken, fixed in ligs:
        pat = re.compile(r"(?<![\w])" + re.escape(broken) + r"(?![\w])")
        lines = [pat.sub(fixed, l) if not l.startswith("<!--") else l for l in lines]
    return lines


def apply_marks(lines, marks):
    """Prefix a bullet to the body line that starts with each noted line text
    (at the line start or after a column gap); each note is used once."""
    pending = [re.compile(r"\s+".join(re.escape(w) for w in pre.split())) for pre in marks if pre.split()]
    out = []
    for l in lines:
        if pending and not l.startswith("<!--"):
            for k, pat in enumerate(pending):
                m = pat.search(l)
                if m and (m.start() == 0 or l[:m.start()].endswith("  ") or not l[:m.start()].strip()):
                    l = l[:m.start()] + "• " + l[m.start():]
                    del pending[k]
                    break
        out.append(l)
    return out


# ------------------------------------------------------------------ blocks

def norm(s):
    """Comparison key: marker glyphs, chapter numbers and spacing removed."""
    s = re.sub(r"^[\s■□◇◆●•○▪▶►➥✓✔]+", "", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    s = re.sub(r"^\d{1,2}(\.\d{1,2})*\s+|\s+\d{1,2}$", "", s)
    return s


def same_heading(body_key, cand_key):
    """The body line may carry up to three leading glyph characters the XML
    rendered differently (e.g. a doubled dingbat)."""
    return body_key == cand_key or (body_key.endswith(cand_key) and len(body_key) - len(cand_key) <= 3)


def has_gap(line):
    return bool(GAP.search(line.strip()))


def indent(l):
    return len(l) - len(l.lstrip(" "))


def table_span(block):
    """(start, end) of the run of table rows inside a block, or None. A row has
    an internal column gap, or is an indented continuation of a wrapped cell.
    Lines before the run are a title, lines after are notes."""
    base = min(indent(l) for l in block if l.strip())
    rowlike = [has_gap(l) or indent(l) - base >= 2 for l in block]
    idx = [i for i, r in enumerate(rowlike) if r]
    if sum(1 for l in block if has_gap(l)) < 2:
        return None
    start, end = idx[0], idx[-1] + 1
    while start < end and not has_gap(block[start]):
        start += 1
    if sum(1 for l in block[start:end] if has_gap(l)) < 0.3 * (end - start):
        return None
    rows = [l.rstrip() for l in block[start:end] if l.strip()]
    return (start, end) if column_cuts(rows) else None


def column_cuts(rows, share=0.9):
    """Character ranges that are blank in the rows having text on both sides of
    them: the column gaps. Rows that end before a gap, or start after it, do
    not vote, so wrapped continuation lines cannot fake a gap inside a column."""
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r.ljust(width) for r in rows]
    stripped = [r.rstrip() for r in rows]
    first = [len(r) - len(r.lstrip(" ")) for r in rows]
    last = [len(r) for r in stripped]
    blank = []
    for i in range(width):
        voters = [r for r, f, l in zip(rows, first, last) if f < i < l - 1]
        ok = [r for r in voters if r[i] == " "]
        blank.append(len(voters) >= 2 and len(ok) >= share * len(voters))
    cuts, i = [], 0
    while i < width:
        if blank[i]:
            j = i
            while j < width and blank[j]:
                j += 1
            if j - i >= 2 and i > 0 and j < width:
                cuts.append((i, j))
            i = j
        else:
            i += 1
    kept = []
    for k, (a, b) in enumerate(cuts):
        left_from = cuts[k - 1][1] if k else 0
        right_to = cuts[k + 1][0] if k + 1 < len(cuts) else width
        left = sum(1 for r in rows if r[left_from:a].strip())
        right = sum(1 for r in rows if r[b:right_to].strip())
        if left >= 2 and right >= 2:
            kept.append((a, b))
    return kept


def split_row(r, cuts):
    """Cells of one row, always one per column. A cut that falls inside text
    (a spanning cell) is not applied; the text stays whole in the left cell
    and the cell to the right is left empty, so later columns keep their index."""
    cells, start, skipped = [], 0, 0
    for a, b in cuts:
        if (r[a:b] if a < len(r) else "").strip():
            skipped += 1
            continue
        cells.append(r[start:a].strip())
        cells.extend([""] * skipped)
        skipped = 0
        start = b
    cells.append(r[start:].strip())
    cells.extend([""] * skipped)
    return cells


def to_table(block):
    rows = [l.rstrip() for l in block if l.strip()]
    cuts = column_cuts(rows)
    # the left edge of the table is the common indent; drop it so cut 0 is real
    base = min(indent(r) for r in rows)
    if base:
        rows = [r[base:] for r in rows]
        cuts = column_cuts(rows)
    if not cuts:
        return None
    width = len(cuts) + 1
    grid = [split_row(r, cuts) for r in rows]
    # merge wrapped cells: a row whose first cell is empty continues the row above
    merged = []
    for cells in grid:
        if merged and not cells[0] and any(cells[1:]):
            for k, c in enumerate(cells):
                if c:
                    merged[-1][k] = (merged[-1][k] + " " + c).strip()
        else:
            merged.append(cells)
    if len(merged) < 2 or width < 2:
        return None
    out = ["| " + " | ".join(c.replace("|", "\\|") for c in merged[0]) + " |", "|" + " --- |" * width]
    for cells in merged[1:]:
        out.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
    return out


def join_lines(lines):
    text = ""
    for l in lines:
        l = l.strip().replace("­", "")
        if not text:
            text = l
            continue
        if re.search(r"[a-z]-$", text) and re.match(r"^[a-z]", l):
            text = text[:-1] + l
        else:
            text += " " + l
    return text


def to_list(block):
    items = []
    for l in block:
        m = BULLET.match(l)
        if m:
            mark = m.group(2)
            mark = mark if re.match(r"^(\(?\w{1,4}[.)]|[①-⑳❶-❿⓫-⓴])$", mark) else "-"
            items.append([mark, m.group(3)])
        elif items:
            items[-1][1] = join_lines([items[-1][1], l])
        else:
            items.append(["", l.strip()])
    out = []
    for mark, text in items:
        out.append((mark + " " + text) if mark else text)
    return out


def render_text(block, phrases):
    """A block without a table: list items, key: value lines, or a joined paragraph.
    Lines holding a boilerplate phrase are removed first, line by line, so a
    document number or date printed next to a legal line survives."""
    block = [l for l in block if not is_boilerplate(l, phrases)]
    if not block:
        return []
    if any(BULLET.match(l) for l in block[:2]):
        return to_list(block) + [""]
    kv = sum(1 for l in block if KEYVAL.match(l) or BULLET.match(l) or DASH_ITEM.match(l))
    if len(block) >= 2 and kv >= 0.5 * len(block):
        out = []
        for l in block:
            if BULLET.match(l):
                out.append(to_list([l])[0])
            elif DASH_ITEM.match(l):
                out.append("  - " + l.strip()[1:].strip())
            elif KEYVAL.match(l) or not out:
                out.append("- " + l.strip())
            else:
                out[-1] = join_lines([out[-1], l])
        return out + [""]
    return [join_lines(block), ""]


def blocks_of(lines):
    blocks, cur, gaps = [], [], []
    gap = 0
    for l in lines:
        if l.strip():
            if not cur:
                gaps.append(gap)
            cur.append(l)
            gap = 0
        else:
            gap += 1
            if cur:
                blocks.append(cur)
                cur = []
    if cur:
        blocks.append(cur)
    return merge_table_blocks(blocks, gaps)


def merge_table_blocks(blocks, gaps):
    """Table rows that -layout separated by one blank line are one table when
    the joined rows still share column gaps."""
    out = []
    for block, gap in zip(blocks, gaps):
        if out and gap <= 1 and tableish(out[-1]) and tableish(block):
            rows = [l.rstrip() for l in out[-1] + block if has_gap(l)]
            if column_cuts(rows):
                out[-1] = out[-1] + block
                continue
        out.append(block)
    return out


def tableish(block):
    gapped = sum(1 for l in block if has_gap(l))
    return gapped >= max(1, 0.5 * len(block)) and not any(BULLET.match(l) for l in block[:1])


def load_boilerplate():
    path = os.path.join(HERE, "boilerplate.txt")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [l.strip().lower() for l in f if l.strip() and not l.startswith("#")]


def is_boilerplate(text, phrases):
    t = text.lower()
    return any(p in t for p in phrases)


def match_headings(lines, cands):
    """Replace heading lines in a page by markdown headings. Returns new lines."""
    if not cands:
        return lines
    wanted = [(norm(t), t, lvl) for t, lvl in cands if norm(t)]
    out, i = [], 0
    while i < len(lines):
        hit = None
        for span in (1, 2, 3):
            if i + span > len(lines):
                break
            chunk = lines[i:i + span]
            if any(not c.strip() for c in chunk):
                break
            key = norm(" ".join(chunk))
            for ck, t, lvl in wanted:
                if same_heading(key, ck):
                    hit = (span, (t, lvl))
                    break
            if hit:
                break
        if hit:
            span, (text, lvl) = hit
            text = re.sub(r"\s+", " ", text).strip().lstrip(MARKS + " ")
            out.append("")
            out.append("#" * min(lvl, 6) + " " + text)
            out.append("")
            i += span
        else:
            out.append(lines[i])
            i += 1
    return out


def figure_labels(figs):
    labels = set()
    for fig in figs:
        for m in re.finditer(r"(?:text-layer labels|nearby labels): (.*?) \| (?=nearby labels|OCR)", fig[0]):
            if not m.group(1).startswith("none"):
                labels.update(x.strip() for x in m.group(1).split(" | "))
    return labels


def is_label_block(block, labels):
    """A short block made only of text that the page's figures list as labels."""
    if len(block) > 3 or not labels:
        return False
    for l in block:
        for piece in GAP.split(l.strip()):
            t = " ".join(piece.split())
            if not t:
                continue
            if not any(t == lab or (t in lab and len(t) >= 3) for lab in labels):
                return False
    return True


def render_page(lines, phrases, subsup, labels=frozenset()):
    """Body lines of one page -> markdown lines."""
    lines = [l for l in lines if not TOC_LINE.search(l)]
    out = []
    for block in blocks_of(lines):
        if is_label_block(block, labels):
            continue
        if block[0].startswith("#") and len(block) == 1:
            out.extend(["", block[0], ""])
            continue
        if block[0].startswith("<!--"):
            out.extend(block + [""])
            continue
        span = table_span(block)
        if span:
            start, end = span
            if start:
                out.extend(render_text(block[:start], phrases))
            table = to_table(block[start:end])
            if table:
                out.extend(table + [""])
            else:
                out.extend(["```"] + [l.rstrip() for l in block[start:end]] + ["```", ""])
            if end < len(block):
                out.extend(render_text(block[end:], phrases))
            continue
        out.extend(render_text(block, phrases))
    if subsup:
        for flat, marked in subsup:
            out = [re.sub(r"(?<![\w_^])" + re.escape(flat) + r"(?![\w])", marked, l) if not l.startswith("<!--") else l for l in out]
    return out


def join_across_pages(pages_out):
    """A paragraph cut by a page break: last text line of a page ends without
    sentence punctuation and the next page's first text line starts lowercase."""
    for a, b in zip(pages_out, pages_out[1:]):
        ia = last_text_index(a["md"])
        ib = first_text_index(b["md"])
        if ia is None or ib is None:
            continue
        la, lb = a["md"][ia], b["md"][ib]
        if la.startswith(("#", "|", "-", "```", "<!--")) or lb.startswith(("#", "|", "-", "```", "<!--")):
            continue
        if not re.search(r"[.:;!?)\]\"”’]$", la) and re.match(r"^[a-z(]", lb):
            a["md"][ia] = join_lines([la, lb])
            del b["md"][ib]
    return pages_out


def last_text_index(md):
    for i in range(len(md) - 1, -1, -1):
        if md[i].strip():
            return i
    return None


def first_text_index(md):
    for i, l in enumerate(md):
        if l.strip():
            return i
    return None


def is_addendum(page):
    head = " ".join(l for l in page["lines"][:6] if l.strip())[:300]
    return bool(ADDENDUM.search(head))


def title_of(pdf, pages, xml):
    info = run(["pdfinfo", pdf]).decode("utf-8", "replace")
    m = re.search(r"^Title:\s+(.+)$", info, re.M)
    t = m.group(1).strip() if m else ""
    # a metadata title that is really a file name (no spaces, an extension) is not used
    if t and not re.search(r"\.[a-z]{2,5}$", t, re.I) and not (" " not in t and "_" in t):
        return t
    first = xml.get(1) or []
    if first:
        big = max(first, key=lambda l: l["size"])
        return big["text"]
    return os.path.splitext(os.path.basename(pdf))[0]


def main(src_md, pdf, out_path, review_md=None):
    notes, pages = parse_extraction(src_md)
    review = load_review(review_md)
    xml, glyph_pats = xml_pages(pdf, load_glyphs(pdf))
    cands = heading_candidates(xml)
    subsup = subsup_from_xml(pdf)
    phrases = load_boilerplate()
    omit = load_omit_titles()
    rendered = []
    title = title_of(pdf, pages, xml)
    prev_header = None
    for page in pages:
        body, figs = split_figures(page["lines"])
        figs = [apply_figure_review(fig, page["pno"], review) for fig in figs]
        ligs, marks = page_notes(body)
        body = apply_glyphs(body, glyph_pats.get(page["pno"]))
        page_cands = [(t, lvl) for t, lvl in cands.get(page["pno"], []) if not (page["pno"] == 1 and norm(t) == norm(title))]
        body = match_headings(body, page_cands)
        body = apply_marks(body, marks)
        header = (page["header"] or "").strip()
        if header and header != prev_header and not any(l.startswith("#") and norm(header) in norm(l) for l in body):
            body = ["", "## " + header, ""] + body
        if header:
            prev_header = header
        labels = set(apply_glyphs(sorted(figure_labels(figs)), glyph_pats.get(page["pno"])))
        md = render_page(body, phrases, subsup.get(page["pno"]), labels)
        md = apply_ligatures(md, ligs)
        md = apply_table_review(md, page["pno"], review)
        if subsup.get(page["pno"]):
            md.insert(0, "<!-- sub/superscripts on this page (from font sizes): " + ", ".join(m for _, m in subsup[page["pno"]]) + " -->")
        for fig in figs:
            md.extend(fig + [""])
        page["md"] = md
        rendered.append(page)
    rendered = join_across_pages(rendered)
    addenda = [p for p in rendered if is_addendum(p)]
    body_pages = [p for p in rendered if p not in addenda]
    out = [f"# {title}", "",
           f"<!-- source: {pdf} | extraction: {src_md} | structured by tools/structure.py; every line can be checked in the extraction"
           + (f" | review: {review_md}" if review_md and os.path.exists(review_md) else "") + " -->", ""]
    out.extend(notes)
    if notes:
        out.append("")
    if addenda:
        out.append("## Addenda and corrections")
        out.append("")
        for p in addenda:
            out.append(marker_of(p))
            out.append("")
            out.extend(p["md"])
    for p in body_pages:
        out.append(marker_of(p))
        out.append("")
        out.extend(p["md"])
    out = dedupe_headings(out)
    out = omit_sections(out, omit)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


def load_review(path):
    """{"figures": {(page, N): (status, lines, note)}, "tables": {(page, first-row key): (rows, note)}}"""
    out = {"figures": {}, "tables": {}}
    if not path or not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]
    i = 0
    while i < len(lines):
        m = REV_FIG.match(lines[i])
        if m:
            n, pno, status, note = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4).strip("; ")
            body = []
            if status == "corrected":
                i += 1
                while i < len(lines) and not lines[i].startswith("<!-- end of reviewed figure"):
                    body.append(lines[i])
                    i += 1
            out["figures"][(pno, n)] = (status, body, note)
        m = REV_TABLE.match(lines[i]) if i < len(lines) else None
        if m and m.group(3) == "corrected":
            pno, key, note = int(m.group(1)), m.group(2), m.group(4).strip("; ")
            rows = []
            i += 1
            while i < len(lines) and not lines[i].startswith("<!-- end of reviewed table"):
                if lines[i].startswith("|"):
                    rows.append(lines[i])
                i += 1
            out["tables"][(pno, key)] = (rows, note)
        i += 1
    return out


def apply_figure_review(block, pno, review):
    """A figure block from split_figures with the review applied."""
    m = FIG_START.match(block[0])
    if not m:
        return block
    rev = review["figures"].get((pno, int(m.group(1))))
    if not rev:
        return block
    status, body, note = rev
    marker = block[0][:-4]   # strip " -->"
    if status == "corrected":
        return [marker + f" | review: text from the page image, unverified by a person {note} -->"] + body + [f"<!-- end of figure {m.group(1)} -->"]
    if status == "verified":
        return [marker + f" | review: tesseract reading verified against the page image {note} -->"] + block[1:]
    if status in ("no_text", "illegible"):
        return [marker + f" | review: {status} on the page image {note} -->"]
    return block


def table_key(line):
    cells = [re.sub(r"\s+", " ", c.strip()) for c in line.strip().strip("|").split("|")]
    return " | ".join(cells)[:120]


def apply_table_review(md, pno, review):
    """Replace markdown tables on this page by their reviewed re-arrangement."""
    if not review["tables"]:
        return md
    out, i = [], 0
    while i < len(md):
        if md[i].startswith("|"):
            j = i
            while j < len(md) and md[j].startswith("|"):
                j += 1
            rev = review["tables"].get((pno, table_key(md[i])))
            if rev:
                rows, note = rev
                out.append(f"<!-- table re-arranged to the printed layout from the page image ({note}); words unchanged -->")
                out.extend(rows)
            else:
                out.extend(md[i:j])
            i = j
            continue
        out.append(md[i])
        i += 1
    return out


def load_omit_titles():
    path = os.path.join(HERE, "omit_sections.txt")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [norm_title(l) for l in f if l.strip() and not l.startswith("#")]


def norm_title(t):
    """Heading text as compared with omit_sections.txt: lower case, spacing
    collapsed, leading chapter number and marker glyphs and a trailing
    parenthetical removed."""
    t = re.sub(r"\s*\((?:[^()]|\([^()]*\))*\)\s*$", "", t.strip())
    return norm(t).strip()


def omit_sections(lines, titles):
    """Replace each section whose heading is an omit title by a marker; the
    section runs to the next heading of any level. Page markers and page
    notes inside it are kept so later text keeps its page cite."""
    if not titles:
        return lines
    out, i, page = [], 0, None
    while i < len(lines):
        l = lines[i]
        pm = PAGE_MARK.match(l)
        if pm:
            page = int(pm.group(1))
        m = re.match(r"^(#+) (.*)$", l)
        if m and any(fnmatch.fnmatchcase(norm_title(m.group(2)), t) for t in titles):
            first, last, n, j = page, page, 0, i + 1
            kept = []
            while j < len(lines) and not re.match(r"^#+ ", lines[j]):
                pm = PAGE_MARK.match(lines[j])
                if pm:
                    last = int(pm.group(1))
                    kept.append(lines[j])
                elif lines[j].startswith(("<!-- sub/superscripts", "<!-- ligatures", "<!-- list markers")):
                    kept.append(lines[j])
                elif lines[j].strip() and not lines[j].startswith("<!--"):
                    n += 1
                j += 1
            if n == 0:   # a container heading with no body of its own: keep it, judge its sub-sections
                out.append(l)
                i += 1
                continue
            pages = f"pdf page {first}" if first == last else f"pdf pages {first}-{last}"
            out.append(f'<!-- omitted: "{m.group(2).strip()}" ({pages}; {n} lines): legal, warranty or regulatory boilerplate; text in the extraction -->')
            out.extend(kept)
            i = j
            continue
        out.append(l)
        i += 1
    return out


def dedupe_headings(lines):
    """Drop a heading that repeats the previous heading of its level (a running
    chapter title that reached the body on several pages)."""
    last = {}
    out = []
    for l in lines:
        m = re.match(r"^(#+) (.*)$", l)
        if m:
            lvl, key = len(m.group(1)), norm(m.group(2))
            if any(last.get(k) == key for k in last if k <= lvl):
                continue
            last[lvl] = key
            for deeper in [k for k in last if k > lvl]:
                del last[deeper]
        out.append(l)
    return out


def marker_of(p):
    m = f"<!-- pdf page {p['pno']}"
    if p["printed"]:
        m += f" | printed page {p['printed']}"
    if p["header"]:
        m += f" | header: {p['header']}"
    return m + " -->"


if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    main(*sys.argv[1:])
