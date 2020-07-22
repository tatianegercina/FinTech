# Using SafeMath to secure your token

In this activity, you will implement the SafeMath library and use it for all math operations in order to secure your token from integer underflow and overflow vulnerabilities, as well as other math-related vulnerabilities.

## Instructions

* Navigate to Remix, and open up your `ArcadeToken.sol` contract. You can also use this [starter file](Unsolved/ArcadeTokenSafeMath.sol).

* Add the following import statement just below the `pragma` and above the `contract` definition:

  ```solidity
  import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
  ```

  * You can find this URL later by a quick internet search for "OpenZeppelin SafeMath" and copying the "raw" URL to the contract from GitHub. You may do this with any other contract library in the future as well.

* Add the following as the first line of code in your smart contract:

  ```solidity
  using SafeMath for uint;
  ```

  * This will link the SafeMath library to the `uint` type, allowing us to call `.add()`, `.sub()`, `.mul()`, `.div()`, and so on directly from a `uint` instead of using `+`, `-`, `*`, and `/`.

* Replace every math operation in the contract with the SafeMath equivalent. For example:

  ```solidity
  balances[msg.sender] -= value;
  ```

  Becomes:

  ```solidity
  balances[msg.sender] = balances[msg.sender].sub(value);
  ```

* Deploy and test your contract. You should now be safe from any integer underflows and overflows!

## Hints

* Remember to include the variable reassignments -- SafeMath will not mutate the variable it is operating on. You must reassign the variable with an `=`.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
