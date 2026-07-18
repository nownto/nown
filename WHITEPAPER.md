# Nown: A Peer-to-Peer Protocol for Portable Trust and Merit-Based Arbitration

**v0.1.** Released into the public domain (the Unlicense).

## Abstract

Trade between strangers needs trust before the trade and judgment after it. Markets supply both through a trusted third party: a platform, an escrow agent, a rating bureau, a court. That party can be censored, bribed, subpoenaed, or shut down, and it owns the reputations and verdicts it issues. This protocol removes it from both. Reputation, called karma, is minted only by an irreversible burn tied to a settled dealing, so it proves an account's own conduct, never another's opinion of it, and it carries between contexts with no platform or identity document. Disputes are decided by a quorum of high-karma accounts drawn at random, anonymous to the traders and to each other, judging only the evidence each side submits. The quorum is an oracle: it attests a verdict a pre-signed escrow executes, and never holds the funds. Honest conduct is made the paying strategy by the structure of the reward, not by appeal to a higher authority, because there is none. There is no company, no token, and no owner. The protocol charges nothing, and rules on the trade, never on the person.

## 1. The problem

Two strangers agree to trade. Each must decide whether the other will perform. If one defects, someone must decide who is owed what. Today a trusted third party makes both decisions, and each such party is a single point of control. A platform censors, extracts rent, and dies by regulation. A named arbiter can be bribed, coerced, or subpoenaed. A rating bureau owns your reputation and rents it back to you. A vote weighted by tokens sells influence to whoever buys the most. Reputation built on one platform stays there and vanishes with it. Settlement of money became trustless once it was made objective and replicated; judgment resisted, because a verdict is a preference with no sum to check it against. The thesis of this paper is narrow: honest conduct can be made the paying strategy, and every party that could be captured can be removed.

## 2. Karma

Karma is the product, and dispute resolution is one use of it: a single number that rises only when an account pays for it and falls when the account is judged against, spending wherever trust is priced. It belongs to the person, not the platform, and travels when the person leaves.

Karma is minted at one source and one posted price: an irreversible burn attached to a dealing the account has settled, a sum paid into a provably unspendable output. Deposits, escrow held at risk, fees, and elapsed time mint nothing, because none of them leaves the world. Endorsement mints nothing either: standing one account can grant another is standing a ring can grant itself, and vouching for a stranger you never dealt with proves nothing about your own conduct, which is the one thing karma exists to prove.

The amount minted rises with the value burned, up to a fixed ceiling each period, and each further burn against the same counterparty is worth less than the last. A conservation follows: any set of accounts holds exactly the karma its own burns minted, whatever its internal shape, so a ring trading with itself earns no unit an honest merchant would not, and farms nothing by trading in a circle. Minted karma decays each period and is renewed only by fresh burns, so a parked account bleeds toward zero.

Karma is held by no one: it is read from a public record of signed events, as a balance is read from a ledger. An account's standing depends only on the events that name it, so any reader derives one account's karma from its own events alone, and because the weights are fixed by the protocol version, every client computes the same number.

## 3. The costly signal and the price of time

A rating that costs nothing to give is worth nothing, because a choice that costs something is the only evidence of a preference. So karma moves only on an act whose cost cannot be recovered: the burn, value destroyed beyond reach and bound to a dealing the account has settled. A free rating, a returned deposit, a stake merely held at risk: none leaves the world, and none moves karma.

If the only cost were money, the protocol would fall to whoever holds the most. Time is the honest price no one can buy more of: a day costs the wealthiest attacker and the poorest honest user the same. So karma is bounded by tenure: what an account can express is the smaller of the karma it holds and a ceiling that rises only as real time passes with the account unbroken, against a public clock no participant controls. A wealthy attacker can burn to the period's mint ceiling within a day, then waits years under the same clock as everyone else. The ceiling and the decay narrow the advantage of wealth without erasing it.

## 4. Escrow

A verdict must move funds or it is only an opinion, but handing them to whoever enforces it restores a trusted party. So the protocol splits the problem: judging the dispute is left to the quorum; checking that the quorum ran correctly is left to arithmetic anyone can repeat.

Funds sit in a two-of-two output controlled by the buyer and the seller alone, holding the price and both deposits, its outcomes signed in advance. If both agree they close it cooperatively and the quorum is never called; if the trade stalls, a timeout returns the funds. Either party alone may open a dispute by a signed opening that consumes the escrow, so the timeout can no longer run. A dispute may open only up to a fixed margin before that timeout matures, sized so a case opened at the last valid moment still concludes first; a later opening is void and the timeout stands, so no one can sit on a grievance until the eligible set drifts his way. Failing agreement, the funds move by exactly one pre-signed outcome, buyer paid, seller paid, or funds returned, each completed only by the quorum's single signature.

