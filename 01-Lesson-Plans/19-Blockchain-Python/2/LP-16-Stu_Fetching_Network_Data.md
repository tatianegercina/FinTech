### 16. Students Do: Fetching Network Data (10 min)

Now, the students will practice using the functions you just demonstrated.

**Instructions:**

* [README.md](Activities/16-Stu_Fetching_Network_Data/README.md)

Have TAs circulate and ensure that students are not stuck and can fetch balances, transaction history, and UTXOs.

### 17. Instructor Do: Network Functions Review (5 min)

Ask the students the following questions:

* Where are we fetching this data from?

  **Answer:** Bitcoin nodes, in this case, publicly available ones that the `bit` library points to.

* Why would it be necessary to fetch blockchain data programmatically?

  **Answer:** You need the latest data in order to construct valid transactions.

* What is a transaction ID? How is it generated?

  **Answer:** It is a hash of the transaction that identifies it on the network.

* What value does `bit` provide?

  **Answer:** It abstracts all of the functions you'd need to interact with Bitcoin, keys, and includes currency conversions.
