#!/usr/bin/env bash
# Typeset a Nown paper into a research-grade PDF.
#
#   ./build-pdf.sh            -> WHITEPAPER.md      -> nown-whitepaper.pdf
#   ./build-pdf.sh article    -> ARTICLE.md         -> nown-article.pdf
#   ./build-pdf.sh win        -> what-is-nown.html  -> nown-what-is.pdf
#   ./build-pdf.sh all        -> all three
#
# The one-pager is hand-authored HTML, so win-to-md.py reads that page and emits
# the markdown this build typesets. The page stays the only source for its text.
#
# One engine, one source. The prose carries FIGURE markers; inject-figures.py
# resolves each marker to figures/<id>.tikz for print and the HTML renderers
# resolve the same marker to figures/<id>.svg, so page and print cannot drift.
# The build runs when the content changes, never when a reader asks for a copy:
# the button on the site serves this artifact, so a print costs nothing.
#
# Template: nown.latex, adapted from the Bitcoin whitepaper LaTeX source
# (github.com/qwinsi/bitcoin-whitepaper-latex): article class, Latin Modern (the
# Unicode descendant of Computer Modern, loaded through fontspec), run-in bold
# "Abstract:", \maketitle author block. Anonymous author; the Unlicense.
#
# Engine: XeLaTeX. Its output driver, xdvipdfmx, writes /Producer and
# /CreationDate after TeX has finished, so it is run with -V 4 (Info dictionary
# stays a plain object, not a compressed object stream) and the finished file is
# blanked below. Title and Author are the only fields a reader gets.
set -euo pipefail
cd "$(dirname "$0")"

command -v pandoc >/dev/null || { echo "pandoc missing"; exit 1; }
export PATH="/Library/TeX/texbin:$PATH"
# Reproducible, metadata-free PDF: no build timestamp, no locale leak.
export SOURCE_DATE_EPOCH=0
command -v xelatex >/dev/null || { echo "xelatex missing"; exit 1; }

TARGET="${1:-whitepaper}"
if [ "$TARGET" = "all" ]; then
  "$0" whitepaper
  "$0" article
  "$0" win
  exit 0
fi

case "$TARGET" in
  whitepaper) MD="WHITEPAPER.md"; PDF="nown-whitepaper.pdf"; TITLE="Nown: A Protocol for Portable Trust" ;;
  article)    MD="ARTICLE.md";    PDF="nown-article.pdf";    TITLE="Nown: Collaborative Research Paper" ;;
  win)        MD="what-is-nown.html"; PDF="nown-what-is.pdf"; TITLE="Nown: What is Nown?" ;;
  *) echo "usage: build-pdf.sh [whitepaper|article|win|all]"; exit 1 ;;
esac

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# The article is composed from its own source plus the whitepaper's section
# text (WP-INTRO markers), so the two surfaces cannot drift.
if [ "$TARGET" = "article" ]; then
  python3 compose-article.py ARTICLE.md WHITEPAPER.md "$TMP/composed.md"
  MD="$TMP/composed.md"
fi

# The one-pager's source is the page. win-to-md.py reads it and emits the same
# shape the other two carry: an Abstract slot, then numbered sections.
if [ "$TARGET" = "win" ]; then
  python3 win-to-md.py what-is-nown.html "$TMP/win.md"
  MD="$TMP/win.md"
fi

# Figures: every FIGURE marker in the prose becomes a TikZ figure from figures/<id>.tikz.
# A marker with no .tikz twin fails the build here rather than printing a figure-less paper.
SRC="$TMP/src-fig.md"
python3 inject-figures.py md "$MD" "$SRC"

# Abstract = the prose between "## Abstract" and the next "## " heading.
awk '/^## Abstract/{f=1;next} /^## /{f=0} f && NF' "$SRC" > "$TMP/abstract.txt"
# Body = everything from the first numbered section ("## 1.") to the end.
awk '/^## 1\./{p=1} p' "$SRC" > "$TMP/body.md"

# Endnotes: gather every note under "Notes" immediately before the references,
# which is where a reader of a printed paper expects them.
python3 - "$TMP/body.md" <<'PY'
import sys
p = sys.argv[1]
s = open(p).read()
block = "\n```{=latex}\n\\theendnotes\n```\n\n"
if "## References" in s:
    s = s.replace("## References", block + "## References", 1)

