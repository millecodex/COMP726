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
  +-- **kitchen-node**
	|
	+-- rpc-node
```
Each node is ready to go but has been configured with different with different parameters. We'll be running the `kitchen-node`.


## 1.  Development Environment
Substrate is written in [rust](https://www.rust-lang.org/) and so a rust compiler is necessary to run any substrate based blockchain. On a linux/macOS system, you can run this [script](https://getsubstrate.io/) for autoconfiguration:

`curl https://getsubstrate.io -sSf | bash -s -- --fast`

If you are using Windows I **do not** recommend attempting to configure rust/substrate, rather [install WSL](https://devblogs.microsoft.com/commandline/install-wsl-with-a-single-command-now-available-in-windows-10-version-2004-and-higher/) (Windows Subsystem for Linux).

More detail about various OS configurations (including Apple arm M1s) is at [substrate.dev](https://substrate.dev/docs/en/knowledgebase/getting-started/).

We will be running a specific configuration of substrate found in the [Recipes](https://substrate.dev/recipes/) cookbook. Clone the Substrate recipes repo:

`git clone https://github.com/substrate-developer-hub/recipes.git`



## 2.  Get your Blockchain Running
Navigate to the `\recipes` directory and build the binary. This will take a while the first time you do it because all the dependencies get compiled.

Build without debug option (takes longer):
`cargo build --release`

Build the node called `kitchen-node`:
`cargo build --bin kitchen-node --release`

Run the compiled binary, here using development (`--dev`) mode and a temporary storage directory (`--tmp`):
`cargo run --bin kitchen-node -- --dev --tmp`



## 3 . Change the Consensus Protocol
