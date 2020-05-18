pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract Message_Board{
    using Counters for Counters.Counter;
    Counters.Counter token_ids;

    // Maps ID's to messages
    mapping(uint => string) public messages;

    event Message(uint mesage_id, string message_uri);

    function postMessage() public returns(uint) {
        token_ids.increment();
        uint token_id = token_ids.current();
        message[token_id] = message_uri;

        emit Message(token_id, message_uri);

        return token_id;
    }
}
