# Nown

### The full construction

Released into the public domain (the Unlicense).

## Abstract

Nown is a protocol for trust between strangers with no trusted third party. A person acts under a keypair, and the public record of how that key has dealt becomes his standing, which anyone can read and no one can revoke. That standing is karma: a density of good dealing over time, held under a key that is his to keep or sell, flowing to him from the keys that stake their own standing to deal with him, confirmed by an oracle. A dispute settled by a drawn panel of strangers is one use. A worker hired on his record, a student vouched for by his teacher, and a certificate notarized without a notary are others. The parts that are not solved are named, each with a place to work on it.

## 1. The keeper is the flaw

Two strangers cannot deal until each believes the other will keep his word. For as long as there has been trade, a third party has supplied that belief: a guild, a court, a bank, a platform. Each can be bribed, coerced, shut down, or quietly corrupted. Each owns the reputation it keeps, so your standing lives on its servers, under its rules, and dies when it does. The stranger you want to deal with is trusting the keeper, not you.

Remove the keeper and the trust has to come from somewhere else. It comes from the record of what you have done, kept by everyone and owned by no one, and from the standing that other people put at risk when they choose to deal with you. Nown is the construction that makes those two things carry the weight the keeper used to carry.

## 2. The key and the record

A person acts under a key.[^key] The private half he holds and never shows. The public half is the name everyone sees. Whoever holds the private half is the person, as far as the protocol can tell, and no registrar stands between a man and the key he made. A key carries no legal name unless he attaches one, and he may hold as many keys as he likes, each with its own standing and its own history, each blind to the others.

A key is meant to be kept. Throw one away after each dealing and you build nothing a counterparty can weigh. Keep one and it gathers a history, and the history is the point.

Every key's history sits on one public record that only grows. A dealing closed, a dispute lost, a mark of standing gained: each is written once and never unwritten. Nothing is edited, nothing is deleted, nothing is hidden. The record is the ground the protocol stands on, and making it tamper-proof without a company to guarantee it is the hardest problem Nown has. Its answer is the timechain.

## 3. Karma density

Karma[^karma] is the standing a reader computes from a key's record. It is not a number the key holds and hands out. It is derived from the events on the record that name the key, by rules every reader shares, so two readers reach the same figure.

Age counts for nothing. A key ten years old that has done little is worth less than a key a month old that has dealt well and often. Trust follows conduct, not existence. What matters is not how long a key has lived but how much good dealing it has packed into recent time, against how much harm.

So karma is a density. Each event is a signed weight, positive for a success, negative for a failure, scaled by the stake behind it. Karma is the sum of those weights over a trailing window, with older events fading as the window moves on. Leave a key idle and its karma thins toward zero, with no bad mark against it, because the window keeps moving while the conduct does not.

Two things follow, and they are the whole point of measuring density instead of a total. Climbing is quick: deal well and often and fresh weight piles up faster than the old weight fades. Holding is slow: to keep a high figure you must keep dealing, replacing what the window drops, the way a business keeps its position only by continuing to serve. A key that has held a high density across many years has shown the one thing money cannot buy in a hurry, which is that it lasts.

The unit is the change in karma over time, which the protocol carries as **Karma DOT**,[^dot] delta over time. Two keys with the same lifetime tally are not the same if one earned it in a burst and let it fade while the other has held it steady. DOT is what a reader is really after, and it is why the clock the density is measured against matters as much as the events. That clock is the timechain.

## 4. How karma flows

Karma changes through one kind of event: a dealing between two keys that ends in success or failure. It is never minted, never printed, never granted for free. To gain karma you need another key to deal with you and the dealing to go right.

A key that deals with you puts a measure of its own standing behind the outcome. That is the source of your gain. On success, karma flows to you out of the standing the other key staked, and the amount turns on two things: the stake the two of you put at risk, and how much standing the other key carried. A thousand dollars trusted to you says more than ten. A proven key dealing with you says more than an unknown, because the proven key had more to lose. Each of you flows standing to the other, so a good dealing between two strong keys lifts both, and a good dealing between a strong key and a weak one lifts the weak one more.

Failure runs the other way. The key that broke the dealing takes a mark that never leaves its record. The key that vouched by dealing loses the standing it staked, because it trusted someone who failed. That second loss is the discipline of the whole system. A high-standing key that deals carelessly bleeds its standing into the failures it backed, so it learns to deal only where it believes the other side will perform. Its willingness to deal with you is worth something precisely because it is not given away.

