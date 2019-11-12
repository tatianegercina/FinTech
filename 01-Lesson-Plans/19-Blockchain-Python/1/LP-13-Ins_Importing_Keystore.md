### 13. Everyone Do: Importing Keystore Accounts (15 min)

Now, let's say we wanted to send a transaction from the account stored in a keystore.

We'll need to import the key in a different way.

**Files:**

* [main.py](Activities/13-Ins_Importing_Keystore/Solved/main.py)

Continue using the keystore that you created earlier in class.

Let's also continue in the same `main.py`. We need to import a couple of modules to securely decrypt the keystore.

Add this to the top of the file:

```python
from pathlib import Path
from getpass import getpass
```

* `getpass` is a library that allows us to ask for a password in the command line securely. We'll use this to get the keystore password later.

Now, we'll need to add the following code to pull the keystore, prompt for a password, decrypt the key and convert to and `Account` object.

Add the following code after the first account assignment:

```python
with open(Path("./keystore")) as keyfile:
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

with open(Path("./keystore")) as keyfile:
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
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
```

Ensure that all of the students are caught up to this point.

We can verify the second account was properly imported by running the following:

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
