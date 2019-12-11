// Building Basic  Smart Contracts

pragma solidity ^0.5.0;

/*
2. Create a contract called `PersonalSavings` than contains:

    * A public payable address variable called `public_savings` with a valid Ethereum address assigned to it.

    * An address variable called `private_savings` with a valid address assigned to it.

    * A string variable called `account_holder` with your name assigned to it.
*/

contract PersonalSavings {
  address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  address private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  string account_holder = "Jane Doe";
}
