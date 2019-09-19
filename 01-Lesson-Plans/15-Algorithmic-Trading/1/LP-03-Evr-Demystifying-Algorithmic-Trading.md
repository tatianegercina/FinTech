### 3. Instructor Do: Reading CSVs (10 min)

The goal of this part of the lesson is to get students comfortable with reading CSV files into Pandas. Financial data is commonly converted from other formats (e.g., an Excel file) to CSV so that it can be manipulated by programs like Pandas. Learning how to read CSV data into Pandas is the first step in getting students started with creating automated analytics pipelines.

**Files:**

* [reading_csvs.ipynb](Activities/01-Ins_Reading_CSVs/Solved/reading_csvs.ipynb)

* [sales.csv](Activities/01-Ins_Reading_CSVs/Resources/sales.csv)

* [sales_no_header.csv](Activities/01-Ins_Reading_CSVs/Resources/sales_no_header.csv)

Introduce Pandas DataFrames and slack out the [Pandas DataFrame documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and [getting started guide](http://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe).

* A DataFrame is a special data structure in Pandas that is designed to work with tabular data (data that has rows and columns like a spreadsheet) and provides some useful functions to help analyze and manipulate tabular data.

* A Pandas DataFrame can be created in several ways, such as using a Python dictionary, a list of lists, or reading data from an external file like CSV or JSON.

* The [Pandas DataFrame documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and [getting started guide](http://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe) are great resources if students want to learn more about creating DataFrames.

* Comma-separated values (CSV) is one of the most common file formats used to share data on finance. Students will start working with DataFrames by creating them from CSV files.

Start by opening the two CSV files in the [Resources](Activities/01-Ins_Reading_CSVs/Resources) directory, `sales.csv` and `sales_no_header.csv` to show students the format of the data. Point out that one file has a header while the other does not. Refer back to these files during the demo as needed.

Next, open `reading_csvs.ipynb` and walk through the following aspects of the code with your students. Highlight the following in sequential order.

First, emphasize how to import Pandas.

* In order to use Pandas, the `pandas` library must be imported. Pandas is commonly aliased as `pd` at this time.

* The `Path` class is also imported from the [`pathlib` module](https://docs.python.org/3/library/pathlib.html) in order to deal with file paths across all operating systems without complexity.

  ```python
  import pandas as pd
  from pathlib import Path
  ```

Next, discuss the `read_csv` function.

* The `read_csv` function allows users to read a CSV file into a DataFrame.

* The function usually just needs the path to the file, which in this case is defined using the `Path` class.

  ```python
  csvpath = Path("../Resources/sales.csv")
  sales_dataframe = pd.read_csv(csvpath)
  sales_dataframe.head()
  ```

Then highlight the `head` function.

* The `head` function shows the first 5 rows of the data by default.

* `head` is a common function used to take a peek at the DataFrame to ensure everything loaded correctly.

  ![dataframe.png](Images/dataframe.png)

Now call attention to the `header` parameter for `read_csv`.

* The `header=None` parameter tells Pandas not to use the first row as the header. Because no header is specified, the column index numbers are used instead.

  ![header-none.png](Images/header-none.png)

* New headers can be supplied by assigning a new list of column names to the `columns` attribute.

  ![header-columns.png](Images/header-columns.png)

* It is common to generate high-level statistics when creating a DataFrame. In this case the Pandas `describe` function can be used.

  * The output of the function is summary statistics for numeric fields, including series counts, averages, minimum value, maximum value, and so on.

  * A limitation of the `describe` function is that it only calculates summary statistics for numeric values columns.

  ![describe_summary.png](Images/describe_summary.png)

Consult the Pandas documentation to read more about the [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function. Show the many options available in the function signature.

Explain that, while the most common scenario is to simply provide the path to the file, Pandas provides a lot of configuration options for almost any other situation that may arise when reading CSV files --- such as the parameters associated with the file path and header that were used in the demo code.

Congratulate students on reading their first CSV file into Pandas as this is an exciting moment because students can now harness the power of Pandas to work with tabular data! Ask if there are any questions before moving on.
