### 19. Everyone Do: Restricting the Withdraw Function with Require (15 min) (Critical)

In this activity we will be replacing our `if` conditional statement with a `require`.

Have students follow along while you code.

Continue with the `JointSavings.sol` contract in [Remix](https://remix.ethereum.org) and ensure that students have theirs open as well.

**Files:**

* [Unsolved - JointSavings.sol](Activities/19-Ins_Restricting_Withdraw_With_Require/Solved/JointSavings.sol)

Up to this point, everyone's contract should look like this:

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  function withdraw(uint amount, address payable recipient) public {
    if (recipient == account_one || recipient == account_two) {
      recipient.transfer(amount);
    }
  }

  function deposit() public payable {}

  function() external payable {}
}
```

Explain to the class:

* Even though this contract is logically sound, there is a special function we need to use called `require` to enforce the account check
  instead of using the `if` statement.

* The `require` function checks a condition just like an `if` statement does, only if the condition is false, it will return the
  leftover `gas` used and any `Ether`, and roll back the entire transaction. Consider it a hard stopping point, that you absolutely `require`
  a certain condition to be true to continue.

Remove the `if` statement, then replace it with the following `require`:

```solidity
function withdraw(uint amount, address payable recipient) public {
    require(recipient == account_one || recipient == account_two, "You do not own this account!");
    recipient.transfer(amount);
  }
```

Have the students catch up with the code, then elaborate:

* The require just like an `if/else` else statement checks if an expression returns `true`.

* If the expression returns `true` then the code after the declaration is executed.

* The major difference between an `if/else` and a `require` is a fundamental one.

  * When an `if/else` is false the code inside the `if` statement does not execute but the contract as a whole continues to executes as if everything was successful, thus continuing to spend the gas that was alloted to the contract call.

  * Unlike the `if/else` when a `require`'s condition fails the contract immediately ends execution and the remaining gas is returned to the person that executed the contract.

  * You can think of a `require` more as like a type of error handling, as you can see we can even declare a custom error message to the user. If withdraw is passed an address that is not one of the two addresses defined in our contract then they will get the message `You do not own this account!`.

Now we have a fully working `JointSavings` account with withdraw protection on our contract account and a deposit function to deposit our funds. Let's compile and deploy our contract to test it out!
