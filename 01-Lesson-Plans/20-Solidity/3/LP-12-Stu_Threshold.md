### 12. Students Do: Adding the Withdraw Threshold (10 min)

In this activity, students will follow the same steps to add the threshold to their withdraw function's timelock.

**Instructions:**

* [README.md](Activities/12-Stu_Threshold/README.md)

**Files:**

* [Unsolved - WithdrawThreshold.sol](Activities/12-Stu_Threshold/Unsolved/WithdrawThreshold.sol)

Send out the instructions and ensure that students are able to wrap their timelock using the proper conditional.

Ensure that students are accessing the contract's balance using `address(this).balance`.

### 13. Instructor Do: Review Withdraw Threshold (5 min)

**Files:**

* [Solved - WithdrawThreshold.sol](Activities/12-Stu_Threshold/Solved/WithdrawThreshold.sol)

Open the solution and explain the following:

* You can access the current balance of the contract by using `address(this).balance`. In this case, `this` is the contract
  and it is being converted into the `address` type, and all `address`es have the `.balance` function available.

* While we are dividing the balance by 3 by using the native `/` symbol, we will be learning more secure ways of dividing numbers
  next week. For now, this works just fine.

Ask for any remaining questions before moving on.
