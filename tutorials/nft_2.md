# Tutorial 10: NFTs Part II

## 🛠️ Under Construction 🚧 👷
## Contents
1. [intro](nft_2.md#intro)
1. [What did we miss?](nft_2.md#what-did-we-miss)
1. [Further Reading - the very short list](nft_2.md#further-reading---the-very-short-list)
1. [Exercises](nft_2.md#exercises)
1. [Sample Code](nft_2.md#sample-code)

In NFTs [Part I](./nft_1.md) we wrote a smart contract to mint an [ERC721](./nft_1.md#erc-721) (NFT) token for our Course Credits app. We used Hardhat to create our app and Alchemy to communicate with Ethereum and MetaMask to sign transactions. Finally we compiled our contract with Hardhat and deployed to Ethereum's testnet Goerli chain.

Here in Part II we will interact with the smart contract and mint our NFT.
# Environment Prerequisites
 * [Same from last time](https://github.com/millecodex/COMP726/blob/master/tutorials/nft_1.md#prerequisites), plus
 * Get yourself a [Pinata](https://app.pinata.cloud/register) account; this is for decentralised storage

## Install [Alchemy's Web3 library](https://docs.alchemyapi.io/alchemy/documentation/alchemy-web3)\
In your home directory type `npm install @alch/alchemy-web3`; a number of packages will be added to your environment

Go to your `\scripts` directory and create a new file called `mint-nft.js`
```js
require("dotenv").config()
const API_URL = process.env.API_URL
const { createAlchemyWeb3 } = require("@alch/alchemy-web3")
const web3 = createAlchemyWeb3(API_URL)
```
Note here that you have already installed the `dotenv` package from last time. The Alchemy package was downloaded in the previous step.

## Prepare the contract ABI
ABI is the *application binary interface* which is the computer science way of saying the code that directly interacts with the blockchain. In this case the Ethereum virtual machine. (More on the EVM here.)

To your `mint-nft.js` script add the following:
```js
const contract = require("../artifacts/contracts/courseNFT.sol/courseNFT.json")
console.log(JSON.stringify(contract.abi))
```
and run the script: `node scripts/mint-nft.js`. The last line we added `console.log` should write the ABI to the console. You can see the `json` in your `/contracts` folder.

## Pinata
NFTs need metadata to differentiate each one (the non-fungible bit). In our example of the Course Credits App, this will be fields like Name, ID, Course, Grade, Date, etc. For a PFP it might be character traits like colour, accessory, logo, shirt, background, and so on.

Login to Pinata and click the `Ipload+` button selecting a file. Any file will do. Satoshi's certificate is [here](https://github.com/millecodex/COMP726/blob/master/my-nft-app/Satoshi-cert.png) if you want to use the same one. Upload your file and after the dashboard refreshes you'll see it along with a content identifier (CID).

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
Change the IPFS link CID to yours. You can edit the other characteristics too. Save the `.json` file and upload it to Pinata.




## Create a contract instance
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

Update the mint-nft.js file to include your public and private keys and setup the transaction (`const tx = {`):
```js
require("dotenv").config()
const API_URL = process.env.API_URL
const PUBLIC_KEY = process.env.PUBLIC_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;

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

## Call the mint
Add the mint with the pinata hashdata `mintNFT("ipfs://QmXd6V3ASnzZpToshcwLZkLRxHxduZKeKSXj4zhHWQUcjB")`


# Up Next
* Next tutorial we are looking to scaling via layer two solutions -- i.e. the Lightning network

# Further Reading - the very short list
* This has been based on this [Tutorial](https://ethereum.org/en/developers/tutorials/how-to-mint-an-nft/) from Ethereum.org
* https://nftschool.dev/ looks like a promising resource

# Exercises
1. Write a script to generate a new random NFT every time that mint is called.

# Sample code
Files be found [here]()
