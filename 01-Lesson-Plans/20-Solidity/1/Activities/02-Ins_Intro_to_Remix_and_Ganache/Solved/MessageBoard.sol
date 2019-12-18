pragma solidity ^0.5.0;

contract MessageBoard {
    string public message;
    function setMessage(string memory newMessage) public {
        message = newMessage;
    }
}
