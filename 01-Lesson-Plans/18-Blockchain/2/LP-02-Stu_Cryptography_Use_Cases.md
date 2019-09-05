### 2. Students Do: Cryptography Use Cases (10 min)

Students will be researching some applications of cryptography in the wild.

**Files:**

* [README.md](Activities/03-Stu_Cryptography_Use_Cases/README.md)

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

    * **Answer**: Banks, exchanges, financial institutions.

    * **Answer**: Messaging platforms, payment systems.

  * What are some risks that could exist if an encryption algorithm is broken?

    * **Answer**: A data breach could occur, private information could be exposed.

  * What about a hashing algorithm?

    * **Answer**: Using that algorithm for data integrity would no longer be secure, since each hash is no longer unique to the data.

Now elucidate that while you expect these services to be using good cryptography, practically every application benefits
from having it. By using good cryptography, a more robust and secure internet can exist.

Remind students that practically all of the hacks you hear about in the news are from misconfigured or lack of cryptography,
so it is very important to integrate it throughout their lives in order to protect their data and identity.
