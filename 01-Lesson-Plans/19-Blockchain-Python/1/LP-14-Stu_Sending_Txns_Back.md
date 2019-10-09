### 14. Students Do: Sending Transactions from Keystore Account (10 min)

Now, challenge the students to use this program that they've written to send a transaction from `account_two` back to `account_one`.

**Files:**

* [main.py](Activities/14-Stu_Sending_Txns_Back/Solved/main.py)

Given the code we've written so far (provided above), this function should be all that is necessary to get the job done:

```python
send_tx(account_two, account_one.address, 333)
```

Have TAs circulate and assist any students that are having difficulties.

If the students are having trouble, remind them that they are passing the entire `account_two` object
as the sending account, and passing just the `account_one.address` to the recipient field.

Remind students that they will need to send what is available in the balance.

### 15. Instructor Do: Review Sending from Keystores (5 min)

Ask the students the following questions:

* How might we check the transaction status?

  **Answer**: By calling `w3.eth.getTransaction` and passing the transaction hash.

* What were to happen if we were to try to send a transaction to ourselves?

  **Answer**: The transaction would still go through, but you'd pay the fee for it.

### 16. Instructor Do: Recap / Prepare for next class (10 min)

Congratulate the students on learning how to program money with Python.

Ask the students:

* Wouldn't it be cool to do this with other blockchains besides Ethereum?

Explain that we'll be learning how to perform this same process with the Bitcoin blockchain, and by proxy,
all of it's decendants (like Litecoin, Dash, Bitcoin Cash, etc).

Send out the following instructions to have the students extract a Bitcoin testnet address and request tokens.

**Files:**

* [Acquiring Test Bitcoins](Activities/16-Ins_Recap/README.md)

Since it takes time for transactions to mine, we are having the students request the testnet coins early,
allowing time in between class for troubleshooting in case students have difficulties.

Before next class, request some test bitcoins of your own to prepare to send to students that had difficulties.