This is why an assertion moves nothing. A key that merely says another is trustworthy has staked nothing and risked nothing, and standing a key can hand out for free is standing a ring can hand itself. Karma moves only when a real dealing, with something at stake, comes out right.

## 5. What counts as a dealing

A dealing is any exchange two keys put something behind: a trade, a job done, a contract kept, a document certified, a course taught. The something at stake is what makes the outcome mean anything, and it is what a faker has to fake.

Which raises a hard question the protocol does not fully answer. If an application that runs Nown lets two keys record a dealing, what stops them from recording dealings that never happened, purely to move karma between themselves? Deciding that a dealing was real is itself an oracle problem, the same shape as deciding that a dealing succeeded. Some contexts answer it cheaply: an escrow that moved real money is hard to fake, a delivery a third party signed for is hard to fake, a payment on a public rail is hard to fake. Others cannot, and there the standing earned is only as trustworthy as the context that recorded it. Nown does not pretend to a general answer. The problem stays open, and the honest position is that a context is responsible for the reality of the dealings it feeds the record, exactly as it is responsible for the oracle that judges them.

## 6. The oracle

Something has to decide whether a dealing succeeded. A context picks how, and the choice is the context's to make.

The parties can attest. Both sign that the dealing closed as agreed, and silence once the agreed time has run out reads as success. Most dealings end here, cheaply, with no one else ever looking. An honest trade that goes right needs no judge.

A quorum can judge. This is the answer when one party disputes the outcome, or when a context needs a fact certified that the parties cannot settle between themselves.

Karma can be its own oracle. A context reads standing directly and lets the outcome follow. An employer sets the karma a role demands, and the keys that clear the bar are the ones he considers. A gate opens when a key passes a threshold. No panel is called; the reading settles the matter, and the dealing resolves the instant it is done.

A context can also borrow an oracle it already trusts. An existing authority, a court, a registry, an exchange, rules on the outcome, and Nown records what it ruled. A context built this way is not trustless, since it leans on the outside authority, but it still gives that authority's judgments a portable, permanent home and lets standing accrue from them. This is how Nown reaches into a world that has not adopted it yet: it improves the bureaucracy that exists before it replaces any of it.

## 7. The quorum

When a dispute needs a stranger to settle it, Nown draws a panel and asks it a plain question. The design is simple on purpose, and every part of it exists to keep the panel honest without an authority standing over it.

The panel is drawn at random from keys of high standing, several steps removed on the record from both parties, so no one who has dealt with either can sit. It is drawn for the one case and dissolves when the case ends. Its members are pseudonymous to the parties, to each other, and to anyone relaying the traffic. No one can find the panel to bribe it, and no one can pack it, because no one chooses it.

Each steward[^steward] reads the same evidence and answers one question in private: which party does the evidence favor. The answer that carries is the one most of them give. That is the whole rule. The quorum does not find the truth and does not pretend to. It is a guessing game whose focal point is the evidence: each steward is really answering what he believes most other honest readers of the same evidence will conclude, and on clear evidence that is simply what the evidence shows. Strangers drawn apart, who cannot coordinate, converge on the reading the evidence best supports, because that is the only answer each can expect the others to reach.

The votes are secret, and only the count is ever published. No one can show afterward how a given steward voted. This is not decoration. A vote that could be proven is a vote that can be bought or punished, so the protocol makes each ballot unprovable and leaves a briber with nothing to verify and a thug with no one to blame. What the panel reveals is a number, never a name.

A steward earns for answering with the majority, enough to cover the cost of reading the evidence with care. A steward who votes at random, or sells his vote to a bloc that reads the evidence the same wrong way, earns less than one who reads honestly, because honest strangers land together and careless ones scatter. The reward needs no knowledge of the truth, only the public count.

The case cannot hang forever, because a ruling that could be stalled would be worth money to stall. A deadline runs from the moment the case opens. Enough stewards are seated that a few going silent changes nothing, and if the panel still fails to reach a count, the stakes return to the parties along terms they signed before the dealing began. When the panel does rule, the ruling is written like any other outcome: the money the two of them set aside moves to the party upheld, and a karma event is written for each, a success for the one and a failure for the other, flowing standing exactly as a settled dealing does.

No appeal follows, and no later panel reopens the record. Finality is the value. A judgment that could be revisited is a judgment no one can rely on, and the point of the quorum is to end the matter.

## 8. The record and the clock

Karma is a density over time, so the record needs two things it cannot fake: an order that cannot be rewritten, and a clock that reads the same for everyone. A company could provide both and would then own both. Nown cannot use a company, so it borrows from the one system that already solved this without an owner.

