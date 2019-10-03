# Unit 10—A Yen for the Future

![Yen Photo](Images/unit-10-readme-photo.png)

## Background

The financial departments of large companies often deal with foreign currency transactions while doing international business. As a result, they're always looking for anything that can help them better understand the future direction and risk of various currencies. Hedge funds, too, are keenly interested in anything that will give them a consistent edge in predicting  currency movements. 

In this assignment, you will test the many time-series tools that you've learned in order to predict future movements in the value of the Japanese yen versus the U.S. dollar. 

You will gain proficiency in the following tasks:

1. [Time-Series Return Forecasting](#Return-Forecasts)
2. [Volatility Forecasting](#Volatility-Forecasts)
3. [Out-of-Sample Predictions](#OOS-Predictions)

- - -

### Files

[Time-Series Starter Notebook](Starter_Code/time_series_analysis.ipynb)

- - -

### Instructions

#### Time-Series Return Forecasting

In this section, you will use the Quandl API to obtain daily **futures** data (a type of financial contract) on the Japanese yen per U.S. dollar exchange rate and use the data to build various time-series models that predict near-term yen returns. 

Follow the steps outlined in the time-series starter notebook to complete the following:

1. Generate a Quandl API key [(free)](https://www.quandl.com/).

     1. Use your API key to read historical daily yen futures data into a Pandas DataFrame. 

     (*Futures contracts are contractual bets made today about what the future value of something will be. They are used a lot for hedging and for speculative trading. For more information on futures contracts, see a few of the links in the [Resources](#Resources) section.*) 

3. Perform a time-series decomposition, using Hodrick-Prescott filter and various moving average (MA) and exponentially weighted moving average (EWMA) smoothers.

4. Estimate a Scikit-Learn time-series regression to identify seasonal effects in the yen.

5. Identify autocorrelation and use that to guide selection for the best fitting autoregressive moving average (ARMA) and autoregressive integrated moving average (ARIMA) models.


#### Volatility Forecasting

In this section, you will use the time-series GARCH (generalized autoregressive conditional heteroskedasticity) or EGARCH (exponential GARCH) models to forecast short-term volatility in the Japanese yen.
Follow the steps outlined in the time-series starter notebook to complete the following:

1. Estimate either a GARCH or EGARCH model using the arch python package.

2. Identify patterns of clustered and/or high yen volatility.

3. Forecast three-day volatility of the yen using a GARCH or EGARCH model.

#### Optional Challenge—Out-of-Sample Predictions

Last, apply your Scikit-Learn regression model under a testing approach commonly used by data scientists and quantitative traders when dealing specifically with time-series data.

1. Use Pandas datetime indexing to slice the dataset into a training and test set, and compare model performance (root mean square error or RMSE) between the two (a one-shot approach).

2. Create a rolling-out-of sample approach that updates to a new model each week using the most recent data and evaluates performance on data over the following week.


#### Optional Challenge—Futures Spread Prediction

Futures spreads, as opposed to futures contracts, often exhibit more seasonal patterns and are generally easier to predict. 

1. Navigating the Quandl website, pull futures data one-month and two-month continuous Japanese yen futures contracts.

2. Construct a futures spread, by taking [(2 month contract return) - (1 month contract return * -1)]. This is effectively a bet that the yen will be stronger two months from now than it will be a month from now (regardless of what it is today).  

3. Use an ARMA model and the out-of-sample approaches you've learned to see if you can build a model with a low RMSE. (Then save it! In a subsequent unit, you'll learn how to apply your best model to actual trading).

- - -

### Resources

[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

[A Traders Guide to Futures (Chicago Mercantile Exchange)](https://www.cmegroup.com/education/files/a-traders-guide-to-futures.pdf)

[Futures Spread Trading - For the Optional Challenge](https://www.investopedia.com/terms/f/futuresspread.asp)
- - -

### Hints and Considerations

[Quandl API Guide for Futures Data](https://blog.quandl.com/api-for-futures-data)

- - -

### Submission

* Create Jupyter Notebooks for the analysis and host the notebooks on GitHub.

* Include a Markdown that summarizes your models and findings and include this report in your GitHub repo.

* Submit the link to your GitHub project to Bootcampspot.
