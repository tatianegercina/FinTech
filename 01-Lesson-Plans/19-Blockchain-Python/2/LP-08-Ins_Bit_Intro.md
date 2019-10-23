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

We can also get the USD equivalent value (if this were mainnet):

```python
key.get_balance("usd")
```

* Several other fiat currency conversions are also available.
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
