[↰ back](../../..)
# Lecture 3: Consensus Part I: Proof of Work
## Contents
1. [Introduction](#introduction)
2. [Byzantine Fault Tolerance](#byzantine-fault-tolerance)
3. [The Double-Spend Problem](#the-double-spend-problem)
5. [Mining](#mining)
6. [PoW Vulnerabilities](#pow-vulnerabilities)
7. [Incentives - Why Participate in the Network?](#incentives---why-participate-in-the-network)
8. [Summary](#summary)
9. [What did we miss?](#what-did-we-miss)
10. [Readings](#readings)
11. [Exercises](#exercises)

## Introduction
Consensus broadly defines the process used by a network to reach a state of agreement. This process is a communication algorithm that allows nodes to determine what has happened and act accordingly. An activity initiated by a user (or by an autonomous process) needs to be recorded by the system which means that all participating nodes must be aware of the activity.

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/e4342bb3-f119-4836-8e53-8151f65dd89b">\
> Figure: Democratic parliaments work this way - a member proposes an update to the legislation, then through the course of debate (and perhaps incentivising favours) the house comes to agreement on updating the legislature. Source: https://www.parliament.nz/en/get-involved/features/parliament-s-debating-chamber-turns-100/

In the parliament-nodes metaphor, each MP needs to be aware of the proposed update, and then make an informed decision to support or deny the change. Not every citizen has equal influence as MPs represent a constituency. The same can be true in computing networks - not all nodes are equal. We can classify computing networks by three types: centralized, decentralized, and distributed. The centralized network has a main server that controls all the events. This is where the rules are implemented, and also where the off switch can be found. As organizations scale, this approach becomes more decentralized either due to computing resource constraints or organizational limits in the case of a global system, such as a bank. The tech giants we are used to todays are distributed - they have nodes, including data centers, in various jurisdictions while operating as a single entity.

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/ac182253-3850-4667-bc72-ed32550de671">\
> Figure: Degrees of decentralisation. The dots are nodes in the network and the graph edges are communication links. Source: Baran (1964) for an excellent overview of redundancy and vulnerability of digital communications networks.

On the right in the figure is a distributed (mesh) network which shows a high degree of decentralisation. If any node goes offline, the remainder of the network is largely unaffected. Compare with the middle figure where certain nodes can have large effects in the network should they be compromised or need to be repaired. 

### Centralised Consensus
Lets consider the case of withdrawing money from an ATM. The bank operates a network of ATM machines that maintain connection to a central server. A user requests \$100 from her local ATM. The machine must connect to the bank's server and query the database for an account balance, confirm that it is greater than the requested amount and respond to the ATM. The machine now sends a second request for withdrawal (step 3 in figure below) and the server will debit the users account, sending a message back to the ATM. It is only at this point that the \$100 can be dispensed; *after* the account has been debited. This is known as a **two-phase commit**; the first phase is a request, and the second phase is an action.

> <img width="800" alt="A single node simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/1fc47f55-f2d3-459a-8447-4a7f595eed3e">\
> Figure: A simplified ATM network and the steps required to withdraw money. This is an example of a client-server relationship. If communication fails at step 4 this could be a problem.

However, in a mutli-user environment it is feasible that two people can debit from the same account from two different locations, causing the database to be **inconsistent**. This can occur because the two transactions are able to alter the originating account value because the first transaction has had the chance write an update to the database. The solution to this problem is **two-phase commit**, which requires that the account record is locked when the first transaction starts and the resources progressively unlocked when they are no longer required. In the meantime, the second transaction waits until the record is fully unlocked or until it times out if the first transaction takes too long. It is only at this point that the $100 can be dispensed; after the account has been debited. 

> <img width="800" alt="Multiple nodes in a simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/e9795dc1-f495-4a7d-af17-1363cdba6f59)">\
> Figure: Multiple nodes in the network. If a simultaneous request comes from 1 and 2, the server needs to order the events and make sure it has heard from every node before responding at 4. Additionally, information may be stuck at 3 if there is a fault or a delay in the network communication and 4 will have to wait.

### Decentralised Consensus
Most systems we use today, from banks to social media to streaming services, employ a form of decentralised consensus where the network contains a small odd number of geographically separated data centers (nodes) to communicate in a manner that maintains truth in the presence of faults. For example, these **fault-tolerant** systems use algorithms such as Paxos (Lamport, 1998), used in many of Google’s systems (Chang et al., 2006), or Dynamo developed by Amazon (Decandia et al., 2007). 

### Distributed Consensus
The picture is different when the centralized server is removed; referred to as a peer-to-peer (p2p) network every participant is at the same level of the hierarchy. Now all the nodes (peers) must communicate with each other and decide on the true state of the blockchain. This is a circular process where all nodes must agree and some must propose updates which then need to be agreed upon.

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/72575c28-0f83-4a5f-a4b2-2099d1136b03">\
> Figure: A state diagram for a distributed blockchain involves continually proposing and processing updates to the state


The process of all nodes agreeing is consensus, and the process of proposing updates is accomplished by mining. The algorithms for consensus must still be fault-tolerant, just like centralized systems, but they must also be resilient against malicious, or *Byzantine* adversaries.

## Byzantine Fault Tolerance
If a node behaves in an arbitrary manner it is unreliable and can be assumed in the worst case to be acting as a malicious adversary. This is known as Byzantine behaviour named after the Byzantine Generals Problem[^BFT] formalized in the seminal paper by Lamport (1982) and inspired by NASA-funded work on fault-tolerant aircraft control systems.

[^BFT]: Lamport originally stole the name from the Chinese Generals problem (also called the General's Paradox) and wanted to name it *The Albanian Generals Problem*, but settled on the fallen empire to avoid offending anyone.

The *Byzantine Generals Problem*, now a famous computer science communication problem, involves the scenario of a general sending and receiving trusted messages. Imagine three generals of the same army, all wanting to attack an enemy fortress at dawn the next morning. Each general knows their individual divisions cannot win the enemy fortress. Each general also knows that with the help of the other's forces they can win the position. So General *Alpha* sends a messenger to General *Beta* with the message "We attack at dawn." This is where the problems start. There are many scenarios that could play out. The messenger could be captured by the enemy; the messenger could be a double-agent; the messenger could get lost and not deliver the message; General Beta could double-cross Alpha, etc. To win the battle, the three generals must come to consensus and agree to attack at dawn. Practically speaking, each general must receive confirmation from each of the other generals that they received the message *and* are in agreement. This scenario maps nicely onto cryptography and message-passing.

In an extension of the Generals Paradox, now several generals of the Byzantine army are camped near an enemy position. Each general commands their own battalion and can communicate via messenger. The generals must come to a decision to either attack or retreat while considering that there could be traitors among them. The generals must have an algorithm such that:
1. all loyal generals reach the same decision, and
2. any traitor(s) decisions can not change the outcome.

In their paper *Reaching Agreement in the Presence of Faults*, Pease (1980) showed for the general case that given $m$ faulty processors that always lie, the number of honest processors must be: $n>3m+1$. This means that up to one-third of the processors can deliver arbitrary information with a lower bound of four in the system.

Early work to overcome **Byzantine Fault Tolerance** (BFT) was either too inefficient or could not allow for messages to be delayed for arbitrary lengths of time. The landmark result by Fischer (1985) concludes that agreement among processors in which at least one is faulty is impossible without some form of timing assumptions such as a message timeout. This is because it is impossible to know if a message has been delayed indefinitely (it may never arrive). The difference between a slow node and a crashed node is difficult to detect.

<!-- Note here about the part-time parliament -->

A decentralized blockchain application has many nodes in the network and each of them has a copy of the blockchain. If Bob wants to send Alice his tokens, the nodes in the network must first agree that Bob has available tokens to spend, and then update the state before Bob can double-spend his tokens. The network needs to be in a state of *consensus* for people to trust it. Consensus in the Byzantine Generals problem has been proven to be impossible if more than a third of the nodes are malicious (Fischer, 1985).

#### What does this have to do with Bitcoin?
Bitcoin is an open, peer-to-peer system, and doesn't have the traditional moat security that corporations have. Thus, participation in a permissionless network has to include Byzantine behaviour assumptions.

So how does this occur without clear rules in the presence of adversaries? A closer look at the double-spend problem will illustrate how nodes come to agreement.

## The Double-Spend Problem
Solving the situation known as the *double spend problem*, is necessary for trustless decentralized digital cash to succeed. 

A dodgy actor, Eve, could manipulate the blockchain by sending some coins to Jeff and receiving a good or service. Then she could send those same coins to Bob's address whom she also controls. If the transaction involving Bob's address is validated on the blockchain, then Eve would have successfully double-spent the same coins. She now has the coins in Bob's address and the goods from the transaction with Jeff.

> <img width="800" alt="Double Spend Success" src="https://github.com/millecodex/COMP842/assets/39792005/3c5e1fdc-7521-4a0f-9b99-66e4f3d123b6">\
> Figure: For Eve to successfully double-spend in the blockchain she must take advantage of a fork in the chain. If the chain with the Eve to Bob transaction is the longest, representing the most cumulative proof of computation effort, she has double-spent.

How can Jeff avoid this scenario, especially when he does not know the other party he is transacting with? The solution is to wait. Over time as more blocks are added, say every ten minutes, the older blocks are more likely to be valid. Standard confirmation time for Bitcoin is six blocks, or one hour[^1]. Stated another way, as more blocks are added to the chain there is an exponential decrease in the probability of a block being rejected by other nodes. This is the method that secures the blockchain against malicious nodes attempting to double spend. 

[^1]: The number of blocks to wait until considering a transaction to be confirmed is a personal preference, there is no guaranteed, mathematically sound formulation for the number 6.

> <img width="800" alt="Double Spend Solution" src="https://github.com/millecodex/COMP842/assets/39792005/2adf3b0c-9a8b-4b52-9353-60931659393d">\
> Figure: Jeff has waited to accept Eve's transaction. After six confirmations it is very unlikely that Eve's alternate chain will accepted as valid. Over time there is increasing probability that transactions are secure.

And what about Eve changing history? She would have to alter the block where the transaction is stored, as well as any subsequent blocks. The older the block is, the more computational effort is required because the hash pointers are linked. Consider that Eve is also competing against other nodes in the network that are honest. Also consider the network is operating 24/7, there is no down-time for Eve to plan her attack where new blocks may be paused.

### ⛓️
Regarding Bitcoin nodes coming to agreement, it does not exactly mirror the model of the Byzantine Generals and so is not impossible to reach consensus. In other words, Bitcoin does achieve consensus despite Byzantine behaviour. More practically, Bitcoin achieves a state of *emergent* consensus. This means that over time as blocks get added to the chain, a general state emerges that everyone agrees on. Here we have a new method of distributed consensus, now known as emergent consensus, or eponymously as Nakamoto consensus. 

The _**absolute revolutionary**_[^revolution] contribution of Nakamoto was to use Proof-of-Work (next) to secure the ledger against double-spending attacks. Participants are insured against their coins being spent twice by the emergent property of the longest chain. If there is only ever a single chain, it will be the longest and represent the most proof-of-work and be the canonical state of the blockchain. As more blocks are added to the chain there is an exponential decrease in the probability of a block being rejected by other nodes. This is the method that secures the blockchain against malicious nodes attempting to double spend. Nakamoto consensus resolves forks in the chain by allowing both branches to remain active (alive) until there is a clear longest chain. At this point the shorter branch will be orphaned and any outstanding transactions need to be reprocessed and may have been superseded by others paying higher fees. This is the general process by which all proofing-style blockchains maintain consensus.

[^revolution]: Emphasis is mine. Not to be understated. Even though many parts of Bitcoin were around before Satoshi, such as ECC key pairing, spam reduction by proof of work, open source software, p2p networks, and so on, this was the component to both incentive honest behaviour and prevent digital double spending 🔥🔥🔥

## Mining
Referring back to the Figure, who gets to propose these blocks and earn the block reward? How do we ensure the distribution is fair Random? How are Sybil attacks prevented?

> <img width="800" alt="A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain." src="https://github.com/millecodex/COMP842/assets/39792005/ce672191-be4a-439e-8c12-af60acccf5b2">\
> Figure: A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain.

A miner is a network participant that contributes their computing power in a demonstrable way. A fair way to allocate the incentives would be by some resource that can not be gamed or monopolized. One such way is by computing power as proposed by Dwork and Naor in 1993 in relation to email spam, and refined by Back with Hashcash in 2002 for digital currency. Bitcoin miners participate by using their hardware to validate transactions and suggest new blocks. For this effort they receive rewards in proportion of their contribution to the network as a whole. A fair way to determine effort used by the miners is to have them search for a particular hash that meets a target. Bitcoin uses the `SHA256` hashing algorithm as the hash ~~puzzles~~ competition[^hashing] that miners have to win.

[^hashing]: One misconception this author notes is the hashes are sometimes referred to as *complex math problems* or hash *puzzles*, both of which are incorrect. SHA256 is just a recipe to scramble bits of data and using the terms *math* and *puzzle* imply that there can be some optization or "correct" solution.

> "Mining is the process of dedicating effort (working) to bolster one series of transactions (a block) over any other potential competitor block” -Gavin Wood, 2015, co-founder of Ethereum

To find a block, the mining node must bundle the available transactions and apply the hashing algorithm such that:
```
Block = Hash(nonce||previousHash||tx||tx||...||tx) < target
````
The `Hash()` output has a random distribution (see last lecture) and so to find a block, your hash must be below a certain target level. The target level will be the hash size with a certain number of leading zero bits, for example:
```
000000000000000000117c467ab5336077cb04f7f70ea6ebcd68e0b3ef6cf909
```
was the successful hash of block `529283`. The only way to find a hash with a smaller value than the target is to change a nonce value and re-hash the bundle of transactions over and over. When a target is hit, the block is broadcast to the network as a proof of computational work done in solving the hash puzzle. Note this is a hex value and so every additional zero bit represents a 16x decrease in probability of meeting the target.

### Difficulty Adjustment
The bits here should be randomly distributed, like a lottery, to prevent gaming the system and earning more rewards than your proportion. Computing cycles in the bitcoin network are called _hashpower_ in reference to `SHA256`. As more miners come online, the total hashpower increases leading to greater overall probability of successfully hashing a value below the target. To keep the temporal distribution of blocks even, this target difficulty automatically adjusts according to the protocol every 2016 blocks, or approximately two weeks.

Figure is a plot of the mining difficulty showing an exponential increase. The slope roughly correlates to the growth of the network. As the bitcoin network has matured, dedicated hardware called ASICs (application specific integrated circuits) to solve the `SHA256` algorithm have dominated. It is no longer feasible for a single participant to mine bitcoin without dedicated hardware.

> <img width="800" alt="Bitcoin mining difficulty plotted on a logarithmic scale." src="https://github.com/millecodex/COMP842/assets/39792005/a877855a-795f-431d-8d82-2c45b6b9cfe8">\
> Bitcoin mining difficulty plotted on a logarithmic scale. Source: https://www.blockchain.com/explorer/charts/difficulty


Consider a simulation using an Intel Core i5 6400 looking for `SHA256` hashes with leading zeroes. The difficulty in this case is increasing by powers of 16. Five leading 0's were found in 8364 seconds and, as of writing this, six leading 0's are predicted to take `≈ 8364×16=133824` seconds, or 37 hours.

```
Difficulty: 1
Nonce: 43
Proof-of-work: 05b7e096306a10c850cd8fe6bf55b1cc97365538cadbe3dc89e1216298275a69
Elapsed time: 0.0009968280792236328

Difficulty: 2
Nonce: 22
Proof-of-work: 002fcd61b3f3188e0f7fdff849e8dd3ee5805a34e06f4c6a8fd4fb86d4577350
Elapsed time: 0.005983591079711914

Difficulty: 3
Nonce: 12489
Proof-of-work: 0003124c9428d9a1c6f2ef0a782a044bcfde374cf6dfef414b161f8594377246
Elapsed time: 0.7731056213378906

Difficulty: 4
Nonce: 224827
Proof-of-work: 0000d66a2b464413b4af3b52ffef44a714ced1c06a4471c389755bf2eca19cef
Elapsed time: 239.61160159111023

Difficulty: 5
Nonce: 1230021
Proof-of-work: 000004ab089b08c3ceed5622dbe1ea0a3d621295379d107707cf2b8f9ffc9098
Elapsed time: 8363.934648275375
```

> <img width="800" alt="A Bitmain Antminer S9, 13.5 terahash edition with power supply. Coffee mug for scale." src="https://github.com/millecodex/COMP842/assets/39792005/676c6c14-d4e4-494e-b475-167c12b69c11">\
> A Bitmain Antminer S9, 13.5 terahash edition with power supply. Coffee mug for scale. Photo credit: Jeff.

The Figure shows a dedicated SHA256 miner. The S9 is (was) the workhorse of the bitcoin network. It contains 189 individual chips that calculate a total of 13.5 trillion hashes per second. (Compare this to the hashrate of the i5 above!)

### Block Time
The difficulty adjustment aims to keep the time between blocks (successful hashes) at around ten minutes. In the early days, Satoshi and a few others could use their PC processors to find blocks every ten minutes. The hashpower has steadily increased and so has the difficulty target to keep the block time constant. Finding a hash of a block that is below the target size is a discrete event; it is either below or it is not. As with a lottery, it is only a matter of time before a hash is found, and the previous hash is independent of the current attempt. Statistically, this is a *Poisson* distribution. 

> <img width="800" alt="Block Time Poisson" src="https://github.com/millecodex/COMP842/assets/39792005/e8c6651b-a33d-4371-9168-375721807172">\
> Figure: From the graph, you can see it's possible to find a block immediately after the last one, but unlikely. Similarly, it's possible that no block could be found for an hour or two, but also unlikely. In practice, the average block time is just under ten minutes because as more miners join the network it is easier overall to find blocks, until the difficulty is reset. Block time is a design consideration; PoW Ethereum adds a block approximately every 15 seconds.


## PoW Vulnerabilities
Two main weaknesses in proof of work cryptocurrencies will be briefly mentioned here and discussed further in the lecture on security.

### 51% attack
Should a single entity gain control of more than half of the hashpower in the network, this could lead to a 51% attack. The attacker can't steal coins directly as this involves subverting elliptic curve cryptography. The attacker can however user their majority status in some interesting ways. At >50% you have the ability to find more blocks and direct consensus of the blockchain, perhaps by censoring some transactions, or prioritizing their friends transactions.

### Selfish mining
An adversary doesn't necessarily need 51% of the hashpower, but with a large number of nodes in the network they could gain an advantage. An interesting analysis was published Eyal (2014) that showed a conglomerate of miners could form with as little as one-third of the hashpower. This mining cartel can continuously mine without broadcasting their blocks until some set time in the future. In the short term the miner is sacrificing the immediate block reward by not propagating their found blocks to neighbouring nodes. In the long run however, the result is that the honest miners are doing work that is not in competition with the selfish miners, increasing the attacker's expected rewards. 


## Incentives - Why Participate in the Network?
### Coinbase Rewards & Fixed Supply
Here is an important distinction where Bitcoin varies from other methods of reaching consensus. There are incentives for nodes to act honestly that are built into the protocol. The first is called the *coinbase* transaction and awards freshly minted bitcoins to whoever added the block to the chain. This is how new bitcoin comes into circulation. 

The economics of creating a new currency are tricky. There are many problems to consider such as: how is the money distributed? How much is there? How will the supply change over time? Bitcoin deviates from the textbook answers to these questions by setting a fixed upper limit on the number of bitcoin that will ever be produced in addition to a mathematical supply schedule.

### Fixed Supply
The fixed upper limit is set at 21 million[^rounding] bitcoin and is an aribtrary constant; as long as the money is divisible the unit amount does not matter[^fixed]. Bitcoin is divisible into 8 decimal places, so the smallest unit, a *satoshi*, is `0.000 000 01` BTC. Divisibility is a benefit of digital money as settlement of small amounts can be handled if fees are cheap enough. (For example, can you send 0.1 cents to someone in New Zealand dollars?)
[^rounding]: Due to rounding, this calculation comes out to slightly less than 21 million, see Exercises, also Antonopolous.
[^fixed]: Some economists may have a different opinion. See [What is the money supply?](https://www.econlib.org/library/Enc/MoneySupply.html). Most of these types of economists do not believe in Bitcoin. Thankfully, this is not an economics course!

> <img width="800" alt="bitcoin supply showing the block reward decrease. Note the y-axis is a logarithmic scale." src="https://github.com/millecodex/COMP842/assets/39792005/0462d774-f34e-46ce-b70f-fdf4e045e398">\
> Figure: Chart showing the block reward decrease. Note the y-axis is a logarithmic scale.

Bitcoin's supply schedule is unique because its known in advance how many new coins are going to be produced and available to the market. Every 210,000 blocks ($\approx$ four years) there is a halving event and the next block found is only allowed to pay out half the bitcoins. This defines a finite money supply. If you run the clock forward, assuming a new block is added every ten minutes, there will be no new bitcoin minted after the year 2140 (not a typo!)[^lastcoin].
[^lastcoin]: The last whole bitcoin will start to be mined in about 2100 with the final few satoshis being rewarded _forty_ years later.

> <img width="800" alt="Chart showing the mining reward decreasing geometric series overlaid with the total supply of bitcoin." src="https://user-images.githubusercontent.com/39792005/147862906-6537e8d0-aa4d-403d-825b-aefd1e31585a.png">\
> Figure: Chart showing the mining reward decreasing geometric series overlaid with the total supply of bitcoin. 

The [CoinGecko chart](https://www.coingecko.com/en/explain/bitcoin_halving) shows bitcoin's total supply approaching 21 million (green) and the blockreward being cut in half every four years (red). After the final fraction of a bitcoin is mined the network will be incentivised entirely from transaction fees being awarded to the miners. 

### Transaction Fees
The second incentive is from transaction fees. By listening to the network, validating transactions, and including them in a block, whoever is operating the node can choose to include transactions that offer an extra fee. Because bitcoin itself is designed to be digital money, this makes perfect sense and is why cryptocurrency is considered the killer app for blockchain. 

# Summary
Consensus is the process of networks coming to agreement when new information is introduced and requires processing. Distributed consensus in computing networks requires an algorithm to decide who updates the network? and how to come to agreement? A common algorithm in distributed systems is PBFT - Practical Byzantine Fault Tolerance, which can tolerate up to $\frac{1}{3}$ of the nodes to be malicious or unresponsive. Blockchains are a hyper-decentralised version of a distributed system and some of the consensus algorithms are based on PBFT (more one this next lecture), but the primary method that maintains Bitcoin and until September 2022 maintained Ethereum was Proof-of-work computing. 

PoW consensus uses the random non-deterministic nature of hash functions to allocate incentives for nodes to maintain a longest-chain of blocks representing the state of the ledger. The nodes are all agreeing that this chain represents the most cumulative computational effort via hashing. It is quick to validate the proof of work because the nonce for every block is published. As soon as a miner learns of a new block, they will abandon shorter chains to compete to build on the longer one to win the block reward. The transactions in this chain will have an increasing probability of being accepted over time as new blocks are mined on top of them. 

# What did we miss?
* We have not discuss alternate consensus mechanisms such as Proof-of-Stake that Ethereum uses.
* We have not mentioned a lot about forking behaviour in consensus, or other particular details such as sybil resistance mechanicsms. More on this next lecture.

# Exercises
1. How does the Proof-of-Work consensus algorithm address the potential issue of Sybil attacks in a blockchain network?
2. In the context of the 'longest chain' rule, can you describe a scenario where a malicious miner with substantial computational power attempts to create an alternate chain in the network? How does the system maintain its integrity in such a situation?
3. Explain the balance required for a fees-based network. What happens when fees get (a) too high? (b) too low?
4. Write a script to calculate the total number of bitcoin that will ever be mined. How many halvings will there be?

# Readings
* SoK (Systemization of Knowledge) from 2015 by the authors of the Princeton Textbook. An oldie but goodie. [(pdf)](https://github.com/millecodex/COMP842/blob/master/papers/SoK_Research_Perspectives_and_Challenges_for_Bitcoin_and_Cryptocurrencies.pdf)
* The ‘Skull of Satoshi’ Proves Bitcoin Mining Discourse Isn’t Dead - [Coindesk](https://www.coindesk.com/consensus-magazine/2023/03/27/the-skull-of-satoshi-proves-bitcoin-mining-discourse-isnt-dead/)

# Next Lecture
* :point_right: [Proof-of-Stake Consensus](4-consensus-pos.md)

# Video Lecture
Here's this lecture recorded live August 01, 2023 on [YouTube](https://www.youtube.com/watch?v=LOGQ7C83tDc).

# References
1. Baran, P. 1964. On distributed communications: I. introduction to distributed communications networks. Santa Monica, CA: RAND Corporation. https://www.rand.org/pubs/research_memoranda/RM3420.html
2. Chang, F., Dean, J., Ghemawat, S., Hsieh, W. C., Wallach, D. A., Burrows, M., Chandra, T., Fikes, A. & Gruber, R. E. 2006. Bigtable: A distributed storage system for structured data. In 7th USENIX symposium on operating systems design and implementation (osdi) (pp. 205–218). https://doi.org/10.1145/1365815.1365816
3. Decandia, G., Hastorun, D., Jampani, M., Kakulapati, G., Lakshman, A., Pilchin, A., Sivasubramanian, S., Vosshall, P. & Vogels, W. 2007. Dynamo: Amazon’s highly available key-value store (Tech. Rep.). https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
4. Eyal, I., Sirer, E. G. (2014). Majority Is Not Enough: Bitcoin Mining Is Vulnerable. *Financial Cryptography and Data Security*, 436–454. https://doi.org/10.1007/978-3-662-45472-5_28
5. Fischer, M. J., Lynch, N. A. & Paterson, M. S. 1985. Impossibility of distributed consensus with one faulty process. ACM, 32(2), 374–382. https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf
6. Lamport, L., Shostak, R., & Pease, M. 1982. The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems, Volume 4, Issue 3, pp. 382–401. https://doi.org/10.1145/357172.357176
7. Lamport, L. 1998, May. The part-time parliament. ACM Trans. Comput. Syst., 16(2), 133–169. http://doi.acm.org/10.1145/279227.279229 doi: 10.1145/279227.279229
