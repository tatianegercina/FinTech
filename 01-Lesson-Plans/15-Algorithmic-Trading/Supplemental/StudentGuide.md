# Unit 15: Algorithmic Trading

### Helpful Links

* For a recorded demo of a trading signal activity from class, click [here.](Activities_walkthrough.md)


---

### Additional Course Resources

* [Asyncio Streamz Installation Guide](Asyncio_Streamz_Install_Guide.md)

* [CCXT Installation Guide](CCXT_Install_Guide.md)

* [Evaluation Metrics Calculations Cheat Sheet](EvaluationsCalculationGuide.md)


---

### FAQs

<details>
<summary>What is Algorithmic Trading and why do I need to understand it?</summary><br>

Algorithmic trading is the trading of stocks using automated computer generated buy/sell decisions.  This type of trading is becoming more and more popular in the FinTech world largely because it can be backtested with historical and current data to prove profitability and for its ability to mitigate profit loss due to human error.  Some algorithmic trading strategies use the technology to inform their end decisions, while others run on auto-pilot - predicting and executing trades autonomously.

Algorithmic trading bots consist of three components:
- Signals:  Information that is useful for predicting the asset movement (such as performance and evaluation metrics, public sentiment).
- Entry Rules:  A decision rule telling you when to buy an asset (such as when a signal reaches a pre-specified, high enough level).
- Exit Rules:  A decision rule telling you when to sell or dispose of an asset (such as when a signal reaches a pre-specified, low enough level).
</details>
<details>
<summary>What is the difference between technical analysis and fundamental analysis?</summary><br>

The two major schools of thought in trading analysis are technical and fundamental analysis.  They are both are beneficial techniques used to develop trading strategies, however the methods of each are quite different.
<blockquote>

<details>
<summary>Technical Analysis</summary><br>

Technical analysis is used to determine the value of a stock based only on the patterns and trends in its price movements and volume.  Examples of technical analysis methods are Moving Averages and Bollinger Bands.  Technical analysts look for known patterns in the trend lines these methods produce, such as pennants, flags and wedges.  Using these patterns, they attempt to predict the stock's future movements.  For an overview list of technical indicator patterns, check out [this](https://www.investopedia.com/articles/technical/112601.asp) Investopedia article.

<br>
</details>
<details>
<summary>Fundamental Analysis</summary><br>

Fundamental analysis attempts to determine the value of a stock based on qualitative factors like management style and business model, quantitative factors such as balance sheet numbers, and even emotional and subjective factors like public sentiment.  Fundamental analysts create complicated mathmatical forecasting models based on these factors, making many assumptions and applying different weights to various factors.

<br>
</details>

</blockquote>
</details>


</details>
<details>
<summary>What is the difference between trading signals and technical indicators?</summary><br>

Technical indicators are metrics used to evaluate stock price movements, while trading signals are the point which those indicators suggest a time to buy or sell.  A good trading strategy will utlize both as one plays off the other.

<blockquote>
<details>
<summary>Technical Indicators</summary><br>

Falling under the umbrella of technical analysis, a technical indicator is a data-driven metric that uses trading data such as closing price and volume to analyze the short or long-term price movements occurring over a specified period. For example, a 20-day simple moving average is a technical indicator representing a rolling 20-day mean of a stock's closing prices.

<br>
</details>
<details>
<summary>Trading Signals</summary><br>

A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security (such as a stock) at that point in time.

<br>
</details>

</blockquote>
</details>

</details>
<details>
<summary>How do I use a Dual Moving Average Crossover?</summary><br>


<blockquote>
<details>
<summary>What it is:</summary><br>
The dual moving average crossover utilizes short and long term simple moving averages.  When these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other.  The value at the time of the crossover is considered the crossover point - a type of technical indicator.

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!
<br>

<br>
</details>
<details>
<summary>How to use it:</summary><br>

If the short-term moving average line goes above the long-term moving average line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the short-term moving average line dips below the long-term moving average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the dual moving average lines and the crossover points, indicating entry (buy signal) and exit (sell signal) points:

<img src=Images/dual_ma_cross.png width=700><br>
</details>
<details>
<summary>How to create it:</summary><br>

The dual moving average crossover can be created by using Pandas functionality.  In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.

<img src=Images/signals_df.PNG width=150>
<blockquote>
<details>
<summary>Step One: Signal, STMA, and LTMA Columns</summary><br>

First we initialize a `Signals` column, then create our short and long term moving average columns using the `.rolling()` and `.mean()` methods:

```python
# Set the short window and long windows
short_window = 50
long_window = 100

# Generate the short and long moving averages (50 and 100 days, respectively)
signals_df['Signal'] = 0.0
signals_df['SMA50'] = signals_df['Close'].rolling(window=short_window).mean()
signals_df['SMA100'] = signals_df['Close'].rolling(window=long_window).mean()

signals_df.tail()
```
<img src=Images/signals_df_sma.PNG width=250>
<br>


</details><br>
<details>
<summary>Step Two: Creating the Signal Values</summary><br>


