## 20.1 Lesson Plan: Debunking Smart Contracts

---

### Overview

Today's class introduces students to smart contracts.

At a glance, smart contracts are computer programs that allow credible transactions of digital assets under certain conditions without third parties. In this Unit, students will learn what a smart contract is, and they will build smart contracts using [Solidity](https://solidity.readthedocs.io/en/latest/index.html), an object-oriented language for implementing smart contracts in Ethereum.

Today's class will introduce students to the fundamental concepts of smart contracts, as well as to the development tools and environment they will use to create, compile, and deploy their smart contracts.

### Class Objectives

By the end of the Unit, students will be able to:

* Explain what a smart contract is, and its applications in FinTech and other business areas.

* Understand how Solidity works and identify its differences with Python as a programming language.

* Explain how the Ethereum Virtual Machine (EVM) is an isolated environment, and how Solidity code can only access on-chain data.

* Recognize that a smart contract is a program that runs on the EVM (Ethereum Virtual Machine)

* Identify the different kinds of smart contracts and their top use cases.

* Explain how Remix & Ganache support blockchain development.

* Set up their developer environment using Remix and Ganache.

### Instructor Notes

* Smart contracts have a lot of math and computing complexity that is beyond the scope of today's class. The goal of this lesson is to show students how smart contracts work and what tools are used to create, compile, and deploy smart contracts.

* Smart contracts have several applications beyond the financial sector such as medical, industrial (supply chain), cybersecurity, and many more. Feel free to include additional use cases or applications that you believe are suitable for the class.

* Setting up the development environment may be tricky; be sure to follow the [installation guide](../Supplemental/unit-20-install-guide.md) before the class to get familiarized with the process.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1nTdsL4xs1-BWEpdjocEA0DW4SoUJRLXGjwRMb3G5L44/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students to the smart contracts unit!

Open the lesson slides and briefly introduce smart contracts:

* Smart contracts are just computer programs that can run on a blockchain.

* They are used to allow credible transactions of digital assets under certain conditions without third parties.

* Using smart contracts allow for building completely decentralized applications, called `dApps`.

* Today, we will be exploring the smart contract/dApp ecosystem and getting familiar with the development tools needed to build them.

Explain to students that smart contracts are disrupting the way we understand the ownership and transference of goods, not only digital but also tangible.

This is why smart contracts are being used beyond the financial sector in government, real state, supply chain, and health care.

Let's start by exploring some use cases of smart contracts!

---

### 2. Instructor Do: Introduction to Smart Contracts and dApps (10 min)

In this activity, students will learn more about smart contracts, and they will be introduced to the concept of decentralized applications (dApps).

Open the lesson slides and conduct a facilitated discussion by starting with the following question:

* If smart contracts are computer programs that allow credible transactions of digital assets under certain conditions without third parties, what could be the building blocks to define and deploy smart contracts?

If nobody answers the question, lean on blockchain enthusiasts in the class to start the discussion by asking the question directly to one of them.

Spend up to three minutes in this initial question, and use the classroom board to create a list of the building blocks shared by the students. Summarize the answers with the following list and explain each bullet.

* A reliable and robust blockchain technology.

 * **Explanation:** We will use Ethereum in this class, a platform that not only offers a cryptocurrency but also, it is a blockchain-based distributed computing platform featuring smart contract functionality and applications development.

* A robust and reliable programming language.

 * **Explanation:** Along the following weeks, we will use Solidity, one of the best programming languages to create and deploy smart contracts in Ethereum.

* An isolated execution environment.

 * **Explanation:** We will use the Ethereum Virtual Machine (EVM), a powerful, sandboxed virtual stack embedded within each full Ethereum node.

* Robust encryption mechanisms.

 * **Explanation:** As we learned in the previous units, Ethereum uses public and private keys encryption mechanisms to ensure the confidentiality of the data transmitted in the blockchain.

* An industry-supported blockchain technology.

 * **Explanation:** Beside the [Ethereum Foundation](https://www.ethereum.org/), who is in charge of the development of the Ethereum framework, several companies also support Ethereum through [the Enterprise Ethereum Alliance (EEA)](https://entethalliance.org/). Various blockchain start-ups, research groups, and Fortune 500 companies form this association ([full list of members](https://entethalliance.org/members/)).

* A suitable set of development tools to create and deploy smart contracts.

 * **Explanation:** As part of the Ethereum development toolbox, we have software tools like Remix, Truffle, and Ganache, that help developers to comfortably and confidently create, compile, and deploy smart contracts. These are the tools we are going to use in this Unit.

Continue in the lesson slides, move the `Decentralized Applications` section, and highlight the following:

* At a glance, a **decentralized application or dApp** is a software that has a decentralized operation and uses decentralized storage or a database.

* In contrast to traditional software applications that generally run in a centralized server and use central storage or database, dApps run in a decentralized environment that is provided by the nodes in the blockchain.

* The concept of dApps was formally presented in 2015 by David Johnston, _et al._ in a white paper entitled ["The General Theory of Decentralized Applications, Dapps"](https://github.com/DavidJohnstonCEO/DecentralizedApplications) where the authors defined the criteria that dApps should comply:

 * Decentralized operation: open-source code, autonomous operation, consensus of its users.

 * Decentralized storage: storage on a blockchain, cryptographically sealed.

 * Cryptographic cryptocurrency: use of tokens for access and value contribution.

 * Token generation: tokens as proof of value, generated through a cryptographic algorithm.

* Using dApps, we can develop software applications not only for the financial sector but also for web browsers, cloud storage, instant messaging, social networks, and even operating systems.

Explain to students that this new paradigm of software development is also known as version 3 of the Internet or Web 3.0. Web 1.0 was the beginning of the Internet were websites were very simple with limited interactivity, and the basic tools and protocols were defined; Web 2.0 was marked by the rise of social networks and cloud computers, the new Web 3.0 is the evolution of the Internet to a decentralized environment powered by blockchain technologies.

Comment to students that in the following weeks, they will learn how to create and deploy dApps using the Ethereum platform.

Answer any questions before moving on.

---

### 3. Student Do: Smart Contracts in Action (15 min)

In this activity, students will work in groups up to three people to analyze several use cases to explore that correspond with popular types of smart contracts like tokens, notaries, supply chain, digital marketplaces, etc.

Circulate through the room while students are completing the activity. Look to identify students who are actively engaging peers and digging deeper. Keep these students in mind for later, as they may be helpful to distribute among groups.

If students are actively engaged with each other and the research process, they are succeeding at this exercise.

The only way to not excel at this exercise is to not participate in the research.

**Instructions:**

* [README.md](Activities/01-Stu_Smart_Contracts_Research/README.md)

---

### 4. Instructor Do: Smart Contracts in Action Review (5 min)

Conduct a facilitated discussion by asking a couple of groups to share their conclusions and insights about the use cases their review, focus on discussing with the class which features they noticed are compliant with the criteria from ["The General Theory of Decentralized Applications"](https://github.com/DavidJohnstonCEO/DecentralizedApplications).

* Decentralized operation: open-source code, autonomous operation, consensus of its users.

* Decentralized storage: storage on a blockchain, cryptographically sealed.

* Cryptographic cryptocurrency: use of tokens for access and value contribution.

* Token generation: tokens as proof of value, generated through a cryptographic algorithm.

Have groups share a few items on the lists of features they curated, answer any questions before moving on.

---

### 5. Everyone Do: Installing MetaMask (10 min)

In this activity, the instructor will have the class installing the [MetaMask](https://metamask.io/) browser extension, and import their mnemonics to enable dApp support on their web browsers.

Open the lesson slides, move to the `Installing MetaMask` section, and highlight the following:

* MetaMask is a web browser extension that allows you to run an Ethereum decentralized application (dApp) right in your browser without running a full Ethereum node.

* We are going to use MetaMask to run our dApps and make transfers to our blockchains.

Slack out the MetaMask web address to students (https://metamask.io/), open the URL in your browser, and ask students to follow you along the installation process.

![MetaMask installation - 1](Images/metamask-1.png)

Explain to students that since MetaMask is a web browser extension, it will run seamlessly in any operating system.

* When you navigate to the MetaMask's URL, your browser will be automatically detected, if not, choose the correct version.

* The Google Chrome extension is going to be used in this demo.

Click on the `Get Chrome Extension` link, a new window is going to be opened where you will be able to install the MetaMask extension from the Chrome Web Store.

![MetaMask installation - 2](Images/metamask-2.png)

Click on the `Add to Chrome` button to start the installation process.

Next, a pop-up window will be opened where you have to click on the `Add Extension` button to continue.

![MetaMask installation - 3](Images/metamask-3.png)

When the `Welcome to MetaMask` website opens, explain to students that they should see a small `fox icon` in the toolbar if MetaMask was successfully installed in their web browsers.

![MetaMask installation - 4](Images/metamask-4.png)

To start configuring your MetaMask account, click on the `Get Started` button.

Explain to students that we will import the wallet that runs in our local blockchain.

Click on the `Import Wallet` button to continue.

![MetaMask installation - 5](Images/metamask-5.png)

Explain the following points about the usage agreement:

* The usage agreement is where the MetaMask team asks you to collaborate on improving the tool.

* This agreement to participate is optional and is a personal choice.

![MetaMask installation - 6](Images/metamask-6.png)

In the next window, explain to students that they should enter the twelve word mnemonic of their local wallet, their wallet password, and they should click on the `I have read and agree to the Terms of Use` checkbox to continue.

Explain to students that we can securely accept the `Terms of Use` from MetaMask. If anyone has a concern about this step, invite them to read through the terms by clicking on the link.

![MetaMask installation - 7](Images/metamask-7.png)

After filling out your wallet details, click on the `Import` button to continue, and you will see the following confirmation page.

![MetaMask installation - 8](Images/metamask-8.png)

Students may notice a message at the bottom of the page that says that `MetaMask cannot recover your seed phrase`. Explain to students that this means that once you import your keys, MetaMask won't export them again, so if you lose your mnemonic, you can't extract it from metamask. Encourage students to keep their mnemonics in a safe place!

Click on the `All Done` button to continue. Explain to students that they will see a page showing the balance of their wallet and the transaction history.

![MetaMask installation - 9](Images/metamask-9.png)

Explain to students that they may have `0 ETH` and no transactions. Explain to students that this is all right from now since we have not started our local blockchain. We will learn how to connect MetaMask with our local wallet in future activities.

Explain the following about the wallet keys:

* In Ethereum, the same keys can be used across any Ethereum network.

* Addresses can have difference balances on each of these networks.

* Regardless of the network (i.e., main net, Kovan, Ropsten, or a local blockchain), all of these networks use the same addresses and keys.

Congratulate students on getting started with their first dApp!

Answer any questions before moving on.

---

### 6. Instructor Do: Intro to Remix and Ganache (15 min)

In this activity, the instructor will demo the tools used by smart contract engineers to develop, compile, and deploy code on the Ethereum blockchain. Students will gain familiarity with tools from the `Truffle Suite`, namely `Ganache`, the one-click development blockchain.

**Files:**

* [MessageBoard.sol](Activities/06-Ins_Intro_to_Remix_and_Ganache/Solved/MessageBoard.sol)

Start by launching Ganache. While Ganache is starting, take a moment to tell the students a little bit about Ganache and the Truffle suite.

* Truffle is a development environment for Solidity. It includes a compiler, some script tools, etc.

* Ganache is a one-click Ethereum blockchain.

* Ganache is part of Truffle. It makes development on blockchains very quick, which is awesome; however, the algorithm that powers it is not secure.

![ganche_create_workspace.png](Images/ganache_create_workspace.png)

Click `New Workspace` to create a new workspace.

![ganache_set_workspace_name.png](Images/ganache_set_workspace_name.png)

* Workspaces in Ganache are a configuration for a development blockchain. Each workspace can be a different template for how you want to launch your development chain.

* Workspaces allow you to customize many things about your chain:
 * An initial pre-mine of any size deposited into any number of generated addresses.

 * Specific ports for talking to your blockchain node.

* Let's name our new workspace `fintech`.

* As you can see, there is another field titled `TRUFFLE PROJECTS`. What this field allows you to do is link a project that uses the `truffle solidity compiler`. Today we will not be using the truffle compiler. We will use `remix`; Ethereum foundations online implementation of the `solidity compiler`.

Click the Server tab.

![ganache_set_server_info.png](Images/ganache_set_server_info.png)

* The `HOSTNAME` field is the interface on your computer where the node will bind to listen for connections. We want this to be set to `127.0.0.1`, commonly referred to as `localhost`.

* The `PORT` field is the port that your node will be listening for communication. For all of our examples, we will be using port `8545`.

* You don't need to worry about the `NETWORK ID` field; it is for Ganache's internal tracking.

* The `automine` feature is a very convenient option; when a transaction happens, such as someone executing/deploying a smart contract or sending/receiving funds, the block is instantaneously processed so that there is no wait time.

* `Automine` is convenient because you can see the results of transactions instantaneously but dangerous in the fact that it is not representative of how a blockchain normally functions.

* The `ERROR ON TRANSACTION FAILURE` is useful because it will log additional information about errors to our GUI.

Now click `Accounts and Keys`.

![ganche_create_workspace.png](Images/ganache_import_mnemonic.png)

* As previously mentioned, Ganache allows you to pre-mine a selected number of coins into a selected number of generated addresses. This is useful for testing smart contracts.

* `ACCOUNT DEFAULT BALANCE` is the number of coins in `Ether` that will be in each address.

* `TOTAL ACCOUNTS TO GENERATE` is the number of accounts that will be generated containing the balance.

Emphasize the importance of the wallet mnemonic to an Ethereum wallet and its ability to generate addresses.

* `AUTOGENERATE HD MNEMONIC` is another way to auto-generate our mnemonic. We, however, are going to be using our previously generated mnemonics.

![ganache_set_chain.png](Images/ganache_set_chain.png)

* We are going to keep our `Gas Limit`, `Gas Price`, and `HardFork` at their default values; these are reasonable defaults.

Click `Save Workspace`.

![ganache_accounts.png](Images/ganache_accounts.png)

Elaborate on the following sections of the Ganache accounts page.

* The workspace info bar displays the settings for your current workspace, many of these values should be familiar from the initial setup.

* As you can see, our wallet mnemonic is also listed.

* We also have the list of pre-generated addresses from our wallet, each with the `100 eth` balance that we set in the Ganache workspace setup.

Click the blocks tab:

![ganache_blocks.png](Images/ganache_blocks.png)

This page should be relatively empty, only listing block zero -- explain:

* Since it is a new workspace, the blockchain only consists of the block that contains our initial blockchain configuration.

* As more transactions happen, more blocks will be mined instantaneously because of the `automine` feature.

* The remaining pages, much like the blocks page, will also be relatively blank until we begin interacting with our blockchain.

Inform the students that they will have time to explore the various pages of Ganache as they set up their Ganache blockchain in the next activity.

* Ganache is now running the local development blockchain on `localhost:8545`.

Open [Remix](http://remix.ethereum.org) in your web browser.

![remix_home.png](Images/remix_home.png)

Briefly introduce Remix:

* Remix is an online IDE and compiler for the `Solidity` smart contract language.

* Remix allows you to write, compile and deploy Solidity smart contracts onto the Ethereum blockchain.

Enable the `Solidity` development environment by clicking on the "Solidity" button on the Remix Home tab.

![remix_solidity_env](Images/remix_enable_solidity_env.gif)

Create a new smart contract by clicking the `Add local file` button. Then, populate the contents with [MessageBoard.sol](Activities/06-Ins_Intro_to_Remix_and_Ganache/Solved/MessageBoard.sol).

![remix_open_file](Images/remix_open_file.png)

The Solidity file's code should appear in the editor window.

![remix_editor_message](Images/remix_editor_message_board.png)

Reassure the students that though this contract may look complicated now, soon it will make a lot more sense.

Click the `Solidity Compiler` button on the Remix sidebar then click `Compile` to compile the contract.

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

You will see a connection request from MetaMask to connect Remix with your local blockchain, click the "Connect" button to continue.

![remix_metamask_connection](Images/remix_metamask_connection.png)

Explain to the students that:

* Web3 is a library that allows you to communicate with Ethereum nodes.

* We must set our environment to `Injected Web3` so that Remix can talk to MetaMask, which can talk to our local blockchain. In this case, MetaMask is "injecting" the Web3 library into your browser, which allows Remix to communicate to the outside world (Ethereum).

* We will be writing our own custom smart contracts tomorrow, but today we will just be familiarizing ourselves with Remix.

---

### 07. Students Do: Setting up Remix and Ganache (15 min)

Students will setup Ganache, create a workspace for `fintech`, set the `RPC port` to `8545`, and import their `mnemonic` into Ganache's settings to keep their wallets consistent in their test blockchain. Then, they will explore the Remix IDE with the time left.

**Instructions:**

* [README.md](Activities/07_Stu_Setting_up_Remix_And_Ganache/README.md)

Have the TA's circulate the room to assist with any installation issues that students may be having -- Students may have to add an allow rule to windows firewall.

---

### 08. Instructor Do: Remix and Ganache Review (5 min)

Open Ganache and ask the students the following questions.

* How might a local development blockchain like Ganache make it easier to develop smart contracts?

 **Answer** It allows potentially insecure code to run in a private(non-public) environment.

 **Answer** It saves you from having to purchase actual ether.

 **Answer** Ether is automatically generated in your wallet for testing smart contracts.

 **Answer** Transactions happen right away.

* How might remix make it easier to write smart contracts?

 **Answer** You can write a smart contract from pretty much any browser.

 **Answer** It allows for writing, compiling, and deploying all in one place.

 **Answer** It supports connecting to local development blockchains.

---

### 09. BREAK (15 min)

---

### 10. Instructor Do: Contextualizing Solidity (15 min)

In this exercise, the instructor will explain to the students that Solidity is a statically typed language and that it runs inside the Ethereum Virtual Machine (EVM) in a sandbox.

* Solidity is the language of smart contracts used by Ethereum, as well as Ethereum-compatible blockchains like IBM's Hyperledger Fabric and Burrow, JPMorgan Chase's Quorum, Ethereum Classic, and last, but not least, Counterparty which extends Bitcoin to support the EVM.

* Solidity is a statically typed language, so it will also help you understand other statically typed languages you may have heard of, like C, C++, Go, Java, Rust, and many more.

Present the following diagram to the class and give them a few minutes to think about what is being illustrated.

Try to conceptualize what is happening in the graphic.

![Diagram](Images/EVM.png)

* The Ethereum Virtual Machine is a sandboxed environment backed by a virtual stack and capable of performing calculations. There's an EVM embedded within every Ethereum full node on the Ethereum network. Since code executes inside the sandboxed processes of the Ethereum node, machine code remains isolated from the host machine. Let's break down the levels of the following graphic.

* Higher Level language

 * Solidity is the `Higher Level Language` of the EVM.

 * A higher level language allows code to be written that is independent of a particular computer's hardware.

 * A higher level language is a language that is more easily understandable for humans than machine code.

 * A higher level language cannot be understood by a computer; it has to be compiled to machine code by the compiler before it can be understood.

* Machine Code

 * EVM machine code consists of a list of instructions that the EVM will perform.

 * A user pays a certain amount of `gas` for each instruction that gets executed by the EVM.

 * Instead of just a plain transaction fee like with Bitcoin, users pay fees based on running different computations. Each computation has a different `gas` cost associated with it.

 * The cost of each of these opcodes is determined by the community, in the Ethereum node software. In fact, it is updated occasionally to keep the network fair when certain opcodes become too expensive for average nodes to process.

Show the class the example machine code.

```bytecode
"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x40 MLOAD PUSH2 0x872 CODESIZE SUB DUP1 PUSH2 0x872 DUP4 CODECOPY DUP2 DUP2 ADD PUSH1 0x40 MSTORE PUSH1 0x20 DUP2 LT ISZERO PUSH2 "
```

* This is what the Solidity code compiles down to. As you can see, there are different instructions, aka "opcodes" that are telling the EVM exactly what to do.

* Virtual Machine

 * The EVM contains a memory, storage, and all of the essential parts of a physical computer, just virtual, and sandboxed inside of your Ethereum node.

 * Every Ethereum node runs the EVM, which is how all Ethereum nodes are able to process and validate transactions and smart contracts.

* Process/Runtime

 * The process/runtime is the actual process that runs on the host machine.

 * The Ethereum node spawns a process for the EVM.

 * While each node can verify transactions within its own EVM, it takes multiple full nodes running their own EVMs to secure the network properly.

 * `Geth` is one implementation of an Ethereum full node written in GO.

* Hardware

 * Since blockchains are written in software, the hardware can be any machine that is capable of running the node software and connecting to the internet.

---

### 11. Students Do: Contextualizing Solidity Worksheet (10 min)

Students will fill in a simple chart (pipeline) of the various levels of the EVM's architecture with the names of the various levels and their real-world implementation.

**Instructions:**

* [README.md](Activities/10_Stu_Contextualizing_Solidity_Worksheet/README.md)

**Files:**

* [WorkSheet - Solved](Activities/10_Stu_Contextualizing_Solidity_Worksheet/Solved/evm_worksheet.md)

* [WorkSheet - Unsolved](Activities/10_Stu_Contextualizing_Solidity_Worksheet/Unsolved/evm_worksheet.md)

---

### 12. Instructor Do: Contextualizing Solidity Review (5 min)

Once again, display the completed graphic of the EVM's architecture to the class.

![Solved](Images/EVM_graphic.png)

Ask the class the following recall questions:

* What is a potential benefit of executing code in a virtual machine?

 **Answer** The code executed in a virtual machine cannot affect the host machine directly.

 **Answer** The code can run anywhere the virtual machine can run.

* What do you think some benefits of Solidity being a compiled language might be?

 **Answer** Human readable code can turn into a machine-readable code.

 **Answer** Code can be executed faster.

* What's an example of a programing language that humans write, e.g. `High-level languages`?

 **Answer** Solidity

 **Answer** C++

 **Answer** Java

---

---

### 12. BREAK (15 min)

---

### 13. Instructor Do: Unveiling Decentralized Apps (15 min)

In this activity, students will learn about the different sectors where dApps are disrupting the traditional market practices in such areas as banking, exchanges, games, and art.

Open the lesson slides, move to the "Unveiling Decentralized Apps" section and highlight the following:

* dApps are currently used beyond the finance sector.

* The dApps universe is still under development, according to a [report made by Fluence Labs](https://medium.com/fluence-network/dapp-survey-results-2019-a04373db6452), the most active projects started as early of 2018, and the oldest is from 2017.

* dApps are currently used in diverse sectors, but gaming seems to be the most popular use case nowadays.

 ![dApps by sector](Images/dapps-by-category.png)
 _[Source](https://medium.com/fluence-network/dapp-survey-results-2019-a04373db6452#21f2)_

* According to the Fluence Labs' report, the major obstacle to dApps adoption is new users onboarding.

Continue with lesson slides and ask the following question to students:

* If you were about to start a dApp program, how will you boost your new users' base?

If no-one answers the question, ask for a volunteer from the blockchain enthusiast in class to share her or his insights. You may conclude with the following example.

* From radio to television and now the internet, every new disrupting technology has faced adoption challenges. In the end, part of the solution has been to ease how people use technology. In other words, improving the user experience may increase the new user base.

Open your browser and navigate to the [State Of The Dapps website](https://www.stateofthedapps.com/). Explain to students that this platform showcases a panorama of the dApps ecosystem and ranks the dApps based on an analysis of GitHub activity.

Start the website navigation as you explain that this ranking was initially focused on Ethereum. However, this website presents dApps developed for other blockchain platforms, as well.

![State Of The Dapps - 1](Images/state-of-the-daps-1.png)

In the navigation menu at the top, click on the "All DApps" option, and highlight the following:

![State Of The Dapps - 2](Images/state-of-the-daps-2.gif)

* This option allows us to search for the best directory of dApps.

* The results can be filtered by `platform`, `category`, and `status`.

* We may be interested in those projects that are `live`.

Click on the "Rankings" option in the navigation menu and explain to the students that using this option, they can navigate through the dApps listing according to the rank given by the website's statistics.

![State Of The Dapps - 3](Images/state-of-the-daps-3.png)

* The rank is updated daily, and it's based on multiple factors including active users (unique source addresses in transactions to DApp contracts), transaction volume, developer activity, profile freshness and strength, and user recommendations.

* The results can be filtered by `platform` and `category`.

Continue by visiting the "Stats" section from the navigation menu and highlight the following:

![State Of The Dapps - 4](Images/state-of-the-daps-4.gif)

* This section of the website presents general statistics about the dApps ecosystem.

* It can be seen that the number of dApps is increasing across the time.

* This information can be used to benchmark the current state of the dApps ecosystem, as well as to analyze trends by a specific sector.

In the search box at the top, look for the `nexo` project, explain to students that you are going to talk about one project that is doing a worth to mention work on attracting new users through improving user experience.

![State Of The Dapps - 5](Images/state-of-the-daps-5.gif)

* Nexo is an instant crypto lending provider on a global scale, servicing more than 40 currencies across more than 200 jurisdictions.

Click on the "Launch DApp/website" button below the logo of Nexo on the right side to open the project's website and highlight the following:

* Nexo is facing the challenge of users' adoption by offering its services via a website and a mobile application.

* Nexo also offers traditional channels to dispose of your money invested in cryptocurrency by a credit card that allows users to get a credit line worldwide based on the amount of cryptocurrency saved in its wallet.

* Nexo also becomes international, by offering its services in different languages.

 ![State Of The Dapps - 6](Images/state-of-the-daps-6.png)

Explain to students that as it can be seen so far, this project is trying to disrupt in the banking sector by offering a solution to earn interest with cryptocurrency savings and offering an automated line of credit.

Go further with the demo, click on the "Create Account" button in the upper right corner, and follow the next steps.

![State Of The Dapps - 7](Images/state-of-the-daps-7.png)

**Note:** You may want to use a testing e-mail account for this demo.

* To create an account, enter your e-mail and password. Solve the verification challenge and click on the "Sign Up" button.

 ![State Of The Dapps - 8](Images/state-of-the-daps-8.png)

* After entering your account details, you will see the next page asking for verification of your e-mail account.

 ![State Of The Dapps - 9](Images/state-of-the-daps-9.png)

* Open your inbox, verify your e-mail address using the message you received from Nexo. This link will redirect you to the following confirmation page.

 ![State Of The Dapps - 10](Images/state-of-the-daps-10.png)

* After clicking on the "Continue to your Nexo Account", you will have instant access to your brand new account.

 ![State Of The Dapps - 11](Images/state-of-the-daps-11.gif)

* The user experience excels since you can start using your brand new account with just a few clicks without leaving your computer.

* You can start making transactions and saving cryptocurrency assets by using Nexo as your wallet.

* To allow bank withdrawal and gain access to the full services offered, you need to verify your identity.

Explain to students that this is a demonstration of how a traditional service (saving money and having a credit card) can be simplified and disrupted using the same blockchain technology they are learning in class.

Ask students the following rhetoric question:

* How could you disrupt in any other sector than finance creating a dApp?

Comment to students that they will answer to this question in the next activity and continue with the next dApp demo.

In the next dApp demo, students will learn how they can use a dApp by transferring `ETH` to use the service provided by the dApp using MetaMask, explain to students that this is how normally they will interact with a dApp.

Open your browser and navigate to https://www.akta.io/. Akta is a cloud file storage service that uses the `Ropsten` test network to work, so you should be sure that you have `ETH` in your wallet in this test network if you don't have any token in this test network, refer to the ["Getting Ropsten Tokens Guide"](../Instructor_Support/getting-ropsten-tokens.md) in the Instructor Support folder.

Once you open the Akta website, follow the next steps to conduct the demo.

1. Click on the MetaMask fox icon in the toolbar, and ensure you have selected the `Ropsten` test network and you have `ETH` available in your wallet.

 ![State Of The Dapps - 12](Images/state-of-the-daps-12.png)

2. Click on the "Log In" button to continue.

3. On the next page, you will be asked to link an Ethereum account to start using Akta, click on the "Connect Account" button to continue.

 ![State Of The Dapps - 13](Images/state-of-the-daps-13.png)

4. You will see a pop-up window where MetaMask is asking you for permissions to connect Akta your account, click on the "Connect" button to continue.

 ![State Of The Dapps - 14](Images/state-of-the-daps-14.png)

 * DApps will typically request access to this connection before using it. Since the wallet address is unique, dApps can use it as login credentials. The connection is then securely made through the selected Ethereum network.


5. Next, you are asked to sign the Smart Contract to continue the connection process, click on the "Sign" button to proceed.

 ![State Of The Dapps - 15](Images/state-of-the-daps-15.png)

6. After signing the smart contract, you are led to the Akta main page. Explain to students that we have not transferred any `ETH` yet. We allow the dApp to connect to our wallet only after signing the contract.

 ![State Of The Dapps - 16](Images/state-of-the-daps-16.png)

7. Now, we are going to upload a document to show how the transactions work. Click on the "Add" button to upload a file.

8. On the next page, you have to choose the file to upload. Optionally, you can send an e-mail to any person if you want to share this file. However, we will omit this part in this demo. Click on the "Choose File" button and select any file from your local computer (you may upload a generic picture for this demo). Continue by clicking the `Upload` button.

 ![State Of The Dapps - 17](Images/state-of-the-daps-17.png)

9. You will be warned that the document has no signature. Since this file is for personal usage, we can proceed by clicking on the `OK` to continue.

 ![State Of The Dapps - 18](Images/state-of-the-daps-18.png)

10. Next, you have to assign a name to the file, type the name of your choice, and click "OK" to continue. You can only use letters and numbers.

 ![State Of The Dapps - 19](Images/state-of-the-daps-19.png)

11. In the next dialog box, you will be informed that your file is going to be uploaded to the blockchain, so the process is going to take some time. Click on the "OK" button to continue.

 ![State Of The Dapps - 20](Images/state-of-the-daps-20.png)
 The upload time depends on your internet connection speed and the current state of the blockchain workload; it takes less than one minute while preparing this demo with a `3.2 MB` file in a WiFi connection with `10 mbps` upload rate, for the class demo you may use a smaller image file or a text file.

12. You are going to be asked to sign the file upload transaction using MetaMask, click on the "Sign" button to proceed.

 ![State Of The Dapps - 21](Images/state-of-the-daps-21.png)

13. Next, you are asked to pay in `ETH` for the transaction using your wallet in MetaMask. You may note that the transaction is free. Still, you are requested to pay the `GAS` fee. This is the particular case for this dApp, explain to students that generally transactions in dApps will incur in costs to be paid in `ETH` in addition to the correspondent `GAS` fee. Click on the "Confirm" button to continue.

 ![State Of The Dapps - 22](Images/state-of-the-daps-22.png)

14. After confirming the transaction fee, you will be lead to the Akta home page where you can see your file uploaded to the blockchain.

 ![State Of The Dapps - 23](Images/state-of-the-daps-23.png)

End the activity by explaining to students that the goal of these two dApps demos is to show them how they can interact with dApps. Highlight the following closing points:

* Nexo is a dApp closer to a traditional web application; it combines the features of the typical web application with the decentralized power of dApps.

* Akta is a dApp with a frontend created to interact with the user and allow transactions using MetaMask.

* We use the `Ropsten` test network in this demo, however, dApps that are monetizing their services use the Ethereum main network, so you have actually to pay for the services those dApps provide.

Answer any questions before moving on.

---

### 14. Student Do: State Of The Dapps (20 min)

In this activity, students will visit [The State Of The Dapps website](https://www.stateofthedapps.com/) to explore the many dApps that exist in the blockchain ecosystem. Students will work in groups up to three people to research and to analyze a dApps from any sector from their interest.

Students will be encouraged to use MetaMask when possible, and write down a short report on their research.

Have TAs circulate the classroom to help students and foster collaboration in each group.

**Instructions:**

* [README.md](Activities/15-Stu_State_of_the_Dapps/README.md)

---

### 15. Instructor Do: State Of The Dapps Review (10 min)

In this activity, conduct a facilitated discussion to allow the students to share their findings after the previous research activity.

Remind students that Ethereum is one of the most used blockchains to create and deploy dApps. This is because Ethereum is more than a Cryptocurrency. It also offers a complete development framework to support different use cases.

Use this activity's time to allow all groups to share their findings regarding the following questions:

* Why did this dApp catch your attention?

* What is the status of this dApp?

* What blockchain network(s) does the dApp use?

* Is it possible to use MetaMask to interact with the dApps?

* How does the dApp disrupt the traditional market in its sector?

* How this dApp is facing new customers onboarding?

Answer any questions before moving on.

---

### 16. Instructor Do: Homework Demo (5 mins)

In this activity, students will get a big-picture overview of the homework.

**Files:**

* [README.md](../../../02-Homework/20-Solidity/Instructions/README.md)

Open the Unit 20 homework assignment instruction and briefly demo the homework instructions for students. Be sure to highlight the following:

* The goal of this homework assignment is to use Solidity to define, create, and deploy a smart contract dApp. MetaMask will be used to interact with the contract operations.

* The smart identity contract will be deployed as a dApp using GitHub pages.

* Starter code is provided that includes a small frontend that can be used to interact with the contract.

* Students will test their dApps locally, and also, by deploying their solution to a test net.

Explain to students that this will be an excellent opportunity to gain hands-on experience in creating and deploying smart contracts using Solidity.

Answer any questions before moving on.

---

### 17. Instructor Do: Recap (5 min)

Congratulate students on completing their first day on smart contracts! End the class by briefly reviewing the main concepts of the day, Smart Contracts and dApps.

Ask students to provide a definition of a smart contract and a dApp and then provide the following definitions:

* Smart contracts are computer programs that run on the blockchain, that allow for any computation. They are mainly used to allow credible transaction of digital assets under certain conditions without third parties.

* A dApp is a software application that has a decentralized operation and uses decentralized storage or database.

* In general terms, a smart contract is a decentralized application that can run on a blockchain.

Explain to students that we will begin to learn how to program smart contracts in Ethereum using the Solidity programming language.

By the end of this Unit, students will be writing their custom smart contracts and dApps for Ethereum!

### End Class
---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
