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

Algorithmic trading is the trading of stocks using automated computer generated buy/sell decisions. This type of trading is becoming more and more popular in the FinTech world largely because it can be backtested with historical and current data to prove profitability and for its ability to mitigate profit loss due to human error. Some algorithmic trading strategies use the technology to inform their end decisions, while others run on auto-pilot - predicting and executing trades autonomously.

Algorithmic trading bots consist of three components:
- Signals:  Information that is useful for predicting the asset movement (such as performance and evaluation metrics, public sentiment).
- Entry Rules:  A decision rule telling you when to buy an asset (such as when a signal reaches a pre-specified, high enough level).
- Exit Rules:  A decision rule telling you when to sell or dispose of an asset (such as when a signal reaches a pre-specified, low enough level).
</details>
<details>
<summary>What is the difference between technical analysis and fundamental analysis?</summary><br>

The two major schools of thought in trading analysis are technical and fundamental analysis. They are both beneficial techniques used to develop trading strategies, however the methods of each are quite different.
<blockquote>

<details>
<summary>Technical Analysis</summary><br>

Technical analysis is used to determine the value of a stock based only on the patterns and trends in its price movements and volume. Examples of technical analysis methods are Moving Averages and Bollinger Bands. Technical analysts look for known patterns in the trend lines these methods produce, such as pennants, flags and wedges. Using these patterns, they attempt to predict the stock's future movements. For an overview list of technical indicator patterns, check out [this](https://www.investopedia.com/articles/technical/112601.asp) Investopedia article.

<br>
</details>
<details>
<summary>Fundamental Analysis</summary><br>

Fundamental analysis attempts to determine the value of a stock based on qualitative factors like management style and business model, quantitative factors such as balance sheet numbers, and even emotional and subjective factors like public sentiment. Fundamental analysts create complicated mathmatical forecasting models based on these factors, making many assumptions and applying different weights to various factors.

<br>
</details>

</blockquote><br>
</details>

</details>
<details>
<summary>What is the difference between technical indicators and trading signals?</summary><br>

Technical indicators are metrics used to evaluate stock price movements, while trading signals are the point at which those indicators suggest a time to buy or sell. A good trading strategy will utlize both as one plays off the other.

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

</blockquote><br>
</details>

</details>
<details>
<summary>What is the difference between a long and short strategy?</summary><br>

Both long and short strategies are attempts at profitting off the buying and selling of financial assets, however the methods of profitting are quite different.

A long strategy is perhaps the most simple to understand and the most commonly used. Going long is the classic - *buy low and sell high* strategy most of us are accustomed to when we think of profitting on a sale. To use this strategy the asset is purchased at the lowest price and sold at the highest price, the profit is the difference.

A short strategy is much more difficult to conceptualize. To short a stock or financial asset, is to make a profit off the decline in value, which seems counterintuitive to many of us at first glance. To better understand, let's use an example scenario.
<blockquote><br>

Let's say that Bob owns 100 shares of *World's Best Co. Inc.* and they are each valued at $100, making their total value $10,000.

You've been researching the *World's Best Co. Inc.* and you've found some information that leads you to believe its not really the best after all, and that its stock is well over-valued at $100 per share. You think its overvalued enough that the price is going to tank. You ask to borrow Bob's shares, and he agrees, temporarily transferring ownership of the shares to you (kind of like renting a home is the temporary transfer of many ownership rights). Now that you own the shares, even though it's temporary, you can sell them!  You sell all 100 shares for $100 each for a $10,000 cash injection - Nice job!

Not long after you do this, the price per share does in fact tank - down to $25 per share. You can now buy another 100 shares of the stock yourself on the open market at a total price of $2,500 to replace the borrowed stock you sold. Just in time too, because you are scheduled to return Bob's 100 shares to him tomorrow per your contract agreement!  You transfer all 100 shares of stock back to Bob, while keeping the $7,500 profit you made on the sale!

You may wonder, what's in it for Bob?  Don't worry - Bob will you charge you interest and fees on the renting of his stock, after all, its a risk to him to rent it out in case you don't return it. But this is one of many reasons why shorting a stock can be both risky and profitable.<br>
<br>

</blockquote><br>
</details>
<details>
<summary>How do I use a Dual Moving Average Crossover?</summary>
<font size = "2">

_For ease of explanation, this example will use a **long strategy**. For a refresher on the difference between **long and short strategies**, see the above section on **_long/short strategy_** in this FAQ._</font>

