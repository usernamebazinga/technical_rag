#!/usr/bin/env python3
"""Stage 3: review, by the model in the session, of what the text layer
cannot carry. No API, no network: this script only prepares the items for
the reviewer and validates the review file the reviewer writes.

Usage:
  review.py prepare  <extracted.md> <source.pdf> <structured.md> <workdir> [--tasks figures,glyphs,tables] [--limit N]
  review.py validate <extracted.md> <source.pdf> <structured.md> <review.md>

prepare writes into <workdir>:
  items.md            one block per item with everything the reviewer needs:
                      the crop file, the sheet and row it is on, tesseract's
                      reading (figures), the markdown table (tables), the
                      text-layer character and context (glyphs)
  sheet_NN.png        contact sheets: several crops stacked, each preceded by
                      a black band holding k white squares = row k on the
                      sheet (read the sheets; open a single crop only when a
                      sheet is not enough)
  fig_pP_N.png, table_pP_K.png, glyph_K.png   single crops at higher resolution
  review.md           the review file with every item PENDING; the reviewer
                      edits it in place

The review file format (also what structure.py applies):
  <!-- reviewed figure N on pdf page P: verified|corrected|no_text|illegible (tag; reviewer); note -->
      corrected: the transcription lines follow, then <!-- end of reviewed figure N -->
  <!-- reviewed table on pdf page P, first row "KEY": matches|corrected|not_a_table|unreadable; note -->
      corrected: the markdown table follows, then <!-- end of reviewed table -->
  <!-- glyph candidate: FONT "c" -> "glyph" (name, confidence high|low; pdf page P, context 'x'; reviewer) not applied: verify against the rendered page and add to tools/glyphs.txt -->

validate checks the reviewer's file: every item exists, no PENDING is left,
a corrected figure has lines, and a corrected table holds exactly the words
of the original cells (nothing added, changed or dropped) - a table that
fails is rewritten as "rejected" with the difference. Then
  structure.py <extracted.md> <source.pdf> <out.md> <review.md>
applies it and check.py counts the numbers of model transcriptions apart.

Rules the reviewer follows:
  figures  transcribe only what is legibly printed, exactly as printed; "?"
           for an unreadable character; "verified" only when tesseract's
           lines are exactly right and complete
  tables   re-arrange cells only; every word once; never add or drop text
  glyphs   name the printed glyph; it goes into glyphs.txt only by hand
"""
import os
import re
import struct
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True   # no __pycache__ in the repository
import pdf_to_md as p1  # noqa: E402
import structure as p2  # noqa: E402

REVIEWER = "Claude in session"
CROP_DPI = 200       # single crops
SHEET_DPI = 130      # crops on a contact sheet
SHEET_W = 1000       # px; widest crop on a sheet (a wider region is rendered at lower dpi)
SHEET_H = 1500       # px; a sheet is closed when the next crop would pass this
BAND = 22            # px; index band above each crop on a sheet

FIG = re.compile(r"^<!-- figure (\d+) on pdf page (\d+) at ([\d.]+),([\d.]+)-([\d.]+),([\d.]+) pt \| (.*) -->$")
FONT_LINE = re.compile(r'^<!-- font check: (.+?) is not a standard text face; glyphs "(.*)" on pages (.+?)\. Verify')
REV_FIG = re.compile(r"^<!-- reviewed figure (\d+) on pdf page (\d+): (\w+)(.*) -->$")
REV_TABLE = re.compile(r'^<!-- reviewed table on pdf page (\d+), first row "(.*)": (\w+)(.*) -->$')
REV_GLYPH = re.compile(r'^<!-- glyph candidate: (.+?) "(.*?)" -> "(.*?)"')


def run(args):
    return subprocess.run(args, check=True, capture_output=True).stdout


# ------------------------------------------------------------- work items

def figure_items(ext_lines):
    """[(N, page, box, "kept"|"below_floor", tesseract lines)] for figures whose OCR saw words."""
    items, i = [], 0
    while i < len(ext_lines):
        m = FIG.match(ext_lines[i])
        if not m:
            i += 1
            continue
        n, pno = int(m.group(1)), int(m.group(2))
        box = tuple(float(m.group(k)) for k in (3, 4, 5, 6))
        lines = []
        if "OCR text follows" in m.group(7):
            i += 1
            while i < len(ext_lines) and not ext_lines[i].startswith("<!-- end of figure"):
                lines.append(ext_lines[i])
                i += 1
        st = p2.OCR_STAT.search(m.group(7))
        if st and int(st.group(2)):
            items.append((n, pno, box, "kept" if p2.ocr_passes(m.string) else "below_floor", lines))
        i += 1
    return items


