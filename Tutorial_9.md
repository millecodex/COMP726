# UNDER CONSTRUCTION

# Substrate Part II
In Part 1 we compiled and ran a substrate backend node (on our local machine) and connected it to the front end from Polkadot. The node was called kitchen-node and when running it sat idle waiting for something to happen. This idle-ness was due to the type of consensus mechanism it was running: instant seal. The idea is that when there is something new to report the runtime calls the consensus module and it is processed. Instant seal wakes up from idle and the transaction is committed instantly. Easy. 

<img width="800" alt="substrate_instant_seal" src="https://user-images.githubusercontent.com/39792005/134260344-46795688-0443-4e35-b317-aa53746f63c5.png">

Lets look at a more traditional consensus mechanism: Proof of Work. A key difference here is that the consensus mechanism runs *independently* of the activity (in the runtime). This means that blocks will be mined and appended regardless of transaction activity. From the users point of view a transaction may have to wait in a queue and you may not know when it will be processed, or if at all. A consequence of interest is the possibility of mining empty blocks.
> Q✋: What are the implications of mining empty blocks?

<img width="800" alt="substrate_pow" src="https://user-images.githubusercontent.com/39792005/134260413-a13066fe-27f1-4b24-af92-0b31f574dc5f.png">

## Basic-PoW
A basic [proof of work node](https://substrate.dev/recipes/basic-pow.html) comes prepackaged with the recipes cookbook. This node uses `sha3pow::MinimalSha3Algorithm` a family of [secure hashing algorithms](https://en.wikipedia.org/wiki/SHA-3) (generation three). The algo is minimal because its just to get you started. When using a PoW there must be difficulty function as well as a validator function. More details are [here](https://substrate.dev/recipes/sha3-pow-consensus.html) and you can see that it is using `256` bits for the hashing length:

```
impl<B: BlockT<Hash = H256>> PowAlgorithm<B> for MinimalSha3Algorithm {
    type Difficulty = U256;
```

## run it
In the `\nodes` folder there are four different nodes. Build the node called `basic-pow`:\
`$ cargo build --bin kitchen-node --release`

Run the compiled binary, here using development `--dev` mode and a temporary storage directory `--tmp`):\
`$ cargo run --bin kitchen-node -- --dev --tmp`

Successful build & run will yield terminal output:
```
2021-09-21 21:24:44 Basic PoW Node    
2021-09-21 21:24:44 ✌️  version 3.0.0-98d3625-x86_64-linux-gnu    
2021-09-21 21:24:44 ❤️  by Substrate DevHub <https://github.com/substrate-developer-hub>, 2019-2021    
2021-09-21 21:24:44 📋 Chain specification: Development    
2021-09-21 21:24:44 🏷 Node name: breakable-bit-0288    
2021-09-21 21:24:44 👤 Role: AUTHORITY    
2021-09-21 21:24:44 💾 Database: RocksDb at /tmp/substrate3ISABJ/chains/dev/db    
2021-09-21 21:24:44 ⛓  Native runtime: super-runtime-1 (super-runtime-1.tx1.au1)    
2021-09-21 21:24:46 🔨 Initializing Genesis block/state (state: 0x1e29…d561, header-hash: 0x31fc…dee0)    
2021-09-21 21:24:46 Using default protocol ID "sup" because none is configured in the chain specs    
2021-09-21 21:24:46 🏷 Local node identity is: 12D3KooWMxCL3TeYsCnE5zEh9FGjhkipCpjXsngEkyiXW7XDVh98    
2021-09-21 21:24:46 📦 Highest known block at #0    
2021-09-21 21:24:46 〽️ Prometheus server started at 127.0.0.1:9615    
2021-09-21 21:24:46 Listening for new connections on 127.0.0.1:9944.    
2021-09-21 21:24:51 💤 Idle (0 peers), best: #0 (0x31fc…dee0), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:24:56 💤 Idle (0 peers), best: #0 (0x31fc…dee0), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:24:56 🙌 Starting consensus session on top of parent 0x31fcce21da0cb1b05f49a36ffd4b529643b69aaf40664abe741ed9291a95dee0    
2021-09-21 21:24:57 🎁 Prepared block for proposing at 1 [hash: 0x61913e14ca84bf465c007f0caaf8c0304ccb454fb355746895116805f46cc0b7; parent_hash: 0x31fc…dee0; extrinsics (1): [0x4a57…c89b]]    
2021-09-21 21:25:01 💤 Idle (0 peers), best: #0 (0x31fc…dee0), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
```