<blockquote>
<details>
<summary>What it is:</summary><br>
The dual moving average crossover utilizes short and long term simple moving averages. When these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other. The value at the time of the crossover is considered the crossover point - a type of technical indicator.
<br>
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

The dual moving average crossover can be created by using Pandas functionality. In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.

<img src=Images/signals_df.PNG width=150>
<blockquote><br>
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

Next we create the signals themselves using `np.where()`. The code begins at the start of the short rolling window because the values prior to that are null. We accomplish this by slicing the column with a colon after the short_window variable: `signals_df[short_window:]`. The complete code loos like this:
```python
# Generate the trading signal (1 or 0) to when the short window is less than the long
# Note: Use 1 when the SMA50 is less than SMA100 and 0 for when it is not.
signals_df["Signal"][short_window:] = np.where(
    signals_df["SMA50"][short_window:] < signals_df["SMA100"][short_window:], 1.0, 0.0
)
```
Don't let the above code confuse you!  It is simply checking if the STMA is smaller than the LTMA and inserted a 1 if it is. A small snippet of the values generated can be seen below:

<img src=Images/signals_df_values.PNG width=350>
</details><br>
<details>
<summary>Step Three: Creating the Entry/Exit Points</summary><br>

The next step is to take the `.diff()` of the `Signals` column and add it to the DataFrame. Remember, `.diff` just subtracts one cell from the previous and provides the difference:

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

</details>
</blockquote><br>
</details>

</blockquote><br>
</details>
</details>
<details>
<summary>How do I create and use Exponential Weighted Moving Average (EWMA) Crossovers?</summary>
<font size = "2">

_For ease of explanation, this example will use a **long strategy**. For a refresher on the difference between **long and short strategies**, see the above section on **_long/short strategy_** in this FAQ._</font>
<blockquote>
<details>
<summary>What it is:</summary><br>

The EWMA crossover works in much the same way as the dual moving average crossover, except instead of a simple moving average, it utilizes short and long term exponentially weighted moving averages. Because the most recent prices are more heavily weighted and because the smaller window has less time included, the short term EWMA is considered a fast moving trend line with more momentum than its long term EWMA counterpart.

These two variables are subsequently referred to as a *fast close* for short term EWMA and a *slow close* for long term EWMA. Much like the dual moving average crossover, when these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other. The value at the time of the crossover is considered the crossover point - a type of technical indicator.<br>

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!

<br>
</details>
<details>
<summary>How to use it:</summary><br>

If the fast close trend line goes above the slow close trend line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the fast close trend line dips below the slow close trend average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the exponentially weighted moving average lines and the crossover points, indicating entry (buy signal) and exit (sell signal) points:

<img src=Images/dual_ewma_cross.png width=700><br>
</details>
<details>
<summary>How to create it:</summary><br>

The exponentially weighted moving average crossover can be created by using Pandas functionality. In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.
```python
import numpy as np
import Pandas as pd
import hvplot.Pandas
from pathlib import Path
```
<img src=Images/signals_ewm_df.PNG width=150>
<blockquote><br>
<details>
<summary>Step One: Signal, Fast_Close, and Slow_Close Columns</summary><br>

First we initialize a `Signal` column, then create our short and long term moving average columns using the `.ewm()` and `.mean()` methods:

```python
# Set the short window and long windows
fast_close = 1
slow_close = 10

# Generate the fast and slow close exponentially weighted moving averages (1 and 10 days, respectively)
signals_df['Fast_Close'] = signals_df['Close'].ewm(halflife=short_window).mean()
signals_df['Slow_Close'] = signals_df['Close'].ewm(halflife=long_window).mean()
signals_df['Signal'] = 0.0

signals_df.tail()
```
<img src=Images/signals_df_ema.PNG width=250>
<br>

</details><br>
<details>
<summary>Step Two: Creating the Signal Values</summary><br>

Next we create the signals themselves using `np.where()`. The code begins at the start of the fast_close window because the values prior to that are null. We accomplish this by slicing the column with a colon after the short_window variable: `signals_df[short_window:]`. The complete code looks like this:
```python
# Generate the trading signal (1 or 0) to when the fast_close is less than the slow_close
# Note: Use 1 when the fast_close is less than the slow_close and 0 for when it is not.
signals_df["Signal"][short_window:] = np.where(
    signals_df["fast_close"][short_window:] < signals_df["slow_close"][short_window:], 1.0, 0.0
)
```
Don't let the above code confuse you!  It is simply checking if the fast close price is smaller than the slow close price and inserting a 1 if it is.