The quorum attests and never holds. It owns no key to the escrow and cannot take or freeze the funds, so no custodial liability arises. A verdict can rule only on facts that reach the record: proof of payment, delivery committed to a fingerprint, a signed receipt. Claims resting on a private, reversible rail wait for a proof that can be checked.

## 5. The quorum

A dispute empanels a quorum: an odd number of accounts, called stewards, drawn from those above a karma threshold, past a minimum tenure, and several steps from both parties in the trust graph, so no one who knows either trader can sit. Each takes its seat by posting a fresh bond, uniform for the tier, so karma buys only the eligibility, never a heavier vote. The share any single cluster can hold, of the eligible set and of the panel drawn, is capped, so a group that certifies itself cannot pack a quorum however large it grows. Stewards are anonymous to the traders and to each other; they never speak, and each reads the same file and votes alone.

These filters assume a populated graph. In a young network too thin to fill a panel, the required distance from the parties relaxes on a schedule fixed in advance and the escrow bound tightens in proportion, disclosed to both traders before they commit. Weak protection disclosed is a price a young network can choose; weak protection disguised would be a fraud by the protocol itself.

Within a case the quorum holds all the power. There is no judge to overrule it and no court of appeal. Every arbitration system before this one ends at an authority that can be captured; the protocol puts in that place a crowd no one can find, bribe by name, or coordinate, and takes its verdict as final. A right to reopen would only invite the patient and the rich to grind the poor into surrender.

## 6. Sortition

The quorum must be unpredictable before it is drawn and unknown after, or it can be bribed, threatened, or packed. Randomness from an outside committee would restore a trusted party, so it is taken from the protocol's own activity: every account carries a seed that changes as it acts, each action folded into an append-only log where it cannot be altered after the fact.

Timing must buy nothing. A dispute opens with a signed record naming one escrow; the first such record counts, and the clock mark under which it lands fixes the moment of opening and freezes eligibility. Entropy for the draw is collected only after the case file closes: the seeds of accounts acting inside a fixed window, the disputants excluded, are combined with the opening and passed through a delay function that takes a fixed span of wall-clock time no parallel hardware can hurry, and runs longer than the window can extend, so no one holds its output, the draw seed, before the window closes.

Each eligible account then checks privately, under its own key, whether the seed selected it. Selection proves itself and reveals nothing about the others, so the panel is a set of pseudonyms that exists for that case alone, unknown to the traders, to each other, and to any relay. No such draw is perfectly unbiasable; the design prices the remaining margin so that skewing a draw costs more than winning the dispute it would decide. The construction of the entropy, the delay function, and the selection proof belongs to the companion article.

## 7. The verdict

Each side seals its exhibits as fingerprints before either unveils, then publishes them in full, so a forgery must be built before the exhibit it rebuts is seen; the file is fixed before a single steward is drawn.

The quorum does not find the truth; it aligns the reward with honest reporting. Only stewards who land with the majority are paid. But a plain majority pays a good guess about the crowd as much as a good judgment of the case, so a steward is scored across a batch of cases for agreement above what the panel's voting habits would produce by coincidence. Reading the evidence is then the only strategy that pays, whatever the others do.

The seal needs no trusted opener, because the panel opens its own tally. Its members jointly build one key for the case that never wholly exists, so there is no holder to subpoena. Each steward casts a ballot sealed under that key, with a short proof that it holds one valid answer; sealed ballots add without opening, so the panel opens the counts alone, never a single ballot. A steward may re-post its sealed ballot at random moments, so a vote changed under coercion looks the same as one that changed nothing. Pay and penalty settle later by nameless proofs: a majority seat proves only that its hidden vote sat with the majority and collects an equal share through a ticket that names no seat, so no steward is ever linked to a case.

The penalty for a wrong verdict rises with how many stewards err together, so a bloc that moves the same wrong way pays toward the whole of its stake, since strangers drawn apart and sworn to silence should not fail in unison. The ballot reads guilty, not guilty, or unresolvable, the last returning the funds, because the common hard case is ambiguity, not deceit. No reward rule catches a mistake every steward makes honestly; against evidence built to deceive the whole panel stands only the bound on what may rest on a single verdict while the network is young. A verdict stays open to review, and a later quorum can overturn it at the erring seats' expense. The sealed tally and the nameless claims belong to the companion article.

## 8. The deadline

