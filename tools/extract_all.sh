#!/usr/bin/env bash
# Run the pipeline over sources/: every PDF -> extracted/<path>.md (verbatim)
# -> structured/<path>.md (headings, paragraphs, lists, tables); every HTML
# file -> both, via html_to_md.py. When review/<path>.md exists (stage 3,
# tools/review.py) stage 2 applies it. Up-to-date outputs are skipped
# unless --force is given. Usage: tools/extract_all.sh [--force]
set -u
cd "$(dirname "$0")/.."
force="${1:-}"
find sources -type f \( -iname '*.pdf' -o -iname '*.html' -o -iname '*.htm' \) | sort | while IFS= read -r src; do
  rel="${src#sources/}"; rel="${rel%.*}.md"
  ext="extracted/$rel"; str="structured/$rel"; rev="review/$rel"
  mkdir -p "$(dirname "$ext")" "$(dirname "$str")"
  case "${src,,}" in
    *.pdf)
      if [ "$force" = "--force" ] || [ ! -f "$ext" ] || [ "$src" -nt "$ext" ]; then
        python3 tools/pdf_to_md.py "$src" "$ext" 2>/dev/null || { echo "FAIL extract $src"; continue; }
      fi
      if [ "$force" = "--force" ] || [ ! -f "$str" ] || [ "$ext" -nt "$str" ] || { [ -f "$rev" ] && [ "$rev" -nt "$str" ]; }; then
        if [ -f "$rev" ]; then
          python3 tools/structure.py "$ext" "$src" "$str" "$rev" 2>/dev/null && echo "ok   $str (with review)" || echo "FAIL structure $src"
        else
          python3 tools/structure.py "$ext" "$src" "$str" 2>/dev/null && echo "ok   $str" || echo "FAIL structure $src"
        fi
      fi ;;
    *)
      if [ "$force" = "--force" ] || [ ! -f "$str" ] || [ "$src" -nt "$str" ]; then
        python3 tools/html_to_md.py "$src" "$ext" && cp "$ext" "$str" && echo "ok   $str" || echo "FAIL html $src"
      fi ;;
  esac
done
