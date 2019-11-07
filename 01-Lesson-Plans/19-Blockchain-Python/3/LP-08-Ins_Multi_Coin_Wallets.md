### 8. Instructor Do: Multi-Coin Wallets with BIP44 (10 min)

In this activity, you will demonstrate the multi-coin functionality of BIP44 and how it has become the "universal wallet" standard.

* Now that we can generate a tree of keys from a single master seed, wouldn't it be awesome to be able to use the same
  master seed for multiple coins as well?

* The BIP44 standard is what allows us to do just that! BIP44 is the standard that most "Universal Wallets" or "Multi-Coin Wallets"
  leverage. This is also the standard that exchanges use to generate your crypto addresses and keep track of customer balances and transactions.

Scroll back to the `Derivation Path` section in the BIP39 tool, then click the `BIP44` tab:

![BIP44](Images/bip44-tab.png)

Scroll down to the list of keys like before.

Point out:

* While these are all different keys than from BIP32, they are still mainnet Bitcoin keys.

* Let's change that by creating some testnet Bitcoin keys.

* The `Coin` number listed is `0` in the derivation path, as well as the `Coin` field under the `Purpose`.

Scroll up to the top, and change the `Coin` dropdown from Bitcoin to Bitcoin Testnet:

![BTC Testnet BIP44](Images/bip44-btc-testnet.png)

Navigate back down to the derived addresses. You should now see the same testnet keys we used earlier this week.

* Notice that the `Coin` number changed from `0` to `1` -- Bitcoin's mainnet is coin 0 and the BTC testnet is coin 1!

* Now, let's generate some Ethereum keys!

Scroll back up to the `Coin` dropdown and select `ETH - Ethereum` .

Back down at the derived addresses section, you should see a list of Ethereum addresses:

![ETH BIP44](Images/bip44-eth-derived.png)

Notice these are the same as used throughout class as well!

Point out:

* The derivation path now uses `60` as the coin number. This means that Ethereum was assigned coin number 60 in the standard.

* Since Ethereum uses the same addresses across main and test networks, these should be the same keys that we've been using since we started learning about blockchain!

Explain to the students that they may be wondering where the list of coins and their corresponding coin numbers come from, and how you might add yours in the future.

Navigate to the [SLIP44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) spec page.

Explain to the students that this is the sister-standard that contains the list of coin numbers and their corresponding blockchain.

![SLIP44](Images/slip44.png)

* This contains the data needed to get a coin registered onto this standard.
  New blockchains need to have a PR opened on this SLIP44 standard and other wallets will use this list for integration.

That was quite a lot, let's have the students get some practice generating keys for multiple coins!
