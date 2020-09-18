pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";
import "../Resources/ICryptoRight.sol";

contract CryptoRight is ICryptoRight {

    using Counters for Counters.Counter;

    Counters.Counter copyright_ids;

    // @TODO: Implement the Work struct

    // @TODO: Implement the copyrights mapping

    // @TODO: Implement the Copyright Event

    // @TODO: Implement the OpenSource Event

    // @TODO: Implement the Transfer Event

    modifier onlyCopyrightOwner(uint copyright_id) {
        // @TODO: Check if copyright owner is equal to msg.sender
    }

    function copyrightWork(string memory reference_uri) public {
        // @TODO: Implement the copyrightWork function
    }

    function openSourceWork(string memory reference_uri) public {
        // @TODO: Implement the copyrightWork function
    }

    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // @TODO: Implement the copyrightWork function
    }

    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
        // @TODO: Implement the copyrightWork function
    }

}
