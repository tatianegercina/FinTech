# 21.3 Lesson Plan: Writing Secure Contracts with OpenZeppelin

### Overview

In the last class students were introduced to several of the popular ERC token standards (20, 721, 777, 1155) and implemented their own ERC20 compliant token using the OpenZeppelin libraries. Today students will be introduced to the concept of crowdsales, a popular method for distributing tokens; they will explore popular historic crowdsales and implement their own crowdsale using the OpenZeppelin libraries.

### Class Objectives

By the end of the unit, students will be able to:

* Articulate different types of crowdsales and how Ethereum/blockchain makes them much easier and auditable.

* Prepare an ERC777Mintable token for Crowdsale

* Build a crowdsale that distributes an ERC777Mintable token.

* Design contracts to avoid common security pitfalls, such as a re-entrancy attack.

* Perform a Mythril security scan on contracts to test for simple security vulnerabilities.

### 1. Instructor Do: Welcome to Class (10 min)

Refresh the students on ERC standards and set the stage for todays class by briefly discussing the topic of token distribution.

Review the following recall questions with the class.

* What are some examples of ERC standards?

* **Answer** Fungible tokens

* **Answer** Non-fungible tokens

* **Answer** Token exchange standards

* **Answer** Ethereum Domain Name Service

* **Answer** Multi Token Standard
* What are some benefits of ERC standards?

* **Answer** Provides a way to submit new standards within the community.

* **Answer** Allows the community to agree on a current standard for a feature.

* **Answer** Helps prevent bugs and security vulnerabilities by creating a specification for implementing certain types of smart contracts.

* What are some of the stages that an ERC goes through before being accepted by the community.

* **Answer**  WIP

* **Answer**  DRAFT

* **Answer** LAST CALL

* **Answer** FINAL

* What are some differences between `fungible` and `non-fungible` tokens?

* **Answer** Non-fungible tokens are unique, fungible tokens are not unique.

* **Answer** Fungible tokens are interchangeable with one another whereas non-fungible are not.

* **Answer** Non-fungible tokens use ERC 721, fungible tokens use ERC 777.
