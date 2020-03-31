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
<summary>How do I create and use a Dual Moving Average Crossover?</summary><br>

The dual moving average crossover utilizes short and long term moving averages.  When these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other.  The value at the time of the crossover is considered the crossover point - a type of technical indicator.

If the short-term moving average line goes above the long-term moving average line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the short-term moving average line dips below the long-term moving average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the dual moving average lines and the crossover points:

<img src=Images/dual_ma_cross.png width=700>

</details>
<details>
<summary>How do I create and use Bollinger Bands?</summary><br>
</details>
<details>
<summary>What is backtesting and how do I use it?</summary><br>
</details>

<details>
<summary>What are evaluation metrics and how do I use them?</summary><br>
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
