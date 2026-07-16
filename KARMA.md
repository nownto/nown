# Karma — the point system

Design draft for the Nown karma system. Research + synthesis, 2026-07-16. Not final: the absolute
constants are Niko's to calibrate, and the honest limits are stated at the end.

Karma is the crown jewel of Nown: a single portable reputation that proves trustworthiness to any
stranger, in any context. Because the quorum can rule on any question, not only trade disputes,
karma must accrue and deplete from **every** action on the protocol. Everything you do carries a
positive or negative outcome for your standing.

---

## In one paragraph

Karma is not a stored balance but a single portable number every client recomputes deterministically
from a public, Bitcoin-anchored, nostr-signed ledger of costly actions. It is the accumulated,
non-refundable cost a participant has paid to behave well per unit of time, expressed as the trust
that flows into them from the already-trusted, independent graph. Only signed, costly, irreversible
acts bound to a distinct bonded counterparty move it; speech and free ratings move it by zero. Every
action across trade, vouching, dispute, stewarding, and governance both mints karma (settled dealings
with new counterparties, coherent quorum service) and can deplete it (slashed bonds for reneging,
losing disputes, incoherent or collusive verdicts, and inactivity decay). Each change is a ratio, not
an absolute unit, shaped by five factors deducible from the costly-signal axiom: value at risk,
concave diminishing returns, a time-gated tenure ceiling no money can buy, counterparty diversity,
and eigenvector trust-flow. So wash-trading rings, praise loops, and whales all hit low ceilings while
sustained honest breadth compounds. Stewards serve only by staking capital and their own karma, sized
to the dispute and slashed harder when many err together, paid solely from the losing deposit and
slashed peers, so no owner profits. Outcomeless governance votes are scored self-containedly by
peer-prediction.

---

## The design

**Karma is a recomputed function, not a balance.** No account holds karma. It is a pure function every
client recomputes from a public append-only ledger of signed events, the way a bank balance is derived
from a ledger rather than kept in a drawer. Each event is nostr-signed by the actor, batched, and the
batch root hash is anchored to Bitcoin (OpenTimestamps style); the data stays off-chain. Every client
runs the same fixed weights and derives the same number, so karma is one canonical, portable value a
stranger reads at a glance.

**What the number measures.** The accumulated, non-refundable cost a person has paid to behave well,
per unit of time, as trust flows in to them from the already-trusted, independent graph. Mechanically
it is the stationary trust-inflow (the EigenTrust / MeritRank random-walk family) over the event graph,
with no pre-trusted seed set, because a seed set would be an ownership backdoor. The anchor that
replaces the seed is a-priori and grants no authority: Bitcoin sacrifice, per-action bonds, and elapsed
time.

**Admissibility.** An event moves karma only if it is (a) signed by the actor, (b) costly and
irreversible (burns capital at risk, produces a settled non-reversible outcome, and/or vests only over
real time), and (c) bound to a distinct bonded counterparty and a timechain timestamp. Speech is not
action: profiles, self-ratings, and free praise cost nothing and move karma by exactly zero.
Demonstrated preference only. What someone paid for is who they are.

**Every action moves karma, up or down.** Positives are minted only by settled dealings with distinct
counterparties and by coherent quorum service. Negatives are slashed from bonds the account posted to
act. Nothing is granted by authority; there is none.

| Action | Karma | Note |
|---|---|---|
| Create an account | − | one-time uniform Bitcoin sacrifice; standing starts at zero |
| Settled trade, seller | + | base mint; concave in value, diversity-weighted |
| Settled trade, buyer | + | smaller than the seller side |
| Cooperative close (mutual release) | + | small bonus; rewards clean exits over silence |
| Repeat trade, same counterparty | +/− | sharply diminishing toward zero |
| Trade with a new/low-karma party | + | diversity uplift; adds an independent edge |
| Non-delivery / reneging (uncontested) | − | scaled to bond and value |
| Vouch for another account | +/− | stake a slice of your own standing; deferred |
| Being vouched by a high-karma independent account | + | real external trust-inflow |
| Voucher slashed after vouchee ruled a fraud | − | fraud propagates back along endorsing edges |
| Open a justified dispute you win | + | small; restitution, not profit |
| Frivolous dispute you lose | − | deposit burned + penalty |
| Vindicated as the accused | + | restores standing the accusation risked |
| Lose a dispute | − | deposit + karma slashed, scaled to value |
| Coherent quorum service | + | bond returned + reward |
| Incoherent verdict / later overturned | − | bond slashed, correlation-scaled |
| Drawn but no-show / abstain | − | availability penalty; lower future draw odds |
| Coherent general (non-trade) vote | + | thin mint / redistribution share |
| Incoherent general vote | − | slashed, redistributed to coherent voters |
| Tenure in good standing | + | slow, capped by the timechain, unbuyable |
| Inactivity / decay | − | geometric half-life on unrenewed karma |
| Transfer / sell an account | 0 | standing carries; a transfer marker is stamped |