Next we create the signals themselves using `np.where()`.  The code begins at the start of the short rolling window because the values prior to that are null.  We accomplish this by slicing the column with a colon after the short_window variable: `signals_df[short_window:]`.  The complete code loos like this:
```python
# Generate the trading signal (1 or 0) to when the short window is less than the long
# Note: Use 1 when the SMA50 is less than SMA100 and 0 for when it is not.
signals_df["Signal"][short_window:] = np.where(
    signals_df["SMA50"][short_window:] < signals_df["SMA100"][short_window:], 1.0, 0.0
)
```
Don't let the above code confuse you!  It is simply checking if the STMA is smaller than the LTMA and inserted a 1 if it is.  A small snippet of the values generated can be seen below:

<img src=Images/signals_df_values.PNG width=350>
</details><br>
<details>
<summary>Step Three: Creating the Entry/Exit Points</summary><br>

The next step is to take the `.diff()` of the `Signals` column and add it to the DataFrame.  Remember, `.diff` just subtracts one cell from the previous and provides the difference:

<img src=Images/signals_df_diff.PNG width=350>
</details><br>
<details>
<summary>Step Four: Visualizing the Indicators</summary><br>

Finally, the entry/exit points can be visualized using the following code:
```python
# Visualize exit position relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
    color='red',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize entry position relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
    color='green',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize close price for the investment
security_close = signals_df[['Close']].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize moving averages
moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(xaxis=None)
```
<img src=Images/signals_df_plot.PNG width=800>

</details><br>
</blockquote>
</details>
</details>
</blockquote>
</details>

<details>
<summary>How do I create and use Exponential Weighted Moving Average (EWMA) Crossovers?</summary><br>

<blockquote>
<details>
<summary>What it is:</summary><br>

The EWMA crossover utilizes short and long term exponentially weighted moving averages.  Because the most recent prices are more heavily weighted and because the smaller window has less time included, the short term EWMA is considered a fast moving trend line with more momentum than its long term EWMA counterpart.

These two variables are subsequently referred to as a *fast close* for short term EWMA and a *slow close* for long term EWMA.

Much like the dual simple moving average crossover, when these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other.  The value at the time of the crossover is considered the crossover point - a type of technical indicator.<br>

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!

<br>
</details>
<details>
<summary>How to use it:</summary><br>

If the short-term moving average line goes above the long-term moving average line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the short-term moving average line dips below the long-term moving average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the dual moving average lines and the crossover points, indicating entry (buy signal) and exit (sell signal) points:

<img src=Images/dual_ma_cross.png width=700><br>
</details>
<details>
<summary>How to create it:</summary><br>

The dual moving average crossover can be created by using Pandas functionality.  In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.

<img src=Images/signals_df.PNG width=150>
<blockquote>
<details>
<summary>Step One: Signal, STMA, and LTMA Columns</summary><br>

</details>
</blockquote>
</details>
</details>
<details>
<summary>How do I create and use Bollinger Bands?</summary><br>

<blockquote>
<details>
<summary>What it is:</summary><br>

The dual moving average crossover utilizes short and long term moving averages.  When these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other.  The value at the time of the crossover is considered the crossover point - a type of technical indicator.<br>

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!

<br>
</details>
<details>
<summary>How to use it:</summary><br>

If the short-term moving average line goes above the long-term moving average line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the short-term moving average line dips below the long-term moving average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the dual moving average lines and the crossover points, indicating entry (buy signal) and exit (sell signal) points:

<img src=Images/dual_ma_cross.png width=700><br>
</details>
<details>
<summary>How to create it:</summary><br>

The dual moving average crossover can be created by using Pandas functionality.  In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.

<img src=Images/signals_df.PNG width=150>
<blockquote>
<details>
<summary>Step One: Signal, STMA, and LTMA Columns</summary><br>

</details>
</blockquote>
</details>
</details>
<details>
<summary>What is backtesting and how do I use it?</summary><br>
</details>

<details>
<summary>What are evaluation metrics used for?</summary><br>

Evaluation metrics are calculations used to assess the value of trades.  Used in conjunction with your trading algorithms, they can be used to analyze it's performance and plan for needed adjustments.  In class we cover the following evluation metrics:

- **Cumulative Return:** the total/aggregated amount of gains and losses for an investment. Cumulative return is measured across time and not for a given time period.

- **Annual Return:** a time-weighted annual percentage representing the return on an investment over a period of time.

- **Annual Volatility:** the annualized degree of variation in trading prices over time.

- **Sharpe Ratio:** The return of investment compared to its risk, measured by the difference between the return on investment and the risk-free return.

- **Downside Deviation/Return:** The measure of risk for returns that are below the minimum acceptable return.

- **Sortino Ratio:** The quotient of harmful volatility and overall volatility. The Sortino ratio focuses on downside deviation rather than the standard deviation.

A cheat sheet to these calculations can be seen [here.](EvaluationsCalculationGuide.md)

</details>

<details>
<summary>What is a trading framework?</summary><br>
</details>

<details>
<summary>How do you design an end-to-end workflow for a trading framework?</summary><br>
</details>

<details>
<summary>What is a trading dashboard?</summary><br>
</details>

<details>
<summary>Why should I persist my data?</summary><br>
</details>

<details>
<summary>Why do I need to use Asyncio?</summary><br>
</details>

<details>
<summary>Time Series Data Refresher?</summary><br>
</details>

<details>
<summary>What is a pre-trained model and how do I implement one?</summary><br>
</details>
