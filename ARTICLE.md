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

Holding many keys buys less than it seems. Each starts from nothing and must build its own standing from its own dealings, so a crowd of keys is a crowd of separate lives to live, not a shortcut to a larger one. Most people will want a few: a public key, a private one, perhaps a working key for business and a quiet one for what they would rather not tie to their name, and past those the use of another falls away fast. A double life is allowed and, as in the flesh, costly to keep, which is the honest arrangement rather than a fault to correct. One thing falls out of it for nothing: since a real history is dear to build, keys spun up to fake or to flood stand out against a graph of genuine human dealing, and any app can strain them out without the protocol banning a soul.

A fresh key is worth nothing. It holds no standing, exactly like a bitcoin address that has never been used: it exists, but there is nothing to see and no reason for anyone to look. A key is meant to be kept and used. Throw one away after each dealing and you build nothing a counterparty can weigh; keep one and it gathers a history, and the history is the only thing that makes a key worth reading. Two empty keys cannot even be told apart, so a browser that reads the record lists only keys that have done something. Until a key deals, it is invisible.

Every key's history sits on one public record that only grows. A dealing closed, a dispute lost, a mark of standing gained: each is written once and never unwritten. Nothing is edited, nothing is deleted, nothing is hidden. The record is the ground the protocol stands on, and making it tamper-proof without a company to guarantee it is the hardest problem Nown has. Its answer is the timechain.

## 3. Karma density

Karma[^karma] is the standing a reader computes from a key's record. No balance of karma sits anywhere, on the key or in the network, waiting to be spent. There is only the record of what a key did, and a figure each reader derives from it under rules everyone shares, so two readers running the same rules reach the same number. Karma is not held. It is read, recomputed from the record by whoever cares to look.

Seniority by itself counts for nothing. A key ten years old that has done little is worth less than a key a month old that has dealt well and often, because trust follows conduct, not age. The years are not thrown away, though. They are the span the density is measured across. A dull fifty-year-old and a sharp twenty-year-old have both lived every one of their years; what parts them is what they did with them. Karma reads a key the same way, weighing not how long it has existed but how much good dealing it packed into the time it has.

So karma is a density. Each event is a signed weight, positive for a success, negative for a failure, scaled by the stake behind it. Karma is the sum of those weights over a trailing window, with older events fading as the window moves on. Leave a key idle and its karma thins toward zero, with no bad mark against it, because the window keeps moving while the conduct does not.

Two things follow, and they are the whole point of measuring density instead of a total. Climbing is quick: deal well and often and fresh weight piles up faster than the old weight fades. Holding is slow: to keep a high figure you must keep dealing, replacing what the window drops, the way a business keeps its position only by continuing to serve. A key that has held a high density across many years has shown the one thing money cannot buy in a hurry, which is that it lasts.

The figure a reader wants has a plain shape. Take the whole span a key has been alive, from its first mark on the record to now, and average its karma across that span. That average is **Karma DOT**,[^dot] delta over time: the area under a key's karma curve, divided by the time it has been alive.

FIGURE karma-dot :: Karma DOT is the average height of a key's karma over its whole life. Two keys can reach the same karma today and still be worth very different amounts. The steady dealer built its standing early and held it, so its average runs high. The late starter sat idle for years, and that dead span averages in and drags its figure down, no matter how well it deals now.

Read this way, two keys with the very same karma today can be worth quite different amounts. A key that built its standing early and held it has a curve that runs high across its whole life, so its average is high. A key that sat idle for years and only lately began has that dead stretch flat on the floor of its average, and no burst of recent dealing lifts it back.

Idle time does not merely fail to help; it bleeds. Because the average divides the area under the curve by the whole time a key has been alive, every block a key sits idle is a block of nothing added to the denominator, so its DOT falls the longer it waits. There is no banking a key. Generating one early and holding it in reserve buys no seniority and, the moment it is on the record, quietly costs DOT for every idle block, which is the exact reverse of what a reputation should do. The only road to a high DOT is to keep dealing well across the time you have, and the clock that time is counted on is the timechain.

## 4. How karma flows

