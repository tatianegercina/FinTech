## 21.1 Lesson Plan: Advanced Solidity

### Overview

In today's class, students will be introduced to the concept of tokens on the Ethereum blockchain.

Students will learn more advanced Solidity data structures, what tokens are, and how to use them.

### Class Objectives

By the end of the unit, students will be able to:

* Explain what gives tokens (digital assets) value, and the different mechanisms in which tokens may be collateralized.

* Distinguish the general difference between a `coin` and a `token` in the context of crypto.

* Use the mapping data structure to associate customer addresses with their individual information.

* Build a simple token on the ETH blockchain.

* Import 3rd OpenZeppelin libraries from Github within Solidity.

* Use the SafeMath library to perform secure math operations.

* Build a simple tokenized reward system in Solidity that distributes tokens to users based on their actions.

* Design smart contracts that can replace traditional business mechanisms.

### Instructor Notes

* @TODO

### 1. Instructor Do: Welcome Back (5 min)

Take a few minutes to discuss the following recall questions with the class.

* Before we move on to new and advanced concepts in Solidity, let's review some of the basics that we already know.

  **Answer** Solidity is:

  * A high-level object-oriented programing language.

  * It is the language used to write smart contracts on the Ethereum blockchain.

  * Is strictly typed.

* What is a `uint`?

* **Answer:** Unsigned Integer.

* What is the difference between an `int` and a `uint`?

  **Answer:** `int` can be positive and negative, `uint` is positive only.

* What is a `payable` address, and why is it different from a regular address?

  **Answer:** A payable address is like a normal address type, except it allows the `.transfer` function to be called in order to send it Ether.

* What is a potential benefit of executing code in a virtual machine?

  **Answer** The code executed in a virtual machine cannot affect the host machine directly.

  **Answer** The code can run anywhere the virtual machine can run.
