pragma solidity ^0.5.0;

/*
1. Modify the `PersonalSavings` contract to initialize the following variables:

    * An address variable `last_to_withdraw`.

    * An unsigned integer variable `last_withdraw_block`.

    * A unsigned integer variable `last_withdraw_amount`.

    * An address variable `last_to_deposit`.

    * A unsigned integer variable `last_deposit_block`.

    * A unsigned integer variable `last_deposit_amount`.

2. Modify the `withdraw` function in the `PersonalSavings` contract as follows:

    * Use the `msg.sender` variable instead of the `recipient` parameter.

    * Use an `if` statement to check if the `last_to_withdraw` is NOT equal to `msg.sender`, if so
      set `last_to_withdraw` equal to `msg.sender`.

    * Set `last_withdraw_block` equal to the `block.number` variable.

    * Set `last_withdraw_amount` equal to the `amount` parameter.

**Note:** You will have to remove the recipient parameter from the `withdraw` function definition.

3. Modify the `deposit` function in the `PersonalSavings` contract as follows:

    * Use an `if` statement to check if the `last_to_deposit` is NOT equal to `msg.sender`, if so
      set `last_to_deposit` equal to `msg.sender`.

    * Set `last_deposit_block` equal to the `block.number` variable.

    * Set `last_deposit_amount` equal to the `msg.value` variable.
*/

contract PersonalSavings {
  address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  address payable private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  string account_holder = "Jane Doe";

  function withdraw(uint amount, address payable recipient) public {
    require(recipient == public_savings || recipient == private_savings, "This is not your account");
    require(address(this).balance >= amount, "You don't have enough funds!");
    return recipient.transfer(amount);
  }

  function deposit() public payable {
  }

  function() external payable {
  }
}
