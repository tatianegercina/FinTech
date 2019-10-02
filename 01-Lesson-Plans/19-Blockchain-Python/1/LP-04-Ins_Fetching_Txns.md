### 4. Everyone Do: Fetching with Web3.py (15 min)

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
```

Now, let's start simple.

Simply run this function in order to pull transaction data:

```python
web3.eth.getTransaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
```

* As you can see, the `getTransaction` function takes a single parameter, the transaction hash or ID.

Voila! Now it's time to start actually working with our private keys!
