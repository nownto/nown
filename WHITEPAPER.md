# Nown: A Protocol for Portable Trust

**v0.1.** Released into the public domain (the Unlicense).

## Abstract

A record of conduct that every reader computes for himself lets two strangers deal on what each has actually done. A person acts under a keypair, and every dealing that key closes writes one mark to a single public record: up where the dealing was ruled correct, down where it was not. The record holds those marks and the seals keys carry, and nothing else. What a dealing was about, what it was worth, and who the other party was are never written, so a reader learns what a key has done without learning anything about the doing. Each reader sums the marks himself under shared rules, so two readers reach the same figure and a man carries one standing into every market he enters. A key at zero confers nothing and can only receive, which is what keeps a thousand fresh keys from writing each other into standing. What decides a ruling is an oracle the parties fix before they deal: their own attestation, or a panel of bonded strangers whose majority is final. The protocol takes custody of nothing.

## 1. Trust between strangers

Dealing with a stranger requires a history neither party holds. Every arrangement that has supplied one has put a keeper in the middle: a guild, a court, a bank, a platform. The keeper owns the record he keeps, and the standing built under him does not leave his doors.

Nown gives a stranger a history that travels with him. Every dealing a key closes leaves one mark on a record every reader can read and sum, so what a man's word is worth is a thing anyone can work out for himself, in any market, from the same source.

## 2. Pretty Good Trust

Evidence can be faked, a man can be mistaken or lying, and worth is subjective, so no protocol can measure what a dealing was worth to either side. Nown supplies pretty good trust:[^pgt] enough to act on, computed by each reader, owned by no one.

The protocol records how a dealing was ruled and makes it permanent, so a ruling against a key costs it and a ruling for it pays. It reads the ruling alone, never who stands behind a key or how he played, and it admits anyone.

## 3. Keys

A person acts under a keypair. The public half is the account others know and the anchor of everything the key carries. It is not a name and it proves nothing about who its holder is.

The private half proves control without being revealed. Whoever holds it is the key's owner, as far as the protocol can tell. A key is therefore lost when its private half is lost and gone when its private half is taken, and no party exists to restore it. The protection is the ordinary one: a key generated offline and kept there.

A key is property. Its holder keeps it, lends it, or sells it, and whoever holds the private half holds everything the key carries. A sale hands the buyer control and cannot remove control from the seller.

A person may hold any number of keys. Each begins at zero and climbs on its own.

## 4. The record

One public record that only grows, held by independent nodes, ordered by block time. Each entry is written once and is never unwritten, edited, or hidden, and anyone may check one copy against another.

**The record holds karma marks and seals. It holds nothing else.** A dealing is never written to it. Its terms are not written, nor the outcomes it fixed, nor its oracle, nor its deadlines, nor its fee, nor the evidence, nor the ballots, nor which two keys took part. When a dealing closes, one mark lands on each key, and that is the whole of what the network learns.

Privacy here is a property of the design rather than a promise made about it. A reader sees that a key carries forty marks up and one down. He cannot see what any of them was for, who was on the other side, or why the one went down. Whether patterns and timing can be read to guess at more is a question for whoever writes the applications; the protocol neither offers that reading nor prevents it.

## 5. Karma

Karma[^karma] is a key's score: the sum of its marks. A dealing ruled correct writes a mark up, one ruled incorrect writes a mark down, and karma is what they add to. Only a recorded mark moves it, and time alone never does.

Karma is not fractionable. A mark is a mark, and no counterparty, no sum at stake, and no judgment of what a dealing was worth makes one mark count for more than another. There is no limit in either direction: a key whose downward marks outnumber its upward ones carries a score below zero, and a key that has dealt well for years carries a large one.

Karma is minted, never moved. A mark is written to a key; nothing is taken from anyone to write it, and karma is never staked, escrowed, or lent.

**A key at zero confers nothing.** It can receive a mark from a counterparty who already carries karma, and it can give none. Two keys at zero dealing only with each other therefore write nothing to either, however often they deal, and a thousand of them write a thousand nothings.[cite:1] A newcomer climbs by dealing with someone who already carries karma.[cite:2]

A mark is valid on a proof that a counterparty co-signed the dealing: a different key from the one being marked, and one whose karma is not zero. The proof shows those two facts and nothing more. Who the counterparty was, the record never learns.

No balance sits anywhere. There is only the record and the rules for reading it, so two readers running the same rules reach the same figure.

## 6. Dealings

A dealing is any exchange a key puts something behind: a trade, a job, a contract, a document to certify, a course taught. It is the only kind of entry there is, and everything else the protocol does is one.

Both keys agree everything before it opens: the outcomes it can have, the oracle[^oracle] that will choose between them, and whether a quorum[^quorum] may be called and when. A dealing that carries money is the same object with deposits attached, and money is never required.

The rulings are polar, and between two keys there are exactly three: a mark up for both, or up for one and down for the other, either way round. There is no ruling where both fall.

