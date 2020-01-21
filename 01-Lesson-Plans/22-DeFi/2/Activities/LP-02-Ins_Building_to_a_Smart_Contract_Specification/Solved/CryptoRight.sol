pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";
import "./ICryptoRight.sol";

contract CryptoRight is ICryptoRight {

    using Counters for Counters.Counter;

    Counters.Counter copyright_ids;

    mapping(uint => string) public copyright_uri;

    mapping(uint => address) public copyright_owner;

    event Copyright(uint copyright_id, address owner, string reference_uri);

    event OpenSource(uint copyright_id, string reference_uri);

    event Transfer(uint copyright_id, address new_owner);

    modifier onlyCopyrightOwner(uint copyright_id) {
        require(copyright_owner[copyright_id] == msg.sender, "You do not have permission to alter this copyright!");
        _;
    }

    function copyrightWork(string memory reference_uri) public {
        copyright_ids.increment();
        uint id = copyright_ids.current();

        copyright_uri[id] = reference_uri;
        copyright_owner[id] = msg.sender;

        emit Copyright(id, msg.sender, reference_uri);
    }

    function openSourceWork(string memory reference_uri) public {
        copyright_ids.increment();
        uint id = copyright_ids.current();

        copyright_uri[id] = reference_uri;
        // no need to set address(0) in the copyright_owner mapping as this is already the default for empty address types

        emit OpenSource(id, reference_uri);
    }

    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
        // set to 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further.
        transferCopyrightOwnership(copyright_id, address(0));

        emit OpenSource(copyright_id, copyright_uri[copyright_id]);
    }

    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        copyright_owner[copyright_id] = new_owner;

        emit Transfer(copyright_id, new_owner);
    }

}