def flagged_glyphs(ext_lines, pdf):
    """[(font, char)] flagged by the font check with no line in glyphs.txt."""
    table = p2.load_glyphs(pdf)
    out = []
    for l in ext_lines:
        m = FONT_LINE.match(l)
        if not m:
            continue
        fam, glyphs = m.group(1), m.group(2)
        if not p1.is_text_face(fam):
            keys = [k for k, _ in table.get(fam, [])]
            for c in glyphs:
                if c.isspace() or c == "…" or any(c in k for k in keys):
                    continue
                out.append((fam, c))
    return out


def glyph_occurrences(pdf, wanted):
    """{(font, char): (page, x0, y0, x1, y1, context)} first occurrence in pt, via pdftohtml -xml."""
    raw = run(["pdftohtml", "-xml", "-i", "-stdout", pdf])
    root = ET.fromstring(p1.CTRL.sub("", raw.decode("utf-8", "replace")))
    fam_of, out, want = {}, {}, set(wanted)
    for pno, page in enumerate(root.iter("page"), start=1):
        for fs in page.iter("fontspec"):
            fam_of[fs.get("id")] = re.sub(r"^[A-Z]{6}\+", "", fs.get("family", ""))
        for t in page.iter("text"):
            fam = fam_of.get(t.get("font"), "")
            txt = "".join(t.itertext())
            for c in txt:
                if (fam, c) in want and (fam, c) not in out:
                    z = 1.5   # pdftohtml -xml coordinates are pt * 1.5
                    l, tp, w, h = (float(t.get(k, 0)) / z for k in ("left", "top", "width", "height"))
                    out[(fam, c)] = (pno, l, tp, l + w, tp + h, txt.strip()[:30])
        if len(out) == len(want):
            break
    return out


def table_items(struct_lines):
    """[(page, first-row key, [markdown lines])] for every table in the structured file."""
    items, page, i = [], 0, 0
    while i < len(struct_lines):
        l = struct_lines[i]
        m = p2.PAGE_MARK.match(l)
        if m:
            page = int(m.group(1))
        if l.startswith("|"):
            j = i
            while j < len(struct_lines) and struct_lines[j].startswith("|"):
                j += 1
            block = struct_lines[i:j]
            if len(block) >= 3:
                items.append((page, p2.table_key(block[0]), block))
            i = j
            continue
        i += 1
    return items


def cells_of(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_tokens(rows):
    c = Counter()
    for cells in rows:
        for cell in cells:
            c.update(cell.replace("\\|", "|").split())
    return c


def locate_table(block, blocks):
    """Bounding box (pt) of the page words that belong to the table's cells,
    or None when too few are found."""
    want = Counter()
    for l in block[0:1] + block[2:]:
        for cell in cells_of(l):
            want.update(w for w in cell.replace("\\|", "|").split() if len(w) >= 2)
    if not want:
        return None
    hit, boxes = Counter(), []
    for b in blocks:
        for x0, y0, x1, y1, text in b["words"]:
            t = text.strip()
            if t in want and hit[t] < want[t]:
                hit[t] += 1
                boxes.append((x0, y0, x1, y1))
    if sum(hit.values()) < 0.6 * sum(want.values()) or len(boxes) < 4:
        return None
    return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))


# ------------------------------------------------------------------ images

def render(pdf, pno, x0, y0, x1, y1, dpi, fmt, out_base, pad=4.0):
    x0, y0, x1, y1 = max(0.0, x0 - pad), max(0.0, y0 - pad), x1 + pad, y1 + pad
    sc = dpi / 72.0
    run(["pdftoppm", "-r", f"{dpi:.2f}", "-f", str(pno), "-l", str(pno),
         "-x", str(int(x0 * sc)), "-y", str(int(y0 * sc)), "-W", str(int((x1 - x0) * sc) + 1), "-H", str(int((y1 - y0) * sc) + 1)]
        + ([fmt] if fmt != "-ppm" else []) + ["-singlefile", pdf, out_base])   # PPM is pdftoppm's default output


