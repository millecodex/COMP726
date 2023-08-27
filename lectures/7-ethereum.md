[↰ back](../../..)

# Lecture 7: Ethereum
## Contents
1. [Motivation](#motivation)
2. [ICO](#initial-coin-offering)
3. [Smart Contracts](#smart-contracts)
4. [Ethereum Architecture](#ethereum-architecture)
6. [Consensus](#consensus-from-poS-to-poW)
5. [Ethereum Virtual Machine](#ethereum-virtual-machine)
3. [Applications](#applications)
4. [Characteristics and Quirks](#characteristics-and-quirks)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

# Motivation
### What was the problem that Vitalik Buterin was looking to solve?
Bitcoin provided a solution to the double-spend problem of creating digital cash by using proof-of-work mining to both maintain the state of the ledger and allow open participation in the network based on computing power. By assigning value to these digitally scarce coins the ledger can be used as a monetary system. This works great for money but comes up short when using Bitcoin's scripting language to make simple extensions such as a decentralized exchange -- how to determine the NZD/BTC rate? or how to do some arbitrary calculation, e.g. what is the probability that your game character encounters a villan?

In late 2013, While writing for *Bitcoin Weekly* and co-founding [*Bitcoin Magazine*](https://bitcoinmagazine.com/),  a nineteen-year-old Russian-Canadian computer science dropout, Vitalik saw the limitations in Bitcoin as an opportunity to create a new blockchain from scratch that can allow developers to build general applications. The first feature to include in this new blockchain was *Turing completness*. In computer programming this means it is possible to have loops in the code which would be necessary, for example, for calculating a probability or the value of π. Bicoin's *script* language is not considered Turing complete because it is stack-based and therefore anything that is needed by the program must be loaded onto the stack. (Also, by definition stacks cannot loop.) If you want to do something that isn't already available in the opcodes, then some very creative ad-hoc programming and second-layer work may be required. Turing-complete refers to a class of computers (programming languages) that can simulate another computer. Named after computer scientist Alan Turing[^Turing], a more practical way of thinking of Turing-completeness is that the language has loops; structures that allow for computation. HTML is not Turing-complete as it cannot calculate digits of π, whereas most programming languages are. Bitcoin's scripting language is not Turing-complete.

[^Turing]: The same namesake as the Turing test in which an artificial intelligence can convince a human they are human. Or, in other words, the human cannot tell if the terminal is answering on behalf of a human or AI.

The second feature was to use an account-based system. The benefit of this style is that each account (address) has a balance *and* the option of some code and storage. (This is in contrast to Bitcoin that uses a UTXO model that only keeps track of coins and not any additional data or code.)

The whitepaper for *Ethereum* was published online in 2013 and a year later a formal specification was written by Gavin Wood and the project raised funds through their initial coin offering. This was followed by the network launch in 2015.

Summarizing Ethereum from the whitepaper[^Buterin2014]:
> [Ethereum] is essentially the ultimate abstract foundational layer: a blockchain with a built-in Turing-complete programming language, allowing anyone to write smart contracts and decentralized applications where they can create their own arbitrary rules for ownership, transaction formats, and state transition functions.

[^Buterin2014]: Buterin, V. (2014). Ethereum: A next-generation smart contract and decentralized application platform.

## Initial Coin Offering
In order to fund their new proposed blockchain network, the founders embarked on a unique [fundraising scheme](https://blog.ethereum.org/2014/07/22/launching-the-ether-sale/) that laid down the template for future crowdfunding sales. An initial coin offering (ICO) seeks to bootstrap user adoption and funding by combining the style of an initial public offering (IPO) with a crowd fund model. A marked difference from the IPO model is that the token sale was open to anyone without geographic or regulatory restriction. All users had to do to participate was deposit bitcoin and receive *ether* tokens that represent their stake in the new network. The token sale was successful resulting in more than 50 million ether (the native currency of ethereum) being sold. Investors were aware of the token distribution from the beginning which included 9.9% of the tokens reserved for the founders (to fund development, salaries, bug bounties, etc.) and another 9.9% for a [foundation](https://ethereum.foundation/) that was set up to guide the long term mission of the network. These tokens didn't have to be purchased in a traditional sense; a practice now known as *pre-mining*.

### ICO Boom Times
The success of Ethereum's ICO and its smart contract capability combined with its open source code made it an ideal model for other founders to fund their projects. A new project could easily copy and modify smart contract code and host their own ICO and issue their own new ERC-20 tokens. (ERC-20 refers to the token standard that most coins that run on Ethereum use.) 2017--2018 was a boom period for ICOs with many projects and tokens launching. Unfortunately many of them had questionable products and practices or were outright scams and because there was no regulation in crypto (as there is for an IPO), there was no recourse for those that invested and lost their money. 

## Smart Contracts
The term *smart contract* refers to some executable code that lives on the blockchain. This code may be a snippet, small or large, it may be straightforward or complex, it may contain bugs, not compile, it may never even be executed. Ethereum allows for code to be stored on the blockchain in *contracts* which have a callable address that looks just like a user's address. All of these bits of code are generically called smart contracts. Pedants will like to tell you that they are not smart nor are they contractual and they might be right in a traditional sense, however, the term has come to be redefined in a blockchain context.

Earlier we mentioned that Ethereum is turing-complete, and here is where that comes in. A developer can write a program, say to issue crop insurance based on weather data, and store this program in a smart contract on the blockchain. As the blockchain is immutable this code will live there forever, it is also visible and thus can be easily verified or audited. The only limits to the applications that can be deployed on Ethereum come from the creativity & skill of the developer, and the amount of computation that program needs to do. Solidity is the name of most common high-level language used to write code that compiles to bytecode to be executed on the Ethereum virtual machine. Created by the co-founder of Ethereum, Gavin Wood, Solidity was intended to resemble JavaScript and be recognizable to web developers.

**Example Contract 1**
Here is an example from *Mastering Ethereum* (Antonopoulos, 2019) to create a faucet which will give out ether[^2] to anyone that interacts with it.

```solidity
// Our first contract is a faucet!
contract Faucet {
    // Give out ether to anyone who asks
    function withdraw(uint withdraw_amount) public {
        
        // Limit withdrawal amount
        require(withdraw_amount <= 100000000000000000);
        
        // Send the amount to the address that requested it
        msg.sender.transfer(withdraw_amount);
    }
    // Accept any incoming amount
    function () public payable {}
}
```

[^2]: Ether (ETH) is the currency used on the Ethereum platform. Gas is the name for the fees that the network will charge to execute contracts, this is priced in very small amounts of ETH.

**Example Contract 2**
A more substantial example is taken from the [solidity documentation](https://solidity.readthedocs.io/en/v0.4.24/introduction-to-smart-contracts.html) and details some functions of a simple cryptocurrency:

```solidity
pragma solidity ^0.4.21;

contract Coin {
    // The keyword "public" makes those variables
    // readable from outside.
    address public minter;
    mapping (address => uint) public balances;

    // Events allow light clients to react on
    // changes efficiently.
    event Sent(address from, address to, uint amount);

    // This is the constructor whose code is
    // run only when the contract is created.
    function Coin() public {
        minter = msg.sender;
    }

    function mint(address receiver, uint amount) public {
        if (msg.sender != minter) return;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}
```

**Example Contract 3**
The Ethereum DAO hack took place in 2016 when a hacker drained US $50 million from a [fundraising account](https://daohub.org/). Here is some logic from the attack:

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

The problem is in the `withdraw()` function. In line 17, `call.value()` sends funds, in this case to the sender, before updating the balance. Here, the hacker can request their funds back, and then a fallback function triggers a recursive call that keeps sending funds back without updating the balance[^Humiston2018].

[^Humiston2018]: Humiston, I. (2018). Attacks and Incidents. In Ethereum Smart Contract Development (pp. 81-94). Apress.

### Gas
Computation occurs in the EVM (Ethereum virtual machine) and we will be light on details, but because its a blockchain, all the nodes need to have a copy of the data and verify any updates. This includes running *all* smart contracts and doing *any* calculation. A scenario could arise, either accidentally or maliciously, to halt the network by deploying a contract with an infinite loop:
```
int i=1
while i>0
  i=i+1
 ```
The simple code above continually updates the counter because the stop condition of $i$ being less than or equal to $0$ is never met. To avoid this scenario all computation in the EVM needs gas. As a contract is executed gas is consumed and if the contract runs out of the gas then the update fails. All gas is paid in ether (`ETH`) and goes to the nodes that perform the calculations. A follow up question is what if I am wealthy and have enough gas to spam the network in this manner? To prevent this there is a gas limit on all transactions that is calculated based on how busy the network is. The  *London* upgrade to Ethereum changed the way that gas is distributed. Previously the miner would be compensated by receiving the entire gas fee in the transaction. Now, part of this fee is *burned*, and the validator gets the remainder. Burning some ETH offsets the overall issuance.


# Ethereum Architecture
Looking at Ethereum from an individual node point of view there are three main clients that work together to (a) maintain consensus and (b) update the state.
> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/fa95396b-7bad-4e43-982a-770405ab08a7">\
> Architecture of an Ethereum node, i.e. Geth, Parity, showing three main clients: Validator, Consensus (Beacon chain), and Execution (EVM). Modified from: https://eth-docker.net/

## Consensus: From PoS to PoW
On September 15, 2022, the Ethereum network executed "[The Merge](https://ethereum.org/en/roadmap/merge/)" which transferred consensus from the main chain that was operating by proof of work to the beacon chain that was running (in parallel) proof of stake. It was always the ethos of the Ethereum community to transition the network to a fully stake-based validation mechanism. What was unknown at the time was how hard it would be; it took developers ~7 years to do it. 

> <img width="600" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/047defb2-1617-4449-b2e2-c6a3fc31f749">\
> Tweet: Tick-tock next block. The network switched consensus methods without missing a block. Source: https://twitter.com/pcaversaccio/status/1591744307215605764 

In a PoS system consensus is handled by validators that maintain skin in the game by contributing a stake in ether and are rewarded in a similar fashion to miners. A validator's rewards are proportional to their stake in the system. The rules of the game dictate the validators must not be able to cheaply spam the network with multiple identities (Sybil resistance), which is enforced by a known list of validators with rewards in proportion to total stake. So multiple entites can join, but you must have >32 ETC to do so. 

> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/24925a07-ad77-46cc-a6d6-132359547d39">\
> Figure: Ethereum consensus enforces sybil resistance by slashing penalties, and uses committee voting to determing the chain-head.

## Beacon Chain
The beacon chain launched at the end of 2020 to act as the proof of stake consensus chain alongside the proof of work chain. It is now the 'main' Ethereum chain. Forks in Ethereum are resolved through voting. Block ordering is done by collecting attestations on each block as to whether or not it is the 'chain-head'. Block proposers are selected in a BFT-style leader election process, and finality is determined by validator voting on checkpoints. There is 1 check point in each epoch (32 slots). There is 1 block proposer and block per slot. Supermajority, or greater than 2/3 of the votes are required for selecting the chain-head[^LMDGHOST] and the epoch check-point. This means that up to 1/3 can be malicious. Each block takes 12 seconds to be published, and thus each epoch is $12*32=384$ seconds, or 6:24.

[^LMDGHOST]: The name of the fork-choice rule algorithm. The acryonym stands for Latest Message Driven Greediest Heaviest Observed SubTree. Read the paper: Combining GHOST and Casper https://arxiv.org/pdf/2003.03052.pdf

Once the beacon chain decides on the chain-head and has a block proposer, the node has 12 seconds to execute transactions and advance the state before publishing the updated block. The block is propagated by sending it out through the network gossip protocol. Executing transactions means it will process all the smart contract code, deploy new contracts, and update account balances. These are all handled by the Ethereum Virtual Machine.

## Ethereum Virtual Machine
### VMs
Virtual machines (VMs) in computer science are emulations of a computer system that provide the functionality of a physical computer, operating on the basis of a host system and creating a separate environment known as the guest system. The main purpose of a VM is to enable multiple operating systems to share the same physical hardware resources, promoting flexibility and isolation for applications such as testing and development. 

```bash
VBoxHeadless --startvm "My_VM"
VBoxManage createvm --name "my_blockchain_vm" --register
VBoxManage modifyvm "my_blockchain_vm" --memory 1024 --acpi on --boot1 dvd
VBoxManage createhd --filename "my_blockchain_vm.vdi" --size 10000
VBoxManage storagectl "my_blockchain_vm" --name "IDE Controller" --add ide
VBoxManage storageattach "my_blockchain_vm" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "my_blockchain_vm.vdi"
VBoxManage storageattach "my_blockchain_vm" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium /path/to/iso
VBoxHeadless --startvm "my_blockchain_vm"
```
> Bash commands to spin up a VM in linux: register, allocate 1 GB memory, 10 GB disc space, and point to the OS

This concept of emulation is shared with the **EVM**, although they serve different purposes. While regular VMs simulate physical hardware, the EVM is a virtual runtime environment designed specifically for executing smart contracts on the Ethereum blockchain. The EVM operates independently of the underlying hardware, ensuring deterministic computation that yields the same result across all network nodes. Each full node runs a copy of the EVM to verify transactions and smart contract executions, playing a crucial role in the decentralisation and security of the Ethereum network.

> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/9c3de5ff-de3f-44e9-bbb7-6a80abf43e4d">\
> Figure: Ethereum EVM shown in the inner box (execution cycle) determines the next state. Source: https://github.com/4c656554/BlockchainIllustrations/ 



-------------------
## Applications
### So what are people doing with this decentralised state machine?
 Decentralised applications, or *dapps* just refer to smart contracts that are executed on a blockchain. When combined with a frontend these dapps can appear just like any other web application with the key difference being that that code and/or user data is stored on the blockchain. 

The [most used dapps](https://dappradar.com/rankings/protocol/ethereum) on Ethereum in 2023 ranked by Unique active wallets (UaW):

| App            | Category                | UaW (k/30 days) |
|:-------------  |:-----                   |-------:|
| Uniswap        |  Decentralised Exchange |    495 |
| MetaMask Swap  |  Decentralised Exchange |    85 |
| OpenSea        |  NFT Marketplace        |    81 |
| Simple FX        |  Decentralised Finance |  80    |
| Ox Protocol     |Decentralised Exchange| 62 |

This list is dominated by DEX activity, so if we [rank](https://dappradar.com/rankings/defi?range=24h) by total value locked (TVL)[^caution]:
| App            | Category                | TVL ($B) |
|:-------------  |:-----                   |-------:|
| Lido            |  Ethereum Staking         |   13.8  |
| Summer.fi        |    Decentralised Finance | 6.1    |
| Maker DAO        |  Stablecoin             |   4.9  |
| Uniswap        |  Decentralised Exchange | 3.2    |
| Aave            |  Decentralised Lending |   2.6  |

[^caution]: Take these stats with some salt, I haven't looked into dappradar's methodology, and they are only representative as of August, 2023. Generally over the past few years, Maker, Uniswap, Aave, Curve have been relatively stable and popular protocols. 

-------------------
# Characteristics and Quirks
* Difficulty Bomb: Also known as the "Ice Age," the Ethereum network has a built-in difficulty bomb designed to make mining exponentially more challenging over time. This was originally introduced to motivate the network to transition from Proof of Work (PoW) to Proof of Stake (PoS). It's a fascinating mechanic that's deeply rooted in the network's consensus strategy.
* The DAO hack was an important event in Ethereum's history. There was a bug, and a lot of money was lost, but then the *immutable* blockchain was rolled back, the community split, now there still exists Ethereum Classic (ETC) and an ongoing question over the decentralised nature of Ethereum. See Laura Shin's book [The Cryptoptians](https://laurashin.com/book/) for an excellent accounting of the events.
* Self-Destruct and Resurrection: A quirky feature in Solidity is the selfdestruct function. When a contract self-destructs, it can send its remaining Ether to another address. Interestingly, if someone sends Ether to a self-destructed contract's address, and a new contract is created at the same address, the new contract will have the Ether sent to the "dead" contract. This resurrection quirk has potential security implications.
* Uncle Blocks: Unlike other blockchain systems, Ethereum incorporates a mechanism to reward stale blocks, referred to as "uncle" blocks. (Bitcoin calls them orphans.) These are blocks that are valid but not included in the main blockchain. This promotes network security and inclusiveness by providing incentives for miners even if their mined blocks are not included in the main chain.

# What did we miss?
* MEV
* zkEVM

# Further Reading - the very short list
* [The Whitepaper by Vitalik Buterin](https://ethereum.org/en/whitepaper/)
* [The Yellowpaper by Gavin Wood](https://github.com/ethereum/yellowpaper), & [pdf](https://ethereum.github.io/yellowpaper/paper.pdf)
* [Extensive list of learning resources](https://ethereum.org/en/learn/)
* [EVM Illustrated (slides)](https://github.com/takenobu-hs/ethereum-evm-illustrated)
* [Beacon Chain Explained](https://ethos.dev/beacon-chain)

# Exercises
1. Visit the [EVM playground](https://www.evm.codes/playground?fork=shanghai) to see the stack in operation.

# Video Lecture
To be posted.