</details><br>
<details>
<summary>Step Three: Creating the Entry/Exit Points</summary><br>

The next step is to take the `.diff()` of the `Signals` column and add it to the DataFrame. Remember, `.diff` just subtracts one cell from the previous and provides the difference:

<img src=Images/signals_df_ewm_diff.PNG width=350>
</details><br>
<details>
<summary>Step Four: Visualizing the Indicators</summary><br>

Finally, the entry/exit points can be visualized using the code below. You'll notice there are many more entry/exit points than with the DMAC. This is because (in this case) the exponentially weighted moving averages uses shorter windows (1 and 10 days, versus 50 and 100), which causes the signals to respond to recent price action faster:
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

# Visualize exponentially weighted moving averages
moving_avgs = signals_df[['Fast_Close', 'Slow_Close']].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(xaxis=None)
```
<img src=Images/signals_df_ewm_plot.PNG width=800>

</details>
</blockquote><br>
</details>
</blockquote><br>

</details>
<details>
<summary>How do I create and use Bollinger Bands?</summary>
<font size = "2">

_For ease of explanation, this example will use a **long strategy**. For a refresher on the difference between **long and short strategies**, see the above section on **_long/short strategy_** in this FAQ._</font>

<blockquote>
<details>
<summary>What it is:</summary><br>

Bollinger Bands are a set of lines representing a positive and negative standard deviation away from the simple moving average (SMA) of the asset's closing price.<br>

These lines create _bands_ that move across the plot, creating an area of empty space. The area within this space represents where the closing price _should_ tend to be. The entry/exit signals are generated when the closing price trend line moves out of that area and dips either below or above the bottom and top barriers of the bands.

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!

<br>
</details>
<details>
<summary>How to use it:</summary><br>

When the closing price trend line moves below the lower band, a long (buy) opportunity exists as the signal suggests that the price action will tend to move upwards and more in line with where the price _should be_ (within the standard deviation area of the bands).

When the closing price trend line moves above the upper band, a short (sell) opportunity exists as the signal suggests that the price action will tend to move lower and more in line with where the price _should be_ (within the standard deviation area of the bands).

<img src=Images/Boll-Bands.PNG width=700><br>

</details>
<details>
<summary>How to create it:</summary><br>

The dual moving average crossover can be created by using Pandas functionality. In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices. We will also need to import the following dependences:
```python
import numpy as np
import Pandas as pd
import hvplot.Pandas
from pathlib import Path
```

<img src=Images/signals_bb_df.PNG width=150>
<blockquote>
<details>
<summary>Step One: Generate the daily return column:</summary><br>

We begin by adding a column to hold our daily return values:

```python
# Drop NAs and calculate daily percent return
btc_df['daily_return'] = btc_df['Close'].dropna().pct_change()
btc_df
```
<img src=Images/bb_df.PNG width=500>

</details>

<details>
<summary>Step Two: Generate the values used to create bands:</summary><br>

Next, we generate the values that are subsequently used to create the bands themselves. We use a rolling standard deviation to do this, after which the upper and lower bounds of the bands are creating by adding or substracting the mid_band from the standard deviation respectively:

```python
# Drop NAs and calculate daily percent return
btc_df['daily_return'] = btc_df['Close'].dropna().pct_change()
btc_df# Set Bollinger band window
bollinger_window = 20

# Calculate rolling mean and standard deviation
btc_df['bollinger_mid_band'] = btc_df['Close'].rolling(window=bollinger_window).mean()
btc_df['bollinger_std'] = btc_df['Close'].rolling(window=20).std()

