# Solidity Global Variables and Functions

In this activity, you will practice global variables and functions in Solidity.

## Instructions

Open [Remix](http://remix.ethereum.org/), import the [starter file](Unsolved/personal_savings.sol), and perform the following code drills. Once you finish, compile the file to ensure the code works.

1. Modify the `PersonalSavings` contract to initialize the following variables:

    * An address variable `last_to_withdraw`.

    * An unsigned integer variable `last_withdraw_block`.

    * A unsigned integer variable `last_withdraw_amount`.

    * An address variable `last_to_deposit`.

    * A unsigned integer variable `last_deposit_block`.

    * A unsigned integer variable `last_deposit_amount`.

2. Modify the `withdraw` function in the `PersonalSavings` contract as follows:

    * Use the `msg.sender` variable instead of the `recipient` parameter.

    * Use an `if` statement to check if the `last_to_withdraw` is NOT equal to `msg.sender`, if so set `last_to_withdraw` equal to `msg.sender`.

    * Set `last_withdraw_block` equal to the `block.number` variable.

    * Set `last_withdraw_amount` equal to the `amount` parameter.

**Note:** You will have to remove the recipient parameter from the `withdraw` function definition.

3. Modify the `deposit` function in the `PersonalSavings` contract as follows:

    * Use an `if` statement to check if the `last_to_deposit` is NOT equal to `msg.sender`, if so set `last_to_deposit` equal to `msg.sender`.

    * Set `last_deposit_block` equal to the `block.number` variable.

    * Set `last_deposit_amount` equal to the `msg.value` variable.

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
