## 18.2 Lesson Plan: Basic Cryptography

### Overview

Today's class will introduce students to the fundamental cryptographic techniques used throughout blockchain and internet
technologies.

The goal of this lesson is to have the students understand and apply basic cryptographic concepts to their daily lives as
well as to arbitrary data, understanding the significance and applications of these techniques.

### Class Objectives

By the end of the class, students be able to:

* Describe what cryptography is used for.

* Describe what a hash is.

* Hash a payload.

* Explain what asymmetric keys are.

* Sign a message with a private key.

* Verify a message with a public key.

* Explain the significance of asymmetric cryptography in the context of blockchain.

* Explain the use of crypto in a blockchain network.

* Explain the basic blockchain data structure.

- - -

### Instructor Notes

* Today is a heavy cryptography day, it is advisable to refresh on symmetric vs asymmetric (public key) cryptography, as well as digital signatures.

* If students are having trouble connecting with the real world examples, they will likely have a better understanding when actually sending encrypted messages to each other.

* Though these cryptographic algorithms and techniques are founded on mathematics, it is not required to understand the algorithms themselves to learn how they generally operate.

* This is not designed to teach someone how the algorithms and math works, only to be able to navigate the blockchain industry and to understand basic security.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 18.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

### 1. Instructor Do: Welcome to Class (5 min)

**Files:**

* [slides x-y]()

Welcome to the cryptography fundamentals part of the course. In today's class you will be covering the basic cryptographic
techniques that blockchain technology, as well as the rest of the internet, is built upon.

Ask the students to refresh their definitions:

* What is a hash?

  **Answer**: A one way function that produces a digital fingerprint of data.

* What is a wallet?

  **Answer**: A set of "keys" to your funds that are on the blockchain.

Explain that today, we will be learning the techniques that make these things possible.

Ask the students to raise their hand if they have heard of:

* Encryption

* Digital Signatures

Ask the students to offer some of their answers, then move on while telling them that we will be learning these very things.

Ask the students to raise their hand if:

* They have ever used a password to protect something like their cell phone, computer, social media, etc.

* They have ever used an encrypted messaging service.

Point out that students may have seen cryptography in action when browsing the internet over HTTPS by pointing out the "green lock"
in the URL bar of their web browsers.

![green lock https](Images/green-lock-https.png)

* Describe that that this means the communication between you and the website is
  "encrypted" so that nobody else on the network can see the information.

### 2. Students Do: Cryptography Use Cases (10 min)

Students will be researching some applications of cryptography in the wild.

Explain to the students that getting good at this type of research is key to succeeding in an emerging field like the blockchain industry.

**Files:**

* [README.md](Activities/02-Stu_Cryptography_Use_Cases/README.md)

Have TAs circulate around the class and ensure students are not stuck. This should be a generally easy going activity.

### 3. Instructor Do: Cryptography Use Case Review (15 min)

Given the research the students just did, ask the students to share some of the most common use cases.

Some examples may include:

* Storing files safely.

* Securing communications.

* Verifying authenticity of some data.

* Payment systems (EMV chips, online payment gateways, banking communication).

Ask the students:

* What sort of institutions would you hold to the standard of using good cryptography?

  **Answer**: Banks, exchanges, financial institutions.

  **Answer**: Messaging platforms, payment systems.

* What are some risks that could exist if an encryption algorithm is broken?

  **Answer**: A data breach could occur, private information could be exposed.

* What about a hashing algorithm?

  **Answer**: Using that algorithm for data integrity would no longer be secure, since each hash is no longer unique to the data.

Now elucidate that while you expect these services to be using good cryptography, practically every application benefits
from having it. By using good cryptography, a more robust and secure internet can exist.

Remind students that practically all of the hacks you hear about in the news are from misconfigured or lack of cryptography,
so it is very important to integrate it throughout their lives in order to protect their data and identity.

### 4. Instructor Do: Hashing Demo (10 min)

**Files:**

* [solution.py](Activities/04-Ins_Hashing/Solved/solution.py)

