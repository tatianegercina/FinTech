# Unit X—Zen and the Art of Portfolio Construction

![Yen Photo](Images/unit-10-readme-photo.png)

## Background

Good portfolio construction is a big deal, because it can determine when you'll have enough money to retire, pay for a house, or cover for a rainy day. If you don't need the money immediately, it generally makes sense to build a portfolio of risky investments, which over the long-term will earn a higher return. But if you might need that money before then, it may make sense to have a portfolio that is less risky on a daily basis. You've learned about how diversification can reduce daily portfolio risk, and of the relationship between risk and return. In this homework, you'll use the statistical methods you've learned in order to construct a portfolio that fits your specific retirement goals. You'll also model the trade-off between risk and return, and use correlation to improve the diversification of your investments.

As these methods have practical implications at the personal level, they have practical implications in industry as well. In particular, firms offering investment advice use Monte Carlo simulation to tailor portfolios to individual's risk tolerances and retirement goals. Trading firms and banks both use Value-at-Risk and diversification to construct better performing portfolios and to understand worst-case scenarios. 

You will gain proficiency in the following tasks:

1. Simulating Portfolios to Plan for Retirement with Monte Carlo Simulation
2. Constructing Portfolios and Analyzing Daily Risk


- - -

### Files

[Simulating Portfolios to Plan for Retirement](Starter_Code/portfolio_planner.ipynb)

[Analyzing Daily Portfolio Risk](Starter_Code/optimizing_portfolio_risk.ipynb)

[Portfolio Planner Stock Data CSV File](Starter_Code/portfolio_planner_stock_data.csv)

[Portfolio Risk Data CSV File](Starter_Code/etf_data.csv)

- - -

### Instructions

#### Simulating Portfolios to Plan for Retirement

In this notebook, you will use the iexfinance or AlpacaTrade API and use Monte-Carlo simulation to investigate different retirement scenarios and investment portfolios combinations.

Follow the steps outlined in the [portfolio planner](Starter_Code/portfolio_planner.ipynb) starter notebook to complete the following:

1. Data Collection: Read in historical stock and bond returns either live from an API, or directly from a CSV file.
2. Monte Carlo Simulation: Conduct a Monte Carlo Simulation to forecast returns from an investment portfolio comprised of 60% equities and 40% bonds.
3. Retirement Analysis: Construct confidence intervals on the simulated portfolio to determine best, worst, and most likely investment outcomes.

Use the results of the Monte-Carlo analysis and modeling to answer the following questions:

1. Given an initial investment of $100,000, what is the expective cumulative return in 30 years for the worst, best, and most likely scenario?
2. If you want to receive at least $30,000 per year from the portfolio in retirement, will a 4% withdraw rate from that portfolio meet or exceed that amount at the 10th percentile?
3. How would a 50% increase in the initial investment amount affect the 4% retirement withdrawal?


#### Analyzing Daily Portfolio Risk

In this notebook, you will analyze short and long-term portfolio risk. You'll first construct portfolios optimized for minimal risk by analyzing correlations and visualizing using pandas as matplotlib. You'll then better quantify portfolio risk by calculating your portfolio's Value-at-Risk (VaR). 

Follow the steps outlined in the [optimizing portfolio risk](Starter_Code/portfolio_planner.ipynb) starter notebook to complete the following:

1. Data Collection: Use iex API, Alpaca API, or the provided CSV to read in and organize the data.
2. Portfolio Optimization: Use correlation and visualization techniques to build portfolios and contrast investment risk.
3. Risk Analysis: Measure Value-at-Risk of your portfolio against a benchmark portfolio.

Use the results of the risk analysis and modeling to answer the following question:

* Does this risk-optimized portfolio perform better or worse that a typical benchmark equity portfolio?

- - -

### Hints and Considerations

* Monte-Carlo analysis takes a given mean and standard deviation and then simulates future returns.
* Stocks with weak or negative correlation, when assembled into a portfolio, tend to exhibit the lowest risk.  

- - -

### Submission

* Create Jupyter Notebooks for the analysis and host the notebooks on GitHub.

* Include a Markdown that summarizes your models and findings and include this report in your GitHub repo.

* Submit the link to your GitHub project to Bootcampspot.
