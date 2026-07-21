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

Age counts for nothing. A key ten years old that has done little is worth less than a key a month old that has dealt well and often. Trust follows conduct, not existence. Karma measures how densely a key has dealt well over a recent stretch of time, weighed against the harm it has done. Leave the key idle and the measure thins, because time keeps moving while your conduct does not. Holding high standing means earning it again and again, the way a business keeps its place only by continuing to serve. Climbing is quick. Staying up is the work. A key that has held its density high across many years has shown the one thing a young key cannot, that it lasts.

## 4. How karma moves

Karma changes through one kind of event: a dealing between two keys that ends in success or failure. A dealing is any exchange they put something behind, a trade, a piece of work, a contract, a document to certify. They enter a context, deal, and the outcome is written against both.

A context is a construct one user sets up for a use of trust. It fixes two things: how the outcome is decided, and how karma flows from it. Whoever needs the trust defines the context, and other keys step into it under their own keys.

Karma flows from a dealing. To gain it you need another key to deal with you and the dealing to succeed. A key that deals with you puts a measure of its own standing behind the outcome. On success, karma flows to you from that standing, in an amount set by the stake the two of you put at risk and by how much standing the other key carried. Dealing well with a proven key is worth more than dealing with an unknown, and each of you flows standing to the other. On failure, the key that broke the dealing takes a permanent mark, and the key that vouched by dealing loses the standing it had staked. That loss is why a high-standing key is careful whom it deals with, and that care is what makes its word worth carrying.

The outcome settles the moment the oracle[^oracle] speaks, and only then does karma move. It is made by a dealing that succeeds and unmade by one that fails, bounded at every step by real value at real risk. None is printed from nothing, and none is taken from a key that was not part of the dealing.

## 5. The success oracle

Something has to decide whether a dealing succeeded. A context picks how, and it can combine ways.

The parties can attest. Both sign that the dealing closed as agreed, and silence with the time run out reads as success. Most dealings end here, with no one else ever involved.

A quorum[^quorum] can judge. When one party disputes, or when a context needs a fact certified, a panel of high-standing strangers is drawn at random for the one case, unknown to the parties and to each other. Each reads the same evidence and answers alone, and the answer that carries is the one most of them give. The same panel that settles a payment can certify that a contract was met, that a delivery arrived, that a translation is faithful, or that a marriage took place, so trust reaches past money into anything two keys can put on the record.

Karma can be its own oracle. A context reads standing directly and the outcome follows. An employer sets the karma a role demands, and the keys that clear it are the ones he considers; a gate opens when a key passes a bar. No panel is called, and the reading settles the matter.

A context can also borrow an oracle it already trusts, an outside system or authority, and use Nown only to record what it rules. That context is no longer trustless, but the standing it writes still carries.

## 6. Your key is your property

A key is yours to do with as you please. You keep it, you lend it, you sell it, because whoever holds the private key holds everything the key carries, standing and all. No one can force a sale onto the record, and no one can stop one off it. A change of hands is written only if someone writes it, so the network may never learn a key found a new owner. It learns soon enough from how the key behaves afterward.

## 7. Proving without showing

A key proves what a counterparty needs and shows nothing more. Under Nown a key can prove that its karma under a stated set of rules clears a bar, that a success it claims was with a counterparty of at least some standing, or that an oracle ruled as it says, all without opening its history or naming who it dealt with. The counterparty reads one fact, the one the context asked for, and the rest of the record stays the key's own business.

## 8. Reading, and more than one Nown

No one hands you your karma. Each reader computes it, applying the same rules to the same record and reaching the same figure. Different readers can run different rules for different purposes, so more than one Nown can exist at once. A network that serves people well draws them in, and its reading of trust becomes the one that counts, while the others keep working for whoever still wants them. The rules are open and the record is shared, so no version can lie about the past. A version can only choose how to weigh it.

## 9. Arbitration, one use of the whole

Trust settles most dealings before they can go wrong. When one goes wrong anyway, someone must decide who is owed what, and that decision has been captured by an authority in every age before this one. Nown draws it instead from the quorum, and the ruling is written like any other outcome. It moves the money the two traders had already set aside for exactly this, money no one but the two of them ever holds, and it marks the standing of each. A steward[^steward] earns by answering as the majority answers, and strangers drawn apart, reading the same evidence, land on what it best supports. Arbitration is the use of karma where its teeth show clearest, and it is one use among as many as trust has prices.

## 10. Known issues

Some parts are not solved. Each is named here, with a place to work on it.

The record must be tamper-proof. Guarding it with a network of miners, paid in a coin minted for the purpose, is impractical for a protocol that mints no coin. Nown must either anchor its record to a proof-of-work record strong enough to borrow, or find an incentive that keeps the record honest on its own. Which of the two is open.
[Work on this problem.](https://github.com/nownto/nown/issues)

Karma flows only from a real dealing, so a context has to tell a real dealing from a staged one. Two keys that fake a dealing between themselves to lift their standing are an oracle problem of their own, with no general answer yet.
[Work on this problem.](https://github.com/nownto/nown/issues)

A ring of real people can deal with each other honestly and often, raising each other's density with dealings that are real but closed. Telling a busy open trader from a busy closed clique means reading the shape of the graph, and the reading is not yet airtight.
[Work on this problem.](https://github.com/nownto/nown/issues)

The rule for how much karma a success flows, and how fast idle standing thins, has to be set so neither the patient nor the rich climbs faster than honest dealing allows. These constants are open.
[Work on this problem.](https://github.com/nownto/nown/issues)

Telling one person from a thousand cheap keys, with no document binding a key to a human, is unsolved everywhere, and Nown does not solve it. It raises the cost of pretending until pretending stops paying.
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

[^karma]: Your standing, computed by anyone from your public record. Not held by the key; derived from it.
[^oracle]: Whatever a context uses to decide a dealing succeeded: the parties attesting, a quorum, or karma itself.
[^quorum]: A panel of high-standing strangers drawn at random to judge one case, anonymous to the parties and to each other.
[^steward]: A member of a quorum. Drawn at random, anonymous, paid only for answering with the majority.

---

*Released into the public domain under the Unlicense. No rights reserved. No owner.*
