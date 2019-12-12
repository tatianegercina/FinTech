# Using If/Else in Solidity

In this activity, you will add an `if` statement to your `JointSavings` contract that checks `if` the recipient address matches either of the account owner addresses.

## Instructions

* Take a moment to look over your `JointSavings` contract from the Instructor's demo. As you may recall, we defined variables at the beginning of the contract that holds the values for two Ethereum addresses generated from our mnemonic phrase.

* Right now, anyone can pass an address to our contract's `withdraw` function and `withdraw` the funds to any address that they choose. We need to make it so that funds from the contract can only be withdrawn to the accounts that we define.

* To implement this check, you will need to use an `if statement` and the `||` (or) operator to check if the `recipient` is `==` to `account_one` or `account_two`.

## Challenge

* Take some time to once again think about what other variables and conditions you could add to the contract to extend it's functionality.

## Hints

* If you are stuck, please refer back to the Conditionals Cheat Sheet.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
