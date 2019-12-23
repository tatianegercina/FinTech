# ERC20Mintable Token Design

In this activity, you will build a mintable ERC20token and prepare it for a crowdsale.

## Instructions

* Open the example contract [ArcadeTokenERC20](Activities/06-Stu_ERC20Mintable_Token_Design/Unsolved/ArcadeToken.sol)

* From the OpenZeppelin libraries, use ArcadeToken to extend ERC20, ERC20Detailed, and ERC20Mintable. Your contract should look something like

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
}
```

## Challenge

* If time remains, try calling your ERC20 mintable token contract with different parameters, such as `name`, `symbol`, and `initial supply`.

## Hints

* In case you need some help, you can refer to the [OpenZeppelin Documentation page](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) on ERC20 tokens.
