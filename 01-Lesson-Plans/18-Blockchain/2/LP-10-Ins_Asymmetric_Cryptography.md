### 10. Instructor Do: Asymmetric Cryptography Demo (10 min)

Let's try and solve that pesky problem of having to share the password.

Pick a volunteer to help assist with this demo. They will be encrypting a message using the instructor's public key.
You can emulate another student by using another tab as well if you do not want to have a volunteer or to test, but it may be more confusing.

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

    * **Answer**: The private key, or password to the message.

Elaborate to the students about how this technique allows for secure communication without having to share private data.

  * The idea is that you encrypt the data using the recipient's **public** key.
    Then, the recipient uses their **private** key to decrypt the message.

  * Only the sender and receiver can decrypt the messages between them, nobody in between, and they do not need
    to share a secret key beforehand.

  * This is what allows for something called "end-to-end" encryption, which is what encrypted messaging platforms use.