# Calculate upper and lowers bands of Bollinger band
btc_df['bollinger_upper_band']  = btc_df['bollinger_mid_band'] + (btc_df['bollinger_std'] * 1)
btc_df['bollinger_lower_band']  = btc_df['bollinger_mid_band'] - (btc_df['bollinger_std'] * 1)
```

<img src=Images/bb_bands_df.PNG width=500>

</details>
<details>
<summary>Step Three: Plot the bands!</summary><br>

We can finally plot our Bollinger bands as follows:

```python
btc_df[['Close','bollinger_mid_band','bollinger_upper_band','bollinger_lower_band']].plot(figsize=(20,10))
```
<img src=Images/bb_df_plot.PNG width=800>

</details>
</details>
</blockquote><br>

</details>
<details>
<summary>What is back testing and how do I use it?</summary><br>

The term sounds more complicated that it actually is - backtesting is simply the testing of your trading strategy using historical data in a simulated scenario. The results indicate how much the gains and losses **_would_** have been if the strategy had been implemented on a dummy portfolio of predetermined share size with a dummy capital amount of a predetermined size. There's no set rule for what share size or capital amount to backtest with, but in the example below, `500` is chosen for the portfolio size and `$100,000` is chosen for the available capital.

For an example of back test simulation check out the steps below:

<blockquote>
<details>
<summary>Step One: </summary><br>

To conduct the simulation in Jupyter, the portfolio size and capital amount are set in variables so they can be easily inserted to our code:
```python
# Set initial capital
initial_capital = float(100000)
# Set the share size
share_size = 500
```
The portfolio size, or *position*, is set in a column titled `Position` and is coded to equal `500` when the crossover signal is 1 by multipying our share size by the signal:
```python
# Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
signals_df['Position'] = share_size * signals_df['Signal']
```
This inserts a column as seen below:

<img src=Images/active-positions.png>
</details>
<details>
<summary>Step Two: </summary><br>

Next, a column is inserted indicating the share size purchase or sale, depending on the entry/exit points. If there is an entry point, the share size is  `500`. If there is an exit point, the share size is `-500`. This is creating by running `.diff()` on the `Position` column.

```python
# Find the points in time where a 500 share position is bought or sold
signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
```

This inserts a column as seen below:

<img src=Images/active-positions_diff.png>
</details>
<details>
<summary>Step Three: </summary><br>

Next, the column `Portfolio Holdings` is inserted to represent the cumulative investment in the chosen stock over time. These values are obtained by multiplying the closing prices of the stock by the cumulative sum for entry/exit positions of 500 shares - or in this case the `Entry/Exity Position` column:

```python
# Multiply share price by entry/exit positions and get the cumulatively sum
signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()
```
This inserts a column as seen below:

<img src=Images/active-positions_holdings.png>

</details>
<details>
<summary>Step Three: </summary><br>

We now add another new column to represent the remaining cash value of our capital as we make our psuedo investments. To calculate this value, we subtract the `initial_capital` from the product of the `close` prices and the cumulative sum of the `Entry/Exit Position`:

```python
# Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
```
This inserts a column as seen below:

<img src=Images/active-positions_cash.png>

</details>
<details>
<summary>Step Four: </summary><br>

Next, we add the values of the `Portfolio Cash` column to the values of the `Portfolio Holdings` column to create a new column of values - `Portfolio Total`. This column represents the total value of the portfolio over time.

```python

# Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
```
This inserts a column as seen below:

<img src=Images/active-positions_total.png>

</details>
<details>
<summary>Step Five: </summary><br>

The final step before plotting is to generate the daily and cumulative returns. The `Portfolio Daily Returns` column is populated by using `.pct_change()` on the `Portfolio Total` column. This converts the daily portfolio value to daily portfolio returns. The `Portfolio Cumulative Returns` column is populated using `cumprod()` on the newly generated `Portfolio Daily Returns` column. This means that we convert those daily portfolio returns to a cumulative performance index, which makes it easy to see total performance over time and total dollars made. 
```python
# Calculate the portfolio daily returns
signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

# Calculate the cumulative returns
signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
```
This inserts columns as seen below:

<img src=Images/active-positions_returns.png>

</details>
<details>
<summary>Step Six: </summary><br>

Finally, we can visualize the simulation and thus the overal success or failure of our strategy by plotting the values.

```python
# Visualize exit position relative to total portfolio value
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Portfolio Total'].hvplot.scatter(
    color='red',
    legend=False,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize entry position relative to total portfolio value
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Portfolio Total'].hvplot.scatter(
    color='green',
    legend=False,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize total portfolio value for the investment
