# Tutorial 6: Its time to build!

For the next few weeks we're going to look at a common system for writing smart contracts (snippets of code) that can be deployed to and interact with Ethereum. 

*Note:* Most students want to build an app that interacts with a blockchain and this is what learning some solidity can help you with. You are not required to use Solidiy/Ethereum for your project; see [below](#alternate-developer-learning-tools) for a list of some alternatives. This is simply informative to give you an idea of whats possible. You are encouraged to use whatever tech/IDE/language/system that interests you. Some students are interested in other aspects of blockchains (not SC-based apps) and that is great too! 

## Solidity
[Solidity](https://docs.soliditylang.org) is a programming language developed specifically to create smart contracts to be executed by the Ethereum virtual machine (EVM). It looks a lot like javascript. The benefit of learning some solidity is that it is widely used, has been around for a long time (relative to other SC languages) and so has support libraries.

Example solidity contract that can ouptut a string: *"Hello there amigo"*
```
/* basic contract structure:
 * https://solidity.readthedocs.io/en/v0.7.1/structure-of-a-contract.html
 */
pragma solidity ^0.7.1;

contract helloWorld{

    function hello() public pure returns(string memory){
        //this function call should be free; check gas
        return 'Hello there amigo';
    }
}
```

## Remix
Head to [remix.ethereum.org](https://remix.ethereum.org/) to get started. Find the LEARNETH tutorials. Note the **Scam Alert** message and always check your URLs.

<p align="center"><img width="" alt="remix_IDE_0 25 3" src="https://user-images.githubusercontent.com/39792005/186281481-9131b786-dc75-48ee-88b6-09d66ee63d82.PNG"></p>

Check the plugins tab to make sure LearnEth is in the Active Modules list. Additionally the Solidity compiler needs to be active. See the [docs](https://remix-learneth-plugin.readthedocs.io/en/latest/index.html) for more info on how to select a tutorial and get started.

<p align="left"><img width="400" alt="plugin_manager_remix" src="https://user-images.githubusercontent.com/39792005/186283135-fc0d374a-2c34-4ec5-815b-4c50c5fd29c0.PNG"></p>


---
***error loading: undefined***
<p align="left"><img width="300" alt="remix_error" src="https://user-images.githubusercontent.com/39792005/186282091-0b5edc91-5fad-4831-99c3-221b895c346b.PNG"></p>
If you are getting an error try with your laptop and alternately try the links below to a different resource. I have been having an issue using this plugin on the 
network.

---
If this tutorial seems too advanced, consider starting with the playlist of videos below or the CryptoZombies game.

## Developer Learning Tools & Resources
Some links that may be helpful:
- [ethereum.org](https://ethereum.org/en/developers/learning-tools/) developer learning tools
- The whole shebang from FreeCodeCamp - [Web3 Ultimate Course](https://github.com/smartcontractkit/full-blockchain-solidity-course-js)
- YouTube tutorial by [Nader Dabit](https://github.com/dabit3/full-stack-ethereum) - [Full-stack ethereum development](https://www.youtube.com/watchv=a0osIaAOFSE&ab_channel=NaderDabit)
- Still one of the best is [CryptoZombies](https://cryptozombies.io/) - a tutorial for you to build a game similar to [CryptoKitties](https://www.cryptokitties.co/)
- Jeff has some videos on Remix. (These are over a year old so you may have to set your compiler accordingly.)
  - [Playlist on youtube](https://www.youtube.com/watch?v=bqyrRS5AN00&list=PLWdMs73ohrSn2ZnaiOQi-3WpVjKXazUkF)
  - [Remix Part I: deploy an empty contract: helloWorld](https://www.youtube.com/watch?v=bqyrRS5AN00)
  - [Remix Part II: Function Call and visibility](https://www.youtube.com/watch?v=dRZIBw-2DO8)
  - [Remix Part III: Gas](https://www.youtube.com/watch?v=BY4o0Qqlh-4)
- [Solidity by example](https://docs.soliditylang.org/en/v0.8.6/solidity-by-example.html) has example smart contracts you can follow to see how features are implemented

## Alternate Developer Learning Tools
You may want to build on other blockchains, for example:
- Avalanche: [docs](https://docs.avax.network/), [sample tutorials](https://docs.avax.network/community/tutorials-contest/2022)
- Substrate/Polkadot: [docs](https://docs.substrate.io/), [sample tutorials](https://wiki.polkadot.network/docs/learn-video-tutorials)
- Solana: [docs](https://docs.solana.com/), [sample tutorials](https://github.com/solana-labs/example-helloworld)
- Fantom: [docs](https://docs.fantom.foundation/), [sample tutorials](https://blog.chain.link/how-to-build-and-deploy-a-smart-contract-on-the-fantom-blockchain/)
- BinanceBNB: [docs](https://docs.bnbchain.org/docs/bnbIntro), [sample tutorials](https://docs.bnbchain.org/docs/bsc-tutorials/)
- Cosmos: [docs](https://docs.cosmos.network/), [sample tutorials](https://tutorials.cosmos.network/)
