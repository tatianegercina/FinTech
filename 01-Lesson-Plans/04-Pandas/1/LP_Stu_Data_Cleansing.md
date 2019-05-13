### 7. Students Do: Data Cleansing (15 mins)

In this activity, students will be given Harold's stock data and are asked to perform a series of data quality checks to ensure the data is ready for analytical use. The objective of the assignment is for the students to learn how to cleanse data using Pandas native functions (`count`,`value_counts`,`isnull`,`sum`,`mean`,`contains`, and `replace`).

**Files:**

* [spring_cleaning.ipynb](Activities/07-Stu_Data_Cleansing/Unsolved/Core/spring_cleaning.ipynb)

**Instructions:**

* [README.md](Activities/07-Stu_Data_Cleansing/README.md)

- - -

### 8. Instructor Do: Review Data Cleansing (5 mins)

**Files:**

* [spring_cleaning.ipynb](Activities/07-Stu_Data_Cleansing/Solved/Core/spring_cleaning.ipynb)

Walkthrough the solution and highlight the following talking points:

* Data cleaning is important because it removes all of the issues and errors that would block or inhibit computation. Without data cleaning, financial data can be calculated and aggregated incorrectly and inaccurately. Data quality issues can skew financial numbers, resulting in numbers being reported either higher or lower than actual. Since numbers drive business decisions in the financial world, use of incorrect data could have catastrophic implications.

* The `shape` function provides a quick and easy way to understand the structure of a DataFrame, including the number of columns and number of tuples/rows in the DataFrame.

  ```python
  csv_data.shape
  ```

  ```
  (504, 13)
  ```

* Sampling a data set to get a better understanding of potential data quality issues can lead you to discovering non-common data quality issues.

  ```python
  csv_data.head()
  ```

  ![LP_Stu_Cleansing_Head.PNG](Images/LP_Stu_Data_Cleansing_Head.PNG)

* Performing a `count` is a great way to assess how many records were loaded into a DataFrame for each Series. The results of `count` creates a view into any data loss that could have happened while loading data into a DataFrame. This number reflects the total number of non-null values. `Count` can also be used to determine the total number of non-null values for a specific field.

  ```python
  csv_data.count()
  ```

  ```
  name                  502
  sector                501
  price                 500
  price_per_earnings    497
  dividend_yield        499
  earnings_per_share    498
  52_week_low           500
  52_week_high          500
  market_cap            500
  ebitda                492
  price_per_sales       500
  price_per_book        492
  sec_filings           500
  dtype: int64
  ```

  Ask the students:

    * What should happen if all values in a Series are null?

      > "The Series should be dropped."

* Nulls can throw a wrench in an analytic pipeline. The `isnull` function can identify which Series has nulls. If there are nulls, they can be removed or filled. The `dropna` and `fillna` functions provide this functionality, respectively. Note that it's important to understand which fields can have nulls and which one's cannot.

  ```python
  csv_data.isnull()
  ```

  ![LP_Stu_Cleansing_Isnull.PNG](Images/LP_Stu_Data_Cleansing_Isnull.PNG)

* Using `mean` and `sum` with `isnull` will calculate the percentage and number of nulls for a DataFrame. This is important when considering the distribution of missing values in a DataFrame. The percentage and number of nulls could impact how the missing values are cleaned.

  ```python
  csv_data.isnull().mean() * 100
  csv_data.isnull().sum()
  ```

  ![LP_Ins_Data_Cleansing_Null_Pct_Check.PNG](Images/LP_Ins_Data_Cleansing_Null_Pct_Check.PNG)

  ![LP_Ins_Data_Cleansing_No_Of_Null.PNG](Images/LP_Ins_Data_Cleansing_No_Of_Null.PNG)

* Instead of dropping nulls in a Series, nulls can be filled with a default value. Common default values are "Unknown", 0, and mean().

  ![LP_Ins_Data_Cleansing_Fill_Na.png](Images/LP_Ins_Data_Cleansing_Fill_Na.png)

* The `dtypes` function can be used on a DataFrame to identify Series data types. A series' data type can also be identified by using `dtype`. Identifying data types is valuable because it allows for incorrectly inferred data types to be corrected and cast to the appropriate data types. If needed, a Series can be cast to the appropriate data type using the `astype` function. (i.e. converting a Date field from `string` to `Date`). Some conversions might require values to cleaned before they can be converted (i.e. removing `$` from an amount field).

  ![LP_Ins_Data_Cleansing_Data_Types.PNG](Images/LP_Ins_Data_Cleansing_Data_Types.PNG)

If time permits, engage the students with the following review questions:

* Two types of rules determine what is considered clean and dirty data. What are they?

* To get a sample of the data stored in a DataFrame, which function should be used?

* When doing a count on the data, the count of rows for some fields was different than others. Why is this?

* If I wanted to fill null values in a Series with a default value of 0, I would use which function?

* What function can be used to change the data type of a Series?

* It's ok to have currency symbols and commas in amount fields. True or False?

* What two functions can be used to identify and remove currency symbols?

Sample Answers:

> "Data quality rules are determined based off of technical and business rules."
>
> " The `sample` function is a great function to use to get n number of records. The `head` function can also be used."
>
> "Panda's `fillna` function would be used, with 0 provided as an argument."
>
> "The `count` function does not include missing values in the aggregation. The numbers are different because some fields have nulls."
>
> "The `astype` function can be used to change the data type of a Series. A data type must be passed as an argument."
>
> "False. Amount fields should be floats. Floats cannot have symbols or commas, as these are strings."
>
> "`contains()` can be used to identify currency symbols, and `replace()` can be used to remove them."

To guide students, you may want to follow up with questions such as:

> "I used fillna(0) to fill NaN values in my DataFrame, but now my first_name and last_name fields have 0s in them. What happened? What should I have done instead?"
>
> "My dates aren't stored in the same format. Some use a dash (`-`) separator, while others do not have a separator at all. Is this a data quality issue?"
>
> "Data quality rules do not conflict with one another. True or false?"

Sample Answers:

> "`Fillna(0)` fills all null/NaN values in the DataFrame, irrespective of the data type of the Series where the null is. Fillna() should have been applied against the specific Series that needed the nulls converted to 0."
>
> "Yes. Because the date are in different formats, data is no standardized and Pandas may have difficult parsing both date formats. This is particularly important when dealing with international data. If date formats are not cleaned and standardized, the integrity of time series data could be affected."
>
> "False. Technical rules might be disregarded in order to satisfy business rules."

Ask for any remaining questions before moving on.
