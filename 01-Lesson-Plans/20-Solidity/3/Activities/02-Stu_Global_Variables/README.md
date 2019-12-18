# Using Global Variables and Attributes in Solidity

In this activity, you will add some more details to your smart contract, storing who previously withdrew and deposited,
when, and how much.

## Instructions

* Remove the `recipient` parameter from the `withdraw` function.

* Replace any instance of `recipient` with `msg.sender` -- this will ensure that we are checking who is sending the transaction, versus some parameter that anyone can control.

* Add the following variable definitions, under the account owner definitions:

  * `last_to_withdraw` -- this will be a regular `address` type.

  * `last_withdraw_block` -- since `block.number` is a `uint`, we'll need to make this variable a `uint` as well.

  * `last_withdraw_amount` -- we'll need this to be a `uint` as well since that's what Ether is measured in.

* Then, in the `withdraw` function, add the following logic (the full `if` statement, including what's inside):

  * "If the last to withdraw is not equal to the message sender, update last to withdraw."

* After the `if` statement:

  * Set the `last_withdraw_amount` to the `value` parameter.

  * Set the `last_withdraw_block` to equal `block.number`.

* Once you complete the withdraw tracking, add the following variables to track deposits:

  * `last_to_deposit` -- again, this will be a regular `address`.

  * `last_deposit_amount` -- since `msg.value` is a `uint`, this will be too.

  * `last_deposit_block` -- another `uint` here, since block numbers are also stored that way.

* In the `deposit` function, add the following logic:

  * "If the last to deposit is different, update the `last_to_deposit` variable."

* Then, set the deposit variables:

  * `last_deposit_block` should equal the current block number.

  * `last_deposit_amount` should equal `msg.value`, since we attach Ether to the transaction when we call `deposit`.

* Finally, set all of the variables you want to access (the ones you just created that track withdraw and deposits)
  as `public` -- this will auto-generate "getter" functions that will allow you to fetch that variable easily.

## Hints

* In case you forget which variables are available to you, visit the [Solidity documentation.](https://solidity.readthedocs.io/en/latest/units-and-global-variables.html)

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
