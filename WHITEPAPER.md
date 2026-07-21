# Nown: A Protocol for Portable Trust

**v0.1.** Released into the public domain (the Unlicense).

## Abstract

Nown is a protocol for trust between strangers. You act under a key, and the record of how that key has behaved is public and permanent, readable by anyone who runs the protocol. You build your standing by dealing well with others, and you carry that standing wherever Nown is read. No platform grants it, and none can take it away. The measure of your standing is called karma.[^karma] It rises when you succeed and falls when you fail, and it flows to you from the keys who deal with you and stake their own standing on the outcome. Settling a dispute is one use of it. There is no company behind Nown, no owner, and nothing it charges for.

## 1. The problem

Two strangers cannot deal until each believes the other will keep his word. For as long as there has been trade, a third party has supplied that belief: a guild, a court, a bank, a platform. Each of them can be bribed, coerced, shut down, or quietly corrupted, and each owns the reputation it keeps. Your standing lives on its servers, under its rules, at its pleasure, and it vanishes when the keeper does. The stranger you want to deal with is trusting the keeper, not you. Nown removes the keeper and leaves the trust with the two people who need it.

## 2. The key and the record

You act under a key. Whoever holds the key is you, as far as the network can tell, and no registrar stands between you and it. Trust needs someone to trust, so a key is meant to be kept. Throw one away after each deal and you build nothing; keep one and it gathers a history. The key carries no name unless you add one. You may write to your own key the things you want a counterparty to see, a brand, a handle, a claim about who you are, and the network carries them beside everything the key has done.

Every key's history sits on one public record that only grows. A deal closed, a dispute lost, a mark of standing gained: each is written once and never unwritten. Nothing is edited after the fact, nothing is deleted, nothing is hidden. What a key did is what it did, for as long as the network runs. Hardening that record against tampering, without spending real energy to do it, is not yet fully solved.

## 3. Karma

Karma is the measure others read from your record. It is your standing, held under your key, computed by anyone who cares to look.

Seniority counts for nothing by itself. A key ten years old that has done little is worth less than a key a month old that has dealt well and often. Trust follows conduct, not age. The time is not thrown away, though: it is the span the conduct is measured across, so what a reader weighs is not how long a key has lived but how much good dealing it packed into the years it has. Leave the key idle and the measure thins, because time keeps moving while your conduct does not. Holding high standing means earning it again and again, the way a business keeps its place only by continuing to serve. Climbing is quick. Staying up is the work. A key that has held its density high across many years has shown the one thing a young key cannot, that it lasts.

## 4. How karma moves

Karma changes through one kind of event: a dealing between two keys that ends in success or failure. A dealing is any exchange they put something behind, a trade, a piece of work, a contract, a document to certify. They enter a context, deal, and the outcome is written against both.

A context is a construct one user sets up for a use of trust. It fixes two things: how the outcome is decided, and how karma flows from it. Whoever needs the trust defines the context, and other keys step into it under their own keys.

Karma flows from a dealing. To gain it you need another key to deal with you and the dealing to succeed. To deal, a key stakes a measure of its own standing on the outcome. On success, karma flows to you from that staked standing, and dealing well with a proven key is worth more than dealing with an unknown, since the proven key put more of itself at risk. On failure, the key that broke the dealing takes a permanent mark, and the key that vouched by dealing loses the standing it staked. That loss is why a high-standing key is careful whom it deals with, and that care is what makes its word worth carrying. What the flow reads is standing, not the worth of the trade.

The outcome settles the moment the oracle[^oracle] speaks, and only then does karma move. A fresh key holds nothing at all, worthless like an address that has never been used, and karma is minted only by dealing: a good outcome creates new standing for both, bounded by the standing staked. So the supply grows with honest dealing and is never locked to whoever came first, while a thousand empty keys dealing among themselves mint nothing, because they bring no standing to bound it. How a true newcomer climbs from zero is open work.

