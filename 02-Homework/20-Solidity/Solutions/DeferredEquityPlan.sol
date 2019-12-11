pragma solidity ^0.5.0;

// lvl 3: equity plan
contract DeferredEquityPlan {
    address human_resources = msg.sender;

    address payable employee; // bob
    bool active;

    uint total_shares = 1000;
    uint annual_distribution = 250; // 1000 shares over 4 years

    uint start_time; // contract start time
    uint unlock_time = now + 365 days; // will increment every year

    uint public distributed_shares; // starts at 0

    constructor(address payable _employee) public {
        human_resources = msg.sender;
        employee = _employee;
        active = true;
        start_time = now;
    }

    function distribute() public {
        require(msg.sender == human_resources || msg.sender == employee, "You do not have permission to execute this contract.");
        require(active == true, "Contract not active.");
        require(unlock_time <= now, "Shares have not vested yet!");
        require(distributed_shares < total_shares, "All shares have been distributed.");

        unlock_time += 365 days; // lock for another year
        distributed_shares = (now - start_time) / 365 days * annual_distribution; // calculate total shares from how many years have passed * annual_distribution
    }

    function deactivate() public {
        require(msg.sender == human_resources, "Cannot deactivate this contract.");
        active = false;
    }

    function() external payable {
        revert("Do not send Ether to this contract!");
    }
}
