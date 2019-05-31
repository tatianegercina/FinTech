## 4.1 Lesson Plan - Meet Pandas

---

### Overview

Today's class will introduce students to a powerful analytics library called Pandas. Pandas is a software library designed specifically for data analytics and time series analysis, which are super useful features for quantitative analytics! This lesson will teach students how to create DataFrames, locate data with indexing, clean data, and create basic data visualizations to tackle financial tasks.

### Class Objectives

By the end of class, students will be able to:

* Describe the benefits of Pandas over spreadsheets to manipulate data on financial use cases.
* Explain what a dataframe is and how it differs from a series.
* Create dataframes from CSV files and becoming confident using the basic commands to manipulate them.
* Demonstrate the ability to clean data using the dataframe built-in commands.
* Manipulate with confidence indexes on dataframes.
* Describe the basic theory and calculations of returns using Pandas.
* Create basic data visualizations with Pandas built-in functions to present preliminary results.

### Instructor Notes

* After learning how to create basic scripts with Python, students are eager to start doing financial analysis beyond the capabilities of Microsoft Excel. In this lesson, students will discover an amazing library for financial analysis that has many benefits over using Excel. Learning about these features and seeing how easy it is to use them will be very exciting for students.

* Students will focus on the basics of Pandas and then learn how to apply Pandas to calculate and visualize daily returns. Not all students may have the financial background to understand returns, so leverage the finance savvy students to help their partners when they get stuck. Be sure to spend extra time explain the returns calculations as they will use this for the remainder of the week.

* Indexing might be challenging for students, so live coding the examples and spending extra time in the review may be necessary to help them understand the fundamentals. Encourage students to practice these techniques after class to gain mastery.

* Data cleaning is an art and not an exact science, so this class focuses on common data cleaning techniques. Each dataset will have unique characteristics and may or may not need the same cleaning steps, but these techniques will help them with most of their data cleaning challenges.

