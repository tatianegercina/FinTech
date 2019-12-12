# Building your First Contract

In this activity, you will build a simple, smart contract to represent a customer's account.

## Instructions

* Use this [Data Type Cheatsheet](Resources/Types_Cheatsheet.md) to easily see how you define variables in Solidity compared to Python.

* Create a basic smart contract named `SimpleCustomerAccount`.

 * The contract should look like:

 ```solidity
 contract SimpleCustomerAccount {
 // insert code here
 }
 ```

* Choose the appropriate data type for the following variables:

 * `owner` - your main Ethereum address (i.e. 0xaaaaaaaaaaaaaaaaa).

 * `is_new_account` - represents if the account is new or not (`true` or `false`).

 * `account_balance` - holds the account balance (10000).

 * `customer_name` - holds the name of the customer ("Bob").

## Challenge

* If time remains, try to set the `account_balance` to an `int` and set it to a negative balance.

## Hints

* Remember to use semicolons at the end of every variable definition, and every line of code that doesn't end in curly brackets!

* Using types is a pain to get used to at first, but once you get the hang of them, they will help prevent bugs in the future, and make your code much less ambiguous!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
