pragma solidity >=0.4.22 <0.6.0;

contract MartianAuction {


    constructor(
        address payable _beneficiary
    ) public {
        beneficiary = _beneficiary;
    }

    function bid(address payable sender) public payable {
    }

    function withdraw() public returns (bool) {
    }

    function pendingReturn(address sender) public view returns (uint) {
    }

    function auctionEnd() public {
    }
}
