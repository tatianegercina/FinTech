## 19.2 Lesson Plan: Bit, A Python Library

### Overview

Today's class students will begin to interact with blockchains using Python libraries `web3.py`, `bit`,
and will also learn how BIP44 works in preparation for the homework.

The goal of today's class is for the students to understand how to talk to Ethereum and Bitcoin nodes using Python,
and to understand how wallets work across the blockchain ecosystem.

### Class Objectives

By the end of the unit, students will be able to:

* Define Unspent Transaction Output (UTXO) (data structure behind Bitcoin-based projects).

* Explain the how UTXOs in Bitcoin transactions allow for multi-input and multi-output transactions.

* Send Bitcoin transactions on bitcoin’s test network.

* Explain the difference between Ethereum and Bitcoin's account models (UTXOs vs Nonces).

- - -

### Instructor Notes

* Before class, ensure that you have funded a Bitcoin testnet wallet using the same mnemonic you've been using throughout the course.
  You may need to send out test bitcoins to students that did not successfully request them from a faucet previously.

* If you can prefund multiple testnet addresses by splitting up what the faucet sends you into multiple addresses,
  you can use these to distribute to students as prefunded private keys if absolutely necessary to keep the class moving
  (for instance, the transaction doesn't confirm between the beginning of class and after the break).

* Use an offline version of the [BIP39 Conversion tool](https://github.com/iancoleman/bip39/releases) to derive your BTC testnet address if necessary.

* Ensure that you have the `bit` Python library install via `pip install bit`.

- - -

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

Welcome students back and refresh a bit on some blockchain architecture.

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Ask the students the following questions:

* What is Ethereum?

  **Answer**: A global computer powered by blockchain technology.

* Why is Ethereum important?

  **Answer**: It makes a decentralized computing and money system available to everyone, powered by everyone.

* Now let's take this back a bit, what was the first blockchain?

  **Answer**: Bitcoin!

Today we're going to talk about the differences in the architectures of Bitcoin and bitcoin-based blockchains versus
Ethereum-based blockchains.

* Can anyone describe a couple differences between Bitcoin and Ethereum?

  **Answer**: Ethereum is "Turing complete" meaning it is capable of general computing.

  **Answer**: Bitcoin supports multiple inputs and outputs in transactions (more on this in a bit).

  **Answer**: Ethereum uses nonces to count transactions sent from an account.

  **Answer**: Ethereum uses a single account system, Bitcoin uses a UTXO system (more on this in a bit).

  **Answer**: Bitcoin supports multisig natively versus needing more complex and expensive smart contracts (more on this later today).

Reassure the students that we will go into detail about the pros and cons of Bitcoin versus Ethereum,
and the pros and cons between the architectures.

### 2. Instructor Do: Architecture Overview (5 min)

Now, let's give a quick comparison between the architectures. Navigate through the slides to help illustrate your points.

Ask the students:

* If Ethereum exists, why is Bitcoin still the number one crypto?

Have the students ponder for a bit, have some students give their ideas.

Then explain:

* Even though Ethereum is quite a bit more capable functionally than Bitcoin, architectures designed for general computing
  are more expensive to use.

* Bitcoin's architecture (and thus, all of its derivatives) is designed for complex payments on the natively
  core layer of the blockchain, and can get them done for less computational effort than Ethereum.

* In the case of Ethereum, you'd have to write smart contracts to do many of types of transactions that Bitcoin can do natively,
  which can end up costing more gas/computational effort.

* Ethereum very well may take over as the main cross-border payments network, but for now, Bitcoin is still the leader in the space.

Ask the students:

* Why might we want to learn about Bitcoin and its architecture?

  **Answer**: Bitcoin's payment system is designed for complex transactions, natively.

  **Answer**: We won't have to write smart contracts for many types of payments.

  **Answer**: It is the number one cross-border cryptocurrency, and is still being upgraded.

  **Answer**: There may not be "one chain to rule them all." A payment-focused network can co-exist with a computing-focused network.

Now, let's start learning why Bitcoin is still a top player, and why it might stay that way for longer than you'd think.

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

### 5. Instructor Do: UTXOs Explained (15 min)

Continue through the slideshow to help illustrate your points.

Ask the students the following question:

* What mechanism allows us to send to multiple addresses in one transaction?

  **Answer:** Unspent Transaction Outputs, aka UTXOs.

Explain to the students that Unspent Transaction Outputs (UTXOs) are the digital equivalent of "change" in a transaction.

* For example, if you have a $20 dollar bill, and you are trying to buy an item for $10, you can't simply rip the bill
  in half and hand the other half to the merchant. The merchant must give you a $10 bill in return as change.

* Bitcoin treats balances as sets of change that can be owned by different private keys. To calculate your
  wallet's balance, you simply sum up all of the UTXOs that your private keys own, much like counting the bills and coins stored
  in your physical wallet.

![Testnet Funding account](Images/utxo-testnet-funding-account.png)

This is a screenshot of a transaction was sent from the bitcoin testnet faucet,
to a freshly generated address.

* On the left, you see `1 input consumed` that takes about 92 test bitcoins stored in a UTXO owned by the faucet's key and uses it as an input to the transaction. Notice the address starts with `2N5YL5`.

* On the right, you see the transaction create "change" from the initial UTXO.

* Ignoring the top bubble on the right, you see `0.03349844 BTC` sent to the freshly generated address starting with `mhrswdPN4`. This means that now that address can spend
  the `~0.0334 BTC` freely.

* Now, if you look back at the top bubble on the right, you will notice that BTC is being
  sent back to the faucet's address. This is the leftover change that goes back to the faucet.

* You can prove this by subtracting the `0.03349844 BTC` from the `92.87116596` from the original UTXO that the faucet spent.

* Now, the faucet has a new UTXO with the value of `92.83749753 BTC` in their wallet, and the new wallet has a UTXO with `0.03349844 BTC` to spend.

Ask the students:

* What is the point of having UTXOs?

  **Answer:** It allows you to do more complex accounting and treats the bitcoins as individuals, versus a simple balance.

* What does having multiple outputs enable?

  **Answer:** You can send to multiple people in one transaction.

* Now, can you have multiple inputs in a transaction?

  **Answer:** Yes, you can!

* What would a multi-input transaction allow you to do?

  **Answer:** You could spend from multiple addresses/wallets at the same time!

* How would you do this?

  **Answer:** By collecting your UTXOs and signing them with their designated private keys.
  As long as all of the inputs are correctly signed, the transaction is good to go!

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

### 8. Everyone Do: Installing Bit and checking balances (10 min)

In this activity, you will lead the class in installing the `bit` Python library and fetch account balances.

First things first. Have everyone install `bit` like so:

```bash
pip install bit
```

Now, open up a new Python file in your workspace. Have the class do the same.

We will need to refer to our (funded) testnet private key that we prepared earlier. Ensure everyone has that ready.

Next, we need to import the library in our Python file:

```python
from bit import wif_to_key
```

This will allow us to work with our testnet private key.

* WIF means "wallet import format" -- it's a special format bitcoin uses to designate the types of keys it generates.

Now, we can initialize the key in an object like so:

```python
key = wif_to_key("cQpxiiQHueFJgK3EaHKvDqAE7cm8gWKMrSj3ZPMMHkDr7v5gbkQW")
```

* By using the `wif_to_key` method, we convert our private key into an object that we can work with easily to sign and send transactions.

Now, we can check our balance like so:

```python
key.get_balance("btc")
```

* Several other fiat currency conversions are also available. We'll learn how to convert to them soon.
  In fact, we can use them in our send functions instead of having to convert them manually!

Fantastic! Most of the class should see a positive balance. If the transaction you sent to the students earlier is confirmed,
those students should also see a positive balance.

If they do not, and the transaction is still pending, it should confirm between now and the break.

### 9. Instructor Do: Review Bit (10 min)

Ask the students the following questions:

* What is a more secure way to import our private key?

  **Answer:** Environment variables

  **Answer:** Keystore

  **Answer:** Hardware wallet

* What does `bit` do as a library?

  **Answer:** It connects to Bitcoin networks and manages keys, much like web3.py works with Ethereum.

* What is does it mean for a transaction to have 6 confirmations?

  **Answer:** There are 6 blocks that were mined after the transaction was mined.
  This threshold makes it virtually impossible to reverse.

- - -

### 10. BREAK (15 min)

- - -

### 11. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to the class.

Have the students check their balances and ensure that everyone has test bitcoins to spend. Otherwise, you may need
to have students pair up, or give away a prefunded private key (if you made extra before class).

Ask the students:

* What allows us to construct a multi-output transaction?

  **Answer:** UTXOs!

Now it's time to send a multi-output transaction ourselves!
### 12. Instructor Do: Multi Output Transaction Demo (10 min)
Now it's time to demonstrate how a multi-output transaction is built.

**Files:**

* [Multi-Output Transaction](Activities/12-Ins_Multi_Output_Tx/Solved/multi-output-testnet-tx.py)

First, ask a couple of students to volunteer their addresses (who haven't already been sent to you).

Copy and paste these addresses into the address array.

The code should look like:

```python
from bit import wif_to_key

key = wif_to_key("")

# replace with student addresses
addresses = ["mn9CfkoXJpkCMkPbRcBfUphso7QaDmBmgz", "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"]

outputs = []

for address in addresses:
    outputs.append((address, 0.001, "btc"))

print(key.send(outputs))
```

* Explain that this program is looping through the list of addresses and adding the following tuple (3-tuple specifically) to the list of outputs in the format of:
  `(address, amount, denomination)`

* `Bit` is smart enough to take these outputs and build the full transaction out of them.
  Essentially we're telling `bit` what the outputs should look like, and it is building the transaction for us.

Now, copy and paste your private key into the `key` assignment as such:

```python
key = wif_to_key("cQpxiiQHueFJgK3EaHKvDqAE7cm8gWKMrSj3ZPMMHkDr7v5gbkQW")
```

Now, run the file. You should see an output like:

`134609e727703576bd4c80de550e00ea29a85af247ba1545d8bf41e00460378c`

* We send the transaction by passing the outputs to the `key.send` function.

* By printing the result of this, we get the transaction ID as the output.

Explore the transaction in a block explorer like [Blockcypher](https://live.blockcypher.com/btc-testnet/).

Alternatively, you can view [this existing transaction](https://live.blockcypher.com/btc-testnet/tx/134609e727703576bd4c80de550e00ea29a85af247ba1545d8bf41e00460378c/).

![multi output tx](Images/multi-output-tx.png)

See if the students can point out the output that has their bitcoins in it.

Point out the outputs on the right that correspond to the student wallets (they are the bubbles with the `0.001 BTC` sent).

Ask the students:

* Where is the rest of the BTC sent?

  **Answer:** Back to the original address, starting with `mhrsdwPN4`.

Now, time for the students to send their own multi-output transactions!

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

### 15. Instructor Do: Network Functions (10 min)

Let's demonstrate a couple more quick functions to get some more insight from our wallets.

First, open up a Python terminal and import the Bit library, as well as your key:

```python
from bit import wif_to_key

key = wif_to_key("cQpxiiQHueFJgK3EaHKvDqAE7cm8gWKMrSj3ZPMMHkDr7v5gbkQW")
```

Now, how would we get the balance of our key? With `bit`, it's easy:

```python
key.get_balance("btc")
```

* This gives us the balance of our key in BTC. It queries a bitcoin node and fetches the latest blockchain data.

* Now, what if we wanted to know the USD value of our BTC (assuming it's mainnet coins)?

Since we already fetched the latest data from the blockchain, we can easily convert the balance to USD:

```python
key.balance_as("usd")
```

You can also use this with `jpy`, `eur`, `cad`, and many other supported currencies available on the `bit` documentation.

Now, let's try fetching this wallet's transaction history:

```python
key.get_transactions()
```

This will output something like:

```python
['134609e727703576bd4c80de550e00ea29a85af247ba1545d8bf41e00460378c', '0ec8ed8433c5727c01ebf9320ba80d9f3abd71bde155a8a3cf3def69f1e95d74']
```

* Much like the `get_balance` function, this function pulls the latest blockchain data and stores it in this key object for later use.

* This will output an array of transaction IDs that correspond to the wallet's transaction history (aka, what this wallet has spent).

* Currently, this is the information Bit exposes to us, so we'd have to dive a bit deeper to get the details of each transaction. For now, we can use this for basic historical purposes.

What if we were to try and look at the unspent bitcoins (UTXOs) in a wallet, just for fun (or perhaps perform a more complex transaction that pulls UTXOs from multiple addresses that you own)?

We can do that too:

```python
key.get_unspents()
```

This will output something like:

```python
[Unspent(amount=3147244, confirmations=116, script='76a91419b4f0134fef7b5465bf301ae90b5ad1b7a33c0188ac', txid='134609e727703576bd4c80de550e00ea29a85af247ba1545d8bf41e00460378c', txindex=2, segwit=False)]
```

* Point out the `amount` field(s) and state that the sum of these amounts is the balance of the address.

* Explain that the `confirmations` field indicates how many blocks ago the UTXO arrived in this wallet.

Now explain to the students that with these functions you can emulate a lot of the functionality that a block explorer provides,
and the more you explore the `bit` library, the more you'll be able to build one yourself.

We are going to use it to build a multi-coin crypto wallet later, and these functions are critical to accomplishing that.

### 16. Students Do: Fetching Network Data (10 min)

Now, the students will practice using the functions you just demonstrated.

**Instructions:**

* [README.md](Activities/16-Stu_Fetching_Network_Data/README.md)

Have TAs circulate and ensure that students are not stuck and can fetch balances, transaction history, and UTXOs.

### 17. Instructor Do: Network Functions Review (5 min)

Ask the students the following questions:

* Where are we fetching this data from?

  **Answer:** Bitcoin nodes, in this case, publicly available ones that the `bit` library points to.

* Why would it be necessary to fetch blockchain data programmatically?

  **Answer:** You need the latest data in order to construct valid transactions.

* What is a transaction ID? How is it generated?

  **Answer:** It is a hash of the transaction that identifies it on the network.

* What value does `bit` provide?

  **Answer:** It abstracts all of the functions you'd need to interact with Bitcoin, keys, and includes currency conversions.

- - -

### End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
