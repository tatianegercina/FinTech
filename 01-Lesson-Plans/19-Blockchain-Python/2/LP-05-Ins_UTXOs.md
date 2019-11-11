### 5. Instructor Do: UTXOs Explained (15 min)

Continue through the slideshow to help illustrate your points.

Ask the students the following question:

* What mechanism allows us to send to multiple addresses in one transaction?

  **Answer:** Unspent Transaction Outputs, aka UTXOs.

Explain to the students that Unspent Transaction Outputs (UTXOs) are the digital equivalent of "change" in a transaction.

* For example, if you have a $20 dollar bill, and you are trying to buy an item for $10, you can't simply rip the bill
  in half and hand the other half to the merchant. The merchant must give you a $10 bill in return as change.

* Bitcoin treats balances as sets of change that can be owned by different private keys. To calculate your
  wallet's balance, you simply sum up all of the UTXOs that your private keys own, much like counting the bills and coins stored
  in your physical wallet.

![Testnet Funding account](Images/utxo-testnet-funding-account.png)

This is a screenshot of a transaction was sent from the bitcoin testnet faucet,
to a freshly generated address.

* On the left, you see `1 input consumed` that takes about 92 test bitcoins stored in a UTXO owned by the faucet's key and uses it as an input to the transaction. Notice the address starts with `2N5YL5`.

* On the right, you see the transaction create "change" from the initial UTXO.

* Ignoring the top bubble on the right, you see `0.03349844 BTC` sent to the freshly generated address starting with `mhrswdPN4`. This means that now that address can spend
  the `~0.0334 BTC` freely.

* Now, if you look back at the top bubble on the right, you will notice that BTC is being
  sent back to the faucet's address. This is the leftover change that goes back to the faucet.

* You can prove this by subtracting the `0.03349844 BTC` from the `92.87116596` from the original UTXO that the faucet spent.

* Now, the faucet has a new UTXO with the value of `92.83749753 BTC` in their wallet, and the new wallet has a UTXO with `0.03349844 BTC` to spend.

Ask the students:

* What is the point of having UTXOs?

  **Answer:** It allows you to do more complex accounting and treats the bitcoins as individuals, versus a simple balance.

* What does having multiple outputs enable?

  **Answer:** You can send to multiple people in one transaction.

* Now, can you have multiple inputs in a transaction?

  **Answer:** Yes, you can!

* What would a multi-input transaction allow you to do?

  **Answer:** You could spend from multiple addresses/wallets at the same time!

* How would you do this?

  **Answer:** By collecting your UTXOs and signing them with their designated private keys.
  As long as all of the inputs are correctly signed, the transaction is good to go!
