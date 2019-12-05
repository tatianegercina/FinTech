pragma solidity ^0.5.0;

// import SafeMath library via Github URL here

contract ArcadeToken {
    // add the "using SafeMath..." line here to link the library to all uint types

    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        balances[msg.sender] -= value; // replace with .sub function
        balances[recipient] += value; // replace with .add
    }

    function purchase() public payable {
        uint amount = msg.value * exchange_rate; // replace with .mul
        balances[msg.sender] += amount; // replace with .add
        owner.transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        balances[recipient] += value; // replace with .add
    }
}
