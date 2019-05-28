## 4.3 Lesson Plan - Investing Like the Pros

---

### Overview

Today's class will focus on the notion of analyzing the performance of not just a single stock, but groups of stocks together -- otherwise known as a portfolio of stocks. Stock portfolios are an important strategy in the realm of investing as total capital is proportioned among several stocks, thereby minimizing risk by preventing the "all eggs in one basket" dilemma.

However, in order to create an optimal portfolio that maximizes returns while minimizing risk, it's necessary to not only analyze the average return and risk of the portfolio overall, but also the correlation between stocks as well (how much one stock price changes with or against another). This lesson will teach students how to analyze the correlations of stocks against one another, calculate rolling statistics and volatility (beta) of stocks together, and optimize the composition of a portfolio and compare its performance against other portfolios.

### Class Objectives

By the end of class, students will be able to:

* Describe the benefits of investing in stock portfolios over a single stock.
* Explain what correlation is and how to calculate it in Pandas.
* Visualize trends through rolling statistics that minimize data noise.
* Compare the volatility of a portfolio against the overall market.
* Calculate expected returns of a portfolio utilizing custom weights
* Build and optimize a portfolio by factoring in risk, correlation, and returns
* Compare a portfolio's performance to other portfolios.

### Instructor Notes

* This lesson brings the heat on two fronts: math/statistics and financial domain knowledge. Not everyone will have extensive experience with either subject so be clear, visualize code/charts, and refer to the examples and notes if you need help!

* Showcase the benefits of rolling statistics by comparing the original data trend against the smoothed trend of the rolling statistic (mean or standard deviation).

* When dealing with portfolios and its characteristics - risk, return, correlation - try to speak in terms of money. If you started with $10,000, how would a poorly optimized portfolio compare with one that is not?

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 mins)

**Files:**

* [Slideshow](placeholder)

Welcome students to the third day of Pandas! Cover the following points:

* Today students will combine what they've learned so far on using Pandas to analyze individual stock returns and risk, and move onto the notion of grouping stocks together to achieve the best risk/reward ratio for their investments.  

* Mention to the class that today's focus is on using Pandas to make more informed (and better) investments! Students should feel invigorated as they are learning the techniques used by real financial analysts, quantitative traders, and portfolio managers.

* Since today's class focuses more on groups of stocks rather than an individual stock, students should be prepared to push their mindset from that of analyzing a single variable to analyzing an amalgamation of variables with relationships to one another.  

* Energize your students! Today is the day where students truly begin leveraging the power of Pandas to create truly insightful analyses that can benefit their skills in financial analysis/investing.

---

### 2. Instructor Do: Intro to Portfolios (5 mins)

Engage the class with the following discussion around portfolios:

* What is an investment portfolio?

  > An investment portfolio is the grouping of various financial assets such as equity, bonds, commodities, private investments, etc, or just that of a single financial asset such as equity.

* What is a stock portfolio?

  > A stock portfolio is an investment portfolio consisting of only equity. Therefore a stock portflio consists of multiple stocks ranging from the 11 sectors of the equity market: financials, utilities, consumer discretionary, consumer staples, energy, healthcare, industrials, technology, telecom, materials, and real estate.

* Why are stock portfolios better than single stock investments?

  > Single stock investments are risky in that they represent the "all eggs in one basket dilemma". If the performance of a single stock fails, then so does the entirety of one's investment (as it is only tied to that particular stock). However, by grouping multiple stocks together, the risk is minimized or spread throughout the portfolio as a single stock may fail but others may continue to succeed.

* What is a stock market index?

  > Similar to a stock portfolio, a stock market index is a collection of stocks used to gauge the performance of a particular area within the stock market. For example, a popular stock market index is the S&P 500, a collection of 500 large market cap U.S. stocks which serve as a general health indicator of the overall U.S. stock market.

* Why do stock market indexes matter?

  > Stock market indexes, like the S&P 500, serve as general health indicators for particular areas in the stock market; however, they also serve as benchmarks to compare performances of portfolios. For example, how does the performance of one's personal stock portfolio compare to that of the S&P 500 or general stock market?

---

### 2. Instructor Do: Correlation (5 mins)

This activity introduces the student to the concept of correlation, or the positive or negative relationship between two variables. Two datasets have been chosen to showcase the example of correlation: ice cream sales and drowning incidents.

**Files:**

* [correlation.ipynb](Activities/01-Ins_Correlation/Solved/correlation.ipynb)

