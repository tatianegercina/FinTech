### 6. Students Do: Adding a Getter and Setter (15 min)

In this exercise Students will be adding a Getter and a Setter function to the `SimpleCustomerAccount` contract that they just wrote.

Send out the instructions to the class so that they may begin reviewing the exercise.

**Instructions:**

* [README.md](Activities/06-Stu_Adding_a_Getter_and_Setter/README.md)

**Files:**

* [Unsolved - Getter_Setter.sol](Activities/06-Stu_Adding_a_Getter_and_Setter/Unsolved/Getter_Setter.sol)

* [Solved - Getter_Setter.sol](Activities/06-Stu_Adding_a_Getter_and_Setter/Solved/Getter_Setter.sol)

Have TAs circulate to address any questions that students may have about Solidity functions, their modifiers and parameters.

* Remember that strings are a more complex datatype and thus require the memory modifier to be specified when you are passing them as a parameter to a function.

* A return statement's values must be contained within parathesis when returning multiple values.

* Functions must contain the public modifier to be accessible outside the contract.

### 7. Instructor Do: Review Getters and Setters (5 min)

**Files:**

* [Getter_Setter.sol](Activities/06-Stu_Adding_a_Getter_and_Setter/Solved/Getter_Setter.sol)

Open the solution and explain the following:

* The `getInfo` function should specify the following return types:

  * `address`

  * `bool`

  * `uint`

  * `string memory`

* Inside the `getInfo` we should return the following variables:

  * `owner`

  * `newAccount`

  * `accountBalance`

  * `accountID`

```solidity
    function getInfo() public returns(address, bool, uint, string memory) {
        return (owner, newAccount, accountBalance, accountID);
    }
```

* The `setInfo` function should accpet the following parameters:

  * newOwner as an `address` type

  * isNewAccount as a `bool`

  * newAccountBalance as a `uint`

  * newAccountID as `string memory`

* Inside the `setInfo` function we should set the folling variables equal to the following function parameters.

  * `owner` is equal to `newOwner`

  * `newAccount` is equal to `isNewAccount`

  * `accountBalance` is equal to `newAccountBalance`

  * `accountID` is equal to `accountID`

Ask for any remaining questions before moving on.
