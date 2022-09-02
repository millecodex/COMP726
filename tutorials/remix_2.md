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

> various crypto extensions running in Brave. *Crypto Wallets* is Brave's native wallet extension. Best practise for security is to disable extensions when they are not in use. See [here](https://coinguides.org/metamask-security/) for a list of recommended Metamask settings and some of the common scams in play.

After installing the extension, you have the option to import a previous wallet using a recovery phrase or create a new one.

<p align="left"><img width="600" alt="MetaMask create screen" src="https://user-images.githubusercontent.com/39792005/188044930-e8934667-f578-4e81-a37b-94a11e4c888e.png"></p>

MetaMask will provide you with a *Secret Recovery Phrase* (often called a seed phrase), and ask you to securely store the words and then submit them back in the correct order. It is very important to keep this recovery phrase of 12 words **private** and **secure**. (Even if only using for testnet activity it is wise crypto behaviour to become comfortable with self custody.)

<p align="left"><img width="600" alt="MetaMask Secret Recovery Phrase" src="https://user-images.githubusercontent.com/39792005/188044954-8da4e5bd-e167-4e8d-9c2d-1c124cfc6c08.png"></p>

After creating a password, watching the video, writing down your phrase, and re-entering your phrase, you'll be at the interface ready to use your new account address (the one shown here is `0x99A95d4d7DDe6B9E663509a41CF3A9eeAfC07Ad9`) in any of the chains that accept Ethereum based addresses.

<p align="left"><img width="800" alt="MetaMask interface" src="https://user-images.githubusercontent.com/39792005/188044996-51bd22f0-1661-4646-9634-840ec3df62ab.png"></p>

## Hierarchical Deterministic (HD) Wallets