Walk through the solution and highlight the following:

* What is correlation?

  > Correlation is the measure of either a positive, negative, or neutral (random) relationship between two variables. For example, there is often a positive correlation with height vs. weight (as you grow in height you tend to weigh more).

* When comparing the line trend of ice cream sales to drowning incidents, it is much harder to detect a relationship between the two. Therefore, use a scatterplot and set the `x` and `y` axis to the corresponding DataFrame columns. With a scatterplot, the relationship becomes much more apparent.

  ![line-chart](Images/line-chart.png)
  ![scatterplot](Images/scatterplot.png)

* Use the `corr` function to calculate and output a matrix of correlation values for each column-to-column pair of a DataFrame. Correlation values range from `-1` to `0` to `+1`, where `-1` indicates a negative relationship (variables move inversely to one another), `0` indicates a neutral relationship (variables have no relationship and move randomly), and `+1` indicates a positive relationship (variables move in tandem with one another). 

  ![correlation.png](Images/correlation.png)

* The `heatmap` function from the `seaborn` library color-codes the different variations in a correlation table. This is particularly useful when there are many variables in a correlation table.

  ![correlation_seaborn.png](Images/correlation-seaborn.png)

* Remember that correlation does not imply causation! Although `Ice Cream Sales` has a positive correlation of `0.819404` with `Drowning Incidents` it does not mean that buying more ice cream causes people to drown. It merely states that there is a positive relationship between the numbers. Chances are, there is another factor at play which makes these two variables so positively correlated. One guess could be as temperatures increase (summer months) people tend to eat more ice cream and go swimming. 

* In order to determine causation, regression analysis should be used where the premise is to find out how x predicts y.

* When applied to stock investments, investigating the correlations of returns among stocks in a portfolio can help analysts properly diversify their portfolios and mitigate risk/volatility. This is due to the fact that non-correlated stocks in a portfolio tend to cancel out large swings in volatility, as one stock may increase in price while another may decrease in price rather than all stocks increasing in price and all stocks decreasing in price.

---

### 4. Students Do: Diversification (15 mins)

**Instructions:**

* [README.md](Activities/02-Stu_Correlation/README.md)

**Files:**

* [market_analysis.ipynb](Activities/02-Stu_Correlation/Unsolved/diversification.ipynb)

### 5. Instructor Do: Diversification (5 mins)

**Files:**

* [diversification.ipynb](Activities/02-Stu_Correlation/Solved/diversification.ipynb)

Open the solution and explain the following:

* Remember that the `corr` function compares values from each column-to-column pair. Therefore, make sure that the DataFrame is properly formatted on a column-by-column basis for analysis.

  ![formatted-dataframe](Images/formatted-dataframe.png)

* When viewing a correlation table, it's difficult to distinguish lower values from higher values when there are many variables present. Therefore, using the `heatmap` function from the `seaborn` library makes it much easier to discern differences by using color gradients.

  ![correlation-table](Images/correlation-table.png)

  ![correlation-heatmap](Images/correlation-heatmap.png)

* Use the `vmin` and `vmax` parameters to the `heatmap` function to modify the scale of the heatmap. Correlation values range from `-1` to `0` to `+1` therefore the scale of the heatmap will need to reflect accordingly.

  ![correlation-heatmap-scaled](Images/correlation-heatmap-scaled.png)

* Looking at the heatmap and cross-referencing the correlation table, it would appear as though AMD stock appears to be the least correlated out of any of the other semiconductor stocks. Therefore, AMD stock would be the best semiconductor stock to add to the existing portfolio.

  ![correlation-heatmap-focus](Images/correlation-heatmap-focus.png)
  
  ![correlation-table-focus](Images/correlation-table-focus.png)

---

### 6. Instructor Do: Rolling Statistics (10 mins)

**Files:**

* [rolling_statistics.ipynb](Activities/03-Ins_Rolling_Statistics/Solved/rolling_statistics.ipynb)

Walk through the solution and explain the following:

* What is a rolling statistic?

  > A rolling statistic is a metric calculated over the range of a shifting (or rolling) window. For example, a 7-day rolling mean of 14 days worth of closing prices for a stock would calculate the mean of the closing prices for days `1-7`, then days `2-8`, then days `3-9`, and so on...

* Why use a rolling statistic?

  > A rolling statistics helps to show the progression or change of a particular metric over time. For example, calculating the average closing price of 1 year's worth of stock data will output a single metric, the average closing price for the year. On the contrary, a rolling 7-day mean will give you the change in weekly average closing prices over the course of the year.

