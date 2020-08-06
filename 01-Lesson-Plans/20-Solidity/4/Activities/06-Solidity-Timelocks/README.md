# Solidity Timelocks

In this activity, a day trading firm has asked you to incorporate a blockchain-based investment account system to replace their current system. In particular, they want to ensure that a user must wait at least 24 hours from their last withdrawal to withdraw again from their account.

Therefore, you will create a `DayTradingAccount` smart contract that utilizes timelocks.

## Instructions

Open [Remix](http://remix.ethereum.org/), import the [starter file](Unsolved/DayTradingAccount.sol) and perform the following code drills. Once you finish, compile, and deploy the contract to ensure the code works.

1. Create a contract called `DayTradingAccount` that contains:

    * Initializes a public payable address variable `owner`.

    * Initialized a public uint variable `unlock_time`.

2. Create a public `constructor` function that sets the `owner` as the `msg.sender`.

3. Create a public payable `deposit` function and a fallback function.

4. Create a public view of `getBalance` function that returns the balance within the contract.

5. Create a public `withdraw` function that...

    * Inputs a payable address variable `recipient` as the first parameter.

    * Inputs a uint variable `amount` as the second parameter.

    * Uses a require statement to check if the `recipient` is equal to the `owner`. Otherwise, the transaction should error out with the following statement: "You are not the owner of this account. Permission denied."

    * Uses a require statement to check if the `unlock` time is before the current `now` time. Otherwise, the transaction should error out with the following statement: "You need to wait at least 24 hours from the last withdrawal before making another one."

    * Uses a require statement to check if the balance of the contract minus the withdrawn amount is greater than 25,000 wei. Otherwise, the transaction should error out with the following statement: "Withdrawing this amount would put you below the day trading threshold of 25,000 wei."

    * Sets the unlock time to the current time plus 24 hours.

    * Transfers the parameterized `amount` to the `recipient` address using the `transfer` function.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
