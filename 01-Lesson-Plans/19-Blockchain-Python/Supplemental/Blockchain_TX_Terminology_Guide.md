# Blockchain Transactions Terminology Guide

This guide serves as an overview for the various concepts required to understand the notion of sending and receiving transactions over a blockchain network using virtual wallets.

## Terminologies

* What is encryption?

  **Answer:** Encryption is the process in which a message is encoded in a format that cannot be read or understood by an external party lacking the necessary credentials.

* What is symmetric encryption?

  **Answer:** Symmetric encryption is the simplest type of encryption that uses only a single key (a private/secret key) to both encrypt and decrypt information. As a result, the parties communicating via symmetric encryption must exchange the secret key so that it can be used in the decryption process, which is a security disadvantage compared to asymmetric encryption.

* What is an asymmetric key?

  **Answer:** Asymmetric encryption uses a key pair: a public and private key. As the name suggests, the public key is made freely available to anyone on the Internet while the private key is kept a secret by the end-user. Therefore, messages that are encrypted using the public key can only be decrypted using the associated private key, and messages that are encrypted using the private key can only be decrypted using the associated public key.

* What are the advantages vs. disadvantages of both types of encryption techniques?

  **Answer:** Symmetric encryption is the oldest and best-known technique for encryption; however, because of its use of only a single key (the private/secret key), there is the potential for a breach in security when exchanging the private key between two parties, especially over a vast network such as the Internet with possible eavesdroppers. In contrast, due to the use of a key pair in asymmetric encryption (public and private key), the private key is never exchanged and therefore is kept a secret at all times. Though as a result of the use of a key pair, asymmetric encryption is slower than symmetric encryption due to the increased processing power used to encrypt and decrypt messages.

* What is a hash?

  **Answer:** A hash value is a product of a function that converts an input of letters and numbers into an encrypted output of a fixed length. Hashing is one way to enable security during message transmission when the message is intended for a particular recipient only, ensuring that the message has not been tampered with, as doing so would generate a new hash value different from the originating hash value.

* What is a digital signature?

  **Answer:** A digital signature is a numerical value that is represented as a sequence of characters and is the product of ensuring the contents of a message have not been altered in transit (integrity), that the message was indeed sent by the sender (authentication), and that the sender cannot deny having sent the message (non-repudiation).

* How does a digital signature work?

  **Answer:** For example, a server could digitally sign a document and asymmetrically encrypt the message using its key pair (private key in this case) and create a one-way hash value. Clients with the associated public key would then be able to decrypt the message, and in doing so verify both the sender as well as the integrity of the message contents.

* What is a (blockchain) wallet?

  **Answer:** A blockchain wallet is a digital wallet containing a public and private key that is used to not only store cryptocurrencies, but also conduct secure transactions amongst other users via wallet addresses (hashed version of a public key). It is imperative that the private key for a digital wallet be kept safe, as losing it will be prevent a user from accessing their funds (no other way for decryption).

* What is BIP?

* What is BIP32?

* What is BIP39?

* What is BIP44?

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

Links:

* https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences - symmetric vs asymmetric
* https://support.microsoft.com/en-us/help/246071/description-of-symmetric-and-asymmetric-encryption - symmetric vs asymmetric
* https://www.instantssl.com/digital-signature - digital signature
* https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5 - digital signature
* https://www.investopedia.com/terms/b/blockchain-wallet.asp - blockchain wallet
* https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a - losing bitcoin wallet keys
* https://www.investopedia.com/terms/h/hash.asp - hash
