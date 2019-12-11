// Building Basic  Smart Contracts

pragma solidity ^0.5.0;

/*
1. Create a contract called `MessageContract` that contains:

    * An Ethereum address variable `my_address` with a valid Ethereum address assigned to it.

    * A string variable `message` with a greeting salutation assigned to it.
*/


contract MessageContract {
  address my_address = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  string message = "Hey there! you can send me Ethereum here.";
}
