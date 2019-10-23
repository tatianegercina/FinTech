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