Walk through the solution and highlight the following:

  * Notice how each hash is different, even though only one character was changed in the input

  * Notice that no matter what, the same input will give the same hash output, it's a one to one relationship.

Ask the students if the output of the hash looks familiar, and where they might have seen them so far:

  **Answer**: Transaction IDs

  **Answer**: Block hashes

Point out that addresses are actually derived from hashing as well, but are not purely hashes as they will learn later today.

### 5. Students Do: Hashing with Hashlib (10 min)

Students will now hash two equivilalent messages and compare the outputs.
Then, they will modify one of the messages and compare again.

**Files:**

* [README.md](Activities/05-Stu_Hashlib/README.md)

* [hashing.py](Activities/05-Stu_Hashlib/Unsolved/hashing.py)

Point out to the students that the strings that are being hashed require the following syntax:

```python
message = b"Message to be hashed"
```

* The `b` prefixing the string definition passes the string as a byte array, which is the required input type for hashing algorithms.

* Explain to the students that this means that hashing works on all types of data, regardless of it's data type,
  since it operates on the actual bits themselves.

Have TAs circulate through the class to ensure that students are able to properly hash messages.

### 6. Instructor Do: Hashing Review (5 min)

Ask the students the following questions:

  * What do you notice about the length of the hashes?

    **Answer**: They are the same length no matter what.

  * Why might this be useful?

    **Answer**: You can verify large amounts of data with a smaller string.

  * What is the biggest functionality hashing enables?

    **Answer**: Data integrity

Reaffirm to the students that the hashes of the messages should only be equal if the messages are equal.

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

### 8. Students Do: Encrypting and Decrypting Messages (10 min)

Students will now use the same tool to encrypt and decrypt messages with a partner. Send out the instructions,
which includes the URL to the TweetNacl.js tool.

**Files:**

* [README.md](Activities/08-Stu_Encrypting_Decrypting/README.md)

Have the students pick a partner to send and receive encrypted messages with.

Have TAs circulate and ensure that students can use the tool properly and are successfully encrypting and decrypting
each other's messages.

### 9. Instructor Do: Symmetric Cryptography Review (10 min)

Ask the students the following questions:

  * What is the biggest security hole you see in this system?

    **Answer**: The key has to be known by both parties.

    **Answer**: It might be hard to securely deliver the key and nonce to the recipient.

  * What is symmetric cryptography best used for?

    **Answer**: Storing secure data on a hard drive. This is also called "encrypting data at rest."

    **Answer**: Securing data that does not need to be transferred over the internet.

### 10. Instructor Do: Asymmetric Cryptography Demo (10 min)

Explain to students that we need a way of sharing secret data without having to share a password beforehand.

Pick a volunteer to help assist with this demo. They will be encrypting a message using the instructor's public key.

