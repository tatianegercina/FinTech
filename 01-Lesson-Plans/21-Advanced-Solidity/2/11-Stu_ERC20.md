### 11. Students Do: Building an ERC20 Token with OpenZeppelin (20 min)

In this activity, students will implement the ArcadeToken using the ERC20 standard, provided by the OpenZeppelin library.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/11-Stu_ERC20/README.md)

**Files:**

* [ArcadeTokenERC20.sol](Activities/11-Stu_ERC20/Unsolved/ArcadeTokenERC20.sol)

Ensure that students are properly passing parameters to the `ERC20Detailed` constructor and that they are properly using the `onlyOwner` modifier.

### 12. Instructor Do: ERC20 Review (10 min)

**Files:**

* [ArcadeTokenERC20.sol](Activities/11-Stu_ERC20/Solved/ArcadeTokenERC20.sol)

Open the solution and explain the following:

* The `onlyOwner` modifier allows us to add `onlyOwner` to the list of modifiers (usually after `public`) on any function we'd like to restrict.

* The constructor passes the `ERC20Detailed` parameters properly to set the token's name, symbol, and number of decimal places.

* Within the constructor, we set the token's owner to `msg.sender`. Then we call `_mint` to add the `initial_supply` to the token owner's balance.

* Our new `mint` function we added will be restricted to `onlyOwner`, and will

Ask for any remaining questions before moving on.
