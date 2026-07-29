# Contributing to Nown

Nown is a peer-to-peer protocol for portable trust between strangers. A person acts under a key, and
every dealing that key closes writes one mark to a public, permanent record. Read the
[whitepaper](WHITEPAPER.md) before contributing; it is short, and it is the design. The
[collaborative research paper](ARTICLE.md) carries the reasoning, and
[OPEN-PROBLEMS.md](OPEN-PROBLEMS.md) carries what is genuinely unsolved. If you want work, start there.

The project is maintained anonymously and stays that way. You are welcome under a pseudonym.

## The ethos is a hard filter

Nown is ownerless by design: no owner, no company, no token, no fee, no admin key, no captured
dependency. A contribution that adds any of those is declined, however good it is otherwise. Any party
that could profit from the protocol could sell it, so there is none.

## How a pull request is reviewed

Every PR is triaged against a fixed rubric, and a human approves every merge:

- **Ethos** — does it keep the project ownerless (no token, company, owner, fee, admin key)?
- **Fidelity** — does it match the whitepaper's design, or is it a real, argued improvement?
- **Correctness** — does it do what it claims without breaking an invariant? `./verify.sh` is the
  mechanical gate, and it has to come back GREEN.
- **Voice** — documents stay in a plain, neutral register; no marketing, no hype.
- **Security and privacy** — nothing that adds tracking, external calls, or a deanonymizing asset.

One rule catches most of what gets declined: **the record holds karma marks and seals, and nothing
else.** Before proposing a rule, check whether the protocol can see the thing the rule depends on.

## Licensing of contributions

By contributing you agree your contribution is released the same way the project is: into the **public
domain under the Unlicense**, documents and code alike, with no rights retained. There is no contributor
licence agreement to sign and nothing to own.

## What there is not

No token, no bounty, no equity, no payment. You contribute because it should exist.
