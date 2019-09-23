## 18.3 Lesson Plan: Building a Blockchain

### Overview

Today's class will have the students actually build a real Ethereum-based blockchain using the `puppeth` tool bundled
with `geth`, the official Ethereum node software.

The goal of this lesson is to build a Proof of Work based chain in class, to prepare the students for building
a "Proof of Authority" based test network at home, as well as explain the differences in consensus algorithms and the
tradeoffs that they balance.

### Class Objectives

By the end of the unit, students will be able to:

* Explain the most popular consensus algorithms and the tradeoffs between each.

* Create a genesis block using `puppeth`.

* Initialize `geth` nodes using a `genesis.json`.

* Run and connect `geth` nodes together.

* Build a blockchain network and produce blocks.

* Send a transaction on their local network.

- - -

### Instructor Notes

* Before class, make sure to follow the `geth` [install instructions](https://github.com/ethereum/go-ethereum/wiki/Installing-Geth)
  and ensure that the tool is functioning.

* Have an address/wallet ready to populate as a pre-funded account. You can generate a new one with MyCrypto, or use the same wallet as before.

- - -

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Welcome students back refresh a bit on the data structure of a blockchain.

Ask the students the following questions:

* What does the "chain" in blockchain refer to?

  **Answer** The chain of hashes that link each block to the previous.

* What is a digital signature?

  **Answer** A message that you can validate the integrity and authenticity of cryptographically.

* What is a node?

  **Answer** A node is a participant in the network that maintains a full copy of the blockchain.

Explain to the students that today they will be building a real, functioning blockchain from scratch, so get excited!

### 2. Instructor Do: Consensus Algorithms (10 min)

Time to explain the differences between some of the most popular consensus algorithms.

First, give these rhetorical questions to the class to ponder on:

* What gives blockchains their inherent value?

* Why are they so secure?

* This is what we will be learning today.

Explain to the students that:

* In a decentralized system, you cannot trust the participants in the network.
  It's a database that can be written to by anyone, which means special rules must be in place to prevent the database
  from being modified in a malicious way.

* This is where something called a "Consensus Algorithm" comes into play.

Break down the main purposes for a consensus algorithm:

* The main purpose of a consensus algorithm in blockchain is to get the entire network to agree on which block
  gets added to the chain next.

* A good consensus algorithm makes it so expensive to cheat, aka "roll back" the chain,
  that you'd make more just playing the game by the rules and just adding to it (aka mining) instead.

Explain that there are many consensus algorithms in development, but blockchain technology has reignited innovation in the
distributed computing field, so we'll discuss the more popular algorithms relevant to blockchain, starting with Proof of Work.

![proof of work](https://image.shutterstock.com/image-photo/bitcoin-cryptocurrency-mining-farm-600w-761471725.jpg)

* Proof of Work is the most popular algorithm in blockchain currently.
  This is what Bitcoin came out with, and where the term "mining" comes from.

* Proof of Work is the act of converting computing power that costs real-world energy and money into a block with transactions in it.
  The block is then submitted to the network for confirmation, and the block with the most "work" put into it gets added.

* This is a very secure algorithm, but the most expensive in terms of resources. This is its biggest criticism.

Ask the students:

* What is the biggest strength of Proof of Work?

  **Answer**: It's the most secure and decentralized consensus algorithm deployed today.

![proof of stake](https://image.shutterstock.com/image-photo/closeup-portrait-shocked-surprised-young-600w-207481837.jpg)

* Explain that Proof of Stake is very similar to PoW, only instead of contributing computational power, you "stake"
  some of the cryptocurrency for a period of time. Once passed a minimum staking interval, you can then submit blocks
  to the rest of the network for confirmation.

* "Staking" your coins means to lock them in a transaction that proves to the rest of the network that you are willing
  to "put your money where your mouth is" in order to be trusted to make blocks.

* The biggest criticism is the "nothing at stake" problem, where block producers have nothing to lose for producing alternative
  versions/histories of the blockchain. Some versions of this algorithm include "punishing" cheaters by "burning" their stake and not
  letting them get it back.

* Despite this concern, much of the blockchain community is moving towards different variations of PoS, including Ethereum.

Ask the students:

* What is the biggest strength of Proof of Stake?

  **Answer**: Similar security to PoW without the energy cost.

Explain to the class that there are many others to research, and give them a few extra examples to go along:

* Proof of Capacity - Using free hard drive space as a contribution to the network.

* Proof of Burn -- "Burning" or making some amount of coins un-spendable to act as a stake to the network.

The last, simplest, and least secure algorithm is called "Proof of Authority."

![proof of authority](https://image.shutterstock.com/image-photo/successful-team-leader-manager-ceo-600w-461317327.jpg)

* Proof of Authority allows only specific addresses to mine/produce blocks in the network.

* This is a centralized but cheap algorithm mainly used to power test networks.

* This algorithm is never used in production, mainnet blockchains, only for development, which is what we'll be using it for.

Ask the students:

* What is the biggest strength of Proof of Authority?

  **Answer**: Fast and cheap, good for test or development networks.

### 3. Students Do: Turn and Teach Consensus Algorithms (10 min)

Students will now turn and teach the three consensus algorithms just covered.

Have the students get into groups of 3 (one student per algorithm).

**Instructions:**

* [README.md](Activities/03-Stu_Consensus_Algos/README.md)

Have TAs circulate and ensure that students are actively engaging in discussion.

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

    **Answer**: Potential wealth distribution issues, incentive structure can possibly be taken advantage of.

  * Proof of Authority

    **Answer**: Highly centralized, least secure.

### 5. Instructor Do: Creating a Genesis Block Demo (10 min)

In this activity, you will be demonstrating the generation of a genesis block using the `puppeth` tool bundled with
`geth`.

First, introduce the `geth` tool to the class.

![golang](https://www.vertica.com/wp-content/uploads/2019/07/Golang-1000x565.png)

* Geth is a command line tool written in the Go programming language -- don't worry, you don't need to know Go, just that it's super fast and has a cute mascot!

* It is the official Ethereum node software used to initialize, run and manage Ethereum nodes.

* By default, running `geth` will create a standard Ethereum node that will sync to the main
  network.

* However, since `geth` comes with a handy tool called `puppeth`, we will create our own networks!

Open a terminal window and type the following command:

```bash
puppeth
```

This should show the following prompt:

![puppeth](Images/puppeth.png)

* Explain to the class that the prompt is saying that this tool can be used to setup a complete
  Ethereum network ecosystem, including nodes, monitoring tools, and more.

* We will be using this tool to creating something called the "Genesis Block" in our new blockchain.

* The Genesis block is the very first block in the chain. It contains the initial rules for the network, like the consensus algorithm and pre-funded accounts.

Ask the class to come up with a clever name for your new network.

Type in the name, like "puppernet" and hit enter to move forward in the wizard.

Type `2` to pick the `Configure new genesis` option, then `1` to `Create new genesis from scratch`:

![genesis](Images/puppeth-genesis.png)

Now you have the option to pick a consensus engine (algorithm) to use.

Explain to the class that we will be using Proof of Work.

* Note that the network difficulty will be low enough that our computers can mine blocks easily.

Type `1` to choose `Proof of Work` and continue.

You will be asked to pre-fund accounts. Paste an address from any Ethereum wallet that you control, without the `0x` prefix.

Use MyCrypto like from the previous class, but explain to the students:

* This is where we are going to prefund any accounts. We're going to paste in the address from the wallet we used the other day,
  and when used on this new network, it will be heavily funded for us to test with.

Once you paste an address and hit enter, hit enter again on the blank `0x` address to continue the prompt.

Continue with the default option for the prompt that asks to pre-fund "precompile-addresses" by hitting enter again,
until you reach the `Chain ID` prompt:

![prefunding accounts](Images/puppeth-prefund.png)

Ask the class to come up with a number to use as a "chain ID" or make one up yourself.

Once you enter the chain ID, the next enter should show this success message and redirect to the original prompt:

![success](Images/puppeth-success.png)

Great! Your genesis configuration is stored in your local home directory.
We'll export this later. For now, it's time to have the students generate a genesis block.

### 6. Students Do: Creating a Genesis Block (10 min)

Students will create their own genesis configuration just like was demonstrated.

**Instructions:**

* [README.md](Activities/06-Stu_Genesis_Creation/README.md)

Have the TAs circulate and ensure that the students are able to get to the "successful genesis creation" message.

Ensure that every student has seen the success message for creating a new genesis configuration.

If a student is stuck, have either a TA or fellow student help get them un-stuck.

Once every student has seen the success message, you can move on.

### 7. Instructor Do: Review Genesis Configuration (5 min)

Ask the students:

* What is important about the genesis block?

  **Answer**: It contains the initial rules for the blockchain network, like consensus algorithm, pre-funded accounts, etc.

* What is the point of pre-funding accounts in the genesis block?

  **Answer**: So that we have some crypto to test with right away, otherwise we'll have to mine it manually (time consuming).

* Since we chose Proof of Work, what mechanism are we using to create new blocks?

  **Answer**: Mining

### 8. Instructor Do: Creating two nodes with accounts (10 min)

First, we need to export our genesis configuration into a `json` file.

In `puppeth`, navigate to the `Manage existing genesis` by typing `2` and enter.

Then, type `2` again to `Export genesis configurations`, then continue with the default (current) directory:

![export genesis puppeth](Images/puppeth-export.png)

* This will export several `networkname.json` files -- we only need the first one without `aleth`, `parity`, or `harmony` suffixes.

* We can use the `networkname.json` file to initialize any new nodes in the system automatically to grow the network!

Now, we need to create at least two nodes to build the chain from the genesis block onward.
Exit `puppeth` by using `Ctrl+C`.

Then create the first node's data directory using `geth` and a couple command line flags:

```bash
geth account new --datadir node1
```

* Explain to the class that you are using `geth` here to create a new account in the `node1` folder.
  This is where all data belonging to the first node will belong, and the address that the mining rewards will go.

You will have to enter a password to encrypt the keypair. Ask the students:

* What type of cryptography are we using when we lock the keys with a password?

  **Answer**: Symmetric cryptography!

* In this case, we're actually locking a pair of asymmetric keys with a symmetric password, wild times!

It might be worth mentioning that by doing this, we create a security bottleneck with our password.
All a hacker has to do is brute force the password, which is significantly easier than the long private key.

**Note**: In production, you would use a hardware wallet, but more on the different types of wallets next unit.

Once you successfully create the account you should see this message:

![geth new account](Images/geth-account-new.png)

Next, create another account using a different `datadir`:

```bash
geth account new --datadir node2
```

* Explain to the students that you typically would only have one node per machine, but you need
  at least two to create a blockchain and that's why we're doubling up on the same computer.

* Now we have two folders that each node can use to store its private key and its copy of the blockchain.

Time to initialize and tell the nodes to use our genesis block!

```bash
geth init puppernet.json --datadir node1
```

You should see this success message:

![geth init](Images/geth-init.png)

* Explain to the class that this node is now initialized. This means that it is using our genesis block as a starting
  point.

Repeat this process for the second node:

```bash
geth init puppernet.json --datadir node2
```

Your directory structure should look something like:

![directory tree](Images/geth-tree.png)

The chain is ready to be started. Now it's time to have the students initialize their nodes.

### 09. Students Do: Creating two nodes with accounts (15 min)

Students will now creating their own nodes and accounts for their custom blockchain network

**Instructions:**

* [README.md](Activities/09-Stu_Nodes_Accounts/README.md)

Have the TAs circulate and ensure that students are successfully following the instructions and initializing their nodes.

### 10. Instructor Do: Review Node configuration (15 min)

Use this time to ensure that all students have properly configured two nodes with accounts.

The student's directory structure should look something like:

![directory tree](Images/geth-tree.png)

If anyone encounters errors, double check that:

* The network is selected in `puppeth` before exporting the genesis configuration.

* The `genesis.json` is in the same directory as the node folders, not inside any node folders.

* The `genesis.json` was actually exported.

- - -

### 11. BREAK (40 min)

- - -

### 12. Instructor Do: Starting the Blockchain (10 min)

Now it's time to start the chain!

Launch the first node into mining mode with the following command:

```bash
geth --datadir node1 --mine --minerthreads 1
```

Explain each of the new command line flags:

* The `--mine` flag tells the node to mine new blocks.

* The `--minerthreads` flag tells `geth` how many CPU threads, or "workers" to use during mining.
  Since our difficulty is low, we can set it to 1.

You should see the node `Committing new mining work`:

![node mining](Images/mining.png)

Now this is our miner in the network. Let's launch the second node and configure it to let us talk to the chain!

First, copy the entire `enode://` address (including the last `@address:port` segment)
of the first node located in the `Started P2P Networking` line:

![enodeid](Images/enodeid.png)

* We will need this address to tell the second node where to find the first node.

Open another terminal window and navigate to the same directory as before.

Launch the second node, enabling RPC, changing the default port, and passing the `enodeid` of the first node in quotes:

```bash
geth --datadir node2 --port 30304 --rpc --bootnodes "enode://69994ca26f775569b5cdb4970299c2265f7dcb7714a4ffaf66400f50e5128e79e2ff465731ddf597030f931375aa90f40d6cff7ace0f4afb84ae8de19da047bf@127.0.0.1:30303"
```

Explain each of the new command line flags:

* The `--rpc` flag enables us to talk to our node, which will allow us to use MyCrypto or Metamask to transact on our chain.

* Since the first node's sync port already took up `30303`, we need to change this one to `30304` using `--port`.

* The `--bootnodes` flag allows you to pass the network info needed to find other nodes in the blockchain. This will allow us to connect both of our nodes to each other.

The output of the second node should show information about `Importing block segments` and synchronization:

![node sync](Images/node-sync.png)

Now it's time to have the students bring their own blockchains to life!

**Note**: If you ever encounter strange errors, or need to start over without destroying the accounts,
run the following command to clear the chain data (this will reset the enode addresses as well):

```bash
rm -Rf node1/geth node2/geth
```

This will be a key command for assisting students during the next activity.

### 13. Students Do: Bringing the blockchain to life (15 min)

Students will now launch their own chains using the same techniques.

**Instructions:**

* [README.md](Activities/13-Stu_Starting_Chain/README.md)

Have the TAs circulate and ensure that students are able to start their chains and mine blocks.

If students encounter errors, have them enter the command to clear the chain data without clearing the accounts:

```bash
rm -Rf node1/geth node2/geth
```

### 14. Instructor Do: Ensuring Block Production (15 min)

Take this time to ensure that every student is successfully mining blocks.

Ensure that:

* The `--mining` flag is set on the first node.

* The `--minerthreads` flag is set to at least 1 on the first node.

* The `enode://` address of the **first** node is copied into the **second** node's `--bootnodes` flag in quotes.

* The firewall of the student's machine is allowing `geth` to bind to the proper ports.

* The `--port` on the second node is set to something different from the first.
  The default sync port is `30303`, so recommend `30304` for the second node.

* The `--rpc` flag is enabled on the second node. This will be necessary to connect MyCrypto to the blockchain in the next activity.

### 15. Instructor Do: Transacting on the chain (10 min)

Now it's time to connect MyCrypto to the chain and send a transaction.

Open up MyCrypto, then click `Change Network` at the bottom left:

![change network](Images/change-network.png)

Click `Add Custom Node`, then add the custom network information that was set in the genesis.
Ensure that you scroll down to choose `Custom` in the `Network` column to reveal more options like `Chain ID`:

![custom network](Images/custom-network.png)

* Explain that the currency is still denominated by ETH since we never changed that.

* The chain ID must match what you came up with earlier.

* The URL is pointing to the default RPC port on your local machine. Everyone should use this same URL.

Once you save and use the network, double check that it is selected and is connected.

Import the account that you pre-funded during genesis creation. This will vary based on the method used to generate,
but will likely be a mnemonic, private key, or keystore file.

![prefunded account](Images/prefunded-account.png)

* Looks like we're filthy rich! This is the balance that was prefunded for this account in the genesis configuration.

* We're going to send a transaction to ourselves to test it out.

First, copy the address into the `To Address` field, then fill in an arbitrary amount of ETH:

![transaction send](Images/transaction-send.png)

Confirm the transaction by clicking `Send` on the next prompt.

Click the `Check TX Status` when the green message pops up, confirm the logout:

![check tx](Images/check-tx-status.png)

You should see the transaction go from `Pending` to `Successful` in around the same blocktime you set in the genesis.

You can click the `Check TX Status` button to update the status.

![successful transaction](Images/transaction-status.png)

Congratulations, that was the first transaction send on this blockchain network!
Now it's time for the students to do the same.

### 16. Students Do: Transacting on their chains (15 min)

Now it's time for the students to connect MyCrypto to their chain and send a transaction!

**Instructions:**

* [README.md](Activities/16-Stu_Transact/README.md)

Have the TAs circulate and ensure that students are successfully connecting MyCrypto to their
second RPC-enabled node and sending a transaction from a prefunded account.

### 17. Instructor Do: Recap and Troubleshooting (35 min)

Take this time to troubleshoot and ensure that the students are successfully transacting.

Ensure that:

* Students are connecting MyCrypto to `http://127.0.0.1:8545` in the custom network.

* The chain ID matches their genesis configuration.

* The account being used is the one that the student prefunded in their genesis configuration.

* Their chain is still running:

  * One node is mining.

  * One node is RPC enabled.
