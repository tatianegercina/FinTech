### 3. Student Do: Encoding Categorical Data for Machine Learning (10 min)

In this activity, students are tasked to encode some categorical and text features of a fictional dataset that contains 100,000 credit card transactions. In forthcoming activities, students will use this dataset to predict fraudulent transactions.

**Instructions:**

* [README.md](Activities/02-Stu_Categorical_Data/README.md)

**Files:**

* [encoding-categorical-data.ipynb](Activities/02-Stu_Categorical_Data/Unsolved/encoding-categorical-data.ipynb)

---

### 4. Instructor Do: Review Encoding Categorical Data for Machine Learning (10 min)

**Files:**

* [encoding-categorical-data.ipynb](Activities/02-Stu_Categorical_Data/Solved/encoding-categorical-data.ipynb)

Walk through the solution and highlight the following:

* Despite the dataset looks huge since it has 100,000 records, this is only a small sample of what a real dataset can be; in industry, you can have millions of records just for one day of transactions.

* After loading the data into the `transactions_df` DataFrame, the only column that could need to be casted is the `date` column. This column can be easily converted to datetime using Pandas.

  ```python
  transactions_df["date"] = pd.to_datetime(transactions_df["date"])
  ```

* The manual integer encoding of the `dateMonthName` and `dateWeekdayName` columns is needed, to create a meaningful numerical representation for those values.

* To encode `dateMonthName` and `dateWeekdayName` columns is needed as integer numbers, the the Pandas `dt` accessor is used.

  ```python
  # Encode month name
  transactions_df["dateMonthName"] = transactions_df["date"].dt.month

  # Encode week day name name
  transactions_df["dateWeekdayName"] = transactions_df["date"].dt.day
  ```

* The `LabelEncoder´ from `sklearn` is used to encode the `type` column, following the Model -> Fit -> Predict/Transform API workflow.

  ```python
  # Create the LabelEncoder instance
  le = LabelEncoder()

  # Fitting the LabelEncoder
  le.fit(transactions_df["type"])

  # Encoding type column
  transactions_df["type"] = le.transform(transactions_df["type"])
  ```

* The `gender` and `merchant` columns, are binary encoded using the Pandas `get_dummies()` function. This will increase the number of columns in the DataFrame up to `3254` columns.

  ![Binary Encoding sample](Images/encoding-categorical-1.png)

* The final touches to the DataFrame, are removing the `date` and `cardholder` columns, as well as renaming the `dateMonthName` and `dateWeekdayName` columns as `dateMonth` and `dateWeekDay`.

* Finally, the preprocessed DataFrame is saved on a `CSV` file named `transactions_data_encoded.csv` for forthcoming usage.

Answer any questions before moving on.
