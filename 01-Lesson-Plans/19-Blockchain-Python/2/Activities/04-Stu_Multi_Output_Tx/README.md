# Multi-Output Transaction

In this activity, you will send a multi-output transaction that sends `0.0003 BTC`
to at least 3 of your fellow students.

## Instructions

* Get at least 3 testnet bitcoin addresses from your neighbors. You'll also need to give away your primary testnet address.

* Using [this starter code](Unsolved/multi-output-testnet-tx.py), construct and send a transaction that sends `0.0003 BTC` to each of these addresses.

 * To do this, you will need to push a tuple with the following format to the outputs array:

 ```python
  ("address", 0.0, "denomination")
 ```

* Add the `send` function using `key.send`. Pass the outputs to this function and print the result.

## Challenge

* If time remains, try to change the denominations to USD.

* Try to fetch the transaction status using the transaction ID.

## Hints

* If you get stuck, take a look at the [Bit documentation](https://ofek.dev/bit/index.html).
