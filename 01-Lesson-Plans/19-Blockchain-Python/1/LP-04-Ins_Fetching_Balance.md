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

Let's check the balance of our primary address that we've been using throughout class.

* Replace your address with an address you've been using on your local chains.

```python
w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")
```

This should return a number that matches the balance in your wallet.

Voila! Now it's time to actually spend some Ether from that address.

Ask the students:

* How might actually do this?

  **Answer**: By importing the private key!