A dealing stays open until it closes, by attestation, by timeout, or by a quorum ruling, and its marks are written once, at the close. A deadline that passes with neither attestation nor verdict closes the dealing as correct for both, which is where a dealing that simply went well arrives. Who decides is a separate question from how it ends.

FIGURE karma-flow-plain :: A dealing without money. Fixed at setup: the outcomes, the oracle, and whether a quorum is called at once to ratify or only on a dispute.

## 7. Oracles

The parties name the oracle before they deal, and its answer is the ruling the record carries. The protocol claims nothing beyond it.

Two oracles are available. The first is the parties themselves, who both sign that the dealing closed as agreed. The second is a quorum, called when they disagree, or called from the start where the dealing is a certification and ratification is the point.

The record admits no outside authority as an oracle. A panel asked to attest a fact that fixed nothing to rule on is a witness: it reports what it read, and no ruling turns on it.

## 8. Quorum

A quorum is a panel of strangers of high karma, called at random for one case, each free to answer the call or decline it. A steward[^steward] is never identifiable: not to the parties, not to the other stewards, not afterward, in any context.

The quorum is a cooperative. Its stewards together are the oracle, and that one side makes a dealing with each steward separately.

> A quorum dealing takes the whole panel as one side and one steward as the other, and the panel is the oracle. Every steward deals with a part of himself, one share in the total size of the quorum. If he is right, his bond and his bounty are wired to him as the dealing closes. If he is wrong, he forfeits the bond and his seat closes with it.

Signing is seating. A steward signs every outcome his own dealing can have at the moment he accepts, and the stewards sign the oracle side together. The slot stays open only until the quorum is full, and whoever has not signed by then is left out of it. Nothing is signed once the case is decided.

Each steward receives the evidence as an encrypted package that opens only for a key that was called in the round and signed the quorum dealing. He reads it, privately picks one of the outcomes the parties fixed, writes his choice as a commitment, and opens it after the deadline. A commitment says nothing about the choice inside it, so no count exists to read while the votes are being cast.

The verdict is the outcome most of the opened choices carry, and it is final. A silent seat is not a choice for anything. The panel is odd, so a majority always exists; where silence leaves an even count, one seat is dropped by the protocol's own randomness, and that steward's bond returns to him.

FIGURE quorum-flow :: A quorum arbitration, opening to settlement, counted in blocks.

A steward who matches the verdict takes his bond back, a bounty out of the fee, and a share of the bonds forfeited by the seats that missed. One who misses it, or stays silent, forfeits his bond to the seats that matched. That is what pays a steward: the men who read the case are paid by the fee and by the men who did not.

Both the verdict and the number of seats that matched are public once the choices open, so every path a seat can take is known before any of them is taken. A steward signs one paying path per possible count of matching seats when he accepts, and the case selects the one that count names. Nobody signs anything afterward: a steward who missed releases nothing, and one who matched waits on no one.

The bond and the bounty are an escrow on a settlement rail, stewards on one side and the oracle aggregate on the other. Neither the protocol nor the quorum holds the money.

FIGURE quorum-draw :: Stewards vote in secret under bond. Most of the opened choices carry the verdict. Each steward then closes his own dealing with the panel: the seats that matched take their bonds, the bounty, and the bonds the seats that missed forfeited.

Where a dealing carries money, the reference construction is a two-of-two escrow[cite:3] between the two traders that commits, at funding, to every way it can end. The verdict reaches the parties, and signing the ruled path is the last act of the dealing. The marks land on the verdict rather than on the money, so a party who stalls has already taken his, and the escrow's timeout path keeps the funds from hanging on his silence. Nown owns no escrow: the protocol supplies the verdict, and any escrow service may implement Nown as its resolver.

FIGURE karma-flow-money :: A dealing that carries money: deposits locked in a two-of-two escrow with every outcome pre-signed, ruled by attestation or a quorum, settled along the ruled path.

Capture is priced rather than prevented. The panel cannot be found, so all an attacker can do is hold keys among those that answer a call. A panel is a sample of them: an attacker holding a share p carries a majority of n seats with probability no greater than exp(-2n(1/2 - p)^2). Fix the capture probability a case will tolerate, call it q, and the panel it needs follows: n at least ln(1/q) divided by 2(1/2 - p)^2. Panel size is the dial.

FIGURE quorum-scaling :: The panel grows with the network, and the cost of holding a majority of the keys that answer grows faster.

## 9. Seals

A seal is a short free-text field carried on a key: a credential, a membership, a certification, an authorship, a season ticket, the ownership of a firm. A key's marks are what it did. Its seals are what others have certified about it.

A seal is a dealing, so both keys agree every consequence before it opens, and a seal lands only with its subject's countersignature. Where no single signer can carry the fact alone, a quorum ratifies it.

