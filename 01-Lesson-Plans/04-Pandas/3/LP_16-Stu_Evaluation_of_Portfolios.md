### 17. Students Do: Portfolio Planner Part II (20 mins)

In this activity, students will work in pairs to continue where they left off in part I of evaluating portfolios. Students will now evaluate correlations and sharpe ratios of the 10 stocks, filter by only non-correlated and positive sharpe ratio stocks, set equal-weighted portfolio allocations to the remaining stocks, and perform an analysis of a `$10,000` investment in the portfolio over time. Then compare the `$10,000` investment in the portfolio to other `$10,000` investments in lesser optimized portfolios.

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

* Unliked volatility which measures risk, sharpe ratios describe the riskiness of stocks relative to their returns. Therefore, sharpe ratios measure risk-to-reward and indicate *value-driven* investments. The `mean` and `std` functions can be used to calculate the sharpe ratios of stocks.

  ![challenge-sharpe-ratios](Images/challenge-sharpe-ratios.png)

* An equal-weighted portfolio consists of the same weight for every stock in the portfolio (totaling `1`). For example, an equal-weighted stock portfolio of `5` stocks would have weights of `0.2`, `0.2`, `0.2`, `0.2`, and `0.2` to each stock.

  ![challenge-evaluate](Images/challenge-evaluate.png)

* The overlay chart of corresponding `$10,000` investments in each respective portfolio over time describes the following:

  * The non-correlated and sharpe-ratio optimized portfolio performs the best of the four portfolios and consistently acheives higher returns with minimized volatility.

  * The non-correlated (diversifed) portfolio performs the second worst of the four portfolios and manages to minimize volatility but at the expense of higher returns.

  * The original/unoptimized portfolio performs the second best of the four portfolios and acheives higher returns that but at the expense of more volatility. For example, returns rose quicker but fell faster as well (notice the dip in early 2019).

  * The risk-optimized portfolio performs the worst of the four portfolios and acheives minimal volatility but at the expense of returns.

  ![challenge-overlay](Images/challenge-overlay.png)