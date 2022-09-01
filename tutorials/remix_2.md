# Remix Part II - Wallets

Remix Part I looked at using the IDE to compile and deploy smart contracts; remix comes with some stock-standard contracts for storage, ownership, etc. These get compiled within the virtual machine (VM) environment that runs within your browser instance. From the [docs](https://remix-ide.readthedocs.io/en/latest/run.html):

> For connecting to a sandbox blockchain in the browser. The Remix VM (previously called JavaScript VM) is its own “blockchain” and on each reload the old chain will be cleared and a new blockchain will be started. The old one will not be saved. The London refers to the London fork of Ethereum.

The next step we'll look at is to connect our Remix environment to a wallet. As it stands now we have access to 10 dummy test accounts that are preloaded with 100 ETH. These accounts are ephemeral and transaction history will not be saved--or mined to the blockchain for that matter.
