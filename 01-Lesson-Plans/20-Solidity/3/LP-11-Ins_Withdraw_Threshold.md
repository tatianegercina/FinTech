### 10. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to class, allow them to settle, and explain the following:

* For the second half of class, we are going to add a threshold that only locks our savings account when more than 1/3 of
  the balance is pulled.

* Then, we are going to add a special function called a `constructor` that will allow us to deploy this contract with custom
  values, versus hardcoding things like our account owners directly in the code.

Have students navigate back to their [Remix IDE](https://remix.ethereum.org) and continue.

### 11. Instructor Do: Adding a Withdraw Threshold (10 min)

In this activity, we will add a simple `if` statement that checks if we are withdrawing over 1/3 of the balance,
and updates the timelock if over that threshold.

* We are going to add a threshold that triggers this timelock only when we withdraw over a third of the balance.
  We will still allow the withdraw, but further withdraws will be locked for 24 hours after that.

* This should be plenty of time for the other account holder to do some explaining as to why they withdrew so much!


**Files:**

* [Unsolved - WithdrawThreshold.sol](Activities/11-Ins_Adding_Withdraw_Threshold/Unsolved/WithdrawThreshold.sol)

This activity is quite simple. All we need to do is add the following `if` statement surrounding the original timelock:

```solidity
if (amount > address(this).balance / 3) {
  unlock_time = now + 24 hours;
}
```

Add this to the contract in Remix, then ask the class:

* What does `address(this).balance` do?

  **Answer:** Gives the current balance of the contract.

Explain to the class:

* This condition is effectively saying: "If the amount we are withdrawing is greater than the balance of the contract divided by 3, lock the contract for 24 hours."

* With this one condition, we are creating a much more customized system than we'd be able to build on top of typical banking infrastructure.
  Simple things like this can also be what make your smart contracts so powerful -- you can enforce whatever rules you decide!

Now, have the students add the same threshold to their contracts!