Karma is minted by dealing, never handed out at birth. A fresh key holds nothing, and it stays at nothing until it deals. It carries no seniority to trade on and no standing to spend, so a thousand fresh keys are a thousand separate climbs from zero, which is exactly why minting keys by the thousand buys a faker nothing.

Karma comes into being when two keys deal and the dealing succeeds. To deal, a key stakes a measure of its own standing on the outcome, and a good outcome mints new standing for both, bounded by the standing staked. What the mint reads is standing, never the worth of the trade, because the worth of a trade cannot be read: the same exchange is precious to one man and trifling to another, and no number the protocol could see would rank one dealing above another. So Nown mints in the one currency it can measure, standing itself, and a dealing between two proven keys lifts both, while a dealing between a proven key and an unknown lifts the unknown more, because the proven key put more of itself at risk. The network's karma grows with the honest dealing done in it, never locked to whoever arrived first. What no key can do is mint standing alone: two keys with nothing, dealing only with each other, stake nothing and mint almost nothing. How the very first standing enters a network where everyone begins at zero, when the worth of a dealing cannot be measured to seed it, is the hardest of the open problems.

A key that deals with you puts its standing behind the outcome. A proven key dealing with you says more than an unknown, because the proven key had more to lose, and a good dealing between two strong keys lifts both, while a good dealing between a strong key and a weak one lifts the weak one more.

Failure runs the other way. The key that broke the dealing takes a mark that never leaves its record. The key that vouched by dealing loses the standing it staked, because it trusted someone who failed. That second loss is the discipline of the whole system. A high-standing key that deals carelessly bleeds its standing into the failures it backed, so it learns to deal only where it believes the other side will perform. Its willingness to deal with you is worth something precisely because it is not given away.

This is why an assertion moves nothing. A key that merely says another is trustworthy has staked nothing and risked nothing, and standing a key can hand out for free is standing a ring can hand itself. Karma is earned only when a real dealing, with something at stake, comes out right.

## 5. What counts as true

A dealing is any exchange two keys put something behind: a trade, a job, a contract, a document to certify, a course taught. Whether it went well, whether a party dealt fairly or lied, is not something Nown can see from the outside, and it does not try to. Nown makes no claim about the truth of the world. It produces a verdict, through the oracle a context chose, and that verdict is the only truth it records.

This is a narrower thing than justice, and stronger for being narrow. The parties may play a deal however they like, with charm or cunning or hard bargaining or any means each thinks will serve him. Nown passes no judgment on how a man plays, because his reasons are his own and appointing someone to weigh them is not a thing worth building. A deal one side rigged can still come out true in the eyes of the counterparty who accepted it, or of a quorum that read the evidence and ruled, and if it does, then for Nown it is true, because the oracle said so and no higher court sits above it.

What Nown does instead is make losing cost you. A lost dealing writes a mark that never leaves your record, moves the money you staked to the other side, and burns the standing anyone put behind you. The game is worth playing straight not because Nown forbids the alternative but because the verdict is real and the loss is permanent. Make losing expensive enough, and honest dealing becomes the paying move on its own, with no one set over the players to judge their hearts.

## 6. The oracle

The oracle[^oracle] that renders the verdict is one of three kinds, and which one serves is the context's to choose.

The parties can attest. Both sign that the dealing closed as agreed, and silence once the agreed time has run out reads as success. Most dealings end here, cheaply, with no one else ever looking. An honest trade that goes right needs no judge.

A quorum[^quorum] can judge. This is the answer when one party disputes the outcome, or when a context needs a fact certified that the parties cannot settle between themselves.

Karma can be its own oracle. A context reads standing directly and lets the outcome follow. An employer sets the karma a role demands, and the keys that clear the bar are the ones he considers. A gate opens when a key passes a threshold. No panel is called; the reading settles the matter, and the dealing resolves the instant it is done.

A context could also borrow an oracle it already trusts, but not on the main network. It might lean on an outside authority, a court, a registry, an exchange, and have Nown record what that authority ruled. The convenience is real, and so is the cost: a corruptible party in the loop dilutes the trust the main record exists to keep clean. So a use that needs a trusted or changeable oracle does not run on the main net. It runs as a fork, a separate Nown with its own rules and its own web of trust, worth spinning up when enough people need it. The main record admits only oracles no one owns: the parties, a drawn quorum, or a reading of karma. That a fork can wrap an old bureaucracy and give its rulings a portable, permanent home is how Nown reaches a world that has not adopted it, without letting that world's weaknesses back into the core.

