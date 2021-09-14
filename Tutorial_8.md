# Substrate
Substrate is a blockchain framework for developers. The modular approach allows the creator to use pre-existing components for their blockchain that are time consuming to develop and risky to deploy if not tested thouroughly. The plug-and-play modules can be interchanged, for example, swapping out a proof-of-work consensus mechanism for instant finality. Additional components (pallets) can be addedd as necessary or created from scratch.

![substrate_stack](https://user-images.githubusercontent.com/39792005/133175571-f387c5e2-8a0b-4a21-b9a0-6e231f95784b.png)

The pieces of a blockchain can be abstracted into the following modules:
* Storage backend
* P2P Networking Layer
* Transaction Queue
* Consensus Engine
* Runtime logic
A standalone client like Bitcoin core has all of the above coded into its base. If someone wanted to create a new blockchain with most of Bitcoin's functionality they would have recode (or copy and refactor) all the modules. This is the motivation behind creating Substrate.

## Nodes
![substrate_architecture](https://user-images.githubusercontent.com/39792005/133176791-f0691be9-5e36-4915-b2ba-7a01f1e61cc8.png)
Substrate node architecture

The runtime logic is the specific funtionality that is required of the chain. For Bitcoin this is a ledger (the unspent-transaction output set). For Ethereum this is the virtual machine that is capable of arbitrary calculation. 

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
Each node is ready to go but has been configured with different with different parameters. We'll be running the `kitchen-node`.


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

The local substrate node (called the kitchen node) is running on your local machine waiting for input to process as a new block in the chain. To manipulate this input we need to call the appropriate functions in the program. A frontend interface here would be helpful...

### Frontend
Conveniently, the super shadowy coders over at Polkadot have done just this. Head to [polkadot.js.org/apps](https://polkadot.js.org/apps/#/) to see a live interface to the Polkadot blockchain.
![substrate_architecture](https://user-images.githubusercontent.com/39792005/133218529-445678f1-cc7f-4bc3-b78f-544cfa27e100.png)\
If our node is running (you can see it has a local server connection at 127.0.0.1:9615) then you can switch the explorer to view your node. Select the main Polkadot button (light blue box) and choose Development -> Local Node -> Switch.
<img width="771" alt="polkadot_explorer_switch" src="https://user-images.githubusercontent.com/39792005/133219220-0c959267-8456-4d0b-8189-82c5e9b1f1a3.png">\
You now have a fully functioning front-end to your substrate node. This is in orange, possibly to avoid the risk of developing and interacting on the real (pink) Polkadot chain.
<img width="818" alt="substrate_frontend" src="https://user-images.githubusercontent.com/39792005/133219675-ffdd526c-e333-4c4f-bfc3-37d430a139f2.PNG">\






## 3 . Change the Consensus Protocol
