# Blockchain FAQ

<details><summary>What is Blockchain?</summary><br>

A blockchain is a type of database that stores an ever-growing list of records, called blocks, that are linked together cryptographically with hashing. Hashing, though similar to encryption is fundamentally different in that it cannot be decrypted - it is a one way scrambling of a message to produce a unique string of characters. This hash string is what links each list of records to the one previous.

The lists of records (blocks), are stored in a distributed manner, meaning that exact copies of all records are stored across all machines (called nodes) that access the network. Combined with hashing, this makes the blockchain extremely trustworthy, as the records are very difficult to alter. Not only does the hashing form a layer of protection, but even if one record is changed, because there are so many duplicates, its easy to prove that the information was altered.

<img src= Images/BlockChain_info.png width=800>

</details>
<details><summary>Why do we need blockchain?</summary><br>

We need blockchain because It solves the fundamental problem of trust between organizations and their affiliated parties, eg (Citizens, Customers, Vendors).

This is achieved thanks to the methodologies in **The Five Pillars of Blockchain**:

<blockquote>
<details><summary>Open</summary><br>

- Openness means that the system is designed to incentivize users to keep it open. The internet is an example of this - it is built on open protocols that anyone can learn and contribute to.

  - Anyone can access the source code and create a project from it, therefore developer access is high.

  - Anyone can access the chain and participate in the ecosystem.

  - Anyone can access the services the blockchain offers.


</details>
<details><summary>Borderless</summary><br>

- Borderless means the network is completely without geographical or political borders.
- To be borderless, the network needs to be decentralized. This means there is **no** central party that holds control of the network.
- Since the blockchain is synchronized onto every device that helps maintain it (called nodes), it lives everywhere.

</details>
<details><summary>Neutral</summary><br>

- Neutral means that the protocol does not discriminate against any user, whether human or machine.

- The blockchain is agnostic to users, regardless of political or social status, or geographic location.

- Open blockchain networks are also governed in a neutral fashion, with many using the blockchain itself for voting on the next network upgrades.
</details>
<details><summary>Censor Resistant</summary><br>

- Decentralized Blockchains are highly resistant to censorship and authoritarian control.

- This means that people suffering in nations that have high censorship can still find a way to use these systems to reach out and to bypass the oppression.

- For example:

  - Blockchain is being used currently around the world to avoid censorship or hyperinflation in many countries.

  - It has been said that blockchain and crypto can be seen as an insurance policy against a dystopian future.

  - Money is often compared to a form of speech. These are systems where this form of expression cannot be censored.

</details>
<details><summary>Public</summary><br>

- Open/Public blockchains are separate from the state and thus well-suited for public affairs.

- Some Blockchains can be private - these are suited to military or government work, where confidentiality is required. This is at least until zero-knowledge proof technology that allows for total privacy on a public blockchain is further developed to scale.

- This separation of state and money is a first in history. It is similar to the separation of church and state to allow for religious freedom; only this allows for monetary freedom.

- These public systems are built by the people, for the people, and are governed by the people.
</details>
</blockquote><br>
</details>

<details><summary>If the blockchain is decentralized, where is it stored?</summary><br>

The blockchain is stored in many remote locations called **nodes**. These nodes are simply computers that log onto the network and store a copy of the blockchain. Anyone can join the network and become a node with their personal computer. This is one of the reasons why the Blockchain is considered open and neutral.

Some nodes are online all the time, constantly downloading new transactions. Others sync up to the system when they log on and update their records to include those newly added.

For more information on nodes, take a look at [this article](https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f).

</details>

<details><summary>What is cryptography and why is relevant to Blockchain?</summary><br>

Cryptography is the science of using math to secure data so that third parties cannot decipher it or tamper with it. There are many types of cryptographic functions, such as hashing, encryption, digital signatures, and other data integrity checks. Each serve a different specific purpose, and when combined together correctly, form highly secured systems.

</details>
<details><summary>What is a hash and why do I need it?</summary><br>

A hash is a one way function that provides a digital fingerprint of data. Hashing is a key component of security on the blockchain, as this is what is used to 'chain' each block (list of records) to the last block. These hashes must match or the block cannot be proven as trustworthy and added to the official blockchain (ledger or list of blocks/records).

A hash function takes an input of any length and turns it into a fixed length scrambled alphanumeric string - regardless of the input contents, or length of characters. The resulting hash cannot be decrypted, as hashing is a one-way function. A hash can be used as a "fingerprint" for any kind of data.

For example the following two input strings result in different output hash strings that are the same length:

### Hash #1
<blockquote>

