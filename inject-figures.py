#!/usr/bin/env python3
"""Single source of truth for whitepaper figures.

figures/manifest.json: [{id, number, anchor, caption}]
figures/<id>.tikz  -> injected into the markdown as raw LaTeX (for build-pdf.sh)
figures/<id>.svg   -> injected into nown-whitepaper.html (HOLD-wrapped until released)

Usage:
  inject-figures.py md  WHITEPAPER.md OUT.md      # raw-latex figure blocks after anchors
  inject-figures.py html nown-whitepaper.html OUT.html
Anchors must match the source verbatim, exactly once. Fails loudly otherwise.
"""
import json, sys, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(ROOT, 'figures')

def load():
    man = json.load(open(os.path.join(FIG, 'manifest.json')))
    return sorted(man, key=lambda f: f['number'])

def inject_md(src, dst):
    s = open(src).read()
    for f in load():
        tikz = open(os.path.join(FIG, f['id'] + '.tikz')).read().strip()
        n = s.count(f['anchor'])
        assert n == 1, f"{f['id']}: anchor found {n} times in {src}"
        # LaTeX auto-numbers figures; pass only the caption text.
        block = ('\n\n```{=latex}\n\\begin{figure}[hbt]\\centering\n' + tikz +
                 f"\n\\figcap{{{f['caption']}}}\n\\end{{figure}}\n```\n")
        i = s.find('\n\n', s.find(f['anchor']))
        if i < 0: i = len(s)
        s = s[:i] + block + s[i:]
    open(dst, 'w').write(s)
    print(f"md: {len(load())} figures -> {dst}")

def html_anchor(a):
    # match the entity encoding render-whitepaper-html.py applies to prose
    return (a.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace("'", '&rsquo;'))


def inject_html(src, dst):
    s = open(src).read()
    for f in load():
        svg = open(os.path.join(FIG, f['id'] + '.svg')).read().strip()
        anchor = f['anchor'] if s.count(f['anchor']) == 1 else html_anchor(f['anchor'])
        n = s.count(anchor)
        assert n == 1, f"{f['id']}: anchor found {n} times in {src}"
        i = s.find('</p>', s.find(anchor)) + len('</p>')
        # Figures are public paper content (the "helpful graphs" Niko publishes), not held.
        block = (f'\n<figure id="fig-{f["id"]}">\n'
                 f'  <div class="fig-frame">{svg}</div>\n'
                 f'  <figcaption>Figure {f["number"]}. {html.escape(f["caption"], quote=False)}</figcaption>\n'
                 f'</figure>')
        s = s[:i] + block + s[i:]
    open(dst, 'w').write(s)
    print(f"html: {len(load())} figures -> {dst}")

if __name__ == '__main__':
    mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    (inject_md if mode == 'md' else inject_html)(src, dst)
