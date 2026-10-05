# Nown — open problems

Everything here is genuinely unsolved. Nothing in the whitepaper is. The paper carries what is built;
this file carries what is not, so a stranger can pick one up without reading either paper end to end.

Each problem below is linked from the [collaborative research paper](nown-article.html), which states it
in context and explains why the obvious answers do not work. Start there, then come back here.

Released into the public domain (the Unlicense), like everything else.

Problems retired by the 2026-07-29 model corrections are kept in
`legacy/OPEN-PROBLEMS-retired-2026-07-30.md`, with the ruling that retired each one.

---

## Reading the tally

Karma is a sum of marks in two directions with no limit either way. The protocol names a ruling correct or
incorrect, which compares a result to terms the two parties fixed themselves, and it names a mark up or
down, which is a direction on a line. Neither word carries a judgment of the man, and that is deliberate:
the protocol cannot measure worth, so it declines to name quality and names direction instead.

**Open:** whether applications converge on a shared vocabulary for reading a tally; what an interface
should show a person who has never seen one, given that the sum alone hides the shape of the history
behind it; and whether a reader needs anything beyond the sum and the count of marks in each direction to
judge a key well.

## Two keys looping

Two keys that both carry karma can deal with each other as often as they like, each dealing writing a mark
up on each, at no cost to either. The record holds no pair, so the protocol has no rule against it, and an
application that wants to discount it has nothing to read.

The candidate is a pair tag. Two keys can each compute the same secret from their own private half and the
other's public half, and nobody else can. Each mark carries a tag derived from that secret, a different
one for each side of the dealing so the two marks never match, and the proof that makes the mark valid
shows the tag came from the real counterparty. Every mark from one counterparty then carries one tag, and
an application can count each tag once or discount a history drawn mostly from one source, without
learning who the counterparty was.

**Open:** whether the repeat count the tag reveals costs more privacy than it buys; the exact derivation
and the proof it adds to a mark; and rings of many keys, which spread their marks across as many tags and
read as varied as a real history.

## The genesis

A key at zero confers nothing, so at the network's first block, when every key is at zero, nothing can
move. The problem is how to launch.

The candidate is a genesis beacon, declared openly in the record's first entries: a node that grants each
new key one small injection and shuts itself down for good once block time and network action pass a
stated saturation.

**Open:** the injection's size and schedule; the saturation test; how a per-key injection is rationed when
a person may open unlimited keys; and the math that leaves the earliest keys no advantage over those who
come after.

## Enough voluntary voters

Everything the quorum promises rests on the panel filling. Seats are voluntary, and nothing in the
protocol makes enough competent readers answer a call. Pricing the bond and the bounty against the cost of
a careful evening is the obvious lever, and it is not obviously sufficient: the same fee has to clear for a
case nobody finds interesting as for one everybody does, and a steward who declines loses nothing. Because
the fee is posted by the party who opens a dealing, a small dispute may call and find no one willing, and
the dealing then closes on its timeout as correct for both.

A matcher is paid twice over, from the fee and from the bonds the missing seats forfeited, so the return
on a seat rises with the share of careless seats. That prices the seat in the right direction and it does
not by itself guarantee anyone answers.

**Open:** what guarantees a sufficient supply of willing readers, without paying anyone to sit who will
not read, without a standing body of appointed stewards, and without letting a case be starved by
indifference; the fee level; the bond priced against the cost of careful reading; the deposit margin above
the fee; and whether the parties of a lapsed call may mark each other, each taking a mark down of his own.

## The panel size function

The capture floor is settled arithmetic: an attacker holding share p of the keys that answer carries a
majority of n seats with probability at most exp(-2n(1/2 - p)^2), so n is at least ln(1/q) over
2(1/2 - p)^2 for a tolerated capture probability q.

**Open:** how the minimum grows with the weight of what is being arbitrated; what the ceiling is; and how
a specialist call scales up as its eligibility narrows the crowd a panel hides in.

