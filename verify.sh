#!/usr/bin/env bash
# verify.sh — mechanical invariants for the Nown whitepaper + website loop.
# GREEN = every artifact that exists holds its invariants. Goal-completion is
# tracked separately in the NIGHTLOG; this checks consistency, not doneness.
set -u
cd "$(dirname "$0")"
fail=0
TMPIDX="$(mktemp -t nownidx)"
trap 'rm -f "$TMPIDX"' EXIT
err(){ echo "  FAIL: $1"; fail=$((fail+1)); }
ok(){ echo "  ok: $1"; }

WP="WHITEPAPER.md"
ART="ARTICLE.md"
FIGDIR="figures"
# the 2026-07-26 rulings: no staked standing, no middle state. These phrases are dead
# in both papers, in every case.
DEAD_0726='staked standing|standing at risk|\bunresolved\b'

echo "== whitepaper =="
if [ ! -f "$WP" ]; then err "$WP missing"; else
  grep -q "Nown" "$WP" || err "name 'Nown' missing"
  grep -qi "Unlicense" "$WP" || err "Unlicense line missing"
  grep -q "CC0" "$WP" && err "stale CC0 mention (license is the Unlicense)"
  n=$(grep -c "—" "$WP"); [ "$n" -eq 0 ] || err "$n line(s) with em-dash (must be 0)"
  n=$(grep -c "–" "$WP"); [ "$n" -eq 0 ] || err "$n line(s) with en-dash (must be 0)"
  n=$(grep -ciE "\b(bitcoin|satoshi|crypto|jury|juror|jurors)\b" "$WP"); [ "$n" -eq 0 ] || err "$n bitcoin/satoshi/crypto/jury/juror mention(s) (#23, must be 0)"
  n=$(grep -ciE "\b(honest|honestly|dishonest|virtuous|malicious)\b" "$WP"); [ "$n" -eq 0 ] || err "$n emotionally loaded word(s) (Niko 2026-07-23, must be 0)"
  n=$(grep -ciE "$DEAD_0726" "$WP"); [ "$n" -eq 0 ] || err "$n staked-standing/unresolved line(s) (Niko 2026-07-26, must be 0)"
  [ "$fail" -eq 0 ] && ok "whitepaper invariants hold"
fi

echo "== article =="
if [ ! -f "$ART" ]; then err "$ART missing"; else
  s0=$fail
  grep -q "Nown" "$ART" || err "name 'Nown' missing"
  n=$(grep -c "–" "$ART"); [ "$n" -eq 0 ] || err "$n line(s) with en-dash (must be 0)"
  n=$(grep -ciE "$DEAD_0726" "$ART"); [ "$n" -eq 0 ] || err "$n staked-standing/unresolved line(s) (Niko 2026-07-26, must be 0)"
  [ "$fail" -eq "$s0" ] && ok "article invariants hold"
fi

