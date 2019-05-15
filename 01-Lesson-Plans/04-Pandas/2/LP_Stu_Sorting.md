### 3. Students Do: Sorting (15 mins)

In this activity, students will calculate daily returns for a single ticker for the year of 2019. The data will then be sorted in descending order to identify the top 5 performing days for returns.

**Files:**

* [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Unsolved/out_of_sorts.ipynb)

**Instructions:**

* [README.md](Activities/03-Stu_Sorting/README.md)

### 4. Instructor Do: Review Sorting (5 mins)

**Files:**

* [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Solved/out_of_sorts.ipynb)

Open the solution and explain the following:

* The `sort_values` function can be used to sort a DataFrame by a specific column.

    ```python
    # Sort data by `NOCP` in descending order
    tsla_sorted = tsla_daily_returns.sort_values("NOCP")
    tsla_sorted.head()
    ```

* The `sort_values` function has an attribute called `ascending` that can be configured as either `True` or `False`. Setting ascending to `True` sorts data in ascending order. `False` sorts data in descending order.

    ```python
    # Sort data by `NOCP` in descending order
    tsla_sorted = tsla_daily_returns.sort_values("NOCP", ascending=False)
    tsla_sorted.head()
    ```

    ![stu_sort_descending.png](Images/stu_sort_descending.png)

  Ask for any remaining questions before moving on.
