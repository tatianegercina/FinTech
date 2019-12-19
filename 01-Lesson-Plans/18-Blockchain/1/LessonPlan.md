## 18.1 Lesson Plan: Blockchain Building Blocks

### Overview

Today's class will introduce students to blockchain technologies. Students will learn the fundamentals of what the technology is, the types of problems it solves, and how it works.

Most of the people believe that blockchain is only about cryptocurrencies; the goal of this lesson is to break this myth, and get the students thinking about how blockchain technology is used and how it will likely affect their lives as a FinTech entrepreneur, as well as be able to use essential tools like wallets and block explorers to navigate the space and to hold a conversation about the topic.

### Class Objectives

By the end of the class, students will be able to:

* Describe why blockchain exists.

* Explain blockchain technology and its use cases to someone that doesn't have any blockchain background

* Describe the 5 Pillars of Open Blockchains.

* Use a blockchain wallet and explain how it works to somebody who doesn't know.

* Visualize transactions via block explorers.

* Students will be able to brainstorm solutions for the blockchain ecosystem without robust financial institutions.

* Students will be able to navigate the blockchain ecosystem

### Instructor Notes

* **Important Note:** For this week's activities, Windows users **MUST** use `git-bash` and not the default command prompt in Windows!

* Some students may already be involved with cryptocurrencies or other blockchain projects and may have some opinions already about particular blockchain implementations. Due to the niche nature of the field, they may have certain biases already.

* Ethereum has the largest developer community in the blockchain space, learning it has high skill transferability.

* While blockchain inherently has a finance-heavy set of use cases, encourage students to think bigger, since the technology can be used for building secure, globally distributed software.

* There is an activity called "Peoplechain" aimed to emulate the public, censor resistant, and borderless nature of the blockchain; be sure to read through before the class.

* If you encounter any issues with requesting KETH from the Kovan faucet, the following mnemonic phrase has been pre-funded with test tokens (**for instructors only!**):

  `use trouble sponsor panda camp grow pact matrix chief black napkin ghost`

  If you end up needing to use this wallet, simply import it into MyCrypto, change to the Kovan network, then distribute the KETH to the class and yourself.
  Since you can work with very small amounts of Ether, you should have plenty of KETH to work with. Sending `0.1` at a time should suffice.
  Make a note to help refill this later for other instructors once the Kovan faucet is back up and running.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1syUXqizy8YoZuYVrYmJwDFv1TADW5IqXX0a_Itkvh_w/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [18.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=17303471-178a-461d-8b72-ab1001881715) Note that this video may not reflect the most recent lesson plan.

---

### 1. Instructor Do: Welcome (5 min)

* **Files:**

Welcome students to the class by expressing excitement over starting the final lap in this boot camp marathon -- BLOCKCHAIN -- and that some might say it’s the most exciting lap by far!

Open the lesson slides and highlight the following:

* Blockchain is exciting - and critical for their careers - because blockchain technology powers not just cryptocurrencies but entire decentralized economies and even enterprise networks.

* Blockchain is a buzz-word in the industry, but it’s much more than that -- it’s a new way of thinking about money.