A seal mints karma from nothing. It writes marks the way any dealing does, and it moves nothing from one key to another. Nothing caps how many a key may issue or hold, and nothing needs to: a school that certifies thousands is read through the graduates it certified, and a seal from a key with no karma carries what that key carries.

FIGURE seals :: A seal is one signed entry a key issues, or a quorum ratifies, and the subject countersigns.

What the protocol fixes is that the field is short, that both parties consented, and that it is permanent. What a seal should say, and which forms become standard, is settled by the applications that read them.

## 10. Block time

Karma is measured against block time.[^blocktime] The clock the protocol requires has two properties: every reader reads it the same way, and no participant can stop it, hurry it, or wind it back.

Every key's first appearance is stamped to a block, and every deadline in the protocol is counted in blocks. Finer time is presentation: a client may show a human date beside a block height, and nothing in the protocol reads it.

## 11. Randomness

The protocol needs randomness no participant can predict or steer: to call a panel, and to drop a seat where an even count leaves no majority. It takes that randomness from its own activity, so the entropy the network produces by dealing is the entropy it draws on.

A clock and a source of randomness are different things and the protocol keeps them apart. Block time says when. This says which.

Both are borrowed at the start and native later. A network with little activity carries little entropy, so Nown begins on an established outside source and moves to its own once its activity carries enough to make forgery impractical.

## 12. Nodes

The clock orders the record but does not hold it, so the record lives on a network of nodes, each keeping a copy.

At intervals the network commits a fingerprint of the whole record to the clock, and any copy checks against it, so a machine that quietly altered its past fails a check anyone can run. Where two fingerprints are offered for the same interval, the record is the first one whose contents are published and check out against it, and where both landed together it is the lower of the two. A node joining the network follows that chain of fingerprints from the beginning, and passes over any fingerprint it cannot expand.

## 13. The application layer

Everything a person touches is an application. The record holds marks and seals; every reading of them, and every service built on them, sits above it.

The call is the first of those services. A dealing that reaches its dispute condition needs eligible keys to hear of it, and the protocol cannot reach a key without an address, which is the one thing a steward may never publish. So the protocol fixes who may answer, each key tests that for itself in private, and the client carries the invitation. A reference client does this and everything else the protocol allows: it holds keys, opens and closes dealings, attests, disputes, sits as a steward, and issues seals.

Every conforming application computes the same karma from the same record. What an application decides is what to show: which marks it reads, what bar it sets, how it ranks what it finds. One weighs recent dealing, another long histories, a third only the marks that bear on a trade.

Karma DOT[^dot] is one such metric: for a key of karma k and age a blocks, DOT is k over (a + c), where c is a settling constant the reader chooses. Dividing by age reads tempo rather than total, so an idle key thins as its divisor grows.

FIGURE karma-dot :: Karma DOT, an application-layer metric: a key's score today over the blocks it has been alive, with a settling constant added to the divisor.

An application may also read the record as a gate. A context sets a bar of karma, and any key whose record clears it is read in: a role filled, access granted, a match made. A gate reads and acts, and it resolves the moment it reads.

FIGURE one-record :: Two applications cut the same keys by different criteria. The record beneath them, and the karma, are one.

## Closing

One construction carries the protocol. Two keys fix the outcomes and the oracle, the oracle rules, and the record keeps one mark for each of them. A quorum seat is that construction with a bond attached, a seal is it applied to a claim, and karma is what a key's marks add to.

[Read the collaborative research paper.](nown-article.html) · [Contribute on GitHub.](https://github.com/nownto/nown)

## References

1. J. R. Douceur. The Sybil Attack. IPTPS, 2002.
2. E. J. Friedman, P. Resnick. The Social Cost of Cheap Pseudonyms. Journal of Economics and Management Strategy, 2001.
3. T. Dryja. Discreet Log Contracts. MIT Digital Currency Initiative (manuscript), 2017.

[^karma]: The score a key accumulates on the record: the sum of its marks, one written for each dealing it closes, up where the dealing was ruled correct and down where it was not. The word is borrowed from the idea that a person's actions accumulate into what he is.
[^dot]: Delta over time. A key's karma divided by the time it has been alive, plus a small settling constant, giving the density of dealing it has sustained rather than the total it has amassed. An application-layer metric, computed from the record like any other reading.
[^oracle]: An agreed source that settles a question a system cannot settle for itself, the way an oracle in antiquity was consulted for an answer taken as final. Here: the parties' own attestation, or a quorum.
[^quorum]: Originally the least number of members a body needs present for its decision to count; by extension, the panel itself. Here, the panel of strangers called to rule one case by majority.
[^steward]: One who keeps a duty in trust for others and answers for it without owning what he keeps. Here, a member of a quorum, called to rule a single case and paid for ruling it with care.
[^pgt]: Pretty good trust, by descent from pretty good privacy: usable, decentralized, computed by each reader, sufficient for people to act on, and never perfect.
[^blocktime]: Block time is a decentralized measure of time defined by globally verified proof of work rather than any clock, government, or trusted authority.
