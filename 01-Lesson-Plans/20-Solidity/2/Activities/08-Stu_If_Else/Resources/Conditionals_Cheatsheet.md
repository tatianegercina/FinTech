#### Conditonals Data Type Cheatsheet

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

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
