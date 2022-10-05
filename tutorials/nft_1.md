# Tutorial 9: NFTs
### Contents
1. [Intro](nft_1.md#intro)
1. [Fungible vs Not](nft_1.md#fungible-vs-non-fungible)
1. [Ethereum Token Standards](nft_1.md#ethereum-token-standards)
1. [Prerequisited - Set up the environment](nft_1.md#prerequisites)
1. [Deploy an NFT Contract](nft_1.md#lets-deploy-an-nft-contract)
1. [Up Next](nft_1.md#up-next)
1. [Further Reading - the very short list](nft_1.md#further-reading---the-very-short-list) 
1. [Exercises](nft_1.md#exercises)
1. [Sample Code](nft_1.md#sample-code)

# Intro
[Earlier](https://github.com/millecodex/COMP726/blob/master/tutorials/archimate.md) we laid out the basics for an app that tracks student progression. Teachers had the authority to confer qualifications upon a student after completing a course (or at checkpoints along the way). Somthing like a qualification certificate is a perfect use case for a non-fungible token. Most paper documents of this sort contain some basic info: title, name, date, authority, potential expiry, logo or signature, etcetera. Lets say you wanted to present your diploma to an institution to prove that you had already completed some Programming classes, it is likely the diploma would not be enough. The registrar at the potential school would have to contact your previous school to validate the claim. If only there was a trustless decentralised system that allowed for easy verification? Hmm....

# Fungible vs Non-fungible
**Q: Are Coins Tokens?**

If you have some bitcoin or ether, yes, these are digital tokens because they are fungible, secure, scarce, transferrable, and have monetary value and utility. (Bitcoin's utility is widely considered to be a store-of-value.) Its confusing at first but there is a difference between value and utility. In Bitcoin's case the utility *is* value. For Ethereum there is broader application, e.g., using ether to purchase an NFT or invest in a new project or pay gas fees. Many tokens claim some form of utility and let value be determined by a market. It is a regulatory grey area when it comes to classifying tokens as securities or otherwise, and has implications for taxation and reporting.

### Non-Fungible
Currency tokens (and cash) are interchangeable, or fungible, because it doesn't matter what specific token you have, everyone agrees on the same value. If people were willing to pay a premium for specific tokens or characteristics, then the overall utility of the medium as money begins to fall apart. This is the problem with barter; there is far too much subjective difference in value between objects for people to easily exchange goods directly. 

Think of paintings in a gallery. All the paintings are similar in many respects─composed of paint, multicolour, framed canvas, 2-dimensional, etc.─however, each painting is obviously unique with value determined by many external factors. Non-fungible tokens, where each unit is unique, are designed for this purpose. In a digital manner they implement security and scarcity. Value and use are subjective like gallery paintings, but these now inherit the open, permissionless, censorship-resistant properties of the blockchain.

NFTs aren't just for collectibles, art, and profile pictures. Any document or data structure that can be digitised can be represented as an NFT: music, certificates, degrees, licenses, passes, patents, title deeds, concert tickets, contracts, voting rights, et-cetera.

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

# Prerequisites
We'll need the following tools in our environment before we can get going.
1. **MetaMask** account with some testnet ether. See our previous steps for this [here](https://github.com/millecodex/COMP726/blob/master/tutorials/remix_2.md#metamask).
2. **Alchemy** account to communicate with Ethereum. Head to https://www.alchemy.com/ and sign up for free. We listed this as an option to get Goerli testnet ETH. The Alchemy accounts allows you to communicate with an Ethereum full node via an API. Other ways to do this are through your own hosted full node, or through [Infura](https://infura.io/), for example.
3. **Node.js** for running javascript applications ([download link](https://nodejs.org/en/download/)), and **NPM** the node package manager to download and install packages. Windows and Mac install instructions [here](https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac).

# Let's Deploy an NFT Contract
### 1. Create your app in Alchemy by clicking `Create App` from the `Apps` menu.

![Alchemy_create_app](https://user-images.githubusercontent.com/39792005/192390028-0b8106c4-fd90-4556-a735-a4afaf96706d.png)

### 2. Use Alchemy's API to check your MetaMask account balance 
The `Composer` tool will create a query to post to the blockchain. In this case its using a JSON RPC. I'll use the account address that (should) already have testnet `ETH`

![Alchemy_composer](https://user-images.githubusercontent.com/39792005/192390914-dde3f9bd-76f9-417e-9ba1-db257eb8b9db.png)

And the response:

![Alchemy_getbalance_response](https://user-images.githubusercontent.com/39792005/192390951-d3dd3dd8-186c-4917-b52d-89eadb60e762.png)

This value `"result":"0x16d2798836302a2"` is in hexadecimal and can be [converted](https://www.rapidtables.com/convert/number/hex-to-decimal.html) to decimal as `102781902492205730`. Recall that ether has 18 decimal places, and this value is in `wei`. Dividing by $10^{18}$ gives us `0.10278` ETH.

### 3. Initialize a new package with NPM:
   - (i)   Create a new working directory for your project: `mkdir my-nft-app`
   - (ii)  Navigate there: `cd mkdir my-nft-app`
   - (iii) Initialize package: `npm init`. I answered as follows with blanks for `test command`, `git repository`, and `keywords`:

```json
{
  "name": "my-nft-app",
  "version": "1.0.0",
  "description": "NFTs for course credits",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Jeff",
  "license": "ISC"
}
```

### 4. Install [Hardhat](https://hardhat.org/hardhat-runner/docs/getting-started#overview) 
Within your app directory type: `npm install --save-dev hardhat`. Hardhat is a dev environment for Ethereum that helps with deploying & debugging smart contracts & apps and all that jazz.
### 5. Create a new Hardhat project
Within your app directory type: `npx hardhat` and select `Create an empty hardhat.config.js` to see a welcome message

![hardhat_welcome_message](https://user-images.githubusercontent.com/39792005/192395287-db1aee49-7534-4048-a805-53089b6917db.png)

### 6. The Smart Contract code
   - (i) Create a folder for organization: Type `mkdir contracts`
   - (ii) Create a new file in the `\contracts` folder; mine is called `courseNFT.sol` This code is based on the [OpenZeppelin](https://docs.openzeppelin.com/contracts/3.x/erc721) standard. Copy and paste the code (file is [here](https://github.com/millecodex/COMP726/blob/master/my-nft-app/contracts/courseNFT.sol)). You can modify the name and tokenID in the constructor: `constructor() ERC721("courseNFT", "ccNFT") {}`. The name `courseNFT` must match the contract name. Save the file.
   - (iii) Install the OpenZeppelin Library via: `npm install @openzeppelin/contracts`
 
 ### 7. Connect MetaMask and Alchemy by storing our details in an environment file
   - (i) Get your Alchemy API URL by clicking `VIEW KEY` in your dashboard. It should look like: `https://eth-goerli.g.alchemy.com/v2/FU3d...dctz`
   - (ii) Export your private key from MetaMask by clicking the hamburger menu, `Account Details`, and `Export Private Key`

![MetaMask_export](https://user-images.githubusercontent.com/39792005/192399646-f63ffc2f-4963-489a-8ff4-6a3dfb3dfad3.png)

   - (iii) Create an environment file to store our keys. From the command line: `npm install dotenv --save`. Now create a `.env` file that contains:

```
API_URL="https://eth-goerli.g.alchemy.com/v2/FU3d3...cdctz"
PRIVATE_KEY="97a08...be6b3d"
```

> **Warning** \
> Never commit these with version control like git or GitHub! If you do so accidentally they must be regenerated immediately.

### 8. Install ether.js 
Back at the command line: `npm install --save-dev @nomiclabs/hardhat-ethers ethers@^5.0.0`

### 9. Update hardhat.config.js
In the project root directory edit the `hardhat.config.js` file with all of our information:
```js
/**
* @type import('hardhat/config').HardhatUserConfig
*/
require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
const { API_URL, PRIVATE_KEY } = process.env;
module.exports = {
   solidity: "0.8.1",
   defaultNetwork: "goerli",
   networks: {
      hardhat: {},
      goerli: {
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY}`]
      }
   },
}
```
### 10. Compile the contract
In the command line compile the contract with Hardhat: `npx hardhat compile`. You should get a success message:

![hardhat_compile](https://user-images.githubusercontent.com/39792005/192401736-2682279c-80ef-45bc-ace8-40dcb0914e86.png)

If you have already compiled the contract and nothing has changed, then the message will say: `Nothing to compile`

### 11. Write the deploy script 
In your project root create a folder for organization. Type `mkdir scripts`. Create a new file called `deploy.js` in the `\scripts` folder. It will contain:
```js
async function main() {
    const CourseNFT = await ethers.getContractFactory("courseNFT")
  
    // Start deployment, returning a promise that resolves to a contract object
    const courseNFT = await CourseNFT.deploy()
    await courseNFT.deployed()
    console.log("Contract deployed to address:", courseNFT.address)
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error)
      process.exit(1)
    })
``` 

### 12. Deploy the contract 
In the command line: `npx hardhat --network goerli run scripts/deploy.js` and you should get a response address where the contract now lives (permanently) on the (testnet) blockchain!

![hardhat_contract_deployed](https://user-images.githubusercontent.com/39792005/192403178-b798cbb5-71a4-4bda-a947-0abcc4fa040b.png)

Copy the address and go to https://goerli.etherscan.io/ and search for it.

![goerli_scan_contract_deployment](https://user-images.githubusercontent.com/39792005/192403228-b22f0a34-8905-45a0-b28f-978928b60d14.png)

Remember your Alchemy dashboard? It now will register the details. Check that the `from` address matches your MetaMask.

![Alchemy_contract_deploy_receipt](https://user-images.githubusercontent.com/39792005/192403486-9e629a6c-78a0-4627-9bf2-9980c1568315.png)

# Up Next
* What can we do with our contract? We'll call it ofcourse. In the next [tutorial](https://github.com/millecodex/COMP726/blob/master/tutorials/nft_2.md) we'll look into calling the mint function.

# Further Reading - the very short list
* This has been based on this [Tutorial from Ethereum.org](https://ethereum.org/en/developers/tutorials/how-to-write-and-deploy-an-nft/)
* https://nftschool.dev/ looks like a promising resource

# Exercises
1. What are some examples of fungible tokens compared to non-fungible tokens that you use that are not blockchain related?
2. How much gas did you pay to deploy your contract? What are some implications of the gas auction fees model?

# Sample code
Files be found [here](https://github.com/millecodex/COMP726/blob/master/my-nft-app/)
