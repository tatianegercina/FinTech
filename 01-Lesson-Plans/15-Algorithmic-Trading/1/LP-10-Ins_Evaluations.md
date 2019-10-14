### 10. Instructor Do: Evaluations (10 min)

Students will receive a dry walk through of the various evaluation metrics that can be used to evaluate their trading algorithms. This will include revisiting metrics such as cumulative returns and sharpe ratios, as well as new metrics such as the Sortino ratio. The instructor will explain how the metrics are calculated and how they are used.

**Files:** [trading_algorithm_evaluation.ipynb](Activities/06-Ins_Evaluations/Solved/trading_algorithm_evaluation.ipynb)

Navigate to the **evaluation** slide of the Unit 15.1 slideshow. Communicate the following:

* Evaluating securities, trades, and portfolios is important regardless if it is a human or algorithm making the trade. The following metrics can be used to evaluate a securities/trades.

  * **Cumulative Return**- the total/aggregated amount of gains and losses for an investment. Cumulative return is measured across time and not for a given time period.

  * **Annual Return**- a time weighted annual percentage representing the return on an investment over a period of time.

  * **Annual Volatility**- the annualized degree of variation in trading prices over time.

  * **Sharpe Ratio**- The return of investment compared to its risk, measured by the difference between the return on investment and the risk-free return.

  * **Downside Deviation/Return**- The measure of risk for returns that are below hte minimal acceptable return.

  * **Sortino Ratio**-  The quotient of harmful volatility and overall volatility. The Sortino ratio focuses on downside deviation rather than standard deviation.

* These metrics can be calculated historically with backtesting, or they can be used to measure future trades and opportunities for portfolio growth.

Transition through a dry walk through of the code used to calculate each of these metrics. Open the solution, and highlight the following:

* One of the advantages of using an algorithm for trading is that evaluation metrics can be calculated using the algorithm as well. This allows for each metric to be calculated within seconds. Having an algorithm calculate the evaluation metrics diminishes chances of human error and improves the overall accuracy and time it takes to comprehensively evaluate a portfolio/security/trade.

* Point out to students the code to calculate cumulative returns.

    ```python
    cum_returns = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
    ```

* Show students the code to calculate annual returns. Highlight that when calculating annual returns, the average of daily return has to be calculated first, and then that value can be multiplied by the number of trading days within a year to derive an annualized value.

    ```python
    annual_returns = ((1 + signals_df['Portfolio Daily Returns'].mean())**252 - 1)
    ```

* Explain the code to calculate annual volatility. Emphasize that annual volatility involves calculating the standard deviation for each daily return. The standard deviation is then annualized by multiplying by the number of trading days in the year.

    ```python
    annual_volatility = ((1 + signals_df['Portfolio Daily Returns'].std())** 252 - 1)
    ```

* Ask students if anyone remembers how to calculate a sharpe ratio.

  **Answer** Calculate the annual average daily return and then divide that by the standard deviation of daily returns. The standard deviation of daily returns will need to be multiplied by the square root of the number of trading days.

    ```python
    sharpe_ratio = (signals_df['Portfolio Daily Returns'].mean() * 252) / (signals_df['Portfolio Daily Returns'].std() * np.sqrt(252))
    ```

* Indicate that the downside returns, or downside deviation, metric is calculated by squaring daily returns less than 0.

    ```python
    sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < target, 'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2
    ```

* Sortino ratios are calculated using the downside return. Sortino ratios are calculated by dividing the average daily return by the square root of the average downside return.

    ```python
    down_stdev = np.sqrt(sortino_ratio_df['Downside Returns'].mean())
    expected_return = sortino_ratio_df['Portfolio Daily Returns'].mean()

    sortino_ratio = expected_return/down_stdev
    portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio
    ```

    ![evluation_metrics.png](Images/evluation_metrics.png)
* Emphasize to students that they should dedicate time outside of class to conduct research on each individual metric to better understand how it can be applied to assess portfolio performance.

If time remains, finish the walk through by reminding students that even when trading with an algorithm, trades and portfolios need to be evaluated. Algorithms are not infallible. Touch upon the following:

* Algorithms have to be tweaked and fine tuned over time, especially as trading strategies evolve or are replaced. Because a machine will be handling the trading process, it is imperative that the algorithm has metrics to use that will help measure performance, detect and mitigate risk, and track trends in returns on the fly.

* Evaluation metrics are also important for traders to have available, even if a machine is doing all of the trading and calculations. By analyzing evaluation metrics, humans can spot nuances in the data that the algorithm might not have been programed/trained to detect. This could lead to new features for the algorithm, as well as increased investment opportunity for the trader.

Ask if there are any questions before moving forward.
