# Tutorial 9: NFTs
## 🛠️ Under Construction 🚧 👷
### Contents
1. [intro](nft_1.md#intro)
1. [second](nft_1.md#second)
1. [third](nft_1.md#third)
1. [What did we miss?](nft_1.md#what-did-we-miss)
1. [Further Reading - the very short list](nft_1.md#further-reading---the-very-short-list)

# Intro
[Earlier](https://github.com/millecodex/COMP726/blob/master/tutorials/archimate.md) we laid out the basics for an app that tracks student progression. Teachers had the authority to confer qualifications upon a student after completing a course (or at checkpoints along the way). Somthing like a qualification certificate is a perfect use case for a non-fungible token. Most paper documents of this sort contain some basic info: title, name, date, authority, potential expiry, logo or signature, etcetera. Lets say you wanted to present your diploma to an institution to prove that you had already completed some Foundation Programming classes, it is likely the diploma would not be enough. The registrar at the potential school would contact the student's previous school to validate the claim. If only there was a trustless decentralised system that allowed for easy verification? Hmm....

# Ethereum Token Standards
Over time standards have emerged that assist developers with creating new projects, building functionality, and interacting with other tokens, contracts, and chains. Some of the main [standards](https://ethereum.org/en/developers/docs/standards/tokens/) that have been developed for Ethereum are:

### ERC-20
The first use case of Ethereum was generating new coins. These projects often launched with fundraising efforts called ICOs (initial coin offerings) that promised buyers a certain allocation of new tokens. All these tokens live inside (or on) the Ethereum blockchain but are separate from ether. Think of tokens as carriages that run on the rails of Ethereum and the whole train is powered by ether. The [Ethereum Request for Comments #20](https://eips.ethereum.org/EIPS/eip-20) is the standard that defines how to make a fungible token that is compatible with Ethereum itself. Because its an open network anyone is free to make their own token and launch it on Ethereum[^ownToken]. The contract will live forever on the blockchain and handle functions like transfers, account balances, token creation and destruction. These tokens can be divided into as small as eighteen decimal places (`0.000 000 000 000 000 001`) to allow for very small and fractional payments.

[^ownToken]: This is often a tutorial exercise when learning about blockchains. Launching a self-token contract on the mainnet is expensive due to gas fees, but you can easily launch one on a testnet.

Examples of the ERC-20 standard include the following tokens (among *many*):
* `DAI` the decentralized algorithmic [stablecoin](https://makerdao.com/en/),
* `LINK` the decentralized [oracle network](https://chain.link/), and
* `wBTC` [wrapped bitcoin](https://wbtc.network/).

### ERC-721
ERC-721 is a standard that includes an *integer* variable called `tokenID` that must be unique. From the EIP: "In general, all houses are distinct and no two kittens are alike. NFTs are distinguishable and you must track the ownership of each one separately." Any tokens deployed with this standard cannot be subdivided, and ownership is wholly transferred. 

Examples of the ERC-721 standard include:
* [CryptoKitties](https://www.cryptokitties.co/) collectibles and game,
* [Ethereum Name Service](https://ens.domains/) domain registrar, and
* [the Bored Ape Yacht Club](https://boredapeyachtclub.com/#/) collectibles and club membership.

### ERC-1155
Further to the previous two standards, the 1155 standard merges both fungible and non-fungible into a new standard that extends functionality. Called a Multi-token standard it can batch transfer groups of items, for example, if your game character kills another it can transfer the plundered items to the winner in a single transaction. It also improves efficiency with a focus on game design where a large number of transfers could be required and it would be cumbersome for the user to stop gameplay to interact with a smart contract and pay associated gas fees.

Examples of the ERC-1155 standard include:
* [OpenSea](https://opensea.io/) the NFT marketplace,
* [Skyweaver](https://www.skyweaver.net/) the game, and
* [The Sandbox](https://www.sandbox.game/en/) metaverse platform.

# Pre-requisites
We'll need the following tools in our environment before we can get going.
1. MetaMask account with some testnet ether. (See our previous steps for this here.)
2. Alchemy account to communicate with Ethereum. (Note there are many other ways to do this.)
3. 

# Let's Mint an NFT
* Point form list
  * second

# Further Reading - the very short list
* [Based on this Tutorial from Ethereum.org](https://ethereum.org/en/developers/tutorials/how-to-write-and-deploy-an-nft/)
* https://nftschool.dev/
* []()

# Exercises
1. What are some examples of fungible tokens compared to non-fungible tokens that you use that are not blockchain related?
