# Advanced Solidity Contracts

In this activity, a small local amusement park has asked you to incorporate a blockchain-based digital tokening system to replace their current physical token system.

Therefore, you will use the fundamentals of Solidity smart contracts to create a `RideToken` contract.

## Instructions

Open [Remix](http://remix.ethereum.org/), import the [starter file](Unsolved/RideToken.sol) and perform the following code drills. Once you finish, compile and deploy the contract to ensure the code works.

1. Create a contract called `RideToken` that contains:

    * Initializes a public address variable `owner`.

    * Initialized a public mapping variable `balances` that maps address to uint.

2. Create a public `constructor` function that sets the `address` variable as the `msg.sender`

3. Create a public `mint` function that...

    * Inputs an address variable `receiver` as the first parameter.

    * Inputs a uint variable `amount` as the second parameter.

    * Uses a require statement to check if the `msg.sender` is equal to the `owner` address variable.

      * If so, the `balances` mapping object should be updated with the associated receiver and newly minted `amount`.

      * If not, the contract should print "Permission Denied. You are not the contract owner."

4. Create a public `send` function that...

    * Inputs an address variable `receiver` as the first parameter.

    * Inputs a uint variable `amount` as the second parameter.

    * Uses a require statement to check if the `amount` is less than or equal to the token balance associated with the `msg.sender`.

      * If so, decrement the token balance of the `msg.sender` by the `amount`, and similarly, increment the token balance of the `receiver` by the `amount`.

      * If not, the contract should print "Insufficient balance."

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