Check back on the terminal output to see that blocks have been mining away! Note that the `best` is incrementing, but the `finalized` is staying at `#0`. More on this in a jiffy. Compare the hashes to see that they're unique. Check the parent_hashes.
```
2021-09-21 21:26:26 💤 Idle (0 peers), best: #3 (0x955c…cbbf), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:26:28 ✅ Successfully mined block on top of: 0x955c…cbbf    
2021-09-21 21:26:28 🙌 Starting consensus session on top of parent 0x9bb272e0c1142e6b4ee7d51e552e8e9ee40f8829280851eef5df1ae4c552688a    
2021-09-21 21:26:28 ✨ Imported #4 (0x9bb2…688a)    
2021-09-21 21:26:28 🎁 Prepared block for proposing at 5 [hash: 0x200dcb7e67f3284fb6951c35957bd517f1dea03bd47ae63602326ae8b9813ebe; parent_hash: 0x9bb2…688a; extrinsics (1): [0x9415…9642]]    
2021-09-21 21:26:31 💤 Idle (0 peers), best: #4 (0x9bb2…688a), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:26:36 💤 Idle (0 peers), best: #4 (0x9bb2…688a), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:26:41 💤 Idle (0 peers), best: #4 (0x9bb2…688a), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:26:46 💤 Idle (0 peers), best: #4 (0x9bb2…688a), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
2021-09-21 21:26:47 ✅ Successfully mined block on top of: 0x9bb2…688a    
2021-09-21 21:26:47 ✨ Imported #5 (0xb48f…9f37)    
2021-09-21 21:26:47 🙌 Starting consensus session on top of parent 0xb48f730718bcfa15ae7ac24847ea3ba2e52bdf225cf0ac29d886b53309b29f37    
2021-09-21 21:26:47 🎁 Prepared block for proposing at 6 [hash: 0x78076a340d56154da5d81724663feb95784092e080011d1f3531d5cb49e2ecf2; parent_hash: 0xb48f…9f37; extrinsics (1): [0x992d…e9a8]]    
2021-09-21 21:26:51 💤 Idle (0 peers), best: #5 (0xb48f…9f37), finalized #0 (0x31fc…dee0), ⬇ 0 ⬆ 0    
```

## Process a transaction
Head to [polkadot.js.org/apps](https://polkadot.js.org/apps/#/) to see a live interface to the Polkadot blockchain and connect to your local node (e.g.: `Prometheus server started at 127.0.0.1:9615` from above output). Your block explorer should show you all the recent blocks. This is a different from last time when we only saw blocks once some activity was processed by the instant seal consensus method.

Click Accounts and send some funds. A notification will let you know the transaction is ready. A further notification will appear when the block is mined.
> Q✋: Do all blocks occur at regular intervals? Why or why not?

<img width="600" alt="substrate_pow_notification" src="https://user-images.githubusercontent.com/39792005/134150946-ba87878a-26aa-43b5-994b-2ae4fb160d3e.png">

Once mined check out some details. Note event count, extrinsic count, & weight. 
<img width="800" alt="substrate_pow_block" src="https://user-images.githubusercontent.com/39792005/134149216-0aa13529-bc9e-46c3-a134-b8cb91aa5dca.png">

## RandomnessDemo

## What about Validators?
Aura and Babe are the names of consensus modules that query the runtime for the set of validators that can be used for block production. As only certain nodes have validator status, they are special,  

## Finalization

# Footnotes
> SHA-3 uses a completely different underlying [recipe](https://stackoverflow.com/questions/14356526/whats-the-difference-between-the-hash-algorithms-sha-2-and-sha-3) to scramble the bits and was chosen for its dissimilarity to SHA-2 which is famous for its SHA-256 used in Bitcoin.