Navigate to the ["Box" feature](https://tweetnacl.js.org/#/box) of the TweetNaCl.js site.
Have your volunteer student do the same.

Generate a `Secret Key` using the first `Random` button.
Have your volunteer student do the same.

This should generate a pair of keys, public and private:

![asymmetric keys](Images/asymmetric-keys.png)

Send the student your Public Key in the `My Public Key` field at the bottom.
Have them paste this public key into the `Their Public Key` field.

![asymmetric public](Images/asymmetric-public.png)

* Explain that in this case, you are free to share your public key. In fact, it is what will be used to encrypt the message.

* You must **always** keep your private/secret key **safe**, and **never** ever share it!

Have the student generate a `Nonce`, then ensure that the student has the following three fields populated:

  * Their Public Key (instructor's)

  * Secret Key

  * My Public Key (student's)

  * Nonce

Have the student type a class-friendly message into the `Message` box, then click `Encrypt`.

Have the student send over the following fields:

  * Public Key

  * Nonce

  * Encrypted Message (in `Box` field)

Once they have done that, copy the information into the running demo.

You should have the **Student** public key in the `Their Public Key` field, the encrypted message in the `Box` field,
and the nonce in the `Nonce` field.

![student's info](Images/asymmetric-students-info.png)

Click `Decrypt` and the message should be displayed:

![decrypted](Images/asymmetric-decrypted.png)

Ask the students:

  * What information was not shared during this encrypted message exchange?

    **Answer**: The private key, or password to the message.

Elaborate to the students about how this technique allows for secure communication without having to share private data.

  * The idea is that you encrypt the data using the recipient's **public** key.
    Then, the recipient uses their **private** key to decrypt the message.

  * Only the sender and receiver can decrypt the messages between them, nobody in between, and they do not need
    to share a secret key beforehand.

  * This is what allows for something called "end-to-end" encryption, which is what encrypted messaging platforms use.

### 11. Students Do: Asymmetric Encryption (10 min)

Students will get into pairs of 2 and encrypt and decrypt messages between each other using
asymmetric encryption instead of symmetric.

**Files:**

* [README.md](Activities/11-Stu_Asymmetric_Encryption/README.md)

Have TAs circulate and ensure that students are successfully encrypting and decrypting each other's messages.

### 12. Instructor Do: Asymmetric Encryption Review (5 min)

Ask the students the following questions:

  * What is the biggest benefit to using asymmetric encryption over symmetric?

    **Answer**: You do not need to share a key beforehand.

    **Answer**: Only the recipient and the sender can decrypt the payloads.

  * What is the difference between symmetric and asymmetric encryption?

    **Answer**: You have a single, private key with symmetric, versus having a pair of keys for public and private use in asymmetric.

### 13. Instructor Do: Digital Signatures (10 min)

Pick another volunteer to help assist with this demo.
You can emulate another student by using another tab as well if you do not want to have a volunteer or to test, but it may be more confusing.

Navigate to the ["Sign" feature](https://tweetnacl.js.org/#/sign) of the demo site.
Have your volunteer do the same, only have them click `Verify` right after instead.

Generate a `Secret Key`.

Type a message to sign.
Make it something like "I authorize transferring $100 to Jane Doe" to stress importance of the data's integrity, and to maliciously modify later.

Click `Sign` to generate the message signature.

![signed message](Images/signed-message.png)

Send the following fields to the student to have them verify the message's signature:

  * Public Key

  * Message

  * Signature

Ensure that the student is at the `Verify` section of the `Sign` feature, and have them paste
the public key, signature, and message into their corresponding fields.

Once they have pasted the values in the correct fields, they should be able to click `Verify`
at the bottom of the page to check the signature against the public key.

The student should see:

![verified message](Images/verified-message.png)

* Ask the student if the message was properly verified, and if they see a green success box.

Navigate to the `Verify` section as well, and demonstrate the same verified message to the class.
The fields should stay populated.

Click `Verify` at the top to re-enable the ability to edit the `Message` field:

![verify again](Images/verify-again.png)

Edit the message to say something different, like increasing the dollar amount from $100 to $1000.

Demonstrate that once you modify the message after it is signed, and click `Verify` at the bottom,
the signature fails to validate.

![verification failed](Images/verify-failed.png)

### 14. Students Do: Signing and Verifying Messages (10 min)

Students will now get with a partner and sign and verify messages between each other.

**Files:**

* [README.md](Activities/14-Stu_Signing_Verifying/README.md)

Have TAs circulate through the class and ensure that students are successfully verifying messages.

### 15. Instructor Do: Digital Signatures Review (10 min)

Ask the students the following questions:

  * It looks like this helps a lot with data integrity. Why not just hash the message instead?

    **Answer**: This proves that the owner actually sent and authorized that data.

    **Answer**: This is an additional layer. This provides authenticity and authentication at the same time, aka ownership and identity.

Explain to the students:

  * Digital signatures in combination with hashing and encryption can be a powerful way to ensure a message is
    delivered securely (without other parties snooping in), and that the right message got there without modification.

Ask the students (critical):

  * So what do transactions on a blockchain and digital signatures have in common?

    **Answer**: A transaction is just a signed message authorizing transfer of funds, hence cannot be modified and can be verified

Tell the students to start thinking about the different ways you might use these cryptographic techniques
in the context of blockchain and cryptocurrencies.

- - -

### 16. BREAK (15 min)

- - -

### 17. Instructor Do: Blockchain Data Structure (10 min)

Now that the students understand the fundamental cryptographic techniques that power the internet and blockchain tech,
let's break down the data structure of a blockchain and why the design is so secure.

Open up the [Anders Blockchain Demo](https://anders.com/blockchain/blockchain.html) and walk through the different fields.

Point out the matching "chain of hashes" located inside of each block:

![matching hashes](Images/blockchain-matching-hashes.png)

* Notice how the hash of the first block is actually inside of the second block

* This means that the hash of the second block is actually dependent on the previous

* Ask the students, "What were to happen if the first block was modified?"

  **Answer**: The second block would be invalidated, since the first block's hash changed

Continuing with the first block, type some data into the data field, like "Alice sends Bob $10."

![blockchain data field](Images/blockchain-data.png)

* Explain to the class that the change from green to red represents a break in the chain

* This means that the hash first block has changed since we changed the data, so we have to rebuild the chain from this point all the way to the end.

Click `Mine` in the first block to change it green and to regenerate the hashes:

![mining](Images/blockchain-mining.png)

* Point out that we still need to mine each block going forward again, one at a time, chronologically
  in order to completely rebuild the chain.

Click on `Mine` in the second block to demonstrate.

![mining gif](Images/blockchain-mining.gif)

* Point out that each block is dependent on each other since the hashes are chained.

Now, it's time to have the students try it for themselves.

### 18. Students Do: Build a Blockchain Online (10 min)

Students will be repeating the blockchain online activity at their computers.

**Instructions:**

* [README.md](Activities/18-Stu_Blockchain_Online/README.md)

Send out the [Anders Blockchain Demo](https://anders.com/blockchain/blockchain.html) to the students.

Have the TAs circulate through the class and ensure that students are connecting blocks and rebuilding the chain.

### 19. Instructor Do: Blockchain Data Structure Review (5 min)

Ask the students the following questions:

  * How are the blocks linked together / What does the "chain" in blockchain mean?

    **Answer**: Each block is linked to the previous by putting the last block's hash inside of it.

  * In a blockchain with 10 blocks, if you were to modify the 3rd block, how many would you need to re-mine?

    **Answer**: 8 blocks, 3 through 10 need to be mined again

* Explain that this is the feature that makes blockchain transactions so "final" -- once a block is accepted by the network,
  it takes an enormous amount of energy to "roll a transaction back" since each block from the point of that transaction forward must be mined *again*, which quickly becomes mathematically infeasible.

### 20. Instructor Do: Recap / Where's the crypto in crypto? (10 min)

Now that the students have a fundamental understanding of cryptography, and how a blockchain is built
using these concepts and data structures, it's time to review and put a cap on the day.

First, congratulate and encourage the students for getting through one of the hardest and conceptually abstract
day of this section. They are now equipped with knowledge of blockchain *and* security.

Ask the students the following questions:

  * So where's the "crypto" in cryptocurrency?

    **Answer**: It's an adage to the cryptography that is **heavily** used throughout the system.

    **Answer**: You could almost call it "cryptography currency" and get away with it.

  * What is a hash?

    **Answer**: A one-way fingerprint of data, usually represented as a long string of alphanumeric characters.

  * What is symmetric cryptography?

    **Answer**: A type of cryptography that uses a single, preshared key for encryption.

  * What is asymmetric cryptography?

    **Answer**: AKA "public key cryptography" -- Cryptography that uses a pair of keys, public and private, for encrypting and signing messages.

  * What is a (digital) signature?

    **Answer**: A message that can be cryptographically validated for its authenticity and integrity.

  * Where is the "chain" in blockchain?

    **Answer**: Blocks are connected via a chain of hashes, giving the structure it's name and security.

Remind the students that cryptography is a tough subject that is taught usually in a Computer Science degree and that they
should be proud for learning it. It is something that few people understand but powers many systems that keep our information
secure every day.
