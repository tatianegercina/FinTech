### 17. Students Do: Portfolio Planner Part II (20 mins)

In this activity, students will work in pairs to research a group of 10 stocks, evaluate correlations and sharpe ratios of stocks, filter by only non-correlated and positive sharpe ratio stocks, set equal-weighted portfolio allocations to the remaining stocks, and perform an analysis of a `$10,000` investment in the portfolio over time. Then compare the `$10,000` investment in the portfolio to other `$10,000` investments in lesser optimized portfolios.

**Instructions:**

* [README.md](Activities/16-Stu_Portfolio_Planner_Part_II/README.md)

**Files:**

* [portfolio_planner_part_2.ipynb](Activities/16-Stu_Portfolio_Planner_Part_II/Unsolved/portfolio_planner_part_2.ipynb)

### 18. Instructor Do: Review Portfolio Planner Part II (5 mins)

**Files:**

* [portfolio_planner_part_2.ipynb](Activities/16-Stu_Portfolio_Planner_Part_II/Solved/portfolio_planner_part_2.ipynb)

Open the solution and explain the following:

* The 10 stocks will need to be filtered down by keeping only non-correlated stocks and stocks with positive sharpe ratios. This is to maximize diversification of the portfolio (and therefore minimize volatility) and maximize the returns-to-risk of the optimized portfolio, respectively.

* Stock correlation describes the linear relationship between the returns of two stocks and indicates whether returns of both stocks tend to move in tandem, inversely, or random (no correlation). The `corr` function used in conjunction with the `heatmap` function from the `seaborn` library makes it easy to spot the highly correlated stocks. In this case, the daily returns of `BK`, `FANG`, `JNJ`, `LUV`, and `MU` appear to be highly correlated and can be dropped from the DataFrame.

  ![challenge-correlation](Images/challenge-correlation.png)

* Stock volatility describes the riskiness of stocks and indicates the range of variability or dispersion returns will be from the average expected return. The `std` function can be used to calculate the volatility of stocks.

  ![challenge-volatility](Images/challenge-volatility.png)

* Sharpe ratios describe the riskiness of stocks relative to their returns. Therefore, sharpe ratios measure risk-to-reward and indicate *value-driven* investments. The `mean` and `std` functions can be used to calculate the sharpe ratios of stocks.

  ![challenge-sharpe-ratios](Images/challenge-sharpe-ratios.png)

* The sum of weights to a portfolio must equal `1`. Therefore, for example, a stock portfolio of `2` stocks would allocate `0.5` and `0.5` to each stock.

* The `dot` function multiples each weight by the daily returns of each stock to calculate the portfolio's daily returns.

* The `cumprod` function calculates the cumulative returns of a portfolio's daily returns over time. Multiplying an initial investment of `$10,000` by the series of cumulative returns for a portfolio expresses returns in terms of money.

  ![challenge-evaluate](Images/challenge-evaluate.png)

* The overlay chart of corresponding `$10,000` investments in each respective portfolio over time describes the following:

  * The optimized portfolio (non-correlated and positive sharpe ratio stocks) performs the best over time and appears fairly consistent over time.

  * The non-correlated portfolio (non-correlated and positive/negative sharpe ratio stocks) performs the worst of the three portfolios, but maintains low volatility.

  * The unoptimized portfolio (correlated/non-correlated and positive/negative sharpe ratio stocks) performs better than the non-correlated portfolio; however, it is more volatile. Returns rose quicker but fell faster as well (notice the dip in early 2019).

  ![challenge-overlay](Images/challenge-overlay.png)