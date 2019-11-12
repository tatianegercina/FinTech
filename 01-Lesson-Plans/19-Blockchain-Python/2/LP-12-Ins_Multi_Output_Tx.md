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