* Traditional financial institutions have been skeptical about blockchain technology, however, JP Morgan Chase, the largest U.S. bank, created [Quorum](https://www.goquorum.com/), an Ethereum-based blockchain, in order to leverage the security that blockchain provides for their own systems (and, probably, because they are afraid of being left in the dust by this new technology!).

* In this unit, students will be building their blockchain wallets, write smart contracts, and construct a blockchain from scratch.

Some of this may seem intimidating to the students, so express that you are proud of how far the class has already traveled together as a team; after 17 weeks together, the students can do Python, Pandas, and ML!; By the end of this block (get it?), they will be able to speak “blockchain” -- but we’re going far beyond the terminology.

Explain to the class that this final stage is huge. That’s going to be challenging, but you know they can do it - after all, they’ve made it this far!

Answer any questions before moving on.

---

### 2. Instructor Do: Blockchain Skill Check (5 min)

Before we dig in, let’s get a sense of where the class might be when it comes to blockchain.

Open the lesson slides and move to the "Have you heard?" section; ask a few questions and have the students give a thumbs up for yes or a thumbs down for no.

* How many of you have heard of blockchain before?

* How many of you have heard of cryptocurrency before?

* How many of you have ever used a blockchain, aka crypto wallet?

* How many of you have ever traded cryptocurrency?

Ask the students to hold out a [fist-to-five](https://k12teacherstaffdevelopment.com/tlb/what-is-fist-to-five-strategy/) (fist for 0, 5 fingers up for 5) to answer how familiar they are with the following topics:

* How familiar are you with blockchain?

* How comfortable do you feel having a conversation about blockchain technology?

* How familiar are you with Ethereum?

Remark on the results.

* “It looks like we have some blockchain experts - awesome!”

Take a mental note of the students with strong familiarity with blockchain, as you will be able to distribute them among groups that have less knowledge about the topic.

Ask the students to hold out again a fist-to-five (fist for 0, 5 fingers up for 5) to answer how familiar they were with the following topics before they started the course.

* How familiar were you with Python?

* How comfortable were you having a conversation about machine learning?

* How familiar were you with data science?

Remind the students that just like they learned how to master Python and ML, and they will surprise themselves with how much they learn over the coming weeks.

It may seem like a foreign language at times, but they’ve already learned a new language as part of this course, and you and the TAs will be there to guide them.

Tell the students it’s time to dig into blockchain: first things first, let’s start with a definition.

Ask the students if anyone has a definition of blockchain that they would like to share with the class. Thank the students for sharing.

Show the definition of blockchain on the slide, and ask the students to read it to themselves.

Ask them if they have questions. Then, break down the definition.

* A blockchain is a distributed "immutable" database that is not controlled by a single, central authority.

* The database is synchronized across the network, with special rules in place to incentivize good actors and disincentivize bad actors.

* It is immutable, which means you can only add to the database: you cannot change the history.

* This provides a powerful means of creating a trusted "source of truth" in a trustless environment.

Answer any questions before moving on.

---

### 3. Instructor Do: The Importance of Blockchain (10 min)

For this activity, the instructor will lead a formal discussion regarding what blockchain technology is and why it’s essential.

First, navigate to the slides and begin with the "Bank CEO" example:

Ask the students the following questions, allowing them to answer, then confirm each of the listed answers:

* "Why would a banker want to use a blockchain?"

 **Answer**: Using a blockchain for inter-bank communication is faster, more secure, and cheaper than the systems in place now, Swift and ACH.

* Why would an individual in an underbanked, developing, or authoritarian country want to use a blockchain?

 **Answer**: Transactions cannot be censored.

 **Answer**: You only need a mobile device and internet connection, which is a common commodity, even in developing countries.

 **Answer**: Some blockchains can be used as a hedge against hyperinflation of their native currency.

* Why would an individual in the US want to use a blockchain?

 **Answer**: Removes intermediaries like PayPal, Venmo, Cashapp, etc., and allows for peer to peer payments, thus lower fees.

 **Answer**: Custody over your funds, versus allowing a bank to have custody.

 **Answer**: Cheaper than domestic wire transfers

 **Answer**: Brings financial services typically available to the upper class to everyone.

* Why would anyone want to use blockchain?

 **Answer**: Fast, global transactions that are not managed by a single authority

 **Answer**: Secure, modern infrastructure for the next generation of the internet. This is also known as Web 3.0.

Answer any questions before moving on.

---

### 4. Students Do: Use Case Study (10 min)

Students will complete a thought experiment in which the students will get together in small groups and examine an example use case application
for different cryptocurrency and blockchain projects.

The goal is to have the students write down the features they glean from the different use cases.

The features listed by students will be compared against the 5 Pillars of Open blockchains in a forthcoming lecture.

Circulate through the room while students are completing the activity. Look to identify students who are actively engaging peers and digging deeper. Keep these students in mind for later, as they may be helpful to distribute among groups.

If students are actively engaged with each other and the research process, they are succeeding at this exercise.

The only way to not excel at this exercise is to not participate in the research.

**Instructions:**

* [README.md](Activities/04-Stu_Use_Case_Study/README.md)

---

### 5. Instructor Do: Use Case Study Review (5 min)

Discuss with the class which features they noticed.

Have groups share a few items on the lists of features they curated.

Some typical features may be:

* Transparency

* Privacy (in the case of Monero)

* Smart contracts

* Neutrality

* Hedge against hyperinflated currencies

* Bridge of trust between parties that might not trust each other

* Cross-border nature

* Pseudonymous system (addresses are your alias, not necessarily attached to identity)

Answer any questions before moving on.

---

### 6. Instructor Do: The 5 Pillars of Open Blockchains (10 min)

For this activity, the instructor will lead a formal lecture regarding what the five pillars of open blockchains are and why they are relevant.

See the [blockchain support document](../Instructor_Support/Blockchain.md) for a background video on this topic.

Start this activity by explaining the following to students:

* As we talk through each pillar, keep in mind what you uncovered during the previous exercise. What feature would you put in each category?

* These pillars are the fundamental features that blockchains were created to provide. Learning these will help you understand how some blockchains sacrifice these features for speed or marketing purposes instead of innovating on the underlying algorithms.

* The chains that innovate on these features are the most universal in terms of feature sets and can be easily adapted to enterprise.

Then, transition through the slides and begin talking about each topic.

Begin by prefacing that each of these pillars ties into each other to build an open blockchain network.

#### Pillar 1: Open

![screenshot of open slide](https://image.shutterstock.com/image-photo/open-blue-door-sunshine-600w-624832211.jpg)

* Openness in this context refers to access:

 * Anyone can access the source code and create a project from it, therefore developer access is high.

 * Anyone can access the chain and participate in the ecosystem.

 * Anyone can access the services the blockchain offers.

* Openness means that the system is designed to incentivize users to keep it open. The internet is an example of this, and it is built on open protocols that anyone can learn and contribute to.

#### Pillar 2: Borderless

![screenshot of borderless](https://image.shutterstock.com/image-photo/abstract-science-global-network-connection-600w-1147048595.jpg)

* Explain to the students that borderless means precisely that, a network without geographical or political borders.

* To be borderless, the network needs to be decentralized. This means that any central party does not hold control of the network.

* Since the blockchain is synchronized onto every device that helps maintain it (called nodes), it lives everywhere.

Ask the students: "Are you moving money across a border when you bring a credit card across customs?"

 **Answer**: No

Ask: "In that case, are you moving money across a border when you load cryptocurrency onto your phone and travel internationally?"

 **Answer**: Nope, you only have to register cash over 10k

Elaborate and bring out this analogy:

* Much like the money is not on the card itself, a crypto wallet does not hold the crypto itself, just the access.

* The blockchain is already synchronized to a device in the country you are traveling to, so accessing it is the same as if you were to swipe a Visa card internationally, only without Visa getting involved.

* You can also use a satellite connection to connect to blockchain networks and broadcast transactions, therefore it is truly global.

#### Pillar 3: Neutral

![screenshot of neutral](https://image.shutterstock.com/image-illustration/net-neutrality-abstract-background-260nw-1049711261.jpg)

* Explain how neutral means that the protocol does not discriminate against any user.

* In fact, users don't even need to be human. The blockchain does not care if you are a human or a washing machine.

* The blockchain is agnostic to the users, regardless of political or social status, or geographic location.

* A wealthy banker or government leader uses the protocol in the exact same way anyone else would.

* Open blockchain networks are also governed in a neutral fashion, with many using the blockchain itself for voting on the next network upgrades.

#### Pillar 4: Censor Resistant

![screenshot of censor resistant](https://image.shutterstock.com/image-illustration/closeup-surprised-desperate-looking-man-600w-1399238933.jpg)

* Blockchains that are properly decentralized are highly resistant to censorship and authoritarian control.

* This means that people suffering in nations that have high censorship can still find a way to use these systems to reach out and to bypass the oppression.

* Blockchain is being used currently around the world to avoid censorship or hyperinflation in many countries.

* It has been said that blockchain and crypto can be seen as an insurance policy against a dystopian future.

* Money is often compared to a form of speech. These are systems where this form of expression cannot be censored.

#### Pillar 5: Public

![screenshot of public](https://image.shutterstock.com/image-illustration/two-way-street-signs-words-260nw-156089513.jpg)

* Explain that this means that open blockchains are separate from the state. Public blockchain networks are suited for public affairs.

* Military or government work, or certain logistic implementations will likely be suited to a private network due to the confidential nature.

* This is at least until zero-knowledge proof technology that allows for total privacy on a public blockchain is further developed to scale.

* This separation of state and money is a first in history. It is similar to the separation of church and state to allow for religious freedom; only this allows for monetary freedom.

* Explain how these systems are built by the people, for the people, and are governed by the people.

Ask the students to compare the 5 Pillars to the features that they had written down during their use case analysis and to compare and contrast what they came up with to what they just learned.

Answer any questions before moving on.

---

### 7. Student Do: Peoplechain (15 min)

For this activity, students will emulate the public, censor resistant, and borderless nature of the blockchain by creating a distributed ledger like system breaking up into groups and using themselves as network participants.

#### Activity Logistics

You will need to group students into at least three groups:

* Group 1 - Money senders. This group will create and send transactions.

* Group 2 - Record Keepers in the US. This group will be a geographical region of "nodes" in the US.

* Group 3 - Record Keepers outside the US. This group will be a second geographical region of "nodes" in a different country than the US.

To speed up this activity, organize the three groups before class and let students know which group they belong to by creating some slides or a document to show in the projector during the activity.

You should create at least two slack channels for this activity, name the channels as follows:

* RecordKeepersUS

* RecordKeepersChina (China is just an example, feel free to choose another country)

Add students to their corresponding slack channel before class.

Run a couple of test transactions after starting the activity. Time the students and allow them to transact for at least 5 minutes.

Have TAs circulate to provide assistance to students facing challenges or to clarify the role of each student.

**Instructions:**

* [README.md](Activities/07-Stu_Peoplechain/README.md)

---

### 8. Instructor Do: Peoplechain Review (10 min)

Ask every group to make a list of all the transactions they have a record of in order of highest dollar amount to lowest dollar amount.

Ask each group to slack their list to you.

Show the two different lists on the board. They should be the same, if they aren’t, ask: why aren’t these the same?

Did someone miss a transaction? In this case, keep in mind this is why we have computers do it for us.

Did someone lie about a transaction? In this case, it’s easy to tell because we have so many records of the transaction.

Ask the students a few questions about the activity:

* If one person lied about a transaction, would it be easy to tell?

 **Answer**: Sure, you could double-check with another one of the many records of the transaction.

 **Answer**: In reality, there are cryptographic features that will also prevent this.

* What would you do if you discovered a record keeper was lying, or not responding?

 **Answer** Take note and stop communicating with them.

 **Answer** You might even tell others that they lied.

* What are the ways this system is making lying harder to do?

 **Answer** Since the ledger is everywhere, and transactions are broadcasted to everyone, it is difficult to lie.

* Theoretically, all the students in each country could be connected.

* In our example, we just had one “internet connection” between the Slackers for each country.

Ask the students to ponder the following (no answer required):

* So, given the possibility of all these connections, what if one entire region had a different list of transactions?

 **Answer** You would have a consensus problem -- we’ll discuss how to manage this with consensus algorithms in a later lesson.

Answer any questions before moving on.

---

### 9. Student Do: Basic Terminology (10 min)

For this activity, students will Google common terminology used in blockchain development.

Have the TAs circulate through the class and clarify definitions for students that are confused.

**Instructions:**

* [README.md](Activities/09-Stu_Basic_Terminology/README.md)

### 10. Instructor Do: Basic Terminology Review (10 min)

Students will learn basic, common terminology that will enable them to navigate the blockchain space.

* **Files:**

 * [Lesson Slides]()

Navigate to the slides and define common terms:

#### Hash

![screenshot of hash](https://image.shutterstock.com/image-photo/man-turning-cryptography-switch-change-600w-1038745234.jpg)

* Explain that a "hash" is a unique fingerprint of a piece of data.

* A hash function is one-way, which means that you cannot reverse a hash much like you can't reverse mixing paint.

* There are several popular hashing algorithms, SHA256 being one of the most popular.

* However, it is easy to run the hash function over the same data again to verify the result is the same.

* If you were to change a single bit of the input, you would get a completely different hash. This allows for something called "data integrity" which is a very important part of the internet and data security as well as blockchain technology.

#### Digital Signature

![screenshot of signature](https://image.shutterstock.com/image-vector/businessman-hands-signing-digital-signature-600w-351292748.jpg)

* Digital signatures are used to prove ownership or authenticity of data mathematically.

* Once a file or message is signed, you can verify a specific individual signed it.

* If the signed message is modified, the signature will be invalidated.

* This means that if you were to sign a document, and the document was later modified, the signature would invalidate. You could then easily prove that the document was modified. This is not just used for documents but secure internet communication as well.

Ask the students, "If a signed message is modified, what happens?"

* **Answer** The message will be invalidated, and you would know the message was modified

#### Crypto Wallet

![screenshot of wallet](https://image.shutterstock.com/image-illustration/digital-wallet-concept-3d-rendering-600w-487340401.jpg)

* A digital wallet is simply a set of "keys" to your funds that are on the blockchain.

* This means that with a wallet, you can create and send transactions, as well as view your balance.

* You can also sign messages with your digital wallet to prove ownership or authenticity of something.

* A digital wallet is much like the debit cards in your wallet, and you use them to access funds in your account. Only in this case, the card is now a key, and the bank is now the blockchain.

At this point, students should be curious about what a transaction is in the context of blockchain, continue with the slides, and highlight the following:

![screenshot of transaction](https://image.shutterstock.com/image-photo/finger-pressing-block-chain-text-600w-1026226699.jpg)

* A transaction is simply a signed message that authorizes a movement of funds between two parties.

* It is essentially "I sign off on the movement of X amount of value from account A to account B" -- now that it is signed off, nobody can modify it.

#### Blockchain Node

![screenshot of node](https://image.shutterstock.com/image-vector/abstract-scheme-modern-computer-network-600w-155306969.jpg)

* A full node keeps a copy of the blockchain. It verifies the signature of every transaction and throws out any that do not validate.

* If you wanted to send a transaction, you would send it to a node to keep track of. Nodes broadcast the transaction to their neighbors until a miner comes along and finalizes the transactions.

* Nodes are enforcing **all** of the rules of the blockchain. Thus they are a very important part of the security of the network.

#### Miner or Block Producer

![screenshot of miner](https://image.shutterstock.com/image-illustration/design-element-3d-illustration-rendering-600w-1167357031.jpg)

* A miner/block producer is a special type of node that is working to solve computations to finalize transactions.

* Miners take the pending transactions from the nodes they are connected to and put them into a block.

* Each miner races against each other to perform this process first, and the winner is rewarded by the network for its work. Then this race happens again and again for each new block in the chain.

Reassure the students that we will dive deeper into the mechanisms in which nodes and miners communicate with each other, as well as the full life cycle of a transaction from creation to being stored in a block.

After the break, students will learn how to use a cryptocurrency wallet using [MyCrypto Desktop App](https://download.mycrypto.com/), ask the class if everyone has installed the app if some students don't, ask them to reach you or TAs during the break to install it.

Answer any questions before moving on.

---

### 11. BREAK (15 min)

---

### 12. Everyone Do: Using a Wallet (15 min)

In this activity, students will learn how a cryptocurrency wallet works using [MyCrypto Desktop App](https://download.mycrypto.com/); students will be requesting `testnet` tokens and sending transactions to their fellow students.

Explain to the students that this activity is a collaborative demo where you are going to show them how to create a crypto wallet using MyCrypto App.

You will lead the activity, and the students should follow you along the process, be sure to keep the pace of the activity and ask your TAs to assist those students that may be stuck.

Open the MyCrypto App, and follow the next steps along with the demo.

1. On the left menu, click on "Create New Wallet", next on the right-side panel click on "Generate a Wallet" under the "Create New Wallet Section."

 ![Create wallet](Images/create.png)

 Explain to students, that we are going to use this option since we are going to make transactions with test Ethereum tokens, this is the best option for testing proposes and it has no cost; students shouldn't be worried about the warning message in red letters that states that this option is "Commonly a target for phishing or hacking".

2. In the "Create New Wallet" screen, scroll down to the "Mnemonic Phrase" option and click on the "Generate a Mnemonic Phrase" button.

 ![Create nmemonic](Images/mnemonic.gif)

3. MyCrypto will generate a unique mnemonic phrase for you, write down this phrase **in order** and store it in a safe place. Do not share this phrase with anyone, treat it like your banking password. Note that the mnemonic phrase bellow is just a sample and will differ in your demo.

 ![Confirm mnemonic](Images/mnemonic.png)

 After writing down this phrase, click on the "Confirm Phrase" button to continue.

4. In the next screen, you will need to confirm the phrase by clicking your words in order. Click on the "Confirm Phrase" button after clicking on the words in order.

 ![Confirm mnemonic step 2](Images/mnemonic_confirm.gif)

5. In the next screen, you will see the steps you will need to unlock your account in the future.

 ![Unlock wallet steps](Images/MyCryptop-Unlock-Steps.png)

At this point, you have created your wallet; now, you need to unlock it to start making transactions.

6. Unlock your wallet by going to the "View & Send" option in the left pane menu and pick the "Mnemonic Phrase" option.

 ![Unlock wallet step 1](Images/unlock-1.png)

7. Type your mnemonic phrase, separated by spaces (you can click the eye to view it), then continue by clicking the "Choose Address" button.

 ![Unlock wallet step 2](Images/unlock-2.png)

8. In the next screen, you will choose a test Ethereum address to unlock. Be sure that the `Testnet(ETH)` option is selected in the "Addresses" dropdown list, select the first available address and click on the "Unlock" button to continue.

 ![Unlock wallet step 3](Images/unlock-3.png)

 The address you unlocked is the address of your cryptocurrency wallet for the Ethereum network.

9. Once you unlocked the address, it's time to make your first transaction. In the next screen, you can see the balance of your wallet, `0 ETH` right now, and the account address. Copy the address by clicking on the "copy address" option to continue.

 ![Unlock wallet step 4](Images/unlock-4.png)

10. At the bottom left of the app, click on "Change network" and select `kovan`. Note that if `kovan` was not selected when you change the network, you should unlock your wallet address again by following steps `6` to `8`.

 ![Change network](Images/change_network_kovan.gif)

Explain to students that, to test a blockchain, there are testing networks (aka `testnets`) that contain a group of testing addresses for development proposes. In the case of Ethereum, the most commonly used testnets are `kovan` and `ropsten`. We will use `kovan` for this demo since it's faster on delivering testing tokens than `ropsten`.

11. Now you are going to request a test Ethereum token from the `kovan` network, and it's going to be transferred to your wallet. Open your browser, and navigate to the testnet token faucet at [https://faucet.kovan.network/](https://faucet.kovan.network/). Once you open the page, click on the "Login with Github" button to continue.

 ![Request ETH -1 ](Images/request-eth-1.png)

Explain to students that the faucet is a means of providing test tokens to users so that they can run their smart contracts on the test networks.

* For this demo, the faucet will allow us to request Kovan Ether (KETH) to be used on Kovan Ethereum test network.

12. After login into the faucet, you will see the following form where you can request one Kovan Ether every 24 hours. Paste the wallet address into the `Kovan address` box and click on the "Send me KETH!" button to continue.

 ![Request ETH -2 ](Images/request-eth-2.png)

13. Once you request the testing KETH token, you will see the following screen that confirms that the transaction was successfully completed.

 ![Request ETH -3 ](Images/request-eth-3.png)

14. You can view the transaction status on `Etherscan` using the link provided.

 ![Request ETH -4 ](Images/request-eth-4.png)

Explain to students that `Etherscan` is a visual BlockExplorer for the Ethereum Blockchain. A BlockExplorer is a search engine that allows users to easily lookup, confirm, and validate transactions that have taken place on the Ethereum Blockchain.

15. Once you confirmed that the transaction was successful, go back to MyCrypto App and refresh your wallet balance by clicking on the refresh icon. Note that now you have one ETH in your wallet, remember that this is not real ETH, it's a testing token for development proposes with no monetary value.

 ![Request ETH -4 ](Images/request-eth-5.gif)

16. Now it's time to make transactions. Slack out your wallet address to a couple of students and have them send theirs.

17. Using MyCrypto, send some transactions to the students. Paste the destination address in the "To Address" box, define an amount to transfer (e.g., `0.02 ETH`), set the transaction fee (you can leave the default value), and click on the "Send Transaction" button to finish. After finishing the transaction, refresh your account balance to reflect the new amount after the transaction.

 ![ETH Transaction](Images/eth-transaction-1.gif)

Explain to students that as they can see in the message that appears after the transaction, it's not an immediate operation; after a transaction is sent, it's mined and confirm in a process that could take three or more hours. You can check the status of the transaction on `Etherscan` using the links provided after the transaction.

Inform the students:

* These test tokens are provided by faucets run by developers just like us, so when we're done with our test tokens, it is polite
  to send them back to the faucet. Otherwise, if we simply discarded our wallets that had test Ether in them, those developers have to
  put more effort into keeping the faucet funded and create new test tokens. This applies for all test blockchain networks as well!

If you encounter any issues with requesting KETH from the Kovan faucet, the following mnemonic phrase has been pre-funded with test tokens (**for instructors only!**):

`use trouble sponsor panda camp grow pact matrix chief black napkin ghost`

If you end up needing to use this wallet, simply import it into MyCrypto, change to the Kovan network, then distribute the KETH to the class and yourself.
Since you can work with very small amounts of Ether, you should have plenty of KETH to work with. Sending `0.1` at a time should suffice.
Make a note to help refill this later for other instructors once the Kovan faucet is back up and running.

Some students may encounter a [rare bug](https://github.com/MyCryptoHQ/MyCrypto/issues/2197) in MyCrypto where duplicate words in their mnemonic phrase causes the confirmation page to "get stuck" after selecting one of the duplicate words. If this occurs, simply have the student restart the "Create a New Wallet" process and generate a new mnemonic.

Answer any questions before moving on.

---

### 13. Instructor Do: Block Explorers Demo (10 minutes)

The goal of this demo is to show the students how block explorers can be used to visualize transactions on the blockchain.

Explain to students that now you are going to explore the transaction history of the wallet. Open your wallet in MyCrypto and click in the link under the "Transaction History" section.

![BlockExplorer - 1](Images/etherscan-1.png)

Comment to students that the web browser will open the `Etherscan` BlockExplorer with the transactions history of your wallet, and highlight the following:

 ![BlockExplorer - 2](Images/etherscan-2.png)

* The balance field reflects that this wallet is part of the public nature of blockchains; some blockchains have this field hidden, like `Zcash` or `Monero`.

* The list of transactions keeps track of all the movements of this account has made, it can be seen that every transaction has a "Transaction Hash" column on the very left.

Click on the transaction hash for the first transaction, and ask the students what they think a transaction hash might be, and what it might be used for.

* **Answer**: The transaction hash is used as the unique ID of the transaction to find it later.

![BlockExplorer - 3](Images/etherscan-3.gif)

Go back to the initial address page, then click on the "Block Number" section of the first transaction.

![BlockExplorer - 4](Images/etherscan-4.gif)

Point out the fields "Mined By" and "Block Reward" and explain that this is the address of the miner that successfully created this block and received that amount of Ether as a reward.

Continue the demo by clicking on the "Transactions" option to view which transactions were mined in that block.

![BlockExplorer - 5](Images/etherscan-5.png)

Explain to students that these are the transactions that were mined in this particular block.

![BlockExplorer - 6](Images/etherscan-6.png)

Answer any questions before moving on.

---

### 14. Student Do: Visualizing Transactions (10 min)

For this activity, students will visualize transactions using the same technique used in the demo.

Students will get into small groups and will explore the blockchain using Etherscan together.

Have TAs circulate to provide assistance to students facing challenges or to clarify the role of each student.

**Instructions:**

* [README.md](Activities/14-Stu_Visualizing_Transactions/README.md)

---

### 15. Instructor Do: Visualizing Transactions Review (5 min)

Review the groups and ensure that students can navigate and visualize transactions.

Recap by asking the students to answer these questions:

* "What is a transaction hash?"

 * **Answer:** It's an identifier used to identify a particular transaction uniquely.

* "What type of information is available to you on a public blockchain's block explorer?"

 * **Answer:** Practically everything, balances, transaction history, data stored on-chain, etc.

* "Is this a fully anonymous blockchain?"

 * **Answer:** No, the current version of the public Ethereum network is pseudonymous, not fully anonymous yet.

Explain to the class that while the current version of Ethereum is pseudonymous, future updates will bring a technology called "Zero-Knowledge Proofs" that will enable completely private transactions on a public network.

* This means that the balances and transaction history between accounts will be encrypted in a way that allows for verification without exposing potentially sensitive information.

* This allows for private, enterprise applications to run on open blockchains!

* This means that in the future, transactions will be private, and you will only be able to view transactions that you are a part of.

* There are currently public blockchains, like `Zcash`, that implement this now by default, so be on the lookout for zero-knowledge protocols in future blockchain upgrades.

Answer any questions before moving on.

---

### 16. Instructor Do: Intro to Ethereum (10 min)

Open the lesson slides, move to the "Intro to Ethereum" section, and ask the students the following question:

* What would it be like to be able to code with money, like this?

 ```python
 amount = $10 dollars
 recipient = "JaneDoe123"
 wallet.send_transaction(amount, recipient)
 ```

Explain to students that's what Ethereum brings to the table, just replace a couple fields:

```python
amount = 0.05 Ether
recipient = "0xc3879B456DAA348a16B6524CBC558d2CC984722c"
wallet.send_transaction(amount, recipient)
```

Comment to students that, despite this is pseudocode, it should get the point across. Continue through the lesson slides and highlight the following.

* Ethereum secures over $20 billion US Dollars in assets without a central authority. It powers a huge ecosystem of decentralized applications and financial ecosystems.

* First generation blockchains were much like the days of carrying a cell phone, iPod, and calculator with you. Each solved a specific problem.

* Ethereum brought to blockchains what the iPhone brought to personal computing, a general-purpose platform where apps take the place of separate devices.

* Now, you can build fully-fledged applications, called "Smart Contracts" on top of the blockchain with Ethereum.

* You can think of Ethereum like the inverse of AWS Lambda. With Lambda, you upload your code to Amazon and pay per use.

* Amazon, in this case, is the central party, they control the computing. Whereas in Ethereum, every person who helps run Ethereum becomes part of the "global computer", and you pay the network itself to run your code instead of a single party.

Ask the students the following question:

* "What are some benefits you can think of to having compute power distributed in such a way?"

 * **Answer:** No bottlenecks in the system, since the world helps run the code

 * **Answer:** Highly reliable systems that will run regardless of if some servers go down

If students are unclear as to how this works, reassure them that they will be learning the inner workings when they begin Smart Contracts in Unit 20.

* The most significant point to get across is that everyone shares computing power to create a platform that anyone can upload and run code on top of.

Now, transition to talk about the types of financial services that you can build with Ethereum:

* Payments - Peer to Peer, Business to Business, Business to Customer, Machine to Machine

* Remittances – Movement of funds across borders into a bank account.

* Loans – Using crypto-currency as collateral for loans to reduce costs of transactions.

* Deposit-taking – Storing crypto in wallets to use as interest-earning assets.

* Notary services – Blockchain-based notary services that authenticate documents.

* Brokerage services – Trading tokens and other digital assets on the Blockchain.

* Foreign exchange – Using crypto as a bridge between fiat/government currencies to reduce the cost of foreign currency fees.

* Decentralized crypto exchange - Using the blockchain as a backend to support a crypto-trading exchange.

* Tokenizing assets - Representing things from the US Dollar, Gold, Securities, to unique video game assets an on the blockchain.

Answer any questions before moving on.

---

### 17. Student Do: Use Case Brainstorm (10 min)

Now that the students have learned about the features of Ethereum and how it acts as a decentralized world computer, it is an excellent time to brainstorm different use cases given these features.

Students will get into groups and come up with different decentralized application ideas, as well as discuss gaps they may be familiar with.

Have TAs circulate throughout the class, facilitating discussion and ensuring students are not lost.

**Instructions:**

* [README.md](Activities/15-Stu_Use_Case_Brainstorm/README.md)

---

### 18. Instructor Do: Use Case Review (10 min)

Ask different groups what their most exciting use case was and have them describe them to the class.

Facilitate the discussion toward the benefits of decentralizing specific applications.

* What are the main benefits of decentralizing your application?

 * **Answer:** The application can only go down if the entire Ethereum network goes down.

 * **Answer:** The application can run without a central server.

 * **Answer:** The application could potentially live forever (as long as Ethereum exists).

 * **Answer:** The application is pay-per-use, much like a decentralized AWS Lambda.

* If the students chose a game-based use case, ask what type of assets they have represented?

* Is there a limit to what you can build with Ethereum's Turing complete smart contracts?

 * **Answer:** No, in theory, you could build any application just as you would with any other general-purpose programming language.

Reinforce the idea that Ethereum's smart contracts are just programs that run on a distributed, decentralized computer.

Explain to students that anyone can upload and pay to run code in a secure sandboxed computer environment, allowing for a safer, immutable web, and for building powerful financial applications.

Answer any questions before moving on.

---

### 19. Instructor Do: Recap (5 min)

Students have learned tons of new information today. Facilitate a discussion around the different ideas that were spoken about during the class, and what questions students may be asking the most.

* What types of blockchain applications excite you the most?

* What types of financial services can blockchains improve?

 * **Answer:** Practically any that currently requires unnecessary middlemen.

* How does blockchain technology improve the lives of people around the world?

 * **Answer:** It provides robust financial platforms that don't always exist, or are not trustworthy.

 * **Answer:** It supports borderless, neutral, and censor resistant finance that cannot be oppressed easily.

---

### End Class

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
