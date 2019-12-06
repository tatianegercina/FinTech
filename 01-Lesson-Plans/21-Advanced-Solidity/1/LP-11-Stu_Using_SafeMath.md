### 11. Students Do: Using SafeMath (15 min)

In this activity students will implement the SafeMath library and replace all math operations with the SafeMath alternatives.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/11-Stu_Using_SafeMath/README.md)

**Files:**

* [ArcadeTokenSafeMath.sol](Activities/11-Stu_Using_SafeMath/Unsolved/ArcadeTokenSafeMath.sol)

Ensure that students:

* Properly import SafeMath via the GitHub URL provided.

* Add the `using SafeMath...` line to the top of their contract.

* Replace the math operations with the SafeMath alternatives.

Take care that students are reassigning the variables with an `=` and not just running the SafeMath operations. SafeMath will not mutate the variable it is operating on, so you will need to ensure that the variables are reassigned.

### 12. Instructor Do: SafeMath Review (10 min)

**Files:**

* [ArcadeTokenSafeMath.sol](Activities/11-Stu_Using_SafeMath/Solved/ArcadeTokenSafeMath.sol)

Open the solution and explain the following:

* We import the SafeMath library directly from GitHub at the top of the file. This is only supported in Remix. We can also copy and paste the contract directly into our code above our own.

* We need the `using SafeMath for uint;` line to link the library to the `uint` type. That way, we can call the `.add()`, `.sub()`, etc functions on any `uint` later.

* By replacing all of the math operations with the SafeMath alternatives, we secure ourselves from potential balance hacks.

Ask for any remaining questions before moving on.