## 7. The quorum

When a dispute needs a stranger to settle it, Nown draws a panel and asks it a plain question. The design is simple on purpose, and every part of it exists to keep the panel honest without an authority standing over it.

The panel is drawn at random from keys of high standing, several steps removed on the record from both parties, so no one who has dealt with either can sit. It is drawn for the one case and dissolves when the case ends. Its members are pseudonymous to the parties, to each other, and to anyone relaying the traffic. No one can find the panel to bribe it, and no one can pack it, because no one chooses it.

Each steward[^steward] reads the same evidence and answers one question in private: which party does the evidence favor. The answer that carries is the one most of them give. That is the whole rule. The quorum does not find the truth and does not pretend to. It is a guessing game whose focal point is the evidence: each steward is really answering what he believes most other honest readers of the same evidence will conclude, and on clear evidence that is simply what the evidence shows. Strangers drawn apart, who cannot coordinate, converge on the reading the evidence best supports, because that is the only answer each can expect the others to reach.

The votes are secret, and only the count is ever published. No one can show afterward how a given steward voted. A vote that could be proven is a vote that can be bought or punished, so the protocol makes each ballot unprovable and leaves a briber with nothing to verify and a thug with no one to blame. What the panel reveals is a number, never a name.

A steward earns for answering with the majority, enough to cover the cost of reading the evidence with care. The reward asks no knowledge of the truth, only the public count: match the crowd and you are paid. There is no cleverer scoring than that, and none is wanted.

What stops a briber is not a detector but a price. To swing a verdict he must reach a majority of a panel he cannot find, drawn at random from a large pool, and the larger the network the larger and more scattered the panel he would have to buy. Collusion is not caught after the fact; it is priced out of reach, and the price rises as the network grows.

The case cannot hang forever, because a ruling that could be stalled would be worth money to stall. A deadline runs from the moment the case opens. If too few stewards answer in time, the panel does not fail, it grows, drawing more stewards, which both replaces the silent and makes the panel harder still to have captured. How large it may grow scales with the network, so a bigger Nown fields bigger, harder-to-buy panels; only if a much-enlarged panel still cannot reach a count do the stakes return to the parties along terms they signed before the dealing began. When the panel does rule, the ruling is written like any other outcome: the money the two of them set aside moves to the party upheld, and a karma event is written for each, a success for the one and a failure for the other, flowing standing exactly as a settled dealing does.

No appeal follows, and no later panel reopens the record. Finality is the value. A judgment that could be revisited is a judgment no one can rely on, and the point of the quorum is to end the matter.

## 8. The record and the clock

Karma is a density over time, so the record needs two things it cannot fake: an order that cannot be rewritten, and a clock that reads the same for everyone. A company could provide both and would then own both. Nown cannot use a company, so it borrows from the one system that already solved this without an owner.

The timechain,[^timechain] bitcoin's public ledger of blocks, is a record no one can rewrite: each block builds on the last, ordered by proof of work, and undoing one means redoing all the work since. It is also a clock. Every block is a tick, the same tick for everyone who reads the chain, owned by no one and stoppable by no one. Its ticks are coarse, roughly one every ten minutes, and that is fine, because karma density does not need the second, it needs a shared and permanent measure of when. Pin a key's first block and read the latest, and the span between them, counted in blocks, is the denominator that turns a tally into a density. Finer time is a matter of presentation, not protocol: readers already localize block times to the second from their own settings, the way a timechain browser shows a human date beside a block height. The protocol commits to blocks. A client may dress them up however it likes.

The borrowing has a cost. Proof of work is often called wasteful, which misses the point. It is impractical: a network of miners guards a record only because they are paid in the coin their work secures, and that coin is the incentive that keeps the record honest. Nown has no coin of its own and wants none, so it cannot run its own proof of work. That leaves two ways out. It can anchor its record to a proof-of-work chain strong enough to borrow, and only bitcoin's is, which ties Nown's permanence to bitcoin's. Or it can find an incentive that keeps a record honest with no coin at all.

