#!/usr/bin/env python3
"""Faithfulness check between an extraction and its structured document.

Usage: check.py [<extracted.md> <structured.md>]      (no arguments: whole corpus)

Every number (with its sign, without its unit) in the structured file must
occur in the extraction: stage 2 may not invent a value.
Every numeric token in the extraction that is missing from the structured
file is listed: stage 2 may drop contents lines and boilerplate, nothing else.
Tokens dropped on pages where a section was omitted (legal, warranty or
regulatory boilerplate, marked "omitted" in the structured file) are counted
apart. Comment markers (page, figure, font-check lines) and the structured
file's title/source header are ignored; OCR text is body text and is
compared, except OCR that stage 2 leaves out as below the confidence floor.
Text a model transcribed from the page image (stage 3, marked "review: text
from the page image") has no counterpart in the extraction; its numbers are
counted apart as "model", never as invented.
Prints one line per file and the offending tokens with their pdf page.
"""
import glob
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True   # no __pycache__ in the repository
from structure import ocr_passes, OMIT_MARK  # noqa: E402

NUM = re.compile(r"(?<![\w.])[+\-±]?\d+(?:[.,]\d+)*(?![\w.])")   # bare numbers; units are text and may be re-spaced by stage 2
PAGE = re.compile(r"^<!-- pdf page (\d+)")
LABELS = re.compile(r"(?:text-layer labels|nearby labels): (.*?) \| (?=nearby labels|OCR)")


FIGN = re.compile(r"^<!-- figure (\d+) on pdf page (\d+) ")


def tokens_by_page(path, figure_labels=False, superseded=frozenset()):
    """{page: Counter of numeric tokens}. With figure_labels, the labels listed
    in figure markers count as present (stage 2 moves label-only text out of
    the body into the marker). superseded: (page, N) of figures whose OCR text
    a reviewer replaced; their OCR block in the extraction is not counted."""
    pages, page = {}, 0
    skip = None   # end condition while inside OCR text stage 2 leaves out
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            if skip == "blank":
                if line.strip() and not line.startswith("<!--"):
                    continue
                skip = None
            elif skip:
                if line.startswith(skip):
                    skip = None
                continue
            m = PAGE.match(line)
            if m:
                page = int(m.group(1))
                continue
            if line.startswith("<!--"):
                if line.startswith("<!-- figure") and "review: text from the page image" in line:
                    skip = "<!-- end of figure"   # model transcription: counted by model_tokens
                    continue
                fm = FIGN.match(line)
                if fm and (int(fm.group(2)), int(fm.group(1))) in superseded and "OCR text follows" in line:
                    skip = "<!-- end of figure"
                    continue
                if "OCR text follows" in line and ocr_passes(line) is False:
                    skip = "<!-- end of figure" if line.startswith("<!-- figure") else "blank"
                    continue
                if figure_labels and line.startswith("<!-- figure"):
                    line = " ".join(lab for m in LABELS.finditer(line) for lab in m.group(1).split(" | ")
                                    if not m.group(1).startswith("none"))
                else:
                    continue
            if i < 3 and line.startswith(("# ", "<!-- source")):
                continue
            cnt = pages.setdefault(page, Counter())
            for t in NUM.findall(line):
                t = re.sub(r"\s+", "", t)
                if re.search(r"\d", t):
                    cnt[t] += 1
    return pages


def superseded_figures(struct):
    """(page, N) of figures whose text a reviewer transcribed (stage 3)."""
    out = set()
    with open(struct, encoding="utf-8") as f:
        for line in f:
            m = FIGN.match(line)
            if m and "review: text from the page image" in line:
                out.add((int(m.group(2)), int(m.group(1))))
    return out


def model_tokens(struct):
    """Numeric tokens inside figure blocks transcribed by a model (stage 3)."""
    c, on = Counter(), False
    with open(struct, encoding="utf-8") as f:
        for line in f:
            if line.startswith("<!-- figure") and "review: text from the page image" in line:
                on = True
                continue
            if line.startswith("<!-- end of figure"):
                on = False
                continue
            if on:
                c.update(re.sub(r"\s+", "", t) for t in NUM.findall(line))
    return c


def total(pages):
    c = Counter()
    for p in pages.values():
        c.update(p)
    return c


def check(ext, struct):
    """invented: tokens in the structured body or figure labels that occur nowhere
    in the extraction. dropped: extraction body occurrences not covered by the
    structured body plus its figure labels, with the pages where the shortfall
    is (a paragraph joined across a page break moves a token by one page)."""
    sup = superseded_figures(struct)
    e_body = tokens_by_page(ext, superseded=sup)
    e_all = total(tokens_by_page(ext, figure_labels=True, superseded=sup))
    s_pages = tokens_by_page(struct, figure_labels=True)
    s_all = total(s_pages)
    e_tot = total(e_body)
    invented = {t: (c, next(p for p, pc in s_pages.items() if t in pc)) for t, c in s_all.items() if t not in e_all}
    dropped = {}
    for t in e_tot:
        short = e_tot[t] - s_all.get(t, 0)
        if short > 0:
            pages = [p for p, pc in e_body.items() if pc.get(t, 0) > s_pages.get(p, Counter()).get(t, 0)]
            dropped[t] = (short, pages)
    return invented, dropped


def omitted_pages(struct):
    pages = set()
    with open(struct, encoding="utf-8") as f:
        for line in f:
            m = OMIT_MARK.match(line)
            if m:
                a, _, b = m.group(2).partition("-")
                pages.update(range(int(a), int(b or a) + 1))
    return pages


def main(pairs):
    total_inv = total_drop = total_omit = total_model = 0
    for ext, struct in pairs:
        invented, dropped = check(ext, struct)
        omit = omitted_pages(struct)
        n_model = sum(model_tokens(struct).values())
        total_model += n_model
        dropped, omitted = ({t: v for t, v in dropped.items() if not (v[1] and all(p in omit for p in v[1]))},
                            {t: v for t, v in dropped.items() if v[1] and all(p in omit for p in v[1])})
        n_inv, n_drop, n_omit = sum(c for c, _ in invented.values()), sum(c for c, _ in dropped.values()), sum(c for c, _ in omitted.values())
        total_inv += n_inv
        total_drop += n_drop
        total_omit += n_omit
        print(f"invented {n_inv:4d}  dropped {n_drop:4d}  omitted {n_omit:4d}  model {n_model:4d}  {struct}")
        for t, (c, p) in sorted(invented.items(), key=lambda kv: -kv[1][0])[:10]:
            print(f"      INVENTED {t!r} x{c} (structured pdf page {p})")
        by_page = Counter()
        for t, (c, pages) in dropped.items():
            for p in pages:
                by_page[p] += 1
        if by_page:
            print("      dropped tokens by extraction pdf page: " + ", ".join(f"p{p}:{n}" for p, n in sorted(by_page.items())))
    print(f"TOTAL invented {total_inv}  dropped {total_drop}  omitted {total_omit}  model {total_model}  over {len(pairs)} files")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main([(sys.argv[1], sys.argv[2])])
    elif len(sys.argv) == 1:
        pairs = []
        for struct in sorted(glob.glob("structured/**/*.md", recursive=True)):
            ext = "extracted/" + struct[len("structured/"):]
            if os.path.exists(ext):
                pairs.append((ext, struct))
        main(pairs)
    else:
        sys.exit(__doc__)
