pragma solidity ^0.6.0;

import "https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/master/contracts/utils/Counters.sol";

contract MessageBoard {
    using Counters for Counters.Counter;
    Counters.Counter message_ids;

    // Maps id's to messages
    mapping(uint => string) public messages;

    event Message(uint message_id, string message_uri);

    function postMessage(string memory message_uri) public returns(uint) {
        message_ids.increment();
        uint message_id = message_ids.current();
        messages[message_id] = message_uri;

        emit Message(message_id, message_uri);

        return message_id;
    }

    function getLatestMessage() public view returns(string memory) {
        uint message_id = message_ids.current();

        return messages[message_id];
    }
}