The second path is open research, and the shape of the answer is already visible in an older idea. When Phil Zimmermann built PGP,[^pgp] he did not promise perfect privacy, and he did not build a central authority to grant it. He let every user be his own authority, choosing whom to trust and computing, from signatures he had collected, whether a key was good enough to rely on. Zimmermann called the result a "decentralized fault-tolerant web of confidence."[^web] It was never perfect, and it never had to be. It was pretty good, and pretty good was usable where perfect was unavailable.

Human action runs on the same currency. A man does not need perfect trust to deal with a stranger; he needs pretty good trust, enough to act on, priced for the risk he is taking. Call it PGT, by the plain descent from Zimmermann's phrase. Fiat money needs trust in an issuer and bitcoin abolished that need, but trust between people was never going to be abolished, only made portable, computable, and owned by the person who earned it. A record kept honest by the incentives of the people who read and write it, rather than by an outside coin, is the standalone answer if one exists. Nown does not claim to have built it. It claims that the problem is the right one, that the timechain solves it today by borrowing, and that PGT is the shape a native solution would take.

PGP is a precedent, not a template. PGP signs that a key belongs to a person, a narrow and near-binary fact. Nown signs conduct across dealings, which is graded and never finished. What Nown takes from PGP is the shape, decentralized, reader-computed, honestly imperfect. Signing a key and scoring a life are not the same act, and Nown does not pretend they are.

## 9. Where the record lives

The timechain keeps the record honest, but it does not hold it. A key's whole history, every dealing, every ruling, every seal, is far more than a chain small enough for anyone to keep could ever carry. So the record itself lives elsewhere, on a network of machines, and the timechain's only part is to keep them honest: at intervals the network commits a fingerprint of the whole record to a block, and any copy can be checked against that fingerprint, so a machine that quietly altered the past would fail a check anyone can run.

The hard part is not correctness but persistence. A record no one is paid to keep is a record that rots, as every attempt at storage without a reward has found: people store what they are using and drop what they are not, and the past slips away. Proof of work solved this for money by paying its miners in a coin, but Nown has no coin and cannot move money without becoming the thing it is not. So it pays in the only currency it mints, standing, and it splits the work of holding the record in two.

The first layer is the swarm. Every client that reads Nown also keeps a shard of it, a small slice of the whole, held as the price of taking part, the way a reader of a shared library lends a shelf of it back. No one is paid for this and no one needs to be, because the cost to each is slight and the slices overlap many thousands deep, so the record is spread across every device that touches it and no ordinary loss can dent it. The swarm gives breadth and redundancy for free, but it guarantees nothing: a shard is kept only as long as its holder stays.

The second layer is the paid node, and here standing does the paying. A node that pledges to hold the whole record and serve it can be made to prove, at any moment, that it still has every part, by answering a challenge that only a machine holding the data could answer against the timechain's fingerprint. A node that proves itself, reliably and over time, earns standing for it, exactly as any dealing well kept earns standing, and a node that goes dark or fails a challenge loses what it staked to take the pledge. Standing is worth holding, so there is a real wage for keeping the record alive, paid in reputation rather than money, and a node's own karma comes to reflect how faithfully it has served.

Between the two, the record is both wide and deep: spread thin across every user's device so it cannot be wiped, and held whole by proven nodes that answer for its keeping and are paid, in standing, to do so. What the exact challenge is, how often it runs, how much standing faithful service earns, and how the two layers hand off between them, is a construction to be worked out, and it is among the open problems.

## 10. A key is property

A key is owned by whoever holds its private half, and it can be kept, lent, or sold like anything else a man owns, because holding the private half is holding everything the key carries, its history and its standing alike.

This makes standing portable in a second sense. A reputation built under one key can pass to a buyer, so a business that has dealt well for years can be sold with the key that carries its name, and the buyer steps into a going concern instead of starting from nothing. A key is worth what someone will pay for it, and a market in keys prices reputations the way a market in businesses prices goodwill. Nown carries monetary value for this reason, with no coin of its own: the value rides on the keys.

