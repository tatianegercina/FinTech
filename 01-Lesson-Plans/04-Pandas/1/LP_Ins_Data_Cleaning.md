### 6. Instructor Do: Data Cleaning (10 mins)

**Files:**

* [Data Cleaning Slides]()

* [data_cleaning.ipynb](Activities/06-Ins_Data_Cleaning/Solved/data_cleaning.ipynb)

So far, students have been equipped with some great knowledge and experience creating functions and using Pandas functions to read in data from CSV files. These are great skills to have; however, they're only useful if the data being processed is clean and usable. For the most part, students have been working with clean data already curated for use. However, in the real world, data is messy and dirty, and it needs to be cleaned and prepared in order for it to be valuable. This process is data cleaning, and data cleaning is comprised of data exploration, data quality checks, and data cleaning strategies. This module will demonstrate each of these facets to ensure students can confidently clean and prep data for analytical use.

Navigate to the Unit 4.1 slides, and introduce Data cleaning to students by working through the below scenario. Allow students to propose ideas as to what they would do in the face of being presented with dirty data:

> "The datasets used so far in this class have been simple and clean datasets curated for training purposes. For example, there were no typos in any of the datasets used. There were no missing values. This will always not be the case in the real world. But imagine if there were. Imagine yourself working as a data scientist on a prediction engine for a large investment trading firm. Your goal is to predict when a trader is going to make a trade and which stocks/sectors they will most likely buy from, as well as recommend trades based off of previous trades made. This will allow for the company to predict portfolio performance and make recommendations on trades. Your coworkers gives you a CSV dataset of customer e-commerce transactions, including customer demographics, order information, and production information. But there's issues with the data. You soon realize that some of the values in the first_name Series are actually customer addresses and not names. You see that some values in the order_total field are not floats but are strings with currency symbols (i.e. `$945.00`). What do you do?"

Once students have answered, introduce data cleaning:

* Data cleaning is critical to financial analytics. Data quality issues create a need for data cleaning. Data quality issues compromise the integrity or "health" of a dataset. The goal of data cleaning is to keep the "plumbing" of data pipelines clean and in working condition so that analytics can run smoothly. The process of data cleaning can be compared to Draino: dirty data can clog analytic pipelines, and when used in calculations, dirty data can regurgitate incorrect data values and cause errors to be thrown. The process of data cleaning is the Draino that unclogs the pipelines and gets things started again. By the end of this module, students will become the Super Mario's of data cleaning, wielding Pandas data cleaning functions in their toolkits, along with Draino.

Discuss how data quality is determined. Most data quality rules are influenced by general coding etiquette and general data requirements. However, many companies create their own data governance rules and policies that dictate what makes each data element complete, consistent, valid, and accurate.

* The rules that govern data cleaning are defined by industry accepted standards. For example, a general data quality rule is that numerical fields should not contain string characters, only digits. Another industry-wide data quality rule is that there should not be any duplicate rows in a dataset. These rules are based off of various data storage design theories and best practices, all of which can be researched by students outside of class.

* Data quality rules are also defined by business or functional rules. Sometimes data needs to be stored or formatted in a unique way for business needs. For example, an international company might store dates as `DD/MM/YYY`, where as an American company might store dates as `MM/DD/YYYY`.

Ask students to propose some explanations of how data becomes dirty. Highlight some of the examples provided by students, and bring attention to the implications/impact of typos, human error, and poor data management if students do not propose these.

* When manually entering data, users can enter typos. If gone unchecked, typos can corrupt data values. There is little to be done to get rid of typos as it is difficult to identify a typo.

* Humans can copy and manipulate data incorrectly. Someone can copy and paste data into the wrong Excel files. A Python function could also incorrectly compute a data value. If these issues are not fixed, data quality issues will arise down the road.

* Poor data management includes not cleaning or storing data in an effective way. While not all data needs to be cleaned, industry standards and business rules should be consistently implemented in order to ensure the integrity of data.

Discuss approaches for identifying data quality issues. Live code a few examples.

* The first step to assessing data for quality issues is to take a sample of the data in order to assess it visually. Visually assessing data provides the opportunity to get a high level snapshot of the data. This view of the data allows programmers to identify obvious data quality issues, as well as identify any skewed rows (i.e. a customer address in a first name field).

  ```python
  # Read in data file Take sample of data
  csv_path = Path("order_data.csv")
  csv_data = pd.read_csv(csv_path, index_col="order_no")
  csv_data.sample(5)
  ```

  ![LP_Ins_Data_Cleansing_Sample_Data.PNG](Images/LP_Ins_Data_Cleansing_Sample_Data.PNG)