## The bar and the answer rate

The eligibility bar is a percentile of the live karma distribution rather than a number, so it moves with
the network and each key tests it privately against its own record. Seats are voluntary, which makes the
answer rate the real security parameter: a key that always answers is over-represented among those who do.

**Open:** the percentile; how it behaves in a young network where the distribution is thin; and the bond
and bounty levels that keep enough competent readers answering.

## Storing the evidence

The evidence reaches the panel as an encrypted package that opens only for a key that was called in the
round and took a seat. The package has to live somewhere between the call and the verdict, and no company
exists to host it.

**Open:** where a case file rests and who serves it, at whose cost; how long it survives and who decides;
how a steward fetches one without the fetch itself identifying him; and what a party can rely on if the
file becomes unavailable mid-case.

## Murky evidence

The quorum converges because the evidence is the most obvious thing for strangers who cannot coordinate to
coordinate on. That holds where a file is clear and weakens as it gets murkier.

**Open:** how to price panel size against the readability of a case without asking anyone to judge
readability, and what the design should concede about cases that are genuinely close.

## Funding a bond unlinkably

A steward is never identifiable, in any context, yet his bond has to be funded from somewhere, and a
funding source links a key to a case.

**Open:** breaking that link without a custodian and without weakening the bond's precommitted paths.

## What a seal carries

A seal is a short free-text field on a key, consented by both parties and permanent. The protocol fixes
those three things and leaves the contents to the applications that read them.

**Open:** whether a minimum shape is worth fixing after all; what the cap on length should be; how a
document is committed to without the document touching the record; and how far a free-text field can carry
a credential system before conventions have to be written down.

## Sealing a company

A firm's key is its reputation and its ownership is a quorum-ratified seal, so transfer is re-sealing and a
cap table is a set of fractional seals.

**Open:** the firm-to-key binding; fractional sealing and re-sealing on a sale; how an ownership dispute is
called and ruled; and what a buyer can rely on, given that a sale hands over control and leaves the seller
holding it too.

## Reading the seals

A seal weighs what its issuer weighs, and no cap exists on granting or holding, because the supply of
seals is bounded by the reputation of the people issuing them.

**Open:** how an application weighs many seals from few issuers; how label conventions converge and split;
and whether accumulation needs any price beyond the weight a reader assigns.

## Pulse time

Karma is measured against block time, which belongs to a network Nown does not govern. The problem is a
native way for the protocol to keep time from its own activity. Pulse time is the candidate: the record's
own committed fingerprints as the tick, a verifiable delay function putting a floor of real sequential
time under each one, and the tick weighted by the karma of the keys dealing in it.

**Open:** the exact pulse function, and how it prices a pair of high-karma keys dealing with each other for
free; the saturation threshold and span before the switch; the delay function's calibration and its
hardware-advantage bound; and the interaction with the nodes that commit the fingerprints.

## The native beacon

The protocol draws the randomness it needs, to call a panel and to drop a seat where an even count leaves
no majority, from its own activity, so an attacker who wants to move the beacon has to move the record. A
young network carries too little activity to pay for that, so Nown starts on an established outside source
and switches to its own once its activity carries enough entropy.

A clock and a beacon are different objects with opposite requirements, so this switchover is a separate
decision from pulse time's, on a separate threshold.

**Open:** the extraction function and what it commits to; the cost of grinding it as a function of network
activity; the threshold and span that trigger the switch; whether the borrowed source stays as a
checkpoint the way the clock's does; and how the beacon behaves in the thin period right after launch.

## Keeping the record

The record has to stay whole and served with no company behind it and no coin to pay its keepers. The
candidate makes node service a dealing paid in karma, with proof-of-holding as its oracle and receipts
making every acceptance checkable.

**Open:** the incentive itself; the proof and its frequency; the shard a client carries; who pays to commit
a fingerprint and how often; the censorship bound the receipt mechanism actually delivers; and whether
karma alone can pay for a storage network at all.