If there are some curious students who want to learn more, [feel free to slack out this link](https://www.kaggle.com/chrisbow/kernels?sortBy=relevance&group=everyone&search=Cleaning+data+with+Python&page=1&pageSize=20&userId=1541110) with some guides and challenges to learn more about data cleaning using Python.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students to the first Pandas day, Today they will start discovering one of the most powerful libraries on python to analyse and manipulate data, so remark to the class that using Pandas is one of the most important superpowers as FinTech professionals.

Mention to the class the fact that Pandas was created by [Wes McKinney](https://en.wikipedia.org/wiki/Wes_McKinney) to offer a high performance and flexible tool for performing quantitative analysis on financial data.

Explain that Pandas provides many advantages over Excel through it's data structures and built-in functions for analyzing data.

Explain to students that they have already installed Pandas through Anaconda, so they don't need to install additional libraries by now. However, if they have issues running Pandas then they can use a free notebook by [Google Colab](https://colab.research.google.com/) and troubleshoot their installation with a TA during a break or office hours.

### 2. Instructor Do: Why Pandas (5 mins)

Students spent an entire day learning Python, and now they are transitioning to learning Pandas. Students need to understand why they are learning Pandas and the relationship between Pandas and Python. In this activity, students will learn the features and advantages of using Pandas. They will also learn how using Pandas can alleviate some of the stressors and challenges presented by Excel.

**Files:**

* [Unit 4.1 Slides](https://docs.google.com/presentation/d/1OyHSaY2IlRT7ncexJgjimA7zulBWV67_Pr5XdS6kyYQ/edit?usp=sharing)

Open the slides and start talking about how awesome spreadsheets are (slide 4).

> "Since spreadsheets appeared in [1969 when LANPAR was first used by the plant budgeting operations of AT&T](http://www.renepardo.com/), through [VisiCalc in 1970](https://en.wikipedia.org/wiki/VisiCalc) to [Microsoft Excel in 1987](https://en.wikipedia.org/wiki/Microsoft_Excel), they transformed the finance and quants analysis forever; however as more data became available and complexity increased, not everything is what it used to be."

Open the discussion (slides 5 and 6) by questioning the class about the pain points they have suffered themselves while dealing the data using a spreadsheet.

You can start a collaborative document on Google Drive to allow students to share their experiences, you can keep this document as a time capsule to be opened at the end of the unit to assess what they have learned and how they can overcome now those pain points using Pandas.

Use the rest of the presentation to introduce Pandas as the light at the end of a dark tunnel, like a beautiful oasis in the middle of the desert, let them know and get exited about the infinite possibilities Pandas will offer them for data analysis as FinTech professionals. Remember to remark that Pandas has its origins on the financial realm.

If there is time, you can end the discussion by presenting some of the applications that Pandas has on different business areas like the ones [discussed here](https://data-flair.training/blogs/applications-of-pandas/).

### 3. Instructor Do: Reading CSVs (10 mins)

The goal of this activity is for students to learn how to read CSV files into Pandas. Financial data is commonly converted from other formats (i.e. Excel XLS) into CSV so that it can be manipulated by programs like Pandas. Learning how to read CSV data into Pandas is the first necessary step in getting students started with creating automated analytics pipelines.

**Files:**

* [reading_csvs.ipynb](Activities/01-Ins_Reading_CSVs/Solved/reading_csvs.ipynb)

* [sales.csv](Activities/01-Ins_Reading_CSVs/Resources/sales.csv)

* [sales_no_header.csv](Activities/01-Ins_Reading_CSVs/Resources/sales_no_header.csv)

* A Pandas DataFrame can be created in several ways such as using a python dictionary, a list of lists, or reding data from an external file like CSV or JSON. Slack out the [Pandas DataFrame documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) as well this [getting started guide](http://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe) for students to use as a reference.

* Comma-separated values (CSV) is one of the most common file formats used to share data on finance, so students will start working with DataFrames by creating them reading data from CSV files.

Start by opening the two CSV files in the Resources directory to show students the format of the data. Point out that one file has a header while the other does not. Refer back to these files during the demo as needed.

Next, open the `reading_csvs.ipynb` file and highlight the following:

* The first step is to import the `pandas` library that is commonly referred as `pd`. The `Path` class is also imported from the [`pathlib` module](https://docs.python.org/3/library/pathlib.html) in order to deal with file paths across all operating systems without complexity.

  ```python
  import pandas as pd
  from pathlib import Path
  ```

* The Pandas library provides a `read_csv` function that can read a CSV file into a DataFrame. The function usually just needs the path to the file, that in this it's defined using the `Path` class.

  ```python
  csvpath = Path("../Resources/sales.csv")
  sales_dataframe = pd.read_csv(csvpath)
  sales_dataframe.head()
  ```

* The `head` function will show the first 5 rows of the data by default. This is a very common function used to take a peek at the DataFrame to make sure that everything loaded correctly.

  ![dataframe.png](Images/dataframe.png)

* CSV files sometimes are missing headers. In this case, Pandas will incorrectly assume that the first row is the header.

  ![no-header.png](Images/no-header.png)

* The `header=None` parameter tells pandas not to use the first row as the header. Because no header is specified, the column index numbers are used instead.

  ![header-none.png](Images/header-none.png)

* New headers can be supplied by assigning a new list of column names to the columns attribute.

  ![header-columns.png](Images/header-columns.png)

Explain to students that while these examples cover the most common use-cases for reading csv files, there are sometimes other scenarios to consider. In these cases, they can refer to the official documentation for further guidance.

Visit the Pandas documentation for the [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function and show the many options available in the function signature. Explain that while the most common scenario is to simply provide the path to the file, Pandas provides a lot of configuration options for almost any other situation that may arise when reading CSV files.

Explore the documentation page with students to help them understand how to read and interpret the documentation. This will help demystify the documentation and encourage them to rely on it for future assignments.

Be sure to point out the parameters associated with the filepath and the header that was used in the demo code.

Congratulate students on reading their first CSV file into Pandas! This is an exciting moment because students can now harness the power of Pandas to work with tabular data!

### 4. Student Do: Reading Stock Data from a CSV File (10 mins)

**Instructions:**

* [README.md](Activities/02-Stu_Reading_CSVs/README.md)

**Files:**

* [reading_stock_data.ipynb](Activities/02-Stu_Reading_CSVs/Unsolved/reading_stock_data.ipynb)

* [amd_stock_data.csv](Activities/02-Stu_Reading_CSVs/Resources/amd_stock_data.csv)

### 5. Instructor Do: Review Reading CSVs (5 mins)

**Files:**

* [reading_stock_data.ipynb](Activities/02-Stu_Reading_CSVs/Solved/reading_stock_data.ipynb)

Start by explaining that a DataFrame is a special data structure in Pandas that is designed to work with tabular data (data that has rows and columns like a spreadsheet). A Pandas DataFrame also provides some useful functions to help analyze and manipulate the tabular data.

Since this is the first time students are exposed to Pandas, it's recommended to live code the solution to show students how the CSV file is read and how the built-ins functions works. Use [the solution](Activities/02-Stu_Reading_CSVs/Solved/reading_stock_data.ipynb) as a guide.

Open the starter file and live code the solution while explaining the following:

Explain that while this example created a DataFrame from reading a CSV file, there are actually several ways to create DataFrames such as creating a DataFrame from a dictionary or a list of lists. Slack out the [Pandas DataFrame documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) as well this [getting started guide](http://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe) for students to use as a reference.

* The first step is to import the Pandas library using its most common acronym `pd`. `Path` from the `pathlib` module is also imported to deal with relative file paths across all operating systems.

  ```python
  import pandas as pd
  from pathlib import Path
  ```

* A DataFrame can be created by reading a CSV file into Pandas. This example uses a Path object to specify the location of the CSV file. Pandas can then read that file and create a DataFrame to hold the data.

![Relative file path to CSV file](Images/05_relative_file_path.png)

* Once the DataFrame is created get the top 10 records and remark to students the importance of verifying if the CSV file has the columns names on the first line, so they can avoid losing the first record of data.

![First record as columns names](Images/05_first_record_as_columns_names.png)

* Fix the columns names by recreating the dataframe and highlighting the usage of the `header=None` parameter while reading the CSV file, notice to the class that this parameter could be used regardless the CSV files has a header or not in order to customize the columns names.

![Setting new columns names](Images/05_set_columns_names.png)

* Finally for the challenge part explain to students that getting the last rows is as easy as calling the `tail()` function of the DataFrame.

![Getting the bottom 10 rows](Images/05_using_df_tail.png)

Ask for any remaining questions before moving on.

### 6. Instructor Do: Column Manipulation (10 mins)

Reading CSV data into Pandas is an easy feat, but sometimes the DataFrame's schema/structure needs to change. This includes changing DataFrame column names, adding columns, and dropping columns. Students will learn how to use the various Pandas functions to perform each of these operations. It's important that students know how to create and curate DataFrames to their needs.

**Files:**

* [column_manipulation.py](Activities/03-Ins_Columns/Solved/column_manipulation.py)

Explain to students that a common first step in Data Wrangling is to fix or adjust column names and column values. This demonstration will cover the common techniques used to manipulate columns.

Demonstrate the fundamentals of column manipulation in Pandas:

* Pandas DataFrames have a `columns` attribute that shows the current column names.

  ![column-names.png](Images/column-names.png)

* The `columns` attribute can be assigned a new list of column values. This has certain restrictions such as the list of column names must match the number of columns in the DataFrame (no partial lists).

  ![replace-columns.png](Images/replace-columns.png)

* In order to replace or update selective column names, the `rename` function can be used. Simply provide a dictionary to the columns parameter that has the following format:

  ```python
  {
    "Old Column Name": "New Column Name"
  }
  ```

  ![rename-columns.png](Images/rename-columns.png)

* Columns can also be reordered by supplying a list of columns in the desired order.

  ![reorder-columns.png](Images/reorder-columns.png)

* New columns can be created by assigning a Pandas Series to a new Column name. This is similar to how dictionaries add values for new keys.

  ![create-columns.png](Images/create-columns.png)

* Sometimes, columns may need to be split into separate values. Pandas allows you to split a column based on a delimiter. In this case, the values are split by the whitespace between the names. The `expand=True` flag tells Pandas to create two new columns from the split. These columns can be assigned to new column names in the DataFrame.

  ![split-columns.png](Images/split-columns.png)

* Finally, columns that are no longer needed can be dropped using the `drop` function. Simply supply a list of the columns that should be dropped from the DataFrame.

  ![customer-drop-columns.png](Images/customer-drop-columns.png)

Send the solution file to students to use as a reference.

### 7. Instructor Do: Data Cleaning (10 mins)

In this activity, students will take part in a lecture and discussion about data cleaning. Students will learn what data cleaning is and why it is necessary, as well as common strategies for cleaning data. This module will be critical to students. Most of the data students will come across in the real world will be dirty and unusable.

**Files:**

* [Data Cleaning Slides]()

* [data_cleaning.ipynb](Activities/04-Ins_Data_Cleaning/Solved/data_cleaning.ipynb)

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

### 8. Students Do: Data Cleaning (15 mins)

In this activity, students will be given Harold's stock data and are asked to perform a series of data quality checks to ensure the data is ready for analytical use. The objective of the assignment is for the students to learn how to cleanse data using Pandas native functions (`count`,`value_counts`,`isnull`,`sum`,`mean`,`contains`, and `replace`).

**Files:**

* [spring_cleaning.ipynb](Activities/05-Stu_Data_Cleaning/Unsolved/Core/spring_cleaning.ipynb)

**Instructions:**

* [README.md](Activities/05-Stu_Data_Cleaning/README.md)

- - -

### 9. Instructor Do: Review Data Cleaning (5 mins)

**Files:**

* [spring_cleaning.ipynb](Activities/05-Stu_Data_Cleaning/Solved/Core/spring_cleaning.ipynb)

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

### 10. Instructor Do: Indexing (10 mins)

In this activity, students will demonstrate that they can locate and select data within a DataFrame through indexing. Indexing allows us to slice and dice our data so we can get or set values for any of the "cells" in our table.

**Files:**

* [indexing.ipynb](Activities/06-Ins_Indexing/Solved/indexing.ipynb)

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

### 11. Students Do: Three-Year Loans (20 mins)

Now that students have the conceptual knowledge to index and look up data, it's time they get some practice in completing the steps demoed by the instructor. xThis activity tests students abilities to understand DataFrame indexing to slice and dice the `loans.csv` data to generate insightful answers regarding three-year loan customers.

The `loans.csv` data is initially a compilation of many different columns and loan durations. Students will need to filter down to what is necessary and use functions on subsets of data to answer the questions set forth by Harold's manager.

**Instructions:**

* [README.md](Activities/07-Stu_Indexing/README.md)

**Files:**

* [loans.ipynb](Activities/07-Stu_Indexing/Unsolved/loans.ipynb)

### 12. Instructor Do: Review Indexing (5 mins) (Low)

**Files:**

* [loans.ipynb](Activities/07-Stu_Indexing/Solved/loans.ipynb)

Open the solution and explain the following with a dry walkthrough:

* Displaying an index of the first 10 rows is similar to what the `head()` function does; however, utilizing `iloc[]` gives you more control over the index ranges.

  ![First 10 Records](Images/first-10-records.png)

* The `iloc[]` function allows for selecting specific row and column indexes. In this case, the `:` keyword suggests that all rows will be kept from the `0`, `3`, `4`, `8`, `11`, `16` column indexes that will be selected.

  ![Specific Columns](Images/specific-columns.png)

* The `loc[]` function is able to combine conditionals with column value re-assignment to modify specific values within a DataFrame.

  ![row-modification-with-warning](Images/row-modification-with-warning.png)

* Sometimes this may lead to a `SettingWithCopyWarning` where pandas tries to set values on a copy of a slice of a DataFrame. Therefore, use the `copy()` function to establish a concrete object (rather than a pointer to an object) to alleviate the error.

  ![row-modification-without-warning](Images/row-modification-without-warning.png)

* The `value_counts()` function counts the frequency of unique values of a specific column or Series object.

  ![Unique Values](Images/unique-values.png)

* Combining the `loc[]` function with conditionals creates a subset of data that can be used to display summary statistics with the `describe()` function. This way, there is no need to separately call the `count()` and `mean()` functions.

  ![Subset Statistics](Images/subset-statistics.png)

Ask for any remaining questions before moving on.

### 13. Instructor Do: Pandas Visualizations (10 mins)

In this activity, students will learn through demonstration how to create charts using Pandas visualization functions. The instructor will demo how to plot data with and without indexes, as well as how to plot data using line and bar charts.

**Files:**

* [visualization.ipynb](Activities/08-Ins_Pandas_Visualization/Solved/visualization.ipynb)

Walk through the demo and explain the following:

* Pandas makes visualization easy by including a DataFrame `plot()` function; the `plot()` function uses data from a DataFrame to set x and y-axis data points.

* Plotting data without defining the index will only display the default index of each row in the DataFrame. In order to set the dates as the x-axis label, the `Date` column needs to be set as the index.

  ![line-chart-without-index](Images/line-chart-without-index.png)

* While setting the `Date` column as the DataFrame index, it's a good practice to convert date strings into datetime objects to have the flexibility of utilizing additional datetime functionality.

  ![set-index](Images/set-index.png)

* Make sure to drop the extra `Date` column after setting it as the index!

  ![drop-column](Images/drop-column.png)

* Plotting data with datetimes as the index now allows us to see the dates as the x-axis label of the line chart.

  ![line-chart-with-index](Images/line-chart-with-index.png)

* Use the `kind` parameter to the `plot()` function to specify different types of charts. The `plot()` function automatically defaults to generating a line chart.

  ![bar-chart](Images/bar-chart.png)

* Use the `figsize` parameter to the `plot()` function to increase or decrease the chart size. This is especially helpful when there are many x or y axis data points.

  ![bar-chart-large](Images/bar-chart-large.png)

### 14. Students Do: Market Analysis (20 mins)

For this activity, students will make three different charts using Pandas: pie chart, bar chart, and scatter plot. This activity will teach students how to create pie scatter charts in addition to bar and line plots. Instructors should walk around to review student progress as they complete the secret key activity. Questions and guidance may be required as this will be the first time students will have been exposed to pie charts and scatter plots.

**Files:**

* [market_analysis.ipynb](Activities/09-Stu_Pandas_Visualization/Unsolved/market_analysis.ipynb)

**Instructions:**

* [README.md](Activities/09-Stu_Pandas_Visualization/README.md)

### 15. Instructor Do: Review Market Analysis (5 mins)

**Files:**

* [market_analysis.ipynb](Activities/09-Stu_Pandas_Visualization/Solved/market_analysis.ipynb)

Open the solution and explain the following:

* Setting the `%matplotlib inline` feature is necessary to displaying the plots in the jupyter notebook file.

  ```python
  # Import libraries and dependencies
  import pandas as pd
  from pathlib import Path
  %matplotlib inline
  ```

* The `value_counts()` function returns a Series object representing the frequency of unique values of a Series object or column of a DataFrame.

  ![value-counts-function](Images/value-counts-function.png)

* The `plot` function defaults to line charts; however, the `kind` parameter allows one to alter the type of chart produced (i.e. pie, bar, etc.).

  ```python
  # Plot a pie chart from the distribution of company sectors
  sector_count.plot(kind='pie')
  ```

* A pie chart is best suited for representing the distribution of a whole category. In this case, the distribution of company sectors in the S&P 500. The plot shows that `Consumer Discretionary` companies hold the greatest weight or proportion amongst the S&P 500 companies.

  ![pie_chart](Images/pie.png)

* To create certain plots, it may be easier to create a subset of the original DataFrame. In this example, the `Symbol` and `Market Cap` columns can be selected as a subset of the original data.

  ```
  market_cap = sp500_companies_csv.loc[:, ['Symbol', 'Market Cap']]
  ```

* Make sure to set the index on DataFrames that are intended for plotting to display the correct labels. For example, the x-axis labels on a line chart.

* Use the `nlargest()` function to return the top `n` number of rows based on a particular DataFrame column.

  ![nlargest-function](Images/nlargest-function.png)

* A bar chart is best suited for comparing the values of several variables of the same type. In this case, the market caps of the top 20 companies in the S&P 500. The plot shows the varying market cap values of the top 20 market cap companies of the S&P 500.

  ![bar_chart](Images/bar.png)

* A scatter plot is best suited for comparing the relationships between two variables. In this case, the relationship between price and earnings. The plot shows that there is generally a range between which most companies tend to cluster around price and earnings; however, as earnings increase there seems to be a slight positive trend in price as well.

  ![scatter_plot](Images/scatter.png)

Ask for any remaining questions before moving on.

### 16. Instructor Do: Returns (10 mins)

The following activity introduces students to calculating daily returns with Pandas. Students are introduced to the concept of `ROIs`, the `pct_change` function, and cumulative returns. This activity will build upon skills taught to read in CSV data, manipulate and clean DataFrames, and plot data.

**Files:**

* [returns.ipynb](Activities/10-Ins_Returns/Solved/returns.ipynb)

Walk through the demo and explain the following:

* What is a return or Return on Investment (ROI)?

  > A Return on Investment (ROI) is a percentage calculation that signifies either a profit or loss relative to the initial cost of an investment. ROI calculations can be used to standardize and compare the investment performances of varying asset classes such as equities, bonds, real estate, etc.

  ```python
  # ROI = (Current Value of Investment - Cost of Investment) / Cost of Investment
  initial_investment = 100
  current_price = 110

  roi = (current_price - initial_investment) / initial_investment
  roi_pct = roi * 100
  print(f"ROI for an initial investment of ${initial_investment}"
        f"now priced at ${current_price}"
        f"is {roi} or {roi_pct}%")
  ```

  ```
  ROI for an initial investment of $100 now priced at $110 is 0.1 or 10.0%
  ```

* What are daily returns?

  > Daily returns are a series of returns calculated over the course of several days, with each daily return representing the relative increase or decrease in investment between days.

* The `shift()` function creates an offset of a DataFrame index by a specified amount. In this case, the index of the `sp500_csv` is offset by `1` to emulate the daily return formula.

  ![shift-function](Images/shift-function.png)

* The `pct_change()` function calculates the percentage difference between each element of a time series. Therefore, for time series data such as daily closing prices of a stock, using the `pct_change()` function conveniently produces a series of daily returns.

  ![pct-change-function](Images/pct-change-function.png)

* Plotting daily returns makes it easier to see overall variations in daily returns over a course of time. In particular, plotting daily returns make it easier to see high and low spikes compared to the general trend. Such spikes in daily returns may indicate a market event.

  ![Plot of Daily Returns](Images/daily-return-plot.png)

* What are cumulative returns?

  > Cumulative returns are a series of returns, with each return representing the relative increase or drecrease in price of an asset at time `t` compared to the initial price of that asset at time `t0`. Cumulative returns describe the progression of the Return on Investment of an asset over time.

* The `cumprod()` function multiplies each number in a series with the next successive number until the end of the series.

* The equation `(1 + daily_returns).cumprod() - 1` therefore means that each daily return is expressed as a multiplier (ex. daily return of 0.5% is 1.005), the `cumprod()` function cumulatively multiplies each number with its successive number, and the `-1` brings the result from a multiplier expression back to a typical return value scale (ex. daily return of 0.5% is 0.005).

  ![cumprod-function](Images/cumprod-function.png)

* Plotting cumulative returns makes it easier to visualize the profitability of a single asset, and in particular, the profitabilites of several asset classes over time. In this case, the plot shows that the S&P 500 grew more than 50% from 2014 to 2019.

  ![Plot of Cumulative Returns](Images/cumulative-return-plot.png)

Now that students know how to calculate and plot returns, students will practice doing this by analyzing and plotting historical AMD data for Harold.

### 17. Students Do: Returns Over Date Ranges (20 mins)

In this activity, Harold's manager wants Harold to analyze the last 10 years of historical price data for AMD and plot the daily returns over the last 1, 3, 5, and 10 year time periods. In addition, Harold's manager wants to see the differences in average daily returns for each time period to perhaps understand whether a short or long term perspective should be used in prospecting AMD as a potential candidate.

Help Harold analyze the last 10 years of AMD stock data.

**Instructions:**

* [README.md](Activities/11-Stu_Returns/README.md)

**Files:**

* [returns_over_date_ranges.ipynb](Activities/11-Stu_Returns/Unsolved/returns_over_date_ranges.ipynb)

### 18. Instructor Do: Review Returns Over Date Ranges (5 mins)

**Files:**

* [returns_over_date_ranges.ipynb](Activities/11-Stu_Returns/Solved/returns_over_date_ranges.ipynb)

Instruct the students to take 3 minutes to complete a turn and teach activity. Students should:

* Work with their neighbors and share two new things they learned about returns

* Share answers to the following questions: What is the value behind calculating cumulative returns? Why not just calculate daily returns over time?

With the remaining time, open the solution, and discuss the following points:

* We need to set the `%matplotlib inline` feature to display plots in Jupyter notebooks.

  ```python
  # Import libraries and dependencies
  import pandas as pd
  from pathlib import Path
  %matplotlib inline
  ```

* After reading in the csv as a DataFrame and doing some quick summary statistical analysis, data should be trimmed to match the needs of the requirements. In this case, only the `close` column is needed to calculate daily returns.

  ![drop-columns](Images/drop-columns.png)

* Setting the date as the index allows us to slice the DataFrame by specified date ranges using the `loc` function, which allows for `[start:end]` notation.

  ![datetime-index](Images/datetime-index.png)

* Notice however the hard-coding that had to be done to create the slice notations for each time period. It would be much more convenient to be able to choose a date and use a function to go 365 days prior to that date to create 1 year, 3 year, 5 year, and 10 year time chunks; `datetime` objects will help us do this in the future.

  ```python
  # Slice DataFrame into 1 year time frame
  daily_return_1_year = daily_return.loc['2018-04-30':'2019-04-29']
  daily_return_1_year
  ```

* The data shows that trading AMD in the short-term is potentially more profitable as the average daily return of a `1 Year` time frame is the highest at `0.004538` or `4.53%`.

Ask for any remaining questions before moving on.

### 19. Decompress

Before ending class, leave some encouraging remarks, and give students a space to vocalize their thoughts.

* Give students positive feedback; ensure them that they are all doing great. Not only have they learned Python, but now they've learned Pandas and have begun automating portfolio performance evaluation. They're one step closer to their goal of being masters of FinTech automation.

* Ask students the following questions:

  * What activity was the most enjoyable to complete? The most fulfilling?

  * What's the most stressful thing about programming?

  * What took you the most time to figure out?

  * Did you come across any shortcuts or unique ways to do things while completing the activities?

* Underscore that the students have been doing excellent at learning both financial and technical concepts. This is not an
easy feat. It takes skill, intellect and abstract thinking, and perseverance to make it this far. They should all pat themselves on the back.

* Underscore that the students have come a long way. Last week they learned Python. Now they're integrating Pandas and Matplotlib into their Python programs. Next they'll start using more advanced Financial calculations and functions, and eventually move onto working with APIs.

* Let the students know that office hours are available for anyone who might have additional questions; would like to review more; or would like to just talk Python, Pandas, Financial Portfolios, and/or FinTech!

### End Class
