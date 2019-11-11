### 5. Instructor Do: Back to BIP32 (10 min)

Now let's actually generate some Bitcoin keys from this!

Back in the BIP39 tool, scroll down to the `Derivation Path` section and click the `BIP32` tab.

![BIP32](Images/bip32-tab.png)

Explain to the students:

* The BIP32 standard allows us to "derive" a tree of new Bitcoin keys from the master seed. BIP32 compatible wallets are also called HD wallets.

* This means that we can generate many addresses from a single seed, without having to create new wallets constantly and having to track their private keys.

Scroll down to the list of derived addresses:

![BIP32 Derivation](Images/bip32-derived.png)

Point out the `Path` column on the left. Explain to the students:

* This is the "derivation path" that is applied to the master seed. By applying this path to the master seed,
  the address and public/private keypair to the right is generated.

* By incrementing the derivation path by 1, you can generate a new address and keypair.

Ask the students:

* Why is this useful?

Allow them to answer, then explain:

* Since Bitcoin is UTXO native, we can generate a new address for every transaction.
  This allows us to make the accounting very easy.

* Because we own all of the keys anyway, we can sign the UTXOs that belong to each of the "child" keys and spend from them all simultaneously.

* Let's say you were a merchant selling goods. For every customer purchase, you can increment the path by 1 and generate a new address for that customer to pay you through.

Ask the students:

* Why might you want to do that?

  **Answer:** That way customers can't see your entire balance and purchase history!

  **Answer:** Accounting becomes much easier, as each address becomes a receipt of sorts containing that transaction only.

  **Answer:** Bitcoin is pseudonymous, not anonymous, so generating new addresses helps preserve privacy.

Now, time for the students to derive some keys of their own!
