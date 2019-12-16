## 20.3 Lesson Plan: Solidity Continued

### Overview

Today's class will dive into more complex Solidity concepts, such as `mapping`s, globally available units and attributes, and how to tell time in the Ethereum blockchain.

### Class Objectives

By the end of the class, students will be able to:

* Use `uint` and `int` Number types in Solidity and explain when to use each.

* Use global variables to tell the current block number, transaction sender, and transaction value.

* Work with time in Solidity and use time variables to create a Timelock.

* Recognize that telling time in Solidity has variability relative to the network's block production time, and static compared to Gregorian calendar time.

* Add conditions to the withdraw function to trigger the timelock from a set threshold.

* Create a contract constructor in Solidity to allow reuse of the contract by preventing hardcoded values.

* Deploy and interact with contracts (Remix + Ganache).

### Instructor Notes

* Today's lesson should be exciting for students now that they have gotten a small taste of building smart contracts with Solidity.

* Expect some or all of the students to be somewhat anxious about learning a new language. Especially when that language differs so much from Python, reassure them that, with practice, they will be able to read and write Solidity in no time at all!

* Today's class introduces students to new programming concepts specific to the Solidity language. They will learn to use these concepts to build sophisticated smart contracts for Ethereum.

* If you are new to Solidity, we recommend reviewing the [Instructor Support documents](../Instructor_Support/Solidity.md) in preparation for this class.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1gRBz8OI5bruHxvoox5qagh13VWJMzG2r_n3yCRX_FMI/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 min)

Welcome students to the class by getting them excited about more advanced Solidity concepts!

* Today, we are going to be learning how to work with time in Solidity, how to add a timelock to our contract, and how to make our contracts reusable with constructors!

