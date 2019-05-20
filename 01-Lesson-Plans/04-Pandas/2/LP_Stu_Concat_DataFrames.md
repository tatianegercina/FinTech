### 13. Students Do: Concat DataFrames (15 mins)

**Instructions:**

* [README.md](Activities/13-Stu_Concat_DataFrames/README.md)

**Files:**

* [joining_forces.ipynb](Activities/13-Stu_Concat_DataFrames/Unsolved/joining_forces.ipynb)

### 7. Instructor Do: Review Concat (5 mins)

**Files:**

* [joining_forces.ipynb](Activities/13-Stu_Concat_DataFrames/Solved/joining_forces.ipynb)

Walkthrough the solution and go over the following discussion points:

* The `concat` function can be used to combine or link more than one DataFrame.

* DataFrames can be concatenated either by `rows` or `columns`. Concatenating by `row` will create a DataFrame that has the total number of rows. Concatenating by `columns` produces a DataFrame that has the columns from all DataFrames concatenated.

  ![concat_axis.png](Images/concat_axis.png)

* DataFrames should be concatenated by `rows` when the columns of the DataFrame are the same and should remain the same. The idea is that the rows are appended.

  ![stu_concat_rows.png](Images/stu_concat_rows.png)

* DataFrames should be concatenated by `columns` when columns from one DataFrame need to be combined with columns from another. The idea is that the columns are appended.

  ![stu_concat_cols.png](Images/stu_concat_cols.png)
