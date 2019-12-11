pragma solidity ^0.5.0;

// lvl 3: equity plan
contract DeferredEquityPlan {
    address human_resources;

    address payable employee; // ceo
    bool active;

    // @TODO: Set the total shares and annual distribution
    // Your code here!

    uint start_time;
    // @TODO: Set the `unlock_time` to be 365 days from now
    // Your code here!

    uint distributed_shares; // starts at 0

    constructor(address payable _employee) public {
        human_resources = msg.sender;
        employee = _employee;
        active = true;
        start_time = now;
    }

    function distribute() public {
        require(msg.sender == human_resources || msg.sender == employee, "You do not have permission to execute this contract.");
        require(active == true, "Contract not active.");

        // @TODO: Add "require" statements to enforce that:
        // 1: `unlock_time` is less than or equal to `now`
        // 2: `distributed_shares` is less than the `total_shares`
        // Your code here!

        // @TODO: Add 365 days to the `unlock_time`
        // Your code here!

        // @TODO: Calculate the shares distributed by using the function (now - start_time) / 365 days * the annual distribution
        // Make sure to include the parenthesis around (now - start_time) to get accurate results!
        // Your code here!

    }

    function deactivate() public {
        require(msg.sender == human_resources, "Cannot deactivate this contract.");
        active = false;
    }

    function() external payable {
        revert("Do not send Ether to this contract!");
    }
}
