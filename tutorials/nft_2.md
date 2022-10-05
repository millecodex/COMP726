# Tutorial 10: NFTs Part II

## Contents
1. [Intro](nft_2.md#intro)
1. [Alchemy's Web3 Library](nft_2.md#alchemys-web3-library)
1. [Contract ABI](nft_2.md#contract-abi)
1. [Pinata](nft_2.md#pinata)
1. [Minting Script](nft_2.md#minting-script)
1. [Call the mintNFT function](nft_2.md#call-the-mintnft-function)
2. [View your NFT in MetaMask](nft_2.md#view-your-nft-in-metamask)
3. [What did we miss?](nft_2.md#what-did-we-miss)
4. [Further Reading - the very short list](nft_2.md#further-reading---the-very-short-list)
5. [Exercises](nft_2.md#exercises)
6. [Sample Code](nft_2.md#sample-code)

# Intro
In NFTs [Part I](./nft_1.md) we wrote a smart contract to mint an [ERC721](./nft_1.md#erc-721) (NFT) token for our Course Credits app. We used Hardhat to create our app and Alchemy to communicate with Ethereum and MetaMask to sign transactions. Finally we compiled our contract with Hardhat and deployed to Ethereum's testnet Goerli chain.

Here in Part II we will interact with the smart contract and mint our NFT.

## Environment Prerequisites
 * [Same from last time](https://github.com/millecodex/COMP726/blob/master/tutorials/nft_1.md#prerequisites), plus
 * Get yourself a [Pinata](https://app.pinata.cloud/register) account; this is for decentralised storage

# Install [Alchemy's Web3 library](https://docs.alchemyapi.io/alchemy/documentation/alchemy-web3)
In your home directory type `npm install @alch/alchemy-web3`; a number of packages will be added to your environment

Go to your `\scripts` directory and create a new file called `mint-nft.js`
```js
require("dotenv").config()
const API_URL = process.env.API_URL
const { createAlchemyWeb3 } = require("@alch/alchemy-web3")
const web3 = createAlchemyWeb3(API_URL)
```
Note here that you have already installed the `dotenv` package from last time. The Alchemy package was downloaded in the previous step.

# Contract ABI
ABI is the *application binary interface* which is the result after compiling our contract code. It *interfaces* the human-readable program language with the EVM executable bytecode. (EVM is the Ethereum Virtual Machine which does all the computation.) 

To your `mint-nft.js` script add the following:
```js
const contract = require("../artifacts/contracts/courseNFT.sol/courseNFT.json")
console.log(JSON.stringify(contract.abi))
```
and run the script: `node scripts/mint-nft.js`. The last line we added `console.log` should write the ABI to the console. You can see the `json` in your `/contracts` folder.

# Pinata
NFTs need metadata to differentiate each one (the non-fungible bit). In our example of the Course Credits App, this will be fields like Name, ID, Course, Grade, Date, etc. For a PFP it might be character traits like colour, accessory, logo, shirt, background, and so on.

Login to Pinata and click the `Upload+` button selecting a file. Any file will do. Satoshi's certificate is [here](https://github.com/millecodex/COMP726/blob/master/my-nft-app/Satoshi-cert.png) if you want to use the same one. Upload your file and after the dashboard refreshes you'll see it along with a content identifier (CID).

![pinata-pinned](https://user-images.githubusercontent.com/39792005/193709900-4442e908-e670-4240-bad3-2723515ff771.png)

You can view your file here: `https://gateway.pinata.cloud/ipfs/<CID>`

## Metadata
Back in your root directory create a new file: `nft-metadata.json` that contains:
```json
{
    "attributes": [
      {
        "trait_type": "Course",
        "value": "Cryptocurrency"
      },
      {
        "trait_type": "Name",
        "value": "Satoshi Nakamoto"
      }
    ],
    "description": "Course Credits Certificate in Cryptocurrency",
    "image": "ipfs://QmVxFXNuVJdk5QFzvkpSSeXypdDsCf8LET1kDnkZQBFyvj",
    "name": "Course Credit Certificate"
  }
```
Change the IPFS link CID image link to yours. You can edit the other characteristics too (or add more). Save the `.json` file and upload it to Pinata. Upload the `nft-metadata.json` file to Pinata.

Check that its been uploaded to the IPFS via Pinata. Copy your CID hash from pinata and create a URL:\
https://gateway.pinata.cloud/ipfs/QmXd6V3ASnzZpToshcwLZkLRxHxduZKeKSXj4zhHWQUcjB

# Minting Script
Get your contract address from Part I, mine is `0xdda15afec918308e8c20f70fb5090ca134063598`.

Add the following to the `mint-nft.js` file:
```js
const contractAddress = "0xdda15afec918308e8c20f70fb5090ca134063598"
const nftContract = new web3.eth.Contract(contract.abi, contractAddress)
```

Add your public key to your `.env` file. It should now look like:
```
API_URL="https://eth-goerli.g.alchemy.com/v2/EUd...crz"
PRIVATE_KEY="97a...b3d"
PUBLIC_KEY="0x99A95d4d7DDe6B9E663509a41CF3A9eeAfC07Ad9"
```

Update the `mint-nft.js` file to include your public and private keys and setup the transaction:
```js
require("dotenv").config()
const API_URL = process.env.API_URL
const PUBLIC_KEY = process.env.PUBLIC_KEY
const PRIVATE_KEY = process.env.PRIVATE_KEY

const { createAlchemyWeb3 } = require("@alch/alchemy-web3")
const web3 = createAlchemyWeb3(API_URL)
const contract = require("../artifacts/contracts/courseNFT.sol/courseNFT.json")
const contractAddress = "0xdda15afec918308e8c20f70fb5090ca134063598"
const nftContract = new web3.eth.Contract(contract.abi, contractAddress)

async function mintNFT(tokenURI) {
  const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest'); //get latest nonce

//the transaction
  const tx = {
    'from': PUBLIC_KEY,
    'to': contractAddress,
    'nonce': nonce,
    'gas': 500000,
    'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI()
  };
}
```

## Sign the transaction
**Don't trust, verify!** When we send the transaction we need to sign it. For this we need access to our `PRIVATE_KEY` variable; remember this is only stored locally in the `.env` file. Add this code to `mint-nft.js`. Most of the code below is for error logging.
```js
const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY)
    signPromise
        .then((signedTx) => {
        web3.eth.sendSignedTransaction(
            signedTx.rawTransaction,
            function (err, hash) {
            if (!err) {
                console.log(
                "The hash of your transaction is: ",
                hash,
                "\nCheck Alchemy's Mempool to view the status of your transaction!"
                )
            } else {
                console.log(
                "Something went wrong when submitting your transaction:",
                err
                )
            }
        }
        )
        })
        .catch((err) => {
        console.log(" Promise failed:", err)
    })
```

# Call the mintNFT function
Lastly call `mintNFT` by adding the following:
```js
mintNFT("ipfs://QmXd6V3ASnzZpToshcwLZkLRxHxduZKeKSXj4zhHWQUcjB")
```
The complete `mint-nft.js` file is [here](https://github.com/millecodex/COMP726/tree/master/my-nft-app/scripts). Now run the script from the command line:
```
> node scripts/mint-nft.js
```
Success looks like 
```
C:\my-nft-app>node scripts/mint-nft.js
The hash of your transaction is:  0x4877840a2e1e21f0cbeacc64801d629e816da93a33f02713697047c027b66cc2
Check Alchemy's Mempool to view the status of your transaction!
```
Go to your Alchemy dashboard to see the recent activty. You can also see it on goerli.etherscan.io.

![goerli-successful-mint](https://user-images.githubusercontent.com/39792005/193971526-f3d7fcc6-8af9-4b0d-85bf-6bb9e9c9c200.png)

## Error: Transaction has been reverted by the EVM:
You may get an error if you used a different account to call the contract. Searching the txid on [goerli.etherscan.io](https://goerli.etherscan.io/tx/0x5a17ff868fc9e099f94ecb3ff43188698d2bccac9b9c982dbc29ad1d105e6be3) this can look like: 

![goerli-error](https://user-images.githubusercontent.com/39792005/193970215-e2fd7e1e-8f9f-4783-8516-177c38788765.png)

We're told that `Fail with error 'Ownable: caller is not the owner'` which is a permissions issue.

# View your NFT in MetaMask
To view your freshly minted certificate go back to MetaMask and select collectibles. You need to tell MetaMask what contract to look in, and the tokenID. So put in the contract address `0x2bb13D3d4F60592611bc4910394aDFC1B4A9EF7C` and the tokenID `ccNFT` and the decimals `0` (no fractional NFTs here!). I've minted two so my balance is 2.

![token-import-metamask-combined](https://user-images.githubusercontent.com/39792005/194160772-c9454bb3-047f-4166-9e47-379b174b7aa4.png)

> **Note** Presently you can see the NFTs in your MetaMask wallet only as tokens. There is not yet native support for viewing custom NFTs (as images). See more: https://metamask.zendesk.com/hc/en-us/articles/360058238591-NFT-tokens-in-your-MetaMask-wallet

# Up Next
* In the next tutorial we are looking al scaling via layer two solutions -- i.e. the Lightning network

# Further Reading - the very short list
* This has been based on this [Tutorial](https://ethereum.org/en/developers/tutorials/how-to-mint-an-nft/) from Ethereum.org
* https://nftschool.dev/ looks like a promising resource

# Exercises
1. Change the metadata and mint another NFT.
2. Investiage how to actually view your NFT certificate that is stored on IPFS via Pinata.
3. Write a script to generate a new random NFT every time `mint` is called.

# Sample code
Files be found [here](https://github.com/millecodex/COMP726/tree/master/my-nft-app). Note your addresses will be different!