total_portfolio_value = signals_df[['Portfolio Total']].hvplot(
    line_color='lightgray',
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Overlay plots
portfolio_entry_exit_plot = total_portfolio_value * entry * exit
portfolio_entry_exit_plot.opts(xaxis=None)
```
The above code generates a chart like the one below. This allows us to visualize our simulation. We can see our entry/exit points in red/green respectively, and we can see the trend line of the value of the portfolio rise over time. This particular simulation increased the initial capital from $100,000 to a total portfolio value of $132,975:

<img src=Images/sim_visualization.PNG>

</details>

</blockquote><br>
</details>
</details>
<details>
<summary>What are evaluation metrics used for?</summary><br>

Evaluation metrics are calculations used to assess the value of trades. Used in conjunction with your trading algorithms, they can be used to analyze it's performance and plan for needed adjustments. In class we cover the following evaluation metrics:

- **Cumulative Return:** the total/aggregated amount of gains and losses for an investment. Cumulative return is typically measured over an extended time period.

- **Annual Return:** a time-weighted annual percentage representing the return on an investment over a year.

- **Annual Volatility:** the annualized degree of variation in trading prices over time. Volatility is measured by standard deviation.

- **Sharpe Ratio:** The return on an investment compared to its risk. Measured by the difference between the return on investment and the risk-free return, all divided by standard deviation. Is often used as an annual performance measure, but can be measured over any period of time.

- **Downside Deviation/Return:** The measure of risk for returns that are below the minimum acceptable return (usually below zero, or negative).

- **Sortino Ratio:** The ratio of investment return to harmful volatility. Similar to Sharpe Ratio, but instead focuses on downside deviation rather than the standard deviation.

A cheat sheet to these calculations can be seen [here.](EvaluationsCalculationGuide.md)

</details>

<details>
<summary>Why do I need a framework?</summary><br>

A framework is much like a template for your code. It's a programming technique that organizes code into a workflow that can easily be reused and applied to different scenarios. Just as a library like Pandas can provide prebuilt code to be easily inserted into your program, the framework provides prebuilt structure and organization into which that code can be inserted. The code inside the framework can be easily changed to fit new data, but the flow of the code remains the same.

The trading framework we build in class provides a work flow for building an entire dashboard to visualize a trading strategy. The code inside the framework can be swapped out to accompodate new data, but the work flow remains the same so that when the dashboard is generated all of its components created and can be populated.

</details>

<details>
<summary>What does it mean to persist data and why is it important?</summary><br>

Data persistence is the concept of saving data to a database to have a reliable copy of data that is persisted rather than transiently stored as in-memory data structures.

Persisting data is generally a best practice as it provides a method for data recovery should an application ever fail; data stored in transient in-memory data structures will be lost forever if the application itself terminates. Also, persisting data to a database allows for separate data analysis to be done at a later time, if desired.

</details>

<details>
<summary>What is a pre-trained model and how do I implement one?</summary><br>

Just as we can persist data using a database for longetivity and reuse, we can persist models for the same reasons. When a model is persisted, it is referred to as pre-trained. Pre-trained models have been created, configured, and fitted to data then saved for later use. The models can be loaded as any file can be loaded, using the right modules of course.

This saves us the time consuming process of splitting our data for training and testing, then fitting the model. If it has been done once, and a successful combination has been found, the model can be saved and reused later.

There are many ways to persist your model, however in class we use a library called `joblib`. To save the model we utilize the following code:

```python
from joblib import dump
dump(model, 'your_model.joblib')
```

Once the model is saved, we can load it whenever we need to use it. We load the model as follows:

```python
from joblib import load
model = load('your_model.joblib')
```

Once the model is loaded, predictions can be made as normal:

```python
predictions = model.predict(X_test)
```
</details>


<details>
<summary>Help, I need a time series refresher!</summary><br>

It's important to convert dates into time series when working with python and Pandas. For a quick refresher on reading time series data into a Pandas DataFrame, see below. for a full refresher, head back to the [Unit 10 - Time Series FAQ.](../../10-Time-Series/Supplemental/StudentGuide.md)

<blockquote>
<details><summary>How do you convert objects to `datetime`?</summary>

Converting objects to `datetime` can be tricky. Using Pandas, the conversion can be handled upon reading in of data. The syntax to handle the conversion from `read_csv()` is:

```python
df = pd.read_csv('your_data.csv', parse_dates=True)
```
This converts each object to a `datetime` object. Alternatively, you can also set the index as the date column for ease of plotting:
```python
df = pd.read_csv('your_data.csv', infer_datetime_format=True, parse_dates=True, index_col='Date')
```

</details>
</blockquote>
<br>
</details>
<br>


© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