**Magnitude: ratios and curves, not units.** No change has an absolute unit. Each is a relative
contribution set by five composable factors, all deducible from the costly-signal axiom. (1)
Value-anchored: the size scales with the bond actually at risk. (2) Concave: every factor passes a
sub-linear curve, so the tenth unit from one source is worth far less than the first, capping what any
single stake or relationship buys. (3) Time-weighted: the whole score is gated by a tenure ceiling
clocked to the timechain, so buyable inputs saturate within about a day and the rest is pure elapsed
time nobody can parallelize. (4) Counterparty-diversity-weighted: up for a fresh independent party,
toward zero for a recycled edge. (5) Trust-flow-weighted: each inbound edge is scaled by the
eigenvector standing and independence of its source (asymmetric transitive trust, so you cannot raise
your own standing by vouching outward); a ring with no external inflow scores nothing.

**Depletion: four ways, all slashing of staked things, never a fine.** (1) Adverse-verdict slashing:
the losing side's deposit burns and karma is cut, scaled to value; fraud propagates back to vouchers.
(2) Incoherent-steward slashing: capital plus staked karma, redistributed to coherent stewards, with
correlated-fault scaling from proof-of-stake, so an isolated error is cheap but a coordinated wrong
bloc is punished toward total loss, because correlation is the signature of collusion. (3) Decay:
unrenewed karma bleeds geometrically against the timechain. (4) Frivolous-action penalties. All
slashes fund the honest side or are burned; none accrue to any operator, because there is none.

**Giving karma costs the giver.** A costless rating moves karma by zero. To vouch, the giver stakes
their own karma plus a capital deposit behind the recipient, slashable if the recipient is later
judged a fraud. The give-budget is quadratic per epoch: one sincere vouch is cheap, the n-th costs
about n squared, so endorsements cannot be sprayed. A mutual-praise ring pays quadratically to endorse
itself while earning nothing, since karma is inflow from outside and a closed loop has none.

**Steward skin in the game.** To serve, a steward locks a capital bond plus a slashable fraction of
their own karma, both sized to the value in dispute. Panels are value-scaled: few stewards on a small
claim, many on a large one, so expected pay for honest reading always clears the cost of reading and no
large sum ever rests on a handful. A coherent verdict (lands with the sealed majority) returns the bond and pays the steward; an incoherent one is slashed and the
steward is drawn less often. Stewards are scored across a batch of cases, so honest reading dominates
any lazy or collusive rule over many cases whatever the others do. Honest stewards are paid from the
losing side's pre-posted deposit plus the slashed stakes of incoherent stewards; the protocol takes
nothing. Two invariants hold it together: expected honest pay exceeds the cost of reading, and the
slash for incoherence exceeds any bribe divided across a panel that grows with the stake.

**Universal (non-trade) voting.** A governance, moderation, or oracle question has no losing deposit to
fund rewards, so the incentive is self-contained. To enter the draw a steward posts a karma bond; the
proposer posts a bounty bond that becomes the reward pool. Since many such questions have no observable
ground truth, scoring uses peer-prediction (the Bayesian truth serum): each steward submits a sealed
vote and a forecast of how the others will vote, scored on agreement with the sealed tally plus
forecast accuracy, so the surprisingly-popular answer scores highest. Coherent participants recover the
bond and mint a share of the bounty; incoherent ones are slashed and redistributed to the coherent. The
panel is zero-sum against itself, with no external loser and no operator subsidy. Every collective
decision writes a signed karma event, so karma becomes the single stake that follows a person across
trade, moderation, and governance.

