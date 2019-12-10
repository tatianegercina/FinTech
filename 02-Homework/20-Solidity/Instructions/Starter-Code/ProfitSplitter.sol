pragma solidity ^0.5.0;

contract ProfitSplitter {
    // @TODO: Insert the three payable beneficiary addresses
    // Your code here!

    constructor(address payable _one, address payable _two, address payable _three) public {
        // @TODO: Set the beneficiary addresses to equal the parameters
        // Your code here!
}

    // @TODO: Create a balance function that returns the `uint` of the current contract balance
    // Your code here!

    function deposit() public payable {
        // @TODO: Split `msg.value` into 3 and store in a `uint` called `amount`

        // @TODO: Transfer the `amount` to each beneficiary address

        // @TODO: Take care of a potential remainder by subtracting `amount * 3` from `msg.value` and sending that to a beneficiary
    }

    function() external payable {
        // @TODO: Call the deposit function from the fallback to ensure the logic executes when Ether is sent directly to the contract
    }
}