A court that can hang is a hostage taker: if a verdict could be withheld forever, the power to withhold would be worth money, and a party facing loss would pay for delay instead of judgment. Every dispute therefore ends, on a clock no participant can hurry, through one of four exits: the parties' late agreement, a verdict, a tie read as unresolvable, or a default that needs no signer.

The deadline passes only when a public clock and a delay function have both run their course. The delay cannot be hurried by adding machines, only by outrunning the fastest one anyone holds, so the deadline cannot meaningfully be brought forward. It can be pushed back only by slowing the public clock, which delays every path equally, including the attacker's own exit.

The draw seats more stewards than the quorate threshold, so absences are absorbed. If a panel fails, it refills once along the order the seed fixed, under the same frozen eligibility, so it cannot be shopped for a better one. If the second also fails, the funds move anyway: at setup the parties pre-sign a ladder of long-stop outcomes that spend the funds after a generous delay with no signer, ordered by what the record objectively committed, so the last rung, a symmetric refund, becomes valid only where the record commits nothing. Funds can wait; they cannot be imprisoned.

## 9. Sovereignty

The protocol rules on the trade, not on the person. It decides who owes what under an agreement two parties entered freely, not whether the trade was wise or legal. No authority sits in the protocol or above it, and rules hold only over what participants have agreed to.

Karma belongs to the account, and an account can be sold as a business is sold. The protocol cannot verify who holds a key; that a key's holder is unknowable is what keeps identity sovereign. But standing does not pass silently with a key: a change of hands, a transfer or a sharp break in conduct alike, resets the account's tenure to zero and collapses what it can express, though the karma it paid for and its history carry over. So a bought reputation buys the history, never the seniority, and must earn its ceiling again under the public clock.

A key can be lost or stolen. An account may retire its key by signing a successor after a public delay, and may register a hidden recovery key published only as a commitment; the older commitment displaces a compromised key and wins any contest, so a thief cannot outrun a commitment made before the theft, and such a recovery does not reset tenure. An account that loses every key is gone, because anyone who could restore it would be an authority the protocol refuses to hold. What remains is a fresh start at zero, real and with its cost.

## 10. Economics

Both traders post their deposits and the dispute fee into the escrow when the trade is set, so opening a dispute costs no new money and a poor honest party is never priced out of defending itself. Karma opens doors and never carries the money: standing decides who may steward, not the size of a dealing, which the bond alone bounds. The capital that makes fraud unprofitable is the fresh deposit posted for this trade, lost on it if the account defects. Good conduct prices the deposit down to a floor, never to where defection turns profitable, so a bought reputation buys only the discount: the stake that must be lost is posted fresh by whoever holds the key today.

A deposit prices one dealing; nothing yet bounds how many a key holds open at once, so a patient fraud could open many and vanish owing on all. The protocol therefore caps a key's total open exposure. Every opening states the value its counterparty could lose if the key defaults, and the sum across a key's open dealings may not exceed a bond it holds locked for the purpose, so the bond bounds the whole of what its counterparties could lose at once. The bond is reclaimable only after a timeout that outlasts every dealing it backs, is the same for every key, and karma never lifts it, because anyone who plans to disappear has already written off his standing, and only capital a verdict can seize changes the arithmetic of an exit. The cap enforces itself: a counterparty's client sums the other key's open exposure and refuses to sign an opening that would breach it.

The protocol takes nothing: every fee flows to the people who did the work of judging, and there is no issuer to pay, because there is none. The absence of an earning model is a requirement, not a preference: anyone who could profit from the court could sell it, and a court that can be sold is a court that will be. Neutrality is the product; an owner would be the flaw.

## 11. Sybil resistance

The security of the protocol is the cost of faking karma, cheap neither to the patient nor to the rich. Creating an account costs an irreversible sacrifice, uniform for everyone, so a thousand accounts cost a thousand times one. Karma itself is minted only by burning value against a settled dealing, and standing decays unless renewed by fresh burns with distinct counterparties, so there is no inflow to capture and no loop to farm.

The mint cannot be farmed, so an attacker's only path is to hold standing he never earns back through honest trade, and one inequality prices it. A threshold key held purely to exploit the protocol costs an irreversible burn and a forced wait under the tenure ceiling to build, and every period after costs the decay it must replace out of fresh burns, which service cannot repay, because service cannot remint the decay that keeps a key eligible. Against that stands the most such a key can earn inside the protocol in a period: a steward margin capped at or below an automated reader's cost, plus the interest saved on its own locked deposits. The decay constant is chosen so that, for any ring size and any budget, holding the threshold costs more each period than the threshold can return each period inside the protocol.

