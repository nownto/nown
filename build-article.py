#!/usr/bin/env python3
"""Build nown-article.html (the long-form companion) from ARTICLE.md.

Reuses the whitepaper HTML shell (head, styles, design tokens, topbar, theme JS),
renders the 19 sections with their subsections and display formulas, places the six
built figures by topic, and embeds the six interactive simulations at section 19.

Usage: build-article.py
"""
import re, os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(ROOT, 'build')  # sim sources live in the repo (relocated 2026-07-20 from a stale temp path; reproducible, single-source)

# Figures FROZEN 2026-07-20 with the sims: the built figures encode the OLD burn/tenure model and its
# section numbering, so none is placed until they are regenerated for the finalized protocol. The article
# stands on prose. To restore, repopulate this map {figure-id: new-section-number} once figures are rebuilt.
FIG_AT = {}


def enc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&rsquo;'))


# Footnotes: [^id] markers in the prose become click/hover popups; [^id]: text lines define them.
_FN = {}


def _fn_markup(word, fid):
    if fid not in _FN:
        return f'{word}[^{fid}]'
    n, text = _FN[fid]
    return (f'<span class="fnw"><span class="fna">{word}</span>'
            f'<sup class="fn"><button type="button" class="fnr" aria-expanded="false" '
            f'aria-label="Footnote {n}">{n}</button></sup>'
            f'<span class="fnpop" role="note">{enc(text)}</span></span>')


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


def is_math(p):
    return ('=' in p and len(p) < 130 and '\n' not in p
            and p.count(' ') < 22 and not p.rstrip().endswith(('.', ':', ',')))


def render_paragraph(p):
    p = re.sub(r'\s+', ' ', p.strip())
    if is_math(p):
        return f'      <p class="math">{enc(p)}</p>'
    # bold and italic passthrough
    body = enc(p)
    body = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', body)
    body = re.sub(r'\*(.+?)\*', r'<i>\1</i>', body)
    body = re.sub(r'([^\s<>]+)\[\^(\w+)\]', lambda m: _fn_markup(m.group(1), m.group(2)), body)
    body = re.sub(r'\[\^(\w+)\]', lambda m: _fn_markup('', m.group(1)), body)
    return f'      <p>{body}</p>'


def parse_article(md):
    title = next(l[2:].strip() for l in md.split('\n') if l.startswith('# '))
    subtitle = ''
    ms = re.search(r'^### (.+)$', md, re.M)
    if ms:
        subtitle = re.sub(r'[*]', '', ms.group(1)).strip()
    abs_m = re.search(r'## Abstract\s*\n(.*?)(?=\n## )', md, re.S)
    abstract = [p.strip() for p in re.split(r'\n\n+', abs_m.group(1).strip()) if p.strip()]
    secs = []
    for m in re.finditer(r'## (\d+)\. (.+?)\n(.*?)(?=\n## \d+\. |\n## References|\Z)', md, re.S):
        num, ttl, body = int(m.group(1)), m.group(2).strip(), m.group(3)
        # split into intro paragraphs + subsections
        blocks = []
        pos = 0
        for sm in re.finditer(r'### (\d+\.\d+)\s+(.+)', body):
            pre = body[pos:sm.start()].strip()
            if pre:
                blocks.append(('paras', pre))
            blocks.append(('sub', sm.group(1) + '  ' + sm.group(2).strip()))
            pos = sm.end()
        tail = body[pos:].strip()
        if tail:
            blocks.append(('paras', tail))
        if not blocks:
            blocks = [('paras', body.strip())]
        secs.append((num, ttl, blocks))
    ref_m = re.search(r'## References\s*\n(.*?)(?=\n---|\Z)', md, re.S)
    refs = []
    if ref_m:
        for rl in ref_m.group(1).strip().split('\n'):
            rm = re.match(r'^\d+\.\s+(.+)', rl.strip())
            if rm:
                refs.append(rm.group(1).strip())
    return title, subtitle, abstract, secs, refs


