### 2. Instructor Do: Intro to BIP39 (Mnemonic Phrases) (10 min)

First, let's begin to explain how these wallets work.

* Explain to the class that just like how the blockchain community comes up with standards for how the chains are designed,
  standards for how crypto wallets work are also agreed upon!

* This is why we are able to use the same 12 word mnemonic phrase across Bitcoin and Ethereum.
  In fact, we can use it across many more blockchains than that!

Now, let's talk about how these mnemonic phrases we've been using.

* So far, we've been using English words as our crypto keys. How might this be possible?

* This is possible because of something called the BIP39 Standard.

* "BIP" means "Bitcoin Improvement Proposal" and in this case, BIP39 helps more than just Bitcoin.

* This standard comes up with exact lists of 2048 words per language like English, Spanish, Japanese, etc.
  as well as a formula that allows you to take a set of those words and generate private keys with them.

* That way, instead of having to remember your private key (which is a long and confusing alphanumeric string),
  or worrying about writing it down correctly, you can remember the exact words that generate the master key/master seed instead,
  and securely convert back and forth from seed to mnemonic phrase.

Now, open up IanColeman's BIP39 online tool [here](https://iancoleman.io/bip39/).

Tell the students to ignore most of the things you see here for now, and pay attention to a couple fields first.

Paste your Instructor Mnemonic into the `BIP39 Mnemonic` field to allow the tool to derive addressess:

![mnemonic conversion](Images/mnemonic-convert.png)

Point out the `BIP39 Seed` field that is generated.

* Explain to the class that this is the "master seed" or "master key" that can be used to derive any of the rest of the keys we'd need/want to use.

* The mnemonic phrase is converted from our English language back to the random numbers
  and letters that make up crypto keys. Great! Can you imagine having to write down the
  master seed instead of just the words?

Now, it's time to have the class convert their mnemonics to a master seed.
