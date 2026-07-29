#!/usr/bin/env python3
"""Compose the article from ARTICLE.md + WHITEPAPER.md.

The article mirrors the whitepaper section for section. In ARTICLE.md each
section's WP-INTRO line marks where the whitepaper's text for the same
heading is injected verbatim, so the two surfaces cannot drift, and an
EXPLORE line marks where the section's research part begins (the HTML
renders it as a disclosure; the print runs continuously). Footnote
definitions come from the whitepaper first; ARTICLE.md adds only ids the
whitepaper does not define.

Usage: compose-article.py [ARTICLE.md WHITEPAPER.md OUT.md]
With no arguments, prints the composed text to stdout.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def compose(article_path, wp_path):
    art = open(article_path).read()
    wp = open(wp_path).read()

    # whitepaper footnote definitions are the source; the article adds only new ids
    wp_defs = re.findall(r'(?m)^(\[\^(\w+)\]:[ \t]*.+)$', wp)
    wp_ids = {fid for _, fid in wp_defs}
    art_defs = re.findall(r'(?m)^\[\^(\w+)\]:', art)
    dup = [fid for fid in art_defs if fid in wp_ids]
    if dup:
        sys.exit(f'compose-article: footnote id(s) defined in both sources: {", ".join(dup)} (whitepaper is the source)')

    def strip_defs(t):
        return re.sub(r'(?m)^\[\^\w+\]:[ \t]*.+\n?', '', t).strip()

    wp_secs = {}
    am = re.search(r'## Abstract\s*\n(.*?)(?=\n## )', wp, re.S)
    wp_secs['Abstract'] = strip_defs(am.group(1))
    for sm in re.finditer(r'## \d+\. (.+?)\n(.*?)(?=\n## |\Z)', wp, re.S):
        wp_secs[sm.group(1).strip()] = strip_defs(sm.group(2))

    # the article's numbered sections must be the whitepaper's, one to one
    art_titles = re.findall(r'(?m)^## \d+\. (.+)$', art)
    wp_titles = re.findall(r'(?m)^## \d+\. (.+)$', wp)
    if art_titles != wp_titles:
        sys.exit('compose-article: section titles diverge from the whitepaper:\n'
                 f'  whitepaper: {wp_titles}\n  article:    {art_titles}')

    out, cur = [], None
    for line in art.split('\n'):
        hm = re.match(r'## (?:\d+\. )?(.+)$', line)
        if hm:
            cur = hm.group(1).strip()
        if line.strip() == 'WP-INTRO':
            if cur not in wp_secs:
                sys.exit(f'compose-article: WP-INTRO under "{cur}", which the whitepaper does not carry')
            out.append(wp_secs.pop(cur))
        else:
            out.append(line)

    text = '\n'.join(out)
    return text.rstrip() + '\n' + '\n'.join(d for d, _ in wp_defs) + '\n'


if __name__ == '__main__':
    if len(sys.argv) == 4:
        open(sys.argv[3], 'w').write(compose(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 1:
        sys.stdout.write(compose(os.path.join(ROOT, 'ARTICLE.md'), os.path.join(ROOT, 'WHITEPAPER.md')))
    else:
        sys.exit(__doc__)
