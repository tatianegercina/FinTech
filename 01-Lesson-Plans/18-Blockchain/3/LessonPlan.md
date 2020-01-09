## 18.3 Lesson Plan: Building a Blockchain

### Overview

Today's class will have the students build a real Ethereum-based blockchain using the `puppeth` tool bundled with `geth`, the official Ethereum node software.

The goal of this lesson is to build a "Proof of Work" based chain in class, to prepare the students for building a "Proof of Authority" based test network at home, as well as explain the differences in consensus algorithms and the tradeoffs that they balance.

### Class Objectives

By the end of the unit, students will be able to:

* Explain the most popular consensus algorithms and the tradeoffs between each.

* Create a genesis block using `puppeth`.

* Initialize `geth` nodes using a `genesis.json`.

* Run and connect `geth` nodes.

* Build a blockchain network and produce blocks.

* Send a transaction on their local network.

---

### Instructor Notes

* **Important Note:** For this week's activities, Windows users **MUST** use `git-bash` and not the default command prompt in Windows!

* Before class, make sure to follow the `geth` [install instructions](https://github.com/ethereum/go-ethereum/wiki/Installing-Geth) and ensure that the tool is functioning in your computer.

* It is highly advised to keep track of the commands you run in order to start a blockchain with `geth`. There are many commands, but two of them will be the most important, and it is easiest to keep track if you are maintaining the notes in each step.

* If all else fails, and a student is absolutely unable to start their own blockchain, you can distribute the pre-built [devchain](../Supplemental/devchain.zip). Within is a prebuilt genesis configuration, with two nodes and accounts, as well as a `README.md` for how to start the chain. The chain has mined about 30 blocks already, so it is ready to continue mining.

* Have an address/wallet ready to populate as a pre-funded account. You can generate a new one with MyCrypto, or use the same wallet from Day 1.

* Have a look at the [Proof of Stake](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ) FAQ on the Ethereum wiki for an in-depth comparison between it and Proof of Work.

* Slack out the [Blockchain TX Installation Guide](../../19-Blockchain-Python/Supplemental/Blockchain_TX_Install_Guide.md) and the [HD Wallet Derive Installation Guide](../../19-Blockchain-Python/Supplemental/HD_Wallet_Derive_Install_Guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1E5gDn4M6ivj1i0ZoUmjhcRUIam97v-scO0xQgu1B_CQ/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [18.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=69e9f9c6-f369-44a7-b574-ab190134eb81) Note that this video may not reflect the most recent lesson plan.

---

### 1. Instructor Do: Welcome Class (10 min)

Welcome students to the third day of the introduction to the blockchain technology, open the lesson slides, and highlight that by the end of Today's class, we will do the following:

* Build a blockchain from scratch!

* Learn the differences between the various consensus algorithms available.

* Make transactions in our very own blockchain.

Continue by refreshing students a bit on the data structure of a blockchain. Ask the students the following questions:

* What does the "chain" in blockchain refer to?

  **Answer** The chain of hashes that link each block to the previous.

* What is a digital signature?

  **Answer** A message that you can validate the integrity and authenticity of cryptographically.

* What is a node?

  **Answer** A node is a participant in the network that maintains a full copy of the blockchain.

Explain to the students that today they will be building a real, functioning blockchain from scratch, so get excited!

Answer any questions before moving on.

---

### 2. Instructor Do: Consensus Algorithms (10 min)

In this activity, students will learn what consensus algorithms are and the differences between the available existing options.

Open the lesson slides and move to the "Consensus Algorithms" section, recall to students the "people chain" we built in Day 1 and have students to ponder about the following:

* How would you know if somebody was lying in the network? This is a consensus problem.

  **Answer**: Since there are many copies of the chain, it is easy to verify with another node.

  **Answer**: In reality, there are also digital signatures that would enforce the integrity

* Do any blockchain enthusiasts know what this problem is called?

  **Answer**: Byzantine General's problem!

Play the following video for the class to explain the problem:

* [Byzantine General's Problem](https://youtu.be/dfsRQyYXOsQ)

Explain to students that **consensus algorithms** are how we solve this problem.

Like most things in blockchain, they are simple words that get complicated fast, so start with some definitions and aks students the following questions:

* Can someone define consensus for us?

  **Answer**: "Coming to an agreement." In a blockchain, we mean agreeing on what block in the chain is going to come next.

* What about consensus algorithms?

  **Answer**: In blockchain, we mean the math that decides what block in the chain will come next.

Explain to the students that:

* In a decentralized system, you cannot trust the participants in the network.

* A decentralized system is like a database that can be written to by anyone, which means special rules must be in place to prevent the database from being modified maliciously.

Explain to students that consensus algorithms help to add trust to the systems. Break down the primary purposes for a consensus algorithm:

* The main purpose of a consensus algorithm in blockchain is to get the entire network to agree on which block gets added to the chain next.

* A good consensus algorithm makes it so expensive to cheat, aka "rollback" the chain, that you'd make more just playing the game by the rules and just adding to it (aka mining) instead.

Explain to students that there are many consensus algorithms in development, but blockchain technology has reignited innovation in the distributed computing field; we'll discuss the more popular algorithms relevant to blockchain.

#### Proof of Authority

The first, most straightforward, and least secure algorithm we'll start with is called "Proof of Authority."

![proof of authority](https://image.shutterstock.com/image-photo/successful-team-leader-manager-ceo-600w-461317327.jpg)

* Proof of Authority allows only specific addresses to mine/produce blocks in the network.

* This is a centralized but cheap algorithm mainly used to power test networks.

* This algorithm is never used in production **mainnet blockchains**, it is only for development and testing in **testnet blockchains**.

#### Proof of Work

![proof of work](https://image.shutterstock.com/image-photo/bitcoin-cryptocurrency-mining-farm-600w-761471725.jpg)

* Proof of Work (PoW) is the most popular algorithm in blockchain nowadays.

* This is what Bitcoin came out with, and where the term "mining" comes from.

* Proof of Work is the act of converting computing power that costs real-world energy and money into a block with transactions in it.

* The block is then submitted to the network for confirmation, and the block with the most "work" put into it gets added.

* This is a very secure algorithm, but the most expensive in terms of resources. This is its biggest criticism.

#### Proof of Stake

![proof of stake](https://image.shutterstock.com/image-photo/closeup-portrait-shocked-surprised-young-600w-207481837.jpg)

Explain to students that Proof of Stake (PoS) is very similar to PoW, the main difference is that instead of contributing computational power, this algorithm "stake" some of the cryptocurrency, aka "collateralize" it while you produce blocks.

* "Staking" your coins means to lock them in a transaction that proves to the rest of the network that you are willing to "put your money where your mouth is" to be trusted to make blocks.

* If you cheat, you are penalized from your stake.

* The most significant criticism is the "nothing at stake" problem, where block producers have nothing to lose for producing alternative versions/histories of the blockchain.

* Some versions of this algorithm include "punishing" cheaters by "burning" their stake and not letting them get it back.

* Despite this concern, much of the blockchain community is moving towards different variations of PoS, including Ethereum, with mathematical safeguards in place to reduce this risk significantly.

Explain to the class that there are many other consensus algorithms under research and development, highlight the following:

* Proof of Capacity - It uses free hard drive space as a contribution to the network.

* Proof of Burn -- This algorithm "burns" or making some amount of coins un-spendable to act as a stake to the network.

Answer any questions before moving on.

---

### 3. Students Do: Turn and Teach Consensus Algorithms (15 min)

In this activity, students will turn and teach the three consensus algorithms just covered.

Have the students get into groups of three (one student per algorithm).

Have TAs circulate and ensure that students are actively engaging in discussion.

**Instructions:**

* [README.md](Activities/01-Stu_Consensus_Algos/README.md)

---

### 4. Instructor Do: Consensus Algorithm Review (5 min)

Ask the students the following questions:

* What is the biggest strength of:

  * Proof of Work

    **Answer**: Most secure, most decentralized.

  * Proof of Stake

    **Answer**: Similar security as PoW without the electricity cost.

  * Proof of Authority

    **Answer**: Fastest, great for testing and development.

* What is the biggest weakness of:

  * Proof of Work

    **Answer**: High energy/computational cost.

  * Proof of Stake

    **Answer**: "Nothing at Stake," potential wealth distribution issues, incentive structure can be taken advantage of.

  * Proof of Authority

    **Answer**: Highly centralized, least secure.

Congratulate the class on learning some of the most important and fundamental algorithms that blockchains are using today. Now, we can take this knowledge and start to build our blockchain.

Finally, highlight to students the following:

* Many computer scientists and mathematicians around the globe are working very hard to solve these problems.

* Understanding fundamentally how these algorithms work allows you to understand the rest of the blockchain community and why individual design decisions are being made, and what makes blockchains different from each other.

Answer any questions before moving on.

---

### 5. Instructor Do: Creating a Genesis Block Demo (10 min)

In this activity, you will be demonstrating the generation of a genesis block using the `puppeth` tool bundled with the Go Ethereum (`geth`) tool.

Explain to students that now we are going to build our blockchain. We will start building the first block of the chain, where we will decide on which consensus algorithm to pick and configure the network.

Introduce the Go Ethereum tool to the class and highlight the following:

* The Go Ethereum tool is one of the three original implementations of the Ethereum protocol.

* It is written in the Go programming language, fully open source, and licensed under the GNU LGPL v3.

* We will use the Go Ethereum tool via the `geth` command-line tool.

* `geth` is the official Ethereum node software used to initialize, run and manage Ethereum nodes.

* Don't worry, you don't need to learn Go! You just have to know that it's super fast and has a cute mascot called Gogopher!

 ![Gogopher](Images/256px-Gogophercolor.png)

Ask the students to recall what a "node" is.

* **Answer**: A participant of the network that keeps a full copy of the blockchain and maintains the consensus rules of the network.

* By default, running `geth` will create a standard Ethereum node that will sync to the main network.

* However, since `geth` comes with a handy tool called `puppeth`, we will create our networks!

Open a terminal window (GitBash in Windows) navigate to your `Blockchain-Tools` folder and type the following command:

```bash
./puppeth
```

This should show the following prompt:

![puppeth](Images/puppeth.png)

Explain to the class that the prompt is saying that this tool can be used to set up a complete Ethereum network ecosystem, including nodes, monitoring tools, and more.

* The Genesis block is the very first block in the chain. It contains the initial rules for the network, like the consensus algorithm and pre-funded accounts.

Ask the class to come up with a clever name for your new network. Type in the name, like "puppernet" and hit enter to move forward in the wizard.

Type `2` to pick the `Configure new genesis` option, then `1` to `Create new genesis from scratch`:

![genesis](Images/puppeth-genesis.png)

Now you have the option to pick a consensus engine (algorithm) to use.

Explain to the class that we will be using Proof of Work.

* Note that the network difficulty will be low enough that our computers can mine blocks easily.

Type `1` to choose `Proof of Work` and continue.

You will be asked to pre-fund accounts. Paste an address from any Ethereum wallet that you control, without the `0x` prefix.

Use MyCrypto like from the previous class, and explain to the students that in this step is where we are going to pre-fund any accounts.

* We're going to paste in the address from the wallet we used the on Day 1, and when used on this new network, it will be heavily funded for us to test with.

Once you paste an address and hit enter, hit enter again on the blank `0x` address to continue the prompt.

Continue with the default option for the prompt that asks, `Should the precompile-addresses (0x1 .. 0xff) be pre-funded with 1 wei?` by hitting enter again until you reach the `Chain ID` prompt.

![prefunding accounts](Images/puppeth-prefund.png)

Ask the class to come up with a number to use as a "chain ID" or make one up yourself, like `333`, for example.

Once you enter the chain ID, hit enter, and you should show this success message and redirect to the original prompt.

![success](Images/puppeth-success.png)

Great! Your genesis configuration is stored in your local home directory.
We'll export this later. For now, it's time to have the students generate a genesis block.

Answer any questions before moving on.

---

### 6. Students Do: Creating a Genesis Block (10 min)

In this activity, students will create their genesis configuration, just like was demonstrated.

Ensure that every student has seen the success message for creating a new genesis configuration.

If a student is stuck, have either a TA or fellow student help get them un-stuck.

Have the TAs circulate and ensure that the students can get to the "successful genesis creation" message.

Once every student has seen the success message, you can move on.

**Instructions:**

* [README.md](Activities/02-Stu_Genesis_Creation/README.md)

---

### 7. Instructor Do: Creating a Genesis Block Review (5 min)

Conduct a facilitated discussion by asking the students the following questions:

* What is important about the genesis block?

  **Answer**: It contains the initial rules for the blockchain network, like consensus algorithm, pre-funded accounts, etc.

* What is the point of pre-funding accounts in the genesis block?

  **Answer**: So that we have some crypto to test with right away; otherwise, we'll have to mine it manually (time-consuming).

* Since we chose **Proof of Work**, what mechanism are we using to create new blocks?

  **Answer**: Mining

Answer any questions before moving on.

---

### 8. Instructor Do: Creating two nodes with accounts (10 min)

In this activity, students will learn how to add nodes to our brand new blockchain. It is advised to keep track of the commands you are using in a text file for reference. Alternatively, you can tap into the `bash history`, but the ordering may not be consistent. There are many commands involved with the next few activities, so it is important to keep track of where you are in the process.

The first step is to export our genesis configuration into a `json` file. Follow the next steps to do so.

* In the `puppeth` prompt, navigate to the `Manage existing genesis` by typing `2` and hit enter.

* Next, type `2` again to choose the `Export genesis configurations` option, then continue with the default (current) directory:

 ![export genesis puppeth](Images/puppeth-export.png)

* This will export several `networkname.json` files -- we only need the first one without `aleth`, `parity`, or `harmony` suffixes. In this demo, we will need the file names `puppernet.json`.

Explain to students that we can use the `networkname.json` file to initialize any new nodes in the system automatically to grow the network!

* Now, we need to create at least two nodes to build the chain from the genesis block onward.

Exit the `puppeth` prompt by using the `Ctrl+C` keys combination.

Explain to students that now you will create the first node's data directory using the `geth` command and a couple of command-line flags. Be sure you are under your `Blockchain-Tools` directory and run the following command from the terminal window:

```bash
./geth account new --datadir node1
```

Copy the address that is printed into your notes file, and label it "Node 1 Key". You will need this for future reference. You can always fetch the address later by printing the keystore file in the node's folder like so:

```bash
cat node1/keystore/UTC--2019-10-08T20-14-04.346928000Z--959a2bd5da6097bab0c2d98e14ebfa65bed06b1b
```

This will output something like:

```bash
{"address":"959a2bd5da6097bab0c2d98e14ebfa65bed06b1b","crypto":{"cipher":"aes-128-ctr","ciphertext":"07d7df14c082d8d4d14c7d2877c968a9bb624f398c4b820127dcd8d0dfe62bc1","cipherparams":{"iv":"494ce9a4fb08101a52eb3f60b1b80a2f"},"kdf":"scrypt","kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"c6a8ce0ed96bada27cd8e82906a78c795953901e90736170180db97196644052"},"mac":"440e051dd3c0333966a403e8a037c50fa80355ea0a911aa323c0f9ef01214f28"},"id":"0de99a24-763b-4c98-8ed7-115954e6d420","version":3}
```

You can simply copy the `address` property from the JSON keystore. Notice that you can also just copy the address from the end of the file name, since it is appended with the address.

Explain to students that you are using the `geth` command here to create a new account in the `node1` folder.

* This is where all data belonging to the first node will reside, and the address that the mining rewards will go.

You will have to enter a password to encrypt the key-pair. Ask the students:

* What type of cryptography are we using when we lock the keys with a password?

 **Answer**: Symmetric cryptography!

* In this case, we're locking a pair of asymmetric keys with a symmetric password, wild times!

It might be worth mentioning that by doing this, we create a security bottleneck with our password. All a hacker has to do is brute force the password, which is significantly easier than the long private key.

Explain to students that in a production environment, you would use a hardware wallet. We will explore the different types of wallets in the next unit.

Once you successfully create the account, you should see this message:

![geth new account](Images/geth-account-new.png)

Next, create another account using a different `datadir` by running the following command in the terminal window:

```bash
./geth account new --datadir node2
```

Copy and label your second node's address in your notes file for later.

Explain to students that you typically would only have one node per machine, but you need to create at least two nodes in your computer to create a blockchain.

* Now we have two folders that each node can use to store its private key and its copy of the blockchain.

Explain to students that now is time to initialize and tell the nodes to use our genesis block! Open the terminal window and run the following command to initialize `node1`.

```bash
./geth init puppernet.json --datadir node1
```

Since you only run the `init` commands once, you do not need to copy these commands into your notes.

You should see this success message:

![geth init](Images/geth-init.png)

Explain to the class that this node is now initialized. This means that it is using our genesis block as a starting point.

Repeat the same process for the second node by running the following command in the terminal window.

```bash
./geth init puppernet.json --datadir node2
```

Your directory structure should look something like this:

![directory tree](Images/geth-tree.png)

Explain to students that the chain is ready to be started. Now it's time to have the students initialize their nodes.

Answer any questions before moving on.

---

### 9. Students Do: Creating two nodes with accounts (15 min)

In this activity, students will create their nodes and accounts for their custom blockchain network.

Have the TAs circulate and ensure that students are successfully following the instructions and initializing their nodes.

Ensure that students are copying the necessary information into their

**Instructions:**

* [README.md](Activities/03-Stu_Nodes_Accounts/README.md)

---

### 10. Instructor Do: Review Node configuration (15 min)

Use this time to ensure that all students have properly configured two nodes with accounts.

* The student's directory structure should look something like this:

 ![directory tree](Images/geth-tree.png)

* If anyone encounters errors, double-check the following:

 * The network is selected in `puppeth` before exporting the genesis configuration.

 * The `genesis.json` is in the same directory as the node folders, not inside any node folders.

 * The `genesis.json` was exported.

Answer any questions before moving on.

---
### 11. BREAK (40 min)

---

### 12. Instructor Do: Starting the Blockchain (10 min)

Now it's time to start the chain! In this activity, students will learn how to build their blockchain.

Open the terminal window (Git Bash in Windows), navigate to your `Blockchain-Tools` folder and launch the first node into mining mode with the following command:

```bash
./geth --datadir node1 --mine --minerthreads 1
```

**Note:** Under Microsoft Windows you may see a pop-up window asking for permission from the firewall, be sure you check all the boxes and click on the "Allow access" button.

**Note:** In the event that your `enode` address ends in an IP address that is _not_ the localhost (127.0.0.1), you may add the `--rpcaddr 127.0.0.1` flag in order to force it to do so.

Explain each of the new command-line flags:

* The `--mine` flag tells the node to mine new blocks.

* The `--minerthreads` flag tells `geth` how many CPU threads, or "workers" to use during mining.

* Since our difficulty is low, we can set it to 1.

You should see the node `Committing new mining work`:

![node mining](Images/mining.png)

Copy this command into your notes and label it `Start Node 1`.

Now, this is our miner in the network. Let's launch the second node and configure it to let us talk to the chain!

Scroll up in the terminal window and copy the entire `enode://` address (including the last `@address:port` segment) of the first node located in the `Started P2P Networking` line:

![enodeid](Images/enodeid.png)

* We will need this address to tell the second node where to find the first node.

Open another terminal window and navigate to the same directory as before.

Launch the second node, enabling RPC, changing the default port, and passing the `enodeid` of the first node you copied in quotes, the command will vary from OS X to Windows:

* Running in OS X:

 ```bash
 ./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://69994ca26f775569b5cdb4970299c2265f7dcb7714a4ffaf66400f50e5128e79e2ff465731ddf597030f931375aa90f40d6cff7ace0f4afb84ae8de19da047bf@127.0.0.1:30303"
 ```

* Running in Windows:

 ```bash
 ./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://69994ca26f775569b5cdb4970299c2265f7dcb7714a4ffaf66400f50e5128e79e2ff465731ddf597030f931375aa90f40d6cff7ace0f4afb84ae8de19da047bf@127.0.0.1:30303" --ipcdisable
 ```

Explain each of the new command-line flags:

* The `--rpc` flag enables us to talk to our node, which will allow us to use MyCrypto to transact on our chain.

* Since the first node's sync port already took up `30303`, we need to change this one to `30304` using `--port`.

* The `--bootnodes` flag allows you to pass the network info needed to find other nodes in the blockchain. This will allow us to connect both of our nodes.

* In Microsoft Windows, we need to add the flag `--ipcdisable` due to the way Windows spawns new IPC/Unix sockets doesn't allow for having multiple sockets running from `geth` at once. Since we are only using `RCP` we can safely disable the `IPC` sockets.

* The output of the second node should show information about `Importing block segments` and synchronization:

 ![node sync](Images/node-sync.png)

Copy this command into your notes and label it `Start Node 2`.

Now it's time to have the students bring their blockchains to life!

**Note**: If you ever encounter strange errors, or need to start over **without** destroying the accounts, run the following command to clear the chain data (this will reset the `enode` addresses as well):

```bash
rm -Rf node1/geth node2/geth
```

This will be a crucial command for assisting students during the next activity. After running this command, you simply need to run another `geth init` on each node, then copy the new `enodeid` for the first node for use in the second node's start command. Everything else should stay the same, since the `genesis.json` contains the same accounts that are still in each node's `node/keystore` folder. Clearing the `node/geth` folder **just** deletes the blockchain data and allows for re-initialization from Block 0. The `enodeid` is the only aspect that will change.

Answer any questions before moving on.

---

### 13. Students Do: Bringing the blockchain to life (15 min)

In this activity, students will launch their chains using the same techniques presented in the demo.

Have the TAs circulate and ensure that students can start their chains and mine blocks.

Ensure that students are keeping track of the commands they run to start each node in their notes file for ease of reference.

If students encounter errors, have them enter the command to clear the chain data without clearing the accounts:

```bash
rm -Rf node1/geth node2/geth
```

**Instructions:**

* [README.md](Activities/04-Stu_Starting_Chain/README.md)

---

### 14. Instructor Do: Ensuring Block Production (15 min)

Take this time to ensure that every student is successfully mining blocks.

Ensure that:

* The `--mining` flag is set on the first node.

* The `--minerthreads` flag is set to at least 1 on the first node.

* The `enode://` address of the **first** node is copied into the **second** node's `--bootnodes` flag in quotes.

* The firewall of the student's machine is allowing `geth` to bind to the proper ports, especially in Windows.

* The `--port` on the second node is set to something different from the first.

* The default sync port is `30303`, so recommend `30304` for the second node.

* The `--rpc` flag is enabled on the second node. This will be necessary to connect MyCrypto to the blockchain in the next activity.

* In Microsoft Windows, the flag `--ipcdisable` should be added.

Answer any questions before moving on.

---

### 15. Instructor Do: Transacting on the chain (10 min)

In this activity, students will learn how to connect MyCrypto to the chain we created and send a transaction.

The first step is to retrieve the private key of the ETH address you use to pre-fund the genesis block. Follow the next steps.

* Open up MyCrypto and be sure the `Kovan` network is selected.

 ![Verify Kovan network](Images/verify-kovan.gif)

* Unlock your wallet using your mnemonic phrase and choose the address you want to inspect.

* Select the ETH address you use to pre-fund your chain, and in the "Select" dropdown list, choose "Wallet Info.

* Click on the eye icon next to the "Private Key" field, and copy and paste the private key of the wallet.

 ![Get private key](Images/get-private-key.gif)

Explain to students that now you are going to connect MyCrypto with the blockchain you created. Follow the next steps.

* In the left pane on MyCrypto, click "Change Network" at the bottom left:

![change network](Images/change-network.png)

* Click on "Add Custom Node", then add the custom network information that was set in the genesis.

* Ensure that you scroll down to choose `Custom` in the "Network" setting to reveal more options like `Chain ID`:

 ![custom network](Images/custom-network.png)

Explain to students that ETH still denominates the currency since we never changed that, type `ETH` in the "Currency" setting.

* The chain ID must match what you came up with earlier.

* The URL is pointing to the default RPC port on your local machine. Everyone should use this same URL: `http://127.0.0.1:8545`.

* Click on the "Save & Use Custom Node" button, to use the network; double-check that it is selected and is connected.

 ![Puppernet connected](Images/puppernet-connected.png)

Open the wallet that you use to pre-fund the chain during genesis creation as follows:

* On the left pane menu, click on "View & Send".

* Next, click on the "Private Key" option to continue.

 ![Open wallet step 1](Images/open-wallet-1.png)

* A new window will pop-up, paste the private key of the pre-fund wallet and click on the "Unlock" button to continue.

 ![Open wallet step 2](Images/open-wallet-2.png)

* Looks like we're filthy rich! This is the balance that was pre-funded for this account in the genesis configuration; however, these millions of ETH tokens are just for testing purposes.

 ![prefunded account](Images/prefunded-account.png)

Explain to students that now we're going to send a transaction to ourselves to test it out. Follow the next steps.

* Copy the pre-fund address into the "To Address" field, then fill in an arbitrary amount of ETH:

 ![transaction send](Images/transaction-send.png)

* Confirm the transaction by clicking "Send Transaction", and the "Send" button in the pop-up window.

 ![Send transaction](Images/send-transaction.gif)

* Click the `Check TX Status` when the green message pops up, confirm the logout:

 ![check tx](Images/check-tx-status.png)

* You should see the transaction go from `Pending` to `Successful` in around the same blocktime you set in the genesis.

* You can click the `Check TX Status` button to update the status.

 ![successful transaction](Images/transaction-status.png)

Congratulations, that was the first transaction send on this blockchain network! Now it's time for the students to do the same.

Answer any questions before moving on.

---

### 16. Students Do: Transacting on their chains (10 min)

In this activity, students will to connect MyCrypto to their chain and send a transaction!

Have the TAs circulate and ensure that students are successfully connecting MyCrypto to their second RPC-enabled node and sending a transaction from a pre-funded account.

Take this time to troubleshoot and ensure that the students are successfully transacting.

Ensure that:

* Students are connecting MyCrypto to `http://127.0.0.1:8545` in the custom network.

* The chain ID matches their genesis configuration.

* The account being used is the one that the student pre-funded in their genesis configuration.

* Their chain is still running:

 * `node1` is mining.

 * `node2` is RPC enabled.

**Instructions:**

* [README.md](Activities/05-Stu_Transact/README.md)

---

### 17. Instructor Do: Career Services Lesson (35 min)

**Note:** If you are teaching this lesson on a weeknight, save this section for the next Saturday class.

Use the following lesson plan to discuss the Career Services content for this week.

**Files:**

* [Career Services Lesson Plan](Career_Services_LessonPlan.md)

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