input = `'Hashing is super fun'`<br>
ouput =  `'82197c1b5722865cf1a98a3a6edc1c35cad6264f2247d9b90713c40344e91722'`<br>
length = `64`
</blockquote>

### Hash #2
<blockquote>

input = `'Hashing is super fun!`<br>
output = `'1e56ea7198cfad7774adf89b32459914b6c165ba19d2e44f28f907384623d15b'`<br>
length = `64`

</blockquote>

Notice that even though we only changed the input very slightly, we got a completely different hash!

The same logic applies for any other type of data. If you download a piece of software from a website that provides the hash of the file, and want to verify that the file you downloaded was exactly what you expected, you could run the same hashing algorithm on the file to verify that you get the **exact** same hash as the website listed. Even if one single bit changed in the file you downloaded, the resulting hash would be dramatically different.
Though the inputs are different lengths and characters, the outputs are both 64 characters long.

Hashing algorithms are complex, but thankfully we don't have to write the algorithms themselves, as there are plenty that have alrady been generated that can be used. Python includes an in-built hashing library called hashlib that includes some of the most popular hashing functions.

For more on hashing, check out [this](https://www.investopedia.com/terms/h/hash.asp) *Investopedia* article.
</details>
<details><summary>What is a Public Key, Private Key and Nonce?</summary><br>

**Public Key** - A public key is a key that is provided publicly to others to use in conjunction with another person's private key to decrypt and encrypt messages securely.

**Private Key** - A private key is a key that is kept secret. It can be used in conjunction with another person's public key to encrypt and decrypt messages with assymetric cryptography or it can be shared with another person so that they might decrypt your symmetric cryptography message.

**Nonce** - A nonce is a number used once. It can be added to cryptographic methods to increase security by introducing an element of randomness.

The uses of these terms is explained in more detail in the next question: *What is the difference between Symmetric and Asymmetric Cryptography?*.

</details>

<details><summary>What is the difference between Symmetric and Asymmetric Cryptography, and how is it related to nonce and digital signatures?</summary><br>

Symmetric cryptography means "one key" to "one lock" -- hence the "symmetry." Asymmetric cryptography doesn't just use one key like symmetric, but now it splits up the key into a "keypair" -- a public key and a private key, or "two keys" to "one lock".

With symmetric cryptography, the private key is shared between the parties in need of the message. The key encrypts and decrypts the message.

Asymmetric cryptography uses a public key *and* a private key to encrypt/decrypt messages.

To **encrypt** and send a message:
-- The sender must have their own private key, and the _recipient's_ public key.

To **decrypt** a received message:
-- The recipient must have their own private key, and the _sender's_ public key

Using a nonce with this method can increase security by adding an element of randomness. The Nonce, _number used once_, is used to make the resulting encrypted message different regardless of the same input, which makes it harder to analyze the output for patterns. If employing the nonce method with your cryptographic algorithm, it would be required to regenerate the same results again later or to decrypt data properly.

Digital signatures are the use of a private key to digitally 'sign' a document. To sign a document digitally, one must use their private key to "sign" the data which produces a string of alphanumeric characters. This string is the "signature". The recipient of the document can then use the public key of the signer to verify that the signature and document was not tampered with.

To read more about digital signatures, click [here](https://www.instantssl.com/digital-signature) and [here](https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5).

</details>

<details><summary>What are consensus algorithms?</summary><br>

Consensus algorithms in blockchain are methods to allow the network to reach agreement (consensus!) on whether a block can be trusted and thus added to the chain. Because blockchains are decentralized, no one person can be trusted to make this decision, so concensus algorithms are used. These algorithms typically use some type of collateral structure to determine trustworthiness. For more information on consensus algorithms in general, check out [this article](https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm).

The three main types of consensus algorithms that we cover in class are:

<blockquote>

<details><summary>Proof of Authority</summary><br>

- This algorithm deviates somewhat from the decentralized nature of blockchains in that there are designated entities that validate the blocks. PoA is almost always used for test networks and not for production.
- With this algorithm, the entities put their reputation on the line as collateral and must typically be voted in.
- For more information on *PoA*, check out [this article](https://www.binance.vision/blockchain/proof-of-authority-explained).
</details>

<details><summary>Proof of Work</summary><br>

- Used by Bitcoin and many other well known Blockchains, *Proof of Work* was the first consensus algorithm used in a public blockchain, and is where the term *mining* originated.
- To malicously attack a blockchain using *PoW*, one would need to use 51% of the computational power that the network uses. This strongly disincentivizes attacking the network.
- With this algorithm, the entities put their computational resources on the line as collateral.
- For more information on *PoW*, check out [this article](https://en.bitcoin.it/wiki/Proof_of_work).
</details>
<details><summary>Proof of Stake</summary><br>

- Developed as alternative to the resource intensive *PoW* algorithm, this method validates blocks based on a monetized stake in the network.
- To malicously attack a blockchain using *PoS*, one would need to hold 51% of the monetary power that the network holds. This strongly disincentivizes attacking the network.
- With this algorithm, the entities put their cryptocurrency on the line as collateral.
- For more information on *PoS*, check out [this article](https://www.investopedia.com/terms/p/proof-stake-pos.asp).
</details>
</blockquote>
</details>
<details><summary>What 'puzzle' is the Proof of Work algorithm solving?</summary><br>

When a block (or collection of records), is 'mined' - meaning validated and added to the chain - a miner will have solved a very difficult mathematical puzzle to do so. With many puzzles, there is some bit of logic involved, however with bitcoin mining, the puzzle is completely random. Essentially the puzzle is solved by finding the Nonce that, when added to the hash of the block itself, will produce a **new** hash with a predetermined number of leading zeros.

Solving the puzzle of which nonce will produce a new hash with **n** number of leading zeros is based solely on trial and error. Because of this it can be quite time intensive to decipher. Large quantities of electricity and computational power are used. This is why the winner of the nonce lottery receives a block reward for solving the puzzle and is the basis for the *Proof of Work* consensus algorithm.
</details>


<details><summary>What is the difference between a node and a miner?</summary><br>

Both miners and nodes are computers. A computer can serve as both miner and node - however they perform different functions. A node is a computer that stores a copy of the blockchain. A miner is a computer that works to solve the puzzle that will allow the a block of transactions to be validated and added to the network of nodes.

To learn about mining, click [this link](https://www.bitcoinmining.com/).

To learn more about nodes, click [this link](https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f).

</details>

<details><summary>What is a digital Blockchain wallet?</summary><br>

A digital, or blockchain, wallet is simply an asymmetric keypair that act as "keys" to your funds that are on the blockchain. It also serves as a place where you can view and send transactions.

Much like a debit card does not hold your actual money, but the access to it, a blockchain wallet holds the access to your funds but not the actual funds. The actual funds live on the blockchain.

For more reading on blockchain wallets, check out these articles from [investopedia](https://www.investopedia.com/terms/b/blockchain-wallet.asp) and [uncoin](https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a).

</details>

<details><summary>What is a Block explorer and how do I use it?</summary><br>

A block explorer is a tool that allows you to search transactions on a particular blockchain. Just as you might use a search engine to search topics online, the block explorer allows you to search blocks on the blockchain. With a block explorer you can see various data about the block and drill down into the specifics. For example on Etherscan, a block explorer for Ethereum, you can find information such as:

* Block Height (block number on the chain)
* Transaction Hash
* From and To Address
* Entity that mined the block
* Block Reward
* Difficulty
* Gas

</details>

<details><summary>Where can I get a quick summary of Blockchain Terminology?</summary>

For a quick run down of all the terms we cover in Unit 18, check out [this terminology guide](Blockchain-Terminology-Guide.md).
</details>

## Helpful Links

<details><summary>Blockchain</summary>

* https://www.investopedia.com/terms/b/blockchain.asp
</details>

<details><summary>Nodes</summary>

* https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f
</details>
<details><summary>Blockchain Wallets</summary>

* https://www.investopedia.com/terms/b/blockchain-wallet.asp

* https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a
</details>
<details><summary>Digital Signature</summary>

* https://www.instantssl.com/digital-signature

* https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5
</details>
<details><summary>Hash</summary>

* https://www.investopedia.com/terms/h/hash.asp
</details>
<details><summary>Blockchain Mining</summary>

* https://www.bitcoinmining.com/
</details>
<details><summary>Consensus Algorithms</summary>

* https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm
</details>
<details><summary>Proof of Authority</summary>

* https://www.binance.vision/blockchain/proof-of-authority-explained
</details>
<details><summary>Proof of Work</summary>

* https://en.bitcoin.it/wiki/Proof_of_work
</details>
<details><summary>Proof of Stake</summary>

* https://www.investopedia.com/terms/p/proof-stake-pos.asp
</details>

## Additional Course Resources


* [Blockchain Installation Guide](blockchain-install-guide.md)

* [Blockchain Terminology Guide](Blockchain-Terminology-Guide.md)

* [Running a POA Blockchain](POA-Blockchain-guide.md)

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
