## 20.2 Lesson Plan: Intro to Solidity

### Overview

Today's class will introduce the Solidity programming language to the class. Solidity is the de-facto smart contract
programming language that is compatible with many blockchains, including Ethereum.

The goal of today is to familiarize the students with the strictly typed language features of Solidity enough to build
a Joint Savings Account smart contract that can store and withdraw Ether.

### Class Objectives

By the end of the class, students will be able to:

* Explain the reason Solidity uses static typing is to increase efficiency and decrease cost.

* Store basic datatypes such as boolean, string, int, and address in Solidity.

* Create a basic smart contract in Solidity.

* Create getters and setters in Solidity including return type.

* Create basic functions in Solidity
  (in this case, a `deposit` function to add Ether, a `withdraw` function to withdraw Ether, and a `fallback` function to capture Ether).

* Utilize the built-in `payable` modifier in Solidity to give addresses or functions the ability to accept Ether.

* Use basic conditionals (if/else) in Solidity.

* Enforce conditionals using the built-in `require` clause in Solidity.

* "Articulate the value of adding the `require` function and how it enables better error handling and returns excess gas.

* Deploy and test a smart contract with Remix + Ganache.

### Instructor Notes

* This is the first time students have encountered a strictly typed programming language. This is going to be a very difficult
  adjustment for the students to make, since they are going to have to remember to specify the data types everywhere, as well as use semicolons to end expressions.

* Remind the students that if they get frustrated, they are learning something that few are skilled at, and by learning
  a strictly typed language now, they will be able to easily learn any other programming language in the future.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome to Class (5 min)

Welcome to Day 2 of Intro to Solidity. Let's start by reviewing some of the concepts that we talked about yesterday and expanding on them a little bit.

* What is Solidity?

  **Answer** Solidity is a high level object oriented programing language. It is the language used to write smart contracts on the Ethereum blockchain.

* What is a smart contract?

  **Answer** A smart contract is essentially just a program that runs on the global computer that is the Ethereum blockchain.

* What is a dApp (Distributed App)?

  **Answer** A dApp is an application stack that leverages one or many smart contracts on the Ethereum blockchain.
* Why are dApps important?

  **Answer:** Instead of relying on centralized infrastructure to run applications, which are prone to censorship and access
  issues, you can write apps that are secured and powered by the blockchain and pay the world to run your application instead of
  a single, fallable entity.

  **Answer:** It is a way of writing applications that require the 5 pillars of open blockchain

* What are the 5 Pillars of Open Blockchains?

  **Answer:** Open, Borderless (Decentralized), Neutral, Censor Resistant, Public

* Why might we be learning Solidity compared to any other programming language?

  **Answer:** We are in an age where blockchain technologies are beginning to shape the world around us in new and exciting ways.
  Learning Solidity will allow us to build complex decentralized applications that plug directly into Ethereum.

  **Answer:** Solidity is quickly becoming the de-facto standard for digital smart contracts, and is supported in multiple blockchains, including
  Ethereum, Ethereum Classic, Hyperledger Fabric, Quorum, and more.

Let's get the class excited about smart contracts.

* Now that we've reviewed a bit and introduced some interesting concepts, let's begin some coding practice.
  In the first half of class today we will translate some of the core coding concepts you have learned to a new language, Solidity, and create your first "smart contract".
