## 20.3 Lesson Plan: Solidity Continued

### Overview

Today's class will dive into more complex Solidity concepts, such as `mapping`s, globally available units and attributes,
and how to tell time in the Ethereum blockchain.

### Class Objectives

By the end of the class, students will be able to:

* Use `uint` and `int` Number types in Solidity and explain when to use each.

* Use global variables to tell the current block number, transaction sender, and transaction value.

* Work with time in Solidity and use time variables to create a Timelock.

* Recognize that telling time in Solidity has variability relative to the network's block production time, and static compared to Gregorian calendar time.

* Add conditions to the withdraw function to trigger the Timelock from a set threshold.

* Create a contract constructor in Solidity to allow reuse of the contract by preventing hardcoded values.

* Deploy and interact with contracts (Remix + Ganache).

### Instructor Notes

* @TODO

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 min)

* **Files:**

 * [Lesson Slides]()

Welcome students to the class by getting them excited about more advanced Solidity concepts!

* Today we are going to be learning how to work with time in Solidity, how to add a timelock to our contract,
  and how to make our contracts reusable with constructors!

Have the students open up [Remix](https://remix.ethereum.org) and open up the `JointSavings.sol` contract from last class.

---

### 2. Instructor Do: Static Typing Refresher (10 min)

First, let's ask the students some recall questions about static data types:

* What is a `uint`?

  **Answer:** Unsigned Integer.

* What is the difference between an `int` and a `uint`?

  **Answer:** `int` can be positive and negative, `uint` is positive only.

* What is a `payable` address and why is it different from a regular address?

  **Answer:** A payable address is like a normal address type, except it allows the `.transfer` function to be called in order to send it Ether.

Ask for remaining questions before moving along.

---
