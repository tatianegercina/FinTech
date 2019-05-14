# Three-Year Loans

The higher-ups at Harold's firm want to know how to better target their customers who are looking for three-year loans. As a result, Harold's manager wants Harold to look into a compilation of loan data, and filter out what is necessary to generate insights regarding customers who have been granted three-year loans.

Use the Pandas library to help Harold slice and dice the loan data to answer the following questions:

1. What kind of employees seem to ask for three-year loans most?
2. What are three-year loans generally used for?
3. What is the difference between counts of three-year loan customers with annual incomes greater than 80,000 compared to those with annual incomes less than 80,000?
4. What is the difference between interest rates for customers with annual incomes greater than 80,000 compared to those with annual incomes less than 80,000?

## Instructions

* Import necessary libraries and dependencies.

* Read in the `loans.csv` data.

* Show the first `10` records of the data.

* View summary statistics for the `loans.csv` data.

* Create a subset DataFrame `filtered_df` by filtering out the important columns: `loan_amnt`, `term`, `int_rate`, `emp_title`, `annual_inc`, and `purpose`.

* Filter `filtered_df` by row values where `term` is equal to `36 months` so as to only focus on the three-year loan records.

* Modify rows with `term` values equal to `36 months` to be `3 Years` (Harold's manager wants to see this).

* Use the `isnull()` function to modify rows with `emp_title` values equal to `NaN` to be `Unknown` (Harold's manager wants to see this).

* View summary statistics for `term_df` after all modifications.

* Use the `value_counts()` function on the `emp_title` column of the `term_df` DataFrame to see the unique value counts for employee titles of three-year loan customers.

* Use the `value_counts()` function on the `purpose` column of the `term_df` DataFrame to see the unique value counts for loan purposes of three-year loan customers.

* Filter `term_df` by rows with `annual_inc` greater than `80000` and use the `mean()` function to see the average `int_rate` of three-year loan customers with annual incomes greater than $80,000.

* Filter `term_df` by rows with `annual_inc` less than `80000` and use the `mean()` function to see the average `int_rate` of three-year loan customers with annual incomes less than $80,000.

* Solve the questions that Harold's manager wants the answers to.

## Hints

* View the pandas documentation for questions on how to use the above functions: [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)