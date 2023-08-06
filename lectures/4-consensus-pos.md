[↰ back](../../..)

# Lecture 4: Consensus Part II: Proof of Stake & Alternatives
## Contents
1. [Proof of Stake](#proof-of-stake)
2. [Digital Scarcity](#digital-scarcity)
3. [Proof-of-X (PoX)](#pox)
5. [Decentralisation](#decentralisation)
6. [What is a Blockchain?](#what-is-a-blockchain)
7. [Summary](#summary)
8. [What did we miss?](#what-did-we-miss)
9. [Readings](#readings)
10. [Exercises](#exercises)

Recall the state diagram from Lecture 3. A distributed computing system has nodes that are geographically separated, may run different versions of the software, have varying latencies, and no minimum or maximum thresholds for participants. All nodes must agree on the state of the ledger without any authority figures. Just like playing recreational sports in the absence of a referee, there are generally agreed upon rules that when followed make the experience worthwhile. These are the consensus rules that are programmed into the software. Keep in mind that truly distributed systems have open source software that anyone can edit[^oss].

[^oss]: Governance in distributed open-source systems is another area of study. It is theoretically possible to change the rules of bitcoin by modifying the core client because anyone can fork the [repo](https://github.com/bitcoin/bitcoin) and make changes. Distributing the `new' version and having it gain acceptance is another matter.

### ⏸️🕐 
Its worth a pause here to think about **How can you chose someone (a node) to make updates?**

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/031d091a-5329-48f7-a9aa-4e37019d79e6">\
> Figure: A state diagram for a distributed blockchain involves continually proposing and processing updates to the state

If your network is distributing rewards such as a coinbase then its imperative that (a) people think the distribution is fair and (b) it can't be gamed. If your network is not distributing obvious financial rewards, then do the same questions apply? And if your network is permissioned (perhaps an Amazon datacenter) then do these questions matter?

## Proof of Stake
Shortly after Bitcoin started people were looking at alternate ways to achieve decentralised consensus by varying the rewards, hashing mechanism, and mechanics of winning a block to append to the chain. One of the primary criticisms of Bitcoin is the mining aspect which seems to incentise more and more miners and specialized hardware coming online just to try and win the block reward.

> "Proof-of-work helped to give birth to Nakamoto’s major breakthrough, however the nature of proof-of-work means that the crypto-currency is dependent on energy consumption, thus introducing significant cost overhead in the operation of such networks, which is borne by the users via a combination of inflation and transaction fees."\
> 👉 Sunny King, Scott Nadal, [PPCoin Whitepaper](./papers/peercoin-paper.pdf), August 2012.

First outlined by King and Nadal, they suggested a mechanism where users put up a stake of their coins to validate transactions and earn rewards proportional to their stake in the network. The [Peercoin](peercoin.net) design still uses a proof-of-work hash system for users to earn the block proposing right by lottery (in combination with a property called *coin age* $=$ days $\times$ stake), but it is in a limited capacity. In this case, seniority wins and allows for minting rewards based on the amount of coins being held and the length of time they've been inactive. The network can be classified as a hybrid PoW/PoS system.

2014 saw a bloom of research and projects into proof-of-staking style blockchain systems. A proof-of-stake-only system will use staking both for network security and for minting of new tokens. 
* Nxt, a "100% proof-of-stake cryptocurrency", is released in late 2013 with a whitepaper in 2014
* Bitshares introduced Delegated Proof-of-Stake
* *Tendermint: Consensus without Mining* is published; an algorithm for blockchain consensus based on PBFT

Motivation for the switch to a staking-type blockchain is primarily mining centralisation risk, but there are also resource consumption concerns, probabalistic versus deterministic transaction finality, and an element of intellecual curiousity - Can we do this without mining?

In July 2015 just before proof-of-work Ethereum launched there was a short discussion about Ethereum's intention to switch to proof-of-stake, with Vitalik [saying](https://www.reddit.com/r/ethereum/comments/3evolq/how_many_ethers_are_going_to_be_created_in_the/) at the time "the plan is 9-12 months." This ended up taking 7 years. [Casper](https://arxiv.org/abs/1710.09437) is published in 2017 by Vitalik Buterin and Virgil Griffith as the groundwork for a transition for Ethereum to proof-of-stake. 

> "Proof-of-stake underlies certain consensus mechanisms used by blockchains to achieve distributed consensus. In proof-of-work, miners prove they have capital at risk by expending energy. Ethereum uses proof-of-stake, where validators explicitly stake capital in the form of ETH into a smart contract on Ethereum. This staked ETH then acts as collateral that can be destroyed if the validator behaves dishonestly or lazily. The validator is then responsible for checking that new blocks propagated over the network are valid and occasionally creating and propagating new blocks themselves."\
> 👉 From the [ethereum.org](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) website describing Proof-of-Stake

Colloquially, proof of stake means any system where a user puts up collateral and earns rewards proportional to their collateral. Proof of stake assumes that participants with the most personal value in the system will have an interest in maintaining operations. It closely relates to shareholding in a public corporation whereby shareholders are entitled to certain rights and expect the corporation to maintain or increase the value of their shares. Stake holders may be awarded voting rights in governance decisions such as disbursement of community funds or changes of protocol. Users are incentivised to maintain their share in the project through block creation and reward, fees, and potential increases in token value.

Proof-of-stake is lightweight compared to Bitcoin by not requiring substantial hardware investment such as mining equipment and therefore also does not have the electricity consumption. There is a low barrier to entry as you simply need to acquire some of the coin to participate. However, this could also allow a large player to influence the network by purchasing their way in. We will cover more staking-specific issues in the Lectures on Ethereum, and Security.

## Digital Scarcity
So far we have two categories of blockchain consensus: proof of computational work, and proof of token-value. We can extend this to other categories as long as the network is allocating a scarce resource. In the case of PoW miners this is the amount of bit-flipping the ASICs can do. For PoS it is the guarantee that tokens-staked are scarce and therefore have value to users of the network. There are other methods of consensus scarcity, votes for example are a scarce resource because one person is entitled to one vote, and only one vote. The same can be said if a node or processor is allocated a single vote.

The table shows various consensus methods classified by the scarce resource that is utilized. Note the resource doesn't have to be universally scarce, just within the bounds of the network and its participants.

|👇Consensus Method| bits | time | cc* | tokens | biology | votes | Fault Tolerance | Example Blockchain |
|------------------|------|------|--------------|--------|---------|-------|-----------------|--------------------|
| PBFT             |      |      |              |        |         | :heavy_check_mark: | 3f+1  | Hyperledger Sawtooth  |
| BFT-SMaRt        |      |      |              |        |         | :heavy_check_mark: | 3f+1  | R3 Corda          |
| Federated BA     |      |      |              |        |         | :heavy_check_mark: | 5f+1 -- 3f+1 | Stellar, Ripple   |
| Honeybadger      |      |      |              |        |         | :heavy_check_mark: | 3f+1  | POA Network       |
| 2PC              |      |      |              |        |         | :heavy_check_mark: | 2c+1  | RSCoin             |
| Paxos            |      |      |              |        |         | :heavy_check_mark: | 2c+1  | none               |
| Raft             |      |      |              |        |         | :heavy_check_mark: | 2c+1  | Quorum             |
| Hashgraph        |      |      |              |        |         | :heavy_check_mark: | 3f+1  | Hashgraph, IOTA   |
| DPoS             |      |      |              | :heavy_check_mark: |         | :heavy_check_mark: | 3f+1 -- 2f+1 | Steem, EOS |
| PoS              |      |      |              | :heavy_check_mark: |         |              | 3f+1  | Ethereum**, Decred |
| Tendermint       |      |      |              | :heavy_check_mark: |         |              | 3f+1  | Cosmos   |
| PoW              |      |      | :heavy_check_mark: |        |         |              | 50\%  | Bitcoin   |
| PoCoinAge        |      | :heavy_check_mark: |              | :heavy_check_mark: |         |              | 50\%  | Peercoin/Ppcoin    |
| PoElapsedTime   |      | :heavy_check_mark: |              |        |         |              | 2c+1  | HL Sawtooth       |
| PoRetrievability | :heavy_check_mark: |      |              |        |         |              | 50\%  | Permacoin (PoR)   |
| PoSpace          | :heavy_check_mark: |      |              |        |         |              | 50\%  | Spacemint          |
| PoSpaceTime      | :heavy_check_mark: | :heavy_check_mark: |              |        |         |              | 50\%  | Filecoin  |
| PoMemory         | :heavy_check_mark: |      | :heavy_check_mark: |        |         |              | 50\%  | Zcash, Beam        |
| PoHumanWork      |      | :heavy_check_mark: |              |        | :heavy_check_mark: |              | -     | none   |
> Table: Taxonomy of blockchain consensus methods. The primary classification is by Scarce Resource that the blockchain occupies. *cc is clock-cycles; **Ethereum switched from Proof-of-Work to Proof-of-Stake in September, 2022. Source: Nijsse & Litchfield, 2020.

**Clock-cycles** The *work* in a proof-of-work system is the computational work done by the processor in finding a hash value subject to some target requirement. Similar to physics work being non-reversible, the computational work done by a chip cannot be recovered or undone. Clock-cycles are scarce because the energy input has non-zero cost. A cryptographic requirement here is that the hash function is one-way—given any hash the data cannot be inferred, and easily verifiable – given the data the hash can be checked against the target.

**Tokens** Proof-of-stake removes the thermodynamic inefficiency by allocating users a stake in the system proportional to their tokens. This stake can then be used to scale incentives for users that participate, generally by committing their tokens in a manner that could result in negative consequences.

**Votes** are different than staked tokens as they hold no utility other than determining a majority. Nearly half of the methods in the Table employ votes as the scarce resource. A BFT system must determine consensus by the replicas voting on the state. Votes are scarce because a replica is only permitted one vote per round, however the votes have no value – in subsequent rounds all replicas are allocated a further vote. Classical consensus methods that maintain state in a non-blockchain system such as Paxos use voting to elect leaders. Many of these methods have been adopted for blockchain consensus and thus bring their votes-as-a-scarce-resource characteristic.

**Bits** represent the state of a transistor and occupy a finite amount of space on disc. Proof of capacity regimes allocate a user’s stake in the system by a proportion of disc space. Just as tokens that are staked, disc space cannot be used for other purposes if it is participating in the blockchain. Disc space scales more slowly compared to processing power and may reduce a blockchain's potential to be dominated by application-specific integrated circuits (ASICs).

**Time** is independent of computing advances. As clock-cycles and read-write times get faster, blockchains secured by these resources may be exposed to unforeseen factors. Proof of elapsed time (PoET) are chips with separate execution environments, or enclaves, that are inaccessible to the system. These modules can return a random delay to a process that can be used to assign block proposers.

**Biometrics** are a range of indicators that can verify identity or life. Similar to a hash function requiring a known average number of clock-cycles, a blockchain based on proof-of-biometrics can require a unique biological solution. The completely automated public Turing-test to tell computers and humans apart (CAPTCHA) system is easy for humans to solve while requiring some small amount of time is an example of using a biological system (time here is implicit) to solve a puzzle. Although there is no current blockchain project incorporating biometrics, it has been proposed by Blocki (2016), and adds a biological element to the dimension of scarce resources.

## PoX
Many alternative methods have been proposed in the literature and some have prototypes, but most of the differentiation or 'innovation' comes from implementation methods, rather than fundamental differences in networks reaching agreement. Some methods include:

**Proof of space** uses disk space as a resource. Most users have unused disk space on their machines; dedicating some of this to secure a blockchain would not require additional power or dedicated hardware. A proof of space system would require a network participant to hold a large file on their system. To prove they have dedicated the disc space, they might have to verify random parts of the file from time to time. 

**Proof of retrievability** is a modification of bitcoin, implemented in Permacoin, that would allow for a large dataset such as the library of congress to be stored across individual participant's computers. This would ensure full data recoverability with high probability while limiting excess power consumption.

**Proof of elapsed time** was developed by Intel in 2016 to take advantage of their new chip architecture instruction set. Blockchain consensus from PoET comes from being able to make trusted processors wait a random amount of time before mining a block. IBM's blockchain *Hyperledger* uses PoET to enforce random block selection.

**Proof of reputation** is based on the reputation of the network participants. In this algorithm, nodes in the network are given voting power in creating new blocks or validating transactions based on their reputation. This reputation could be determined by various factors like the age of the node, its historic behavior, or the amount of work it has done for the network, among other things. The theory is that nodes with higher reputation would be more trustworthy and less likely to attempt malicious actions, similar to the concept of 'reputation' in many online platforms and marketplaces.

You can see where this is going. Bouraga (2021), for example, also mentions Proof-of-Luck, Proof-of-Vote, Proof-of-Disease, Proof-of-Play, and Proof-of-Learning. Anything you can code can be implemented as a consensus algorithm, although not necessarily well, and to the standard required of global networks that transmit value. There is a balance that needs to be met between performance -- collecting and processing transactions, security -- incentivising honest behaviour and preventing attacks, and decentralisation -- too centralised and we're back to big-tech. This three-pronged tradeoff is the **blockchain trilemma** and will be discussed in the next lecture on scaling.

## Decentralisation
Quick sidequest here::The last point in the trilemma - decentralisation - exists on a scale and is debatable, or subjective. We can summarize some of the features that distinguish a decentralised blockchain from a centralised pseudo-blockchain.

| | Centralized | Distributed (p2p) |
|---|---|---|
| **Structure** | Top-down; rules based | 1-node at a time; protocol based |
| **Membership** | Gatekeepers allow you to join and can expel/blacklist | Anyone can join (and leave) based on the protocol |
| **Consensus** | Voting and elections; democracy | Proofing methods: proof-of-work, proof-of-stake, etc.; meritocracy |
| **Robustness** | Fault-tolerant; no expected Byzantine actors | Fault and Byzantine tolerant |
| **Incentive structure** | Honesty enforced by legal structure of the corporation and therefore the state in which it operates | Honesty incentivised by some kind of reward (monetary, token, social, etc.) |
| **Examples** | banks, Facebook, governments | Bit-torrent, email, wikis* & the internet* |
| **Blockchain examples** | Enterprise blockchains: Hyperledger (IBM/Linux), Azure (Microsoft), Quorum (JP Morgan) | Bitcoin, Ethereum, etc. |
> Table: Centralized versus decentralized organizations and some of their features. *depending on your perspective

## What is a blockchain?
We are now in a position to pose a definition of a blockchain.

A blockchain is a distributed architecture that maintains a totally ordered list of transactions. To maintain the true state of the ledger, the protocol must have:
1. Strong Sybil Resistance, and
2. A Fork Choice Rule.

**Sybil Resistance** - Once the system is open and permissionless there is risk of entities joining that don't have the same incentives to stay honest as do regular network participants. (stick: lock stake/spend electricity, subject to slashing; carrot: rewards)(closed systems use permissions, and just have to replicate their database for CAP)

**Fork Choice Rule** determines how the network behaves in the presence of network partitions. We take network partitions as a certainty, we just don't know when or where the fault will occur that causes a partition, thus a consensus mechanism accounts for their presence. Two further conditions must be met when the network partitions:
  1. **Safety** is the state of updates being true. You can think of this as "Nothing bad has happened yet."
  2. **Liveness** is the guarantee of future updates. You can phrase this as "Something eventually happens."
     
If safety and liveness are met the network can continue to operate with some guarantee that it will maintain a source of truth. If the network is also sybil resistant, then it can be said the blockchain is Byzantine fault tolerant. (Recall from last lecture Byzantine behaviour is malicious behaviour by a node.)

The figure summarizes these properties: 
![image](https://github.com/millecodex/COMP842/assets/39792005/2b1f994c-0d64-4433-a178-2a2f56c418fa)


## Summary
Understanding consensus mechanisms in blockchain technology is crucial for building robust and decentralized systems. Proof of work style chains rely on a longest-chain rule for resolving network partitions (forks) while proof of stake style chains ues a mix of longest-chain, or committee-based voting styles. The work in proof of work is used to disincentivise bots from subverting the blockchain while locked stake can be subject to slashing in a PoS blockchain.

# What did we miss?
* We skipped a lot of the computer science details on how consensus methods work such as leader selection, transaction finality, timing assumptions, & fault tolerance guarantees.
* We have yet to get into the security element of blockchains in which we'll cover topics such as: 51%, sybil, nothing-at-stake, grinding, long-range, DDoS, ....

# Exercises
1. Choose an alternative consensus mechanisms (such as proof of space, or proof of elapsed time) and explain how it meets the requirements of a blockchain. How is it different compared to traditional mechanisms like proof-of-work and proof-of-stake.
2. If a blockchain is just a database, what is the significance of safety and liveness? Explain why both properties are important for maintaining the integrity and functionality of a blockchain network, especially in the presence of network partitions. What are the trade-offs between safety and liveness in different consensus algorithms?

# Readings
* PPCoin: Peer-to-Peer Crypto-Currency with Proof-of-Stake ([pdf](./papers/peercoin-paper.pdf))
* Ethereum's Whitepaper ([2014 pdf, historical](https://ethereum.org/669c9e2e2027310b6b3cdce6e1c52962/Ethereum_Whitepaper_-_Buterin_2014.pdf), current: https://ethereum.org/en/whitepaper/)
* Tendermint: Consensus without Mining ([pdf](./papers/tendermint.pdf))

# Resources
* Watch Lera Nikolaenko (a16z crypto research partner, super smart) given you the deep dive into Proof of Stake blockchains ([Youtube](https://www.youtube.com/watch?v=mZ-Ya7NRDxM))

# Next Lecture
* :point_right: [Network Scaling](5-scaling.md)

# References
1. Blocki, J. & Zhou, H.-S. (2016). Designing proof of human-work puzzles for cryptocurrency and beyond. In Theory of cryptography (pp. 517–546). Springer Berlin Heidelberg. [PDF](https://eprint.iacr.org/2016/145.pdf). [DOI](https://doi.org/10.1007/978-3-662-53644-5_20).
2. Bouraga, S. (2021). A taxonomy of blockchain consensus protocols: A survey and classification framework. *Expert Systems with Applications*, 168, 114384. [DOI](https://doi.org/10.1016/j.eswa.2020.114384)
3. Nijsse, J. & Litchfield, A. (2020). A taxonomy of blockchain consensus methods. Cryptography, 4, 1-15. [DOI](https://doi.org/10.3390/cryptography4040032)
