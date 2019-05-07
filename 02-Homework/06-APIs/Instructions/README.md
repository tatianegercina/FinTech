# Unit 5 - How do you like them Apps

![Financial Planner](Images/financial-planner.png)

## Background

The consumer division of Harold's company has decided to offer budgeting and financial planning services to customers. They want to build a report for customers that links to their banking and investment accounts and automatically refreshes the data and charts on login. However, some of the calculations are tricky, and Harold could really use some help connecting the accounts and simulating the retirement investment projections. Luckily, there are APIs available to obtain account transactions and fetch retirement portfolio prices.

In this homework assignment, you will help Harold complete the following tasks:

1. [Budget Analysis with Plaid](#Budget-Analysis)
2. [Retirement Planner](#Retirement-Planner)
3. [Report Generation](#Report-Generation)

- - -

### Files

[Budget Starter Notebook](Starter-Code/budget_analysis.ipynb)

[Retirement Planner Starter Notebook](Starter-Code/retirement_planner.ipynb)

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
3. Slice the last day prices from the simulation data and plot a histogram.
4. (Optional Challenge) Calculate the lower, median, and upper quantiles for the monte carlo data and plot the projections as a prediction of the portfolio returns using a 90% confidence interval.

  ![projected-returns.png](Images/projected-returns.png)

#### Do Z

Instructions for doing Z

- - -

### Resources

Resources that will help students

- - -

### Examples

Show good examples

Show bad examples

- - -

### Hints and Considerations

Share ideas or hints for the best way to proceed with the homework

- - -

### Submission

Tell the student how they will submit the homework
