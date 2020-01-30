# 22.3 Lesson Plan:

### Overview

In today's class, students will be introduced to auction contracts. Students will create an ERC721 token that leverages their created auction contracts in an internal mapping structure to facilitate the sale of `Auctionable Non-Fungible Martian Land Tokens`.

### Class Objectives

By the end of the unit, students will be able to:

* Modify and Deploy an Auction contract written in Solidity

* Use the .value function to pass Ether from one function to another in Solidity, and understand the difference between .value, .call.value, .send, and .transfer

* Create an ERC721 token that leverages the Auction contracts in an internal mapping structure to create "Auctionable Non-Fungible Martian Land Tokens

* Create a landing page that points to the Martian Land ERC721 dApp

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1devzesQ1UKT2weYAz43Ei9YBIM863dYDtw9IFIMfLis/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/presentation/d/1_BDSSZoS2qRvOOAZJvW0dtQVaJfvhtqYzjunIsDO02o/edit ).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

### Instructor Notes

* Refer to the [solidity documentation for open auction](https://solidity.readthedocs.io/en/v0.5.11/solidity-by-example.html#blind-auction)

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome to Class (10 min)

During the previous lecture, students were introduced to the thought process and techniques that go into taking a formalized contract spec and implementing it into solidity code.  Students learned to take a simple yet formalized smart contract specification and implement it to fit the interface of an already established frontend dApp. Students then deployed the configured dApp to a centralized production environment, Github pages.

Today students will once again be leveraging the Github Pages service to host their static dApp bundle.

Review the following recall questions with the class.

* What are some benefits of using Github pages?

* **Answer** Quick and Easy Deployments.

* **Answer** Free Static Web Hosting

* **Answer** Free-SSL

* **Answer** Integrated Version Control(GIT)

* Why is having a documented/formalized API for your applications and libraries important?

* **Answer** Good documentation is always important.

* **Answer** Helps set forth standards from and for your given implementation. (like `EIPS` and `ERCS`)

* **Answer** So that others can build off of your application.

* Having written many smart contracts, and now deployed a dApp. What are some contracts that you believe could be leveraged within a dApp?

* **Potential Answer** A contract that tracks the immutable locations of historical landmarks.

* **Potential Answer** A contract that transfers tokens between two users within a decentralized product swapping website.

* **Potential Answer** Maintain an immutable achievement list of users' achievements within an online course dApp.

* **Potential Answer** Any other dApp or smart contract that you can think of; the Ethereum blockchain is a globally distributed datastore and supports a fully Turing complete programing language.
