[↰ back](../../..)

# Lecture 5: Scaling
## Contents
1. [Blockchain Stack](#blockchain-stack)
2. [The Trilemma](#the-trilemma)
3. [Scalability](#scalability)
4. [Storage](#storage)
5. [State Channels](#state-channels)
6. [Side Chains](#side-chains)
7. [What did we miss?](#what-did-we-miss)
8. [Further Reading - the very short list](#further-reading---the-very-short-list)
9. [Exercises](#exercises)

## Blockchain Stack
A technology stack is a model to represent the sections and subsections of a complex system. A classic example can be seen in the internet. Underneath the application that we interface with there are many sub-layers to the entire technology. The internet standard defines four layers: application, transport, internet, and link[^1^]. Contrast this with the stack from[^2^] that has five divisions. There is no first-principles based ordering to the stack, and one may have more or fewer layers if sufficient to describe the system. This has been inspired by the OSI model (Open Systems Interconnection, see [link](https://en.wikipedia.org/wiki/OSI_model)).

> [^1^]: Braden1989
> [^2^]: Stallings2007

|   | Internet STD 3 |   |   | Stallings (text) |   | Example            |
|---|----------------|---|---|------------------|---|---------------------|
| 4 | Application    |   | 5 | Application      |   | HTTP/FTP           |
| 3 | Transport      |   | 4 | Transport        |   | TCP/UDP            |
| 2 | Internet       |   | 3 | Internet         |   | IPv6               |
| 1 | Link           |   | 2 | Network Access   |   | MAC addressing     |
|   |                |   | 1 | Physical         |   | Integrated circuit |
> Table: The internet standard technology stack as defined by the Internet Engineering Task Force has 4 layers. Others could have different layers, Stallings includes Physical as Level 1.

The blockchain stack also has various definitions with many of them excluding the base layers 1 and 2 of internet; these are assumed. At Level 1 sits consensus, the rules that maintain the ledger. Some kind of network infrastructure is required for consensus to run atop, such as HTTP gateway access and gossip protocol message passing. Level 2 has broad usage and could refer to payment channels such as the lightning network, storage optimisation like sharding, or secondary chains that interact with a main chain. Beyond this is even more diffuse, but generally there must be an application layer on top.

| Bitcoin |   | Ethereum |     | Example          |
|---------|---|----------|-----|------------------|
|         |   | Dapps    | 4   | Stable Coins     |
| Appl    |   | ication  | 3   | Smart Contracts  |
| `Layer 2` |   |          | 2   | Payment Channels |
| Consen  |   | sus      | 1   | Proof of Work    |
| Network |   |          | 0   | Gossip Protocol  |
| Physical |  |          | -1  | ASICs            |
> Table: The blockchain technology stack generally begins with consensus as the base, layer 2 has various scaling improvements, and applications are on top.

The main criticism of Bitcoin is that the network has a limit on throughput; the number of transactions that get recorded in the ledger is difficult to scale. Good security and decentralisation come at the expense of scalability.



## The Trilemma

> <img width="400" alt="The blockchain trilemma: pick any two ideal properties at the risk of sacrificing the third." src="https://github.com/millecodex/COMP842/assets/39792005/7489c108-9d92-47c0-8b26-94f8a0920163">\
> Figure: The blockchain trilemma: pick any two ideal properties at the risk of sacrificing the third.


## Scalability
Two design decisions fundamentally limit the number of transactions the network can process: the block-time and the block-size, hard-coded to ten minutes and 1 MB. Each block in bitcoin is 1 MB, or 1,000,000 bytes and the average transaction size is 580 bytes so $\frac{1000000}{580}=1724$ standard transactions per block. The average block time is 576 seconds[^1] and so 
$\text{throughput }=\frac{1724}{576}=2.998\text{ transactions per second.}$

[^1]: 600s is the theoretical blocktime, in practice blocks have been mined on average every 576 seconds in the past two years.


In a global network there must be time for a 1  MB block to flood the network, allowing for consensus, before the subsequent block is found. These two properties dictate a trade-off and in Bitcoin's case limit the capacity to around 3 transactions per second. For a global payments system this is orders of magnitude smaller than it needs to be[^2].

[^2]: The VISA network averages over 1,700 transactions per second with rumoured peaks of 100,000 during singles day in China; comparatively PayPal averaged 241 TPS in 2017.~\cite{website:PayPal, website:VISA}

An economy with blockchain components will require tens of thousands TPS. In addition to global payments consider a few use-cases:
- Credits in a state sponsored system - millions of citizens using services like ID verification, licensing, or voting.
- Tokenized value exchange - electricity credits moving from solar generation to national grid: smart grids or managed between electric cars and a grid.
- Micro subscription services - paying for video content on a per-second basis or per-share on social media.
- IoT in general is poised to require orders of magnitude more data-exchange.

TPS is one factor in the scaling debate and many solutions have been proposed such as Schnorr signatures, sharding, Merkelized Abstract Syntax Trees, and Segregated Witness[^segwit]. These improvements are considered may require the software code base to be upgraded and possibly forked and sit at layer 2 in the stack; not altering consensus but improving the application layer. 
[^segwit]: Segregated witness, known as *Segwit*, is partially implemented; https://en.wikipedia.org/wiki/Bitcoin_scalability_problem



## Storage
### Segregated Witness
This backwards compatible software upgrade separates witness data from the list of transaction inputs. A bitcoin transaction has a witness, or digital signature, attached to it that must be verified for it to be spent in the future. Segregating this part makes room for more transactions in a block without affecting the transactions themselves because the inputs and outputs are preserved and the signatures (witness) are kept in another tree. Antonopoulos (2017, p. 170) lists several advantages of Segwit including network and storage scaling (Antonopoulos, 2017). Segwit transactions introduced a weighting limit rather than a size limit which means more can fit into a block. The result is an approximate doubling in block size from 1 MB to 2 MB and throughput from $\approx$3 to $\approx$6 TPS.

The other variable in our equation -- block time -- can be reduced but at the expense of latency. Doubling the block size will result in double the time for the block to propagate through the network. If block propagation time exceeds or comes near to the time needed to mine a new block then the network will fork and be unable to achieve consensus.


### Sharding
Sharding takes its name from replicated hardware: A **S**ystem for **H**ighly **A**vailable **R**eplicated **D**ata, but simply splits a data-table horizontally to allow for smaller index size. Sharding leads to a hierarchical, and perhaps less decentralized, structure, seen in myriad natural and social systems. Systems by Google, for example Spanner (Corbett, 2012) and BigTable are databases with automatic fail-over and re-sharding for load balancing.

Blockchains can also be sharded and current projects include Elastico, Rapidchain, OmniLedger, and of course, Ethereum's Casper. Every node in a standard blockchain stores a copy of the entire ledger and validates all activity. Partitioning the ledger into parent/child shards, or even horizontally, can improve scalability. Given enough nodes to validate a portion of the ledger it can remain relatively secure. Each shard will manage its own history and only be updated if required. The downside is that decentralization erodes with more shards added to the network.

## State Channels
A state channel is a communication rail that is opened between a main chain and an intermediary. This allows you to transact with the intermediary and occasionally as required settle on the main chain. Communication can be two-way such that you can send and receive via the intermediary given that appropriate constraints are met (like enough funds).

The present idea with the most promise for increasing throughput operates as an intermediary that maintains contact with the main chain is called the Lightning Network.

### Lightning Network
The lightning network represents an off-chain scaling solution for Bitcoin because the functionality occurs in a separate network with only the endpoints connecting to the Bitcoin blockchain. All the transacting happens in the middle between lightning nodes that don't need to write to the blockchain.

Imagine three friends go to dinner and one person pays the bill. The next day the two friends that did not pay work together and so one person, *Alice*, gives their portion to their co-worker, who will see the bill-payer later that night. In this simple scenario Alice did not have a direct link to the payer and so gave their cash to an intermediary. If everyone is friends, then their trust is maintaining order and the co-worker is doing a favour by passing along the cash. Another way to frame the transaction is that the co-worker has borrowed from Alice and lent to the payer. Viewed this way, any two parties are not settled: co-worker owes Alice, payer owes co-worker, and Alice still owes payer from dinner, but taken together everyone is happy. Additionally, if Alice goes to lots of dinners with friends, they may all want to contribute a set amount to a pool and only settle every couple of months. 

The lightning network allows Alice to make payments to parties she does not have a direct link with. First she must open a payment channel which is a bi-directional commitment of funds. If Alice and Bob have a channel this means that Alice can only pay Bob. However, if Bob has a separate channel with a third party, then Bob can act as a router and transfer Alice's payment to Carol. Bob will receive a small fee for his efforts in forwarding payment.

> <img width="479" alt="Lightning network: A path of four payment channels between five nodes in a second layer network as described by Antonopoulos" src="https://github.com/millecodex/COMP842/assets/39792005/620695d8-ef05-4b71-9489-25f74da6bfd2">\
> Figure: A path of four payment channels between five nodes in a second layer network as described by Antonopoulos (2017, p.315).


If Alice and Bob each commit 2 coins, their channel has a total capacity of 4. They cannot commit more than 2 coins to a transaction because then one party would be at risk of loss. For Alice to pay Eric 1 coin, she will first need an invoice from Eric for payment. Eric's invoice will contain a hashed-secret that is stored by nodes along the way and used to redeem their fees. There is a separate part of the network that keeps track of what nodes are in the network and this allows for Alice to have directions to Eric. Next, Alice creates a transaction to Bob and includes a bit extra to pay the intermediary nodes, along with the hashed-secret. If Bob knows the secret, he can redeem the full amount. Next Bob will create a *new* transaction with Carol using the funds in his separate Bob-Carol channel, but with the details he received from Alice. Part of this will include 0.002 fee for the upcoming nodes. Note Bob's balance here: 2 coins in his Alice-Bob channel and 0.998 coins in his Bob-Carol channel. These are steps 2-3 in figure [^fig:ln2].

> <img width="481" alt="Lightning network: Details for Alice to indirectly pay Eric" src="https://github.com/millecodex/COMP842/assets/39792005/0f6e58da-efc8-46bc-a459-c73adeac94f6">\
> Figure: Details for Alice to indirectly pay Eric. Source: (Antonopoulos p.316, 2017).

Following along the example in Antonopolous, when Eric receives payment from Diana, he has the secret to unlock the funds in the transaction and receive the 1 coin he originally invoiced Alice for. The secret will propagate back through the nodes, unlocking everyone's commitment. At the end, Bob, Carol, and Diana all have earned a fee of 0.001 coins. There is no additional blockchain here and so there is no wait time for blocks to be mined or confirmed. These lightning transactions happen at network speed and are promising for merchants that want to offer goods and services using cryptocurrency.

At some point Alice will want to settle the dinner party transactions between her friends and this is when she will close her channel with Bob and write their remaining balances back to the blockchain. Both Bob and Alice need to agree on this using a multi-sig transaction. Decreasing the frequency of settlement with the main chain is beneficial by reducing fees, decreasing confirmation time, and increasing overall volume of transactions.

Various off-chain or *second-layer* solutions exist for other blockchains as well: [Raiden](https://raiden.network/) for Ethereum, and Trinity for NEO. These networks add a settlement layer to the system to increase capacity but they still must only transact within the constraints of the original design.



## Side Chains
Side chains are separate blockchains that can interact with a main chain. Interoperability is when two chains can exchange messages and tokens. If value is transferred away from chain A and appear on chain B then it must be settled on chain A and cannot reappear.

This is different from a state channel where the off-chain transacting happens at network speed without the constraints of consensus inherited from the main chain. A side chain is subject to its own (new) design consensus rules. Plasma and Polkadot are example side chain projects. Plasma is a proposal to interact with Ethereum (in addition to Raiden) and Polkadot was conceived by Gavin Wood (co-founder of Ethereum) as a stand alone chain (Wood, 2017). Wood summarizes the approach:

> Scalability is addressed through a divide-and-conquer approach to [security and transport], scaling out of its bonded core through the incentivisation of untrusted public nodes. The heterogeneous nature of this architecture enables many highly divergent types of consensus systems interoperating in a trustless, fully decentralised "federation", allowing open and closed networks to have trust-free access to each other.

The benefit of using a side chain is that you can have enhanced properties such as faster timing or lower fees and then only settle transactions on the main chain when necessary. The risk is that you are essentially outsourcing some portion of the protocol.

## What did we miss?

## Further Reading - the very short list

## Exercises

