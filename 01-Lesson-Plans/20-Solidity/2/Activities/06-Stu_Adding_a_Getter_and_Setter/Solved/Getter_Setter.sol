pragma solidity ^0.5.11;

contract SimpleCustomerAccount {
    address owner;
    bool newAccount;
    uint accountBalance;
    string accountID;

    function getInfo() public returns(address, bool, uint, string memory) {
        return (owner, newAccount, accountBalance, accountID);
    }

    function setInfo(address newOwner, bool isNewAccount, uint newAccountBalance, string memory newAccountID) public {
        owner = newOwner;
        newAccount = isNewAccount;
        accountBalance = newAccountBalance;
        accountID = accountID;
    }
}
