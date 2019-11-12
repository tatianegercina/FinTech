# Visualizing UTXOs

In this activity, you will navigate through several transactions in a Bitcoin block explorer,
and decipher the different key parts, including the UTXOs.

## Instructions

* Navigate to the [latest BTC transactions on Blockcypher](https://live.blockcypher.com/btc/).

* Click on a transaction hash in the `Latest Transactions` section.

You should see a transaction visualized like the following:

![btc tx](Images/btc-tx.png)

* Identify the following fields in the transaction:

  * Transaction Inputs

  * Transaction Outputs (UTXOs)

  * Transaction Fee

* Identify the UTXO that matches the `Amount Transacted` field at the top.
  This is the new Unspent Transaction Output that can be spent by the destination address.

* Identify the address that the funds are ultimately being sent to.

* Repeat these steps with another transaction. See if you can decipher what is going on!

## Hints

* The destination address should be in the same bubble as the UTXO that matches the `Amount Transacted`.
