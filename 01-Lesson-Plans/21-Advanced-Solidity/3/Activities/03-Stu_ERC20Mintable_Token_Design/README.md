# ERC20Mintable Token Design

In this activity, you will build a mintable ERC20token and prepare it for a crowdsale.

## Instructions

* Open the example contract [ArcadeTokenERC20.sol](Unsolved/ArcadeTokenMintable.sol).

* From the OpenZeppelin libraries, use ArcadeToken to extend ERC20, ERC20Detailed, and ERC20Mintable. Your contract should look something like:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
}
```

* Add a constructor that accepts `string memory name`, `string memory symbol`, and `uint initial_supply`. Pass the `name` and `symbol` variables to a secondary `ERC20Detailed` constructor, and hardcode the third `decimals` parameter to `18` (Ethereum's default).

* Within the constructor body, call the `mint` function and pass the `msg.sender` and `initial_supply`.

* Deploy your new contract on your local Ganache blockchain.

## Challenge

* If time remains, play around with changing the various contract parameters to create new and unique tokens.

## Hints

* In case you need some help, you can refer to the [OpenZeppelin Documentation page](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) on ERC20 tokens.
