### 3. Students Do: Build a Basic Contract (15 min)

In this exercise Students will use their data type cheat sheet to build a basic contract that stores simple variables that represent a rewards/bank account balance.
Instructor will explain to the class that by the end of today, we will have build a simple joint savings account.
Tomorrow, we will add special features like a timelock based on a threshold.

**Instructions:**

* [README.md](Activities/03-Stu_Building_a_Basic_Contract/README.md)

**Files:**

* [Unsolved - SimpleCustomerAccount.sol](Activities/03-Stu_Building_a_Basic_Contract/Unsolved/SimpleCustomerAccount.sol)

* [Solved - SimpleCustomerAccount.sol](Activities/03-Stu_Building_a_Basic_Contract/Solved/SimpleCustomerAccount.sol)

### 4. Instructor Do: Data Types Review (5 min)

**Files:**

* [SimpleCustomerAccount.sol](Activities/03-Stu_Building_a_Basic_Contract/Solved/SimpleCustomerAccount.sol)

Open the solution and ask the students the following questions:

* Why is Solidity so strict with its typing?

  **Answer:** It allows for better error handling in code.

  **Answer:** Contracts should not leave room for ambiguity.

  **Answer:** Being upfront about data types and the size to store them results in less computational overhead/gas costs.

* Why do we have a separate datatype for addresses in Solidity?

  **Answer:** Addresses are a fixed size so it is more cost effective than a string, which uses a variable amount of storage space.

* What's the difference between an `int` and a `uint`?

  **Answer:** An `int` stores positive and negative numbers, a `uint` only stores positive numbers.

Now that we've thoroughly covered many of the types within Solidity, let's add some functions to our contract!
