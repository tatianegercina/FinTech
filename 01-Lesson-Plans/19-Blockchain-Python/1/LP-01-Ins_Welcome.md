## 19.1 Lesson Plan: Intro to Web3.py

### Overview

Today's class students will begin to interact with blockchains using Python libraries `web3.py`, `bit`,
and will also learn how BIP44 works in preparation for the homework.

The goal of today's class is for the students to understand how to talk to Ethereum and Bitcoin nodes using Python,
and to understand how wallets work across the blockchain ecosystem.

### Class Objectives

By the end of the unit, students will be able to:

* Explain the role of web3 in communicating with Ethereum nodes.

* Activate their Ethereum network (using cheat sheet).

* Use web3 to fetch data.

* Import a private key into web3.

* Use web3 to send transactions on their own Ethereum blockchain.

* Request testnet tokens from Bitcoin.

- - -

### Instructor Notes

* Before class, prepare to use the mnemonic phrase you have been using throughout the course, we will
  be extracting keys and addresses from it.

* Ensure that an ETH address from this mnemonic is prefunded in your custom chain.

- - -

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Welcome students back refresh a bit on some blockchain architecture.

Ask the students the following questions:

* What is a keypair?

  **Answer**: A set of public and private keys used in asymmetric encryption.

* What is a digital signature?

  **Answer**: A cryptographic technique used to ensure the integrity and authority of data.

* What is a transaction in the context of blockchain?

  **Answer**: A signed message that authorizes the transfer of funds from one account to another.

Explain that today we are going to be talking to blockchains in our favorite language, Python.

Ask the class:

* What Python library might we use to talk to Ethereum nodes?

  **Answer**: web3.py

Time to get excited, let's dive into working with Web3.
