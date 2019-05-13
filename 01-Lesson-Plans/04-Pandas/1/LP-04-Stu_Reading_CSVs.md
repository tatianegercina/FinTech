### 4. Student Do: Reading Stock Data from a CSV File (10 mins)

**Instructions:**

* [README.md](Activities/04-Stu_Reading_CSVs/README.md)

**Files:**

* [reading_stock_data.ipynb](Activities/04-Stu_Reading_CSVs/Unsolved/reading_stock_data.ipynb)

* [amd_stock_data.csv](Activities/04-Stu_Reading_CSVs/Resources/amd_stock_data.csv)

### 5. Instructor Do: Reading CSVs Review (5 mins)

**Files:**

* [reading_stock_data.ipynb](Activities/04-Stu_Reading_CSVs/Solved/reading_stock_data.ipynb)

Start by explaining that a DataFrame is a special data structure in Pandas that is designed to work with tabular data (data that has rows and columns like a spreadsheet). A Pandas DataFrame also provides some useful functions to help analyze and manipulate the tabular data.

Since this is the first time students are exposed to Pandas, it's recommended to live code the solution to show students how the CSV file is read and how the built-ins functions works. Use [the solution](Activities/04-Stu_Reading_CSVs/Solved/reading_stock_data.ipynb) as a guide.

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
