### 4. Students Do: Hashing with Hashlib (10 min)

* **Files:**

  * [README.md](Activities/04-Stu_Hashlib/README.md)

  * [hashing.py](Activities/04-Stu_Hashlib/Unsolved/hashing.py)

Students will now hash two equivilalent messages and compare the outputs. Then, they will modify one of the messages and compare again.

Point out to the students that the strings that are being hashed require the following syntax:

```python
message = b"Message to be hashed"
```

* The `b` prefixing the string definition passes the string as a byte array, which is the required input type for hashing algorithms.

* Explain to the students that this means that hashing works on all types of data, regardless of it's data type,
  since it operates on the actual bits themselves.

Have TAs circulate through the class to ensure that students are able to properly hash messages.

### 5. Instructor Do: Hashing Review (5 min)

Ask the students the following questions:

  * What do you notice about the length of the hashes?

    * **Answer**: They are the same length no matter what.

  * Why might this be useful?

    * **Answer**: You can verify large amounts of data with a smaller string.

  * What is the biggest functionality hashing enables?

    * **Answer**: Data integrity

Reaffirm to the students that the hashes of the messages should only be equal if the messages are equal.
