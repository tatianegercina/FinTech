## 19.1 Lesson Plan: Intro to Web3.py

### Overview

Today's class students will begin to interact with blockchains using Python libraries `web3.py`, `bit`,
and will also learn how BIP44 works in preparation for the homework.

The goal of today's class is for the students to understand how to talk to Ethereum and Bitcoin nodes using Python,
and to understand how wallets work across the blockchain ecosystem.

### Class Objectives

By the end of the unit, students will be able to:

* Explain the role of web3 in communicating with Ethereum nodes.

* Activate their Ethereum network (using cheat sheet).

* Use web3 to fetch data.

* Import a private key into web3.

* Use web3 to send transactions on their own Ethereum blockchain.

* Request testnet tokens from Bitcoin.

---

### Instructor Notes

* Before class, prepare to use the mnemonic phrase you have been using throughout the course, we will be extracting keys and addresses from it.

* Ensure that an ETH address from this mnemonic is prefunded in your custom chain.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1uvjogs9QdNzxzry7Y38QffEFtTZlAAV6IStk6kzAJ_Y/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [19.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=6b0987ef-966d-4ba5-8689-ab1e0124ac2a) Note that this video may not reflect the most recent lesson plan.

---

### 1. Instructor Do: Welcome Class (5 min)

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Welcome the students to today's class. Cover the agenda slides and then provide a blockchain architecture refresher.

Ask the students the following questions:

* What is a keypair?

  **Answer**: A set of public and private keys used in asymmetric encryption.

* What is a digital signature?

  **Answer**: A cryptographic technique used to ensure the integrity and authority of data.

* What is a transaction in the context of blockchain?

  **Answer**: A signed message that authorizes the transfer of funds from one account to another.

Explain to students that today, we are going to be talking to blockchains in our favorite language, Python.

Ask the class:

* What Python library might we use to talk to Ethereum nodes?

  **Answer**: web3.py

Wrap up the welcome with some encouraging or engaging language:

> Time to get excited! Let's dive into working with Web3!

### 2. Instructor Do: Intro to Web3.py (5 min)

Continue through the slides, introducing the concept of "Web 3.0" and the Python library.

![web 1.0](Images/web-1.0.png)

* Remember when websites looked like this?

* This was the first generation of the web. The screenshot here is from February 2000.

* Nowadays, we are used to very interactive sites that work really well and don't require the page to be re-rendered every time you click something.
  This is the Web 2.0 we use today.

