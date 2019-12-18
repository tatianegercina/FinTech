pragma solidity ^0.5.0;

// @TODO: import the SafeMath library via Github URL
// YOUR CODE HERE!

contract ArcadeToken {
    // @TODO: Add the "using SafeMath..." line here to link the library to all uint types
    // YOUR CODE HERE!

    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        // @TODO: Modify the following line of code to use the `.sub` function
        balances[msg.sender] -= value;
        // @TODO: Modify the following line of code to use the `.add` function
        balances[recipient] += value;
    }

    function purchase() public payable {
        // @TODO: Modify the following line of code to use the `.mul` function
        uint amount = msg.value * exchange_rate;
        // @TODO: Modify the following line of code to use the `.add` function
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        // @TODO: Modify the following line of code to use the `.add` function
        balances[recipient] += value;
    }
}
