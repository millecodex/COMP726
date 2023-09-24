[↰ back](../../..)

# Lecture 9: Security
## Contents
1. [Blockchain Security Taxonomy](#blockchain-securitytaxonomy)
1. [What did we miss?](#what-did-we-miss)
1. [Further Reading - the very short list](#further-reading---the-very-short-list)
1. [Exercises](#exercises)

Divided into five layers, security of a blockchain involves being aware of different attacks from the infrastructure (hardware & physical security) to the social level (applications & phishing). This list is not exhaustive and only represents some of the main security considerations that must be made when evaluating blockchains. Not every attack mentioned will be described, but there is an excellent source for blockchains security considerations [here](https://hackn.gitbook.io/l1-security/).

# Blockchain Security Taxonomy
Taking inspiration from the blockchain tech stack, we will orgnaize the security threats according to layers:
1. [Infrastructure Layer Security](#1-infrastructure-layer-security)
2. [Data Layer Attacks](#2-data-layer-attacks)
3. [Network Layer Attacks](#3-network-layer-attacks)
4. [Protocol (Consensus) Layer Attacks](#4-protocol-consensus-layer-attacks)
5. [Application Layer Attacks](#5-application-layer-attacks)

## 1. Infrastructure Layer Security

| Blockchain | General |
|---------------------|--|
|  Validators (PoS) |  Routers   |
|  Nodes  (PoW) | Cloud Services |
|  Miners (PoW)  | Mobile Services |

The infrastructure layer involves the hardware components that build up the network. For blockchains this could mining hardware, node hardware, and their secure components, both physical and digital. Mining attacks are discussed below as part of consensus. We will exclude discussions on securing routers, validators, and the communication between them. Any cloud services will have a security policy for their services. Similarly, mobile services that run light clients or wallets will also use inherited security policy.

## 2. Data Layer Attacks

| Cryptographic       | Transaction Related     |
|---------------------|-------------------------|
|    Cryptanalysis    | Double Spending         | 
|  Hash Collision     | Transaction Malleability | 
|   Length Extension   | Time-Locked Transaction |

Cryptanalysis and various cryptographic attacks will not be discussed here as they apply in general and are not specific to blockchain networks.

### Double Spend Attack
A transaction replay, or a double-spend attack is a type of fraudulent activity in which digital coins are spent more than once. Should someone be able to double spend, this will undermine the integrity and trust in the network, making it crucial for blockchain networks to have mechanisms to prevent this type of attack.

PoW Mitigations:
* Confirmation Time: In PoW blockchains like Bitcoin, transactions are considered secure after several block confirmations. This makes it increasingly difficult for an attacker to reverse a transaction as they would need to redo the work for the confirmed blocks and catch up with the network's ongoing mining efforts.
* Economic Disincentives: Successfully executing a double-spend attack in a PoW system would require an attacker to control at least 51% of the network's hashing power. The cost of acquiring this much computational power makes such attacks economically unfeasible in well-established networks.
* Network Propagation: Transactions and blocks are rapidly propagated across the network, making it difficult for an attacker to propagate a fraudulent transaction without other network nodes becoming aware of the inconsistency.

PoS Mitigations:
* Slashing: validators are required to "stake" or lock up a significant amount of cryptocurrency as collateral. Malicious actions can result in the loss of this stake, creating a financial disincentive for double spending.
* Finality: introduce the concept of "finality," meaning that once a block has been confirmed to a certain degree, it can't be changed. This makes it impossible to double-spend without violating the protocol rules, which would lead to penalties.
* Long-range Attacks Prevention: PoS systems often implement mechanisms like checkpoints or other finality-enforcing techniques to prevent attackers from forking the blockchain far back in history to double-spend.

Transaction Malleability allows altering a transaction's ID without changing its effect, creating potential for fraud. Time-Locked Transactions execute after a condition is met but can be exploited to manipulate transaction order.

## 3. Network Layer Attacks

| P2P Components  | Data Integrity  | Resource Exhaustion | Routing & IPs  |
|-----------------|-----------------|---------------------|----------------|
| Sybil            | Eavesdropping   | Denial of Service   | BGP      |
| Eclipse         |                 |                       | Alien    |
|||                                                        | Timejacking     |

### DoS
A Denial of Service (DoS) attack aims to disrupt normal functioning by overwhelming the network with excessive requests or traffic. DoS attacks can manifest in various ways, such as flooding the network with invalid transactions, overloading node capacities, or targeting the consensus mechanism.

In Proof of Work (PoW) systems, two economic factors act as natural deterrents to DoS attacks:
* Transaction Fees: Each transaction requires a fee, which discourages attackers from flooding the network with numerous low-value or invalid transactions. The financial cost of such an attack would be prohibitively high.
* Cost of Hashpower: Miners invest in significant computational resources to participate in the network. To successfully launch a DoS attack, an adversary would need to outcompete these miners, requiring an impractically high investment in hashpower.

Preventive measures against DoS attacks include rate limiting to cap the number of requests from a single source and using a distributed architecture to make it harder for an attacker to target specific nodes. Additionally, decentralized peer discovery mechanisms can decrease the risk of DoS attacks by not relying on a central authority for network participation.

### Sybil
In a Sybil[^sybil] attack on a blockchain network, a single adversary controls multiple nodes, essentially creating a large number of fake identities. This can undermine mechanisms that rely on redundancy and trust. For example, in peer-to-peer blockchain networks, nodes often share information based on a mutual trust assumption. A Sybil attacker could disseminate false information, manipulate transactions, or undermine mechanisms that rely on redundancy and trust, such as routing between nodes or the formation of quorums in consensus algorithms.

[^sybil]: From the book "Sybil," published in 1973, which is about a young woman with a dissociative identity disorder. In the book, Sybil Dorsett, the main character, has multiple personalities as a result of childhood abuse. The term was adopted to describe attacks in computer networks where a single adversary controls multiple nodes, essentially creating multiple fake identities, much like Sybil Dorsett's multiple personalities. The concept of the Sybil attack was formalized in a 2002 paper by researcher John Douceur, and it has since become a fundamental concern in the field of network security, particularly in decentralized systems like peer-to-peer networks and blockchains.

In Proof of Work (PoW) blockchains, Sybil attacks are generally less effective because block creation is computationally expensive, and controlling a significant portion of the network's computational power is costly. Similarly, in Proof of Stake (PoS) systems, staking a significant amount of the cryptocurrency makes Sybil attacks expensive to execute.

However, in networks where reputation or simple node count matters, Sybil attacks can be more problematic. For instance, in networks using simple majority voting without a staking or computational component, a Sybil attacker can create a majority of nodes and have undue influence over the network.

Defenses against Sybil attacks often involve some form of validation that makes it expensive or cumbersome to create a large number of nodes, such as requiring some form of validation or introducing computational or financial costs to participate in network activities.

### Routing & Other
BGP, Alien, and Timejacking highlight some vulnerabilities in routing, and time synchronization across decentralized systems. BGP (Border Gateway Protocol) hijacking involves diverting internet traffic by falsely announcing IP spaces, potentially intercepting or tampering with data. Alien attacks focus on subverting the consensus in blockchain networks by exploiting network delays and out-of-order message delivery. Timejacking manipulates a node's perception of network time, causing discrepancies in block timestamps or transaction validation.

## 4. Protocol (Consensus) Layer Attacks

| Proof Mechanisms | Transaction Validation | Chain Manipulation   | Mining-Related      |
|------------------|------------------------|----------------------|---------------------|
| 51% (PoW)        | Race*                   | Long Range         | Selfish Mining      |
| $>\frac{1}{3}$ (PoS) | Finney*             |  Grinding           | Pool Hopping        |
| Nothing at Stake | One-Confirmation*       | Chain Re-org        |  Bribery            |
|                  |                         |                      | Block Discarding    |
|                  |                         |                      | Block Withholding   |
|                  |                         |                      | Fork After Withholding |
|                  |                         |                      | Uncle-Block   |

\* A type of double-spend attack

### 51% Attack
Should a single entity gain control of more than half of the hash power in the network, this could lead to a 51% attack. The attacker can't steal coins directly as this involves subverting elliptic curve cryptography. The attacker can, however, use their majority status in some interesting ways. At >50%, they have the ability to find more blocks and direct the consensus of the blockchain. The attacker can censor transactions by refusing to add blocks containing someone's address. This would be akin to blacklisting certain addresses but does not completely exclude them from being included in blocks mined by honest nodes (the 49%). As the proportion in control increases, it will be harder to get a blacklisted transaction published on the blockchain. With this majority, the attacker will now earn a larger proportion of block rewards but still have to find SHA256 hashes like everyone else.

The Proof-of-Stake equivallent to the 51% majority hashpower is the Byzantine Fault Tolerance limit which usually requires that at least 2/3rds of the validators must be honest for the network to function correctly. In BFT-based PoS systems, this means that an attacker would need to control more than 1/3rd of the total stake to compromise the network's safety properties, such as preventing agreement on the next valid block. In BFT systems like Tendermint or PoS Ethereum, the 2/3rd majority is crucial for achieving both safety and liveness properties. Safety ensures that nothing "bad" happens (e.g., double-spending), and liveness ensures that something "good" eventually happens (e.g., transactions get confirmed).

### Selfish Mining
An adversary doesn't necessarily need 51% of the hash power, but with a large number of nodes in the network, they could gain an advantage. An interesting analysis was published in 2014[^eyal] by Eyal and Sirer that showed a conglomerate of miners could form with as little as one-third of the hash power. This mining cartel can continuously mine without broadcasting their blocks until some set time in the future. In the short term, the miner is sacrificing the immediate block reward by not propagating their found blocks to neighboring nodes. In the long run, however, the result is that the honest miners are doing work that is not in competition with the selfish miners, increasing the attacker's expected rewards. The results of Eyal and Sirer's study conclude a group can increase their mining payout with as little as 1/3 of the network's hash power.

[^eyal]: Eyal, I., & Sirer, E. G. (2014). Majority is not enough: Bitcoin mining is vulnerable.

### Nothing at Stake
Given a fork in a proof of stake system, the user is incentivized to build on every branch. In a proof of work system, the user has a finite amount of hashpower that is most profitable if used to build on the main chain. This constraint is gone in a pure proof of stake system as the user can bid for blocks on any and all branches. The probability of finding a block remains constant. Here, the blockchain may never reach consensus as everyone is scrambling to build blocks rather than maintain the longest chain (BitFury, 2015).

A simple solution is to penalize someone who publishes blocks on multiple branches. This is known as slashing and acts as a disincentive to build on non-consensus chains.

### Short and Long Range Attacks
A Long Range attack involves rebuilding a blockchain from scratch with the intention of overtaking main-chain consensus. A user with enough computational power could accomplish this easier than the same attack on a proof of work chain. To prevent an attacker from building a long competing chain, milestones can be reached along the way that act as finality checkpoints. Going back in time before a checkpoint is not possible as any other branches, including the potential attack, would be pruned. Ethereum uses validator nodes that vote on checkpoint blocks within an epoch.

In the short term, an attacker can attempt a double-spend by incentivizing participants to build on an orphaned chain as soon as a malicious transaction is broadcast. This is done secretly. If the alternate chain succeeds in overtaking the main chain, the double spend was successful. Basically, miners can be bribed to compete on the alternate chain, and this will be profitable up to the value of the double spend. Similar to the Nothing at Stake problem, a short-range attacker is penalized by slashing or revocation of validation privileges.

### Grinding Attack
In a grinding attack, the attacker increases their probability of being selected for block minting. For example, a validator could iterate through many combinations of block parameters searching for a favorable one to get published. Given enough computing power, the attacker could always "find" a suitable block. A general mitigation measure for this is to use a source of randomness that cannot be known in advance, like a random function that uses seeds from a group of validators. Of course, the validators could work together and collude. Workarounds for this can be found in Ethereum's Proof of Stake FAQ.

## 5. Application Layer Attacks

| User Interface           | Smart Contracts                 | Social  |
|--------------------------|---------------------------------|----------------------|
| Phishing                 | Reentrancy                      | Social Engineering   |
| Multi-Signature          | Front-Running / MEV             | Rug Pull           |
| Weak Randomness          | Uninitialized Storage Pointers  | Decentralisation   |
|                           | Integer Overflow/Underflow     | Regulatory Risks    |  
|                           |Timestamp Dependence            |                        |

### Smart Contracts
As the industry matures and well known SC exploits are learned from a number of best practices emerge. See the [smart contract security field guide](https://scsfg.io/hackers/) for best practices in smart contract development.

#### DAO Hack
The most famous smart contract exploit is the Ethereum **DAO hack** that took place in 2016 when a hacker drained US $50 million from a [fundraising account](https://www.gemini.com/cryptopedia/the-dao-hack-makerdao#section-the-dao-hack-remedy-forks-ethereum). Here is some logic from the attack:

```solidity
contract donateDAO {
    mapping (address => uint256) public credit;

    // add funds to the contract
    function donate(address to) payable {
        credit[msg.sender] += msg.value;
    }

    // show ether credited to address
    function assignedCredit(address) returns (uint) {
        return credit[msg.sender];
    }

    // withdrawal ether from contract
    function withdraw(uint amount) {
        if (credit[msg.sender] >= amount) {
            msg.sender.call.value(amount)();
            credit[msg.sender] -= amount;
        }
    }
}
```

The problem is in the `withdraw()` function. In line 17, `call.value()` sends funds, in this case to the sender, before updating the balance. Here, the hacker can request their funds back, and then a fallback function triggers a recursive call that keeps sending funds back without updating the balance[^Humiston2018]. The **reentrancy** attack took advantage of the fact that the smart contract logic allowed external calls to untrusted contracts before the internal state was updated. In simple terms, the attacker was able to repeatedly "re-enter" the smart contract and drain funds before the contract had a chance to update its internal record of withdrawals. This resulted in a substantial portion of the DAO's funds being siphoned off by the attacker.

[^Humiston2018]: Humiston, I. (2018). Attacks and Incidents. In Ethereum Smart Contract Development (pp. 81-94). Apress.

#### MEV
MEV refers to the maximum value that can be extracted from transaction reordering, transaction inclusion, and transaction censorship by validators within a block. Essentially, it quantifies the financial incentives for validators to deviate from the "honest" behavior expected of them. In Ethereum validators have the authority to choose the transactions that will be included in the next block. Because transactions pay fees to validators for their inclusion in a block, validators naturally prioritize transactions offering higher fees. However, the ability to choose transactions and their ordering within a block creates opportunities for MEV.

Validators can strategically reorder transactions to take advantage of arbitrage opportunities or even [front-run](https://hacken.io/discover/front-running/) specific transactions. Front-running involves placing a transaction ahead of another transaction in a block to take advantage of some profitable condition before the latter transaction can be executed. For example, if a trader is about to buy a large amount of a particular token, which is expected to increase the token price, a front-running validator can buy the token first and sell it after the trader's purchase, thereby making a profit.

Although mentioned here in the context of security, MEV is more of a consequence of the nature of fee market transactions in a decentralised system, rather than malicious behaviour.

### Exchanges & Scams
The list of hacks and breaches of cryptocurrency exchanges is long and colorful. A sampling can be found [here](https://www.hedgewithcrypto.com/cryptocurrency-exchange-hacks/) and includes a New Zealand (Christchurch based) company _Cryptopia_.

Outright scams are also prominent as Bitcoin becomes popular and increases in value, many 'alternatives' make the rounds promising massive gains and better features. The OneCoin scam was recently popularized in the excellent BBC podcast series _The Missing Queen_ by Jamie Bartlett. Episodes available [here](https://www.bbc.co.uk/programmes/p07nkd84/episodes/downloads). Often these types of scams are called **Rug Pulls** as the founders or one of the founders decides to abscond with user funds, often leaving nothing more than a trail of transaction history for victims to search.

### Mining Centralisation
The main practical threat to a single entity controlling the majority of the hashpower is that it will lead to centralization and cause users to abandon the system altogether. Once hashpower gets close to this threshold it is also possible that developers will step in and update the software to limit this behaviour. It is unknown how this will play out in the future. Thus far the bitcoin network has been relatively decentralized, but a few mega mining pools have emerged. There have been some cases of 51% attacks on alternative cryptocurrencies such as Verge, Horizen, and Vertcoin. Smaller cryptocurrencies are more vulnerable to a large mining pool shifting their resources for this purpose. See Case Studies (next).

# Case Studies (🏗️ Under Construction 👷‍♀️)
* Verge 
* Horizon
* Vertcoin

# What did we miss?
* There are a number of mining-related attacks; most of which are theoretical for Bitcoin because of its decentralisation and large network hashpower, but could be more practicle for smaller PoW based cryptocurrencies.

# Further Reading - the very short list
* Blockchain Security Vulnerabilities by Hackn https://hackn.gitbook.io/l1-security/ 

# Exercises
1. To be posted.

# Resources
* Watch Lera Nikolaenko (a16z crypto research partner, super smart) given you the deep dive into Proof of Stake blockchain attacks ([Youtube](https://youtu.be/-uxHoEfxXC4))

# Video Lecture
To be posted.