* Rolling statistics tend to smooth out the trend of the initial dataset, allowing for more general or holistic analysis of a dataset rather than focusing on every twist and turn of the data. Overlaying a rolling statistic trend on top of the original data trend makes this feature easier to spot.

  ![rolling-statistic-overlay](Images/rolling-statistic-overlay.png)

* Rolling statistics factor in the progression of time. Therefore, a rolling 7-day window makes sense when looking at a short-term weekly investment scope; however, if investing for the long-term a rolling-180 day window might make more sense.

* Sometimes comparing different scopes of time can reveal insights that would not have been found otherwise. For example, comparing the 30-day rolling standard deviation to the 180-day rolling standard deviation of TSLA stock shows that although on a monthly scale there was a spike in volatility in late 2018, overall on a 6-month scale the highest spike in volatility was in late 2016, where the stock skyrocketed (remember standard deviation/volatility is how far data points deviate from the mean, this does not always necessarily have to be negative).

  ![daily-close-tsla](Images/daily-close-tsla.png)

  ![rolling-std-dev-30](Images/rolling-std-dev-30.png)

  ![rolling-std-dev-180](Images/rolling-std-dev-180.png)

---

### 7. Students Do: Simple Moving Averages (15 mins)

**Instructions:**

* [README.md](Activities/04_Stu_Rolling_Statistics/README.md)

**Files:**

* [simple_moving_averages.ipynb](Activities/04_Stu_Rolling_Statistics/Unsolved/simple_moving_averages.ipynb)

### 8. Instructor Do: Simple Moving Averages (5 mins)

**Files:**

* [simple_moving_averages.ipynb](Activities/04_Stu_Rolling_Statistics/Solved/simple_moving_averages.ipynb)

Open the solution and explain the following:

* The `rolling` function and the `window` parameter set the time window for the calculated metric, in this case the average or `mean`.

  ![rolling-mean-calculation](Images/rolling-mean-calculation.png)

* Notice the last `19` datetime indexes contain `NaN` values, this is because the `window` parameter has been set to `20` and therefore the last `19` indexes do not have enough data to support the `20` day time window. 

  ![not-enough-window-data](Images/not-enough-window-data.png)

* When overlaying the SMAs over the plot of the daily closing prices for NFLX, one can see the ways in which larger rolling time windows smooth data and show general trends as opposed to smaller rolling time windows that showcase more volatility.

  ![sma-overlay](Images/sma-overlay.png)

* When overlaying the STDs over the plot of the daily closing prices for NFLX, one can see the differences in volatility for different time scopes. 

  ![std-overlay](Images/std-overlay.png)

* Because Harold's company is looking to invest long-term in NFLX, the `SMA100` and `STD100` should hold more emphasis. Based on the chart overlays, although there is a recent price uptrend in late 2018, long-term volatility has been high for the entirety of 2018 to 2019. Therefore, it may be best to hold off on investing in NFLX long-term for now.

---

### 9. Instructor Do: Beta (10 mins)

**Files:**

* [beta.ipynb](Activities/05-Ins_Beta/Solved/beta.ipynb)

Walk through the solution and explain the following:

* What is covariance?

  > Covariance is a measure of the directional relationship between two variables. For example, covariances between two financial assets such as stock returns would imply that both stock returns would move together with a positive covariance and move inversely with a negative covariance.

  ![covariance.png](Images/covariance.png)

* What is variance?

  > Variance is a measurement of the spread between each number in a data set compares to the overall mean. It is calculated by taking the differences between each number in the data set and the mean, squaring the differences and dividing the sum of the squares by the number of values in the set.

  ![variance.png](Images/variance.png)

* What is the difference between covariance and variance?

  > Covariance refers to the measure of the directional relationship between two random variables while variance refers to the spread of a data set around its mean value.

* What is the difference between covariance and correlation?

  > Covariance is a measure of correlation. Correlation describes the directional relationship between two variables in a unit-free manner, while covariance describes the directional relationship between two variables with consideration for the type of data used (in this case, daily return values).

* What is beta?

  > Beta is the measure of the volatility of an individual stock in comparison to the volatility of the entire market.

  ![beta.png](Images/beta.png)

* What is the difference between beta and correlation?

  > Beta tries to measures the effect of one variable impacting the other variable. Correlations measure the possible frequency of similarly directional movements without considerations of cause and effect. Beta is the slope of the two variables. Correlation is the strength of that linear relationship.

  ![beta-vs-correlation.png](Images/beta-vs-correlation.png)

