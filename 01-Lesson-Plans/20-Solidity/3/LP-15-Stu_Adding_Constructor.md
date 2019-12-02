### 15. Students Do: Adding a Constructor to the Contract (15 min)

In this activity, students will replace their hardcoded values with a constructor in order to make their contracts
reusable and more production-ready.

**Instructions:**

* [README.md](Activities/15-Stu_Adding_Constructor/README.md)

**Files:**

* [Unsolved - Constructors.sol](Activities/15-Stu_Adding_Constructor/Unsolved/Constructors.sol)

Send out the instructions and have TAs circulate the class.

Ensure that students are:

* Removing the hardcoded address variables, while keeping the definition of the variable.

* Adding a constructor that takes two `payable` address types in the parameters.

* Setting the accounts properly within the constructor.

### 16. Instructor Do: Review Constructors (10 min)

**Files:**

* [Solved - Constructors.sol](Activities/15-Stu_Adding_Constructor/Solved/Constructors.sol)

Open the solution and explain the following:

* We can remove the hardcoded address definitions because we added a constructor.

* In the constructor, we set the account owners to equal the addresses we pass during deployment.

Ask the students the following questions:

* When is the constructor function called?

  **Answer:** During deployment.

* Can the function be called again after the contract is on-chain?

  **Answer:** No, it is only called during deployment.

* Why is a constructor better to use than hardcoding values?

  **Answer:** We can now reuse our contract code over and over again, as-is, and just pass new parameters during deployment.

Ask for any remaining questions before moving on.
