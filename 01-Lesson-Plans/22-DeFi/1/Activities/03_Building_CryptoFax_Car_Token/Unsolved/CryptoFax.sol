pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";

contract CryptoFax is ERC721Full {

    using Counters for Counters.Counter;

    constructor() constructor() ERC721Full("TokenName", "TKN") public { }

    Counters.Counter token_ids;

    struct Car {
      //Implement car struct
    }

    // Stores token_id => Car
    // Only permanent data that you would need to use in a smart contract later should be stored on-chain
    mapping(/* Iplement cars mapping*/) public cars;

    event Accident(uint token_id, string report_uri);

    function registerVehicle(/* Fucntion parameters */) public returns(/* Fucntion returns */) {
      //Implement registerVehicle
    }

    function reportAccident(/* Fucntion parameters */) public returns(/* Fucntion returns */) {
       //Implement reportAccident
    }
}