## 5. The success oracle

Something has to decide whether a dealing succeeded. A context picks how, and it can combine ways.

The parties can attest. Both sign that the dealing closed as agreed, and silence with the time run out reads as success. Most dealings end here, with no one else ever involved.

A quorum[^quorum] can judge. When one party disputes, or when a context needs a fact certified, a panel of high-standing strangers is drawn at random for the one case, unknown to the parties and to each other. Each reads the same evidence and answers alone, and the answer that carries is the one most of them give. The same panel that settles a payment can certify that a contract was met, that a delivery arrived, that a translation is faithful, or that a marriage took place, so trust reaches past money into anything two keys can put on the record.

Karma can be its own oracle. A context reads standing directly and the outcome follows. An employer sets the karma a role demands, and the keys that clear it are the ones he considers; a gate opens when a key passes a bar. No panel is called, and the reading settles the matter.

A context that needs a trusted or outside oracle does not run on the main network, where a corruptible party would dilute the trust the record keeps clean. It runs instead as a fork, a separate Nown with its own rules. The main record admits only oracles no one owns: the parties, a quorum, or karma itself.

Whatever the oracle rules is the outcome, and Nown claims no truth beyond it. It does not ask how a party won, or whether he was fair, or whether he lied, because a man's means are his own and policing them is not the protocol's work. A deal one side rigged is still true if the counterparty accepts it or a quorum upholds it. What Nown makes costly is losing: a lost dealing marks your record for good, moves the money you staked, and burns the standing behind you. Make losing dear enough, and honest dealing pays for itself.

## 6. Your key is your property

A key is yours to do with as you please. You keep it, you lend it, you sell it, because whoever holds the private key holds everything the key carries, standing and all. No one can force a sale onto the record, and no one can stop one off it. A change of hands is written only if someone writes it, so the network may never learn a key found a new owner. It learns soon enough from how the key behaves afterward.

## 7. Proving without showing

A key proves what a counterparty needs and shows nothing more. Under Nown a key can prove that its karma under a stated set of rules clears a bar, that a success it claims was with a counterparty of at least some standing, or that an oracle ruled as it says, all without opening its history or naming who it dealt with. The counterparty reads one fact, the one the context asked for, and the rest of the record stays the key's own business.

## 8. One record, many readings

No one hands you your karma. Each reader computes it, applying the same rules to the same record and reaching the same figure. This is what lets many applications sit on one Nown: a Nown browser is a client that reads the one record and shows whatever slice of it a user asks for, one weighing recent dealing, another long steady histories, a third only the dealings that bear on a trade. These are not separate Nowns but separate views of the same record, and none can lie about the past, because the record beneath them is one. A truly separate network is a fork, with its own rules, for a use the main one will not serve, and it is rare. The common case is one Nown read many ways.

## 9. Arbitration, one use of the whole

Trust settles most dealings before they can go wrong. When one goes wrong anyway, someone must decide who is owed what, and that decision has been captured by an authority in every age before this one. Nown draws it instead from the quorum, and the ruling is written like any other outcome. It moves the money the two traders had already set aside for exactly this, money no one but the two of them ever holds, and it marks the standing of each. A steward[^steward] earns by answering as the majority answers, and strangers drawn apart, reading the same evidence, land on what it best supports.

Capture is beaten by size, not by watching for it. The panel is drawn at random from the whole network, so to swing a verdict an attacker must buy a majority of a panel he cannot see in advance, drawn from a pool he does not control. As the network grows the pool grows, the panel drawn from it grows, and the number an attacker must find and corrupt to have any chance climbs faster than the panel itself. A larger Nown fields larger, harder quorums, and a case that stalls for want of answers is met by drawing more seats, not fewer. The exact rate belongs to the network's size and is left to calibration.

FIGURE quorum-scaling :: As the network grows, the quorum drawn for a case grows with it, and the cost to swing a verdict, buying a majority of an unfindable random panel, climbs out of reach faster than the panel itself.

