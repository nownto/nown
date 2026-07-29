#!/usr/bin/env python3
"""Build nown-article.html from the composed article source.

compose-article.py injects each section's whitepaper text at its WP-INTRO
marker, so the article mirrors the whitepaper section for section. The EXPLORE
marker splits a section: the whitepaper text renders as the section's intro,
and everything after EXPLORE renders inside a "Let's explore more" disclosure.
The shell (head, styles, design tokens, topbar, theme JS) is reused from
nown-whitepaper.html.

Usage: build-article.py
"""
import re, os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(ROOT, 'build')  # sim sources live in the repo (reproducible, single-source; sims frozen)


def enc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&rsquo;'))


# Footnotes: [^id] markers in the prose become click/hover popups; [^id]: text lines define them.
_FN = {}


def _fn_markup(word, fid):
    if fid not in _FN:
        return f'{word}[^{fid}]'
    n, text = _FN[fid]
    return (f'<span class="fnw"><button type="button" class="fnterm" aria-expanded="false">{word}'
            f'<sup class="fnnum">{n}</sup></button>'
            f'<span class="fnpop" role="note">{enc(text)}</span></span>')


# A footnote anchors to the whole TERM, never the last word before the marker.
# Niko, 2026-07-22: "block time" takes the note, not "time".
ANCHOR_WORDS = {'blocktime': 2, 'dot': 2, 'pgt': 3, 'vdf': 3, 'karma': 1, 'oracle': 1,
                'quorum': 1, 'steward': 1, 'seal': 1, 'key': 1, 'pgp': 1, 'web': 1}


def _anchor_sub(m):
    phrase, fid = m.group(1), m.group(2)
    n = ANCHOR_WORDS.get(fid, 1)
    words = phrase.split()
    if len(words) < n:
        return _fn_markup(phrase, fid)
    lead = words[:-n]
    head = (' '.join(lead) + ' ') if lead else ''
    return head + _fn_markup(' '.join(words[-n:]), fid)


ANCHOR_RE = r'((?:[^\s<>]+ ){0,3}[^\s<>]+)\[\^(\w+)\]'


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


_CITE_SEEN = set()


def _cite_sub(m):
    """First mention of a reference carries the id the back link points at."""
    n = m.group(1)
    if n in _CITE_SEEN:
        return f'<a class="refcite" href="#ref{n}">[{n}]</a>'
    _CITE_SEEN.add(n)
    return f'<a class="refcite" id="cite{n}" href="#ref{n}">[{n}]</a>'


def render_paragraph(p):
    p = re.sub(r'\s+', ' ', p.strip())
    if is_math(p):
        return f'      <p class="math">{enc(p)}</p>'
    # markdown links [text](url) survive escaping and become anchors
    links = []

    def _stash(m):
        links.append((m.group(1), m.group(2)))
        return f'\x00LINK{len(links) - 1}\x00'

    p = re.sub(r'\[([^\]]+)\]\((https?://[^)]+|[\w./-]+\.html)\)', _stash, p)
    # bold and italic passthrough
    body = enc(p)
    for i, (text, url) in enumerate(links):
        tgt = '' if not url.startswith('http') else ' target="_blank" rel="noopener noreferrer"'
        body = body.replace(f'\x00LINK{i}\x00', f'<a href="{url}"{tgt}>{enc(text)}</a>')
    body = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', body)
    body = re.sub(r'\*(.+?)\*', r'<i>\1</i>', body)
    body = re.sub(ANCHOR_RE, _anchor_sub, body)
    body = re.sub(r'\[\^(\w+)\]', lambda m: _fn_markup('', m.group(1)), body)
    body = re.sub(r'\[cite:(\d+)\]', _cite_sub, body)
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
    for m in re.finditer(r'## (\d+)\. (.+?)\n(.*?)(?=\n## \d+\. |\n## References|\n## Closing|\Z)', md, re.S):
        num, ttl, body = int(m.group(1)), m.group(2).strip(), m.group(3)
        # EXPLORE splits the whitepaper intro from the research part
        explore = None
        if re.search(r'(?m)^EXPLORE\s*$', body):
            body, explore = re.split(r'(?m)^EXPLORE\s*$\n?', body, maxsplit=1)

        def blockify(text):
            blocks, pos = [], 0
            for sm in re.finditer(r'### (.+)', text):
                pre = text[pos:sm.start()].strip()
                if pre:
                    blocks.append(('paras', pre))
                blocks.append(('sub', sm.group(1).strip()))
                pos = sm.end()
            tail = text[pos:].strip()
            if tail:
                blocks.append(('paras', tail))
            return blocks

        secs.append((num, ttl, blockify(body), blockify(explore) if explore else None))
    close_m = re.search(r'## Closing\s*\n(.*?)(?=\n## )', md, re.S)
    closing = [p.strip() for p in re.split(r'\n\n+', close_m.group(1).strip())] if close_m else []
    ref_m = re.search(r'## References\s*\n(.*?)(?=\n---|\Z)', md, re.S)
    refs = []
    if ref_m:
        for rl in ref_m.group(1).strip().split('\n'):
            rm = re.match(r'^\d+\.\s+(.+)', rl.strip())
            if rm:
                refs.append(rm.group(1).strip())
    return title, subtitle, abstract, secs, closing, refs


