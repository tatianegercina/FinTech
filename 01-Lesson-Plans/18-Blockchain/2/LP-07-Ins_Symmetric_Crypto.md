### 7. Instructor Do: Symmetric Cryptography (10 min)

Open up the [Secretbox demo](https://tweetnacl.js.org/#/secretbox) from TweetNacl.js.
This tool demonstrates symmetric and asymmetric crypto, as well as hashing, signing, and verifying messages.

* Explain to the students that this JavaScript library contains all of the cryptography tools we need to get our job done.

Type an arbitrary message into the `Message` box:

![symmetric message](Images/symmetric-message.png)

* Reinforce that this message is a secret, and could be some corporate or health data that needs protecting

Generate a random symmetric key by clicking the `Random` button in the `Key` field:

![symmetric key](Images/symmetric-key.png)

* Explain that this key is just like using a password that you would think of on your own.

* In this case, we're going to let the tool generate a random key for us, as it will be formatted properly.

Generate a random nonce:

![nonce](Images/symmetric-nonce.png)

* Explain to the students that a "nonce" stands for "number used once."

* This means that you add a bit of randomness to your data, so that when you encrypt it, the result is unique.

* Without this, if you encrypt the same data with the same key, you'll get the same encrypted output every time.
  This adds to a hacker's ability to do something called "cryptanalysis" in which they analyze encrypted data in order
  to break the encryption. By adding randomness, this becomes much harder of a task.

Encrypt the message:

![symmetric encryption](Images/symmetric-encryption.png)

* Explain that the encrypted message can now be copied securely to a safe place.

Delete everything in the `Message` box, then click `Decrypt` again to demonstrate the process of decryption.
Only the key, nonce, and encrypted message are needed to decrypt back to the original message.
