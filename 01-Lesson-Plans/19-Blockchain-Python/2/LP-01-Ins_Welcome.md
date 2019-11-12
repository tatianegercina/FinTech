## 19.2 Lesson Plan: Bit, A Python Library

### Overview

Today's class students will begin to interact with blockchains using Python libraries `web3.py`, `bit`,
and will also learn how BIP44 works in preparation for the homework.

The goal of today's class is for the students to understand how to talk to Ethereum and Bitcoin nodes using Python,
and to understand how wallets work across the blockchain ecosystem.

### Class Objectives

By the end of the unit, students will be able to:

* Define Unspent Transaction Output (UTXO) (data structure behind Bitcoin-based projects).

* Explain the how UTXOs in Bitcoin transactions allow for multi-input and multi-output transactions.

* Send Bitcoin transactions on bitcoin’s test network.

* Explain the difference between Ethereum and Bitcoin's account models (UTXOs vs Nonces).

- - -

### Instructor Notes

* Before class, ensure that you have funded a Bitcoin testnet wallet using the same mnemonic you've been using throughout the course.
  You may need to send out test bitcoins to students that did not successfully request them from a faucet previously.

* If you can prefund multiple testnet addresses by splitting up what the faucet sends you into multiple addresses,
  you can use these to distribute to students as prefunded private keys if absolutely necessary to keep the class moving
  (for instance, the transaction doesn't confirm between the beginning of class and after the break).

* Use an offline version of the [BIP39 Conversion tool](https://github.com/iancoleman/bip39/releases) to derive your BTC testnet address if necessary.

* Ensure that you have the `bit` Python library install via `pip install bit`.

- - -

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

Welcome students back and refresh a bit on some blockchain architecture.

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Ask the students the following questions:

* What is Ethereum?

  **Answer**: A global computer powered by blockchain technology.

* Why is Ethereum important?

  **Answer**: It makes a decentralized computing and money system available to everyone, powered by everyone.

* Now let's take this back a bit, what was the first blockchain?

  **Answer**: Bitcoin!

Today we're going to talk about the differences in the architectures of Bitcoin and bitcoin-based blockchains versus
Ethereum-based blockchains.

* Can anyone describe a couple differences between Bitcoin and Ethereum?

  **Answer**: Ethereum is "Turing complete" meaning it is capable of general computing.

  **Answer**: Bitcoin supports multiple inputs and outputs in transactions (more on this in a bit).

  **Answer**: Ethereum uses nonces to count transactions sent from an account.

  **Answer**: Ethereum uses a single account system, Bitcoin uses a UTXO system (more on this in a bit).

  **Answer**: Bitcoin supports multisig natively versus needing more complex and expensive smart contracts (more on this later today).

Reassure the students that we will go into detail about the pros and cons of Bitcoin versus Ethereum,
and the pros and cons between the architectures.

### 2. Instructor Do: Architecture Overview (5 min)

Now, let's give a quick comparison between the architectures. Navigate through the slides to help illustrate your points.

Ask the students:

* If Ethereum exists, why is Bitcoin still the number one crypto?

Have the students ponder for a bit, have some students give their ideas.

Then explain:

* Even though Ethereum is quite a bit more capable functionally than Bitcoin, architectures designed for general computing
  are more expensive to use.

* Bitcoin's architecture (and thus, all of its derivatives) is designed for complex payments on the natively
  core layer of the blockchain, and can get them done for less computational effort than Ethereum.

* In the case of Ethereum, you'd have to write smart contracts to do many of types of transactions that Bitcoin can do natively,
  which can end up costing more gas/computational effort.

* Ethereum very well may take over as the main cross-border payments network, but for now, Bitcoin is still the leader in the space.

Ask the students:

* Why might we want to learn about Bitcoin and its architecture?

  **Answer**: Bitcoin's payment system is designed for complex transactions, natively.

  **Answer**: We won't have to write smart contracts for many types of payments.

  **Answer**: It is the number one cross-border cryptocurrency, and is still being upgraded.

  **Answer**: There may not be "one chain to rule them all." A payment-focused network can co-exist with a computing-focused network.

Now, let's start learning why Bitcoin is still a top player, and why it might stay that way for longer than you'd think.