* A best practice is to review and assess the data types of the DataFrame. The `dtypes` function can be used to return the data type of each Series/column. When loading data into a DataFrame, Pandas will try and infer the appropriate data type automatically. It is always key to review data types after loading data into a DataFrame to ensure that Pandas inferred the correct data type. There are also instances where Pandas will be unable to infer the data type, and the series/column will be given the `object` data type.

  ```python
  # Retrieving DataFrame data types
  csv_data.dtypes
  ```

  ![LP_Ins_Data_Cleansing_Data_Types.PNG](Images/LP_Ins_Data_Cleansing_Data_Types.PNG)

* Record counts should always be reviewed to ensure the expected number of rows matches the actual. The total number of records can be identified by using the `count` function. The `count` function counts the number of non-null cells for each column or row in a Pandas DataFrame. This means that the count will not include any nulls. The number of records in a DataFrame is important to know because rows can get lost in translation. Calculations and aggregations can go wrong and produce the wrong number of records. Records can also be lost when data is sent between systems.

    ```python
    # Identifying Series count
    csv_data.count()
    ```

    ![LP_Ins_Data_Cleansing_Count.PNG](Images/LP_Ins_Data_Cleansing_Count.PNG)

  Ask the students the following question:

  * Why do you think there are unequal counts in the data?

    > "Nulls and missing data"

* Similarly, the quality of data can be assessed by using the `value_counts` function, which is a function that identifies the number of times a value occurs in a Series. `Value_counts` will reveal how many times a value occurs in a Series, with the most occurring value first.

    ```python
    # Identifying frequency values
    csv_data['customer_no'].value_counts()
    ```

    ![LP_Ins_Data_Cleansing_Distinct_Customer.PNG](Images/LP_Ins_Data_Cleansing_Distinct_Customer.PNG)

* Identifying nulls are key to assessing data quality health, and it's done so often using the `count` function that Pandas provides a specific function to help identify missing values. Nulls make it difficult to assess whether or not data is incomplete or if data is not applicable for a given field. Nulls and NullPointerExceptions can also get in the way of function execution. Pandas has the answer though! Pandas offers a native function `isnull()` that can be used to identify missing values in a field, Python `None`. The `isnull()` function identifies which column values are nulls and which ones are not. If a column value is null, `isnull()` returns `True`. If the value is not null, `isnull` returns `False`.

    ```python
    # Checking for null
    csv_data.isnull()
    ```

    ![LP_Ins_Data_Cleansing_CSV_Isnull.png](Images/LP_Ins_Data_Cleansing_CSV_Isnull.png)

* Assessing the percentage of nulls for the entire DataFrame is also valuable, especially when it comes to determining what should be done with the nulls in a DataFrame. The percentage of nulls will influence the course of action for cleaning nulls: i.e. dropping the nulls or leaving them alone.

    ```python
    # Checking for percentage of null
    csv_data.isnull().mean() * 100
    ```

    ![LP_Ins_Data_Cleansing_Null_Pct_Check.PNG](Images/LP_Ins_Data_Cleansing_Null_Pct_Check.PNG)

* Another method of determining how many nulls are in the DataFrame is to calculate the sum of all nulls.

    ```python
    # Checking for number of nulls
    csv_data.isnull().sum()
    ```

    ![LP_Ins_Data_Cleansing_No_Of_Null.PNG](Images/LP_Ins_Data_Cleansing_No_Of_Null.PNG)

* Nulls can be cleaned by replacing them with a default value (i.e. "Unknown", 0, or mean()), which is exactly what the Pandas `fillna` does! `Fillna` will replace every instance of null with the provided default value. It's important to note that while `fillna` can be used on an entire DataFrame, it is best used with a Series. This allows for the scope of the default value to be specific to the Series. For example, assigning a default value of 0 or "Unknown" to a null `order_amount` field would actually create a data quality issue.

    ```python
    # Cleanse nulls from DataFrame by filling na
    csv_data['customer_no'] = csv_data['customer_no'].fillna("Unknown")
    csv_data
    ```

    ![LP_Ins_Data_Cleansing_Fill_Na.png](Images/LP_Ins_Data_Cleansing_Fill_Na.png)

