# Nown

A peer-to-peer protocol for portable trust and merit-based arbitration.
A reputation you carry, and a verdict no one can capture. No owner, no token, no company.

- **Site:** https://nown.to
- **Whitepaper:** [read online](https://nown.to/nown-whitepaper.html) · source [`WHITEPAPER.md`](WHITEPAPER.md) · [typeset PDF](nown-whitepaper.pdf)

## Status

A design and research draft, not running code. It cannot be proven in advance; its worth is a
question for the market, answered by adoption.

## The three commitments

- **Karma** — a reputation you own. Earned through costly action, carried between strangers, held by
  no platform.
- **Quorum** — a verdict no one can buy. Disputes are judged by an anonymous quorum of stewards
  selected at random; their verdict is final, because no authority sits above them to capture.
- **Sovereignty** — you answer for yourself. The protocol rules on the trade, not on the person.

## The site

Static and self-contained, no build step to serve. `index.html` is the landing page,
`nown-whitepaper.html` is the interactive whitepaper, and `nown-whitepaper.pdf` is the typeset print
edition. The PDF is generated from `WHITEPAPER.md` by `./build-pdf.sh` (pandoc + LaTeX, template in
`nown.latex`, styled after the Bitcoin whitepaper).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Every pull request is reviewed against the ethos and the
whitepaper, and a human approves every merge. There is no token, no bounty, and no equity. You
contribute because it should exist.

## License

Released into the public domain. Everything in the repository, the whitepaper included, is under
the **Unlicense** ([`LICENSE`](LICENSE)). Nothing here is owned, so there is nothing to
capture. See [`NOTICE`](NOTICE).
