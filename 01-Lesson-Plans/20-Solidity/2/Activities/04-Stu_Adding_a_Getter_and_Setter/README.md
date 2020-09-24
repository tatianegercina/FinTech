# Adding a Getter and Setter

In this activity, you will be adding a `Getter` and `Setter` to the Customer Account code that you previously created.

## Instructions

* Using your Customer Account contract as a starting point implement one function for getting the user account information, and a second function for setting the user account information.

* Create a "getter" function called `getInfo` -- it should look something like this:

```solidity
function getInfo() public returns() {
  // return user data here
}
```

* Since this function is returning data, specify the types this function will return in `returns`.

* Return all of the variables you specified before, such as the `address`, `newAccount`, `accountBalance`, and `accountID`.

* Remember to wrap multiple return values in parenthesis, and don't forget your semicolons!

* You will no longer need the default values for the customer info; go ahead and remove them.

  ```solidity
  address owner;
  bool is_new_account;
  uint account_balance;
  string customer_name;
  ```

* The `setter` function should be named `setInfo` and look something like this.

```solidity
function setInfo(address newOwner, bool isNewAccount, uint newAccountBalance, string memory newCustomerName) public {
  // set user data here
}
```

## Challenge

* If you have time think about what other customer details could be stored to make our customer savings account even better.

## Hints

* Really think about all of the variables that your `getter` is going to return and their order in the returns statement.

* For the `setter` don't forget that all you are doing is `setting` the new values for the customer variables.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