No sale can be forced onto the record, and none can be stopped off it. A change of hands is written only if someone chooses to write it, and there is no way to make a man announce that he sold a key or bought one. So the network may never learn a key changed owner. It learns soon enough from conduct. A buyer who keeps dealing well keeps the standing he paid for, and the density he inherited carries him only as far as his own dealings sustain it, since the window fades an inherited history like any other. A buyer who cashes the standing out in one last scam spends it, and the record keeps the exit for the next reader to see. Both the patient buyer and the fast one already exist wherever businesses change hands, and Nown records both without preventing either.

## 11. Proving without showing

A man's whole dealing history is his own business, and a counterparty usually needs one fact from it, not the ledger behind it. Nown lets a key prove the fact and reveal nothing more.

A key can prove that its karma, under a stated set of rules, clears a bar, without opening the events the figure was computed from. It can prove that a success it claims was with a counterparty above some standing, without naming the counterparty. It can prove that an oracle ruled as it says. In each case the reader checks a short proof and learns the one fact the context asked for. A man can walk up to a market that demands a karma of a thousand and prove he has it, while the market learns neither whom he dealt with nor how far past the bar he sits.

The simplest proof of all is a signature. A key that signs a fresh message proves, to anyone, that its holder is present and in control, right now. Attach that signature to a public karma profile and it becomes a claim the reader can check himself: this living person holds this key, and this key holds this record. That is the seed of the uses that follow.

## 12. One record, many readings

No one issues a key's karma. Each reader computes it, running the shared rules over the shared record, so two readers who run the same rules reach the same figure. Standing is settled by a computation anyone can repeat, not by an authority anyone must trust.

This is what lets a thousand applications sit on one Nown. A Nown browser is a client. It reads the one record, under the one protocol, and shows a user whatever slice of it he asks for. One browser weights recent dealing and forgets fast; another rewards long, steady histories; a hiring app reads only the dealings that bear on work; a lender reads only the record of debts paid. These are not different Nowns. They are different views of the same record, extracted on the reader's own machine, and none can lie about what a key did, because the record beneath them is one and the same. The protocol holds the record and the rules of the flow; everything above is a filter someone wrote for a use of his own.

A genuinely separate Nown is a rarer thing: a fork, a new network with its own rules, for a use the main one will not serve, such as one that admits a trusted outside oracle. A fork is its own web of trust, worth starting only when enough people need what it offers. The common case is not many Nowns but one Nown read a thousand ways.

## 13. What it is for

Karma is the product, and its uses run as wide as trust has prices. Four show the range.

**A dispute, settled.** Two strangers escrow a trade in an output only the two of them control, and deal. If it goes right they attest and the escrow releases. If it goes wrong they open a dispute, the quorum rules, and the ruling moves the escrowed money and marks each key. This is the use where the teeth show clearest, because real money hangs on the answer.

**A worker, hired.** An application that runs Nown lets an employer describe the karma a role demands: this much standing, in dealings of this kind, held this steadily. It finds the keys that match and, where a key has published a way to reach its holder, reaches out; or it lets those keys raise a hand. A candidate proves he clears the bar by signing a fresh message with his private key, and that signature, beside his public profile, is proof of eligibility the employer can check without a resume, a reference, or a school. The signature and the key together are the oracle the hiring context resolves on: any holder who signs and clears the bar is a valid answer, and the employer picks among them.

**A degree, replaced.** A man wants to prove he knows a field. Instead of paying a university for a certificate, he studies under a master of the field, a working expert who takes students. The teaching is a dealing: the master is paid, and at the end he fixes a seal[^seal] to the student's key, a signed mark that says this man learned the craft under me. The master stakes his own standing to seal it, because a seal on a student who cannot do the work costs the master the standing he vouched with, exactly as a failed dealing costs any voucher. Years later the student applies for a post, and the employer reads on the key that a prominent name in the field put his own reputation behind this man, at his own risk. The master vouched by teaching and sealing, which is a real dealing with a real stake, not a free endorsement. A credential becomes a chain of people who staked their names, readable end to end.