# Carousels print as framed minipages, one card per frame, full width.
import re
# inline reference citations: [cite:N] -> bracketed [N] (matches the References list, never a footnote)
s = re.sub(r"\[cite:(\d+)\]", r"[\1]", s)
s = re.sub(r"(?m)^EXPLORE\s*$\n?", "", s)
s = re.sub(r"(?m)^CAROUSEL-START.*$\n?", "", s)
s = re.sub(r"(?m)^CAROUSEL-END.*$\n?", "", s)
def card(m):
    title, body = m.group(1).strip(), m.group(2).strip()
    return ("```{=latex}\n\\par\\medskip\\noindent\\fbox{\\begin{minipage}{0.94\\linewidth}\\small\n"
            "\\textbf{" + title + ".}\\hspace{0.4em}\n```\n" + body +
            "\n```{=latex}\n\\end{minipage}}\\medskip\n```\n")
s = re.sub(r"(?m)^CARD\s*::\s*(.+?)\s*::\s*(.+)$", card, s)
open(p, "w").write(s)
PY

# Feed the abstract and the title to the template's slots via metadata.
{ echo "---"; echo "doctitle: \"$TITLE\""; echo "abstract: |"; sed 's/^/  /' "$TMP/abstract.txt"; echo "..."; } > "$TMP/meta.yaml"

# Output: repo clone has public/; the vault master keeps a copy beside the sources.
OUT="$PDF"; [ -d public ] && OUT="public/$PDF"

pandoc "$TMP/body.md" \
  --template=nown.latex \
  --metadata-file="$TMP/meta.yaml" \
  --pdf-engine=xelatex \
  --pdf-engine-opt="-output-driver=xdvipdfmx -V 4 -q -E" \
  --shift-heading-level-by=-1 \
  -o "$OUT"

# xdvipdfmx signs its work: /Producer names the tool and its build date, and
# /CreationDate stamps the file. Both are written after TeX has run, so they are
# removed here, overwritten with spaces so every byte offset in the cross
# reference table still points where it did. Title and Author survive.
python3 - "$OUT" <<'PY'
import re, sys
p = sys.argv[1]
d = open(p, 'rb').read()

# The trailer names the Info object; only that object is touched, so nothing in
# a content stream can be hit by accident.
m = re.search(rb'/Info\s+(\d+)\s+(\d+)\s+R', d)
if not m:
    sys.exit('build-pdf: no /Info reference in ' + p)
num, gen = m.group(1), m.group(2)
# The object number can also occur inside a compressed stream, so the one that
# carries the title is the Info dictionary.
om = next((c for c in re.finditer(rb'(?<![0-9])' + num + rb'\s+' + gen + rb'\s+obj(.*?)endobj',
                                  d, re.S) if b'/Title' in c.group(1)), None)
if not om:
    sys.exit(f'build-pdf: Info object {num.decode()} not found in {p} '
             '(is the driver still writing an object stream?)')

info = om.group(1)
for key in (b'Producer', b'Creator', b'CreationDate', b'ModDate'):
    info = re.sub(rb'/' + key + rb'\s*\((?:\\.|[^()\\])*\)',
                  lambda mm: b' ' * len(mm.group(0)), info)
left = [k for k in (b'Producer', b'Creator', b'CreationDate', b'ModDate') if b'/' + k in info]
if left:
    sys.exit('build-pdf: metadata left in ' + p + ': ' + b','.join(left).decode())

# Same length in, same length out: every cross reference offset still points
# where it did, so the file needs no repair.
d = d[:om.start(1)] + info + d[om.end(1):]

# The trailer id is the last thing that varies between two builds of the same
# text: the driver draws it fresh each run. Deriving it from the file's own
# bytes makes it a fingerprint of the content instead, so an unchanged source
# produces an identical file, and two different papers still differ.
import hashlib
idre = re.compile(rb'/ID\s*\[\s*<[0-9A-Fa-f]*>\s*<[0-9A-Fa-f]*>\s*\]')
if not idre.search(d):
    sys.exit('build-pdf: no trailer /ID in ' + p)
def rewrite(fill):
    """Replace the digits between < and >, never the D of /ID, keeping length."""
    return lambda mm: re.sub(rb'<[0-9A-Fa-f]*>',
                             lambda h: b'<' + fill(len(h.group(0)) - 2) + b'>',
                             mm.group(0))

zeroed = idre.sub(rewrite(lambda n: b'0' * n), d)
tid = hashlib.md5(zeroed).hexdigest().encode()
out = idre.sub(rewrite(lambda n: (tid * 2)[:n]), zeroed)
if len(out) != len(d) or re.search(rb'/ID\s*\[\s*<0+>', out):
    sys.exit('build-pdf: trailer id rewrite failed on ' + p)
open(p, 'wb').write(out)
PY

# Keep the vault copy in step with the served one.
[ "$OUT" != "$PDF" ] && cp "$OUT" "$PDF"

echo "OK -> $OUT ($(du -h "$OUT" | cut -f1), $(pdfinfo "$OUT" 2>/dev/null | awk '/Pages/{print $2" pages"}'))"
