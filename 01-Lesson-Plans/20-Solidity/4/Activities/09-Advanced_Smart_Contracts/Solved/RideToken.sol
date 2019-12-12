pragma solidity ^0.5.0;

contract RideToken {

    // Initializes an address variable
    address public minter;

    // Creates a mapping variable to map addresses to token balances
    mapping (address => uint) public balances;

    // Constructor sets the minter address as the contract creator
    constructor() public {
        minter = msg.sender;
    }

    // Sends an amount of newly created coins to an address and can only be called by the contract creator
    function mint(address receiver, uint amount) public {
        require(msg.sender == minter, "Permission Denied. You are not the owner.");
        balances[receiver] += amount;
    }

    // Sends an amount of existing coins rom any caller to an address
    function send(address receiver, uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance.");
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
    }
}
