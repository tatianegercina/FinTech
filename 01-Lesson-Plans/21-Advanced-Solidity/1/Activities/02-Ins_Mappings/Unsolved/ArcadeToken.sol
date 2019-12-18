pragma solidity ^0.5.0;

contract ArcadeToken {
    // set the contract owner to msg.sender here (make sure it is a payable address)
    // set the symbol of the token here (make sure to set the string as public)
    // set the exchange_rate for how many tokens to distribute per wei

    // set a mapping of address to uint called "balances"

    function balance() public view returns(uint) {
        // return the balance of msg.sender from the balances mapping
    }

    function transfer(address recipient, uint value) public {
        // subtract the value from msg.sender's balance
        // add value to the recipient's balance
    }

    function purchase() public payable {
        uint amount = ; // multiply the exchange rate by the msg.value
        // add the amount to the msg.sender's balance
        // transfer the msg.value to the owner address
    }

    function mint(address recipient, uint value) public {
        // require that the msg.sender is the owner
        // add the value to the recipient's balance
    }
}
