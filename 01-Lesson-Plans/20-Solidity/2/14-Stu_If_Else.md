### 14. Students Do: Using If/Else in Solidity (10 min)

In this activity, students will add to their `JointSavings` contract functionality that uses if/else statements.

In this case, we are adding an `address` called `last_used` to keep track of which was the last withdraw address.
`If` the latest address is different from the `last_used`, then update `last_used`.

Send out the instructions, which includes a cheat-sheet that compares how conditionals work in Python vs Solidity.

**Instructions:**

* [README.md](Activities/14-Stu_If_Else/README.md)

**Files:**

* [JointSavings.sol](Activities/14-Stu_If_Else/Unsolved/JointSavings.sol)

* [Conditionals Cheat Sheet](Activities/14-Stu_If_Else/Conditionals_Cheatsheet.md)

Have the TAs circulate the class and ensure that students are properly implementing their if/else statements.

Remind them that they have to:

* Put the condition in parenthesis.

* Put the body of the if statement in curly brackets.

### 15. Instructor Do: Conditionals Review (5 min)

**Files:**

* [JointSavings.sol](Activities/14-Stu_If_Else/Solved/JointSavings.sol)

Open the solution and explain the following:

* Inside the `withdraw` function we added a check to make sure that the accounts that we are withdrawing funcds to is one of the two account owners.

* We took the previous `recipient.transfer(amount)` line and moved it inside of our `if/then` block; now this code will only execute if the condition returns `true`.

* Inside the condition itself we are checking that `recipient` is equal to `account_one` or `recipient` is equal to `account_two`.

```Solidity
if (recipient == account_one || recipient == account_two) {
    recipient.transfer(amount);
}
```

Ask for any remaining questions before moving on.
