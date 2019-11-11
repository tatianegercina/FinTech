### 13. Students Do: Sending a multi-output transaction (15 min)

In this activity, students will write their own Python program that will send a multi-output transaction.

**Instructions:**

* [README.md](Activities/13-Stu_Multi_Output_Tx/README.md)

**Files:**

* [multi-output-testnet.tx](Activities/13-Stu_Multi_Output_Tx/Unsolved/multi-output-testnet-tx.py)

Have TAs circulate and ensure that students are not stuck.

If students encounter issues, ensure that they have spendable UTXOs in their wallet.
This means checking their balance on a block explorer like Blockcypher and ensuring that the incoming transactions
are confirmed and the wallet has a positive balance.

### 14. Instructor Do: Bitcoin Transactions Review (5 min)

Congratulate the students on programming money!

Ask the students the following questions:

* What are some benefits the UTXO system provides?

  **Answer:** Treating the bitcoins as individuals enables more complex transactions.

  **Answer:** Can send to multiple addresses simultaneously in one transaction.

  **Answer:** Can spend *from* multiple keys simultaneously in one transaction.

* What are some of the cons of the UTXO system?

  **Answer:** It is slightly more complex to understand, otherwise it is very powerful.

* Can you send multiple transactions in parallel in UTXO based systems (i.e., two separate transactions being mined at the same time from the same wallet)?

  **Answer:** It depends. As long as you are spending different UTXOs in each transaction, you can send them at the same time.

  If you were to try to spend the same UTXOs in both transactions, the first one to be mined would succeed, and the second would be invalidated.

  It would be impossible to store both in the same block if they were spending the same UTXOs.

Now, let's get a little bit more detail from the transactions and wallets with `bit`.
