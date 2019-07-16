# ACID


* What are the ACID properties of SQL transactions? If possible, explain each property with an illustration of an example.


## Solution

* ACID stands for Atomicity, Consistency, Isolation, and Durability.

* Atomicity: each transaction must be all-or-nothing. That is, a transaction takes place if it's only partly completed. In a bank transfer from person A to person B, for example, person B's account cannot be credited unless withdrawal takes place from person A's account.

* Consistency: all constraints are followed for each transaction. Constraints such as keys, data types, uniqueness are followed. The database should remain in a consistent state before and after the transaction.

* Isolation: no transaction affects another transaction. If there are multiple bank transfers, for example, only one can be carried out at the same time, before another one can begin.

* Durability: the transaction will persist in the database after a transaction. For example, after a bank transfer, even if a power outage should take place, the record of the transaction remains intact.

* For another analogy, see [https://stackoverflow.com/questions/3740280/acid-and-database-transactions#3741079](https://stackoverflow.com/questions/3740280/acid-and-database-transactions#3741079).
