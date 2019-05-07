# Unit 5 - How do you like them Apps

![Financial Planner](Images/financial-planner.png)

## Background

The consumer division of Harold's company has decided to offer budgeting and financial planning services to customers. They want to build a report for customers that links to their banking and investment accounts and automatically refreshes the data and charts on login. However, some of the calculations are tricky, and Harold could really use some help connecting the accounts and simulating the retirement investment projections. Luckily, there are APIs available to obtain account transactions and fetch retirement portfolio prices.

In this homework assignment, you will help Harold complete the following tasks:

1. [Budget Analysis with Plaid](#Budget-Analysis)
2. [Retirement Planner](#Retirement-Planner)
3. [Financial Report](#Financial-Report)

- - -

### Files

[Budget Starter Notebook](Starter_Code/account_summary.ipynb)

[Retirement Planner Starter Notebook](Starter_Code/portfolio_planner.ipynb)

- - -

### Instructions

#### Budget Analysis

In this section, you will use the Plaid API to obtain transaction and account data for the budget analysis section of the report.

Follow the steps outline in the budget starter notebook to complete the following:

1. Generate a Plaid access token to access the Developer Sandbox.

2. Use the Access token to fetch account transactions from the sandbox. You should fetch the last 90 days of transactions from the sandbox using the following institution:

    ```python
    INSITUTION_ID = "ins_109508"
    ```

3. Perform basic budget analysis on the sandbox transaction and generate the following plots:

* Expenses per category

* Expenses per month

4. (Optional Challenge) Use the API to fetch income data from the sandbox and print the following:

* Last Year's Income Before Tax

* Current Monthly Income

* Projected Year's Income Before Tax

#### Retirement Planner

In this section, you will use the IEX API to fetch historical closing prices for a retirement portfolio and then run monte carlo simulations to project the portfolio performance at 30 years.

Follow the steps outline in the budget starter notebook to complete the following:

1. Use the IEX API to fetch historical closing prices for a traditional 60/40 portfolio using the `SPY` and `AGG` tickers to represet the 60% stocks (SPY) and 40% bonds (AGG).
2. Run a Monte Carlo Simulation of 1000 runs and 30 years for the 60/40 portfolio and plot the results.
3. Slice the last day prices from the simulation data and calculate the 95% confidence interval.
4. Slice the last day prices from the simulation data and plot a histogram of the last day's prices.
5. (Optional Challenge) Calculate the lower, median, and upper quantiles for the monte carlo data and plot the projections as a prediction of the portfolio returns using a 90% confidence interval.

  ![projected-returns.png](Images/projected-returns.png)

#### Financial Report

In this section, you will compile an example financial report to present to the development team. The report should be written as a Markdown file and include the following sections:

1. Budget Analysis - Summarize the transaction data from the budget analysis and include images for each chart and table produced.
2. Retirement Planning - Summarize the retirement portfolio anlaysis and include the charts for the Monte Carlo simulation.

- - -

### Resources

[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

- - -

### Examples

Show good examples

- - -

### Hints and Considerations

[Plaid API Docs](https://plaid.com/docs/)

[IEX Financial API Docs])(https://addisonlynch.github.io/iexfinance/stable/)

- - -

### Submission

* Create Jupyter Notebooks for the analysis and planner and host the notebooks on Github.

* Include a Markdown Financial Planner report that summarizes your assumptions and finding and include this report in your Github repo.

* Submit the link to your Github project to Bootcampspot.
