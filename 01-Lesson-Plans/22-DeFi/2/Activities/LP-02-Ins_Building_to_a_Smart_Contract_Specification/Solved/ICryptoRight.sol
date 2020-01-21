pragma solidity ^0.5.0;

interface ICryptoRight {

    event Copyright(uint copyright_id, address owner, string reference_uri);

    event OpenSource(uint copyright_id, string reference_uri);

    event Transfer(uint copyright_id, address recipient);

    function copyright_uri(uint copyright_id) external returns(string memory);

    function copyright_owner(uint copyright_id) external returns(address);

    function copyrightWork(string calldata reference_uri) external;

    function openSourceWork(string calldata reference_uri) external;

    function renounceCopyrightOwnership(uint copyright_id) external;

    function transferCopyrightOwnership(uint copyright_id, address new_owner) external;
}
