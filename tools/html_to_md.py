#!/usr/bin/env python3
"""Convert an HTML document (e.g. saved from Word or a web manual) to markdown.

Usage: html_to_md.py <input.html> <output.md>

Headings, paragraphs, lists and tables are kept as markdown; images become a
marker with their source and alt text; scripts, styles and comments are
dropped. Text is verbatim. Standard library only.
"""
import html
import re
import sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6", "table", "ul", "ol", "pre"}


class MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.table = None      # list of rows while inside <table>
        self.row = None
        self.cell = None
        self.heading = None
        self.list_depth = 0

    def emit(self, s):
        if self.cell is not None:
            self.cell.append(s)
        elif self.heading is not None:
            self.heading.append(s)
        else:
            self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading = []
            self.hlevel = int(tag[1])
        elif tag == "table":
            self.table = []
        elif tag == "tr" and self.table is not None:
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = []
        elif tag == "img":
            self.emit(f"\n<!-- image: {a.get('src', '')} alt: {a.get('alt', '')} -->\n")
        elif tag in ("ul", "ol"):
            self.list_depth += 1
        elif tag == "li":
            self.emit("\n" + "  " * (self.list_depth - 1) + "- ")
        elif tag == "br":
            self.emit("\n")
        elif tag in ("p", "div", "pre"):
            self.emit("\n\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self.heading is not None:
            text = " ".join("".join(self.heading).split())
            self.heading = None
            if text:
                self.out.append(f"\n\n{'#' * self.hlevel} {text}\n\n")
        elif tag in ("td", "th") and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()).replace("|", "\\|"))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if any(c for c in self.row):
                self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            rows = self.table
            self.table = None
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
                lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                self.out.append("\n\n" + "\n".join(lines) + "\n\n")
        elif tag in ("ul", "ol"):
            self.list_depth = max(0, self.list_depth - 1)
            self.emit("\n")
        elif tag in ("p", "div", "pre"):
            self.emit("\n")

    def handle_data(self, data):
        if self.skip:
            return
        if self.cell is not None or self.heading is not None:
            self.emit(data)
        else:
            self.emit(re.sub(r"[ \t\r\n]+", " ", data))


def main(src, dst):
    with open(src, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    p = MD()
    p.feed(raw)
    text = "".join(p.out)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