def crop_png(pdf, pno, box, path, pad=4.0):
    x0, y0, x1, y1 = box
    dpi = min(CROP_DPI, 1568 * 72.0 / max(x1 - x0 + 2 * pad, y1 - y0 + 2 * pad, 1.0))
    render(pdf, pno, x0, y0, x1, y1, dpi, "-png", path[:-4], pad)


def crop_rgb(pdf, pno, box, pad=4.0):
    """(width, height, rgb bytes) of a region rendered for a sheet."""
    x0, y0, x1, y1 = box
    dpi = min(SHEET_DPI, SHEET_W * 72.0 / max(x1 - x0 + 2 * pad, 1.0), SHEET_H * 72.0 / max(y1 - y0 + 2 * pad, 1.0))
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, "c")
        render(pdf, pno, x0, y0, x1, y1, dpi, "-ppm", base, pad)
        with open(base + ".ppm", "rb") as f:
            data = f.read()
    m = re.match(rb"P6\s+(\d+)\s+(\d+)\s+255\s", data)
    w, h = int(m.group(1)), int(m.group(2))
    return w, h, data[m.end():m.end() + w * h * 3]


def write_png(path, w, rows):
    raw = b"".join(b"\x00" + r for r in rows)

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, len(rows), 8, 2, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b""))


def band_rows(width, k):
    """A black band with k white squares: the row index on a sheet."""
    rows = []
    for y in range(BAND):
        row = bytearray(width * 3)
        if 6 <= y < BAND - 6:
            for i in range(k):
                x0 = 8 + i * 16
                for x in range(x0, min(width, x0 + 10)):
                    row[x * 3:x * 3 + 3] = b"\xff\xff\xff"
        rows.append(bytes(row))
    return rows


def make_sheets(crops, workdir):
    """crops: [(item id, w, h, rgb)]. Returns ({item id: (sheet, row)}, number of sheets)."""
    where, sheets, cur, cur_h = {}, [], [], 0
    for item in crops:
        _, w, h, _ = item
        if cur and cur_h + h + BAND > SHEET_H:
            sheets.append(cur)
            cur, cur_h = [], 0
        cur.append(item)
        cur_h += h + BAND
    if cur:
        sheets.append(cur)
    for s, items in enumerate(sheets, start=1):
        width = max(w for _, w, _, _ in items)
        rows = []
        for k, (iid, w, h, rgb) in enumerate(items, start=1):
            rows.extend(band_rows(width, k))
            for y in range(h):
                rows.append(rgb[y * w * 3:(y + 1) * w * 3] + b"\xff" * ((width - w) * 3))
            where[iid] = (s, k)
        write_png(os.path.join(workdir, f"sheet_{s:02d}.png"), width, rows)
    return where, len(sheets)


# ----------------------------------------------------------------- prepare

