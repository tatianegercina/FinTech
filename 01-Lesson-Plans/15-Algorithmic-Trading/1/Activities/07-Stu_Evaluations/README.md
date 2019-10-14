## Evaluations

Evaluate the backtesting results by calculating the annual return, cumulative returns, annual volatility, Sharpe ratio, and Sortino ratio for your portfolio. These evaluation metrics will provide insight into how well the trading algorithm performed in terms of maximizing returns and minimizing risk and volatility.

### Instructions

1. Open the starter file, and begin by calculating cumulative returns using the `signals_df` DataFrame.

2. Calculate annualized returns. Remember to multiply by the number of trading days.

3. Measure annual volatility.

4. Calculate the Sharpe ratio.

5. Calculate the downside deviation/return.

6. Calculate the Sortino ratio by dividing the average downside deviation by the average daily return.

7. Wrap all of these calculations into a single function called `calculate_eval_metrics`. The function should accept the `signals_df` DataFrame as a parameter, and it should return the `portfolio_evaluation_df` DataFrame.

8. Call the `calculate_eval_metrics` function with `signals_df` as the argument

### Hint

Consult the [evaluations calculation guide](../../../Supplemental/EvaluationsCalculationGuide.md) for the above calculations/formulas.
