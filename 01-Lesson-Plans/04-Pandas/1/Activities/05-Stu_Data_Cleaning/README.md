## Spring Cleaning!

It's that time of year again: the end of the fiscal year and the time to begin Financial Spring Cleaning! Within a month, auditors will be camped out at your investment firm, inspecting everyone's trades and the company's end-of-year financial statements. All of the traders in the firm are under a lot of pressure to finalize their portfolio earnings and deliver them to their managers. Everyone, except you.

You automated your end-of-year financial reporting last week, and now you're using the pipeline to help out Harold with his reports. Before loading Harold's stock ticker data into Pandas, you open the Excel file he sent you, and look at the quality of the data. You realize that Harold has not subscribed to any data quality standards and that the data is a mess.

For this activity, use Pandas to clean Harold's portfolio data to get it fit for use.

## Instructions

Using the [starter-file](Unsolved/Core/spring_cleaning.ipynb) provided, and Harold's financial [data](Resources/stock_data.csv), complete the following steps:

1. Load CSV data into Pandas using `read_csv`.

2. Identify the number of rows and columns (shape) in the DataFrame.

3. Generate a sample of the data to visually ensure data has been loaded in correctly.

4. Identify the number of records in the DataFrame, and compare it with the number of rows in the original file.

5. Identify null records by calculating average percent of nulls for each Series. Hint: Will require `mean` function.

6. Drop null records.

7. Validate all nulls have been dropped by calculating the `sum` of values that are null.

8. Default null `ebitda` values to 0.

9. Check to ensure there are no null `ebitda` values using the `sum` function.

10. Remove duplicate rows.

## **Challenge**

Now that nulls and duplicates have been wrangled, clean and wrangle the data a little more by removing the `$` currency symbols from the `price` field. Then, use the `astype` function to cast `price` to a `float`. Complete the challenge activity using the [starter-file](Unsolved/Challenge/spring_cleaning.ipynb) provided.

### Hint

Pandas offers a `replace` function that can be executed against a Series. Documentation can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html).
