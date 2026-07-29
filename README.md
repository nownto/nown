# Nown: portable trust for sovereign individuals

**Live at https://nown.to · repo https://github.com/nownto/nown · public domain (the Unlicense)**

A peer-to-peer protocol for trust between strangers with no trusted third party. You act under a key, and
every dealing that key closes writes one mark to a public, permanent record: up where the dealing was
ruled correct, down where it was not. Your **karma** is the sum of those marks. **The record holds karma
marks and seals, and nothing else**, so a reader learns what a key has done without learning anything
about the doing. It is carried wherever Nown is read, held under a key that is yours to keep or to sell.
No platform grants it and none can take it away. Settling a dispute is one use of it, decided by a
**quorum** of high-karma strangers
called at random, anonymous to the traders and to each other, ruling over an escrow held only by the two
traders, never a custodian. No company, no owner.

The one-paragraph version is the abstract of [WHITEPAPER.md](WHITEPAPER.md) (v0.1, the source of record;
the typeset PDF and the interactive page are generated from it).

## What ships (v0.1)

The **whitepaper**, the **Collaborative research paper**, and the **lander** ship together as v0.1, with
every figure the two papers carry, in the page and in the print. The interactive **simulations** are the
one thing held back, until they are rebuilt to the protocol as it now stands. The public lander is
derived from the dev master via `strip-hold.py`.

## This directory

| File | What it is |
|---|---|
| **[WHITEPAPER.md](WHITEPAPER.md)** | The short paper, v0.1, MVP-complete. Source of record. Start here. |
| `nown-whitepaper.html` / `.pdf` | The whitepaper, rendered |
| **[ARTICLE.md](ARTICLE.md)** / `nown-article.html` / `.pdf` | The Collaborative research paper: the reasoning, the economics, the objections, and the open problems |
| `public/` | What the site serves: the lander, `what-is-nown.html` (+ its PDF), both papers, the assets |
| `figures/` + `inject-figures.py` | One figure per id, `.svg` for the page and `.tikz` for the print. A `FIGURE <id> :: <caption>` marker in the prose is the only place a figure is declared, and a marker missing either twin fails the build. |
| `compose-article.py` + `build-article.py` | Compose the article from its sections and render it |
| `render-whitepaper-html.py` | The whitepaper, md to HTML |
| `build-pdf.sh` + `nown.latex` | Typeset-PDF pipeline (pandoc + xelatex). `./build-pdf.sh all` builds all three prints |
| `win-to-md.py` | Reads `what-is-nown.html` and emits the markdown for `nown-what-is.pdf`, so the one-pager stays the only source of its own text |
| `strip-hold.py` | Derives the public lander from the dev master |
| **[OPEN-PROBLEMS.md](OPEN-PROBLEMS.md)** | The fourteen genuinely unsolved parts, one section each. Every "Work on this problem" card in the article links to its section here. |
| `verify.sh` | Invariant checks (register, banned terms, structure) |

## Honest status

A **design and research draft, not running code.** The whitepaper carries solutions only. Everything
unfinished is named in the Collaborative research paper, in the section it belongs to, and each card
links to its own section of [OPEN-PROBLEMS.md](OPEN-PROBLEMS.md). Fourteen problems, fourteen sections.
Some of them:

- **The genesis.** A key at zero confers nothing and can only receive, which is the sybil bound. It is
  also the launch problem: at the network's first block every key is at zero, so nothing can move.
- **Enough voluntary voters.** Everything the quorum promises rests on the panel filling, and seats are
  voluntary. A matcher is paid from the fee and from the bonds the missing seats forfeited, which prices
  the seat in the right direction and does not by itself guarantee anyone answers.
- **Keeping the record.** The record must stay whole and served with no company behind it and no coin to
  pay its keepers, and the censorship bound the receipt mechanism delivers is unproven.
- **Pulse time.** Karma is measured against block time, which belongs to a network Nown does not govern.
  Pulse time, the protocol's own clock kept from its own activity, is the candidate and is unbuilt.
- **The native beacon.** The protocol draws its randomness from its own activity and starts on a borrowed
  source. How much activity is enough to switch is open, and it is a separate question from the clock's.
- **Storing the evidence.** The case file reaches the panel encrypted and has to live somewhere between
  the call and the verdict, with no company to host it.

## Working model

Contributions arrive as pull requests on `nownto/nown`. The maintainer reviews and merges, and a merge
to `main` deploys nown.to. Nothing ships any other way.
