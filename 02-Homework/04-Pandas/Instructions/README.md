# Unit 4 Assignment - A Whale off the Port(folio)

![Portfolio Analysis](Images/portfolio-analysis.png)

## Background

The investment division of Harold's company has been investing in algorithmic trading strategies -some of the investment managers love it and others hate it- but they ALL think their way is the best.

Harold comes to you with a challenge- because you have just learned all of these new quantitative analysis techniques with Python/Pandas, can you help Harold determine which of the portfolios is performing best across MANY dimensions of 'success' (volatility, returns, risk, sharpe ratios)? You will get some of the firm's algo-made portfolio returns, and for comparison, some that represent the portfolios of famous ""whale"" investors like Warren Buffett (and some from big hedge/mutual funds).

You have to make a tool (analysis notebook) that analyzes and visualizes the major metrics of the portfolios across all the dimensions and tell us which outperformed the others.

You will then use that analysis to compare a custom portfolio of stocks that you chose to see how they compare to the other portfolios and the bigger market (S&P 500).

In this homework assignment, you will be accomplishing three main tasks:

1. [Read in and Wrangle Returns Data](#Data-Preparation)
2. [Determine how successful each portfolio is](#Quant-Analysis)
3. [Choose and evaluate a custom portfolio](#Custom-Portfolio)

- - -

### Files

[Whale Analysis Starter Code](Starter_Code/whale_analyis.ipynb)

### Instructions

#### Data Preparation

In this section, you will read and prepare several CSV files for analysis. The CSV files include Whale Portfolio Returns, Algorithmic Trading Portfolio Returns, and S&P 500 Historic Prices. You will need to follow the starter workbook to complete the following steps:

1. Use Pandas to read each of the CSV files listed as a DataFrame. Be sure to convert the dates to a `DateTimeIndex`.
2. Detect and remove null values.
3. Remove dollar signs from the numeric values and convert the data types as needed.
4. The Whale Portfolios and Algorithmic Portfolio CSV files contain daily returns, but the S&P 500 CSV file contains closing prices. You will need to convert the S&P 500 closing prices to daily returns.
5. Join the `Whale Returns`, `Algorithmic Returns`, and the `S&P 500 Returns` into a single DataFrame with columns for each portfolio's returns.

  ![returns-dataframe.png](Images/returns-dataframe.png)

#### Quant Analysis

Now that the data is all cleaned up, you can start to analyze the data to see if any of the portfolios outperform the stock market (i.e. the S&P 500).

Performance Analysis:

1. Calculate and plot cumulative returns. Does anything beat the performance of the S&P 500?
2. Calculate the cumulative terms by Month and Year. What were the best returns in 2017? What were the best returns for December of 2018?

Risk Analysis:

1. As we've learned, it's not all about returns, it's about risk (volatility) too. Create a box plot for each of the returns. Which box has the largest spread? Which has the smallest spread?

2. Let's try and quantify what we see with the box plot using some statistics. Calculate the standard deviation for each portfolio. Which portfolios are riskier than the S&P 500?

Rolling Statistics:

1. Risk changes over time. Managers change, investment strategies are modified, and equity markets fluctuate. Plot the rolling standard deviation of the firm's portfolios along with the rolling standard deviation of the S&P 500. Does risk increase for each of the portfolios at the same time risk increases in the S&P?

2. Let's get serious and quantify this! Construct a correlation table between Algo, Whale, and S&P 500 returns. Who's returns seem to mimick most closely the S&P?

3. Last, pick one of the portfolios and plot a rolling beta between that portfolio's returns and S&P 500 returns. Does the portfolio seem sensitive to movements in the S&P 500?

Sharpe Ratios:

In reality, investment managers and their institutional investors look at the ratio of return-to-risk, and not just returns alone. (After all, if you could invest in one of two portfolios, each offered the same 10% return, yet one offered lower risk, you'd take that one, right?)

1. Using the daily returns, calculate and plot these sharpe ratios using a bar plot. On the basis of this performance metric, do our algo strategies outperform both 'the market' and the whales?

#### Custom Portfolio

Harold is ecstatic that you were able to help him prove that his algorithmic trading portfolios are doing so well compared to the Market and other Whales. You start wondering though if you could pick your own portfolio that does just as well as the algos. Visit The [Nasdaq's Historical Price Data](https://www.nasdaq.com/aspx/historical_nocp.aspx?symbol=COST&selected=COST) and choose 3-5 stocks for your own portfolio. Download the data as CSV files and calculate the portfolio returns. Then, try adding your portfolio returns to the DataFrame with all of the other portfolios and re-run your analysis from above. How does your portfolio fair?

- - -

### Resources

[Pandas API Docs] (https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- - -

### Hints and Considerations

All of the pandas functions we've learned this week will be really useful for this homework assignment. By working your way through this, you're on your way to true Pandas mastery.

Make sure to use head() or tail() when you want to look at your data but don't want to print a giant DataFrame.

- - -

### Submission

* Create a Jupyter Notebook that contains your data preparation, analysis and visualizations.  In discussing your analysis (i.e., answering the questions), add raw text (Markdown) cells to the report to document your findings.

* Submit your Notebook to a new Github repository.

* Add the web url of your github repository to Bootcampspot.