* Once nulls have been identified through a data quality process, a decision can be made to either drop the nulls or leave them. To drop all null values, the `dropna` Pandas function can be used. Providing `inplace=True` as an argument will ensure the `dropna` function does not make a copy of the DataFrame but rather performs the operation on the original.

    ```python
    # Cleaning nulls from DataFrame by dropping
    csv_data.dropna(inplace=True)
    csv_data
    ```

* It is best practice to combine the `isnull` function with the `sum` function to test the `dropna` function. This serves as a unit test of the `dropna` function. The expectation is there should be a count of 0 nulls for each Series.

  ```python
  csv_data_cleaned.isnull().sum()
  ```

    ![LP_Ins_Data_Cleansing_No_Of_Null_2.PNG](Images/LP_Ins_Data_Cleansing_No_Of_Null_2.PNG)

* Pandas also offers a function to identify duplicate rows in a dataframe. Duplicate rows are important to check because they can result in increased wait times for processing. Duplicate rows will also skew data aggregations, inflating aggregated numbers. Duplicate rows can be identified using the `duplicated` function. The function will check for duplicates based off of indexes or based off of the chosen field. The function returns `True` or `False` depending on whether or not the value for that index/series is duplicated.

    ```python
    # Checking duplicates
    csv_data.duplicated()
    csv_data['customer_no'].duplicated()
    ```

    ![LP_Ins_Data_Cleansing_Duplicated_Check.PNG](Images/LP_Ins_Data_Cleansing_Duplicated_Check.PNG)

* Duplicate rows can be cleansed using the `drop_duplicates` function. This function can be executed against a DataFrame or a Series.

  ```python
  # Cleaning duplicates
  csv_data.drop_duplicates()
  ```

Live code a few data quality checks that are especially relevant for financial data.

* FinTech is all about manipulating Financial Data. Inspecting numeric values and gauging the quality of numerical data is going to be critical to student success when analyzing and aggregating data. A quick and easy way to confirm the quality of a numeric value is to sample the data and conduct a spot check!

    ```python
    # Generate sample of DataFrame to inspect for issues with numerical data
    csv_data.head()
    ```

    ![LP_Stu_Data_Cleansing_Head_Currency.PNG](Images/LP_Stu_Data_Cleansing_Head_Currency.PNG)

* Because the `order_total` field has currency symbols in the values, numeric operations cannot be performed. `order_total` is actually interpreted by Pandas to be of type `object` rather than `float` because of these symbols. Pandas does not have an out of the box cleaning function for removing symbols from numeric fields. A custom cleaning function/operation will need to be created to remove these symbols from the dataset. The cleaning function/operation can be created by leveraging and combining other Pandas functions (i.e. the Pandas `replace` function).

    ```python
    # Cleaning identified numeric fields with $ symbol
    csv_data['order_total'] = csv_data['order_total'].str.replace('$', '')
    csv_data['order_total']
    ```

    ![LP_Ins_Data_Cleansing_Currency_Clean.png](Images/LP_Ins_Data_Cleansing_Currency_Clean.png)

* Once currency symbols have been removed from the numeric field, the field can be converted to the appropriate data type.

  ```python
  csv_data.dtypes
  csv_data['order_total'] = csv_data['order_total'].astype('float')
  csv_data.dtypes
  ```

  ![LP_Ins_Data_Cleansing_AsType.PNG](Images/LP_Ins_Data_Cleansing_AsType.PNG)

* Lastly, flagging malformed data values streamlines the process of identifying and correcting data quality issues. Flagging is the process of creating an indicator field that will indicate whether or not a data value in a series passed the data quality check. If the value passes, the indicator will be `False`; if not, the value will be `True`. Flagging can be an alternative to actual data cleaning, especially if the two tasks need to be decoupled. A value can be flagged as malformed, and then cleaned at a later point in time. Consider the example of identifying nulls for field `customer_no`.

  ```python
  csv_data['null_err_chk'] = csv_data['customer_no'].isnull()
  csv_data
  ```

  ![LP_Ins_Data_Cleansing_Null_Check.PNG](Images/LP_Ins_Data_Cleansing_Null_Check.PNG)
