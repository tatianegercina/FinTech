pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/ownership/Ownable.sol";

contract ArtToken is ERC721Full, Ownable {

  constructor() ERC721Full("ArtToken", "ART") public { }

  event Appraisal(uint token_id, string appraisal_uri);

  function registerArtwork(address owner, string memory token_uri) public returns(uint) {
        uint token_id = totalSupply();
        _mint(owner, token_id);
        _setTokenURI(token_id, token_uri);
        return token_id;
    }

    function newAppraisal(uint token_id, string memory report_uri) public {
        emit Appraisal(token_id, report_uri);
    }
}
