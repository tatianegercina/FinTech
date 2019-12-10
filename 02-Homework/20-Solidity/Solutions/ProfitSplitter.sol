pragma solidity ^0.5.0;

contract ProfitSplitter {
    address payable beneficiary_one;
    address payable beneficiary_two;
    address payable beneficiary_three;

    constructor(address payable _one, address payable _two, address payable _three) public {
        beneficiary_one = _one;
        beneficiary_two = _two;
        beneficiary_three = _three;
}

    function balance() public view returns(uint) {
        return address(this).balance;
    }

    function deposit() public payable {
        uint amount = msg.value / 3;

        beneficiary_one.transfer(amount);
        beneficiary_two.transfer(amount);
        beneficiary_three.transfer(amount);

        beneficiary_one.transfer(msg.value - amount * 3); // take care of a potential remainder
    }

    function() external payable {
        deposit();
    }
}
