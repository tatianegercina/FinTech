### 7. Everyone Do: Creating a Keystore (10 min)

Time to create a keystore, an encrypted file that contains the private key to an account.

* Explain to class that a keystore is a more secure method of storing the keys long-term, but requires a password to decrypt/unlock.

Present the following scenario to the class:

* Suppose your sibling or other relative wants in on the action that is your new blockchain.
  They are begging you to send them some crypto, and now you feel you're ready to.

* Let's create a keystore for your relative, so that we can send funds to their account later, with pure Python.

First, open up MyCrypto again, then select `Create new Wallet` at the left hand side.

Click `Generate a Wallet`, then click `Generate a Keystore File`.

![mycrypto create keystore](Images/mycrypto-create-keystore.gif)

Have the class follow along, and have them all create a unique password for their relative's keystore.

Instruct the class that they will be prompted to download their keystore file. Tell the students to save the keystore file into the same directory that their Python web3 code is in.

Students can optionally choose to save a paper wallet version of the keystore for safe keeping, which includes the private key and address.

Ensure that all students have created a new keystore and saved the file before continuing.

### 8. Instructor Do: Keystore Review (5 min)

Ask the students a few questions about keystores:

* What is a keystore?

  **Answer**: An encrypted file that contains some data, like a private key.

* Why use a keystore instead of just a private key?

  **Answer**: The private key stays protected on disk, since it's encrypted.

* What type of cryptography does a keystore use to encrypt a private key?

  **Answer**: Symmetric Cryptography! (The password is the symmetric key).

- - -

### 9. BREAK (15 min)

- - -
