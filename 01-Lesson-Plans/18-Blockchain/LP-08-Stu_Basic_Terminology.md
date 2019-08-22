### 8. Student Do: Basic Terminology (10 mins)

For this activity, students will Google common terminology used in blockchain development.

Have the TAs circulate through the class and clarify definitions for students that are confused.

**Instructions:**

* [README.md](Activities/08-Stu_Basic_Terminology/README.md)

### 7. Instructor Do: Basic Terminology Review (10 mins)

Students will learn basic, common terminology that will enable them to navigate the blockchain space.

**Files:**

* [slides x-y]()

Navigate to the slides and define common terms:

![screenshot of hash](hash.png)

* Explain that a "hash" is a unique fingerprint of a piece of data.

* A hash function is one-way, which means that you cannot reverse a hash much like you can't reverse mixing paint.

* However, it is easy to run the hash function over the same data again to verify the result is the same.

* If you were to change a single bit of the input, you would get a completely different hash.
  This allows for something called "data integrity" which is a very important part of internet and data security as well as blockchain technology.

![screenshot of signature](signature.png)

* Digital signatures are used to mathematically prove ownership or authenticity of data.
  Once a file or message is signed, you can verify it was signed by a specific individual.

* If the signed message is modified, the signature will be invalidated.

* This means that if you were to sign a document, and the document was later modified, the signature would invalidate.
  You could then easily prove that the document was modified. This is not just used for documents, but secure internet communication as well.

* Ask the students "If a signed message is modified, what happens?"

  * **Answer** The message will be invalidated and you would know the message was modified

![screenshot of wallet](wallet.png)

* A digital wallet is simply a set of "keys" to your funds that are on the blockchain.

* This means that with a wallet, you can create and send transactions, as well as view your balance.

* You can also sign messages with your digital wallet to prove ownership or authenticity of something.

* A digital wallet is much like the debit cards in your own wallet, you use them to access funds in your account.
  Only in this case, the card is now a key, and the bank is now the blockchain.

![screenshot of transaction](transaction.png)

* "So what's a transaction then?"

* Explain that a transaction is simply a signed message that authorizes a movement of funds between two parties.

* It is essentially "I sign off on the movement of X amount of value from account A to account B" -- now that it is signed off, nobody can modify it.

![screenshot of node](nodes.png)

* A full node keeps a copy of the blockchain. It verifies every transactions signatures and throws out any that do not validate.

* If you wanted to send a transaction, you would send it to a node to keep track of. Nodes broadcast the transaction to
  their neighbors, until a miner comes along and finalizes the transactions.

* Nodes are enforcing **all** of the rules of the blockchain, thus they are a very important part of the security of the network.

![screenshot of miner](miner.png)

* A miner/block producer is a special type of node that is working to solve computations in order to finalize transactions.

* Miners take the pending transactions from the nodes they are connected to and put them into a block.

* Each miner races against each other to perform this process first, and the winner is rewarded by the network for its work.
  Then this race happens again and again for each new block in the chain.

Reassure the students that we will dive deeper into the mechanisms in which nodes and miners communicate with each other,
as well as the full lifecycle of a transaction from creation to being stored in a block.
