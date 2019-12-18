# Adding a Withdraw Threshold to your Joint Savings Account

In this activity, you will add a simple `if` statement that checks if the withdrawal amount is greater than 1/3 of the contract
balance.

## Instructions

* Add an `if` statement that surrounds the original `unlock_time = now + 24 hours` line.

* In this `if` statement, check if `amount` is greater than the current balance of the contract, divided by 3.

## Hints

* You can access the current balance of the contract by using `address(this).balance`. In this case, `this` is the contract
  and it is being converted into the `address` type, and all `address`es have the `.balance` function available.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