**A certificate, notarized without a notary.** Two people marry and want it on a record that outlives any registry. A translator swears his translation is faithful and wants that on record too. A context sets a quorum, or a single trusted checker, to certify the fact, and the certification is written like any other outcome. No state office holds the paper, no notary holds the stamp. The record holds the fact, the standing of whoever certified it stands behind it, and anyone can read both. Trust reaches a plain human need, with no money changing hands and no authority in the middle.

In every case the shape is the same. Someone defines a context and its oracle for a use of trust. Other keys step in under their own keys. The outcome, however it is decided, writes a karma event that flows standing by the one rule that governs all of them. The protocol supplies the trust. People supply the uses.

## 14. The killer app: reading people by their record

A permanent, portable, unfakeable record of how a person has dealt sits under a whole class of problems that share one shape: a stranger must be trusted, misjudging him is costly, and the only party who can vouch for him today is a corruptible silo that owns his reputation and can be gamed or bought. Wherever that shape appears, a karma browser, a client that reads the one record and filters people by the conduct that matters, is pretty good trust made concrete.

The shape recurs everywhere. An employer reads a resume the applicant wrote and calls references the applicant chose, a signal so self-refereed that one federal case uncovered thousands of fabricated nursing diplomas, a third of whose buyers passed the national licensing exam regardless. A buyer reads star ratings the platform owns and the seller can buy, and fake reviews are reckoned to sway on the order of a hundred and fifty billion dollars of spending a year. A lender must price a stranger's promise to repay while the bureau that scores him is central, gameable by invented identities, and simply blank for tens of millions it holds no file on. A person online can no longer tell an accountable human from one of the machines that now make up half of internet traffic, or from the day-old identity behind a romance scam that took billions last year. Each is a stranger to be trusted, at real cost, vouched for only by a silo.

A karma browser answers them the same way. It issues no badge and grants no credential. It lets whoever must decide read, for himself, an unerasable history of how a key has dealt, filtered to what he cares about: contracts honored, for a hire; debts paid, for a loan; years of real dealing, for a stranger who claims to be real. The applicant cannot curate it, the seller cannot wipe it by opening a new account, the impostor cannot fake the years his fresh key does not have. And because the reading happens on the reader's own machine against a record no platform owns, the reputation is portable across every app at once and captive to none, which is the second thing the silos get wrong.

The honesty is in the edges. A record of past conduct says nothing about a first dealing, so an honest newcomer starts indistinguishable from a fresh fake, and that cold start recurs in every one of these uses. Cost and permanence raise the price of faking a history without making it impossible. The record is blind to harm nobody reports, and to the man who was trustworthy until the moment he was not. And a permanent public ledger of a person's dealings is itself a thing to handle with care, which is why he keeps more than one key and shows only the standing a dealing needs. Karma reads the recurring, high-stakes deal between strangers whose conduct accrues. Where the deal is one-shot, or the fact is private, or what is wanted is whether a claim is true rather than whether a person is reliable, it says so and stays out.

## 15. Clustering is not cheating

A worry raised against every reputation system is the closed ring: a group that deals only with itself and votes each other up. In Nown it is not a hole to plug, because it is not an attack. People and firms deal inside their own circles all the time. A company is a cluster by definition, its people dealing with each other far more than with the world; a family, a guild, a town are the same. Banding together to get more done is not a flaw in civilization, it is civilization, and a reputation system that fought clustering would be fighting the thing reputation is for.

What a circle cannot do is conjure standing from nothing. Karma flows from the standing put at risk, and a group starting near zero has little to flow to itself; dealing in a ring moves small amounts around a small pool without enlarging it. Standing grows when the circle deals well with the world outside, and the world stakes its own standing to deal back. So Nown lets the circle form, lets it deal inside itself freely, and simply reflects what it is: a tight group with a deep internal history and, until it earns more, little standing past its own edge. A reader sees that for what it is and weighs it as he likes.

A cluster can also become a thing in its own right: a company that holds a key of its own and deals under it as a person would.

## 16. Seals and ownership

A key carries two kinds of thing. The first is its history, the record of what it did. The second is its seals, the marks others have fixed to it to certify a fact about its holder. History is earned by dealing; a seal is granted by someone who stakes his own standing on the granting. The two are read together, and they are read differently: a history is a pattern a reader weighs for himself, a seal is a single claim by a named certifier who answers for it.

