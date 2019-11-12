## 19.3 Lesson Plan: Wallet Standards (BIP39, BIP32, and BIP44)

### Overview

Today's class students will learn how BIP44 works in preparation for the homework.

The goal of today's class is for the students to understand how to talk to Ethereum and Bitcoin nodes using Python,
and to understand how wallets work across the blockchain ecosystem.

### Class Objectives

* By the end of the unit, students will be able to:

* Explain that BIP32 generates a tree of keys from a single "master key" 256bit seed, and why it is used (increased privacy, merchants, etc).

* Explain that BIP39 allows you to back up this master key as a set of words (mnemonic phrase).

* Explain that BIP44 allows you to use your master key with multiple coins (blockchains).

* Use `hd-wallet-derive` (BIP44 wallet) to generate BIP44 keys using their own mnemonic.

* Discuss the differences in wallet implementations and the pros and cons (cold -> hot, paper/hardware -> software).

* Integrate basic terminal output (stdout) into Python code.

- - -

### Instructor Notes

* Ensure that you have your 12 word mnemonic ready. We will be using it throughout the class.

* Take some time before class to familiarize yourself with the [BIP39 online wallet converter](https://iancoleman.io/bip39/) and how to convert your mnemonic into different coins.

* Ensure that you have properly installed the [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive#installation-and-running) PHP CLI tool at least once before class.

- - -

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

Welcome students back and refresh a bit on some blockchain wallet architecture.

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Ask the students the following questions:

* What is a UTXO?

  **Answer:** Unspent Transaction Output

* What is a private key in the context of blockchain?

  **Answer:** A key that allows you to sign transactions.

* What is a wallet?

  **Answer:** A piece of software that manages your private keys and allows you to sign and send transactions.

Explain to the class that there are two parts of a wallet.

Ask the students to make an educated guess as to what the two main parts are.

Then, explain that the two parts of a wallet is:

* **Key Manager** -- Code that takes your mnemonic or private key and converts it to the proper blockchain address format.
  This is the low-level cryptographic library.

* **Blockchain Node Connectors** -- Code that connects to the blockchains that the wallet supports.
  This is the library that connects the wallet to live blockchain nodes, where signed transactions from the key manager are sent to the network.

Remind the class that we have already worked with several wallets already, that contain both of these parts.

Ask the class to name a few, such as:

  **Answer:** MyCrypto

  **Answer:** Web3.py

  **Answer:** Bit

Elaborate:

* Notice how we have used the same 12 word mnemonic phrase across each blockchain?

* While this is incredibly useful, wouldn't it be easier to have one library that works with both Ethereum, Bitcoin, and potentially others?

* Today we will learn the wallet standards that allow us to use the same master key across multiple blockchains,
  as well as how to integrate a universal key manager tool with Web3.py and Bit using our good pal, Python.

  This will allow us to have one Python wallet that supports both of the blockchains we've learned so far, so that we no longer
  have to use separate tools to send transactions!
