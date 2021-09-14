# Substrate
Substrate is a blockchain framework for developers. The modular approach allows the creator to use pre-existing components for their blockchain that are time consuming to develop and risky to deploy if not tested thouroughly. The plug-and-play modules can be interchanged, for example, swapping out a proof-of-work consensus mechanism for instant finality. Additional components (pallets) can be addedd as necessary or created from scratch.

<img width="800" alt="substrate_modules" src="https://user-images.githubusercontent.com/39792005/133334949-eb949e8a-9d38-4d33-b007-7021730de4a7.png">
 
The pieces of a blockchain can be abstracted into the following modules:
* Storage backend; need to keep the state of the chain
* P2P Networking Layer; how to communicate updates / message passing
* Transaction Queue; ordering of events - what gets processed into a block?
* Consensus Engine; agreement on the state of the chain
* Runtime logic; what the blockchain does, business logic, the state transition function

A standalone client like Bitcoin core has all of the above coded into its base. If someone wanted to create a new blockchain with most of Bitcoin's functionality they would have recode (or copy and refactor) all the modules. This is the motivation behind creating Substrate.

## Nodes
A standalone node architecture:

<img width="800" alt="substrate_architecture" src="https://user-images.githubusercontent.com/39792005/133337126-e304dcbe-6663-435e-92d5-a090820b21bb.png">

The runtime logic is the specific funtionality that is required of the chain. For Bitcoin this is a ledger (the unspent-transaction output set). For Ethereum this is the virtual machine that is capable of arbitrary calculation. For Polkadot this is keeping track of the heads of the parachains. The entire node is written in Rust, however the Runtime is *also* compiled into web assembly (Wasm) and this means that so-called *forkless upgrades* are possible.

There are four pre-made node arrangements in the package we'll be looking at:
```
+-- nodes
	|
	+-- basic-pow
	|
	+-- hybrid-consensus
  	|
  	+-- kitchen-node
	|
	+-- rpc-node
```
Each node is ready to go but has been configured with different with different parameters. When these are up and running they will represent *different* blockchains. We'll be running the `kitchen-node`.

