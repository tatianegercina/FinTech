### 11. Students Do: Implementing Ether Management functions (15 min)

In this exercise students will beging implementing a `joint savings account` contract using the ether management functions from the previous activity. By the end of this activity students will be able to deposit and witdraw ether from their contract's address.

**Instructions:**

* [README.md](Activities/11-Stu_Implement_Ether_functions/README.md)

**Files:**

* [Unsolved - JointSavings.sol](Activities/11-Stu_Implement_Ether_functions/Unsolved/JointSavings.sol)

* [Solved - JointSavings.sol](Activities/11-Stu_Implement_Ether_functions/Solved/JointSavings.sol)

### 12. Instructor Do: Review Ether Management Functions (5 min)

**Files:**

* [JointSavings.sol](Activities/11-Stu_Implement_Ether_functions/Solved/JointSavings.sol)

Open the solution and explain the following:

* The `withdraw` function accepts the following parameters:

  * A `uint` named `amount`.

  * A `payable address` named `recipient`.

* Inside the `withdraw` function we transfer our designated amount to our designated recipient address.

* Remember, since we set our recipient address as payable we are able to call the built-in `transfer` method and pass it an amount.

```solidity
  function withdraw(uint amount, address payable recipient) public {
      recipient.transfer(amount);
    }
```

* We also added an empty function called deposit so that our contract can store our `Eth`.

```solidity
  function deposit() public payable {}
```

* Lastly, we added our payable fallback function so that any `Eth` sent to our contract outside of the deposit function,
  such as sending `Eth` directly to the contract's address, will also be stored.

```solidity
  function() external payable {}
```

Ask for any remaining questions before moving on.