The timechain,[^timechain] bitcoin's public ledger of blocks, is a record no one can rewrite: each block builds on the last, ordered by proof of work, and undoing one means redoing all the work since. It is also a clock. Every block is a tick, the same tick for everyone who reads the chain, owned by no one and stoppable by no one. Its ticks are coarse, roughly one every ten minutes, and that is fine, because karma density does not need the second, it needs a shared and permanent measure of when. Pin a key's first block and read the latest, and the span between them, counted in blocks, is the denominator that turns a tally into a density. Finer time is a matter of presentation, not protocol: readers already localize block times to the second from their own settings, the way a timechain browser shows a human date beside a block height. The protocol commits to blocks. A client may dress them up however it likes.

The borrowing has a cost. Proof of work is often called wasteful, which misses the point. It is impractical: a network of miners guards a record only because they are paid in the coin their work secures, and that coin is the incentive that keeps the record honest. Nown has no coin of its own and wants none, so it cannot run its own proof of work. That leaves two ways out. It can anchor its record to a proof-of-work chain strong enough to borrow, and only bitcoin's is, which ties Nown's permanence to bitcoin's. Or it can find an incentive that keeps a record honest with no coin at all.

The second path is open research, and the shape of the answer is already visible in an older idea. When Phil Zimmermann built PGP,[^pgp] he did not promise perfect privacy, and he did not build a central authority to grant it. He let every user be his own authority, choosing whom to trust and computing, from signatures he had collected, whether a key was good enough to rely on. Zimmermann called the result a "decentralized fault-tolerant web of confidence."[^web] It was never perfect, and it never had to be. It was pretty good, and pretty good was usable where perfect was unavailable.

Human action runs on the same currency. A man does not need perfect trust to deal with a stranger; he needs pretty good trust, enough to act on, priced for the risk he is taking. Call it PGT, by the plain descent from Zimmermann's phrase. Fiat money needs trust in an issuer and bitcoin abolished that need, but trust between people was never going to be abolished, only made portable, computable, and owned by the person who earned it. A record kept honest by the incentives of the people who read and write it, rather than by an outside coin, is the standalone answer if one exists. Nown does not claim to have built it. It claims that the problem is the right one, that the timechain solves it today by borrowing, and that PGT is the shape a native solution would take.

Where PGP is a precedent and not a template, the paper says so. PGP signs that a key belongs to a person, a narrow and near-binary fact. Nown signs conduct across dealings, which is graded and never finished. The lineage Nown claims from PGP is the architecture, decentralized, reader-computed, honestly imperfect, not the specific thing being certified.

## 9. A key is property

A key is owned by whoever holds its private half, and it can be kept, lent, or sold like anything else a man owns, because holding the private half is holding everything the key carries, its history and its standing alike.

This makes standing portable in a second sense. A reputation built under one key can pass to a buyer, so a business that has dealt well for years can be sold with the key that carries its name, and the buyer steps into a going concern instead of starting from nothing. A key is worth what someone will pay for it, and a market in keys prices reputations the way a market in businesses prices goodwill. Nown carries monetary value for this reason, with no coin of its own: the value rides on the keys.

No sale can be forced onto the record, and none can be stopped off it. A change of hands is written only if someone chooses to write it, and there is no way to make a man announce that he sold a key or bought one. So the network may never learn a key changed owner. It learns soon enough from conduct. A buyer who keeps dealing well keeps the standing he paid for, and the density he inherited carries him only as far as his own dealings sustain it, since the window fades an inherited history like any other. A buyer who cashes the standing out in one last scam spends it, and the record keeps the exit for the next reader to see. Both the patient buyer and the fast one already exist wherever businesses change hands, and Nown records both without preventing either.

## 10. Proving without showing

A man's whole dealing history is his own business, and a counterparty usually needs one fact from it, not the ledger behind it. Nown lets a key prove the fact and reveal nothing more.

A key can prove that its karma, under a stated set of rules, clears a bar, without opening the events the figure was computed from. It can prove that a success it claims was with a counterparty above some standing, without naming the counterparty. It can prove that an oracle ruled as it says. In each case the reader checks a short proof and learns the one fact the context asked for. A man can walk up to a market that demands a karma of a thousand and prove he has it, while the market learns neither whom he dealt with nor how far past the bar he sits.