A seal is made the way any outcome is made, through an oracle. A teacher who has taught a student signs a seal for the skill the student showed; a body that certifies a trade signs a seal for the certification; a fact two parties cannot settle alone is put to a quorum, and the quorum's ruling is fixed to the key as a seal. Whoever seals stakes standing on it, so a false seal costs the sealer exactly as a failed dealing costs a voucher, and a seal is therefore worth what its sealer's standing is worth. Some seals are permanent, a schooling completed, a degree conferred. Others carry a term and lapse when it ends, a membership for a year, a ticket for a season. The record keeps a lapsed seal as it keeps everything, but a reader sees that its term has run.

Seals are not free to grant. Whoever seals stakes standing on it, which is the natural check on the granting: a body that hands out a thousand seals has staked its name on all thousand, and pays for every one that proves false. So the granting side needs no rate limit, and it should not have one, since a school graduates a class at once and a club admits its members together.

The trouble is on the receiving side. A key that collects seals without limit dilutes them all, until the record of what others have certified about it is noise a reader learns to skip. A seal is meant to be read and acted on, and a key wearing a hundred says less than a key wearing three. So the cap belongs to the key that receives, not the one that grants: a key can carry only so many live seals before new ones crowd out old, and the holder must choose which to keep shown. Setting that cap so it curbs dilution without turning away a person who has honestly earned many marks is not solved, and it is one of the open problems.

Ownership is written as a seal, and this is where seals do their heaviest work. A company is not a person and earns no history of its own, but it can carry a key. Someone inside the firm with the authority to bind it signs a key into being and ties the firm to it; from then on that key is the firm's reputation, and its dealings build a history exactly as a person's do. Who owns the firm is written on the key as a seal: the firm draws up a binding document of ownership, a quorum ratifies it, and the ratified fact rides with the key. To transfer the business is to hand over the key and re-seal its ownership to the buyer, ratified again, so that the chain of owners is readable end to end and proving who owns a company is as plain as reading the last seal on its key.

This turns a problem that has always needed registries and courts into a matter of reading a record. A share is the same idea divided: a cap table becomes a set of ownership seals on a key, and a sale of shares becomes a re-sealing. A dispute over who owns what goes where every dispute goes, to a quorum, and its ruling is written like any other. The exact way a firm binds to a key, how fractional ownership is sealed, and how an ownership dispute is drawn and ruled, is a construction still to be worked out, and one of the more promising doors Nown opens.

## 17. Open problems

Nown rests on reasoning about how people act, not on a record of it running. Some parts are settled in shape but not in detail, and naming them plainly is the honest course.

**Measuring a dealing.** This is the deepest of them. To mint karma in proportion to a dealing, the protocol would need to know how much the dealing was worth, and worth cannot be measured. The same exchange is precious to one man and trifling to another; even a price in money is only what these two agreed, not a common yardstick that ranks their dealing against anyone else's. So there is no honest way to say one dealing earned more than another by its value. Nown works around this by minting in standing rather than worth, since standing is the one quantity it can read, but that leaves the genesis unsolved: the mint bounds a gain by the standing staked, and at the start no one has any standing to stake. How the first standing enters a network where everyone begins at zero, without a measure of worth to seed it and without opening a door a faker walks through, is the hardest problem Nown has.

**The mint's rates.** Even granting a measure, the amount minted per dealing cannot be the client's to set, or anyone could print karma. It is fixed in the protocol, one rate per kind of dealing, and held in percentages rather than raw numbers. What those percentages should be, and how they keep the supply growing with real dealing without cheapening what everyone before has earned, is design work still to be done.

**Paying the nodes.** The record is held by a swarm of user devices and a layer of proven nodes paid in standing, and the exact terms of that wage, the challenge that proves a node still holds the record, how often it runs, how much faithful service earns, and how the two layers hand off, are unsettled. That reputation alone can pay for a network of nodes is the bet the design rests on, and it is load-bearing.

**Seal dilution.** A key that collects seals without limit dilutes them all. The granting side needs no cap, since a sealer stakes standing on every mark and a school may graduate a class at once, but the receiving side does, or the record of what a key was certified to be becomes noise. Setting a cap on the receiving end that curbs dilution without turning away a person who has honestly earned many marks is unsolved.

