#!/usr/bin/env bash
# Typeset WHITEPAPER.md -> nown-whitepaper.pdf
# Template: nown.latex, adapted from the Bitcoin whitepaper LaTeX source
# (github.com/qwinsi/bitcoin-whitepaper-latex): article class, Computer Modern,
# run-in bold "Abstract:", \maketitle author block. Anonymous author; nown.to + repo links; CC0.
set -euo pipefail
cd "$(dirname "$0")"

command -v pandoc >/dev/null || { echo "pandoc missing"; exit 1; }
export PATH="/Library/TeX/texbin:$PATH"
# Reproducible, metadata-free PDF: no build timestamp, no locale leak.
export SOURCE_DATE_EPOCH=0
command -v pdflatex >/dev/null || { echo "pdflatex missing"; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Figures: inject TikZ blocks from figures/manifest.json into a working copy.
SRC="WHITEPAPER.md"
# Figures frozen 2026-07-20 (with the sims) pending protocol finalization; PDF builds without them.
# To restore: re-add figure anchors to WHITEPAPER.md and uncomment below.
# if [ -f figures/manifest.json ]; then
#   python3 inject-figures.py md WHITEPAPER.md "$TMP/wp-fig.md"
#   SRC="$TMP/wp-fig.md"
# fi

# Abstract = the prose between "## Abstract" and the next "## " heading.
awk '/^## Abstract/{f=1;next} /^## /{f=0} f && NF' "$SRC" > "$TMP/abstract.txt"
# Body = everything from the first numbered section ("## 1.") to the end.
awk '/^## 1\./{p=1} p' "$SRC" > "$TMP/body.md"

# Feed the abstract to the template's $abstract$ slot via metadata.
{ echo "---"; echo "abstract: |"; sed 's/^/  /' "$TMP/abstract.txt"; echo "..."; } > "$TMP/meta.yaml"

# Output: repo clone has public/; the vault master writes beside the sources.
OUT="nown-whitepaper.pdf"; [ -d public ] && OUT="public/nown-whitepaper.pdf"

pandoc "$TMP/body.md" \
  --template=nown.latex \
  --metadata-file="$TMP/meta.yaml" \
  --pdf-engine=pdflatex \
  --shift-heading-level-by=-1 \
  -o "$OUT"

echo "OK -> $OUT ($(du -h "$OUT" | cut -f1), $(pdfinfo "$OUT" 2>/dev/null | awk '/Pages/{print $2" pages"}'))"
