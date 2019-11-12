### 6. Students Do: Visualizing UTXOs (15 min)

In this activity, you will have the students explore different transactions using the Blockcypher block explorer.

They will pick apart the individual details of the transactions, including the UTXOs.

**Instructions:**

* [README.md](Activities/06-Stu_Visualizing_UTXOs/README.md)

### 6. Instructor Do: Review UTXOs (10 min)

Ask the students the following questions:

* What is a UTXO?

  **Answer:** Unpent Transaction Output

* What does it represent?

  **Answer:** Unspent bitcoins

* How do you calculate your balance with them?

  **Answer:** Sum up all of the UTXOs you own the private keys for.

* When are new UTXOs created?

  **Answer:** They are created when the transaction is sent.

* What happens when a UTXO is spent?

  **Answer:** You cannot use it anymore, only the new UTXOs created from the transaction output.

* Why is the UTXO model more powerful than Ethereum's accounting model?

  **Answer:** You can spend from multiple keys in one transaction, and construct
  much more complex transactions natively without smart contracts.

Now it's about time we start spending some of our own UTXOs. But first, we need
to learn the Python to do so. Time to install the `bit` Python library!
