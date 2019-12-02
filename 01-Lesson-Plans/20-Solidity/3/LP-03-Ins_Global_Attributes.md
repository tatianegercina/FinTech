### 3. Instructor Do: Globally Available Variables and Attributes in Solidity (10 min)

In this activity, we will cover some globally available attributes and variables in Solidity, such as
`block` and `msg` in order to save the details of who last withdrew, when, and how much was withdrawn.
We'll also add the ability to save the same details, but for deposits.

**Files:**

* [Solved - GlobalAttributes.sol](Activities/03-Ins_Global_Attributes/Solved/GlobalAttributes.sol)

* [Unsolved - GlobalAttributes.sol](Activities/03-Ins_Global_Attributes/Unsolved/GlobalAttributes.sol)

Propose to the students:

* What if we wanted to store the details of who last withdrew, when, and how much they withdrew?
  To do this, we'll need some built-in variables in Solidity that we can use to access
  this information.

Open up [Remix](https://remix.ethereum.org) and continue in the `JointSavings.sol` -- the unsolved `GlobalAttributes.sol`
contains the code that `JointSavings` should have up to this point.

First, we need to change the way we check who the account owners are.

* Currently, we are checking whether or not the recipient parameter matches either of the accounts we set as the owners.
  This actually opens up a slight "vulnerability" where anyone can force this contract to withdraw funds into either of the
  owner wallets. While this doesn't transfer the Ether away from the owners, you certainly wouldn't want someone to have *any*
  control over your funds, even if it means moving between accounts you own.

* We can do this by checking the built-in `msg.sender` variable.

Remove the recipient parameter from the `withdraw` function, then replace any instance of `recipient` with `msg.sender`:

```solidity
  function withdraw(uint amount) public {
    require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");
    msg.sender.transfer(amount);
  }
```

* Now are contract is safe from other people controlling our funds. We are now checking that the person who is actually
  sending the transaction, `msg.sender` is any of the account owners. Now, only the owners can successfully `withdraw` to their accounts.

* Notice that we can actually call the `.transfer` function just like we did before -- this means that we can replace `recipient`
  with `msg.sender` as a drop in -- in other words, `msg.sender` is a payable address type.

Let's add an `address` variable called `last_to_withdraw` to the contract:

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  address last_to_withdraw;

  function withdraw(uint amount) public {
    require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");
    msg.sender.transfer(amount);
  }

  function deposit() public payable {}

  function() external payable {}
}
```

* Notice that the address is not payable. This is because we only want to use this variable for tracking purposes,
  so we won't be calling `.transfer` on it.

Now we need to add a check to see if the current recipient is different from the previous in the withdraw function.
Add an `if` statement that checks if the recipient is different from the previous.

```solidity
function withdraw(uint amount) public {
  require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

  if (last_to_withdraw != msg.sender) {
    last_to_withdraw = msg.sender;
  }

  msg.sender.transfer(amount);
}
```

Ask the students:

* Why might we include this if statement, versus just setting the `last_to_withdraw` every time?

  **Answer**: It costs gas to write to the chain. By checking beforehand, we can prevent spending unnecessary gas
  when the variable doesn't need to change.

Let's add a couple more variables to the mix for more details. Under the `last_to_withdraw` variable,
add the following variables:

```solidity
address last_to_withdraw;
uint last_withdraw_block;
uint last_withdraw_amount;

address last_to_deposit;
uint last_deposit_block;
uint last_deposit_amount;
```

* We are going to add a couple uint variables that will keep track of which block number the withdraw occurred at,
  as well as how much was withdrawn. We'll do the same for deposits.

* While this data is already on-chain, visible from a block explorer, it is sometimes useful to have available in-contract.

* Solidity can't jump outside of its sandbox, so we need to be explicit about the variables we need, and don't need.

Now, set these values using the built in `block.number`, `msg.sender`, and `msg.value`, starting with the `withdraw` function:

```solidity
function withdraw(uint amount) public {
  require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

  if (last_to_withdraw != msg.sender) {
    last_to_withdraw = msg.sender;
  }

  last_withdraw_block = block.number;
  last_withdraw_amount = amount;

  msg.sender.transfer(amount);
}
```

Do the same for `deposit`:

```solidity
function deposit() public payable {

  if (last_to_deposit != msg.sender) {
    last_to_deposit = msg.sender;
  }

  last_deposit_block = block.number;
  last_deposit_amount = msg.value;
}
```

Explain to the class:

* Notice that we are able to access the current block number using `block.number`. In this case, `block` is a built-in
  global variable that we can use to access various data about the current block.

* In the `deposit` function, we are setting the `last_deposit_amount` to equal `msg.value`.
  `msg` refers to the current transaction that is executing the smart contract. `msg.value` actually refers
  to the amount of Ether that is attached to said transaction. In our case, we can save the amount that was deposited by
  storing the `msg.value`. We can use `msg.value` for many other calculations in the future, creating conditions that require
  a certain amount of Ether, or that keep track of how much Ether each user has stored in your contract.

Lastly, we need to add the `public` keyword to these variables in order to auto-generate "getter" functions for them:

```solidity
address public last_to_withdraw;
uint public last_withdraw_block;
uint public last_withdraw_amount;

address public last_to_deposit;
uint public last_deposit_block;
uint public last_deposit_amount;
```

Explain to the class:

* Instead of creating a special function that fetches these values, a getter, like we did before,
  we can actually simply set a variable to `public` and Solidity will automatically generate a "getter" function
  for that variable, with the exact name as the variable!

* For example, we can now access the `last_to_withdraw` variable by calling the variable name as a function,
  like `last_to_withdraw()` -- the getter function name is equal to the variable name automatically.

* We still have to specify whether our functions are `public`, but this will make fetching data for us much easier.

Great! Now it's time for the students to modify their contracts and add some more details using `block` and `msg`!
