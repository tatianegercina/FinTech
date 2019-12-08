# 21.2 Lesson Plan: Writing Secure Contracts with OpenZeppelin

### Overview

Previously students were introduced to the concept of tokens on the Ethereum blockchain. They learned what tokens are and how to use them. Today they will be introduced to the concept of `fungibility`, `fungible` vs `non-fungible` goods, and how this relates to tokens and the various token standards.

### Class Objectives

By the end of the unit, students will be able to:

* Explain the difference between fungible and non-fungible tokens and their use-cases.

* Explain that ERC standards are official smart contract implementations for various use cases.

* Explain which ERC token standards correspond with fungible vs non-fungible tokens

* Implement an ERC20 compatible fungible token using OpenZeppelin libraries

* Evaluate different ERC standards and determine which work for different use cases

* Leverage open, community-maintained libraries in Solidity to implement ERC standards

### Instructor Notes

* Focus on really conveying that ERC's are just standards that can be implemented a number of ways.

* Refer to the [OpenZeppenlin Documentaion](https://docs.openzeppelin.com/contracts/2.x/tokens) for additional links and examples.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome to Class (10 min)

Review tokens, and the concept of tokenomics with the class.

* What are things that can be represented by a token?

* **Answer** Property

* **Answer** Currency

* **Answer** Votes

* **Answer** Potentially any other store of value

* What are some common aspects of a `token`.

* **Answer** They have a supply which can be a fixed or infinite amount.

* **Answer** They represent some store of value.

* **Answer** They can be programed with a smart contract.

* What are some generally accepted differences between `coins` and `tokens`?

* **Answer** Tokens are commonly built on top of an existing blockchain platform, whereas coins are commonly a fundamental component of a blockchain platform.

* **Answer** Coins are typically used as just a currency for buying and selling things whereas tokens can have broader use cases.

* **Answer**  Sometimes there's no difference at all; many people within the crypto communities use the terms interchangeably.

* What are some potential benefits of tokenizing an asset on an open blockchain?

* **Answer** The asset can be traded globally without any additional infrastructure.

* **Answer** Easy transfer of ownership with improvements in liquidity and audibility.

* **Answer** Benefits of an open blockchain; open, public, borderless, censorship-resistant, and neutral.