The simplest proof of all is a signature. A key that signs a fresh message proves, to anyone, that its holder is present and in control, right now. Attach that signature to a public karma profile and it becomes a claim the reader can check himself: this living person holds this key, and this key holds this record. That is the seed of the uses that follow.

## 11. More than one Nown

No one issues a key's karma. Each reader computes it, running shared rules over the shared record, and two readers who run the same rules reach the same figure. Standing is settled by a computation anyone can repeat, not by an authority anyone must trust.

Because the rules are chosen rather than decreed, more than one set can run at once. One reading weights recent dealing heavily and forgets fast. Another rewards long steady histories. A third reads only a slice of the record that bears on a trade it cares about. Each is a version of Nown, reading one underlying record through a different lens, and none can lie about what a key did, because the record is one. A version can only choose how to weigh it. An application built on Nown is mostly a choice of lens: which dealings it counts, what karma its context demands, how it presents a block height as a date. The protocol holds the record and the rules of the flow. Everything above that is a filter someone wrote for a use of his own.

## 12. What it is for

Karma is the product, and its uses run as wide as trust has prices. Four show the range.

**A dispute, settled.** Two strangers escrow a trade in an output only the two of them control, and deal. If it goes right they attest and the escrow releases. If it goes wrong they open a dispute, the quorum rules, and the ruling moves the escrowed money and marks each key. This is the use where the teeth show clearest, because real money hangs on the answer. It is one use, not the definition.

**A worker, hired.** An application that runs Nown lets an employer describe the karma a role demands: this much standing, in dealings of this kind, held this steadily. It finds the keys that match and, where a key has published a way to reach its holder, reaches out; or it lets those keys raise a hand. A candidate proves he clears the bar by signing a fresh message with his private key, and that signature, beside his public profile, is proof of eligibility the employer can check without a resume, a reference, or a school. The signature and the key together are the oracle the hiring context resolves on: any holder who signs and clears the bar is a valid answer, and the employer picks among them.

**A degree, replaced.** A man wants to prove he knows a field. Instead of paying a university for a certificate, he studies under a master of the field, a working expert who takes students. The teaching is a dealing: the master is paid, and at the end he signs a badge for what the student showed. The master stakes his own standing to sign it, because a badge on a student who cannot do the work costs the master the standing he vouched with, exactly as a failed dealing costs any voucher. Years later the student applies for a post, and the employer sees that a prominent name in the field put his own reputation behind this man, at his own risk. The master vouched by teaching and signing, which is a real dealing with a real stake, not a free endorsement. A credential becomes a chain of people who staked their names, readable end to end.

**A certificate, notarized without a notary.** Two people marry and want it on a record that outlives any registry. A translator swears his translation is faithful and wants that on record too. A context sets a quorum, or a single trusted checker, to certify the fact, and the certification is written like any other outcome. No state office holds the paper, no notary holds the stamp. The record holds the fact, the standing of whoever certified it stands behind it, and anyone can read both. Trust reaches a plain human need, with no money changing hands and no authority in the middle.

In every case the shape is the same. Someone defines a context and its oracle for a use of trust. Other keys step in under their own keys. The outcome, however it is decided, writes a karma event that flows standing by the one rule that governs all of them. The protocol supplies the trust. People supply the uses.

## 13. The cost of faking

A standing anyone can read is worth faking, so the flow is built so faking costs more than it returns.

Karma is never printed. It flows only from a real dealing with a real, separate counterparty, at a real stake, confirmed by an oracle. To lift a key's density you must find keys willing to deal with you and to come out right, and each stakes its own standing to do so.

A ring of keys that deal only with each other is the obvious attack, and it fails on two counts. Its members can flow only their own standing to each other, which starts near zero and stays bounded, so a closed ring cannot lift itself above the honest baseline by trading inside itself. And the ring shows on the record as a closed loop, a cluster that deals with itself and rarely with the wider graph, which a careful reader discounts. To gain real standing the ring needs an outside high-standing key to deal with it, and that key stakes its own standing to do so, which it will not spend on a cluster it can see is closed. Reading the shape of the graph well enough to discount a farming ring without punishing a small honest community that happens to trade mostly among itself is not yet airtight, and it stays open.

## 14. Known issues

Nown rests on reasoning about how people act, not on a record of it running, and no early data would settle the questions that remain. Five are open, and naming them is the honest thing and the useful one, since each is a place to build.

**Securing the record without a coin.** The record must be tamper-proof, and a network of miners paid in a coin is impractical for a protocol that mints no coin. Nown anchors to bitcoin's timechain today, which works by borrowing. Whether an incentive exists that keeps a record honest on its own, the PGT problem, is open research.

