### 6. Instructor Do: Telling time in Solidity (10 min)

In this activity, we'll be adding a bit more logic to create a withdraw threshold.

We will be adding a "timelock" that locks withdrawals for 24 hours when someone withdraws, as well as explain
the nuances when it comes to telling time in Ethereum.

Continue in the same contract as before, `JointSavings.sol`, or leverage the equivalent unsolved version below.

**Files:**

* [TellingTime.sol](Activities/06-Ins_Time_Solidity/Unsolved/TellingTime.sol)

First, add another variable called `uint unlock_time` -- this will be used to control when our contract is locked and unlocked:

```solidity
contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  address public last_to_withdraw;
  uint public last_withdraw_block;
  uint public last_withdraw_amount;

  address public last_to_deposit;
  uint public last_deposit_block;
  uint public last_deposit_amount;

  uint unlock_time;

// ...
}
```

* Explain to the class that there are a few things to understand about telling time in Ethereum.

  * The first is that we are storing the time in `uint` format. This is standard for many systems (originating from Unix), allowing us to store the current time in an integer format.

  * Let's dig into the other nuances by continuing our code.

Add the following `require` to the contract at the top of the `withdraw` function:

```solidity
function withdraw(uint amount) public {)
  require(unlock_time < now, "Account is locked!");
  require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

  if (last_to_withdraw != msg.sender) {
    last_to_withdraw = msg.sender;
  }

  last_withdraw_block = block.number;
  last_withdraw_amount = amount;

  msg.sender.transfer(amount);
}
```

Explain to the students:

* You may notice that we are using the keyword `now` -- this is an alias for `block.timestamp`.

* Using `now`, we can calculate the current time within a window of 15 seconds.

* You may notice the compiler is saying to "avoid using now/block.timestamp" -- this is because of the inherent inaccuracy of the current time caused by the average blocktime.

* In Ethereum, the accuracy of `now` will always fluctuate based on the average blocktime. For the majority of our use cases, we can get away with a 15 second window.
  However, timing-critical applications will need to use special contracts called "Oracles" that can provide the exact current time, but we will not need to engineer these in our case,
  but keep this in mind for the future, if you decide to build timing-critical decentralized applications.

Now, add the locking functionality by adding `unlock_time = now + 24 hours;` just before the `msg.sender.transfer`.

The `withdraw` function should look like:

```solidity
function withdraw(uint amount) public {
  require(unlock_time < now, "Account is locked!");
  require(msg.sender == account_one || msg.sender == account_two, "You don't own this account!");

  if (last_to_withdraw != msg.sender) {
    last_to_withdraw = msg.sender;
  }

  last_withdraw_block = block.number;
  last_withdraw_amount = amount;

  unlock_time = now + 24 hours;

  msg.sender.transfer(amount);
}
```

* Notice how expressive we can calculate the time 24 hours from now, right in the native Solidity syntax!

* Solidity provides time units in `seconds`, `minutes`, `days`, and `weeks` -- and does not consider leap years!

* This is another reminder that if we need extremely specific time, we'll need special smart contracts to maintain the Gregorian calendar for us,
  but we are just fine using this implementation.

* Using this logic, the withdraw function will first check if the `unlock_time` has passed, by checking if it is less than now.
  Then, just before withdrawing, it sets the new `unlock_time` to be 24 hours from now.

Now it's time for the students to create the timelock!
