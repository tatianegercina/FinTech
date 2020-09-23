pragma solidity ^0.5.0;

contract SimpleCustomerAccount {
    address owner;
    bool is_new_account;
    uint account_balance;
    string customer_name;

    function getInfo() public returns(address, bool, uint, string memory) {
        return (owner, is_new_account, account_balance, customer_name);
    }

    function setInfo(address newOwner, bool isNewAccount, uint newAccountBalance, string memory newCustomerName) public {
        owner = newOwner;
        is_new_account = isNewAccount;
        account_balance = newAccountBalance;
        customer_name = newCustomerName;
    }
}
