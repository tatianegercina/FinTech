# Building an ArcadeToken with a Mapping

In this activity, you will leverage the `mapping` data structure to build an `ArcadeToken` smart contract.

This will allow you to collect Ether in exchange for `ARCD` tokens that users can spend at your Arcade (or any other business you can think of)!

## Instructions

* Open up Remix, and create a new contract called `ArcadeToken.sol`. You can also use this [starter file](Unsolved/ArcadeToken.sol).

* After you define and name your contract `ArcadeToken`, add the following variables:

  * A `address payable` called `owner`. Set this to `msg.sender`. Since this is only called once during the deployment, you will become the contract owner.

  * A `string` called `symbol`. Set this to `ARCD` and make sure that it is `public`. This will allow wallets like MetaMask to recognize your token's symbol/ticker.

  * Set an `exchange_rate` variable to equal the number of tokens to be distributed per `wei`. Make sure the variable is a `uint public` type!

* Next, it's time to add the most important data structure, the `mapping`:

  * Create a new `mapping` that pairs `address` to `uint`. Name this variable `balances`.

* Now, add a new function that is a `public view` that `returns(uint)` called `balance`:

  * This function should fetch the balance of `msg.sender` by accessing the `balances` mapping, using `msg.sender` as the index/selector/key.

* Add a new `transfer` function that accepts `address recipient` and `uint value` as parameters:

  * In this function, subtract `value` from the balance of `msg.sender` in the `balances` mapping.

  * Then, add the `value` to the `recipient` balance in the mapping.

* Customers will now need a way to purchase new `ARCD` tokens! Add a `public payable` function called `purchase`. It does not need any parameters. Within the function:

  * Calculate a new `uint` called `amount` by multiplying `msg.value` with the `exchange_rate`. This will calculate the number of tokens to distribute.

  * Next, add the `amount` to the balance of `msg.sender`.

  * At the end of the function, transfer the `msg.value` to the `owner` address. (Remember, `owner` must be set to `payable` to call `.transfer` on it)

* Finally, since you as the Arcade owner will need to create new tokens when you need to, add a new function called `mint`:

  * Use the same parameters as the `transfer` function you defined earlier.

  * At the beginning of the function, `require` that the `msg.sender` is equal to `owner`. Make sure to put an error message in the `require`.

  * Then, simply add the `value` you'd like to the `recipient` address' balance in the mapping.

* Test out your contract by deploying and calling the functions that Remix exposes. Try minting some tokens for yourself, then sending them to another address!

* Celebrate the fact that you can now build out these not-so-magical tokens everyone has been talking about! You can extend these contracts to do anything you'd like. You can now create complex systems of value, that are customized to any use case!

## Challenge

* If time remains, try to convert the hardcoded variables to a constructor format to allow for this contract to be reused.

## Hints

* Remember, a mapping associates one data type to another. By pairing `address` to `uint`, we can track balances.

  * For example, `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333` is what the data might look like in contract storage.

* For more details about how mappings work, visit the [Solidity Documentation](https://solidity.readthedocs.io/en/v0.5.13/types.html#mapping-types).

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