Arbitration is the use of karma where its teeth show clearest, and it is one use among as many as trust has prices.

## 10. Known issues

Some parts are settled in shape but not in detail. Each is named here, with a place to work on it.

A fresh key holds nothing, and karma is minted only by dealing, bounded by the standing each side brings. So a newcomer must earn his first karma from a key that already has standing, and the rule that lets him climb from zero without letting a faker mint from a thousand empty keys is not yet fixed. The bound is the defense; calibrating it is the work.
[Work on this problem.](https://github.com/nownto/nown/issues)

The record must be tamper-proof, and a network of miners paid in a coin is impractical for a protocol that mints no coin. Nown either anchors to a proof-of-work record strong enough to borrow, or finds an incentive that keeps a record honest on its own. Which of the two is open.
[Work on this problem.](https://github.com/nownto/nown/issues)

The record itself is too large for that chain, so it lives on a network of nodes that each keep a copy, anchored to the chain so none can rewrite it. What keeps a node storing and serving with no coin to pay it is the same open question, one more place trust must come from incentives, not a token.
[Work on this problem.](https://github.com/nownto/nown/issues)

Karma is computed under constants, how fast idle standing fades and how much a success weighs. The base protocol must fix a default set so every reader reaches the same figure. Choosing them well is design work, not a guard against anyone: a key that deals more, or bigger, and so climbs faster has earned it.
[Work on this problem.](https://github.com/nownto/nown/issues)

Collusion in a quorum is priced out by the panel's size and randomness, and a stalled case is answered by a larger panel. The function tying a network's size to its quorum's size is still to be derived.
[Work on this problem.](https://github.com/nownto/nown/issues)

## 11. What it is for

Nown gives a person a trust that is his own: built by his conduct, carried under his key, read by anyone, held by no one who can take it back. It does not try to make people good or to catch every liar, and no protocol can. It puts conduct on one honest record, so a stranger is judged by what he has done rather than by whose permission he carries. Arbitration between strangers, the oldest work of civilization, becomes something one person can reach without asking anyone. The result belongs to everyone, because a thing meant for everyone must be owned by no one.

## References

1. J. R. Douceur. The Sybil Attack. IPTPS, 2002.
2. E. J. Friedman, P. Resnick. The Social Cost of Cheap Pseudonyms. Journal of Economics and Management Strategy, 2001.
3. S. Micali, M. O. Rabin, S. P. Vadhan. Verifiable Random Functions. FOCS, 1999.
4. V. Shnayder, A. Agarwal, R. Frongillo, D. C. Parkes. Informed Truthfulness in Multi-Task Peer Prediction. ACM EC, 2016.
5. T. Dryja. Discreet Log Contracts. MIT Digital Currency Initiative (manuscript), 2017.
6. E. Hughes. A Cypherpunk's Manifesto. 1993 (essay, activism.net).
7. L. Dover. Chronicle: An Open Protocol for Public Trust and Accountability on the Web. Cartographers Guild, https://chronicle-network.org (accessed 2026). Related work.

[^karma]: A person's standing, computed by anyone from the public record of how his key has dealt. The word is borrowed from the idea that a person's actions accumulate into what he is. Not a number the key holds; each reader derives it from the record.
[^oracle]: An agreed source that reports whether something is true, feeding a fact the system cannot check for itself into a decision, the way an oracle in antiquity was consulted for an answer taken as final. Here: the parties, a quorum, or a reading of karma.
[^quorum]: The number of members who must take part for a body's decision to count, and by extension the panel itself. Here, the strangers drawn to settle one case by majority.
[^steward]: Someone who holds a duty in trust for others and answers for it without owning it. Here, one of the strangers drawn onto a quorum to judge a case.

---

*Released into the public domain under the Unlicense. No rights reserved. No owner.*
