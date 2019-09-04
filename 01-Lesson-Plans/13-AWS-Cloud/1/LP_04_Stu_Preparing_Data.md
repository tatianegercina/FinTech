### 4. Students Do: Understanding customers (20 mins)

In this activity, students will perform some data preparation tasks on a dataset that contains data from purchases on a e-commerce website made by 200 customers. Students will use this dataset on further activities to find customers segments.

There are some data transformations that should be made on the dataset, so ask TAs to assist students if there are any questions about why the following changes are needed.

* **Annual Income:** This feature should be regularized since it’s in a different scale than the other features; dividing by `1000` is the simplest solution.

* **Gender:** The `Gender` should be transformed to a numerical value, in this case, transforming `Male` to `1` and `Female` to `0` is a feasible solution.

* **CustomerID:** Since this column is not relevant to the clustering algorithm, it should be dropped from the DataFrame.

**Instructions:**

* [README.md](Activities/02-Stu_Preparing_Data/README.md)

**Files:**

* [preparing_data.ipynb](Activities/02-Stu_Preparing_Data/Unsolved/preparing_data.ipynb)

* [shopping_data.csv](Activities/02-Stu_Preparing_Data/Resources/shopping_data.csv)

---

### 5. Instructor Do: Review Understanding customers (10 mins)

**Files:**

* [preparing_data.ipynb](Activities/02-Stu_Preparing_Data/Solved/preparing_data.ipynb)

* [shopping_data.csv](Activities/02-Stu_Preparing_Data/Resources/shopping_data.csv)

* [shopping_data_cleaned.csv](Activities/02-Stu_Preparing_Data/Resources/shopping_data_cleaned.csv)

Walk through the solution and highlight the following:

* Unsupervised learning algorithms only work with numerical data, so checking data types is an important task to ensure that numerical values were loaded to the DataFrame with the appropriate data type.

  ![Data types check](Images/datatypes-check.png)

* All columns have an appropriate data type, so no adjustments are needed.

* The `CustomerID` column can be dropped, it's not relevant for clustering since it doesn't denote any relevant characteristic of customers shopping habits.

  ```python
  df_shopping.drop(columns=["CustomerID"], inplace=True)
  ```

* Looking for `null` values and duplicate entries is part of any data preprocessing workflow; there are no `null` values nor duplicates on this DataFrame, so no additional adjustments are needed on this matter.

* The `Genre` column is categorical, so it should be transformed to numerical values. Transforming `Male` to `1` and `Female` to `0` is a common practice.

  ```python
  def changeGenre(genre):
    if genre == "Male":
        return 1
    else:
        return 0

  df_shopping["Genre"] = df_shopping["Genre"].apply(changeGenre)
  ```

* The `Annual Income` column is on a different scale than the other columns, so this column should be rescaled. Dividing by `1000` is the simplest approach.

  ```python
  df_shopping["Annual Income"] = df_shopping["Annual Income"] / 1000
  ```

* Finally, the cleaned DataFrame is saved as a `CSV` file for being used on forthcomming activities.

```python
  file_path = Path("../Resources/shopping_data_cleaned.csv")
  df_shopping.to_csv(file_path, index=False)
  ```

Be sure that there are no pending questions before moving forward.
