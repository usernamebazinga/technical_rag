#!/usr/bin/env python3
"""Survey PDFs for the extraction problem classes. Prints one row per PDF.

Usage: survey.py <pdf> [<pdf> ...]        (or: find sources -name '*.pdf' | xargs -d '\\n' tools/survey.py)

Columns
  pages     page count
  notext    pages with no text layer (OCR candidates)
  img       pages whose images cover >50 % of the page (figure or scan pages)
  1col      pages with text only left of the midline, extracted as one flow
  2col      pages the extractor splits into two columns somewhere
  table     pages with text on both sides that the extractor keeps as one flow (tables, wide text)
  draw      pages flagged as drawings in the existing extraction ("-" if not extracted yet)
  sym       fonts whose family name matches a known symbol/pictogram face
  nouni     fonts without a ToUnicode map (characters may extract wrong)
  unknown   font families not in the standard text-face list (classify once)

Requires poppler-utils (pdffonts, pdfimages, pdftotext).
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True   # no __pycache__ in the repository
import pdf_to_md as x  # noqa: E402

TEXT_FACE = x.TEXT_FACE
SYMBOL_FACE = x.SYMBOL_FACE


def run(args):
    return subprocess.run(args, capture_output=True).stdout.decode("utf-8", "replace")


def fonts(pdf):
    lines = run(["pdffonts", pdf]).splitlines()
    if len(lines) < 3:
        return []
    head = lines[0]
    c_type, c_uni, c_obj = head.index("type"), head.index("uni"), head.index("object")
    out = []
    for r in lines[2:]:
        if len(r) < c_obj:
            continue
        name = r[:c_type].strip()
        uni = r[c_uni:c_uni + 3].strip()
        fam = re.sub(r"^[A-Z]{6}\+", "", name)
        out.append((fam, uni))
    return out


def image_pages(pdf, pages):
    # pdfimages -list: page num type width height color comp bpc enc interp object ID x-ppi y-ppi size ratio
    rows = run(["pdfimages", "-list", pdf]).splitlines()[2:]
    cover = {}
    for r in rows:
        p = r.split()
        if len(p) < 4 or not p[0].isdigit():
            continue
        pno, w, h = int(p[0]), int(p[3]), int(p[4])
        try:
            xppi, yppi = float(p[12]), float(p[13])
        except (IndexError, ValueError):
            continue
        if xppi <= 0 or yppi <= 0:
            continue
        W, H, _ = pages.get(pno, (0, 0, []))
        if not W:
            continue
        area = (w / xppi * 72) * (h / yppi * 72) / (W * H)
        cover[pno] = cover.get(pno, 0) + area
    return sum(1 for a in cover.values() if a > 0.5)


def drawing_pages(pdf):
    md = "extracted/" + pdf.split("sources/", 1)[-1].rsplit(".", 1)[0] + ".md"
    if not os.path.exists(md):
        return "-"
    with open(md, encoding="utf-8") as f:
        return sum(1 for line in f if line.startswith("<!-- drawing page"))


def layout_counts(pages):
    """Pages by the extractor's own decision: all one flow, or split in columns somewhere."""
    c = dict(one=0, two=0, table=0, notext=0)
    for pno, (W, H, blocks) in pages.items():
        if not blocks:
            c["notext"] += 1
            continue
        xlim = x.tab_limit(blocks, W)
        blocks = [b for b in blocks if b["x0"] < xlim]
        bands = x.bands_for(blocks, W, H)
        if any(k == "two" for k, *_ in bands):
            c["two"] += 1
        elif len(bands) == 1 and not any(b["x0"] >= W / 2 - x.TOL for b in blocks):
            c["one"] += 1
        else:
            c["table"] += 1
    return c


def main(paths):
    print("pages notext img  1col 2col table draw  sym nouni unknown  file")
    for pdf in paths:
        n = x.page_count(pdf)
        pages = x.blocks_by_page(pdf)
        for p in range(1, n + 1):
            pages.setdefault(p, (0.0, 0.0, []))
        lc = layout_counts(pages)
        fs = fonts(pdf)
        fams = sorted({f for f, _ in fs})
        sym = [f for f in fams if SYMBOL_FACE.search(f)]
        nouni = sorted({f for f, u in fs if u == "no"})
        unknown = [f for f in fams if not TEXT_FACE.search(f) and not SYMBOL_FACE.search(f)]
        print(f"{n:5d} {lc['notext']:6d} {image_pages(pdf, pages):3d}  {lc['one']:4d} {lc['two']:4d} {lc['table']:5d} {str(drawing_pages(pdf)):>4}  "
              f"{len(sym):3d} {len(nouni):5d} {len(unknown):7d}  {pdf}")
        for tag, lst in (("sym", sym), ("nouni", nouni), ("unknown", unknown)):
            if lst:
                print(f"      {tag}: {', '.join(lst)}")


if __name__ == "__main__":
    main(sys.argv[1:] or sys.exit(__doc__))
