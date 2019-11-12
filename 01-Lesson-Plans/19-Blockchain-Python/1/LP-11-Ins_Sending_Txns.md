### 10. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to class, and have them get settled in.

Have the students prepare the address of the keystore they created before break by opening up MyCrypto,
importing the Keystore File, and entering the password:

![mycrypto import keystore](Images/mycrypto-import-keystore.gif)

Have the students copy the address given and keep MyCrypto open just in case.

* Get excited, because we're about to send a transaction to this address in pure Python!

### 11. Everyone Do: Sending Transactions with Python (15 min)

Now we will start the process of importing keys and sending transactions with Python.

**Files:**

* [main.py](Activities/11-Ins_Sending_Txns/Solved/main.py)

Continue in the `main.py` you've been working in.

Students that are running a PoA chain will have to use a special middleware function to support their chain.

Ask the students to raise their hand if the local chain they are using is using Proof of Authority.

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

Now, we need to convert the private key into an object that we can use to sign transactions, as well as messages, with.

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

Now, lets take these parameters and arrange them in a way that aligns with a proper Ethereum transaction.

First, we need a way of estimating the gas, aka transaction fee, needed to send the transaction:

```python
def create_raw_tx(account, recipient, amount):
  gasEstimate = w3.eth.estimateGas({ "from": account, "to": recipient, "value": amount })
  return {}
```

* Explain that the `w3.eth.estimateGas` function takes the raw transaction parameters and estimates the price you will pay in fees.
  We can customize the algorithm used to estimate the fees later.

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
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
```

* Explain that the `w3.eth.sendRawTransaction` function takes the raw, signed transaction bytes and sends it to the node you are connected to.

With this function, we can now send a transaction.

Let's take our relative's new address that we generated from the keystore and send them some crypto!

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

Congratulations! You now know how to create and send transactions manually using pure Python!

### 12. Instructor Do: Sending Transactions Review (5 min)

Ask the students a few questions:

* Why is this useful to us?

  **Answer**: We can programmatically manage money and build next generation applications.

* What cryptographic technique are we using when we sign a transaction?

  **Answer**: Digital signatures.

* How is the transaction ID generated?

  **Answer**: It is a hash of the transaction!

* Why do we need to estimate the gas?

  **Answer**: We need to calculate the fee needed to send this exact transaction, so miners will pick it up.
