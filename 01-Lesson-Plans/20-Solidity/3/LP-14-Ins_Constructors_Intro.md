### 14. Instructor Do: Intro to Constructors (10 min) (Critical)

In this activity, we will be removing hardcoded address values, and setting them in a `constructor` function instead.

Continue working in the same `JointSavings.sol` or leverage the equivalent contract below.

**Files:**

* [Unsolved - Constructors.sol](Activities/14-Ins_Constructors/Unsolved/Constructors.sol)

Explain to the class:

* Notice how we have our account owners hardcoded? Meaning, we set the values directly in the code to equal the addresses we want.

* While this works functionally, it is a code smell, as we'd have to modify the contract code manually every time we wanted to
  deploy a new JointSavings account.

* To make this contract reusable over and over again, we need to add a special function called a `constructor`.

First, add the constructor below the variable definitions, then remove the addresses being set, leaving only the address variable definitions:

```solidity
contract JointSavings {
  address payable account_one;
  address payable account_two;

  address public last_to_withdraw;
  uint public last_withdraw_block;
  uint public last_withdraw_amount;

  address public last_to_deposit;
  uint public last_deposit_block;
  uint public last_deposit_amount;

  uint unlock_time;

  constructor(address payable _one, address payable _two) public {
    account_one = _one;
    account_two = _two;
  }

// ...
}
```

* This constructor takes in the two payable addresses we want to set as our account owners, and sets them to the designated addresses.

* This constructor function will only run ONCE, during the deployment of the contract. It will never be run again after that,
  it is simply used to "construct" the necessary variables in order to get the contract built.

* Soon, we will deploy this contract, and you will see an option in Remix that allows us to pass in these parameters during deployment.

Now it's time for the students to add their constructors!
