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

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome Class (5 min)

**Files:**

* [welcome-slides]()

Welcome students back refresh a bit on the data structure of a blockchain.

Ask the students the following questions:

* What does the "chain" in blockchain refer to?

  **Answer** The chain of hashes that link each block to the previous.

* What is a digital signature?

  **Answer** A message that you can validate the integrity and authenticity of cryptographically.

* What is a node?

  **Answer** A node is a participant in the network that maintains a full copy of the blockchain.

Explain to the students that today they will be building a real, functioning blockchain from scratch, so get excited!
