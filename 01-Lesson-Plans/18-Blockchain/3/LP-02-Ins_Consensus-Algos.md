### 2. Instructor Do: Consensus Algorithms (10 min)

Time to explain the differences between some of the most popular consensus algorithms.

First, give these rhetorical questions to the class to ponder on:

* What gives blockchains their inherent value?

* Why are they so secure?

* This is what we will be learning today.

Explain to the students that:

* In a decentralized system, you cannot trust the participants in the network.
  It's a database that can be written to by anyone, which means special rules must be in place to prevent the database
  from being modified in a malicious way.

* This is where something called a "Consensus Algorithm" comes into play.

Break down the main purposes for a consensus algorithm:

* The main purpose of a consensus algorithm in blockchain is to get the entire network to agree on which block
  gets added to the chain next.

* A good consensus algorithm makes it so expensive to cheat, aka "roll back" the chain,
  that you'd make more just playing the game by the rules and just adding to it (aka mining) instead.

Explain that there are many consensus algorithms in development, but blockchain technology has reignited innovation in the
distributed computing field, so we'll discuss the more popular algorithms relevant to blockchain, starting with Proof of Work.

![proof of work](https://image.shutterstock.com/image-photo/bitcoin-cryptocurrency-mining-farm-600w-761471725.jpg)

* Proof of Work is the most popular algorithm in blockchain currently.
  This is what Bitcoin came out with, and where the term "mining" comes from.

* Proof of Work is the act of converting computing power that costs real-world energy and money into a block with transactions in it.
  The block is then submitted to the network for confirmation, and the block with the most "work" put into it gets added.

* This is a very secure algorithm, but the most expensive in terms of resources. This is its biggest criticism.

Ask the students:

* What is the biggest strength of Proof of Work?

  **Answer**: It's the most secure and decentralized consensus algorithm deployed today.

![proof of stake](https://image.shutterstock.com/image-photo/closeup-portrait-shocked-surprised-young-600w-207481837.jpg)

* Explain that Proof of Stake is very similar to PoW, only instead of contributing computational power, you "stake"
  some of the cryptocurrency for a period of time. Once passed a minimum staking interval, you can then submit blocks
  to the rest of the network for confirmation.

* "Staking" your coins means to lock them in a transaction that proves to the rest of the network that you are willing
  to "put your money where your mouth is" in order to be trusted to make blocks.

* The biggest criticism is the "nothing at stake" problem, where block producers have nothing to lose for producing alternative
  versions/histories of the blockchain. Some versions of this algorithm include "punishing" cheaters by "burning" their stake and not
  letting them get it back.

* Despite this concern, much of the blockchain community is moving towards different variations of PoS, including Ethereum.

Ask the students:

* What is the biggest strength of Proof of Stake?

  **Answer**: Similar security to PoW without the energy cost.

Explain to the class that there are many others to research, and give them a few extra examples to go along:

* Proof of Capacity - Using free hard drive space as a contribution to the network.

* Proof of Burn -- "Burning" or making some amount of coins un-spendable to act as a stake to the network.

The last, simplest, and least secure algorithm is called "Proof of Authority."

![proof of authority](https://image.shutterstock.com/image-photo/successful-team-leader-manager-ceo-600w-461317327.jpg)

* Proof of Authority allows only specific addresses to mine/produce blocks in the network.

* This is a centralized but cheap algorithm mainly used to power test networks.

* This algorithm is never used in production, mainnet blockchains, only for development, which is what we'll be using it for.

Ask the students:

* What is the biggest strength of Proof of Authority?

  **Answer**: Fast and cheap, good for test or development networks.
