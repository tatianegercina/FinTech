pragma solidity ^0.5.0;

contract RideToken {

    address public minter;
    mapping (address => uint) public balances;

    // Constructor code is only run when the contract is created
    constructor() public {
        minter = msg.sender;
    }

    // Sends an amount of newly created coins to an address and can only be called by the contract creator
    function mint(address receiver, uint amount) public {
        require(msg.sender == minter);
        balances[receiver] += amount;
    }

    // Sends an amount of existing coins rom any caller to an address
    function send(address receiver, uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance.");
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
    }
}
