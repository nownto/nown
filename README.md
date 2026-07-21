# Nown: portable trust for sovereign individuals

**Live at https://nown.to · repo https://github.com/nownto/nown · public domain (the Unlicense)**

A peer-to-peer protocol for trust between strangers with no trusted third party. You act under a key,
and the record of how it has dealt is public and permanent. Your standing (**karma**) is a density of
good dealing over time, earned by dealing well and carried wherever Nown is read, held under a key that
is yours to keep or to sell. No platform grants it and none can take it away. Settling a dispute is one
use of it, decided by a **quorum** of high-karma strangers drawn at random, anonymous to the traders and
to each other, ruling over an escrow held only by the two traders, never a custodian. No company, no owner.

The one-paragraph version is the abstract of [WHITEPAPER.md](WHITEPAPER.md) (v0.1, the source of record;
the typeset PDF and the interactive page are generated from it).

## What ships (v0.1)

The **whitepaper**, the **article** (its full companion construction), and the **lander** ship together
as v0.1. The interactive **simulations** and the built **figures** are frozen pending protocol
finalization; their sources stay in the repo. The public lander is derived from the dev master via
`strip-hold.py`.

## This directory

| File | What it is | Public? |
|---|---|---|
| **[WHITEPAPER.md](WHITEPAPER.md)** | The short paper, v0.1, MVP-complete. Source of record. Start here. | yes |
| `nown-whitepaper.html` / `.pdf` | The whitepaper, rendered | yes |
| **[ARTICLE.md](ARTICLE.md)** / `nown-article.html` | The full companion construction (the deep model) | yes |
| `nown-site.html` | The lander (dev master; `strip-hold.py` → public build) | yes (derived) |
| `figures/` + `inject-figures.py` | Figures as SVG+TikZ from one manifest | frozen |
| `build-pdf.sh` + `nown.latex` | Typeset-PDF pipeline | yes |
| `render-whitepaper-html.py` / `build-article.py` | md to HTML renderers (single source) | tooling |
| **[MASTER-DESIGN.md](MASTER-DESIGN.md)** | Operational map. Read after ARCHITECTURE.md every session. | no |
| `wiki/` | Vault concept notes (one node per mechanism) | no |
| `legacy/` | Superseded artifacts, kept for the record (zero-loss) | no |
| `verify.sh` | Invariant checks (register, banned terms, structure) | tooling |

## Honest status

A **design and research draft, not running code.** The whitepaper names its own open problems (§10): the
record must be made tamper-proof without spending real energy to secure it; a closed ring of real people
is hard to tell from a busy open trader by the shape of the graph alone; the constants of the flow are
still to be set; and telling one person from a thousand cheap keys has no full answer anywhere. Each is
written down as work to do, each links a pull request.

## Working model

Claude opens PRs on `nownto/nown`; Niko reviews and merges; merge to `main` auto-deploys nown.to
(Git-connected Cloudflare Worker). Local edits land here first; this directory and the repo stay in sync.
Only Niko merges, and a merge is a deploy.