def render_paras(text):
    out = []
    for p in re.split(r'\n\n+', text):
        p = p.strip()
        if not p:
            continue
        # carousel markers: CAROUSEL-START <id> ... CARD :: title :: body ... CAROUSEL-END
        if p.startswith('CAROUSEL-START'):
            cid = p.split()[1] if len(p.split()) > 1 else 'c'
            out.append(f'      <div class="carousel" id="car-{cid}" tabindex="0">')
            continue
        if p.startswith('CAROUSEL-END'):
            out.append('      </div>')
            continue
        cm = re.match(r'^CARD\s*::\s*(.+?)\s*::\s*(.+)$', p, re.S)
        if cm:
            body = render_paragraph(cm.group(2)).strip()
            out.append('        <article class="card">')
            out.append(f'          <h3>{enc(cm.group(1))}</h3>')
            out.append(f'          {body}')
            out.append('        </article>')
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
        # block quote: every line starts with ">"
        if all(l.strip().startswith('>') for l in p.split('\n') if l.strip()):
            q = ' '.join(re.sub(r'^>\s?', '', l).strip() for l in p.split('\n') if l.strip())
            out.append(f'      <blockquote class="epigraph">{render_paragraph(q).strip()}</blockquote>')
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
    composed = subprocess.run([sys.executable, os.path.join(ROOT, 'compose-article.py')],
                              capture_output=True, text=True, check=True).stdout
    md = extract_footnotes(composed)
    title, subtitle, abstract, secs, closing, refs = parse_article(md)
    shell = open(os.path.join(ROOT, 'nown-whitepaper.html')).read()

    # Simulations FROZEN 2026-07-20 (Niko: leave them out until the protocol is nailed down).
    # Sources kept in build/sim-*.txt; to restore, uncomment the three reads below.
    sim_css = sim_markup = sim_js = ''
    # sim_css = open(os.path.join(SP, 'sim-css.txt')).read()
    # sim_markup = open(os.path.join(SP, 'sim-markup.html')).read()
    # sim_js = open(os.path.join(SP, 'sim-js.txt')).read()

    # --- head: take shell head, append sim CSS before </style> (last style close in head) ---
    head_end = shell.index('</head>')
    head = shell[:head_end]
    # retarget canonical/og URLs, title, social card and description to the article.
    # The shell is the whitepaper's, so every one of these has to be rewritten or the
    # article ships the whitepaper's identity: og:title read "Nown . whitepaper" on the
    # article page until 2026-07-26, so every share of it previewed as the wrong paper.
    head = head.replace('nown-whitepaper.html', 'nown-article.html')
    head = re.sub(r'<title>.*?</title>',
                  '<title>Nown &middot; Collaborative Research Paper</title>', head, flags=re.S)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                  r'\1Nown &middot; the collaborative research paper\2', head)
    ART_DESC = ('The collaborative research paper behind Nown: the reasoning, the economics, the open '
                'problems, and the constructions under the protocol. Public domain (the Unlicense).')
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + ART_DESC + m.group(2), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + ART_DESC + m.group(2), head)
    head = head[:head.rindex('</style>')] + '\n/* --- embedded simulations --- */\n' + sim_css + \
        '\n#simulations .math{ display:none }\n' + head[head.rindex('</style>'):]
    # math style
    head = head.replace('</style>', ".math{ font-family:var(--mono); text-align:center; font-size:1rem; "
                        "color:var(--ink); margin:1.1rem auto; letter-spacing:.02em }\n"
                        ".subsec{ font-family:var(--serif); font-weight:600; font-size:1.16rem; "
                        "color:var(--ink); margin:2.1rem 0 .3rem; letter-spacing:-.01em }\n"
                        ".wpfig{ margin:2rem 0; }\n"
                        ".carousel{ display:grid; grid-auto-flow:column; grid-auto-columns:min(330px,82%); gap:1rem;"
                        " overflow-x:auto; scroll-snap-type:x mandatory; padding:.4rem .2rem 1.1rem; margin:1.6rem 0;"
                        " scrollbar-width:thin; scrollbar-color:transparent transparent }\n"
                        ".carousel:hover,.carousel:focus-within{ scrollbar-color:color-mix(in srgb,var(--rule-2) 60%,transparent) transparent }\n"
                        ".carousel::-webkit-scrollbar{ height:10px; background:transparent }\n"
                        ".carousel::-webkit-scrollbar-thumb{ background-color:transparent; background-clip:padding-box;"
                        " border:3px solid transparent; border-radius:999px }\n"
                        ".carousel:hover::-webkit-scrollbar-thumb{ background-color:color-mix(in srgb,var(--rule-2) 60%,transparent) }\n"
                        ".card{ scroll-snap-align:start; border:1px solid var(--rule); border-radius:10px; background:var(--paper-2);"
                        " padding:1.15rem 1.25rem; display:flex; flex-direction:column; gap:.45rem }\n"
                        ".card h3{ font-family:var(--serif); font-size:1.06rem; font-weight:600; margin:0; color:var(--ink); letter-spacing:-.01em }\n"
                        ".card p{ font-size:.92rem; line-height:1.52; color:var(--ink-2); margin:0; text-wrap:pretty }\n"
                        ".wpfig .fig-frame svg{ display:block; width:100%; height:auto; max-width:560px; margin:0 auto }\n"
                        "details.explore{ margin:1.6rem 0 0; border-top:1px solid var(--rule) }\n"
                        "details.explore>summary{ cursor:pointer; list-style:none; display:flex; align-items:center; gap:.6rem;"
                        " padding:.9rem .1rem; font-family:var(--mono); font-size:.78rem; letter-spacing:.12em;"
                        " text-transform:uppercase; color:var(--bronze); -webkit-tap-highlight-color:transparent }\n"
                        "details.explore>summary::-webkit-details-marker{ display:none }\n"
                        "details.explore>summary::after{ content:''; width:.46rem; height:.46rem;"
                        " border-right:1.5px solid currentColor; border-bottom:1.5px solid currentColor;"
                        " transform:rotate(45deg) translateY(-15%); transition:transform .2s ease }\n"
                        "details.explore[open]>summary::after{ transform:rotate(225deg) translateY(-15%) }\n"
                        "details.explore>.explore-body{ padding:.1rem 0 .5rem }\n</style>", 1)

    # --- topbar / brand: reuse from shell (between </head> and <div class="wrap">) ---
    wrap_i = shell.index('<div class="wrap">')
    top = shell[head_end + len('</head>'):wrap_i]
    # brand nav: keep the Whitepaper link pointing to the whitepaper, mark Article as the current page
    top = top.replace('<a href="nown-whitepaper.html" class="bcur" aria-current="page">Whitepaper</a>',
                      '<a href="nown-whitepaper.html">Whitepaper</a>')
    top = top.replace('<a href="nown-article.html">Article</a>',
                      '<a href="nown-article.html" class="bcur" aria-current="page">Article</a>')
    # The article has its own typeset PDF, built from this same source by build-pdf.sh
    # with the same FIGURE markers, so the link points at the artifact rather than at
    # the browser's print dialog. Every other reader control comes through unchanged.
    pdf_btn = (
        '<a class="btn" id="pdfBtn" href="nown-article.pdf" target="_blank" rel="noopener" '
        'title="Open the typeset PDF">\n'
        '      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2'
        'h16a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2M6 14h12v7H6z"/></svg>\n'
        '      <span class="blab">PDF</span>\n'
        '    </a>')
    top = re.sub(r'<a class="btn" id="pdfBtn".*?</a>', lambda m: pdf_btn, top, count=1, flags=re.S)

    # --- TOC ---
    toc = ['      <li><a href="#abstract"><span class="n">&middot;</span> Abstract</a></li>',
           '      <li class="sepli"><span class="sep"></span></li>']
    for num, ttl, _, _ in secs:
        toc.append(f'      <li><a href="#s{num}"><span class="n">{num}</span> {enc(ttl)}</a></li>')
    toc.append('      <li class="sepli"><span class="sep"></span></li>')
    toc.append('      <li><a href="#notes"><span class="n">&middot;</span> Notes</a></li>')
    toc.append('      <li><a href="#refs"><span class="n">&middot;</span> References</a></li>')

    # --- title block ---
    titleblock = '''    <section class="title" id="top">
      <p class="eyebrow">Article &middot; v0.1</p>
      <h1 class="name">Nown</h1>
      <p class="thesis">Collaborative <b>research</b> paper.</p>
      <p style="margin-top:1.4rem"><a href="nown-whitepaper.html">New here? Start with the whitepaper &rsaquo;</a></p>
    </section>'''

    # --- abstract ---
    parts = [titleblock, '\n    <section class="abstract" id="abstract">', '      <p class="lbl">Abstract</p>']
    for p in abstract:
        parts += render_paras(p)
    parts.append('    </section>')

    # --- sections: whitepaper intro, then the research part inside a disclosure ---
    def emit_blocks(blocks):
        for kind, content in blocks:
            if kind == 'sub':
                parts.append(f'      <h3 class="subsec">{enc(content)}</h3>')
            else:
                parts.extend(render_paras(content))

    for num, ttl, intro, explore in secs:
        parts.append(f'\n    <section id="s{num}">')
        parts.append(f'      <h2 class="sec"><span class="num">&sect;{num}</span> {enc(ttl)}</h2>')
        emit_blocks(intro)
        if explore:
            parts.append('      <details class="explore">')
            parts.append('        <summary>Dive deeper</summary>')
            parts.append('        <div class="explore-body">')
            emit_blocks(explore)
            parts.append('        </div>')
            parts.append('      </details>')
        parts.append('    </section>')

    # --- references ---
    if closing:
        parts.append('\n    <section id="closing" class="closing">')
        for c in closing:
            cls = ' class="exit-links"' if c.startswith('[') else ''
            parts.append(render_paragraph(c).replace('<p>', f'<p{cls}>', 1))
        parts.append('    </section>')

    if _FN:
        parts.append('\n    <section id="notes" class="notes">')
        parts.append('      <details class="endnotes">')
        parts.append(f'        <summary>Notes <span class="cnt">{len(_FN)}</span></summary>')
        parts.append('        <ol class="enlist">')
        for fid, (n, text) in sorted(_FN.items(), key=lambda kv: kv[1][0]):
            parts.append(f'          <li id="en{n}">{enc(text)}</li>')
        parts.append('        </ol>')
        parts.append('      </details>')
        parts.append('    </section>')

    parts.append('\n    <section id="refs" class="refs">')
    parts.append('      <h2 class="sec"><span class="num">&sect;</span> References</h2>')
    parts.append('      <div class="reflist">')
    for i, r in enumerate(refs, 1):
        parts.append(f'        <div class="refrow" id="ref{i}"><a class="theme refback" href="#cite{i}" aria-label="back to the text">[{i}]</a><span class="src">{enc(r)}</span></div>')
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
    print(f'built nown-article.html: {len(secs)} mirrored sections, {len(refs)} refs, {len(out):,} bytes')


if __name__ == '__main__':
    build()
