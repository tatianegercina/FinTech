# Part I: Blockchain Case Study

## Background

As a FinTech professional, it is important to be aware of the advancements happening within the FinTech blockchain space. The blockchain domain is rapidly changing, and even those in a highly technical role must stay abreast of what is happening in the digital finance landscape as many FinTech companies are using and creating tools and services that are powered by blockchain.

One of the key methods used to conduct corporate analysis is the **case study**. Case studies are often 50–100 pages or more, but your task is to create a more focused case study that analyzes how a Canadian FinTech blockchain company is using technology to solve a standing financial problem in Canada.

In this homework assignment, you will:

* Select a Canadian FinTech blockchain company that interests you.

* Research the domain and company.

* Write a detailed case study of the company.

* Upload your case study to your git repository.

This assignment will challenge you to learn more about Canadian advancements in the blockchain industry.

## Instructions

### 1. Choose a FinTech domain that you find relevant or interesting

**Note:** We covered a number of FinTech domains in class this week. If you already have a Canadian company in mind that you want to research, skip ahead to Step 3.

* Payments/Billing

* Capital Investment

* Investment Management

* Wealth Management

* Enterprise Solutions

* Insurance (InsurTech)

* Mortgage/Real Estate

* Personal Finance/Deposits/Online Banking

* Lending

* Blockchain and Cryptocurrencies

* Regulation Technology (RegTech)

* Open Banking

* Robo-advising

Remember that because FinTech is an evolving field, different FinTech reports may use different names and definitions for various domains and sectors (e.g., CB Insights, Investopedia, Accenture). In addition, you may come across lists of FinTech domains online that are either longer or shorter than the list above; there is no one comprehensive list.

### 2. Choose a Canadian company (or project) within  your chosen FinTech domain

Use online research to identify the trends in your domain in the Canadian market, and choose a Canadian company that is successful or otherwise interesting to you. For example, if you chose Wealth Management, you may want to look at online journals, periodicals, reports, and websites about the future of Wealth Management, or how FinTech is changing or disrupting Wealth Management in Canada.

Your company could be:

* A new, emerging Canadian FinTech company that is doing well in a particular domain. Examples include Coinsquare, Borrowell, Shopify, or Finaeo.

* A large incumbent financial or technology company that is doing something interesting and new with technology. Examples include National Bank of Canada Blockchain, Goldman Sachs’ Marcus, JP Morgan’s JPMCoin, Facebook Libra, and Apple Card.

* A smaller start-up that is not yet wildly successful, but that you find promising and interesting. This may include a FinTech company in your local area or a company with a new idea that you would like to learn more about.

### 3. Conduct your research, using the case study template as a guide

We recommend that you use the case study template below in order to focus your research. You may lengthen, shorten, or––if necessary––remove sections from the template to accommodate the information available about your company.

**Note** If you have chosen a project within a larger company (such as the Apple Credit Card), you may want to focus your research on the origins and scope of the project rather than on the company itself.

---

# Proof of Authority Development Chain

For this assignment, you will take on the role of a new developer at a small bank.

Your mission, should you choose to accept it, will be to set up a testnet blockchain for your organization.

To do this, you will create and submit four deliverables:

* Set up your custom testnet blockchain.

* Send a test transaction.

* Create a repository.

* Write instructions on how to use the chain for the rest of your team.

## Background

You have just landed a new job at ZBank, a small, innovative bank that is interested in exploring what
blockchain technology can do for them and their customers.

Your first project at the company is to set up a private testnet that you and your team of developers
can use to explore potentials for blockchain at ZBank.

You have decided on setting up a testnet because:

There is no real money involved, which will give your team of developers the freedom to experiment.

Testnets allows for offline development.

In order to set up a testnet, you will need to use the following skills/tools we learned in class:

* Puppeth, to generate your genesis block.

* Geth, a command-line tool, to create keys, initialize nodes, and connect the nodes together.

* The Clique Proof of Authority algorithm.

Tokens inherently have no value here, so we will provide pre-configured accounts and nodes for easy setup.

After creating the custom development chain, create documentation for others on how to start it using the pre-configured
nodes and accounts. You can name the network anything you want, have fun with it!

Be sure to include any preliminary setup information, such as installing dependencies and environment configuration.

## Instructions

### Setup the custom out-of-the-box blockchain

* Create a new project directory for your new network. Call it whatever you want!

* Create a "Screenshots" folder inside of the project directory.

* Create accounts for two (or more) nodes for the network with a separate `datadir` for each using `geth`.

* Run `puppeth`, name your network, and select the option to configure a new genesis block.

* Choose the `Clique (Proof of Authority)` consensus algorithm.

* Paste both account addresses from the first step one at a time into the list of accounts to seal.

* Paste them again in the list of accounts to pre-fund. There are no block rewards in PoA, so you'll need to pre-fund.

* You can choose `no` for pre-funding the pre-compiled accounts (0x1 .. 0xff) with wei. This keeps the genesis cleaner.

* Complete the rest of the prompts, and when you are back at the main menu, choose the "Manage existing genesis" option.

* Export genesis configurations. This will fail to create two of the files, but you only need `networkname.json`.

* You can delete the `networkname-harmony.json` file.

* Screenshot the `puppeth` configuration once complete and save it to the Screenshots folder.

* Initialize each node with the new `networkname.json` with `geth`.

* Run the first node, unlock the account, enable mining, and the RPC flag. Only one node needs RPC enabled.

* Set a different peer port for the second node and use the first node's `enode` address as the `bootnode` flag.

* Be sure to unlock the account and enable mining on the second node!

* You should now see both nodes producing new blocks, congratulations!

### Send a test transaction

* Use the MyCrypto GUI wallet to connect to the node with the exposed RPC port.

* You will need to use a custom network, and include the chain ID, and use ETH as the currency.

![custom-node](Images/custom-node.png)

* Import the keystore file from the `node1/keystore` directory into MyCrypto. This will import the private key.

* Send a transaction from the `node1` account to the `node2` account.

* Copy the transaction hash and paste it into the "TX Status" section of the app, or click "TX Status" in the popup.

* Screenshot the transaction metadata (status, tx hash, block number, etc) and save it to your Screenshots folder.

* Celebrate, you just created a blockchain and sent a transaction!

![transaction-success](Images/transaction-success.png)

### Create a repository, and instructions for launching the chain

* Create a `README.md` in your project directory and create documentation that explains how to start the network.

* Remember to include any environment setup instructions and dependencies.

* Be sure to include all of the `geth` flags required to get both nodes to mine and explain what they mean.

* Explain the configuration of the network, such as it's blocktime, chain ID, account passwords, ports, etc.

* Explain how to connect MyCrypto to your network and demonstrate (via screenshots and steps) and send a transaction.

* Upload the code, including the `networkname.json` and node folders.

### Remember, *never* share your mainnet private keys! This is a testnet, so coins have no value here!

### Challenge mode

* Create a separate `bootnode` dedicated to connecting peers together

* There will be a new DevOps engineer joining the team, add an additional sealer address to the network on the fly!