**No karma millionaires.** Three clamps, all rooted in time as the equalizer: a tenure ceiling bounds
maximum karma by account age; concave accrual plus decay means early bursts in a thin network yield
little and evaporate unless renewed with fresh distant counterparties; and money enters as one
diminishing input. The pioneer's only durable edge is seniority, which is mild and dilutes as the
network grows.

**Freeze and anti-manipulation.** Karma is frozen the moment a vote or quorum opens, so selection and
vote-weight cannot be manipulated at the last minute. Cluster caps (spectral / community detection)
limit any single trust-cluster's share of the eligibility set and of any drawn quorum, so a large
self-certifying sybil ring still cannot pack panels.

---

## The rule set (developer-facing spec)

R1. Karma is never a stored balance. Every client recomputes it from the public append-only event
ledger with protocol-fixed weights, so all honest clients derive the same canonical number.
Personalized re-weighting from a viewer's own seed is an optional overlay only.
R2. Substrate: each event is nostr-signed, carries a timechain timestamp, is batched, and the batch
root hash is anchored to Bitcoin. Event data stays off-chain; Bitcoin stores only the timestamped root.
R3. Admissibility: an event moves karma only if signed by the actor, costly and irreversible, and bound
to a distinct bonded counterparty. Fail any and it is inadmissible.
R4. Speech moves karma by zero. Profiles, self-ratings, free praise are inadmissible.
R5. Karma = stationary trust-inflow over the event graph (EigenTrust / MeritRank), asymmetric so no
account raises its own standing by vouching outward. Never hardcode a pre-trusted seed set; the anchor
is Bitcoin sacrifice + per-action bonds + elapsed time.
R6. Every admissible event carries a signed change of the form sign · f(bond-at-risk, tenure, trust-
inflow, counterparty-novelty). Positives minted only by settled distinct-counterparty dealings and
coherent quorum service; negatives slashed from posted bonds.
R7. Magnitude set by five composable, sub-linear factors: value-anchored, concave per source,
time-gated by a tenure ceiling, diversity-weighted, trust-flow-weighted by the source's standing and
independence.
R8. Absolute constants (base reward, decay half-life, tenure-ceiling height, slash fractions, entry
sacrifice, quadratic give coefficient) are free network parameters, NOT derived from axioms. Set them
explicitly, version them, keep them protocol-fixed (no discretionary admin retuning).
R9. Account creation costs a uniform irreversible Bitcoin sacrifice; standing starts at zero. N
accounts cost N times one; no volume discount. This is the sybil entry price, not proof-of-personhood.
R10. Settled trade mints karma: seller base, buyer smaller. Cooperative close adds a small bonus over
bare settlement.
R11. Repeat trade with one counterparty diminishes toward zero; a new/low-karma counterparty gets a
diversity uplift. Trust comes from breadth, not one recycled edge.
R12. Uncontested non-delivery/reneging records a negative, scaled to bond and value.
R13. Vouching stakes a slice of the giver's own karma + a capital deposit; deferred until the vouchee
resolves; slashed if the vouchee is judged a fraud. Fraud propagates back along endorsing edges.
R14. Give-budget is quadratic per epoch: the n-th vouch costs about n squared.
R15. Disputes: justified win returns deposit + restitution; frivolous loss burns deposit + karma;
vindication restores risked standing; loss slashes deposit + karma scaled to value.
R16. Steward stake to serve = capital bond + slashable fraction of own karma, both sized to the value
in dispute. Panels value-scaled: few stewards on small claims, many on large ones.
R17. Coherent verdict (lands with the sealed majority) returns bond
+ reward. Incoherent (against outcome, or provably lazy) is slashed and redistributed to coherent
stewards.
R18. Correlated-fault slashing: the incoherent penalty rises with how many stewards were wrong in the
same window. Isolated error cheap; a coordinated wrong bloc punished toward total loss.
R19. Stewards scored across a batch of cases, so honest reading dominates any lazy/collusive rule over
the batch. Verdicts repeatedly overturned by later quorums bleed karma retroactively.
R20. Steward funding is closed and ownerless: honest stewards paid from the losing deposit + slashed
incoherent stakes; the protocol takes nothing. Invariants: expected honest pay > cost of reading;
slash-for-incoherence > max bribe / panel size.
R21. Drawn-but-no-show/abstain: small availability penalty, forfeit reward, lower future draw odds.
R22. General (non-trade) quorums fund themselves: steward posts a karma bond; proposer posts a bounty
bond as the pool. Score with peer-prediction (sealed vote + forecast of others). Coherent recover bond
+ bounty share; incoherent slashed and redistributed. Zero-sum against itself; no operator subsidy.
R23. Grave-case escalation to a written-question round requires an added bond, returned + standing if
coherent, slashed if frivolous.
R24. Tenure: karma accrues slowly with elapsed time in good standing, capped by a timechain ceiling;
unbuyable, unparallelizable. Seniority is the only residual bias and dilutes as the network grows.
R25. Decay: unrenewed karma bleeds geometrically against the timechain. Renewal needs fresh costly
conduct with distinct, independently-trusted counterparties; circular self-maintenance cannot offset it.
R26. Freeze karma the moment a vote/quorum opens (block last-minute manipulation).
R27. Cluster caps: spectral/community detection caps any single trust-cluster's share of the
eligibility set and of any drawn quorum.
R28. Karma gates eligibility (threshold tiers to steward and to take larger stakes). The fresh
slashable per-action bond, not karma history, is what makes fraud negative-EV at decision time.
R29. Account transfer carries standing but stamps a visible transfer marker; graph-inflow must
re-establish. The marker reports a discontinuity; it cannot prove the key changed hands.
R30. All slashes fund the honest side or are burned. Nothing accrues to any operator, because there is
none.

