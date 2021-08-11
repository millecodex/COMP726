# Tutorial 5: Its time to build!

For the next few weeks we're going to look at a common system for writing smart contracts (snippets of code) that can be deployed to and interact with Ethereum. 

*Note:* Most students want to build an app that interacts with a blockchain and this is what learning some solidity can help you with. You are not required to use Solidiy/Ethereum for your project; see [below](#developer-learning-tools) for a list of some alternatives. This is simply informative to give you an idea of whats possible. You are encouraged to use whatever tech/IDE/language/system that interests you. Some students are interested in other aspects of blockchains (not SC-based apps) and that is great too! 

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
Head to [remix.ethereum.org](https://remix.ethereum.org/) to get started. Find the LEARNETH tutorials.![LearnEth](https://user-images.githubusercontent.com/39792005/128951882-1708100a-927e-48a9-8e51-947c37d3f4f2.PNG)
Check the plugins tab to make sure LearnEth is in the Active Modules list. Additionally the Solidity compiler needs to be active.

***error loading: undefined***
If you are getting an error try with your laptop and alternately try the links below to a different resource. I have been having an issue using this plugin on the network.



## Developer Learning Tools
Some links that may be helpful:
- [ethereum.org](https://ethereum.org/en/developers/learning-tools/) developer learning tools
- [Eth.Build](https://eth.build/) has a drag and drop interface
- [CryptoZombies](https://cryptozombies.io/en/solidity) is a very popular game to help you learn
- Jeff has some videos on Remix. (These are over a year old so you may have to set your compiler accordingly.)
  - [Playlist on youtube](https://www.youtube.com/watch?v=bqyrRS5AN00&list=PLWdMs73ohrSn2ZnaiOQi-3WpVjKXazUkF)
  - [Remix Part I: deploy an empty contract: helloWorld](https://www.youtube.com/watch?v=bqyrRS5AN00)
  - [Remix Part II: Function Call and visibility](https://www.youtube.com/watch?v=dRZIBw-2DO8)
  - [Remix Part III: Gas](https://www.youtube.com/watch?v=BY4o0Qqlh-4)
- [Solidity by example](https://docs.soliditylang.org/en/v0.8.6/solidity-by-example.html) has example smart contracts you can follow to see how features are implemented
