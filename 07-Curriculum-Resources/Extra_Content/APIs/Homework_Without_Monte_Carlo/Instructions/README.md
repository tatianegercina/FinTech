# Unit 5 — How do you like them apps?

![Financial Planner](Images/financial-planner.png)

## Background

The Consumer Division of Harold's company has decided to offer budgeting and financial planning services to customers. They want to build a report for customers that links to their banking and investment accounts and automatically refreshes the data and charts on login. However, some of the calculations are tricky, and Harold could really use some help connecting the accounts. Luckily, there are APIs available to obtain account transactions.

In this homework assignment, you will help Harold complete the following tasks:

1. [Budget Analysis with Plaid](#Budget-Analysis)

2. [Financial Report](#Financial-Report)

---

### Files

* [Budget Starter Notebook](Starter_Code/account_summary.ipynb)

---

## Instructions

__Note__: The data produced from the api calls will vary depending on the dates used, causing results that vary from those pictured.

### Budget Analysis

In this section, you will use the Plaid API to obtain transaction and account data for the budget analysis section of the report.

Follow the steps outlined in the budget starter notebook (`account_summary.ipynb`) to complete the following:

1. Generate a Plaid access token to access the Developer Sandbox.

2. Use the Access token to fetch account transactions from the sandbox. You should fetch the last 90 days of transactions from the sandbox using the following institution:

    ```python
    INSTITUTION_ID = "ins_109508"
    ```

3. Perform basic budget analysis on the sandbox transaction and generate the following plots:

    * Spending Categories Pie Chart.

      ![Expenses per category](Images/spending-pie.png)

    * Spending Per Month Bar Chart.

      ![Expenses per month](Images/spending-month.png)

4. Use the API to fetch income data from the sandbox and print the following:

* Last Year's Income Before Tax.

* Current Monthly Income.

* Projected Year's Income Before Tax.

### Financial Report

In this section, you will compile a financial report to demo your calculations to the Consumer App Team. The report should be written as a markdown file and include a summary of the transaction data from the budget analysis and include images for each chart and table produced.

---

### Resources

* [Plaid API Docs](https://plaid.com/docs/)

* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

---

### Submission

* Create a Jupyter Notebook for the budget analysis and host the notebook on GitHub.

* Include a Markdown Financial Planner report that summarizes your assumptions and findings and include this report in your GitHub repo.

* Submit the link to your GitHub project to Bootcampspot.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