* It's often a good practice to plot the progression of beta values for a stock over time using rolling windows to see it's historical volatility relative to the market.

  ![rolling-beta.png](Images/rolling-beta.png)

---

### 10. Students Do: Beta Comparisons (15 mins)

**Instructions:**

* [README.md](Activities/06-Stu_Beta/README.md)

**Files:**

* [beta_comparisons.ipynb](Activities/06-Stu_Beta/Unsolved/beta_comparisons.ipynb)

### 11. Instructor Do: Beta Comparisons (5 mins)

**Files:**

* [beta_comparisons.ipynb](Activities/06-Stu_Beta/Solved/beta_comparisons.ipynb)

Open the solution and explain the following:

* Remember that combining the separate DataFrames for each social media stock and the S&P 500 into a single DataFrame makes it easier to calculate the daily returns for each stock by simply calling the `pct_change` function on the combined DataFrame.

  ![combined-dataframe](Images/combined-dataframe.png)

* The covariance quantifies the linear relationship between the each social media stock's returns and the returns of the overall market.

  ![social-media-covariance](Images/social-media-covariance.png)

* The variance quantifies the extent to which each data point tends to differ from the mean. In this case, variance describes the extent to which each daily return tends to differ from the overall average daily returns of the S&P 500.

  ![sp500-variance](Images/sp500-variance.png)

* The beta quantifies the relative volatility of each social media stock's returns to that of the overall market. For example, if the S&P 500 returns `10%` for the year, TWTR with a beta of `1.52` should expect to return approx. `15.2%` for the year.

  ![social-media-beta](Images/social-media-beta.png)

* Plotting multiple rolling beta values for each social media stock shows the progression of relative volatility to the market over time.

  ![rolling-social-media-beta](Images/rolling-social-media-beta.png)

* Based on the overall beta calculations and the plotted chart, it is evident that `SNAP` holds the lowest beta or relative volatility to the market. Interestingly enough however, while `FB` and `TWTR` took a steep plunge in early 2019, `SNAP` rose dramatically.

---

### 12. Instructor Do: Portfolio Returns (10 mins)

**Files:**

* [portfolio_returns.py](Activities/07-Ins_Portfolio_Returns/Solved/portfolio_returns.py)

Explain that portfolios of stocks are used by investors to manage and diversify risk. They can choose a portfolio of different percentages of stocks to control and adjust their risk.

Walk through the solution and highlight the following:

* To calculate portfolio returns, each stock's closing prices are added as a column to the final portfolio DataFrame.

  ![portfolio-dataframe.png](Images/portfolio-dataframe.png)

* Portfolio Daily Returns are first calculated individually with `pct_change`, but the total portfolio return is calculated using the weighted average (how much of each stock contributes to the total portfolio).

  ![portfolio-returns.png](Images/portfolio-returns.png)

* The portfolio returns can also be calculated using a dot product which is just a shortcut for the previous calculation. This can be handy for large portfolios with a lot of weights.

  ![dot-product.png](Images/dot-product.png)

* The purpose of a portfolio is to control the amount of risk and diversity in an investment. In the following example, AMD has more volatility than MU, so changing the weights of the portfolios (how much of each stock in invested in) may affect the returns.

  ![risk-management.png](Images/risk-management.png)

---

### 13. Students Do: Portfolio Planner Part I (20 mins)

In this activity, students will work in pairs to research a group of 10 stocks, find the least to most volatile stocks, drop the top 5 highly volatile stocks, set portfolio weights to the remaining stocks according to risk profile, and perform an analysis of a `$10,000` investment in the portfolio over time. 

**Instructions:**

* [README.md](Activities/08-Stu_Portfolio_Planner_Part_I/README.md)

**Files:**

* [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner_Part_I/Unsolved/portfolio_planner_part_1.ipynb)

### 14. Instructor Do: Portfolio Planner Part I (10 mins)

**Files:**

* [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner_Part_I/Solved/portfolio_planner_part_1.ipynb)

Open the solution and explain the following:

* Make sure to sort the DataFrame by index in ascending order when dealing with datetime indexes so as to start from the past to the present. This is particularly important when employing time-series functions such as `pct_change`.

  ![portfolio-planner-part-1-combine-sort-df](Images/portfolio-planner-part-1-combine-sort-df.png)

