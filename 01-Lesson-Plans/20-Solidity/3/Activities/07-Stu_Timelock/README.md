# Creating a Timelock in Solidity

In this activity, you will add a `require` and a timelock calculation to your `JointSavings.sol` contract
that will lock the contract for 24 hours after withdrawing.

## Instructions

* Add a new variable called `unlock_time` -- this will be a `uint` type.

* In the `withdraw` function, add a `require` that checks if `unlock_time < now` and returns the error "Account locked!"
  when the condition is not met.

* Right before the `msg.sender.transfer` call at the end of the `withdraw` function, update the `unlock_time` to `now + 24 hours;`

* Voila! Congratulate yourself on learning how to work with rudimentary time calculations in the native Solidity syntax!

## Hints

* To see what time units are available, with even more details, visit the [Solidity documentation.](https://solidity.readthedocs.io/en/latest/units-and-global-variables.html)