echo "== figures =="
# Two em-dashes once shipped inside the PDF through a figure, because the dash check
# ran over the prose alone. The figures are part of the paper, so they hold the rule too.
if [ ! -d "$FIGDIR" ]; then echo "  info: $FIGDIR not present"; else
  s0=$fail
  for f in "$FIGDIR"/*.tikz "$FIGDIR"/*.svg; do
    [ -e "$f" ] || continue
    n=$(grep -c "—" "$f"); [ "$n" -eq 0 ] || err "$f: $n line(s) with em-dash (must be 0)"
    n=$(grep -c "–" "$f"); [ "$n" -eq 0 ] || err "$f: $n line(s) with en-dash (must be 0)"
    n=$(grep -c "&#8212;" "$f"); [ "$n" -eq 0 ] || err "$f: $n line(s) with &#8212; em-dash entity (must be 0)"
    n=$(grep -c "&#8211;" "$f"); [ "$n" -eq 0 ] || err "$f: $n line(s) with &#8211; en-dash entity (must be 0)"
  done
  # in TikZ, --- is LaTeX's em-dash; a path uses -- , never three
  for f in "$FIGDIR"/*.tikz; do
    [ -e "$f" ] || continue
    n=$(grep -c -- "---" "$f"); [ "$n" -eq 0 ] || err "$f: $n line(s) with --- (LaTeX em-dash, must be 0)"
  done
  # forward: every FIGURE marker in the papers has both twins
  if [ ! -f "inject-figures.py" ]; then err "inject-figures.py missing (figures gate cannot run)"
  elif [ ! -f "$WP" ] || [ ! -f "$ART" ]; then err "a paper is missing (figures gate cannot run)"
  else
    python3 inject-figures.py check "$WP" "$ART" || err "inject-figures check failed (a FIGURE marker has no twin)"
  fi
  # reverse: every .svg is claimed by a marker and carries its .tikz twin
  for svg in "$FIGDIR"/*.svg; do
    [ -e "$svg" ] || continue
    id=$(basename "$svg" .svg)
    if [ -f "$WP" ] && [ -f "$ART" ]; then
      grep -qE "^FIGURE[[:space:]]+$id[[:space:]]*::" "$WP" "$ART" || err "orphan figure: $id.svg has no FIGURE marker in $WP or $ART"
    fi
    [ -f "$FIGDIR/$id.tikz" ] || err "orphan figure: $id.svg has no $FIGDIR/$id.tikz twin"
  done
  [ "$fail" -eq "$s0" ] && ok "figure invariants hold"
fi

echo "== website =="
SITE="nown-site.html"
if [ ! -f "$SITE" ]; then echo "  info: $SITE not built yet"; else
  s0=$fail
  grep -qiE '<script[^>]+src="https?:' "$SITE" && err "external <script src> (not self-contained)"
  # rel=canonical / og:url are metadata, never fetched; only fetched <link> assets break self-containment
  grep -viE '<link[^>]+rel="canonical"' "$SITE" | grep -qiE '<link[^>]+href="https?:' && err "external <link href> stylesheet/font (not self-contained)"
  grep -qiE '@import[^;]*url\(\s*["'"'"']?https?:' "$SITE" && err "external @import"
  grep -qiE '(src|href)="//' "$SITE" && err "protocol-relative external resource"
  grep -qiE '<img[^>]+src="https?:' "$SITE" && err "external <img> (embed as data URI)"
  # lander simplified 2026-07-22 to hero + invitation only; pillars/contribute moved off the front door
  for kw in Nown reputation trust; do grep -q "$kw" "$SITE" || err "missing content: $kw"; done
  grep -qi "whitepaper" "$SITE" || err "missing whitepaper reference"
  grep -qiE "github" "$SITE" || err "missing GitHub link"
  grep -qi "what-is-nown" "$SITE" || err "missing What-is-Nown invitation"
  grep -qi 'name="viewport"' "$SITE" || err "missing viewport meta (mobile)"
  grep -qi 'prefers-color-scheme' "$SITE" || err "missing dark-mode support"
  [ "$fail" -eq "$s0" ] && ok "site invariants hold"
fi

echo "== prints =="
# Three surfaces, three typeset PDFs, one build (build-pdf.sh all). A print that
# is older than the text it prints is a drifted copy, so it fails here.
WIN="what-is-nown.html"
stale(){
  p="$1"; shift
  if [ ! -f "$p" ]; then err "$p missing (run ./build-pdf.sh all)"; return; fi
  for s in "$@"; do
    [ -e "$s" ] || continue
    if [ "$s" -nt "$p" ]; then err "$p is older than $s (run ./build-pdf.sh all)"; fi
  done
}
s0=$fail
TIKZ=""
[ -d "$FIGDIR" ] && TIKZ=$(printf '%s ' "$FIGDIR"/*.tikz)
for dir in "." "public"; do
  [ -d "$dir" ] || continue
  # shellcheck disable=SC2086
  stale "$dir/nown-whitepaper.pdf" "$WP" nown.latex build-pdf.sh inject-figures.py $TIKZ
  # shellcheck disable=SC2086
  stale "$dir/nown-article.pdf" "$ART" "$WP" nown.latex build-pdf.sh compose-article.py inject-figures.py $TIKZ
  stale "$dir/nown-what-is.pdf" "$WIN" nown.latex build-pdf.sh win-to-md.py
done
# The one-pager is hand-authored HTML and win-to-md.py is the only reader of it.
# If a concept card is added and the extractor cannot see it, the print silently
# loses a concept, so the two counts are held equal here.
if [ ! -f "$WIN" ]; then err "$WIN missing"
elif [ ! -f "win-to-md.py" ]; then err "win-to-md.py missing (the one-pager print has no source)"
else
  cards=$(grep -c '<div class="c">' "$WIN")
  got=$(python3 win-to-md.py count "$WIN" 2>/dev/null || echo x)
  heads=$(python3 win-to-md.py "$WIN" - 2>/dev/null | grep -c '^## [0-9]' || echo x)
  [ "$got" = "$cards" ] || err "win-to-md reads $got concept(s), $WIN carries $cards"
  [ "$heads" = "$cards" ] || err "win-to-md emits $heads section(s), $WIN carries $cards concept(s)"
  grep -q 'nown-what-is.pdf' "$WIN" || err "$WIN has no PDF control (nown-what-is.pdf)"
fi
[ "$fail" -eq "$s0" ] && ok "three prints, built from their sources"

echo "== public build =="
s0=$fail
for f in what-is-nown.html nown-whitepaper.html nown-article.html; do
  if [ ! -f "public/$f" ]; then err "public/$f missing"
  elif ! cmp -s "$f" "public/$f"; then err "public/$f differs from $f (re-copy after editing)"; fi
done
if [ -f nown-site.html ]; then
  ./strip-hold.py nown-site.html "$TMPIDX" >/dev/null 2>&1 || err "strip-hold.py failed"
  cmp -s "$TMPIDX" public/index.html || err "public/index.html differs from strip-hold.py nown-site.html"
  rm -f "$TMPIDX"
fi
[ "$fail" -eq "$s0" ] && ok "public build matches its sources"

echo "== anonymous-publishing runbook =="
RB="ANONYMOUS-PUBLISHING.md"
if [ ! -f "$RB" ]; then echo "  info: $RB not written yet"; else
  s0=$fail
  grep -qiE "onion|tor" "$RB" || err "missing Tor/onion path"
  grep -qiE "monero|xmr" "$RB" || err "missing anonymous-payment path"
  grep -qiE "stylometr" "$RB" || err "missing stylometry note"
  [ "$fail" -eq "$s0" ] && ok "runbook invariants hold"
fi

echo
if [ "$fail" -eq 0 ]; then echo "VERIFY: GREEN"; exit 0; else echo "VERIFY: RED"; exit 1; fi
