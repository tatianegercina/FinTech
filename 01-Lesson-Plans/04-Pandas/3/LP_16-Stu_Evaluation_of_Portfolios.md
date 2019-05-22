### 17. Students Do: Constructing Optimized Portfolios (20 mins)

**Instructions:**

* [README.md](Activities/16-Stu_Evaluation_of_Portfolios/README.md)

**Files:**

* [portfolio_evaluation.ipynb](Activities/16-Stu_Evaluation_of_Portfolios/Unsolved/portfolio_evaluation.ipynb)

### 18. Instructor Do: Review Constructing Optimized Portfolios (5 mins)

**Files:**

* [portfolio_evaluation.ipynb](Activities/16-Stu_Evaluation_of_Portfolios/Solved/portfolio_evaluation.ipynb)

Open the solution and explain the following:

* The 10 stocks will need to be filtered down by keeping only non-correlated stocks and stocks with positive sharpe ratios. This is to maximize diversification of the portfolio (and therefore minimize volatility) and maximize the returns-to-risk of the optimized portfolio, respectively.

* Stock correlation describes the linear relationship between the returns of two stocks and indicates whether returns of both stocks tend to move in tandem, inversely, or random (no correlation). The `corr` function used in conjunction with the `heatmap` function from the `seaborn` library makes it easy to spot the highly correlated stocks. In this case, the daily returns of `BK`, `FANG`, `JNJ`, `LUV`, and `MU` appear to be highly correlated and can be dropped from the DataFrame.

* Stock volatility describes the riskiness of stocks and indicates the range of variability or dispersion returns will be from the average expected return. The `std` function can be used to calculate the volatility of stocks.

* Sharpe ratios describe the riskiness of stocks relative to their returns. Therefore, sharpe ratios measure risk-to-reward and indicate *value-driven* investments. The `mean` and `std` functions can be used to calculate the sharpe ratios of stocks.

* The sum of weights to a portfolio must equal `1`. Therefore, for example, a stock portfolio of `2` stocks would allocated `0.5` and `0.5` to each stock.

* The `dot` function multiples each weight by the daily returns of each stock to calculate the portfolio's daily returns.

* The `cumprod` function calculates the cumulative returns of a portfolio's daily returns over time. Multiplying an initial investment of `$10,000` by the series of cumulative returns for a portfolio expresses returns in terms of money.

* The overlay chart of corresponding `$10,000` investments in each respective portfolio over time describes the following:

  * The optimized portfolio (non-correlated and positive sharpe ratio stocks) performs the best over time and appears fairly consistent over time.

  * The non-correlated portfolio (non-correlated and positive/negative sharpe ratio stocks) performs the worst of the three portfolios, but maintains low volatility.

  * The unoptimized portfolio (correlated/non-correlated and positive/negative sharpe ratio stocks) performs better than the non-correlated portfolio; however, is more volatile. Returns rose quicker but fell faster as well (notice the dip in early 2019).