Have the students open up [Remix](https://remix.ethereum.org) and open up the `JointSavings.sol` contract from the last class.

---

### 2. Instructor Do: Static Typing Refresher (10 min)

First, let's ask the students some recall questions about static data types:

* What is a `uint`?

  * **Answer:** Unsigned Integer.

* What is the difference between an `int` and a `uint`?

  * **Answer:** `int` can be positive and negative, `uint` is positive only.

* What is a `payable` address, and why is it different from a regular address?

  * **Answer:** A payable address is like a normal address type, except it allows the `.transfer` function to be called in order to send it Ether.

Ask for any remaining questions before moving along.

---

### 3. Instructor Do: Globally Available Variables and Attributes in Solidity (10 min)

In this activity, we will cover some globally available attributes and variables in Solidity, such as `block` and `msg` in order to save the details of who last withdrew, when, and how much was withdrawn. We'll also add the ability to save the same details, but for deposits.

**Files:**

* [Solved - GlobalAttributes.sol](Activities/03-Ins_Global_Attributes/Solved/GlobalAttributes.sol)

* [Unsolved - GlobalAttributes.sol](Activities/03-Ins_Global_Attributes/Unsolved/GlobalAttributes.sol)

Propose to the students:

* What if we wanted to store the details of who last withdrew, when, and how much they withdrew?

* To do this, we'll need some built-in variables in Solidity that we can use to access this information.

Open up [Remix](https://remix.ethereum.org) and continue in the `JointSavings.sol` -- the unsolved `GlobalAttributes.sol` contains the code that `JointSavings` should have up to this point.

First, we need to change the way we check who the account owners are.

* Currently, we are checking whether or not the recipient parameter matches either of the accounts we set as the owners.

* This actually opens up a slight "vulnerability" where anyone can force this contract to withdraw funds into either of the owner wallets. While this doesn't transfer the Ether away from the owners, you certainly wouldn't want someone to have *any* control over your funds, even if it means moving between accounts you own.

* We can do this by checking the built-in `msg.sender` variable.

Remove the recipient parameter from the `withdraw` function, then replace any instance of `recipient` with `msg.sender`:

```solidity
 function withdraw(uint amount) public {
 require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");
 msg.sender.transfer(amount);
 }
```

* Now that the contract is safe from other people controlling our funds, we want to verify the sender. In other words, we check that the person who is sending the transaction, `msg.sender`, is one of the account owners. Doing this ensures that only the owners can successfully `withdraw` to their accounts.

* Notice that we can call the `.transfer` function just like we did before. This means that we can replace `recipient` with `msg.sender` as a drop-in. In other words, `msg.sender` is a payable address type.

Let's add an `address` variable called `last_to_withdraw` to the contract:

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
 address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
 address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

 address last_to_withdraw;

 function withdraw(uint amount) public {
 require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");
 msg.sender.transfer(amount);
 }

 function deposit() public payable {}

 function() external payable {}
}
```

* Notice that the address is not payable. This is because we only want to use this variable for tracking purposes so that we won't be calling `.transfer` on it.

* Now we need to add a check to see if the current recipient is different from the previous in the withdraw function.

Add an `if` statement that checks if the recipient is different from the previous.

```solidity
function withdraw(uint amount) public {
 require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

 if (last_to_withdraw != msg.sender) {
 last_to_withdraw = msg.sender;
 }

 msg.sender.transfer(amount);
}
```

Ask the students:

* Why might we include this if statement, versus just setting the `last_to_withdraw` every time?

  * **Answer**: It costs gas to write to the chain. By checking beforehand, we can prevent spending unnecessary gas when the variable doesn't need to change.

Let's add a couple more variables to the mix for more details. Under the `last_to_withdraw` variable, add the following variables:

```solidity
address last_to_withdraw;
uint last_withdraw_block;
uint last_withdraw_amount;

address last_to_deposit;
uint last_deposit_block;
uint last_deposit_amount;
```

* We are going to add a couple of uint variables that will keep track of which block number the withdraw occurred at, as well as how much was withdrawn. We'll do the same for deposits.

* While this data is already on-chain, visible from a block explorer, it is sometimes useful to have available in-contract.

* Solidity can't jump outside of its sandbox, so we need to be explicit about the variables we need and don't need.

Now, set these values using the built in `block.number`, `msg.sender`, and `msg.value`, starting with the `withdraw` function:

```solidity
function withdraw(uint amount) public {
 require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

 if (last_to_withdraw != msg.sender) {
 last_to_withdraw = msg.sender;
 }

 last_withdraw_block = block.number;
 last_withdraw_amount = amount;

 msg.sender.transfer(amount);
}
```

Do the same for `deposit`:

```solidity
function deposit() public payable {

 if (last_to_deposit != msg.sender) {
 last_to_deposit = msg.sender;
 }

 last_deposit_block = block.number;
 last_deposit_amount = msg.value;
}
```

Explain to the class:

* Notice that we are able to access the current block number using `block.number`. In this case, `block` is a built-in global variable that we can use to access various data about the current block.

* In the `deposit` function, we are setting the `last_deposit_amount` to equal `msg.value`.

* `msg` refers to the current transaction that is executing the smart contract.

* `msg.value` Refers to the amount of Ether that is attached to said transaction. In our case, we can save the amount that was deposited by storing the `msg.value`. We can use `msg.value` for many other calculations in the future, creating conditions that require a certain amount of Ether, or that keep track of how much Ether each user has stored in your contract.

Finally, we need to add the `public` keyword to these variables in order to auto-generate "getter" functions for them:

```solidity
address public last_to_withdraw;
uint public last_withdraw_block;
uint public last_withdraw_amount;

address public last_to_deposit;
uint public last_deposit_block;
uint public last_deposit_amount;
```

Explain to the class:

* Instead of creating a special function that fetches these values, a getter, like we did before, we can set a variable to `public` and Solidity will automatically generate a "getter" function for that variable, with the exact name as the variable!

* For example, we can now access the `last_to_withdraw` variable by calling the variable name as a function, like `last_to_withdraw()`. Note: The getter function name is equal to the variable name automatically.

* We still have to specify whether our functions are `public`, but this will make fetching data for us much easier.

Great! Now it's time for the students to modify their contracts and add some more details using `block` and `msg`!

---

### 4. Students Do: Using Global Variables (10 min)

In this activity, students will be adding the same details using `msg` and `block` variables in their contracts.

**Instructions:**

* [README.md](Activities/04-Stu_Global_Variables/README.md)

**Files:**

* [Unsolved - GlobalAttributes.sol](Activities/04-Stu_Global_Variables/Unsolved/GlobalAttributes.sol)

Send out the instructions, and have the TAs circulate the room to ensure that students are following along.

Encourage the students to visit the Solidity documentation link provided to reference what variables are available, such as `block` and `msg`.

### 5. Instructor Do: Review Global Attributes (10 min)

**Files:**

* [Solved - GlobalAttributes.sol](Activities/04-Stu_Global_Variables/Solved/GlobalAttributes.sol)

Open the solution and explain the following:

* We set the variables as `public` so that we don't have to create our getter functions manually.

* `block` accesses the current block's information.

* `msg` refers to the current transaction's information.

Ask the students the following questions:

* Why might we want to access these variables in our contracts?

  * **Answer:** It allows us to make decisions on what to do next based on who is calling the function, and under what conditions.

* What is `msg.value`?

  * **Answer:** The amount of Ether that was sent with the transaction.

Ask for further questions before moving on.

---

### 6. Instructor Do: Telling time in Solidity (10 min)

In this activity, we'll be adding a bit more logic to create a withdraw threshold.

We will be adding a "timelock" that locks withdrawals for 24 hours when someone withdraws, as well as explain the nuances when it comes to telling time in Ethereum.

Continue in the same contract as before, `JointSavings.sol`, or leverage the equivalent unsolved version below.

**Files:**

* [TellingTime.sol](Activities/06-Ins_Time_Solidity/Unsolved/TellingTime.sol)

First, add another variable called `uint unlock_time` -- this will be used to control when our contract is locked and unlocked:

```solidity
contract JointSavings {
 address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
 address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

 address public last_to_withdraw;
 uint public last_withdraw_block;
 uint public last_withdraw_amount;

 address public last_to_deposit;
 uint public last_deposit_block;
 uint public last_deposit_amount;

 uint unlock_time;

// ...
}
```

* Explain to the class that there are a few things to understand about telling time in Ethereum.

  * The first is that we are storing the time in `uint` format. This is standard for many systems (originating from Unix), allowing us to store the current time in an integer format.

  * Let's dig into the other nuances by continuing our code.

Add the following `require` to the contract at the top of the `withdraw` function:

```solidity
function withdraw(uint amount) public {)
 require(unlock_time < now, "Account is locked!");
 require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

 if (last_to_withdraw != msg.sender) {
 last_to_withdraw = msg.sender;
 }

 last_withdraw_block = block.number;
 last_withdraw_amount = amount;

 msg.sender.transfer(amount);
}
```

Explain to the students:

* You may notice that we are using the keyword `now` -- this is an alias for `block.timestamp`.

* Using `now`, we can calculate the current time within a window of 15 seconds.

* You may notice the compiler is saying to "avoid using now/block.timestamp" -- this is because of the inherent inaccuracy of the current time caused by the average blocktime.

* In Ethereum, the accuracy of `now` will always fluctuate based on the average blocktime. For the majority of our use cases, we can get away with a 15-second window.

  * Timing-critical applications will need to use special contracts called "Oracles" that can provide the exact current time. Note: we will not need to engineer these in our case, but any timing-critical decentralized applications may need Oracles.

Now, add the locking functionality by adding `unlock_time = now + 24 hours;` just before the `msg.sender.transfer`.

The `withdraw` function should look like:

```solidity
function withdraw(uint amount) public {
 require(unlock_time < now, "Account is locked!");
 require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

 if (last_to_withdraw != msg.sender) {
 last_to_withdraw = msg.sender;
 }

 last_withdraw_block = block.number;
 last_withdraw_amount = amount;

 unlock_time = now + 24 hours;

 msg.sender.transfer(amount);
}
```

* Notice how expressive we can calculate the time 24 hours from now, right in the native Solidity syntax!

* Solidity provides time units in `seconds`, `minutes`, `days`, and `weeks` -- and does not consider leap years!

* This is another reminder that if we need an extremely specific time, we'll need special smart contracts to maintain the Gregorian calendar for us, but we are just fine using this implementation.

* Using this logic, the withdraw function will first check if the `unlock_time` has passed, by checking if it is less than now. Then, just before withdrawing, it sets the new `unlock_time` to be 24 hours from now.

Now it's time for the students to create the timelock!

---

### 7. Students Do: Creating a Timelock (10 min)

In this activity, students will add the same timelock to their `JointSavings` contracts.

**Instructions:**

* [README.md](Activities/07-Stu_Timelock/README.md)

**Files:**

* [Unsolved - TellingTime.sol](Activities/07-Stu_Timelock/Unsolved/TellingTime.sol)

Send out the instructions, and have TAs circulate and ensure that students are:

* Placing the new `require` at the top of `withdraw`.

* Placing the timelock right before the `msg.sender.transfer`.

### 8. Instructor Do: Review Time in Solidity (10 min)

**Files:**

* [Solved - TellingTime.sol](Activities/07-Stu_Timelock/Solved/TellingTime.sol)

Open the solution and explain the following:

* We must enforce the timelock right away, which is why we place the `require` at the very top of the function.

* We also set the timelock right before we transfer, and not after. We want to make sure we calculate the lock before we send the funds for security purposes. Always remember to calculate the new state `BEFORE` sending funds. Otherwise, something called a "re-entry" attack may be possible, which we will learn about in the next unit.

Ask the students:

* What does a `require` do again? Why is it better than an `if` statement for this check?

  * **Answer:** `require` enforces a requirement, stopping the contract if the requirement is not satisfied, and returns leftover gas and Ether. In this case, we want this hard stopping point, as we will not move forward if this condition is not met.

* Why is there variability in the accuracy of time when using `now`/`block.timestamp`?

  * **Answer:** This is due to the average block time of the network. Unless we use special Gregorian Calendar contracts, we will have to work within the block time window.

Ask for any remaining questions before moving on.

---

### 9. BREAK (40 min)

---

### 10. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to class, allow them to settle, and explain the following:

* For the second half of class, we are going to add a threshold that only locks our savings account when more than 1/3 of
 the balance is pulled.

* Then, we are going to add a special function called a `constructor` that will allow us to deploy this contract with custom
 values, versus hardcoding things like our account owners directly in the code.

Have students navigate back to their [Remix IDE](https://remix.ethereum.org) and continue.

---

### 11. Instructor Do: Adding a Withdraw Threshold (10 min)

In this activity, we will add a simple `if` statement that checks if we are withdrawing over 1/3 of the balance, and updates the timelock if over that threshold.

* We are going to add a threshold that triggers this timelock only when we withdraw over a third of the balance. We will still allow the withdraw, but further withdrawals will be locked for 24 hours after that.

* This should be plenty of time for the other account holder to do some explaining as to why they withdrew so much!

**Files:**

* [Unsolved - WithdrawThreshold.sol](Activities/11-Ins_Adding_Withdraw_Threshold/Unsolved/WithdrawThreshold.sol)

This activity is quite simple. All we need to do is add the following `if` statement surrounding the original timelock:

```solidity
if (amount > address(this).balance / 3) {
 unlock_time = now + 24 hours;
}
```

Add this to the contract in Remix, then ask the class:

* What does `address(this).balance` do?

  * **Answer:** Gives the current balance of the contract.

Explain to the class:

* This condition is effectively saying: "If the amount we are withdrawing is greater than the balance of the contract divided by 3, lock the contract for 24 hours."

* With this one condition, we are creating a much more customized system than we'd be able to build on top of typical banking infrastructure.

* Simple things like this can also be what makes your smart contracts so powerful -- you can enforce whatever rules you decide!

Now, have the students add the same threshold to their contracts!

---

### 12. Students Do: Adding the Withdraw Threshold (10 min)

In this activity, students will follow the same steps to add the threshold to their withdraw function's timelock.

**Instructions:**

* [README.md](Activities/12-Stu_Threshold/README.md)

**Files:**

* [Unsolved - WithdrawThreshold.sol](Activities/12-Stu_Threshold/Unsolved/WithdrawThreshold.sol)

Send out the instructions and ensure that students can wrap their timelock using the proper conditional.

Ensure that students are accessing the contract's balance using `address(this).balance`.

### 13. Instructor Do: Review Withdraw Threshold (5 min)

**Files:**

* [Solved - WithdrawThreshold.sol](Activities/12-Stu_Threshold/Solved/WithdrawThreshold.sol)

Open the solution and explain the following:

* You can access the current balance of the contract by using `address(this).balance`. In this case, `this` is the contract and it is being converted into the `address` type, and all `address`es have the `.balance` function available.

* While we are dividing the balance by three by using the native `/` symbol, we will be learning more secure ways of dividing numbers next week. For now, this works just fine.

Ask for any remaining questions before moving on.

---

### 14. Instructor Do: Intro to Constructors (10 min) (Critical)

In this activity, we will be removing hardcoded address values and setting them in a `constructor` function instead.

Continue working in the same `JointSavings.sol` or leverage the equivalent contract below.

**Files:**

* [Unsolved - Constructors.sol](Activities/14-Ins_Constructors/Unsolved/Constructors.sol)

Explain to the class:

* Notice how we have our account owners hardcoded? Meaning, we set the values directly in the code to equal the addresses we want.

* While this works functionally, it is a code smell, as we'd have to modify the contract code manually every time we wanted to deploy a new JointSavings account.

* To make this contract reusable over and over again, we need to add a special function called a `constructor`.

First, add the constructor below the variable definitions, then remove the addresses being set, leaving only the address variable definitions:

```solidity
contract JointSavings {
 address payable account_one;
 address payable account_two;

 address public last_to_withdraw;
 uint public last_withdraw_block;
 uint public last_withdraw_amount;

 address public last_to_deposit;
 uint public last_deposit_block;
 uint public last_deposit_amount;

 uint unlock_time;

 constructor(address payable _one, address payable _two) public {
 account_one = _one;
 account_two = _two;
 }

// ...
}
```

* This constructor takes in the two payable addresses we want to set as our account owners and sets them to the designated addresses.

* This constructor function will only run ONCE, during the deployment of the contract. It will never be run again after that. It is used to "construct" the necessary variables in order to get the contract built.

* Soon, we will deploy this contract, and you will see an option in Remix that allows us to pass in these parameters during deployment.

Now it's time for the students to add their constructors!

---

### 15. Students Do: Adding a Constructor to the contract (15 min)

In this activity, students will replace their hardcoded values with a constructor in order to make their contracts
reusable and more production-ready.

**Instructions:**

* [README.md](Activities/15-Stu_Adding_Constructor/README.md)

**Files:**

* [Unsolved - Constructors.sol](Activities/15-Stu_Adding_Constructor/Unsolved/Constructors.sol)

Send out the instructions and have TAs circulate the class.

Ensure that students are:

* Removing the hardcoded address variables, while keeping the definition of the variable.

* Adding a constructor that takes two `payable` address types in the parameters.

* Setting the accounts properly within the constructor.

### 16. Instructor Do: Review Constructors (10 min)

**Files:**

* [Solved - Constructors.sol](Activities/15-Stu_Adding_Constructor/Solved/Constructors.sol)

Open the solution and explain the following:

* We can remove the hardcoded address definitions because we added a constructor.

* In the constructor, we set the account owners to equal the addresses we pass during deployment.

Ask the students the following questions:

* When is the constructor function called?

  * **Answer:** During deployment.

* Can the function be called again after the contract is on-chain?

  * **Answer:** No, it is only called during deployment.

* Why is a constructor better to use than hardcoding values?

  * **Answer:** We can now reuse our contract code over and over again, as-is, and pass new parameters during deployment.

Ask for any remaining questions before moving on.

---

### 17. Everyone Do: Deploying and Testing the Contract (15 min) (Critical)

In this activity, you will have the class follow along and deploy the current contract, setting the account owners in the
constructor in the deployment tab of Remix.

Ensure that everyone has the same contract setup that looks just like the solution below.

**Files:**

* [Solved - JointSavings.sol](Activities/17-Ins_Deploying_Testing/Solved/JointSavings.sol)

First, open up `Ganache` and ensure that your local network is running.

![Ganache](Images/ganache.png)

Have students open up their Ganache workspaces as well, and allow them to catch up.

In Remix, navigate to the `Deploy` tab, switch the Web3 provider to `Injected Web3` to connect to MetaMask, then login/confirm the MetaMask connection:

![Remix Deploy](Images/remix-deploy.png)

Have the students perform the same, and allow them to catch up.

Ensure that everyone is connected to the `localhost:8545` network in MetaMask before moving forward!

The `Environment` section at the top left should look like:

![Environment](Images/injected-web3.png)

* Notice that we can now expand the `Deploy` section in the contract to add parameters upon deployment.

* This is our constructor!

Paste in the first two addresses that Ganache generates (should be the same mnemonic throughout class) into these fields:

![Remix Constructor](Images/deploy-constructor.png)

Ensure students are caught up, then hit `transact` to deploy to Ganache, then confirm in MetaMask!

![Confirm deployment](Images/confirm-deploy.png)

Now, in Remix, we can interact with our contract via MetaMask:

![Deployed](Images/deployed.png)

Change the value field to send `10 ether`, then click the `deposit` button to deposit into the contract:

![Deposit](Images/deposit.png)

Now, have students do the same.

Once everyone has deposited funds into their contract successfully, have them try
withdrawing.

Remind students that we will need to convert the Ether units to Wei units when withdrawing!
We can use [eth-converter.com](https://eth-converter.com) for easy conversion.

Have students continue interacting with the various functions in their contracts.

Get the class excited, as they have just built a complex smart contract that can be deployed to any Ethereum network, building their own rules!

### 18. Instructor Do: Review Smart Contracts (10 min)

Congratulate the students on building smart contracts, and remind them that few in the world can do this, let alone tried! They are already differentiating themselves from the crypto-crowd. However, you must remind them that with this power comes responsibility -- security should be top of mind, and we cannot allow cutting corners in Solidity!

Ask the students the following questions:

* What are smart contracts useful for?

  * **Answer:** We can build any program on top of the blockchain, giving us the ability to write fully decentralized applications.

* Why do we use a constructor?

  * **Answer:** So we can avoid hardcoded values and reuse our code.

* Why do we use strict data types in Solidity?

  * **Answer:** We need to be unambiguous in our code, just like we need to be unambiguous in legal contracts.

  * **Answer:** It is more efficient, and thus cheaper, to define the types upfront, versus having Solidity figure it out after the fact, spending precious gas.

* What nuances are there when it comes to telling time in Solidity/Ethereum?

  * **Answer:** We are limited to the static time that is not Gregorian.

  * **Answer:** We are limited to a window of accuracy defined by the average block time.

  * **Answer:** To get more accurate time, we need special Oracle contracts.

---

### 19. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
