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

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

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
