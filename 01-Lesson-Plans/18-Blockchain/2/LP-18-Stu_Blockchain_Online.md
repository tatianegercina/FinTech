### 18. Students Do: Build a Blockchain Online (10 min)

Students will be repeating the blockchain online activity at their computers.

**Instructions:**

* [README.md](Activities/18-Stu_Blockchain_Online/README.md)

Send out the [Anders Blockchain Demo](https://anders.com/blockchain/blockchain.html) to the students.

Have the TAs circulate through the class and ensure that students are connecting blocks and rebuilding the chain.

### 19. Instructor Do: Blockchain Data Structure Review (5 min)

Ask the students the following questions:

  * How are the blocks linked together / What does the "chain" in blockchain mean?

    * **Answer**: Each block is linked to the previous by putting the last block's hash inside of it.

  * In a blockchain with 10 blocks, if you were to modify the 3rd block, how many would you need to re-mine?

    * **Answer**: 8 blocks, 3 through 10 need to be mined again

* Explain that this is the feature that makes blockchain transactions so "final" -- once a block is accepted by the network,
  it takes an enormous amount of energy to "roll a transaction back" since each block from the point of that transaction forward must be mined *again*, which quickly becomes mathematically infeasible.
