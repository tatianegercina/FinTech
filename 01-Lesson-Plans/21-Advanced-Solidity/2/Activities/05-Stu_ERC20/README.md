# Building an ERC20 token with OpenZeppelin

In this activity, you will build an official ERC20-compatible version of the `ArcadeToken` using the OpenZeppelin libraries.

## Instructions

The starter code will contain the basics like file imports and boilerplate to save you time.

* Starting with the `onlyOwner` modifier, add a `require` that checks to see if `msg.sender` is equal to the `owner` of the contract.

  * Leave the underscore `_` at the end of the function in order to tell Solidity how to return to the function that calls the modifier.

* For the constructor function's definition, perform the following:

  * Pass in the variables that ERC20Detailed expects, which are `string name`, `string symbol`, and `uint decimals`. Use the following values:

    * `"ArcadeToken"` for the first parameter.

    * `"ARCD"` as the second.

    * `18` as the third. This is setting our token's `decimals` variable to be the same as Ethereum, which is `18` decimal places.

    * The constructor call should look something like `ERC20Detailed("TokenName", "TKN", 18)`

* Within the constructor, set `owner` to be the `msg.sender`. Then, call the internal `_mint` function and give the `initial_supply` to the `owner`.

* In the `mint` function, call the internal `_mint` function the same way, only pass the `recipient` and `amount` parameters to `_mint` instead.

* Finally, restrict the `mint` function only to be called by the owner by adding `onlyOwner` to the function's modifiers. Since the only modifier is `public`, you can add `onlyOwner` after `public`.

## Hints

* It can be helpful to bring up the OpenZeppelin documentation for the [ERC20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) in order to help remember the function names and parameters available.

* Scrolling down to the [ERC20Detailed](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#ERC20Detailed) section will give you more details about the extension contract.
