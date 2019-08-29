# Encrypting and Decrypting Messages with Asymmetric Encryption

Now, you'll be sending encrypted messages the real way, by using public key (asymmetric) cryptography!

## Instructions

Get together with a partner that you will be sending messages with.

1. Navigate to the ["Box" feature](https://tweetnacl.js.org/#/box) of the TweetNaCl.js demo.

2. Generate a keypair by clicking `Random` in the `My Secret Key` field:

![asymmetric keys](../../Images/asymmetric-student-keys.png)

3. Send your public key to your partner.

4. When you receive your partner's public key, paste it into the `Their Public Key` field.

![their public key](../../Images/asymmetric-their-public.png)

5. Generate a `Nonce` to go with the message you'll send.

6. Type a message into the `Message` field to encrypt.

7. Once you have the all of the fields filled out, you can click `Encrypt`.

![encrypted message](../../Images/asymmetric-student-encrypted.png)

8. Send the following information in the message to your partner:

  * Encrypted Message from `Box` field

  * Nonce

9. Now, without clearing out your secret key, try to decrypt their message by pasting
   their encrypted message and nonce into the corresponding fields in your browser.

![partner's info](../../Images/asymmetric-partners-info.png)

Congrats! You have successfully communicated securely using real asymmetric encryption!

Think to yourself:

  * What is the main benefit of using this over symmetric encryption?

  * What makes this safer than symmetric encryption for communications?
