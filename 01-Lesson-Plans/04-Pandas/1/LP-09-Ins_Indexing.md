### 9. Instructor Do: Indexing (10 mins)

In this activity, students will learn how to locate and select data within a DataFrame through indexing. Indexing allows us to slice and dice our data so we can get or set values for any of the "cells" in our table.

**Files:**

* [indexing.ipynb](Activities/09-Ins_Indexing/Solved/indexing.ipynb)

Walk through the demo and explain the following:

* The `iloc[]` function returns a row based off of a numerical index.

  ![iloc-first-row](Images/iloc-first-row.png)

* The `iloc[]` function can return a range of rows based off of a numerical index range.

  ![iloc-first-10](Images/iloc-first-10.png)

* The `iloc[]` function can return specific columns.

  ![iloc-second-column](Images/iloc-second-column.png)

* The `iloc[]` function can return a combination of specific rows and columns.

  ![iloc-row-column-combo](Images/iloc-row-column-combo.png)

* The `iloc[]` function can be used to modify specific row values.

  ![iloc-assignment](Images/iloc-assignment.png)

* To use the `loc[]` function on the index of a DataFrame, string values will need to be set as the index using the `set_index()` function.

  ![set-index-first-name](Images/set-index-first-name.png)

* The `loc[]` function returns a row based off of a string index.

  ![loc-string](Images/loc-string.png)

* The `loc[]` function can return a range of rows based on a range of string indexes.

  ![loc-string-range](Images/loc-string-range.png)

* The `loc[]` function can be used to return rows based off of column value conditionals.

  ![loc-conditional](Images/loc-conditional.png)

* The `loc[]` function can be used to modify specific row values.

  ![loc-assignment](Images/loc-assignment.png)

* Finally, explain that it will take some time to get used to indexing data with Pandas, but over time, it will become second nature -- practice makes perfect!