def render_paras(text):
    out = []
    for p in re.split(r'\n\n+', text):
        p = p.strip()
        if not p:
            continue
        # inline figure: "FIGURE <id> :: <caption>" -> read figures/<id>.svg
        fm = re.match(r'^FIGURE\s+([\w-]+)\s*::\s*(.+)$', p, re.S)
        if fm:
            svg = open(os.path.join(ROOT, 'figures', fm.group(1) + '.svg')).read().strip()
            cap = re.sub(r'\s+', ' ', fm.group(2).strip())
            out.append('      <figure class="wpfig">')
            out.append(f'        <div class="fig-frame">{svg}</div>')
            out.append(f'        <figcaption>{enc(cap)}</figcaption>')
            out.append('      </figure>')
            continue
        # bullet list?
        if all(l.strip().startswith(('- ', '* ')) for l in p.split('\n') if l.strip()):
            out.append('      <ul>')
            for l in p.split('\n'):
                if l.strip():
                    out.append(f'        <li>{enc(re.sub(r"^[-*] ", "", l.strip()))}</li>')
            out.append('      </ul>')
        else:
            out.append(render_paragraph(p))
    return out


def build():
    md = extract_footnotes(open(os.path.join(ROOT, 'ARTICLE.md')).read())
    title, subtitle, abstract, secs, refs = parse_article(md)
    shell = open(os.path.join(ROOT, 'nown-whitepaper.html')).read()

    figs = {f['id']: f for f in json.load(open(os.path.join(ROOT, 'figures/manifest.json')))}
    fig_svg = {fid: open(os.path.join(ROOT, 'figures', fid + '.svg')).read().strip() for fid in FIG_AT}
    # Simulations FROZEN 2026-07-20 (Niko: leave them out until the protocol is nailed down).
    # Sources kept in build/sim-*.txt; to restore, uncomment the three reads below.
    sim_css = sim_markup = sim_js = ''
    # sim_css = open(os.path.join(SP, 'sim-css.txt')).read()
    # sim_markup = open(os.path.join(SP, 'sim-markup.html')).read()
    # sim_js = open(os.path.join(SP, 'sim-js.txt')).read()

    # --- head: take shell head, append sim CSS before </style> (last style close in head) ---
    head_end = shell.index('</head>')
    head = shell[:head_end]
    # retarget canonical/og URLs and title to the article
    head = head.replace('nown-whitepaper.html', 'nown-article.html')
    head = re.sub(r'<title>.*?</title>',
                  '<title>Nown: The Full Construction &middot; companion article</title>', head, flags=re.S)
    head = head[:head.rindex('</style>')] + '\n/* --- embedded simulations --- */\n' + sim_css + \
        '\n#simulations .math{ display:none }\n' + head[head.rindex('</style>'):]
    # math style
    head = head.replace('</style>', ".math{ font-family:var(--mono); text-align:center; font-size:1rem; "
                        "color:var(--ink); margin:1.1rem auto; letter-spacing:.02em }\n"
                        ".subsec{ font-family:var(--serif); font-weight:600; font-size:1.16rem; "
                        "color:var(--ink); margin:2.1rem 0 .3rem; letter-spacing:-.01em }\n"
                        ".wpfig{ margin:2rem 0; }\n"
                        ".wpfig .fig-frame svg{ display:block; width:100%; height:auto; max-width:560px; margin:0 auto }\n</style>", 1)

    # --- topbar / brand: reuse from shell (between </head> and <div class="wrap">) ---
    wrap_i = shell.index('<div class="wrap">')
    top = shell[head_end + len('</head>'):wrap_i]
    # brand nav: keep the Whitepaper link pointing to the whitepaper, mark Article as the current page
    top = top.replace('<a href="nown-whitepaper.html" class="bcur" aria-current="page">Whitepaper</a>',
                      '<a href="nown-whitepaper.html">Whitepaper</a>')
    top = top.replace('<a href="nown-article.html">Article</a>',
                      '<a href="nown-article.html" class="bcur" aria-current="page">Article</a>')
    # The article is web-only (no typeset PDF). Swap the inherited PDF link for a
    # Print control (window.print()) so the reader chrome parallels the whitepaper's;
    # every other reader control comes through from the shell unchanged.
    print_btn = (
        '<button class="btn" id="printBtn" type="button" title="Print this article" aria-label="Print this article">\n'
        '      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2'
        'h16a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2M6 14h12v7H6z"/></svg>\n'
        '      <span class="blab">Print</span>\n'
        '    </button>')
    top = re.sub(r'<a class="btn" id="pdfBtn".*?</a>', lambda m: print_btn, top, count=1, flags=re.S)

    # --- TOC ---
    toc = ['      <li><a href="#abstract"><span class="n">&middot;</span> Abstract</a></li>',
           '      <li class="sepli"><span class="sep"></span></li>']
    for num, ttl, _ in secs:
        toc.append(f'      <li><a href="#s{num}"><span class="n">{num}</span> {enc(ttl)}</a></li>')
    toc.append('      <li class="sepli"><span class="sep"></span></li>')
    toc.append('      <li><a href="#refs"><span class="n">&middot;</span> References</a></li>')

    # --- title block ---
    titleblock = f'''    <section class="title" id="top">
      <p class="eyebrow">Companion article &middot; full construction</p>
      <h1 class="name">Nown</h1>
      <p class="subtitle">{enc(subtitle)}</p>
      <p class="thesis">The construction the short paper states in brief, built here <b>in full</b>.</p>
      <div class="meta"><span>v0.1</span><span class="dot">&middot;</span><span>companion to the whitepaper</span><span class="dot">&middot;</span><span>Public domain &middot; the Unlicense</span></div>
      <p style="margin-top:1.4rem"><a href="nown-whitepaper.html">Read the short whitepaper first &rsaquo;</a></p>
    </section>'''

    # --- abstract ---
    parts = [titleblock, '\n    <section class="abstract" id="abstract">', '      <p class="lbl">Abstract</p>']
    for p in abstract:
        parts += render_paras(p)
    parts.append('    </section>')

    # --- sections ---
    for num, ttl, blocks in secs:
        parts.append(f'\n    <section id="s{num}">')
        parts.append(f'      <h2 class="sec"><span class="num">&sect;{num}</span> {enc(ttl)}</h2>')
        # figure for this section, if any
        figid = next((fid for fid, sn in FIG_AT.items() if sn == num), None)
        if figid:
            parts.append('      <figure class="wpfig">')
            parts.append(f'        <div class="fig-frame">{fig_svg[figid]}</div>')
            parts.append(f'        <figcaption>{enc(figs[figid]["caption"])}</figcaption>')
            parts.append('      </figure>')
        for kind, content in blocks:
            if kind == 'sub':
                parts.append(f'      <h3 class="subsec">{enc(content)}</h3>')
            else:
                # strip FIGURE/SIM marker lines
                content = '\n'.join(l for l in content.split('\n') if not l.strip().startswith('FIGURE/SIM'))
                parts += render_paras(content)
        # embed the six interactive sims inside section 19
        if num == 19:
            parts.append('    </section>')
            parts.append('\n' + sim_markup)
            continue
        parts.append('    </section>')

    # --- references ---
    parts.append('\n    <section id="refs" class="refs">')
    parts.append('      <h2 class="sec"><span class="num">&sect;</span> References</h2>')
    parts.append('      <div class="reflist">')
    for i, r in enumerate(refs, 1):
        parts.append(f'        <div class="refrow"><span class="theme">[{i}]</span><span class="src">{enc(r)}</span></div>')
    parts.append('      </div>')
    parts.append('    </section>')

    body_content = '\n'.join(parts)

    # --- assemble: shell wrap through <main>, our content, </main> + footer/scripts ---
    main_open = shell.index('<main>', wrap_i) + len('<main>')
    toc_block = re.sub(r'(<nav class="toc"[^>]*>.*?<ol>\n).*?(\n\s*</ol>)',
                       lambda m: m.group(1) + '\n'.join(toc) + m.group(2),
                       shell[wrap_i:main_open], count=1, flags=re.S)
    footer_i = shell.index('</main>')
    tail = shell[footer_i:]  # </main> ... footer ... scripts ... </html>
    # inject sim JS just before the closing </body>
    tail = tail.replace('</body>', f'<script>\n{sim_js}\n</script>\n</body>', 1)

    out = head + '</head>' + top + toc_block + '\n' + body_content + '\n\n  ' + tail
    open(os.path.join(ROOT, 'nown-article.html'), 'w').write(out)
    print(f'built nown-article.html: {len(secs)} sections, {len(refs)} refs (figures+sims frozen), {len(out):,} bytes')


if __name__ == '__main__':
    build()
