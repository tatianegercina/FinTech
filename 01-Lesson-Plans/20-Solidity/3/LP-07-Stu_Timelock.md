### 7. Students Do: Creating a Timelock (10 min)

In this activity, students will add the same timelock to their `JointSavings` contracts.

**Instructions:**

* [README.md](Activities/07-Stu_Timelock/README.md)

**Files:**

* [Unsolved - TellingTime.sol](Activities/07-Stu_Timelock/Unsolved/TellingTime.sol)

Send out the instructions, and have TAs circulate and ensure that students are:

* Placing the new `require` at the top of `withdraw`.

* Placing the timelock right before the `msg.sender.transfer`.

### 8. Instructor Do: Review Time in Solidity (10 min)

**Files:**

* [Solved - TellingTime.sol](Activities/07-Stu_Timelock/Solved/TellingTime.sol)

Open the solution and explain the following:

* We must enforce the timelock right away, which is why we place the `require` at the very top of the function.

* We also set the timelock right before we transfer, and not after. We want to make sure we calculate the lock before
  we send the funds for security purposes. Always remember to change calculate the new state BEFORE sending funds.
  Otherwise, something called a "re-entry" attack may be possible, which we will learn about in the next unit.

Ask the students:

* What does a `require` do again? Why is it better than an `if` statement for this check?

  **Answer:** Require enforces a requirement, stopping the contract if the requirement is not satisfied, and returns leftover gas and Ether.
  In this case, we want this hard stopping point, as we will not move forward if this condition is not met.

* Why is there variability in the accuracy of time when using `now`/`block.timestamp`?

  **Answer:** This is due to the average block time of the network. Unless we use special Gregorian Calendar contracts,
  we will have to work within the block time window.

Ask for any remaining questions before moving on.

- - -

### 9. BREAK (40 min)

- - -