def prepare(ext_md, pdf, struct_md, workdir, tasks, limit):
    with open(ext_md, encoding="utf-8") as f:
        ext_lines = f.read().split("\n")
    with open(struct_md, encoding="utf-8") as f:
        struct_lines = f.read().split("\n")
    figs = figure_items(ext_lines) if "figures" in tasks else []
    glyphs = flagged_glyphs(ext_lines, pdf) if "glyphs" in tasks else []
    tables = table_items(struct_lines) if "tables" in tasks else []
    if limit is not None:
        figs, glyphs, tables = figs[:limit], glyphs[:limit], tables[:limit]
    os.makedirs(workdir, exist_ok=True)
    geom = p1.blocks_by_page(pdf) if tables else {}
    occ = glyph_occurrences(pdf, glyphs) if glyphs else {}
    crops, items, review = [], [], []
    for n, pno, box, st, tess in figs:
        iid = f"F{len(items) + 1}"
        fn = f"fig_p{pno}_{n}.png"
        crop_png(pdf, pno, box, os.path.join(workdir, fn))
        crops.append((iid, *crop_rgb(pdf, pno, box)))
        tag = "tesseract above floor" if st == "kept" else "tesseract below floor"
        items.append((iid, f"figure {n} on pdf page {pno} ({tag}) - {fn}",
                      "tesseract: " + (" / ".join(tess) if tess else "nothing reliable")))
        review.append(f"<!-- reviewed figure {n} on pdf page {pno}: PENDING ({tag}; {REVIEWER}); note -->")
    for k, (pno, key, block) in enumerate(tables, start=1):
        iid = f"T{k}"
        W, H, blocks = geom.get(pno, (0.0, 0.0, []))
        box = locate_table(block, blocks) if blocks else None
        where = "located by its words" if box else "not located by its words: whole page"
        if not box:
            box = (0.0, 0.0, W or 612.0, H or 792.0)
        fn = f"table_p{pno}_{k}.png"
        crop_png(pdf, pno, box, os.path.join(workdir, fn), pad=8.0)
        crops.append((iid, *crop_rgb(pdf, pno, box, pad=8.0)))
        items.append((iid, f'table on pdf page {pno}, first row "{key}" ({where}) - {fn}', "\n".join(block)))
        review.append(f'<!-- reviewed table on pdf page {pno}, first row "{key}": PENDING; note -->')
    for k, (fam, c) in enumerate(glyphs, start=1):
        iid = f"G{k}"
        if (fam, c) not in occ:
            items.append((iid, f'glyph {fam} "{c}" (U+{ord(c):04X}) - no occurrence found in the XML text', ""))
            continue
        pno, x0, y0, x1, y1, ctx = occ[(fam, c)]
        fn = f"glyph_{k}.png"
        crop_png(pdf, pno, (x0, y0, x1 + 80, y1), os.path.join(workdir, fn), pad=3.0)
        crops.append((iid, *crop_rgb(pdf, pno, (x0, y0, x1 + 80, y1), pad=3.0)))
        items.append((iid, f'glyph {fam} "{c}" (U+{ord(c):04X}), pdf page {pno}, text-layer context {ctx!r} - {fn}', ""))
        review.append(f'<!-- glyph candidate: {fam} "{c}" -> "PENDING" (name, confidence high|low; pdf page {pno}, context {ctx!r}; {REVIEWER}) not applied: verify against the rendered page and add to tools/glyphs.txt -->')
    where, nsheets = make_sheets(crops, workdir) if crops else ({}, 0)
    with open(os.path.join(workdir, "items.md"), "w", encoding="utf-8") as f:
        f.write(f"# Review items for {os.path.basename(pdf)}\n\n{len(figs)} figures, {len(tables)} tables, {len(glyphs)} glyphs; {nsheets} sheets.\n"
                "Each sheet stacks crops top to bottom; the black band above a crop holds k white squares = row k.\n\n")
        for iid, title, body in items:
            s = where.get(iid)
            f.write(f"## {iid}  {title}" + (f" - sheet {s[0]} row {s[1]}" if s else "") + "\n")
            if body:
                f.write(body + "\n")
            f.write("\n")
    with open(os.path.join(workdir, "review.md"), "w", encoding="utf-8") as f:
        f.write(f"<!-- review of {ext_md} | source {pdf} | reviewer {REVIEWER} | figures {len(figs)} glyphs {len(glyphs)} tables {len(tables)} -->\n")
        f.write("\n".join(review) + "\n")
    print(f"prepared {len(figs)} figures, {len(tables)} tables, {len(glyphs)} glyphs on {nsheets} sheets in {workdir}")


# ---------------------------------------------------------------- validate

