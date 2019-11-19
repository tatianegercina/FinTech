# Building your First Contract

In this activity, you will build a simple smart contract to represent a customers account.

## Instructions

* Use this [Data Type Cheatsheet](Types_Cheatsheet.md) to easily see how you define variables in Solidity compared to Python.

* Create a basic smart contract named `SimpleCustomerAccount`.

  * The contract should look like:

    ```solidity
      contract SimpleCustomerAccount {
        // insert code here
      }
    ```

* Add the following variables:

  * An `address` named `owner` -- make this equal to your main Ethereum address.

  * A `bool` named `isNewAccount` -- we can set this to `true` or `false` to represent if the account is new.

  * A `uint` (non-negative integer) called `account_balance` -- we can set this to whatever number we'd like for now (as long as it is positive!).

  * A `string` called `customer_name` -- set this to equal the name of the customer.
  Remember to use the `"` double-quote when defining strings in Solidity!

## Challenge

* If time remains, try to set the `account_balance` to an `int` and set it to a negative balance.

## Hints

* Remember to use semicolons at the end of every variable definition, and every line of code that doesn't end in curly brackets!

* Using types is a pain to get used to at first, but once you get the hang of them, they will help prevent bugs in the future,
  and make your code much less ambiguous!
