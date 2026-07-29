#!/usr/bin/env python3
"""One-pager, one source: what-is-nown.html -> markdown for the typeset print.

The one-pager is hand-authored HTML, not markdown, so there is nothing for
pandoc to read. A second copy of the text would be a second source, and two
sources drift. This reads the page itself and emits the markdown that
build-pdf.sh feeds to the same template as the whitepaper and the article:

    # <the page title>
    ## Abstract
    <the hook line, then the lede>
    ## 1. <concept>
    - <bullet>
    ...

so the shape is the one the build already understands: the abstract slot, then
numbered sections whose numbers live in the heading text (the template's
secnumdepth is 0).

Usage:
  win-to-md.py what-is-nown.html OUT.md   # write the markdown ('-' = stdout)
  win-to-md.py count what-is-nown.html    # print the concept count, for verify.sh
"""
import html
import re
import sys

CARD = re.compile(r'<div class="c">\s*<h2>(.*?)</h2>\s*<ul>(.*?)</ul>\s*</div>', re.S)
LI = re.compile(r'<li>(.*?)</li>', re.S)
TAG = re.compile(r'<[^>]+>')
# LaTeX would read these as syntax; pandoc escapes markdown, not raw specials.
SPECIAL = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
           '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
           '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}


def text(fragment):
    """Tag-free, entity-free, single-spaced text, safe to typeset."""
    t = html.unescape(TAG.sub('', fragment))
    t = re.sub(r'\s+', ' ', t).strip()
    return ''.join(SPECIAL.get(c, c) for c in t)


def parse(src):
    page = open(src).read()
    title = text(re.search(r'<title>(.*?)</title>', page, re.S).group(1))
    hook = text(re.search(r'<h1 class="hook">(.*?)</h1>', page, re.S).group(1))
    lede = text(re.search(r'<p class="lede">(.*?)</p>', page, re.S).group(1))
    cards = [(text(m.group(1)), [text(li) for li in LI.findall(m.group(2))])
             for m in CARD.finditer(page)]
    if not cards:
        sys.exit('win-to-md: no concept cards found in ' + src)
    return title, hook, lede, cards


def to_md(src):
    title, hook, lede, cards = parse(src)
    out = ['# ' + title, '', '## Abstract', '', hook + ' ' + lede + '.', '']
    for n, (name, bullets) in enumerate(cards, 1):
        out.append(f'## {n}. {name}')
        out.append('')
        out.extend('- ' + b for b in bullets)
        out.append('')
    return '\n'.join(out)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'count':
        print(len(parse(sys.argv[2])[3]))
    elif len(sys.argv) == 3:
        md = to_md(sys.argv[1])
        if sys.argv[2] == '-':
            sys.stdout.write(md)
        else:
            open(sys.argv[2], 'w').write(md)
    else:
        sys.exit(__doc__)
