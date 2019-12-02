pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  // insert last to withdraw variables here

  // insert last to deposit variables here

  function withdraw(uint amount, address payable recipient) public {
    require(recipient == account_one || recipient == account_two, "You don't own this account!");

    // add an if statement checking the msg.sender here
    // set the last_to_withdraw within the if statement

    recipient.transfer(amount);
  }

  function deposit() public payable {

    // insert if statement that checks and updates the last_to_deposit here

    // update the last_deposit_block and last_deposit_amount variables after the if statement here

  }

  function() external payable {}
}
