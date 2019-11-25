### 17. Everyone Do: Deploying and Testing the Contract (15 min) (Critical)

In this activity, you will have the class follow along and deploy the current contract, setting the account owners in the
constructor in the deployment tab of Remix.

Ensure that everyone has the same contract setup that looks just like the solution below.

**Files:**

* [Solved - JointSavings.sol](Activities/17-Ins_Deploying_Testing/Solved/JointSavings.sol)

First, open up `Ganache` and ensure that your local network is running.

![Ganache](Images/ganache.png)

Have students open up their Ganache workspaces as well, and allow them to catch up.

In Remix, navigate to the `Deploy` tab, switch the Web3 provider to `Injected Web3` to connect to MetaMask,
then login/confirm the MetaMask connection:

![Remix Deploy](Images/remix-deploy.png)

Have the students perform the same, and allow them to catch up.

Ensure that everyone is connected to the `localhost:8545` network in MetaMask before moving forward!

The `Environment` section at the top left should look like:

![Environment](Images/injected-web3.png)

* Notice that we are able to now expand the `Deploy` section in the contract to add parameters upon deployment.

* This is our constructor!

Paste in the first two addresses that Ganache generates (should be the same mnemonic throughout class) into these fields:

![Remix Constructor](Images/deploy-constructor.png)

Ensure students are caught up, then, hit `transact` to deploy to Ganache, then confirm in MetaMask!

![Confirm deployment](Images/confirm-deploy.png)

Now, in Remix, we can actually interact with our contract via MetaMask:

![Deployed](Images/deployed.png)

Change the value field to send `10 ether`, then click the `deposit` button to deposit into the contract:

![Deposit](Images/deposit.png)

Now, have students do the same.

Once everyone has deposited funds into their contract successfully, have them try
withdrawing.

Remind students that we will need to convert the Ether units to Wei units when withdrawing!
We can use [eth-converter.com](https://eth-converter.com) for easy conversion.

Have students continue interacting with the various functions in their contract.

Get the class excited, as they have just built a complex smart contract that can be deployed to any Ethereum network, building their own rules!

### 18. Instructor Do: Review Smart Contracts (10 min)

Congratulate the students on building smart contracts, and remind them that few in the world can do this, let alone tried!
They are already differentiating themselves from the crypto-crowd.
However, you must remind them that with this power comes responsibility -- security should be top of mind and we cannot allow cutting corners in Solidity!

Ask the students the following questions:

* What are smart contracts useful for?

  **Answer:** We can build any program on top of the blockchain, giving us the ability to write fully decentralized applications.

* Why do we use a constructor?

  **Answer:** So we can avoid hardcoded values and reuse our code.

* Why do we use strict data types in Solidity?

  **Answer:** We need to be unambiguous in our code, just like we need to be unambiguous in legal contracts.

  **Answer:** It is more efficient, and thus cheaper, to define the types up front,
  versus having Solidity figure it out after the fact, spending precious gas.

* What nuances are there when it comes to telling time in Solidity/Ethereum?

  **Answer:** We are limited to static time that is not Gregorian.

  **Answer:** We are limited to a window of accuracy defined by the average block time.

  **Answer:** In order to get more accurate time, we need special Oracle contracts.

### 19. Instructor Do: Recap/Career Services (35 min)

This section is reserved for the career services portion of class.
