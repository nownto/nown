#!/usr/bin/env python3
"""Figures, from one source: the FIGURE markers in the prose.

A marker line in WHITEPAPER.md / ARTICLE.md reads:

    FIGURE <id> :: <caption>

and is the only place a figure is declared. Every renderer resolves the same
marker against the same id:

    figures/<id>.svg   -> the HTML renders (render-whitepaper-html.py, build-article.py)
    figures/<id>.tikz  -> the LaTeX print (build-pdf.sh, via this script)

so the paper, the page, and the print cannot drift. A marker whose .tikz is
missing fails the build loudly rather than printing a figure-less paper.

Usage:
  inject-figures.py md   WHITEPAPER.md OUT.md     # FIGURE markers -> raw-latex figure blocks
  inject-figures.py check WHITEPAPER.md [MORE.md] # every marker has both twins
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(ROOT, 'figures')
MARKER = re.compile(r'^FIGURE\s+([\w-]+)\s*::\s*(.+?)\s*$', re.M | re.S)


def markers(text):
    """Every FIGURE marker in source order, as (id, caption, whole_line)."""
    out = []
    for line in text.split('\n'):
        m = MARKER.match(line)
        if m:
            out.append((m.group(1), m.group(2), line))
    return out


def twins(fid):
    return (os.path.join(FIG, fid + '.svg'), os.path.join(FIG, fid + '.tikz'))


def check(paths):
    missing = []
    for p in paths:
        for fid, _cap, _line in markers(open(p).read()):
            svg, tikz = twins(fid)
            for f in (svg, tikz):
                if not os.path.exists(f):
                    missing.append(f'{os.path.basename(p)}: {fid} -> missing {os.path.relpath(f, ROOT)}')
    if missing:
        for m in missing:
            print('  FAIL: ' + m, file=sys.stderr)
        return 1
    return 0


def inject_md(src, dst):
    text = open(src).read()
    for fid, caption, line in markers(text):
        _svg, tikz = twins(fid)
        if not os.path.exists(tikz):
            sys.exit(f'inject-figures: {fid} has no figures/{fid}.tikz (print would drop the figure)')
        body = open(tikz).read().strip()
        block = ('```{=latex}\n\\begin{figure}[hbt]\\centering\n' + body +
                 f'\n\\figcap{{{caption}}}\n\\end{{figure}}\n```')
        text = text.replace(line, block, 1)
    open(dst, 'w').write(text)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'check':
        sys.exit(check(sys.argv[2:]))
    if len(sys.argv) == 4 and sys.argv[1] == 'md':
        inject_md(sys.argv[2], sys.argv[3])
        sys.exit(0)
    sys.exit(__doc__)
