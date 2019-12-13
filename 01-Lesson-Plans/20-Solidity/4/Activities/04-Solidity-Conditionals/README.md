# Solidity Conditionals

In this activity, you will practice conditionals in Solidity.

## Instructions

Open [Remix](http://remix.ethereum.org/), import the [starter files](Unsolved/), and perform the following code drills. Once you finish, compile the files to ensure the code works.

1. Use the `latest_trade.sol` file to create a contract named `TradeController` that contains:

    * An unsigned integer variable `previous_price`.

    * A string variable `trade_type`.

2. Add a public function named `makeTrade` to the `LatestTrade` contract as follows:

    * Define an unsigned integer `current_price` as the unique function's parameter.

    * Into the body of the function, use an `if` statement to check if the input parameter `current_price` is less than the contract variable `current_price`, if so, set the `trade_type` string variable as "Buy" and set the `previous_price` to the `current_price`.

3. Modify the `makeTrade` function of the `LatestTrade` contract as follows.

    * Add a boolean variable `buy_anyway` as the second parameter.

    * Use and `OR ( || )` clause within the `if` statement to check if it's true that the `current_price` is less that `previous_price` or `buy_anyway` is true.

    * Add an `else if` statement to check if the `current_price` is greater than the `previous_price`, if so, set the `trade_type` to "Sell" and the `previous_price` equal to the `current_price`.

    * Add an `Else` statement to set the `trade_type` to "Hold" in case the previous conditions were false.

4. Use the `personal_savings.sol` file to update the `PersonalSavings` contract as follows:

    * Add an `if` statement to the `withdraw` function to validate if the `recipient` address parameter is equal to the `public_savings` or the `private_savings` addresses, and the balance of the contract is greater than or equal to the `amount` parameter; if so, call the `transfer` method of the `recipient` address.

## Conditonals Data Type Cheatsheet

English             | Python   | Solidity
--------------------|----------|---------
 "Red" `or` "blue"  | `or`     | `||`
   1 `and` 4        | `and`    |  `&&`
 `Not` "funny"      | `not`    | `!`

Some code examples

Python `or`:

 ```python
if number == 1 or number == 2:
  return number
 ```

Solidity `or`

 ```solidity
if (number == 1 || number == 2) {
  return number;
}
 ```

 Python `and`:

 ```python
if number > 1 and color > 4:
  return number
 ```

Solidity `and`

 ```solidity
if (number > 1 && number > 4) {
  return number;
}
 ```

## Hints

* You can get the balance of the current contract by calling `address(this).balance` as mentioned [here](https://ethereum.stackexchange.com/a/21449).

* [Conditionals Cheatsheet](https://github.com/coding-boot-camp/FinTech-Lesson-Plans/blob/master/01-Lesson-Plans/20-Solidity/2/Activities/06-Stu_If_Else/Resources/Conditionals_Cheatsheet.md)

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