**Telling a real dealing from a staged one.** Karma flows only from a real dealing, so a context must know its dealings are real. Where an escrow, a delivery receipt, or a public payment backs the dealing, this is cheap. Where nothing does, two keys can stage dealings to move standing between themselves, and deciding a dealing was real is an oracle problem with no general answer yet.

**Reading a closed ring.** A cluster that deals honestly and often among itself raises its own density with dealings that are real but insular. Discounting such a cluster by the shape of the graph, without punishing a small honest community, is not yet a settled computation.

**The constants of the flow.** How much a success flows, and how fast idle standing fades, must be set so neither the patient nor the rich climbs faster than honest dealing allows. The shape of the flow is fixed; the constants are proposals, to be tightened against use.

**Telling one person from many cheap keys.** Binding a key to a distinct human, with no document to appeal to, is unsolved everywhere, and Nown does not solve it. It raises the cost of standing up a thousand keys until it stops paying, and it says plainly that a determined attacker with a supply of real-seeming people is bounded by cost, not by a wall.

Each is a problem to work on, not a reason the protocol cannot run. A young network can launch with conservative constants and a hard cap on the value at risk in any one dealing, and tighten as the answers come.

## 15. The end of the keeper

Trade between strangers has always rested on someone trusted to vouch and someone trusted to judge, and each of them has been a place to capture the whole. Nown takes the vouching from the standing that keys stake on each other when they deal, draws the judging from a crowd no one can find, holds the money with the two parties alone, and keeps no power for itself. A man's standing becomes his own, built by his conduct, carried under his key, read by anyone, held by no one who can take it back. It does not make people good and does not catch every liar, because nothing can. It puts conduct on one honest record, so a stranger can be judged by what he has done rather than by whose permission he carries, and it leaves the uses of that record to the people who need them. The result belongs to everyone, because a thing meant for everyone must be owned by no one.

## References

1. J. R. Douceur. The Sybil Attack. IPTPS, 2002.
2. E. J. Friedman, P. Resnick. The Social Cost of Cheap Pseudonyms. Journal of Economics and Management Strategy, 2001.
3. S. Micali, M. O. Rabin, S. P. Vadhan. Verifiable Random Functions. FOCS, 1999.
4. C. Komlo, I. Goldberg. FROST: Flexible Round-Optimized Schnorr Threshold Signatures. SAC, 2020.
5. J. Groth, M. Kohlweiss. One-Out-of-Many Proofs: Or How to Leak a Secret and Spend a Coin. Advances in Cryptology, 2015.
6. T. Dryja. Discreet Log Contracts. MIT Digital Currency Initiative (manuscript), 2017.
7. P. R. Zimmermann. PGP User's Guide, Volume I: Essential Topics. Version 2.6.2. Phil's Pretty Good Software, 1994.
8. P. Zimmermann, J. Callas. The Evolution of PGP's Web of Trust. In Beautiful Security, O'Reilly Media, 2009.
9. J. Callas, L. Donnerhacke, H. Finney, D. Shaw, R. Thayer. OpenPGP Message Format. RFC 4880. IETF, 2007.
10. E. Hughes. A Cypherpunk's Manifesto. 1993 (essay, activism.net).
11. L. Dover. Chronicle: An Open Protocol for Public Trust and Accountability on the Web. Cartographers Guild, https://chronicle-network.org (accessed 2026). Related work.

[^key]: A keypair. The private half proves you are its holder and stays secret; the public half is your identity on the record. Holding the private half is owning the key, its history, and its standing.
[^karma]: A key's standing, computed from its public record by rules every reader shares. Not held by the key; derived from it.
[^dot]: Karma DOT, delta over time. Karma read as a density, the change in standing measured against the timechain clock, rather than a lifetime total.
[^steward]: A high-standing key drawn at random onto a quorum to judge one case. Anonymous, temporary, unpaid beyond the reward for answering with the majority.
[^timechain]: A public record of blocks kept by the bitcoin network, ordered by proof of work and impossible to rewrite. Nown uses it as a record no one owns and a clock that reads the same for everyone.
[^pgp]: Pretty Good Privacy, Phil Zimmermann's 1991 encryption software. Its web of trust let each user compute a key's trustworthiness from signatures, with no central authority, accepting a good-enough rather than perfect guarantee.
[^web]: Zimmermann, PGP User's Guide, Volume I, 1994.

---

*Released into the public domain under the Unlicense. No rights reserved. No owner.*
