### 6. Students Do: Deriving BIP32 Keys (HD Wallets) (10 min)

Have the students derive some Bitcoin keys and check their addresses.
They should all have empty balances, as we are generating mainnet Bitcoin keys, not the testnet keys used earlier this week.

**Instructions:**

* [README.md](Activities/06-Stu_BIP32_Derivation/README.md)

Have the TAs circulate and ensure that students are deriving the proper BIP32 keys.

### 7. Instructor Do: Review BIP32 (5 min)

Ask the students:

* Why is BIP32 useful?

  **Answer:** Since Bitcoin is UTXO native, we can generate a new address for every transaction.

  **Answer:** Allows for better and easier accounting on the blockchain.

  **Answer:** Preserves privacy by using new addresses for receiving money.

* What do you notice about the balance on these addresses?

  **Answer:** They are empty, and not the same as we used last week.

* Why are these addresses different from those we used last week?

  **Answer:** These are mainnet keys, which are different from Bitcoin's testnet keys.

Explain to the students that we will learn how to generate keys for different coins,
including Bitcoin Testnet and Ethereum in this next activity.
