# Unit 6 Assignment

## Background

![Portfolio Analysis](Images/shutterstock_1099878122.png)

Congratulations! You have just been promoted to Quantitative Analyst for Trading Daze Inc. For your first assignment, you have been asked to analyze the returns for a portfolio of stocks. You will need to perform basic ROI calculations on each dataset to find the daily ROI and annualized returns. You can use that information to calculate all sorts of useful risk indicators such as volatility, Sharpe Ratios, and Annualized Sharp Ratios. Don't forget to include basic correlation analysis to make sure that you have a well-balanced portfolio of stocks. Finally, you will calculate the weighted total return for the portfolio and then try and find a portfolio balance of those stocks that improve the return. Happy Analyzing!

In this homework assignment, you will be accomplishing five main tasks:

1. [Collect Stocks](#Collect-Stocks)
2. [Analyze Daily Returns](#Analyze-Daily-Returns)
3. [Analyze Volatility and Risk](#Analyze-Volatility-Risk)
4. [Analyze Stock Correlation](#Analyze-Stock-Correlation)
5. [Analyze Portfolio Returns](#Analyze-Portfolio-Returns)

- - -

### Instructions

#### Collect Stocks

* Use the Quandl API to collect stocks from `Dec 31, 2017 - Present` for at least 5 different stocks.

* Save the stocks to a CSV file in order to reduce your total API calls to Quandl.

#### Analyze Daily Returns

* Calculate the `Normalized Adjusted Return` for all stocks and use this as a baseline to compare and visualize the performance for each stock.

  ![normalized_adjusted_returns](Images/normalized_adjusted_returns.png)

  ![normalized_area](Images/normalized_area.png)

* Calculate the Daily ROI and Log Daily ROI and visualize the results to identify spikes in the returns.

  ![daily roi](Images/daily_roi.png)

* Calculate and visualize the cumulative return.

  ![cumulative returns](Images/cumulative_returns.png)

* Calculate the annualized returns for all stocks.

* View the distribution of each stock's daily roi.

  ![stock distributions](Images/stock_distributions.png)

#### Analyze Volatility and Risk

* Use a box and whiskers plot to visualize the distribution of each stock to gain a sense of the risk and volatility.

  ![box plot](Images/box_plot.png)

* Calculate the Annualized Volatility.

* Calculate the Sharpe Ratio for the daily returns.

* Calculate the Annualized Sharpe Ratio.

#### Analyze Correlation

* Use Pandas to create a correlation table for each stock and plot the results as a heatmap.

  ![Correlation Heatmap](Images/correlation_heatmap.png)

#### Analyze Portfolio Returns

* Calculate the average annualized returns for each stock assuming an equal amount of each stock.

* Experiment with new weights to find a portfolio balance that outperforms the equally weighted portfolio.

**Note:** The weights should all sum to 1, so for 5 stocks, the initial numpy array should be:
```python
array([0.2, 0.2, 0.2, 0.2, 0.2])
```

- - -

### Resources

* [Return on Investment](https://www.investopedia.com/terms/r/returnoninvestment.asp)

* [Sharpe Ratio Definition](https://www.investopedia.com/terms/s/sharperatio.asp)

* [Portfolio Return](https://www.investopedia.com/terms/p/portfolio-return.asp)

- - -

### Hints and Considerations

Follow the comments in the starter workbook to complete each section. Refer to the ROI cheatsheet to find calculations for each step.

With this homework, you will be analyzing and comparing multiple stocks simultaneously. Try and take advantage of Pandas and Numpy to vectorize the calculations, but you can also loop through each stock. Checkout [this article](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6) on the different techniques!

- - -

### Submission

* Create a Jupyter Notebook and host the notebook on Github

* Include a README.md file that summarizes your assumptions and findings

* Submit the link to your Github project to Bootcampspot