One problem stays open. Telling distinct persons apart without an identity document is unsolved at scale, and the defense against an attacker who can cheaply create real-seeming humans is only as strong as the best answer to that problem. The protocol raises the cost of an attack; it does not claim to make one impossible.

## 12. Where it runs

The protocol lives in two places. Value lives on a settlement rail: escrows, deposits, bonds, burns, and account sacrifices are outputs on the rail, their spending paths signed before they are needed. Everything else lives on the record: an append-only log of signed events, held in full by many independent relays that anyone may read and copy. A public clock binds the two: events are gathered into batches, each reduced to one commitment placed on the rail under a clock mark, so the order the rail carries becomes an order over the record. One object crosses back to the rail, the verdict signature, on a spending path the traders signed in advance. Money never appears on the record, and nothing on the record moves money except that one signature.

No machine is trusted for correctness. A relay stores the log and serves it; relays are assumed hostile, and the answer is redundancy, since the same event rests on many. A client verifies the log by replay, or checks one account's standing from only the events that name it. A summary publisher posts a bond and publishes signed totals, so a client reads an aggregate without gathering it; any client that proves a discrepancy from the log takes the bond, so a false total is corrected by arithmetic, not by a judge.

Relays are caches, not gatekeepers: any machine may carry any event, and an actor whom every relay refuses can anchor his own commitment on the rail, so censorship degrades to delay. The full architecture, what the record keeps and forgets and who pays to carry it, belongs to the companion article.

## 13. Limits and the social fork

The protocol rests on reasoning about how people act, not on evidence that it works: it cannot be proven in advance, and a correlation in early data would not prove it either. Four limits survive every part of the design, and are named rather than buried. A signing key can be bribed, and no sealed ballot stops its owner from selling the vote; what the sale cannot deliver is a score, since a bought vote fails the batch's bar and forfeits its bond. Stewards who find a channel outside the protocol can coordinate, and the reward for honest reporting weakens when they do; against this stands only that they know nothing of each other. Telling distinct persons apart without an identity document is unsolved. And the final defense against an attacker who has bought the whole graph is that the graph is expensive to buy, not that it cannot be.

One defense stands behind that last limit. Karma is a computation over a public log, not an instrument an attacker can own. If a set of accounts is shown to be a fabrication ring, clients can adopt a new version of the rules that discounts those accounts and denies them standing, recomputed by everyone from the same log. Nothing is confiscated and nothing is voted on; within any version everyone still derives one number, and what forks is only the choice of version. The attacker keeps his entries and loses his audience, so the prize for capturing the graph is a graph whose readers have left.

## 14. Conclusion

Trade between strangers has rested on someone trusted to attest and someone trusted to judge, and each such someone has been a point of failure. This protocol earns the attestation from a costly burn tied to real conduct, draws the judgment from a crowd no one can find, holds the funds with the traders alone, and keeps no power for itself. The pieces are known; what is new is their assembly into a whole no one owns and no one can capture. The protocol does not claim to be unstoppable. It claims to make honest conduct the paying strategy, and to remove every party a bribe, a subpoena, or a switch could reach. The result belongs to the public domain, to use, to build on, and to improve, without permission and without an owner, because a thing meant for everyone must be owned by no one.

## References

A companion long-form article develops, with interactive simulations, the deep construction this paper only states: the endogenous entropy and delay function of the draw, the sealed tally and nameless claims of the verdict, the full record architecture, and the anti-farming arithmetic of karma.

1. J. R. Douceur. The Sybil Attack. 2002.
2. E. Friedman, P. Resnick. The Social Cost of Cheap Pseudonyms. 2001.
3. S. Micali, M. Rabin, S. Vadhan. Verifiable Random Functions. 1999.
4. D. Boneh, J. Bonneau, B. Bunz, B. Fisch. Verifiable Delay Functions. 2018.
5. D. Prelec, H. S. Seung, J. McCoy. A Solution to the Single-Question Crowd Wisdom Problem. Nature, 2017.
6. V. Shnayder, A. Agarwal, R. Frongillo, D. C. Parkes. Informed Truthfulness in Multi-Task Peer Prediction. 2016.
7. C. Komlo, I. Goldberg. FROST: Flexible Round-Optimized Schnorr Threshold Signatures. 2020.
8. T. Dryja. Discreet Log Contracts. 2017.
9. L. von Mises. Human Action. 1949.
10. E. Hughes. A Cypherpunk's Manifesto. 1993.

---

*Released into the public domain under the Unlicense. No rights reserved. No owner.*