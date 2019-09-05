### 17. Instructor Do: Blockchain Data Structure (10 min)

Now that the students understand the fundamental cryptographic techniques that power the internet and blockchain tech,
let's break down the data structure of a blockchain and why the design is so secure.

Open up the [Anders Blockchain Demo](https://anders.com/blockchain/blockchain.html) and walk through the different fields.

Point out the matching "chain of hashes" located inside of each block:

![matching hashes](Images/blockchain-matching-hashes.png)

* Notice how the hash of the first block is actually inside of the second block

* This means that the hash of the second block is actually dependent on the previous

* Ask the students, "What were to happen if the first block was modified?"

  * **Answer**: The second block would be invalidated, since the first block's hash changed

Continuing with the first block, type some data into the data field, like "Alice sends Bob $10."

![blockchain data field](Images/blockchain-data.png)

* Explain to the class that the change from green to red represents a break in the chain

* This means that the hash first block has changed since we changed the data, so we have to rebuild the chain from this point all the way to the end.

Click `Mine` in the first block to change it green and to regenerate the hashes:

![mining](Images/blockchain-mining.png)

* Point out that we still need to mine each block going forward again, one at a time, chronologically
  in order to completely rebuild the chain.

Click on `Mine` in the second block to demonstrate.

![mining gif](Images/blockchain-mining.gif)

* Point out that each block is dependent on each other since the hashes are chained.

Now, it's time to have the students try it for themselves.