**The default metrics.** Karma DOT is computed under constants: how fast idle standing fades, how a success is weighed, how the mean is taken. The base protocol fixes a default set so every reader reaches the same figure, with apps free to layer their own on top. This is design work, not a guard against anyone; a key that deals more, and so climbs faster, has earned it.

**Sizing the quorum.** Collusion is priced out by the size and randomness of the panel, and a stalled case is answered by a larger one. The function that ties a network's size to its quorum's size and growth is a parameter still to be derived.

**Sealing a company.** How a firm binds to a key, how fractional ownership is sealed and re-sealed on a sale, and how an ownership dispute is drawn and ruled, is a construction still to be worked out.

## 18. The end of the keeper

Trade between strangers has always rested on someone trusted to vouch and someone trusted to judge, and each of them has been a place to capture the whole. Nown takes the vouching from the standing that keys stake on each other when they deal, draws the judging from a crowd no one can find, holds the money with the two parties alone, and keeps no power for itself. A man's standing becomes his own, built by his conduct, carried under his key, read by anyone, held by no one who can take it back. It does not make people good and does not catch every liar, because nothing can. Nothing should. It puts conduct on one honest record, so a stranger can be judged by what he has done rather than by whose permission he carries, and it leaves the uses of that record to the people who need them. The result belongs to everyone, because a thing meant for everyone must be owned by no one.

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
12. U.S. Department of Justice. Operation Nightingale: fraudulent nursing diploma scheme (7,600 diplomas/transcripts). USAO Southern District of Florida, 2023.
13. World Economic Forum. Fake online reviews are a $152 billion problem. 2021.
14. Imperva. 2024 Bad Bot Report (bots 49.6% of internet traffic in 2023). 2024.
15. Consumer Financial Protection Bureau. Data Point: Credit Invisibles (26M credit-invisible, ~45M unscorable). 2015.
16. Federal Bureau of Investigation, IC3. 2024 Internet Crime Report ($16.6B losses; $5.8B crypto relationship-investment fraud). 2025.

[^key]: A keypair: two matched numbers. The private one is a secret only its holder knows, used to sign; the public one is shared and lets anyone check those signatures. Holding the private key is owning everything the key carries, its history and its standing.
[^karma]: A person's standing, computed by anyone from the public record of how his key has dealt. The word is borrowed from the idea that a person's actions accumulate into what he is. It is not a number the key holds; each reader derives the same figure from the record.
[^dot]: Delta over time: karma read as a rate, the change in standing across a span of blocks, rather than a lifetime total. Recent, sustained conduct counts for more than an old and idle history.
[^oracle]: An oracle is an agreed source that reports whether something is true, feeding a fact the system cannot check for itself into a decision, the way an oracle in antiquity was consulted for an answer taken as final. In Nown the parties, a quorum, or a reading of karma can each serve as one.
[^quorum]: A quorum is the number of members who must take part for a body's decision to count, and by extension the panel itself. In Nown it is the group of strangers drawn to settle one case by majority.
[^steward]: A steward is someone who holds a duty in trust for others and answers for it without owning it. In Nown, a steward is one of the strangers drawn onto a quorum to judge a case.
[^seal]: A seal is a signed or quorum-ratified mark fixed to a key and carried with it on the record, standing for a fact about its holder: a skill shown, a document certified, a membership held, ownership of a firm. A key's history is what it did; its seals are what others have certified about it.
[^timechain]: The timechain is bitcoin's public ledger: a chain of blocks, each built on the one before and ordered by proof of work, which cannot be rewritten without redoing all the work since. Nown uses it as a record no one owns and a clock that ticks the same for everyone.
[^pgp]: Pretty Good Privacy, Phil Zimmermann's 1991 email-encryption software. Its web of trust let each user judge a key's authenticity from signatures collected from other people, with no central authority, on a good-enough rather than perfect standard.
[^web]: Zimmermann, PGP User's Guide, Volume I, 1994.

---

*Released into the public domain under the Unlicense. No rights reserved. No owner.*
