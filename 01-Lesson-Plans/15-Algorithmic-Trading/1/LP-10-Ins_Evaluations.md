### 10. Instructor Do: Evaluations (10 min)

Students will receive a dry walk through of the various evaluation metrics that can be used to evaluate their trading algorithms. This will include revisiting metrics such as cumulative returns and sharpe ratios, as well as new metrics such as the sortino ratio. The instructor will explain how the metrics are calculated and how they are used.

**Files:** [trading_algorithm_evaluation.ipynb](Activities/06-Ins_Evaluations/Solved/trading_algorithm_evaluation.ipynb)

Navigate to the **evaluation** slide of the Unit 15.1 slideshow. Communicate the following:

* Evaluating securities, trades, and portfolios is important regardless if it is a human or algorithm making the trade. The following metrics can be used to evaluate a securities/trades.

  * Cumulative Return

  * Annual Return

  * Annual Volatility

  * Sharpe Ratio

  * Portfolio Daily Return

  * Downside Return

  * Sortino Ratio

* These metrics can be calculated historically with backtesting, or they can be used to measure trades as they are made.

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
