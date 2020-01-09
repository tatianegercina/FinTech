## 22.1 Lesson Plan: DeFi (Decentralized Finance)

### Overview

In today's class, students will be introduced to the concept of DeFi short for decentralized finance. Though DeFi most commonly refers to financial systems built upon distributed ledgers frequently leveraging smart contracts. Students will gain the scope that DeFi is not a particular technology or implementation but rather a movement within the financial technology sector where future financial systems are being created and deployed with an open, decentralized, and permissionless architecture.

### Class Objectives

By the end of the unit, students will be able to:

* Build non-fungible ERC721 tokens with OpenZeppelin

* Explain what events are and how they can be used to create a dApp

* Use IPFS to store immutable data off-chain to save gas

* Use Filters in Web3.py to react to Events from smart contracts

### Instructor Notes

* The contracts you will be deploying today are relatively large and may take a few minutes to compile.

* Refer to OpenZeppelin ERC721 documentation for further information about Non-Fungible Tokens. [ERC721 Docs](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721)

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome Back (10 min)

Previously students have implemented both a basic token as well as the ERC21 fungible token standard using the OpenZeppelin libraries. Today they will be implementing their first ERC721 Non-fungible token using the Openzeppelin libraries. Take a few minutes to review ERC's, OpenZeppelin and the concept of fungibility by discussing the following recall questions with the class.

* What are some differences between `fungible` and `non-fungible` tokens?

* **Answer** Non-fungible tokens are unique, fungible tokens are not unique.

* **Answer** Fungible tokens are interchangeable with one another whereas non-fungible are not.

* **Answer** Non-fungible tokens use ERC 721, fungible tokens use ERC 777.

* What are some examples of `fungible` assets?

* **Answer** United States Dollars (USD)

* **Answer** Ethereum (ETH)

* **Answer** Bitcoin (BTC)

* **Answer** Gold

* What are some examples of `non-fungible` assets?

* **Answer** Art

* **Answer** Diamonds

* **Answer** Land Ownership

* What are some potential benefits of using open source libraries such as OpenZeppelin?

* **Answer** They are freely available to use and contribute to under the MIT license.

* **Answer** It's a community-backed project that has implemented many of the communities agreed-upon standards (EIPS/ERCS).

* **Answer** It provides a secure, standardized starting point for various smart contract standards.

Now that the class has been refreshed on fungibility, set the stage for today's lesson by introducing the concept of `DeFi`.

* `DeFi` is short for decentralized finance.

* `DeFi` encompasses many of the technologies and paradigms that we have learned throughout the previous unit, however, defi is not a particular technology or implementation.

* `DeFi` is a movement within the financial technology sector where future financial systems are being created and deployed with an open, decentralized, and permissionless architecture.