---

## Open questions (stated plainly, not hidden)

1. The absolute constants are unproven. Base reward, half-life, ceiling height, slash fractions, entry
   sacrifice, and the quadratic give coefficient are free parameters; only live adoption reveals a good
   set. Needs Niko's initial calibration and a low-stakes tuning period.
2. "Coherence" without ground truth measures honest agreement, not truth. A large, patient, coordinated
   majority sharing a sincere false belief scores as coherent. The mechanism resists collusion and
   crowd-prediction, not universal sincere error. Decide whether to bound the stakes of outcomeless
   votes.
3. The trust-flow computation must run over a continuously growing graph. That is a real computational
   and data-availability cost the a-priori design assumes away. Needs a concrete deterministic scheme
   (for example staked reputation-miners who submit a slashable root hash) so everyone derives the same
   number without an owner.
4. Sybil cost is bounded, not provably sufficient a priori. Security is only as strong as the entry
   sacrifice plus honest-graph diversity, and cannot be validated in a lab. Open: what stake ceiling is
   defensible while the network is young?
5. Proof-of-personhood is unsolved. An adversary who cheaply mints or simply buys real humans defeats
   one-key-per-person. Decide whether an optional personhood overlay is worth adding later.
6. A bought aged key inherits standing; the transfer marker reports a discontinuity but cannot detect
   gradual capture, a slow sellout, or a stolen key. This is why decision-time security must rest on
   the live bond.
7. The Advogato capacity flaw must be actively avoided: node trust-capacity must be computed before an
   attack, never inflated by the edges under attack. Needs a concrete algorithm choice and audit.
8. Cluster-cap tuning: how aggressively to cap panel share without excluding legitimate tight-knit
   honest communities is an unsolved calibration tradeoff.
9. Buyer/seller asymmetry, panel-size curves, and the value-to-panel-size mapping are asserted
   qualitatively; the precise functions need modeling against the two steward invariants.
10. No empirical validation exists. The whole system is a-priori reasoning from demonstrated preference
    and time as the equalizer. The honest bounded claim: karma raises the cost of forging trust above
    the value it protects only for stakes within the sybil-cost bound while the network is young. Not
    that it is unforgeable or unstoppable.

---

## Prior art borrowed

EigenTrust / MeritRank (stationary trust-inflow, no seed set) · asymmetric transitive trust
(Cheng-Friedman, Advogato, so standing cannot be self-manufactured) · proof-of-stake slashing with
correlated-fault penalties (coordinated error punished hardest) · quadratic funding (super-linear cost
to spray) · Colony (karma-with-decay, freeze-at-vote) · peer-prediction / Bayesian truth serum and the
surprisingly-popular answer (scoring votes with no ground truth) · Chronicle Network, Luka Dover
(costly signed reputation graph, Bitcoin-anchored, the companion substrate). Credit these where the
work is used.
