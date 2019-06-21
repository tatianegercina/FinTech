# Three-Year Loans

The higher-ups at Harold's firm want to know how to better target customers who are seeking three-year loans. Harold's manager has asked him to review a compilation of loan data, and then filter out the necessary data to generate insights about customers who have been granted three-year loans. 

Follow the instructions to help Harold answer his manager's questions. 

## Instructions

Complete the following steps. 

1. Import the necessary libraries and dependencies.

1. Read in the `loans.csv` data.

1. Show the first `10` records of the data.

1. View summary statistics for the `loans.csv` data.

1. Create a subset DataFrame `filtered_df` by filtering out the important columns: 
    
    * `loan_amnt`
    * `term`
    * `int_rate`
    * `emp_title`
    * `annual_inc`
    * `purpose`

1. Filter `filtered_df` by row values where `term` is equal to `36 months` in order to focus on only three-year loan records.

1. Modify rows with `term` values equal to `36 months` to be `3 years`. (Harold's manager wants to see this.)

1. Use the `isnull()` function to modify rows with `emp_title` values equal to `NaN` to be `Unknown`. (Harold's manager wants to see this.)

1. View summary statistics for `term_df` after all modifications.

1. Use the `value_counts()` function on the `emp_title` column of the `term_df` DataFrame to see the unique value counts for employee titles of three-year loan customers.

1. Use the `value_counts()` function on the `purpose` column of the `term_df` DataFrame to see the unique value counts for loan purposes of three-year loan customers.

1. Filter `term_df` by rows with `annual_inc` greater than `80000`. Use the `mean()` function to see the average `int_rate` of three-year loan customers with annual incomes greater than $80,000.

1. Filter `term_df` by rows with `annual_inc` less than `80000`. Use the `mean()` function to see the average `int_rate` of three-year loan customers with annual incomes less than $80,000.

1. Help Harold answer the following questions for his manager: 

    * What kind of employee seems to ask for three-year loans most frequently?

    * What are three-year loans generally used for?

    * What is the difference between counts of three-year loan customers with annual incomes greater than 80,000, compared to those with annual incomes less than 80,000?

    * What is the difference between interest rates for customers with annual incomes greater than 80,000 compared to those with annual incomes less than 80,000?

## Hint

View the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) for additional explanations about using specific functions. 

- - - 

© 2019 Trilogy Education Services