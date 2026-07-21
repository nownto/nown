#!/usr/bin/env python3
"""Regenerate the content of nown-whitepaper.html from WHITEPAPER.md.

WHITEPAPER.md is the single source. This preserves the HTML shell (head, styles,
brand nav, title block chrome, footer, scripts) and regenerates the parts that
carry paper text: the table of contents, the version strings, the abstract, the
numbered sections, and the references. Figures are injected afterward by
inject-figures.py from figures/manifest.json, so this never touches figure SVGs.

Usage: render-whitepaper-html.py WHITEPAPER.md nown-whitepaper.html
"""
import sys, re


def enc(t):
    t = t.replace('&', '&amp;')
    t = t.replace('<', '&lt;').replace('>', '&gt;')
    t = t.replace("'", '&rsquo;')
    t = re.sub(r'\bv(\d)', r'v\1', t)
    return t


def _anchor(url, text):
    ext = '' if 'nown.to' in url else ' target="_blank" rel="noopener noreferrer"'
    return f'<a href="{url}"{ext}>{text}</a>'


def _linkify_bare(escaped):
    # wrap bare http(s) urls in already-escaped text
    return re.sub(r'(https?://[^\s<)\]]+)', lambda m: _anchor(m.group(1), m.group(1)), escaped)


def render_text(t):
    # markdown [text](url) links first, then bare urls in the surrounding escaped text
    out, pos = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)', t):
        out.append(_linkify_bare(enc(t[pos:m.start()])))
        out.append(_anchor(m.group(2), enc(m.group(1))))
        pos = m.end()
    out.append(_linkify_bare(enc(t[pos:])))
    return re.sub(r'\[\^(\w+)\]', lambda m: _fn_markup(m.group(1)), ''.join(out))


# Footnotes: [^id] markers become click/hover popups; [^id]: text lines define them.
_FN = {}


def _fn_markup(fid):
    if fid not in _FN:
        return f'[^{fid}]'
    n, text = _FN[fid]
    return (f'<sup class="fn"><button type="button" class="fnr" aria-label="Note {n}">{n}</button>'
            f'<span class="fnpop" role="note">{enc(text)}</span></sup>')


def extract_footnotes(md):
    defs = dict(re.findall(r'(?m)^\[\^(\w+)\]:[ \t]*(.+)$', md))
    md = re.sub(r'(?m)^\[\^\w+\]:[ \t]*.+\n?', '', md)
    _FN.clear()
    seen = []
    for mm in re.finditer(r'\[\^(\w+)\]', md):
        fid = mm.group(1)
        if fid in defs and fid not in seen:
            seen.append(fid)
    for n, fid in enumerate(seen, 1):
        _FN[fid] = (n, defs[fid])
    return md


def parse_md(md):
    title = next(l[2:].strip() for l in md.split('\n') if l.startswith('# '))
    mver = re.search(r'\*\*v([0-9.]+)\.\*\*', md)
    ver = 'v' + (mver.group(1) if mver else '0.5')
    abs_m = re.search(r'## Abstract\s*\n(.*?)(?=\n## )', md, re.S)
    abstract = [re.sub(r'\s+', ' ', p.strip()) for p in re.split(r'\n\n+', abs_m.group(1).strip()) if p.strip()]
    secs = []
    for m in re.finditer(r'## (\d+)\. (.+?)\n(.*?)(?=\n## |\Z)', md, re.S):
        paras = [re.sub(r'\s+', ' ', p.strip()) for p in re.split(r'\n\n+', m.group(3).strip()) if p.strip()]
        secs.append((int(m.group(1)), m.group(2).strip(), paras))
    ref_m = re.search(r'## References\s*\n(.*?)(?=\n---|\Z)', md, re.S)
    note, refs = '', []
    for para in re.split(r'\n\n+', ref_m.group(1).strip()):
        para = para.strip()
        if re.match(r'^\d+\. ', para):
            for rl in para.split('\n'):
                rm = re.match(r'^\d+\. (.+)', rl.strip())
                if rm:
                    refs.append(rm.group(1).strip())
        elif para and not note:
            note = re.sub(r'\s+', ' ', para)
    return title, ver, abstract, secs, note, refs


def build(md_path, html_path):
    md = extract_footnotes(open(md_path).read())
    title, ver, abstract, secs, note, refs = parse_md(md)
    h = open(html_path).read()

    # 1. TOC
    toc = ['      <li><a href="#abstract"><span class="n">&middot;</span> Abstract</a></li>',
           '      <li class="sepli"><span class="sep"></span></li>']
    for num, ttl, _ in secs:
        toc.append(f'      <li><a href="#s{num}"><span class="n">{num}</span> {enc(ttl)}</a></li>')
    toc.append('      <li class="sepli"><span class="sep"></span></li>')
    toc.append('      <li><a href="#refs"><span class="n">&middot;</span> References</a></li>')
    h = re.sub(r'(<nav class="toc"[^>]*>.*?<ol>\n).*?(\n\s*</ol>)',
               lambda m: m.group(1) + '\n'.join(toc) + m.group(2), h, count=1, flags=re.S)

    # 2. version strings in the title block
    h = re.sub(r'<p class="eyebrow">Whitepaper[^<]*</p>', f'<p class="eyebrow">Whitepaper &middot; {ver}</p>', h)
    h = re.sub(r'(<div class="meta">\s*<span>)v[0-9.]+(</span>)', rf'\g<1>{ver}\g<2>', h)

    # 3. content region: abstract through references (regenerated wholesale)
    parts = []
    parts.append('    <section class="abstract" id="abstract">')
    parts.append('      <p class="lbl">Abstract</p>')
    for p in abstract:
        parts.append(f'      <p>{render_text(p)}</p>')
    parts.append('    </section>')
    for num, ttl, paras in secs:
        parts.append(f'\n    <section id="s{num}">')
        parts.append(f'      <h2 class="sec"><span class="num">&sect;{num}</span> {enc(ttl)}</h2>')
        for p in paras:
            parts.append(f'      <p>{render_text(p)}</p>')
        parts.append('    </section>')
    parts.append('\n    <section id="refs" class="refs">')
    parts.append('      <h2 class="sec"><span class="num">&sect;</span> References</h2>')
    if note:
        parts.append(f'      <p>{render_text(note)}</p>')
    parts.append('      <div class="reflist">')
    for i, r in enumerate(refs, 1):
        parts.append(f'        <div class="refrow"><span class="theme">[{i}]</span><span class="src">{render_text(r)}</span></div>')
    parts.append('      </div>')
    parts.append('    </section>')
    content = '\n'.join(parts)

    i = h.find('<section class="abstract" id="abstract">')
    j = h.find('</section>', h.find('<section id="refs"')) + len('</section>')
    # keep the leading indentation of the abstract section
    line_start = h.rfind('\n', 0, i) + 1
    h = h[:line_start] + content + h[j:]

    open(html_path, 'w').write(h)
    print(f'rendered {len(secs)} sections + {len(refs)} refs, {ver}, into {html_path}')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
