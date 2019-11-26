### 6. Instructor Do: Intro to Remix and Ganache (15 min)

In this activity, the instructor will demo the tools used by smart contract engineers to develop, compile, and deploy code on the Ethereum blockchain. Students will gain familiarity with tools from the `Truffle Suite` namely `Ganache`, the one-click development blockchain.

**Files:**

* [MessageBoard.sol](Activities/06-Ins_Intro_to_Remix_and_Ganache/Solved/MessageBoard.sol)

Start by launching Ganache. While Ganache is starting, take a moment to tell the students a little bit about Ganache and the Truffle suite.

* Truffle is a development environment for Solidity. It includes a compiler, some script tools, etc.

* Ganache is a one-click Ethereum blockchain.

* Ganache is part of Truffle. It makes development on blockchains very quick, which is awesome; however the algorithm that powers it is not secure.

![ganche_create_workspace.png](Images/ganache_create_workspace.png)

Click `New Workspace` to create a new workspace.

![ganache_set_workspace_name.png](Images/ganache_set_workspace_name.png)

* Workspaces in Ganache are a configuration for a development blockchain. Each workspace can be a different template for how you want to launch your development chain.

* Workspaces allow you to customize many things about your chain:
  * An initial pre-mine of any size deposited into any number of generated addresses.

  * Specific ports for talking to your blockchain node.

* Let's name our new workspace `fintech`

* As you can see, there is another field titled `TRUFFLE PROJECTS`. What this field allows you to do is link a project that uses Truffle's Solidity compiler.  Today we will not be using Truffle's compiler. We will use `Remix`; Ethereum foundations online implementation of a Solidity IDE that has its own built-in compiler.

Click the Server tab.

![ganache_set_server_info.png](Images/ganache_set_server_info.png)

* The `HOSTNAME` field is the interface on your computer where the node will bind to listen for connections. We want this to be set to `127.0.0.1`, commonly referred to as `localhost`.

* The `PORT` field is the port that your node will be listening for communication. For all of our examples, we will be using port `8545`.

* You don't need to worry about the `NETWORK ID` field; it is for ganaches internal tracking.

* The `automine` feature is a very convenient option; when a transaction happens, such as someone executing/deploying a smart contract or sending/receiving funds, the block is instantaneously processed so that there is no wait time.

* `Automine` is convenient because you can see the results of transactions instantaneously but dangerous in the fact that it is not representative of how a blockchain normally functions.

* The `ERROR ON TRANSACTION FAILURE` is useful because it will log additional information about errors to our GUI.

Now click `Accounts and Keys`.

![ganche_create_workspace.png](Images/ganache_import_mnemonic.png)

* As previously mentioned Ganache allows you to pre-mine a selected number of coins into a selected number of generated addresses. This is useful for testing smart contracts.

* `ACCOUNT DEFAULT BALANCE` is the number of coins in `Ether` that will be in each address.

* `TOTAL ACCOUNTS TO GENERATE` is the number of accounts that will be generated containing the balance.

Emphasize the importance of the wallet mnemonic to an Ethereum wallet and its ability to generate addresses.

* `AUTOGENERATE HD MNEMONIC` is another way to auto-generate our mnemonic. We, however, are going to be using our previously generated mnemonics.

![ganache_set_chain.png](Images/ganache_set_chain.png)

* We are going to keep our `Gas Limit`, `Gas Price` and `HardFork` at their default values; these are reasonable defaults.

Click `Save Workspace`.

![ganache_accounts.png](Images/ganache_accounts.png)

Elaborate on the following sections of the Ganache accounts page.

* The workspace info bar displays the settings for your current workspace, many of these values should be familiar from the initial setup.

* As you can see, our wallet mnemonic is also listed.

* We also have the list of pre-generated addresses from our wallet, each with the `100 eth` balance that we set in the Ganache workspace setup.

Click the blocks tab:

![ganache_blocks.png](Images/ganache_blocks.png)

This page should be relatively empty, only listing block zero, explain.

* Since it is a new workspace, the blockchain only consists of the block that contains our initial blockchain configuration.

* As more transactions happen, more blocks will be mined instantaneously because of the `automine` feature.

* The remaining pages, much like the blocks page, will also be relatively blank until we begin interacting with our blockchain.

Inform the students that they will have time to explore the various pages of Ganache as they setup their Ganache blockchain in the next activity.

Now that Ganache is running the local development blockchain on `localhost:8545`, Open [Remix](http://remix.ethereum.org) in your web browser.

![remix_home.png](Images/remix_home.png)

Briefly introduce remix.

* Remix is an online IDE, and compiler for the `Solidity` smart contract language.

* Remix allows you to write, compile and deploy Solidity smart contracts onto the Ethereum blockchain.

Open the example smart contract [MessageBoard.sol](Activities/06-Ins_Intro_to_Remix_and_Ganache/Solved/MessageBoard.sol) by clicking the `Add local file` button.

![remix_open_file](Images/remix_open_file.png)

The Solidity file's code should appear in the editor window.

![remix_editor_message](Images/remix_editor_message_board.png)

Reassure the students that though this contract may look complicated now, soon it will make a lot more sense.

Click the `Solidity Compiler` button on the remix sidebar then click `Compile` to compile the contract.

![remix_compile_message_board](Images/remix_compile_message_board.png)

* Compiling a contract with Remix is as easy as selecting a compatible compiler version and clicking `Compile`.

* Solidity is compiled to basic instructions that are read by the `Ethereum Virtual Machine`.

Now click the `Deploy and Run Transaction` button on the remix sidebar bar.

![remix_deploy_messsage_board](Images/remix_deploy_messsage_board.png)

At this point, open `MetaMask`. MetaMask may prompt you to sign-in. Then select `localhost:8545` from the dropdown menu at the top.

![remix_meta_mask_chain](Images/remix_meta_mask_chain.png)

* MetaMask is the bridge between the Remix IDE in our browser and whatever blockchain we are trying to execute a smart contract on.

* In this case, the blockchain that we are communicating with is our local development chain.

Change the Environment to `Injected Web3`:

![remix_injected_web3](Images/remix_injected_web3.png)

Explain to the students that:

* Web3.js is a set of javascript libraries which allow you to communicate with an Ethereum node.

* We must set our environment to `Injected Web3` so that remix can talk to our local development chain.

* We will be deploying our first contracts tomorrow but we will be taking some time today to familiarize ourselves with Remix.
