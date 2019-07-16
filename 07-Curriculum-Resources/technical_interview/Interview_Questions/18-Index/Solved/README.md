# Index

## Part 1

* Explain an index in SQL.

## Part 2

* What are the different types of `index`? If possible, explain each type with an illustration.

## Solutions

* Part 1: an `index` is used to creat indexes in tables. They aid in quick data retrieval by speeding up searches and queries. When creating an index, table data is not changed. Instead, a new data structure is created that refers to the table.

* Part 2: There are three types of index:

  * Unique: if a column is uniquely indexed, no duplicate values will be allowed in the field. If a primary key is already defined, then a unique index is automatically applied.

  * Clustered: this type of index will reorder the physical order of the table and searches based off the key values. Only one clustered index is allowed per table.

  * Non-Clustered: a non-clustered index will not alter the physical form of the table. More than one non-clustered indexes are allowed per table.
