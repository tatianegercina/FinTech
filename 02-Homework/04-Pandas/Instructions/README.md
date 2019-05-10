# Unit 4 Assignment - A Whale off the Port(folio)

![Image Goes Here]()

## Background

The investment division of Harold's company has been investing in algorithmic trading strategies -some of the investment managers love it and others hate it- but they ALL think their way is the best. 

They come to Harold with a challenge- if you're so great at Python/Pandas, can you resolve this and tell us which of our portfolios is performing best across MANY dimensions of 'success' (volatility, returns, risk, sharpe ratios)? You will get several of the firm's algo-made portfolio returns, and for comparison, some that represent the portfolios of famous ""whale"" investors like Warren Buffett and some from big hedge/mutual funds. 

You have to make a tool that analyzes and visualizes the major metrics of the portfolios across all the dimensions and tell us which outperformed the others."

In this homework assignment, you will be accomplishing three main tasks:

1. [Read in and Wrangle Return Data](#Datamunge)
2. [Compare Benchmark Performance](#BenchmarkComparison)
3. [Visualize and Group/Describe Annual Results](#DescribeAnalyze)

- - -

### Instructions

#### Datamunge

1. Read in each of the different portfolio return data. Some are dataframes, some are series.  
* Whale Returns
* Algo Returns 
* S&P 500 Returns
2. For each of the above, set thier index to be daily datetime.
3. Construct a dataframe of all these returns together.

#### BenchmarkComparison

1. After any nan cleaning, construct and plot cumulative returns. Does anything beat the performance of the S&P 500? 
2. As we've learned, it's not all about returns--it's about risk (volatility) too. Calculate the standard deviation for each portfolio. Which portfolios are riskier than the S&P 500? 
3. Risk changes over time. Managers change, investment strategies are modified, and equity markets fluctuate. Plot the rolling standard deviation of the firm's algo portfolios along with the rolling standard deviation of the S&P 500. Does risk increase for each of the portfolios at the same time risk increases in the S&P?
4. Let's get serious and quantify this! Construct a correlation table between Algo, Whale, and S&P 500 returns. Who's returns seem to mimick most closely the S&P?  
5. Last, plot a rolling beta between the firms algo portfolio returns and S&P 500 returns. Which portfolio seems more sensitive to movements in the S&P 500?
*Bonus Points! Can you plot the beta line using SeaBorn? 

#### DescribeAnalyze

In reality, investment managers and thier institutional investors look at the ratio of return-to-risk, and not just returns alone. (After all, if you could invest in one of two portfolios, each offered the same 10% return, yet one offered lower risk, you'd take that one, right?) 

1. Using the daily returns dataframe, construct and print() annualized sharpe ratios, and plot() these sharpe ratios using a barplot. On the basis of this performance metric, do our algo strategies outperform both 'the market' and the whales? 

2. The investment managers also want to compare the year-by-year performance of these funds over the years. Using groupby(), produce a dataframe that displays the total annual percentage performance of each portfolio, by year. Who seems to have torn away from the rest of the pack? 
- - -

### Resources

[Pandas API Docs] (https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- - -

### Hints and Considerations

All of the pandas functions we've learned this week will be really useful for this homework assignment. By working your way through this, you're on your way to true pandas mastery.

- - -

### Submission

Create a Jupyter Notebook that contains your analysis and visualizations. Make sure to use head() or tail() when you want to look at your data but don't want to print a giant dataframe. In discussing your analysis (i.e., answering the questions), put them into 'Raw NBConvert' cells throughout the report, where relevant.
