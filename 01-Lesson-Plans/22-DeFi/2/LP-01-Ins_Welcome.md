## 22.1 Lesson Plan: DeFi (Decentralized Finance)

### Overview

In today's class, students will be introduced to the techniques and thought process that goes into taking a formalized contract spec and implementing it into solidity code. Throughout the process of software development, employees are oftwen required to collaborate with one-another createing a separation of concernes within a system's architecure. Students will learn to take a simple yet more formalized smart contract specification and implement it to fit the interface of an already established frontend dApp. Students will then deploy the configured dApp to a centralized production environment, Github pages.

### Class Objectives

By the end of the unit, students will be able to:

* Implement a given smart contract specification into real solidity code.

* Integrate the contract with a JavaScript/HTML/CSS frontend.

* Deploy a bundled dApp to Github Pages

* Customize and deploy a landing page for projects on Github Pages

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1devzesQ1UKT2weYAz43Ei9YBIM863dYDtw9IFIMfLis/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

### Instructor Notes

* Refer to the `IPFS` documentation for further information about [IPFS Docs](https://docs.ipfs.io/)

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome Back (10 min)

In the previous day students

* What are some benefits of solidity events?

* **Answer** They are a cheap amount of gas.

* **Answer** They allow you to keep a log of information on-chain.

* **Answer** Events are MUCH cheaper than contract storage

* **Answer** Events are solidity's built-in way to interact with something external, such as a user interface.

* What are some potential issues that IPFS seeks to solve?

* **Answer** Inefficiencies in the web such as `duplicate files`.

* **Answer** Inefficiencies in the web such as having to route to a faraway sever to get the file you need when it might be right next door.

* **Answer** Problems with security and file integrity, such as not knowing whether or not files you have accessed over the web have changed.

* **Answer** Problems with the security of centralized servers providing a centralized attack vector.
