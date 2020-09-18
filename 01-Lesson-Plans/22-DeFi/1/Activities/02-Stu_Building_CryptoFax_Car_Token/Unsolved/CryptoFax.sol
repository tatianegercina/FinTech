pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract CryptoFax is ERC721Full {

    constructor() ERC721Full("TokenName", "TKN") public { }

    using Counters for Counters.Counter;
    Counters.Counter token_ids;

    struct Car {
      //Implement car struct
    }

    // Stores token_id => Car
    // Only permanent data that you would need to use in a smart contract later should be stored on-chain
    mapping(/* Implement cars mapping*/) public cars;

    event Accident(uint token_id, string report_uri);

    function registerVehicle(/* Function parameters */) public returns(/* Function returns */) {
      //Implement registerVehicle
    }

    function reportAccident(/* Function parameters */) public returns(/* Function returns */) {
       //Implement reportAccident
    }
}
