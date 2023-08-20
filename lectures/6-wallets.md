[↰ back](../../..)

# Lecture 6: Wallets and Tokens
## Contents
1. [Wallets](#wallets)
2. [Seed Phrases](#seed-phrases)
3. [Hierarchical Deterministic (HD) Wallets](#hierarchical-deterministic-hd-wallets)
4. [Multisig](#multisig)
5. [Multi-Party Computation](#multi-party-computation)
6. [Token standards](#token-standards-ethereum)
7. [Non-Ethereum Token Standards](#non-ethereum-token-standards)
8. [A Token's Lifecycle](#a-tokens-lifecycle)
9. [What did we miss?](#what-did-we-miss)
10. [Further Reading - the very short list](#further-reading---the-very-short-list)
11. [Exercises](#exercises)


Contrary to popular belief, there is no standardized encryption in the Bitcoin protocol. As a decentralized system of exchange, there is no need for encryption. All the transactions are stored in the blockchain and accessible to everyone. Access to the private keys controlling addresses is maintained solely through personal security of the user. It is imperative that users keep their private keys secret, just as in any other cryptosystem. There are some added enhancements for encrypting passwords and wallets, but these are third-party additions and not built into the protocol.



## Wallets
The term wallet is both a good name and a bad name to describe its purpose in the cryptocurrency lexicon. It's bad because there are no coins to store in a wallet, only keys that can sign transactions. Also, if you lose your wallet, it does not mean your crypto tokens can be used by whoever finds it. It is a good term because it fits into the metaphor of using a wallet to access the financial system similar to accessing credit card networks with a VISA card, trade with your neighbour using cash, and coffee via stamped vouchers.

Wallets have evolved past the point of storing randomly generated private keys and now use a master seed through which multiple child keys can be derived. HD, or hierarchical deterministic wallets do not need access to the private key to be able to spawn children. The child keys can then be used to generate grand-child keys, and so forth allowing multiple transactions to use different public addresses all derived from the same private key. This increases security because you can delete the private key from the device as long as you have a backup method to recreate it. Using common words as a seed phrase to derive a key is easier to backup than a sequence of characters.

The user experience for blockchain applications is an area for improvement. As an example, *Mycellium* has been in wallet development since 2009, switching their focus from secure hardware after bitcoin was released. From the figure below you get the sense that setting up a wallet and sending coins is not user-friendly.

> <img width="800" alt="The Mycelium bitcoin wallet interface." src="https://github.com/millecodex/COMP842/assets/39792005/7f6ef20d-451d-4ccc-8821-52204777631d">\
> The Mycelium bitcoin wallet interface (2019). The home screen (left); Adding a new account (middle); Sending a transaction (right).

## Seed Phrases
After selecting *backup now*, two warning messages are displayed and then a word list which you must write down (screenshots and copy/paste are disabled). The word list for this account is:

|   |   |   |
|---|---|---|
| 1. envelope | 2. motor | 3. heart |
| 4. circle   | 5. apple | 6. essay |
| 7. close    | 8. ranch | 9. powder |
| 10. cause   | 11. royal | 12. brass |
> Table: a backup seed phrase maps common words (in this case English) to bytes.

The list must be verified by the user after being displayed in the app. In the case of losing your device, the seed phrase can be used to import the wallet. Screenshots from Trustwallet, show a different approach. The home screen is much less cluttered and appears more like what you would expect from a wallet app. 

> <img width="800" alt="Screenshots from Trustwallet showing the recovery phrase" src="https://github.com/millecodex/COMP842/assets/39792005/8e708174-23a2-4ca3-8264-daac159180c6">\
> Figure: Screenshots from Trustwallet showing the recovery phrase. 

Trustwallet will let you export the 12-word seed phrase but will not let you dump your private keys to the screen as an added security measure[^1]. The Mycelium private key of the seed phrase is shown in Figure below.

[^1]: Using both Mycelium and Enjin wallets for Android, I could not screen-capture or share the screen with my PC.

> <img width="250" alt="The Mycelium bitcoin wallet interface." src="https://github.com/millecodex/COMP842/assets/39792005/efcb1db3-c720-4fc2-86c2-83f32696eac2">\
> Figure: Mycelium private key of the seed phrase shown above. Note the warning message: "whoever knows this code can spend all your current and future bitcion from this account."

### Key Storage
Storage of cryptocurrency is similar to storage of your online banking details. There are no actual coins or crypto-assets to keep safe; there is no `<bitcoin object>` to keep password protected. Remember, the blockchain is an open ledger of every transaction in the network. Bitcoin is cryptographically secured, and if you have the private keys to an address, then you control the funds that address references in the blockchain.

A Bitcoin address is the public key of a public-private key pair generated by a 256-bit elliptic curve function. The public key is encoded in base-58 to reduce errors in transcription by removing similar characters like `0`, `O`, `1`, and `l`.

Cryptocurrencies are riskier than traditional online banking because if you lose your private keys, they are not recoverable. There is no password reset or government-issued ID verification to recover your account.

There are a number of ways to store your keys:

- **Hot Wallet**: This is the most common method. It is a software application that stores your private keys so you can sign transactions, keeps track of your tokens, and may offer additional functionality like multiple addresses or multiple token support. The risk here is that if you lose your device, your private keys are gone with it. Day-to-day transactions using a smartphone would be done through a hot wallet.

- **Cold Storage**: For larger amounts, savings, investments, and custodial services, a cold or hardware wallet is recommended. This is a device that is not powered and has no connectivity and stores your private keys internally. When tokens are required, it can be plugged into a USB and connected to the network.

- **Paper Wallet**: Once a key pair has been generated and used to receive tokens, that private key will always have ownership of the tokens. The private key can be printed out or written down, sometimes as a QR code for easy scanning. After the memory has been cleared, there is no more digital record of the private keys.

- **Brain Wallet**: The most serious storage system is to remember your private keys and destroy all physical and digital evidence of them. Certain memory mnemonics and the use of common words as seed phrases can help with this.

It's important to note that for all these methods, including memorization, it is possible to receive tokens to your address without connecting the keys to the network. These transactions will be recorded by all the nodes running the blockchain and propagated accordingly. Private keys are only required to sign transactions (spend tokens). All of these methods are vulnerable to crises such as fire or theft and represent a single point of failure. Backing up your keys can solve the crisis issues, but someone could still steal the backup.

## Hierarchical Deterministic (HD) Wallets
Each instance of MetaMask that has a recovery phrase is called a hierarchical deterministic wallet. Within this hierarchy you can generate multiple accounts, each having their own public/private key pair and each being able to be regenerated with the recovery phrase. This allows many addresses to be generated from the same seed entropy[^1], so you can always invoice with a fresh address. The new accounts generated under this regime are ordered, with one 'leading' to the next, and deterministic such that when recovering a wallet the child accounts generated will be the same and in the same order.

[^1]: Seed entropy refers to the orignal source of randomness used to generate the seed phrase. In the case of browser generation such as with MetaMask this comes from the OS random function and is the safest way to do so online. Good ways to generate your own entropy include [dice](https://vault12.com/securemycrypto/cryptocurrency-security-how-to/dice-crypto-recovery-seed/particle-29) and [lava-lamps](https://www.cloudflare.com/en-gb/learning/ssl/lava-lamp-encryption/).

> <p align="left"><img width="600" alt="HD key generation tree" src="https://user-images.githubusercontent.com/39792005/188350149-c50a1858-6a84-4f47-bd2d-740b47b8657b.png"></p>

## BIP39
The seed phrase is a mapping of common English (& some other) language words to numbers that when assembled in the correct order represent the master private key. **BIP39**[^2] is a standard that was developed for Bitcoin and now used in many cryptocurrency projects. The total list is [2048 words](https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md) and contains words as short as `mom` and as long as `mosquito`. From the master key many branches and children can be derived as per the algorithm below. To generate a seed phrase, you first need some entropy, then run it through `SHA256`, append the bit difference to the entropy, and split the output into the required number of words (12, 18, 24, etc.). These individual pieces then map to one of the 2048 words.

[^2]: Bitcoin improvement proposal number [39](https://en.bitcoin.it/wiki/BIP_0039). See also [BIP32](https://en.bitcoin.it/wiki/BIP_0032) and [BIP44]()

> <p align="left"><img width="600" alt="extending parent public key" src="https://user-images.githubusercontent.com/39792005/188350155-7f26f889-fcc9-45bd-9691-74d2245031db.png"></p>
>
> Key diagram sources: Antonopolous, Mastering Bitcoin. 2nd ed. 2018. https://github.com/bitcoinbook/bitcoinbook. 

## Security
In order to guess someone's private key you need to guess a sequence of 12, or 24 words from the list. Since there are 2048 possibilities for each guess, you have a one-in-2048 chance of guessing the first word correctly. At this point it may seem feesible for a computer to run this search fairly easily. Keeping in mind there is no progress indicator like making it past the first tumbler in a lock, so the probability to find the first two words is now $p= {1 \over 2048}{1 \over 2048}={1 \over 4,194,304} $. Extending this to a twelve word seed phrase: $p={1 \over 2048^{12}}$ and inverting to represent the number of possibilities we get $5.44E10^{39}$. On average it might take half the time to correctly guess a seed, so this is $2.72E10^{39}$ attemps. This is [roughly](https://en.wikipedia.org/wiki/Orders_of_magnitude_(numbers)#1036) the same size as the theoretical maximum number of Internet addresses that can be allocated under the IPv6 addressing ( $10^{36}$ ); or the estimated number of atoms in Earth ( $10^{50}$ ).

*Exercise:* How much harder is it to guess a 24-word phrase? How long would it take your computer to guess every possible key?

## Multisig
Multisignature (multisig) refers to the requirement of multiple private keys to authorise a cryptocurrency transaction. It's akin to a digital lock that needs multiple keys to be opened. Initially developed to enhance the security of Bitcoin[^multisig] transactions, multisig is now a well known key application. Imagine two out of three business owners needing to sign with their private keys to disburse funding, or a family that requires agreement among siblings and their lawyer to settle an estate, or a governance structure that needs majority voting to fund a proposal. A multiple-signature transaction requires more than one authorizing key. Sometimes referred to as an $M$ of $N$ system, if a minimum of $M$ private keys sign a transaction out of $N$ possible signatories, then the transaction can proceed.  

[^multisig]: *Multisig* is a useful feature in bitcoin although includes a bug requiring an extra item to be added to the script stack before execution. Although technically easy to fix, the bug has always been included in the reference implementation and is now a part of the consensus rules. At this stage it is considered too risky to fix because of unknown downstream effects. Antonopoulos (2017) details multisig transactions and the more advanced *pay-to-script-hash* functionality.

To enhance personal security you can arrange your funds in a 2 of 3 multisig (or more!) with private keys stored on different devices. This way, if one gets compromised, you can use the other two to move the funds. This additional layer provides enhanced protection against malware and phishing as the compromised device can't move your coins without at least one other signature.

Here's a pseudocode algorithm to create a multisig address:
```js
// Define Parameters
M = 2 // Minimum number of required signatures
N = 3 // Total number of possible signatures
publicKeys = [PublicKey1, PublicKey2, PublicKey3] 

// Create the Redeem Script
redeemScript = concatenate(M, publicKeys[0], publicKeys[1], publicKeys[2], N, "OP_CHECKMULTISIG")

// Compile Redeem Script to Bytecode (implementation varies based on the specific language and environment)
bytecode = compileToBytecode(redeemScript)

// Hash the Redeem Script to create a P2SH address
p2shHash = SHA256(RIPEMD160(bytecode))

// Add Network Information and Checksum, then encode into Base58Check for the final P2SH address
p2shAddress = Base58CheckEncode(p2shHash, networkPrefix, checksum)

// The P2SH address is now ready for use in transactions
```

Logically extending $M$ of $N$ signatures leads to transactions that can execute a small amount of instructions. Transactions are just data that is stored by all the nodes in the network, and there is no reason why this data could not be code -> *Smart Contracts*?

### Secret Sharing
In the scenario where someone eventually steals our private keys, secret sharing can provide an additional layer of security. The idea behind secret sharing is to split the key into multiple parts, or shares, such that a certain number of shares are required to reconstruct the key.

Let's consider a simple example with 2 shares ($N=2$) and a threshold of 2 shares ($K=2$). Suppose the secret $S$ is a 128-bit number, and we generate a random 128-bit number $R$. One share can be $R$, and the other share can be $S \oplus R$ (bitwise XOR). With only one share, $R$ is random and provides no information about $S$. The share $S \oplus R$ depends on knowing $R$, so it also provides no information about $S$. However, when both shares are combined, $R$ cancels out and the original secret $S$ can be reconstructed. This concept is similar to encrypting the secret with a one-time pad cipher where $R$ is the key.

Now, let's consider the case where we split the secret into four shares and require any two shares to reconstruct the secret. We can use some linear algebra to achieve this. We can think of the shares as points on a line. Any two points can construct a line, but if we introduce a third random point, it is unlikely to be collinear with the first two points. By generating $N$ shares along this line, any two of these shares can reconstruct the line and determine the $x$-intercept, which is the original secret $S$. However, any single share is useless because the slope of the line is unknown.

This approach of secret sharing provides a way to distribute the shares among trustworthy individuals. Even if one or more shares are compromised, they provide no useful information about the secret without the required threshold number of shares to reconstruct it.

> <img width="461" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/840adfd1-f4ee-40cc-9286-fbb0b0af1b45">\
> Figure: The point $(0,S)$ represents the secret, a large random number less than a large prime, $P$. The shares are linear combinations modulo $P$, up to $N$, where any 2 of them will recover the secret.

$$
\begin{align}
x=0,\quad y&=S\\
x=1,\quad y&=(S+R)\mod P\\
x=2,\quad y&=(S+2R)\mod P\\
x=3,\quad y&=(S+3R)\mod P\\
\vdots\\
x=N,\quad y&=(S+NR)\mod P\\
\end{align}
$$

What if you require more than 2 shares necessary to reconstruct the key? If we increase the degree of our share-reconstruction function from linear to parabolic, then we have $K=3$ is necessary to find $S$ because 3 points can uniquely define a parabola. This can be continued up to $K=N-1$ shares. Since multiple people can store portions of an individuals private key it would be convenient if a similar setup was in place for specific transactions or sets of transactions.

## Multi-Party Computation
**The Millionaire's Problem** is a classic problem in the field of cryptography, specifically in the context of Multi-Party Computation (MPC). It was introduced by Andrew Yao (1986), and it forms the basis for understanding how privacy can be preserved during computation. Two millionaires, Alice and Bob, want to compare their wealth to find out who is richer without revealing the actual amount of their wealth to each other or anyone else. They want to know the result of the comparison but are unwilling to disclose any additional information.

The Millionaire's Problem can be seen as a special case of secure multi-party computation, where two parties wish to jointly compute a function over their inputs (in this case, a comparison function) while keeping those inputs private. Here, the answer is Max(Alice's Salary, Bob's Salary). An MPC protocol will take the private information (salaries), compute the function (max) and relay the information (Alice) without revealling the private info (salary). Also, the protocol is just that, a protocol, and not a trusted third party.

Multi-Party Computation (MPC) wallets are an innovation in cryptocurrency storage that leverages cryptographic protocols to securely distribute private keys among multiple parties. This distribution ensures that no single entity has control, enhancing security, and removing single points of failure.

Distinguishing MPC wallets from regular ones like single-key, multi-signature, or hardware wallets, MPC wallets are more secure, protocol-agnostic, and less cumbersome in authorization. They also overcome issues like damage to physical devices or the loss of private keys.

Benefits of MPC Wallets include:
* Decentralization: Elimination of trusted third parties for storing private keys.
* Data Privacy: No revealing of private information to other parties.
* Correctness: All parties are confident the result is correct (as they cannot see the inputs).
* Removal of Single Points of Failure: Distributing private keys among multiple parties.
* Scalability: Flexibility in adding or removing parties.

Risks of MPC Wallets include:
* High Communication Costs: Extensive communication can increase network latency and expose to attacks.
* Technical Complexity: Advanced cryptographic techniques might lead to vulnerabilities.
* Lack of Interoperability: Incompatibility with conventional wallets due to non-standardization.

Some popular MPC wallets are ZenGo, Fireblocks, Coinbase, and Qredo, each catering to different types of users with varying features and security levels.

## Token Standards (Ethereum)
Over time standards have emerged that assist developers with creating new projects, building functionality, and interacting with other tokens, contracts, and chains. Some of the main [standards](https://ethereum.org/en/developers/docs/standards/tokens/) that have been developed for Ethereum are:

### ERC-20
The first use case of Ethereum was generating new coins. These projects often launched with fundraising efforts called ICOs (initial coin offerings) that promised buyers a certain allocation of new tokens. All these tokens live inside (or on) the Ethereum blockchain but are separate from ether. Think of tokens as carriages that run on the rails of Ethereum and the whole train is powered by ether. The [Ethereum Request for Comments #20](https://eips.ethereum.org/EIPS/eip-20) is the standard that defines how to make a fungible token that is compatible with Ethereum itself. Because its an open network anyone is free to make their own token and launch it on Ethereum[^ownToken]. The contract will live forever on the blockchain and handle functions like transfers, account balances, token creation and destruction. These tokens can be divided into as small as eighteen decimal places (`0.000 000 000 000 000 001`) to allow for very small and fractional payments.
[^ownToken]: This is often a tutorial exercise when learning about blockchains. Launching a self-token contract on the mainnet is expensive due to gas fees, but you can easily launch one on a testnet.

Examples of the ERC-20 standard include the following tokens (among *many*):
* `DAI` the decentralized algorithmic [stablecoin](https://makerdao.com/en/),
* `LINK` the decentralized [oracle network](https://chain.link/), and
* `wBTC` [wrapped bitcoin](tokens.md#bridging).

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

## Non-Ethereum Token Standards
Ethereum may be the original smart contract platform, but there are plenty of younger ones vying for your tokens. Here I've listed some of the main smart contract platforms and their associated token standards. EVM compatibiliy refers to the Ethereum virtual machine which handles the processing of smart contracts. If compatible, the chain can understand contracts made for Ethereum which can help with bootstrapping users and projects that already exist there.

|Blockchain|Native Token|EVM Compatible?|Comments|
|:---------|:-----------|:--------------|:-------|
|Ethereum |`ETH`|:heavy_check_mark:|`ETH` is the native currency; ERC-20 tokens run on top and are processed by the EVM.|
|Avalanche|`AVAX`|:heavy_check_mark:|Avalanche has a 'X-chain' for native assets but also a 'C-chain' designed to be compatible with Ethereum **C**ontracts.|
|Fantom   |`FTM` |:heavy_check_mark:|The `FTM` token [exists on Ethereum](https://etherscan.io/address/0x4E15361FD6b4BB609Fa63C81A2be19d873717870), but is the native asset of the Fantom ecosystem and can be bridged between the two.|
|Polkadot |`DOT` |:heavy_check_mark:|Although compatible with the EVM, this is not the main functionality. `DOT` is a new standard of the [Polkadot](https://polkadot.network/) ecosystem.|
|Solana   |`SOL` |:negative_squared_cross_mark:|Solana has [built-in support](https://spl.solana.com/token) for creating new tokens; EVM compatibility is in progress.|
|Tezos    |`XTZ` |:negative_squared_cross_mark:|Tezos has its own standards; [FA2](https://gitlab.com/tezos/tzip/-/blob/master/proposals/tzip-12/tzip-12.md) is a unified token contract interface.|
|Cosmos   |`ATOM`|:negative_squared_cross_mark:|The `ATOM` token can be found on Ethereum and Binance Smart Chain, but is the native asset of the Cosmos ecosystem. EVM compatibility is [in progress]().|

## a Token's Lifecycle
### Minting 👉 Wrapping 👉 Bridging 👉 Burning
Many things can happen to our cryptographic tokens during their life span. To begin with: where do tokens come from?

### Minting
Minting tokens refers to the same process of creating tradeable items of value as coins being minted as new currency. Just as with coins, it seems best to increase token supply slowly, or at least according to a set plan. All of the New Zealand dollars weren't created at once, rather they are minted over time as the Reserve Bank seeks to increase the [monetary supply](https://www.interest.co.nz/charts/credit/money-supply). A key difference with the minting of cryptocurrencies such as bitcoin is that they adhere to a [fixed schedule](bitcoin.md#economic-incentives--monetary-supply), set in advance, written into the code. For example, new bitcoins are created in the coinbase transaction of every block, presently 6.25 `BTC` every ten minutes. 

Compare the minting of New Zealand dollars to new bitcoin. Bitcoin's chart goes well into the future as the supply schedule is fixed in code. Click for larger version.
|New Zealand M3 money supply since 1990 [(source)](https://tradingeconomics.com/new-zealand/money-supply-m3)|Bitcoin supply (green) since 2009 [(source)](https://www.coingecko.com/en/explain/bitcoin_halving) |
|:---|:---|
|<p align="center"><img width="600" alt="New_Zealand_m3_money_supply" src="https://user-images.githubusercontent.com/39792005/159141186-1d657bf2-924d-44c2-89c0-db5fad3f2b2d.PNG"></p>|<p align="center"><img width="600" alt="bitcoin_supply" src="https://user-images.githubusercontent.com/39792005/147862906-6537e8d0-aa4d-403d-825b-aefd1e31585a.png"></p>|

A slow and steady issuance has its benefits such as knowing in advance how many will ever be minted. If all the tokens were created at inception there would be a distribution problem: the creator(s) would have the total supply and have to incentivise newcomers.  Tokenomics is the central-planning activity of deciding who gets how many tokens and at what intervals. This is a hard problem because it involves human nature. For example: How much is too much to reserve for the creators? (called a pre-mine) Developers? VCs? Is the supply infationary or deflationary? Can the details be changed in the future?

The popularity of NFTs has brought *minting* into common usage. NFTs are usually created one at a time, such that when the contract is called it spawns a new token in the set which is then sent to the buyer. 

### Wrapping
Next, our token may want to venture out beyond its home chain and explore some of the broader ecosystem. Taking a bitcoin as an example, this token is only built to be transferred between users of the Bitcoin network. What if our intrepid bitcoin wanted to participate in some yield farming on the Ethereum blockchain? One method to do this would be for someone to act as a escrow service and hold your bitcoin (on the Bitcoin blockchain) while releaseing a new bitcoin-ish token (on the Ethereum blockchain). This is where wrapping comes in. The new tokenized version, [wrapped bitcoin](https://wbtc.network/), or `wBTC`, can be used in Ethereum wallets and apps while tracking the value of bitcoin 1:1. Ether itself can be wrapped to travel to other chains where it may be seen as `wETH`.

### Bridging
Transferring tokens from one blockchain to another requires a bridge because there is no native compatibility between blockchains. In a multi-blockchain world interoperability is a necessity to transfer value from one chain to another[^inter]. An analogy on bridging tokens comes traditional finance. To send money overseas a third party needs to buy the first currency and then sell you the second currency. The forex broker or bank is fine with taking this position because they can resell the excess currency while earning a fee. This parallel isn't entirely accurate because the bank is not minting new currency to sell you, rather they are using their inventory. The blockchain case can involve creating new tokens or purchasing pre-existing sythetic ones..
[^inter]: Some blockchain ecosystems have been designed with this in mind, particularly Cosmos and Polkadot. This does not, however, mean that they work with each other, just that the parachains of Polkadot and individual blockchains of Cosmos are interoperable within their respective ecosystems.

The process to bridge tokens from Bitcoin to Ethereum, using wrapped bitcoin as an example:
1. send `BTC` to a trusted third party custodial service; wrapped bitcoin uses [BitGo](https://www.bitgo.com/)
2. `BTC` is locked up and held by BitGo; its visible, but not available on the bitcoin blockchain
3. BitGo mints new tokens called wrapped bitcoins, `wBTC`, in an ERC-20 contract, to be used on Ethereum. The wrapped version must track the price of the original token. Value transfer in this case is 1:1, and any deviation would be an opportunity for arbitrage.
4. the custodian sends `wBTC` to the user and can now be traded as an ERC-20 token.

To bridge back, or redeem, from Ethereum to Bitcoin:
1. send `wBTC` to BitGo's contract
2. `wBTC` is now taken out of circulation by burning
3. original `BTC` is unlocked and 
4. sent to the user on the bitcoin blockchain

For minting and burning wrapped bitcoin through the steps above the third party collects KYC information and so this process isn't entirely decentralized. For retail users that don't need to mint/burn and just want to use `wBTC` they can still use a decentralized exchange like SushiSwap or Uniswap to get the token.  According to [DeFi Llama](https://defillama.com/protocols/Bridge) there is over $13B bitcoin that has been bridged to other chains, mostly Ethereum. 

The general bridging process is shown in the diagram below, this time using Ethereum as the native blockchain and Avalanche as the destination. First the `ETH` is deposited into the bridging contract, it is locked, and the bridge is activated to mint new `wETH` tokens on Avalanche, which are then sent to the destination wallet. Redemption happens in reverse except step 3 is replaced with a burn, and step 2 is an unlock.
> <p align="center"><img width="800" alt="" src="https://user-images.githubusercontent.com/39792005/158924916-bb061d54-4164-4638-89f3-d21bf461a2bf.PNG"></p>
Bridging isn't just for bitcoin and ether. The [Multichain](https://app.multichain.org/#/router) service has over 600 bridged assets across most major blockchains. They also have a router for multi-chain bridging and support for NFTs. Multichain's protocol relies on a network of nodes and results in a decentralised trustless service that uses [Secure Multi-Party Computation](https://docs.multichain.org/how-it-works). 

### Burning
Burning tokens is a provable way to remove them from circulation and the overall supply. This is necessary,as we saw above, in bridging operations to prevent supply inflation or [theft](https://cointelegraph.com/news/wormhole-hack-illustrates-danger-of-defi-cross-chain-bridges). Protocols may also want to burn their tokens according to scheduled supply changes or upgrades. Part of the Ethereum network's transition to proof-of-stake involved an upgrade in July 2021 that changed the fee distribution policy for miners. After the [London](https://blog.ethereum.org/2021/07/15/london-mainnet-announcement/) hardfork, miner's fees were split into two groups with a base fee being burned and a priority fee going to the miner. This has effectively changed the supply of ether from inflationary to defationary.

Practically speaking, tokens are burned by being sent to an unspendable address. This provides the verification that they can no longer be used. For Ethereum this means the recipient address has neither a private key nor a contract capable of accepting ether. You may have seen some burn addresses:

|Ethereum address|note|
|:---|:---|
|`0x0000000000000000000000000000000000000000`|the zero address; this is a default used for contract creation| 
|`0x000000000000000000000000000000000000dEaD`|note the "dead" in hex at the end| 
|`0xdEAD000000000000000042069420694206942069`|not technically unspendable but highly unlikely this [address](https://www.reddit.com/r/ethereum/comments/nenuk0/comment/gyi4pkn/?utm_source=share&utm_medium=web2x&context=3) is ever generated| 

Sending any tokens, either accidentally or on purpose, to these addresses will be interpreted as a burn and result in a loss of funds.

### A Cautionary Note
Sending tokens to any address that you do not control or have the private keys to requires diligence in checking the destination, both to ensure the right network is being used, and the address is as intended. If tokens get sent to a random address there is no method or process for recovering them. There is no consumer protection in crypto!

## What did we miss?
* [Airdrops](https://airdrops.io/) - because blockchain data is public new projects can easily view wallet addresses and send them tokens to increase visibility and achieve immediate wider token distribution. Famous airdrops include Stellar Lumens, Uniswap, Ethereum Name Service, and Arbitrum.
* [Tokenomics](https://101blockchains.com/tokenomics/) is the new blockchain branch of token distribution and incentives. It's wise to view most projects as 'experiments-in-progress' and be cautious of marketing claims.

## Further Reading - the very short list
* What is MPC? [Fireblocks explainer](https://www.fireblocks.com/what-is-mpc/)
* Andrew Yao's Protocol for Secure Computations [pdf](https://github.com/millecodex/COMP842/blob/master/papers/yao1982-ocr.pdf)
* Garbled Circuits ([wikipedia](https://en.wikipedia.org/wiki/Garbled_circuit))
* [An Ethereum token list standard](https://tokenlists.org/)
* [The Tokens chapter from *Mastering Ethereum*](https://github.com/ethereumbook/ethereumbook/blob/develop/10tokens.asciidoc)

## Exercises
1. a
2. b
3. c
