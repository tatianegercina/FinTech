# Implementing Ether Management Functions (Joint Savings Account)

In this activity, you will be implementing basic functions for `depositing`, and `withdrawing` ether from a contract's address.

## Instructions

* Open the Remix IDE and create a new file called `JointSavings.sol`.

* Create a new contract named `JointSavings`; it should look something like this.

```solidity
contract JointSavings {
 // insert code here
}
```

* Inside this new contract define a variable named `account_one` of type `address` and set it's value to one of the `wallet's addresses` that you generated from your mnenonic phrase. Then define a second variable named `account_two` of type `address` and set it as another one of your addresses.

* Now define a function named `withdraw` that will accept a `uint` named `amount`, and a `payable address` named `recipient`.

* Inside the `withdraw` function, you are going to call the `transfer` method on the passed `recipient` variable and tell it the `amount` to transfer. The inside of the function should look something like this.

```solidity
recipient.transfer(amount);
```

* Next implement the empty `public payable` function. We have named `deposit`. Think back on why this function does not require any logic inside; it is because we are just trying to move the Ether into the contract's address.

* Finally, add the default fallback function that was previously discussed so that our contract can store `Eth` sent from outside the deposit function.

## Challenge

* In future exercises, we will be implementing checks to add additional features. Think about what different `if/then` conditions you could create to add additional features now.

## Hints

* Don't forget that the `withdraw` functions needs to be `public`.

* Don't forget that the `deposit` functions needs to be `public payable`.

* Don't forget that the address that we are passing into our withdraw function to transfer the funds to must also be marked `payable`.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
