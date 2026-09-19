#!/usr/bin/env python3
"""Find figure regions on a page: graphics that the text layer cannot see.

Method: render the page at low resolution (grey), blank out every text block,
and look at the edges that remain (a pixel that differs from its neighbour).
Uniform fills such as shaded heading bars leave only their outline; photos,
drawings and diagrams leave many edges. Connected edge pixels form
components; components whose boxes overlap are merged (a frame encloses its
drawing, a neighbouring box stays separate). A region is a figure when it is
big enough and is not a table: a table holds many text blocks aligned in
columns, a figure holds few scattered labels. Works for raster and vector
graphics alike. Requires poppler-utils.
"""
import os
import re
import subprocess
import tempfile

DPI = 30
EDGE = 24           # grey difference to a neighbour that makes an edge pixel (light UI screenshots need a low value)
MIN_PIXELS = 12     # smaller components are noise
MIN_SIDE = 40.0     # pt; smallest figure side kept
MIN_DENSITY = 0.02  # edge share of the region box below which it is a stray rule
TABLE_BLOCKS = 8    # a region with this many text blocks, mostly column-aligned, is a table
TABLE_ALIGN = 0.5   # share of those blocks sharing a left edge with two others
ROW_SHARE = 0.6     # share of inside blocks on a baseline shared with longer outside text: a table column
MAX_LABEL = 40      # a text block this short inside a region is a figure label
NEAR = 40.0         # pt; a short block this close to a region is a nearby label (callout, dimension)


def render(pdf, tmpdir):
    subprocess.run(["pdftoppm", "-gray", "-r", str(DPI), pdf, os.path.join(tmpdir, "p")],
                   check=True, capture_output=True)
    out = {}
    for f in os.listdir(tmpdir):
        m = re.search(r"-(\d+)\.pgm$", f)
        if m:
            out[int(m.group(1))] = os.path.join(tmpdir, f)
    return out


def read_pgm(path):
    with open(path, "rb") as f:
        data = f.read()
    m = re.match(rb"P5\s+(\d+)\s+(\d+)\s+(\d+)\s", data)
    w, h = int(m.group(1)), int(m.group(2))
    return w, h, data[m.end():]


def components(ink, w, h):
    """8-connected components of edge pixels: [(x0, y0, x1, y1, npix)]."""
    seen = bytearray(w * h)
    out = []
    for i in range(w * h):
        if not ink[i] or seen[i]:
            continue
        seen[i] = 1
        stack, n = [i], 0
        x0 = x1 = i % w
        y0 = y1 = i // w
        while stack:
            j = stack.pop()
            n += 1
            x, y = j % w, j // w
            x0, x1, y0, y1 = min(x0, x), max(x1, x), min(y0, y), max(y1, y)
            for dy in (-1, 0, 1):
                ny = y + dy
                if ny < 0 or ny >= h:
                    continue
                for dx in (-1, 0, 1):
                    nx = x + dx
                    if nx < 0 or nx >= w:
                        continue
                    k = ny * w + nx
                    if ink[k] and not seen[k]:
                        seen[k] = 1
                        stack.append(k)
        if n >= MIN_PIXELS:
            out.append([x0, y0, x1 + 1, y1 + 1, n])
    return out


def merge_boxes(boxes, pad=2):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(boxes):
            a = boxes[i]
            j = i + 1
            while j < len(boxes):
                b = boxes[j]
                if a[0] < b[2] + pad and b[0] < a[2] + pad and a[1] < b[3] + pad and b[1] < a[3] + pad:
                    a[0], a[1] = min(a[0], b[0]), min(a[1], b[1])
                    a[2], a[3] = max(a[2], b[2]), max(a[3], b[3])
                    a[4] += b[4]
                    del boxes[j]
                    changed = True
                else:
                    j += 1
            i += 1
    return boxes


def row_share(inside, outside):
    """Share of inside blocks that share a baseline with a block outside the region."""
    if not inside:
        return 0.0
    n = 0
    for a in inside:
        ha = a["y1"] - a["y0"]
        for b in outside:
            ov = min(a["y1"], b["y1"]) - max(a["y0"], b["y0"])
            if ov > 0.5 * min(ha, b["y1"] - b["y0"]):
                n += 1
                break
    return n / len(inside)


def aligned_share(blocks):
    n = 0
    for a in blocks:
        if sum(1 for b in blocks if b is not a and abs(b["x0"] - a["x0"]) <= 1.5) >= 2:
            n += 1
    return n / len(blocks) if blocks else 0.0


def regions(pgm_path, W, H, blocks):
    """Return [(x0, y0, x1, y1, density, labels, nearby)] in page points."""
    w, h, px = read_pgm(pgm_path)
    if not W or not H:
        return []
    sx, sy = w / W, h / H
    ink = bytearray(w * h)
    for y in range(h - 1):
        row, nxt = y * w, (y + 1) * w
        for x in range(w - 1):
            v = px[row + x]
            if abs(v - px[row + x + 1]) > EDGE or abs(v - px[nxt + x]) > EDGE:
                ink[row + x] = 1
    for b in blocks:
        x0, x1 = max(0, int(b["x0"] * sx) - 2), min(w, int(b["x1"] * sx) + 3)
        y0, y1 = max(0, int(b["y0"] * sy) - 2), min(h, int(b["y1"] * sy) + 3)
        for y in range(y0, y1):
            ink[y * w + x0:y * w + x1] = bytes(x1 - x0)
    out = []
    for px0, py0, px1, py1, n in merge_boxes(components(ink, w, h)):
        x0, y0, x1, y1 = px0 / sx, py0 / sy, px1 / sx, py1 / sy
        if x1 - x0 < MIN_SIDE or y1 - y0 < MIN_SIDE:
            continue
        dens = n / ((px1 - px0) * (py1 - py0))
        if dens < MIN_DENSITY:
            continue
        inside = [b for b in blocks
                  if b["x0"] >= x0 - 2 and b["x1"] <= x1 + 2 and b["y0"] >= y0 - 2 and b["y1"] <= y1 + 2]
        if len(inside) >= TABLE_BLOCKS and aligned_share(inside) >= TABLE_ALIGN:
            continue
        outside = [b for b in blocks if b not in inside and len(b["text"]) > 12]
        if len(inside) >= 3 and row_share(inside, outside) >= ROW_SHARE:
            continue
        labels = [b["text"] for b in inside if len(b["text"]) <= MAX_LABEL]
        nearby = [b["text"] for b in blocks
                  if b not in inside and len(b["text"]) <= MAX_LABEL and b["nlines"] <= 2
                  and b["x0"] >= x0 - NEAR and b["x1"] <= x1 + NEAR and b["y0"] >= y0 - NEAR and b["y1"] <= y1 + NEAR]
        out.append((x0, y0, x1, y1, dens, labels, nearby))
    out.sort(key=lambda r: (r[1], r[0]))
    return out


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.dont_write_bytecode = True   # no __pycache__ in the repository
    import pdf_to_md as x
    pdf, pages = sys.argv[1], [int(p) for p in sys.argv[2:]]
    geom = x.blocks_by_page(pdf)
    with tempfile.TemporaryDirectory() as td:
        pgms = render(pdf, td)
        for p in pages:
            W, H, blocks = geom.get(p, (0, 0, []))
            for r in regions(pgms[p], W, H, blocks):
                print(f"p{p}: {r[0]:.0f},{r[1]:.0f}-{r[2]:.0f},{r[3]:.0f}  density {r[4]:.2f}  labels {r[5][:6]}  nearby {r[6][:6]}")
