# Multi-coin Python Wallet

This project contains a Python wallet that supports Ethereum and BTC testnet transactions. This uses the BIP44 standard, and leverages the following libraries:

- [`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive) BIP44 Command Line tool that supports 300+ coins

- [`bit`](https://ofek.github.io/bit/) Python Bitcoin library

- [`web3.py`](https://github.com/ethereum/web3.py) Python Ethereum library

To use the wallet, set an account like so:

`account = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])`

Then, send a transaction by doing:

`send_tx(BTCTEST, account, 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB', '0.001')`

The `coins` object contains a list of child wallets for each coin, in this case `BTCTEST` and `ETH`.

![wallet-object](../../Instructions/Images/wallet-object.png)

Here is an example `ETH` transaction on a local testnet:

![eth-test](../../Instructions/Images/eth-test.png)

Here is an example `BTCTEST` transaction on testnet3:

![eth-test](../../Instructions/Images/btc-test.png)