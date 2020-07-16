pragma solidity ^0.5.0;

contract ArtTokenVulnerable {
    address payable owner = msg.sender;
    string public symbol = "ART";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        balances[msg.sender] -= value;
        balances[recipient] += value;
    }

    function purchase() public payable {
        uint amount = msg.value * exchange_rate;
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        balances[recipient] += value;
    }

    function withdrawBalance() public{
        if( ! (msg.sender.call.value(balances[msg.sender])() ) ){
            revert()
        }

        balances[msg.sender] = 0;
    }
}
