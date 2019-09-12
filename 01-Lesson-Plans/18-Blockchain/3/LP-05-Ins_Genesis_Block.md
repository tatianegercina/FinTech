### 5. Instructor Do: Creating a Genesis Block Demo (10 min)

In this activity, you will be demonstrating the generation of a genesis block using the `puppeth` tool bundled with
`geth`.

Before class, make sure to follow the `geth` [install instructions](https://github.com/ethereum/go-ethereum/wiki/Installing-Geth)
and ensure that the tool is functioning.

Have an address/wallet ready to populate as a pre-funded account. You can generate a new one with MyCrypto, or use the same wallet as before.

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

Once you paste an address and hit enter, hit enter again on the blank `0x` address to continue the prompt.

Continue with the default option for the prompt that asks to pre-fund "precompile-addresses" by hitting enter again,
until you reach the `Chain ID` prompt:

![prefunding accounts](Images/puppeth-prefund.png)

Ask the class to come up with a number to use as a "chain ID" or make one up yourself.

Once you enter the chain ID, the next enter should show this success message and redirect to the original prompt:

![success](Images/puppeth-success.png)

Great! Your genesis configuration is stored in your local home directory.
We'll export this later. For now, it's time to have the students generate a genesis block.
