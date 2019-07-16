pragma solidity ^0.5.0;

import "../node_modules/openzeppelin-solidity/contracts/validation/CappedCrowdsale.sol";
import "../node_modules/openzeppelin-solidity/contracts/distribution/RefundableCrowdsale.sol";
import "../node_modules/openzeppelin-solidity/contracts/emission/MintedCrowdsale.sol";
import "../node_modules/openzeppelin-solidity/contracts/ERC20/ERC20Mintable.sol";
import "../node_modules/openzeppelin-solidity/contracts/ERC20/ERC20Detailed.sol";

contract PupperCoin is ERC20Mintable, ERC20Detailed {
    constructor () public ERC20Detailed("PupperCoin", "PPY", 18) {
        // solhint-disable-previous-line no-empty-blocks
    }
}

contract PupperCoinCrowdsale is CappedCrowdsale, RefundableCrowdsale, MintedCrowdsale {
    constructor (
        uint256 openingTime,
        uint256 closingTime,
        uint256 rate,
        address payable wallet,
        uint256 cap,
        ERC20Mintable token,
        uint256 goal
    )
        public
        Crowdsale(rate, wallet, token)
        CappedCrowdsale(cap)
        TimedCrowdsale(openingTime, closingTime)
        RefundableCrowdsale(goal)
    {
        require(goal <= cap, "PupperCoin Crowsdale: goal is greater than cap");
    }
}
