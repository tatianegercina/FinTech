### 3. Students Do: Wallet Check (10 min)

In this activity, students will ensure that they have funded their wallet (using their mnemonic phrase and the BIP39 tool)
with testnet bitcoins, and prepare their testnet bitcoin private key.

For the students that were unable to request tokens for any reason before class, they will be instructed to send you a bitcoin test address.
**You will need to have testnet bitcoins ready in your instructor wallet for this activity.**

Using the Python program below, you can paste each student's testnet address into the designated array
the script will send a multi-output transaction that funds all of the addresses with `0.001 BTC` simultaneously.

By bundling into a single transaction, we do not have to wait for multiple transactions to confirm in the blockchain.
We can guarantee that once this transaction completes, every student will be funded at once, without having to wait for others to confirm.
The test network may be slow at times, so this is our best option.

Later today, we will show students how to perform this method.
But first, send out the instructions too all students and have the students prepare their keys using the BIP39 tool.

**Instructions:**

* [README.md](Activities/03-Stu_Wallet_Check/README.md)

**Files:**

* [multi-output-tesnet-tx.py](Activities/03-Stu_Wallet_Check/Solved/multi-output-testnet-tx.py)

Once the students have prepared their testnet address and private keys, we can move on.

### 4. Instructor Do: Wallet Check Review (5 min)

Ask the students:

* Notice that we were able to send to multiple addresses in one transaction. Can we do this with Ethereum? If so, how?

  **Answer:** We would have to write a smart contract to do this, which would be more computationally expensive.

* Why is it better to have this functionality native in the bitcoin core blockchain?

  **Answer:** It is computationally less expensive, thus can scale cheaper than a smart contract.

* Would it be possible for Ethereum to do this natively?

  **Answer:** Possibly, but it would require significant architecture changes.
