pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";
import "./ICryptoRight.sol";

contract CryptoRight is ICryptoRight {

    using Counters for Counters.Counter;

    Counters.Counter copyright_id;

    mapping(uint => string) public copyrights;

    mapping(uint => address) public copyright_owner;

    event Copyright(uint token_id, string reference_uri);

    event Transfer(uint token_id, address recipient);

    modifier onlyCopyrightOwner(uint token_id) {
        require(copyright_owner[token_id] == msg.sender, "You do not have permission to alter this copyright!");
        _;
    }

    function copyrightWork(string memory reference_uri) public {
        copyright_id.increment();
        uint id = copyright_id.current();

        copyrights[id] = reference_uri;
        copyright_owner[id] = msg.sender;

        emit Copyright(id, reference_uri);
    }

    function renounceCopyrightOwnership(uint token_id) public onlyCopyrightOwner(token_id) {
        copyright_owner[token_id] = address(0); // set to 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further.
    }

    function transferCopyrightOwnership(uint token_id, address recipient) public onlyCopyrightOwner(token_id) {
        copyright_owner[token_id] = recipient;
        emit Transfer(token_id, recipient);
    }

}
