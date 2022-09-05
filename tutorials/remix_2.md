# Remix Part II - Wallets
Remix Part I looked at using the IDE to compile and deploy smart contracts; remix comes with some stock-standard contracts for storage, ownership, etc. 

## Environment
These get compiled within the virtual machine (VM) environment that runs within your browser instance. This is a simulated blockchain; there are no real blocks, or miners, or validators here. From the [docs](https://remix-ide.readthedocs.io/en/latest/run.html):

> For connecting to a sandbox blockchain in the browser. The Remix VM (previously called JavaScript VM) is its own “blockchain” and on each reload the old chain will be cleared and a new blockchain will be started. The old one will not be saved. The London refers to the London fork of Ethereum.

<p align="left"><img width="300" alt="remix environment options" src="https://user-images.githubusercontent.com/39792005/188035509-b90d1cda-bdd5-4b40-84a6-385beacad1f0.png"></p>

The default is *London* which includes support for the [London fork](https://ethereum.org/en/history/#london) which changed how fees are handled. As it stands now we have access to 10 dummy test accounts that are preloaded with 100 ETH. These accounts are ephemeral and transaction history will not be saved--or mined to the blockchain for that matter. 

*Injected Provider* will allow communication with MetaMask and Brave's native crypto wallet.

## MetaMask
[Metamask](https://metamask.io/download/) is a Chrome extension. It can run with Chrome/Firefox/Brave/Edge and acts as a middleman between blockchains (mainnets, testnets, custom interfaces, etc.) and applications. The 'wallet' part will store your private keys and sign messages and transactions as well as manage multiple accounts. 

<p align="left"><img width="800" alt="various crypto extensions" src="https://user-images.githubusercontent.com/39792005/188037152-bd2711d2-633b-4d73-a388-9d4bc56b5630.png"></p>

> various crypto extensions running in Brave. *Crypto Wallets* is Brave's native wallet extension. Best practise for security is to disable extensions when they are not in use. See [here](https://coinguides.org/metamask-security/) for a list of recommended MetaMask security settings and some of the common scams in play.

After installing the extension, you have the option to import a previous wallet using a recovery phrase or create a new one.

<p align="left"><img width="600" alt="MetaMask create screen" src="https://user-images.githubusercontent.com/39792005/188044930-e8934667-f578-4e81-a37b-94a11e4c888e.png"></p>

MetaMask will provide you with a *Secret Recovery Phrase* (often called a seed phrase), and ask you to securely store the words and then submit them back in the correct order. It is very important to keep this recovery phrase of 12 words **private** and **secure**. (Even if only using for testnet activity it is wise crypto behaviour to become comfortable with self custody.)

<p align="left"><img width="600" alt="MetaMask Secret Recovery Phrase" src="https://user-images.githubusercontent.com/39792005/188044954-8da4e5bd-e167-4e8d-9c2d-1c124cfc6c08.png"></p>

After creating a password, watching the video, writing down your phrase, and re-entering your phrase, you'll be at the interface ready to use your new account address (the one shown here is `0x99A95d4d7DDe6B9E663509a41CF3A9eeAfC07Ad9`) in any of the chains that accept Ethereum based addresses.

<p align="left"><img width="800" alt="MetaMask interface" src="https://user-images.githubusercontent.com/39792005/188044996-51bd22f0-1661-4646-9634-840ec3df62ab.png"></p>

## Hierarchical Deterministic (HD) Wallets
Each instance of MetaMask that has a recovery phrase is called a hierarchical deterministic wallet. Within this hierarchy you can generate multiple accounts, each having their own public/private key pair and each being able to be regenerated with the recovery phrase. This allows many addresses to be generated from the same seed entropy[^1], so you can always invoice with a fresh address. The new accounts generated under this regime are ordered, with one 'leading' to the next, and deterministic such that when recovering a wallet the child accounts generated will be the same and in the same order.

[^1]: Seed entropy refers to the orignal source of randomness used to generate the seed phrase. In the case of browser generation such as with MetaMask this comes from the OS random function and is the safest way to do so online. Good ways to generate your own entropy include [dice](https://vault12.com/securemycrypto/cryptocurrency-security-how-to/dice-crypto-recovery-seed/particle-29) and [lava-lamps](https://www.cloudflare.com/en-gb/learning/ssl/lava-lamp-encryption/).

<p align="left"><img width="600" alt="HD key generation tree" src="https://user-images.githubusercontent.com/39792005/188350149-c50a1858-6a84-4f47-bd2d-740b47b8657b.png"></p>

## BIP39
The seed phrase is a mapping of common English (& some other) language words to numbers that when assembled in the correct order represent the master private key. **BIP39**[^2] is a standard that was developed for Bitcoin and now used in many cryptocurrency projects. The total list is [2048 words](https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md) and contains words as short as `mom` and as long as `mosquito`. From the master key many branches and children can be derived as per the algorithm below. To generate a seed phrase, you first need some entropy, then run it through `SHA256`, append the bit difference to the entropy, and split the output into the required number of words (12, 18, 24, etc.). These individual pieces then map to one of the 2048 words.

[^2]: Bitcoin improvement proposal number [39](https://en.bitcoin.it/wiki/BIP_0039). See also [BIP32](https://en.bitcoin.it/wiki/BIP_0032) and [BIP44]()

<p align="left"><img width="600" alt="extending parent public key" src="https://user-images.githubusercontent.com/39792005/188350155-7f26f889-fcc9-45bd-9691-74d2245031db.png"></p>

> Key diagram sources: Antonopolous, Mastering Bitcoin.

## Security
In order to guess someone's private key you need to guess a sequence of 12, or 24 words from the list. Since there are 2048 possibilities for each guess, you have a one-in-2048 chance of guessing the first word correctly. At this point it may seem feesible for a computer to run this search fairly easily. Keeping in mind there is no progress indicator like making it past the first tumbler in a lock, so the probability to find the first two words is now $p= {1 \over 2048}{1 \over 2048}={1 \over 4,194,304} $. Extending this to a twelve word seed phrase: $p={1 \over 2048^{12}}$ and inverting to represent the number of possibilities we get $5.44E10^{39}$. On average it might take half the time to correctly guess a seed, so this is $2.72E10^{39}$ attemps. This is [roughly](https://en.wikipedia.org/wiki/Orders_of_magnitude_(numbers)#1036) the same size as the theoretical maximum number of Internet addresses that can be allocated under the IPv6 addressing ( $10^{36}$ ); or the estimated number of atoms in Earth ( $10^{50}$ ).

*Exercise:* how much harder is it to guess a 24-word phrase?


