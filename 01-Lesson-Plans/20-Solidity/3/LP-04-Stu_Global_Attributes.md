### 4. Students Do: Using Global Variables (10 min)

In this activity, students will be adding the same details using `msg` and `block` variables in their contracts.

**Instructions:**

* [README.md](Activities/04-Stu_Global_Variables/README.md)

**Files:**

* [Unsolved - GlobalAttributes.sol](Activities/04-Stu_Global_Variables/Unsolved/GlobalAttributes.sol)

Send out the instructions, and have the TAs circulate around the room to ensure that students are following along.
Encourage the students to visit the Solidity documentation link provided to reference what variables are available,
such as `block` and `msg`.

### 5. Instructor Do: Review Global Attributes (10 min)

**Files:**

* [Solved - GlobalAttributes.sol](Activities/04-Stu_Global_Variables/Solved/GlobalAttributes.sol)

Open the solution and explain the following:

* We set the variables as `public` so that we don't have to manually create our own getter functions.

* `block` accesses the current block's information.

* `msg` refers to the current transaction's information.

Ask the students the following questions:

* Why might we want to access these variables in our contracts?

  **Answer:** It allows us to make decisions on what to do next based on who is calling the function, and under what conditions.

* What is `msg.value`?

  **Answer:** The amount of Ether that was sent with the transaction.

Ask for further questions before moving on.