* Annualized volatility is calculated by multiplying standard deviation by the square root of the number of trading days in a year (252 days). Using the `sort_values` function quickly sorts each stock from least volatile to most volatile.

  ![assess-riskiness](Images/assess-riskiness.png)

* Portfolio weights represent the percentage of allocated capital to each stock. For example, a weight of `0.5` indicates that a single stock will be allocated `50%` of the capital within the portfolio. The sum of the weights should always equal `1`.

* The `dot` function multiples the weights by the daily return of each columns (4 weights, 4 stocks) and sums the total for each row.

  ![portfolio-planner-part-1-weights](Images/portfolio-planner-part-1-weights.png)

* Cumulative returns indicate the total return profit or loss from a percentage standpoint. Multiplying an initial investment of `$10,000` by the series of cumulative returns outputs a trend over time of cumulative profit or loss.

  ![portfolio-planner-cumulative-returns](Images/portfolio-planner-cumulative-returns.png)

  ![plot-cumulative-profit-loss](Images/plot-cumulative-profit-loss.png)

---

### 15. BREAK (40 mins)

---

### 16. Students Do: Portfolio Planner Part II (25 mins)

In this activity, students will work in pairs to continue where they left off in part I of evaluating portfolios. Students will now evaluate correlations and sharpe ratios of the 10 stocks, filter by only non-correlated and positive sharpe ratio stocks, set equal-weighted portfolio allocations to the remaining stocks, and perform an analysis of a `$10,000` investment in the portfolio over time. Then compare the `$10,000` investment in the portfolio to other `$10,000` investments in lesser optimized portfolios.

**Instructions:**

* [README.md](Activities/09-Stu_Portfolio_Planner_Part_II/README.md)

**Files:**

* [portfolio_planner_part_2.ipynb](Activities/09-Stu_Portfolio_Planner_Part_II/Unsolved/portfolio_planner_part_2.ipynb)

### 17. Instructor Do: Review Portfolio Planner Part II (5 mins)

**Files:**

* [portfolio_planner_part_2.ipynb](Activities/09-Stu_Portfolio_Planner_Part_II/Solved/portfolio_planner_part_2.ipynb)

Open the solution and explain the following:

* The 10 stocks will need to be filtered down by keeping only non-correlated stocks and stocks with positive sharpe ratios. This is to maximize diversification of the portfolio (and therefore minimize volatility) and maximize the returns-to-risk of the optimized portfolio, respectively.

* Stock correlation describes the linear relationship between the returns of two stocks and indicates whether returns of both stocks tend to move in tandem, inversely, or random (no correlation). The `corr` function used in conjunction with the `heatmap` function from the `seaborn` library makes it easy to spot the highly correlated stocks. In this case, the daily returns of `FANG` and `JNJ` appear to be highly correlated and can be dropped from the DataFrame.

  ![part-2-correlation](Images/part-2-correlation.png)

* Unlike volatility which measures risk, sharpe ratios describe the riskiness of stocks relative to their returns. Therefore, sharpe ratios measure risk-to-reward and indicate *value-driven* investments. The `mean` and `std` functions can be used to calculate the sharpe ratios of stocks.

  ![part-2-sharpe-ratios](Images/part-2-sharpe-ratios.png)

* An equal-weighted portfolio consists of the same weight for every stock in the portfolio (totaling `1`). For example, an equal-weighted stock portfolio of `5` stocks would have weights of `0.2`, `0.2`, `0.2`, `0.2`, and `0.2` to each stock.

  ![part-2-equal-weighted](Images/part-2-equal-weighted.png)

* The overlay chart of corresponding `$10,000` investments in each respective portfolio over time describes the following:

  * The non-correlated and sharpe-ratio optimized portfolio performs the best of the four portfolios and consistently acheives higher returns with minimized volatility.

  * The non-correlated (diversifed) portfolio performs the second worst of the four portfolios and manages to minimize volatility but at the expense of higher returns.

  * The original/unoptimized portfolio performs the second best of the four portfolios and acheives higher returns that but at the expense of more volatility. For example, returns rose quicker but fell faster as well (notice the dip in early 2019).

  * The risk-optimized portfolio performs the worst of the four portfolios and acheives minimal volatility but at the expense of returns.

  ![part-2-overlay](Images/part-2-overlay.png)

### 18. Instructor Do: Structured Office Hours (35 mins)

Please use the entire office hours time to review questions with the students.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### End Class

- - -

Trilogy Education Services © 2019. All Rights Reserved.