## 1.  Development Environment
Substrate is written in [rust](https://www.rust-lang.org/) and so a rust compiler is necessary to run any substrate based blockchain. On a linux/macOS system, you can run this [script](https://getsubstrate.io/) for autoconfiguration:\
`$ curl https://getsubstrate.io -sSf | bash -s -- --fast`

If you are using Windows I **do not** recommend attempting to configure rust/substrate, rather [install WSL](https://devblogs.microsoft.com/commandline/install-wsl-with-a-single-command-now-available-in-windows-10-version-2004-and-higher/) (Windows Subsystem for Linux).

More detail about various OS configurations (including Apple arm M1s) is at [substrate.dev](https://substrate.dev/docs/en/knowledgebase/getting-started/).

We will be running a specific configuration of substrate found in the [Recipes](https://substrate.dev/recipes/) cookbook. Clone the Substrate recipes repo:\
`$ git clone https://github.com/substrate-developer-hub/recipes.git`

## 2.  Get your Blockchain Running
### Backend
Navigate to the `\recipes` directory and build the binary. This will take a while the first time you do it because all the dependencies get compiled.

Build using the flag `--release` which builds without the debug option and is quicker:\
`$ cargo build --release`

In the `\nodes` folder there are four different nodes (see above). Build the node called `kitchen-node`:\
`$ cargo build --bin kitchen-node --release`

Run the compiled binary, here using development `--dev` mode and a temporary storage directory `--tmp`):\
`$ cargo run --bin kitchen-node -- --dev --tmp`

If successful we will get a lot of useful output. Note the node we're running in line 2, a generated name (6), the runtime (9) -- more on this in a moment, and the ''blockchain'' being processed (>16). This will continue in idle mode every 5 seconds or until a transaction is processed at which point a block will be added to the chain.
```
1 2021-09-14 16:20:18 Running in --dev mode, RPC CORS has been disabled.    
2 2021-09-14 16:20:18 Kitchen Node    
3 2021-09-14 16:20:18 ✌️  version 3.0.0-98d3625-x86_64-linux-gnu    
4 2021-09-14 16:20:18 ❤️  by Substrate DevHub <https://github.com/substrate-developer-hub>, 2019-2021    
5 2021-09-14 16:20:18 📋 Chain specification: Development    
6 2021-09-14 16:20:18 🏷 Node name: embarrassed-pollution-8954    
7 2021-09-14 16:20:18 👤 Role: AUTHORITY    
8 2021-09-14 16:20:18 💾 Database: RocksDb at /tmp/substratew3PomX/chains/dev/db    
9 2021-09-14 16:20:18 ⛓  Native runtime: super-runtime-1 (super-runtime-1.tx1.au1)    
10 2021-09-14 16:20:19 🔨 Initializing Genesis block/state (state: 0x09b1…a1ef, header-hash: 0x0725…9fda)    
11 2021-09-14 16:20:19 Using default protocol ID "sup" because none is configured in the chain specs    
12 2021-09-14 16:20:19 🏷 Local node identity is: 12D3KooWLvczW8BaJ1yhB4j6en7PQrJMwQw2aUUUAU7RjNm639W3    
13 2021-09-14 16:20:19 📦 Highest known block at #0    
14 2021-09-14 16:20:19 〽️ Prometheus server started at 127.0.0.1:9615    
15 2021-09-14 16:20:19 Listening for new connections on 127.0.0.1:9944.    
16 2021-09-14 16:20:24 💤 Idle (0 peers), best: #0 (0x0725…9fda), finalized #0 (0x0725…9fda), ⬇ 0 ⬆ 0    
17 2021-09-14 16:20:29 💤 Idle (0 peers), best: #0 (0x0725…9fda), finalized #0 (0x0725…9fda), ⬇ 0 ⬆ 0    
```

The local substrate node (called the kitchen node) is running on your local machine waiting for input to process as a new block in the chain. To manipulate this input we need to call the appropriate functions in the program. If only there was a frontend interface to help...🤔

### Frontend
Conveniently, the super shadowy coders over at Polkadot have done just this. Head to [polkadot.js.org/apps](https://polkadot.js.org/apps/#/) to see a live interface to the Polkadot blockchain.\
<img width="800" alt="polkadot_explorer" src="https://user-images.githubusercontent.com/39792005/133219965-35567470-3a12-4558-aac8-641685c0a58c.png">\
If our node is running (you can see it has a local server connection at `127.0.0.1:9615`) then you can switch the explorer to view your node. Select the main Polkadot button (light blue box) and choose Development -> Local Node -> Switch.
<img width="800" alt="polkadot_explorer_switch" src="https://user-images.githubusercontent.com/39792005/133219220-0c959267-8456-4d0b-8189-82c5e9b1f1a3.png">
> Sidebar: you can explore all sorts of chains and parachains that are connected through the polkadot network from the Development dropdown.

You now have a (nearly) fully functioning front-end to your substrate node. This is in orange, possibly to avoid the risk of developing and interacting on the real (pink) Polkadot chain.
<img width="800" alt="substrate_frontend" src="https://user-images.githubusercontent.com/39792005/133219675-ffdd526c-e333-4c4f-bfc3-37d430a139f2.PNG">

## 3. Do some Stuff
In order to do some stuff, we need a few things: accounts + balances, and send + sign + receive functionality. These functions (sending a transaction) are called extrinsics in Substrate. You can send some coins straight away by clicking Accounts and choose someone with a non-zero balance and click Send. Type in an amount and click Make Transfer -> Sign and Submit.
<img width="800" alt="send_funds" src="https://user-images.githubusercontent.com/39792005/133223388-432befc7-5078-4a4c-bea3-4860b0317b67.PNG">\
At this point it is likely you'll see an error: *verification Error: Runtime error: Execution failed*, etc. There is an easy remedy. We need to instruct the frontend to look for specific *types* that are allowed in our chain, for example a `balance` or `u32` (unsigned integer). Head to Settings -> Developer and paste in the following JSON. Be sure to match parentheses.

<img width="800" alt="json_types" src="https://user-images.githubusercontent.com/39792005/133225698-71fa8d51-7e7c-4d71-8162-446a4b3bdef2.PNG">

```
{
  "AccountInfo": "AccountInfoWithDualRefCount",
  "Address": "AccountId",
  "LookupSource": "AccountId",
  "ContinuousAccountData": {
    "principal": "u64",
    "deposit_date": "BlockNumber"
  },
  "U16F16": "[u8; 4]",
  "GroupIndex": "u32",
  "ValueStruct": {
    "integer": "i32",
    "boolean": "bool"
  },
  "BufferIndex": "u8",
  "AccountIdOf": "AccountId",
  "BalanceOf": "Balance",
  "FundInfoOf": "FundInfo",
  "FundInfo": {
    "beneficiary": "AccountId",
    "deposit": "Balance",
    "raised": "Balance",
    "end": "BlockNumber",
    "goal": "Balance"
  },
  "FundIndex": "u32",
  "InnerThing": {
    "number": "u32",
    "hash": "Hash",
    "balance": "Balance"
  },
  "SuperThing": {
    "super_number": "u32",
    "inner_thing": "InnerThing"
  },
  "InnerThingOf": "InnerThing"
}
```
>Sidebar: this JSON can be found here: `runtimes\super-runtime\types.json`. Remember when our node first started (line 9) it said: `Native runtime: super-runtime-1`? Well this is the module our node is using to execute the logic.

Click Save and refresh the page. Try again to send some funds. If successful you should see an extrinsic event listener notification. **Quickly** flip to your terminal to see the backend output (you may need to scroll up):
```
2021-09-14 20:20:28 💤 Idle (0 peers), best: #0 (0x0725…9fda), finalized #0 (0x0725…9fda), ⬇ 0 ⬆ 0    
2021-09-14 20:20:31 🙌 Starting consensus session on top of parent 0x0725bbae0b15b4b21842fb959279a4ff031b17333a4d0f500083e47e4dbb9fda    
2021-09-14 20:20:31 🎁 Prepared block for proposing at 1 [hash: 0xac14ea544421411c8e3889ab9b55ab7b61eda0686250a866476dfd814101bd06; parent_hash: 0x0725…9fda; extrinsics (2): [0x0cfd…c1c3, 0x4cb6…305c]]    
2021-09-14 20:20:31 ✨ Imported #1 (0xac14…bd06)    
2021-09-14 20:20:31 Instant Seal success: CreatedBlock { hash: 0xac14ea544421411c8e3889ab9b55ab7b61eda0686250a866476dfd814101bd06, aux: ImportedAux { header_only: false, clear_justification_requests: false, needs_justification: false, bad_justification: false, is_new_best: true } }    
2021-09-14 20:20:33 💤 Idle (0 peers), best: #1 (0xac14…bd06), finalized #0 (0x0725…9fda), ⬇ 0 ⬆ 0   
```
Note the block number increase between the first and last line. Our blockchain has been sitting idle this whole time waiting for something to process. Once it had the transfer it began the consensus session, checked the signatures and balances, and declared `Instant Seal success: CreatedBlock {hash: 0xac..bd06 ..}`

### Congrats 🥳 you're now running a functional development blockchain!
 
## 4. Exercises
Mess around with the functions available in the frontend (you can't break anything!) Send some transactions, then view the chain state. Clicking the plus sign adds state to the display.
<img width="800" alt="chain_state" src="https://user-images.githubusercontent.com/39792005/133228889-b45325f1-091d-4a0f-b13a-e4e06482eaed.PNG">

## 5. Next time
I'm not sure yet...its late and Jeff has three classes tomorrow!

## FAQ
Please send me your questions or errors so I can start to compile a FAQ. I expect this to be updated in the future.

## Image Credits:
Parity & Substrate Recipes Workshop https://www.youtube.com/watch?v=KVJIWxZSNHQ&t=4112s (Slightly out of date if you're following along but the concepts still apply.)