![web 3.0](https://image.shutterstock.com/image-photo/man-switching-next-generation-internet-600w-1449537596.jpg)

* Now with Web 3.0, we refer less to the user experience, but to the infrastructure of the internet.

* In the current model, servers are highly centralized, websites can go down, and archiving information is a difficult task. For example, we all know how hard Wikipedia works to get you to donate.

* With the emergence of blockchains and other distributed technologies, we can build the Web 3.0 -- a decentralized web where sites like Wikipedia wouldn't struggle since we'd just store a local copy ourselves.

![web3.py](Images/web3.py.png)

* Web3.py is a library that gives us the ability to talk to Ethereum nodes in our favorite language, Python.

* Think of it like any other SDK you've used to talk to other APIs, only the API comes from an Ethereum node this time.

* Speaking of Ethereum nodes, let's get our networks started so we can start using this library.

### 3. Students Do: Activate Ethereum Network (10 min)

Students will now activate their local custom chains; they build the last unit.

Provide a checklist for the students with the commands necessary to start the chain, as well as a backup chain for students to use if something went wrong with theirs.

Circulate around with the TAs to ensure that everyone is able to start their networks. If any student cannot complete this, ask them to pair with a neighbor until they can troubleshoot their system during a break.

**Instructions:**

* [README.md](Activities/01-Stu_Activate_Network/README.md)

**Files:**

* ["puppernet" Backup Blockchain](../../../02-Homework/18-Blockchain/Solutions/puppernet.zip) -- Use this for students that do not have a functioning local blockchain.

### 4. Instructor Do: Review Networks (5 min)

Ask the students a few questions that they might have realized during the homework.

* What does the RPC port allow us to do?

  **Answer**: This exposes these Ethereum APIs needed to talk to our node.

Assure the students that if they don't know the answers to these next questions, it's totally okay:

* What is a `bootnode`?

  **Answer**: A special type of node that facilitates connecting to other nodes. It helps
  new nodes get connected quickly by providing a list of peers to connect to.

* Why can we use a regular node as a `bootnode`?

  **Answer**: A regular node still is connected to other nodes, so it can provide its peer list as well, even though it might not be as large.

Alright, that's enough architecture; for now, let's start fetching data from our blockchain!

### 4. Everyone Do: Fetching balance with Web3.py (15 min)

Time for us to start pulling transactions from the chain.

Everyone will code along together, ensure that students are keeping up with every step.

Create a new folder called `web3` then `cd` into it:

```bash
mkdir web3
cd web3
```

Make sure the Web3 library is installed via `pip`:

```bash
pip install web3
```

Get your Python dev environment ready and create a new Python file called `crypto.py`.

In this file, type the following:

```python
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
```

Now, let's start simple.

Simply run this function in order to pull transaction data:

```python
w3.eth.blockNumber
```

This should display the latest block number.

If students encounter an error at this stage, ensure that their local chains are properly running with the RPC port `8545` exposed.

Let's check the balance of our primary address that we've been using throughout the class.

* Replace your address with an address you've been using on your local chains.

```python
w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")
```

This should return a number that matches the balance in your wallet.

Voila! Now it's time to actually to spend some Ether from that address.

Ask the students:

* How might actually do this?

  **Answer**: By importing the private key!

### 5. Everyone Do: Importing Private Keys into Web3.py (15 min)

Explain that it's now time to import the private key of this address into Web3.py.

Show students how to extract the private key from the mnemonic phrases we've been using.

Open up MyCrypto, import the mnemonic, and select the first address:

![mycrypto import mnemonic](Images/mycrypto-import-mnemonic.gif)

Then, click on the dropdown at the top and select "Wallet Info," then click the eye icon
to reveal the private key:

![mycrypto private key](Images/mycrypto-private-key.gif)

Have the students catch up to this point and ensure everyone knows how to extract the private key.

Now, navigate back to your Python editor.

Define the private key in a variable. Your code should look like this at this point:

```python
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = "0x31938fae629c2e5f42c7c983dfba11a1b5122d005ba4ab43caaf59ad611bf734"
```

Ask the students:

* Can anyone tell what's wrong with this code so far?

  **Answer**: We have a private key directly in the code! That is a big no-no for security.

* Can anyone guess as to what solutions might exist out here to help us keep private variables more secure?

  **Answer**: Environment Variables!

Great, let's find a way to import this a more secure way.

Create a file called `.env` in the same directory. Have the class follow along.

In this file, define the private key in an environment variable as such:

```bash
PRIVATE_KEY=0x31938fae629c2e5f42c7c983dfba11a1b5122d005ba4ab43caaf59ad611bf734
```

Great! Explain to the class that this `.env` file should **never** be committed to any Git repo, or uploaded to any server. It should stay on your local machine **ALWAYS**.

In fact, we'll add it to a `.gitignore` just in case:

```bash
echo ".env" >> .gitignore
```

Ensure students are complete to this point.

Now, we need to import the key from the environment variable. Replace the `private_key` definition with the following:

```python
private_key = os.environ["PRIVATE_KEY"]
```

Then, `import os` at the top of the file:

```python
import os
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = os.getenv("PRIVATE_KEY")

print(private_key)

```

* If we were to run this code, we would print `None`, since the environment variable hasn't actually been loaded into the system.

* We can solve this problem by installing a pip module called `python-dotenv` to do this automatically.

Install `python-dotenv`:

```bash
pip install python-dotenv
```

Then, at the top of our [file](Activities/02-Ins_Importing_Private_Keys/Solved/main.py), we can auto-import the environment variables:

```python
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = os.getenv("PRIVATE_KEY")

print(private_key)

```

Have the students save and run this file. Ensure that the students are successfully printing their keys.

Now we're getting keys loaded in a much more secure way!
Congratulate the students on learning a bit of cybersecurity on top of all of their FinTech skills.

### 6. Instructor Do: Importing Keys with Environment Variables Review (5 min)

Ask the students a few questions about why we wrote the code the way we did.

* What is the point of environment variables?

  **Answer**: One reason is for having machine-specific variables; another is to keep sensitive data out of the code.

* Why not just keep the key in the code?

  **Answer**: Anyone who has access to the code can then spend the funds.

* What else might environment variables be used for?

  **Answer**: Helping setup deployment environments, developer environments, etc.

### 7. Everyone Do: Creating a Keystore (10 min)

Time to create a Keystore, a Keystore is an encrypted file that contains the private key to an account.

* Explain to the class that a Keystore is a more secure method of storing the keys long-term, but requires a password to decrypt/unlock.

Present the following scenario to the class:

* Suppose your sibling or other relative wants in on the action that is your new blockchain.
  They are begging you to send them some crypto, and now you feel you're ready to.

* Let's create a Keystore for your relative, so that we can send funds to their account later, with pure Python.

First, open up MyCrypto again, then select `Create new Wallet` at the left-hand side.

Click `Generate a Wallet`, then click `Generate a Keystore File`.

![mycrypto create keystore](Images/mycrypto-create-keystore.gif)

Have the class follow along, and have them all create a unique password for their relative's Keystore.

Instruct the class that they will be prompted to download their Keystore file. Tell the students to save the Keystore file into the same directory that their Python web3 code is in.

Students can optionally choose to save a paper wallet version of the Keystore for safekeeping, which includes the private key and address.

Ensure that all students have created a new Keystore and saved the file before continuing.

### 8. Instructor Do: Keystore Review (5 min)

Ask the students a few questions about Keystores:

* What is a Keystore?

  **Answer**: An encrypted file that contains some data, like a private key.

* Why use a Keystore instead of just a private key?

  **Answer**: The private key stays protected on the disk since it's encrypted.

* What type of cryptography does a Keystore use to encrypt a private key?

  **Answer**: Symmetric Cryptography! (The password is the symmetric key).

---

### 9. BREAK (15 min)

---

### 10. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to class, and have them get settled in.

Have the students prepare the address of the Keystore they created before the break by opening up MyCrypto,
importing the Keystore File, and entering the password:

![mycrypto import keystore](Images/mycrypto-import-keystore.gif)

Have the students copy the address given and keep MyCrypto open just in case.

* Get excited, because we're about to send a transaction to this address in pure Python!

### 11. Everyone Do: Sending Transactions with Python (15 min)

Now we will start the process of importing keys and sending transactions with Python.

**Files:**

* [main.py](Activities/03-Ins_Sending_Txns/Solved/main.py)

Continue in the `main.py` you've been working in.

Students that are running a PoA chain will have to use a special middleware function to support their chain.

Ask the students to raise their hands if the local chain they are using is using Proof of Authority.

For the students that raise their hands, have them add the following to their code:

Import the `geth` PoA middleware at the top of the code:

```python
from web3.middleware import geth_poa_middleware
```

Then, right after their `w3` definition, inject the PoA middleware:

```python
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
```

Their code should look something like this:

```python
import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

private_key = os.getenv("PRIVATE_KEY")
```

The students that are using Proof of Work locally do not need to follow these steps.

Now, we need to convert the private key into an object that we can use to sign transactions, as well as messages with.

Import the `Account` module from `eth_account` at the top of the file:

```python
from eth_account import Account
```

* This will allow us to pass a private key to the `Account` function to create an account object.

Next, add this to the end of the file:

```python
account_one = Account.from_key(private_key)
```

* We can use this object to sign transactions.

For example, we can print the address of the account as such:

```python
print(account_one.address)
```

Next, we need to create a function to create new transactions using a few parameters.

```python
def create_raw_tx():
    return {}
```

Have the students define the function to this point. We will return an object that represents an unsigned transaction.

Ask the students:

* What sort of parameters do we need to send a transaction?

  **Answer**: The account we are sending from.

Add the "from address" parameter as `account`:

```python
def create_raw_tx(account)
```

* What other parameters do we need?

  **Answer**: The recipient address we are sending to.

Follow the same pattern, adding `recipient` to the parameter list:

```python
def create_raw_tx(account, recipient)
```

Ask the students the same question and repeat the steps for the `amount` parameter.

The function definition should become:

```python
def create_raw_tx(account, recipient, amount):
    return {}
```

Ensure students have defined their functions to this point.

Now, let us take these parameters and arrange them in a way that aligns with a proper Ethereum transaction.

First, we need a way of estimating the gas, aka transaction fee, needed to send the transaction:

```python
def create_raw_tx(account, recipient, amount):
  gasEstimate = w3.eth.estimateGas({ "from": account, "to": recipient, "value": amount })
  return {}
```

* Explain that the `w3.eth.estimateGas` function takes the raw transaction parameters and estimates the price you will pay in fees. We can customize the algorithm used to estimate the fees later.

Add the following fields to the object in the `return` clause:

```python
def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }
```

Stop and wait for the class to catch up. Explain the following fields to the class:

* The `gasPrice` field contains a function call to get the network's `gasPrice`.
  In this case, it's likely going to be denominated in a unit called `Gwei`, which is equal to `0.000000001` Ether.

* The `nonce` field is the index of the latest transaction on the specified sender account.
  The first transaction sent from an account uses `0` as the `nonce`, and so on.

Voila! This is all we need to get the transaction signed and sent. Let's do that together!

Define a function called `send_tx` with the same exact parameters as `create_raw_tx`:

```python
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
```

Stop to explain:

* We create the raw unsigned transaction when we assign `send_tx`

* We then sign that transaction with the sending account's private key.

Now, all we need is to add the "send" piece:

```python
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()
```

* Explain that the `w3.eth.sendRawTransaction` function takes the raw, signed transaction bytes and sends it to the node you are connected to.

* This outputs the hexadecimal format of the transaction hash so that we can read it in our terminal and use it for later, versus printing the raw bytes.

With this function, we can now send a transaction.

Let's take our relative's new address that we generated from the Keystore and send them some crypto!

```python
send_tx(account_one, "0xa2C1eC996ceE707bB3c323f2D5D9334Ad51F835b", 3333333333)
```

This will return something like:

```python
HexBytes('0x53aab3d6b39642337c4ddf75463fa925d4796b913f91f4ec6a2d41c2cf17de0a')
```

This is the transaction ID. You can check the status of this transaction as such:

```python
w3.eth.getTransactionReceipt("0x53aab3d6b39642337c4ddf75463fa925d4796b913f91f4ec6a2d41c2cf17de0a")
```

This will return `None` if the transaction is still pending, otherwise, it will return something like:

```python
AttributeDict({'blockHash': HexBytes('0xff057860c590f610f18acadedb46505443019436c11c1498941b21c8d51b9922'), 'blockNumber': 972, 'contractAddress': None, 'cumulativeGasUsed': 21000, 'from': '0xc3879b456daa348a16b6524cbc558d2cc984722c', 'gasUsed': 21000, 'logs': [], 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'status': 1, 'to': '0xa2c1ec996cee707bb3c323f2d5d9334ad51f835b', 'transactionHash': HexBytes('0x53aab3d6b39642337c4ddf75463fa925d4796b913f91f4ec6a2d41c2cf17de0a'), 'transactionIndex': 0})
```

If students encounter an "invalid address" or "address checksum" error, then the way the recipient address was copied did not copy in the "uppercase" format.
To solve this, we can simply wrap the address in `Web3.toChecksumAddress(address)`. When Ethereum addresses are uppercase, they have a "checksum" that allows
the wallet software to check if the address is correct. Since the address wasn't copied in checksum format, we have to make sure that the address is exactly
the same, since the wallet can no longer verify if the address is valid, but will be able to send to it anyway.

Congratulations! You now know how to create and send transactions manually using pure Python!

### 12. Instructor Do: Sending Transactions Review (5 min)

Ask the students a few questions:

* Why is this useful to us?

  **Answer**: We can programmatically manage money and build next-generation applications.

* What cryptographic technique are we using when we sign a transaction?

  **Answer**: Digital signatures.

* How is the transaction ID generated?

  **Answer**: It is a hash of the transaction!

* Why do we need to estimate the gas?

  **Answer**: We need to calculate the fee needed to send this exact transaction, so miners will pick it up.

### 13. Everyone Do: Importing Keystore Accounts (15 min)

Now, let's say we wanted to send a transaction from the account stored in a Keystore.

We'll need to import the key in a different way.

**Files:**

* [main.py](Activities/04-Ins_Importing_Keystore/Solved/main.py)

Continue using the Keystore that you created earlier in class.

Let's also continue in the same `main.py`. We need to import a couple of modules to decrypt the Keystore securely.

Add this to the top of the file:

```python
from pathlib import Path
from getpass import getpass
```

* `getpass` is a library that allows us to ask for a password in the command line securely. We'll use this to get the Keystore password later.

Now, we'll need to add the following code to pull the Keystore, prompt for a password, decrypt the key and convert to and `Account` object.

Add the following code after the first account assignment:

```python
with open(
    Path(
        "./keystore/UTC--2019-10-09T00-24-47.260Z--a2c1ec996cee707bb3c323f2d5d9334ad51f835b"
    )
) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(
        encrypted_key, getpass("Enter keystore password: ")
    )
    account_two = Account.from_key(private_key)
```

* Explain to the students that we are reading the keyfile, then decrypting it with a password that we ask for in the command line using `getpass`.

* We use the `w3.eth.account.decrypt` function to actually perform the decryption, passing it the encrypted key and the password we get from the terminal.

The file should look something like:

```python
import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account

from pathlib import Path
from getpass import getpass

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

account_one = Account.from_key(os.getenv("PRIVATE_KEY"))

with open(
    Path(
        "./keystore/UTC--2019-10-09T00-24-47.260Z--a2c1ec996cee707bb3c323f2d5d9334ad51f835b"
    )
) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(
        encrypted_key, getpass("Enter keystore password: ")
    )
    account_two = Account.from_key(private_key)

def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()
```

Ensure that all of the students are caught up to this point.

We can verify that the second account was properly imported by running the following:

```python
print(account_two.address)
```

When we run `main.py` again, we will be prompted for the password. If it prints the address after, we win!

### 14. Instructor Do: Review Importing Keystores (10 min)

Ask the students a few questions comparing the two methods we just used to import keys:

* What is the benefit of importing the key this way?

  **Answer**: Since we securely ask for the password, we don't store any sensitive data that would allow the funds to be spent.

* Why not just store the password in an environment variable?

  **Answer**: The environment variables are stored in plaintext,
  which means anyone who has access to the machine has access to the keys.

* What are some other ways we might want to access private keys in the future?

  **Answer**: Hardware wallet via USB.

  **Answer**: Deriving the keys from the original mnemonic phrase.

* What is the benefit of creating the unsigned transaction first?

  **Answer**: We can prepare a transaction for signing, regardless of the method we use to import the keys.

* How might we use the `create_raw_tx` function to create a payment system?

  **Answer**: We can use this to request a transaction, filling in all of the necessary parameters,
  then all the user has to do is sign it.

### 14. Students Do: Sending Transactions from Keystore Account (10 min)

Now, challenge the students to use this program that they've written to send a transaction from `account_two` back to `account_one`.

**Files:**

* [main.py](Activities/05-Stu_Sending_Txns_Back/Solved/main.py)

Given the code we've written so far (provided above), this function should be all that is necessary to get the job done:

```python
send_tx(account_two, account_one.address, 333)
```

Have TAs circulate and assist any students that are having difficulties.

If the students are having trouble, remind them that they need to pass the entire `account_two` object
as the sending account, and passing just the `account_one.address` to the recipient field.

Remind students that they will need to send what is available in the balance.

### 15. Instructor Do: Review Sending from Keystores (5 min)

Ask the students the following questions:

* How might we check the transaction status?

  **Answer**: By calling `w3.eth.getTransaction` and passing the transaction hash.

* What were to happen if we were to try to send a transaction to ourselves?

  **Answer**: The transaction would still go through, but you'd pay the fee for it.

### 16. Instructor Do: Recap / Prepare for next class (10 min)

Congratulate the students on learning how to program money with Python.

Ask the students:

* Wouldn't it be cool to do this with other blockchains besides Ethereum?

Explain that we'll be learning how to perform this same process with the Bitcoin blockchain and by proxy,
all of its descendants (like Litecoin, Dash, Bitcoin Cash, etc.).

Send out the following instructions to have the students extract a Bitcoin testnet address and request tokens.

**Files:**

* [Acquiring Test Bitcoins](Activities/06-Ins_Recap/README.md)

Since it takes time for transactions to mine, we are having the students request the testnet coins early,
allowing time in between class for troubleshooting in case students have difficulties.

Before the next class, request some test bitcoins of your own to prepare to send to students that had difficulties.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
