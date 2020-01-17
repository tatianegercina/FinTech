pragma solidity ^0.5.0;

interface ICryptoRight {

    event Transfer(uint token_id, address recipient);

    function copyrights(uint token_id) external returns(string memory);

    function copyright_owner(uint token_id) external returns(address);

    function copyrightWork(string calldata reference_uri) external;

    function renounceCopyrightOwnership(uint token_id) external;

    function transferCopyrightOwnership(uint token_id, address recipient) external;

}
