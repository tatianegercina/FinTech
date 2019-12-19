# Encrypting and Decrypting Messages with Asymmetric Encryption

In this activity, you'll be sending encrypted messages the real way, by using public key (asymmetric) cryptography!

## Instructions

Get together with a partner, you will be sending messages with and do the following:

* Navigate to the ["Box" feature](https://tweetnacl.js.org/#/box) of the TweetNaCl.js demo.

* Generate a keypair by clicking `Random` in the `My Secret Key` field:

 ![asymmetric keys](Images/asymmetric-student-keys.png)

* Send your public key to your partner.

* When you receive your partner's public key, paste it into the `Their Public Key` field.

 ![their public key](Images/asymmetric-their-public.png)

* Generate a `Nonce` to go with the message you'll send.

* Type a message into the `Message` field to encrypt.

* Once you have all of the fields filled out, you can click `Encrypt`.

 ![encrypted message](Images/asymmetric-student-encrypted.png)

* Send the following information in the message to your partner:

 * Encrypted Message from the `Box` field.

 * Nonce.

* Now, without clearing out your secret key, try to decrypt their message by pasting their encrypted message and nonce into the corresponding fields in your browser.

 ![partner's info](Images/asymmetric-partners-info.png)

Congrats! You have successfully communicated securely using real asymmetric encryption!

Think to yourself and discuss with your partner:

* What is the main benefit of using this over symmetric encryption?

* What makes this safer than symmetric encryption for communications?

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
