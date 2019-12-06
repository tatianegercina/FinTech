pragma solidity ^0.5.0;

// import SafeMath library via Github URL here

contract ArcadeToken {
    // @TODO: add the "using SafeMath..." line here to link the library to all uint types
    // YOUR CODE HERE!

    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        // replace the following with the .sub function
        balances[msg.sender] -= value;
        // replace the following with the .add function
        balances[recipient] += value;
    }

    function purchase() public payable {
        // replace the following with the .mul function
        uint amount = msg.value * exchange_rate;
        // replace the following with the .add function
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        // replace the following with the .add function
        balances[recipient] += value;
    }
}