def validate(ext_md, pdf, struct_md, review_md):
    with open(ext_md, encoding="utf-8") as f:
        ext_lines = f.read().split("\n")
    with open(struct_md, encoding="utf-8") as f:
        struct_lines = f.read().split("\n")
    with open(review_md, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]
    figs = {(int(m.group(2)), int(m.group(1))) for l in ext_lines for m in [FIG.match(l)] if m}
    tables = {(pno, key): block for pno, key, block in table_items(struct_lines)}
    out, problems, i = [], [], 0
    counts = Counter()
    while i < len(lines):
        l = lines[i]
        m = REV_FIG.match(l)
        if m:
            n, pno, status = int(m.group(1)), int(m.group(2)), m.group(3)
            body = []
            if status == "corrected":
                i += 1
                while i < len(lines) and not lines[i].startswith("<!-- end of reviewed figure"):
                    body.append(lines[i])
                    i += 1
            if (pno, n) not in figs:
                problems.append(f"figure {n} on pdf page {pno}: no such figure in the extraction")
            elif status == "PENDING":
                problems.append(f"figure {n} on pdf page {pno}: still PENDING")
            elif status not in ("verified", "corrected", "no_text", "illegible"):
                problems.append(f"figure {n} on pdf page {pno}: unknown status {status!r}")
            elif status == "corrected" and not [b for b in body if b.strip()]:
                problems.append(f"figure {n} on pdf page {pno}: corrected without lines")
            else:
                counts[f"figure {status}"] += 1
            out.append(l)
            out.extend(body)
            if status == "corrected":
                out.append(f"<!-- end of reviewed figure {n} -->")
            i += 1
            continue
        m = REV_TABLE.match(l)
        if m:
            pno, key, status = int(m.group(1)), m.group(2), m.group(3)
            rows = []
            if status == "corrected":
                i += 1
                while i < len(lines) and not lines[i].startswith("<!-- end of reviewed table"):
                    if lines[i].startswith("|"):
                        rows.append(lines[i])
                    i += 1
            block = tables.get((pno, key))
            if block is None:
                problems.append(f"table on pdf page {pno} {key[:40]!r}: no such table in the structured file")
                out.append(l)
            elif status == "PENDING":
                problems.append(f"table on pdf page {pno} {key[:40]!r}: still PENDING")
                out.append(l)
            elif status == "corrected":
                body_rows = [cells_of(r) for k, r in enumerate(rows) if not (k == 1 and set(r.replace("|", "").strip()) <= set("- :"))]
                have = table_tokens([cells_of(r) for r in block[0:1] + block[2:]])
                got = table_tokens(body_rows)
                if have != got:
                    missing = list((have - got).elements())[:6]
                    extra = list((got - have).elements())[:6]
                    out.append(f'<!-- reviewed table on pdf page {pno}, first row "{key}": rejected; cells changed: missing {missing}, added {extra} -->')
                    problems.append(f"table on pdf page {pno} {key[:40]!r}: rejected, words changed (missing {missing}, added {extra})")
                elif len(body_rows) < 2 or max(len(r) for r in body_rows) < 2:
                    out.append(f'<!-- reviewed table on pdf page {pno}, first row "{key}": rejected; fewer than two rows or columns -->')
                    problems.append(f"table on pdf page {pno} {key[:40]!r}: rejected, fewer than two rows or columns")
                else:
                    width = max(len(r) for r in body_rows)
                    out.append(l)
                    out.append("| " + " | ".join(body_rows[0] + [""] * (width - len(body_rows[0]))) + " |")
                    out.append("|" + " --- |" * width)
                    for r in body_rows[1:]:
                        out.append("| " + " | ".join(r + [""] * (width - len(r))) + " |")
                    out.append("<!-- end of reviewed table -->")
                    counts["table corrected"] += 1
            elif status in ("matches", "not_a_table", "unreadable", "rejected"):
                counts[f"table {status}"] += 1
                out.append(l)
            else:
                problems.append(f"table on pdf page {pno} {key[:40]!r}: unknown status {status!r}")
                out.append(l)
            i += 1
            continue
        m = REV_GLYPH.match(l)
        if m:
            if m.group(3) == "PENDING":
                problems.append(f'glyph {m.group(1)} "{m.group(2)}": still PENDING')
            else:
                counts["glyph candidate"] += 1
        out.append(l)
        i += 1
    with open(review_md, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip("\n") + "\n")
    for p in problems:
        print("PROBLEM " + p)
    print("validated: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f"; problems {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    argv = sys.argv[1:]
    if not argv or argv[0] not in ("prepare", "validate"):
        sys.exit(__doc__)
    cmd, rest = argv[0], argv[1:]
    args, opts, i = [], {}, 0
    while i < len(rest):
        a = rest[i]
        if a.startswith("--"):
            if "=" in a:
                k, v = a.split("=", 1)
                opts[k] = v
            elif a in ("--tasks", "--limit") and i + 1 < len(rest):
                opts[a] = rest[i + 1]
                i += 1
            else:
                opts[a] = True
        else:
            args.append(a)
        i += 1
    if len(args) != 4:
        sys.exit(__doc__)
    if cmd == "prepare":
        prepare(*args, tasks=str(opts.get("--tasks", "figures,glyphs,tables")).split(","),
                limit=int(opts["--limit"]) if "--limit" in opts else None)
    else:
        sys.exit(validate(*args))
