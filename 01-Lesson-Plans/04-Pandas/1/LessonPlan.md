## 4.1 Lesson Plan: Investing Like the Pros

---

### Overview

Today’s class will focus on analyzing the performance of groups of stocks, otherwise known as a portfolios. Stock portfolios proportion capital among several stocks to minimize risk. To create an optimal portfolio that maximizes returns while minimizing risk, it’s necessary to analyze the average return and risk of the portfolio overall and the correlations between stocks. In this lesson, students will learn how to analyze correlations between stocks, calculate rolling statistics and beta of stocks, optimize a portfolio, and compare portfolio performance.

### Class Objectives

By the end of class, students will be able to:

* Describe the benefits of investing in stock portfolios over investing in a single stock.

* Define correlation and explain how to calculate it in Pandas.

* Visualize trends through rolling statistics that smooth datasets and minimize data noise.

* Compare the volatility of a portfolio against the overall market (beta).

* Calculate expected returns of a portfolio utilizing custom weights.

* Build and optimize a portfolio by factoring in risk, correlation, and returns.

* Compare a portfolio's performance to that of other portfolios.

### Instructor Notes

* This lesson brings the heat on two fronts: statistics and financial knowledge. Not all students have experience in these subjects, so be mindful of this during class discussions and demonstrations. Be clear in your lectures, present code and charts visually whenever possible, and draw from your industry experience.

* Be aware that students may be confused about the differences between correlation and beta. Both attempt to measure relationships between variables; but whereas correlation measures the linear relationship between two variables, beta measures the unit-driven relationship between two variables (stock A returns vs. stock B returns). Be sure to explain these concepts clearly and allow time for students to ask questions.

* When explaining the notion of rolling statistics and how they benefit in identifying statistical trends, emphasize the comparison of the original data trend against the smoothed trend of the rolling statistic (mean or standard deviation).

* When discussing portfolios and its characteristics—risk, return, correlation—explain the concepts in terms of money. For example, if you start with $10,000, how would a poorly optimized portfolio compare with one that is not?

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [4.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2f56d5fa-30a1-4faf-b2af-aaa800fbbb53) Note that this video may not reflect the most recent lesson plan.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1j7jRO2rmGlzStxqgHDOZRPKMT9F5AKb66WqXxEK9y7Q/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Introduce today's lesson and get students excited for what they are about to learn. Today is when they will truly leverage Pandas to create insightful financial analyses.

Welcome students to the third day of Pandas! Open the slideshow and introduce the concepts that will be covered in today's class. Tell students the following:

* In the previous two classes, we focused on Pandas basics and single stock evaluation. Today, students will transition to analyzing groups of stocks (stock portfolios) to achieve the best risk-to-reward ratio for their investments.

* The focus of this lesson is on using Pandas to make more informed—and better!—investments. Students will be learning and using techniques used by financial analysts, quantitative traders, and portfolio managers. This should feel exciting and invigorating!

* Students should be prepared to test themselves mentally today, as they go from analyzing a single variable to analyzing an amalgamation of variables with relationships to one another.

* Get excited! Feel energized! Today is the day where students truly begin leveraging the power of Pandas to create insightful analyses that can benefit their skills in financial analysis and investing.

---

### 2. Instructor Do: Introduction to Portfolios (5 min)

Introduce stock portfolios using a discussion format to get students engaged in the topic.

Ask students the following questions about portfolios and then explain the corresponding answers:

* What is an investment portfolio?

  **Answer:** An investment portfolio is the grouping of various financial assets such as equities, bonds, commodities, and private investments, or the grouping of a single type of financial asset, such as equity.

* What is a stock portfolio?

  **Answer:** A stock portfolio is an investment portfolio consisting of only equity. A stock portfolio consists of multiple stocks ranging from some or all the 11 sectors of the equity market: financials, utilities, consumer discretionary, consumer staples, energy, health care, industrials, technology, telecom, materials, and real estate.

* Why are stock portfolios better than single stock investments?

  **Answer:** Single stock investments are risky in that they represent the "all eggs in one basket" problem. If the performance of a single stock fails, then so does the entirety of one's investment (as it is tied only to that particular stock). However, by grouping multiple stocks together, the risk is minimized or spread throughout the portfolio; a single stock might fail, but others can continue to succeed.

* What is a stock market index?

  **Answer:** Similar to a stock portfolio, a stock market index is a collection of stocks used to gauge the performance of a particular area within the stock market. For example, a popular stock market index is the S&P 500, a collection of 500 large market cap U.S. stocks that serve as a general health indicator of the overall U.S. stock market.

* Why do stock market indexes matter?

  **Answer:** Stock market indexes, like the S&P 500, serve as general health indicators for particular areas in the stock market. However, they also serve as benchmarks to compare performances of portfolios. For example, how does the performance of one's personal stock portfolio compare to that of the S&P 500 or general stock market?

Ask if there are any questions before moving on.

---

### 3. Instructor Do: Correlation (5 min)

**Corresponding Activity:** [01-Ins_Correlation](Activities/01-Ins_Correlation)

This part of the lesson introduces students to the concept of correlation, or the positive or negative relationship between two variables. Two datasets have been chosen to showcase the example of correlation: ice cream sales and drowning incidents.

**File:** [correlation.ipynb](Activities/01-Ins_Correlation/Solved/correlation.ipynb)

Open [correlation.ipynb](Activities/01-Ins_Correlation/Solved/correlation.ipynb). As you demo and show the plotted data, cover the following points:

* **Correlation** is the measure of a positive, negative, or neutral (random) relationship between two variables. For example, there is often a positive correlation between height and weight; that is, as you grow in height, you tend to weigh more.

* When comparing the line trend of ice cream sales to drowning incidents, it is difficult to detect a relationship between the two. Therefore, use a scatterplot and set the _x_ and _y_ axes to the corresponding DataFrame columns. With a scatterplot, the relationship becomes more apparent.![line-chart](Images/line-chart.png)
![scatterplot](Images/scatterplot.png)

* Use the `corr` function to calculate and output a matrix of correlation values for each column-to-column pair of a DataFrame. Correlation values range from -1 to +1.

  * -1 indicates a negative relationship: variables move inversely to one another.

  * 0 indicates a neutral relationship: variables have no relationship and move randomly.

  * +1 indicates a positive relationship: variables move in tandem with one another.

  ![correlation.png](Images/correlation.png)

* The `heatmap` function from the `seaborn` library color codes the different variations in a correlation table. This is particularly useful when there are many variables in a correlation table.

  ![correlation_seaborn.png](Images/correlation-seaborn.png)

* Remember that correlation does not imply causation!

  * Although `Ice Cream Sales` has a positive correlation of `0.819404` with `Drowning Incidents`, this does not mean that buying more ice cream causes people to drown; it simply means that there is a positive relationship between the numbers.

  * Chances are there is another factor at play that results in this positive correlation. One possible factor is that as temperature increases (during the summer months), people tend to both eat more ice cream and go swimming.

* **Multiple regression analysis** is a method we'll learn in a later unit that can measure multiple relationships at the same time (e.g., the effect of both weather and income on ice cream sales). This does not solve our problem of confusing correlation with causation, but it will help us better tease out economic relationships from multiple influences.

* How do these concepts apply to stock investments?

  * Investigating the correlations of returns among stocks in a portfolio can help analysts properly diversify their portfolios and mitigate risk and volatility.

  * Non-correlated stocks in a portfolio tend to cancel out large swings in volatility; one stock may increase in price while another may decrease in price rather than all stocks increasing or all stocks decreasing.

Ask if there are any questions before moving on.

---

### 4. Student Do: Diversification (15 min)

**Corresponding Activity:** [02-Stu_Correlation](Activities/02-Stu_Correlation)

In this activity, students will apply the concept of correlation to diversify a portfolio, a practical financial use case. In order to create a diversified portfolio that tends to minimize long-term volatility and risk, stocks within the portfolio should be as non-correlated as possible. Students need to find the stock with returns that are least correlated to the returns of stocks in an existing portfolio.

**File:** [market_analysis.ipynb](Activities/02-Stu_Correlation/Unsolved/diversification.ipynb)

**Instructions:** [README.md](Activities/02-Stu_Correlation/README.md)

### 5. Instructor Do: Review Diversification (5 min)

In this section, you will review the solution to the Diversification activity with students.

**File:** [diversification.ipynb](Activities/02-Stu_Correlation/Solved/diversification.ipynb)

Open the solution file, [diversification.ipynb](Activities/02-Stu_Correlation/Solved/diversification.ipynb), and explain the following:

* Diversification of stock portfolios is an important strategy in the realm of investing, as total capital is proportioned among several stocks, thereby minimizing risk by preventing the "all eggs in one basket" dilemma. Therefore, it is necessary to not only analyze the average return and risk of the portfolio overall, but also the correlation between stocks (how much one stock price changes with or against another).

* The `corr` function compares values from each column-to-column pair. Therefore, make sure that the DataFrame is properly formatted on a column-by-column basis for analysis.

  ![formatted-dataframe](Images/formatted-dataframe.png)

* When viewing a correlation table with many variables present, it's difficult to distinguish lower values from higher values. Using the `heatmap` function from the `seaborn` library makes it easier to discern differences by using color gradients.

  ![correlation-table](Images/correlation-table.png)

  ![correlation-heatmap](Images/correlation-heatmap.png)

* Use the `vmin` and `vmax` parameters with the `heatmap` function to modify the scale of the heatmap. Correlation values range from `-1` to `0` to `+1` , therefore the scale of the heatmap will need to reflect this.

  ![correlation-heatmap-scaled](Images/correlation-heatmap-scaled.png)

* Look at the heatmap and cross reference the correlation table. It would appear as though the AMD stock appears to be the least correlated of the semiconductor stocks. Therefore, AMD stock would be the best semiconductor stock to add to the existing portfolio.

  ![correlation-heatmap-focus](Images/correlation-heatmap-focus.png)

  ![correlation-table-focus](Images/correlation-table-focus.png)

Ask if there are any questions before moving on.

---

### 6. Instructor Do: Rolling Statistics (10 min)

**Corresponding Activity:** [03-Ins_Rolling_Statistics](Activities/03-Ins_Rolling_Statistics)

This section focuses on the concept of rolling statistics, in which a series of a particular metric is calculated over a shifting window of time. Rolling statistics help view the change or progression of a particular metric over time and therefore aid in identifying statistical trends.

**File:** [rolling_statistics.ipynb](Activities/03-Ins_Rolling_Statistics/Solved/rolling_statistics.ipynb)

Walk through the solution and explain the following:

* A **rolling statistic** is a metric calculated over the range of a shifting, or rolling, window. For example, a 7-day rolling mean of 14 days' worth of closing prices for a stock would calculate the mean of the closing prices for days 1–7, and then days 2–8, and then days 3–9, and so on.

* Some commonly used rolling statistics are rolling averages, otherwise known as simple moving averages, and rolling standard deviations.

* Rolling statistics help to show the progression or change of a particular metric over time. For example, calculating the average closing price of one year's worth of stock data will output a single metric, the average closing price for the year. But a rolling 7-day mean will give you the change in weekly average closing prices over the course of the year.

* Rolling statistics tend to smooth out the trend of the initial dataset, allowing for more general or holistic analysis of a dataset rather than focusing on every twist and turn of the data. Overlaying a rolling statistic trend on top of the original data trend makes this feature easier to spot.

  ![rolling-statistic-overlay](Images/rolling-statistic-overlay.png)

* Rolling statistics factor in the progression of time. Therefore, a rolling 7-day window makes sense when looking at a short-term weekly investment scope. However, if investing for the long term, a rolling 180-day window might make more sense.

* Comparing different scopes of time can sometimes reveal insights that would not have been found otherwise.

  For example, consider the 30-day rolling standard deviation as compared to the 180-day standard deviation of TSLA stock.

  Although on a monthly scale there was a spike in volatility in late 2018, over a 6-month period, the highest spike in volatility was in late 2016 when the stock skyrocketed.

  **Note:** Remember that standard deviation/volatility is how far data points deviate from the mean; this does not necessarily need to be negative.

  ![daily-close-tsla](Images/daily-close-tsla.png)

  ![rolling-std-dev-30](Images/rolling-std-dev-30.png)

  ![rolling-std-dev-180](Images/rolling-std-dev-180.png)

---

### 7. Students Do: Simple Moving Averages (15 mins)

**Corresponding Activity:** [04-Stu_Rolling_Statistics](Activities/04-Stu_Rolling_Statistics)

In this activity, students will calculate multiple windows of rolling statistics, such as moving averages and rolling standard deviations, in order to identify trends in average price and volatility/risk that can provide insight to the investment decisions concerning a particular stock.

**Instructions:**

Students will calculate multiple windows of rolling statistics such as moving averages and rolling standard deviations. The goal is to identify trends in average price and volatility/risk in order to make the smartest investment decision.

**File:** [simple_moving_averages.ipynb](Activities/04-Stu_Rolling_Statistics/Unsolved/simple_moving_averages.ipynb)

**Instructions:** [README.md](Activities/04-Stu_Rolling_Statistics/README.md)

### 8. Instructor Do: Review Simple Moving Averages (5 min)

In this section, review the solution to the previous activity, Simple Moving Averages.

**File:** [simple_moving_averages.ipynb](Activities/04-Stu_Rolling_Statistics/Solved/simple_moving_averages.ipynb)

Open the solution file, [simple_moving_averages.ipynb](Activities/04-Stu_Rolling_Statistics/Solved/simple_moving_averages.ipynb), and explain the following:

* The `rolling` function and the `window` parameter set the time window for the calculated metric, which in this case is the average or mean.

  ![rolling-mean-calculation](Images/rolling-mean-calculation.png)

* Notice that the last 19 datetime indexes contain NaN values. This is because the `window` parameter has been set to `20`; therefore, the last 19 indexes do not have enough data to support the 20-day window.

  ![not-enough-window-data](Images/not-enough-window-data.png)

* When overlaying the plot of daily closing prices for NFLX with its simple moving averages, you can see the ways in which larger rolling time windows smooth data and show general trends, as opposed to smaller rolling time windows that showcase more volatility.

  ![sma-overlay](Images/sma-overlay.png)

* When overlaying the plot of daily closing prices for NFLX with its rolling standard deviations, you can see the differences in volatility for different time periods.

  ![std-overlay](Images/std-overlay.png)

* Because the desire is to invest long term in NFLX, the `SMA100` and `STD100` should hold more emphasis. Based on the chart overlays, although there is a recent price uptrend in late 2018, long-term volatility has been high for the entirety of 2018 to 2019. Therefore, it may be best to hold off on investing in NFLX long term for now.

Ask if there are any questions before moving on.

### 9. Instructor Do: Beta (10 min)

**Corresponding Activity:** [05-Ins_Beta](Activities/05-Ins_Beta)

In this activity, students will be introduced to the concept of beta and how it is used to determine the relative *unit-driven* performance of one variable to another. For example calculating the beta value of a stock's returns relative to the returns of the overall market.

**File:** [beta.ipynb](Activities/05-Ins_Beta/Solved/beta.ipynb)

Open [beta.ipynb](Activities/05-Ins_Beta/Solved/beta.ipynb). As you walk through the demo, explain the following.

* What is covariance?

  * **Covariance** is a measure of the directional relationship between two variables. For example, the covariances between two financial assets such as stock returns would imply that both stock returns would move together with a positive covariance and move inversely with a negative covariance.

  ![covariance.png](Images/covariance.png)

* What is variance?

  * **Variance** is the measurement of how far numbers in a dataset are spread about their mean. For example, let's say stock A has an average price of $50, but varies in price as low as $5 and as high as $90. However, stock B averages $50, but varies in price as low as $40 and as high as $60. Stock A has a higher variance than stock B.

  ![variance.png](Images/variance.png)

* What is the difference between covariance and variance?

   * Variance looks at one variable, measuring the range in which that variable’s values may take. By contrast, covariance looks at the variance of two variables, and studies how those two variables vary together.
   * Covariance is similar in concept to correlation: the difference is that covariance values are usually too difficult to interpret (other than being positive or negative), whereas correlation is a standardized value (regardless of data type) that ranges from -1 to 1.

* How do covariance and variance relate to beta?

  * **Beta** uses covariance and variance to calculate the relative volatility of an individual stock's returns in comparison to the volatility of the overall market's returns.

  ![beta.png](Images/beta.png)

* What is the difference between beta and correlation?

  * Beta measures the impact of one variable on another variable. Correlations measure the possible frequency of similar directional movements without consideration for cause and effect.

  * Beta is the slope of the two variables. Correlation is the strength of that linear relationship.

  ![beta-vs-correlation.png](Images/beta-vs-correlation.png)

* A good practice is to plot the progression of beta values for a stock over time using rolling windows to see its historical volatility relative to the market.

  ![rolling-beta.png](Images/rolling-beta.png)

Ask if there are any questions before moving on.

---

### 10. Student Do: Beta Comparisons (15 min)

**Corresponding Activity:** [06-Stu_Beta](Activities/06-Stu_Beta)

In this activity, students will apply their knowledge of rolling statistics and beta to plot the 30-day rolling betas of a group of stocks. The goal is to determine the most conservative stock choice, or the stock with the lowest beta.

**File:** [beta_comparisons.ipynb](Activities/06-Stu_Beta/Unsolved/beta_comparisons.ipynb)

**Instructions:** [README.md](Activities/06-Stu_Beta/README.md)

### 11. Instructor Do: Review Beta Comparisons (5 min)

In this section, review the solution to the previous activity, Beta Comparisons.

**File:** [beta_comparisons.ipynb](Activities/06-Stu_Beta/Solved/beta_comparisons.ipynb)

Open the solution file, [beta_comparisons.ipynb](Activities/06-Stu_Beta/Solved/beta_comparisons.ipynb), and explain the following:

* Combine the DataFrames for each social media stock and the S&P 500 into a single DataFrame. This makes it easier to calculate the daily returns for each stock; simply call the `pct_change` function on the combined DataFrame.

  ![combined-dataframe](Images/combined-dataframe.png)

* The covariance quantifies the linear relationship between each social media stock's returns and the returns of the overall market.

  ![social-media-covariance](Images/social-media-covariance.png)

* The variance quantifies the extent to which each data point tends to differ from the mean. In this case, variance describes the extent to which each daily return tends to differ from the overall average daily returns of the S&P 500.

  ![sp500-variance](Images/sp500-variance.png)

* The beta quantifies the relative volatility of each social media stock's returns to that of the overall market. For example, if the S&P 500 returns 10% for the year, `TWTR` with a beta of 1.52 should expect to return approximately 15.2% for the year.

  ![social-media-beta](Images/social-media-beta.png)

* Plotting multiple rolling beta values for each social media stock shows the progression of relative volatility to the market over time.

  ![rolling-social-media-beta](Images/rolling-social-media-beta.png)

* Based on the overall beta calculations and the plotted chart, it is evident that `SNAP` holds the lowest beta, or relative volatility to the market. Interestingly enough, however, while `FB` and `TWTR` took a steep plunge in early 2019, `SNAP` rose dramatically.

Ask if there are any questions before moving on.

---

### 12. BREAK (40 min)

---

### 13. Instructor Do: Portfolio Returns (10 min)

**Corresponding Activity:** [07-Ins_Portfolio_Returns](Activities/07-Ins_Portfolio_Returns)

This section focuses on calculating returns for a group of stocks, or stock portfolios. Students should understand that portfolios of stocks are used by investors to manage and diversify risk. Defining a portfolio with varying capital allocations of stocks allows an investor to control and adjust their risk.

**File:** [portfolio_returns.py](Activities/07-Ins_Portfolio_Returns/Solved/portfolio_returns.ipynb)

Open [portfolio_returns.py](Activities/07-Ins_Portfolio_Returns/Solved/portfolio_returns.ipynb) to review the solution. Cover the following points as you walk through the solved file.

* To calculate portfolio returns, each stock's closing prices are added as a column to the final portfolio DataFrame.

  ![portfolio-dataframe.png](Images/portfolio-dataframe.png)

* Portfolio daily returns are first calculated individually with `pct_change`. The total portfolio return is calculated using the weighted average (how much of each stock contributes to the total portfolio).

  ![portfolio-returns.png](Images/portfolio-returns.png)

* The portfolio returns can also be calculated using a dot product, which is just a shortcut for the previous calculation. This can be handy for large portfolios with a lot of weights.

  ![dot-product.png](Images/dot-product.png)

* The purpose of a portfolio is to control the amount of risk and diversity in an investment. In the following example, AMD has more volatility than MU, so changing the weights of the portfolios (how much of each stock in invested in) may affect the returns.

  ![risk-management.png](Images/risk-management.png)

Ask if there are any questions before moving on.

### 14. Student Do: Portfolio Planner, Part 1 (20 min)

**Corresponding Activity:** [08-Stu_Portfolio_Planner_Part_I](Activities/08-Stu_Portfolio_Planner_Part_I)

In this activity, students will work in pairs to research a group of 10 stocks, find the least to most volatile stocks, drop the top five highly volatile stocks, set portfolio weights to the remaining stocks according to risk profile, and perform an analysis of a `$10,000` investment in the portfolio over time.

**File:** [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner_Part_I/Unsolved/portfolio_planner_part_1.ipynb)

**Instructions:** [README.md](Activities/08-Stu_Portfolio_Planner_Part_I/README.md)

### 15. Instructor Do: Review Portfolio Planner, Part 1 (10 min)

In this section, review the solution to the previous activity, Portfolio Planner, Part 1.

**File:** [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner_Part_I/Solved/portfolio_planner_part_1.ipynb)

Open the solution, [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner_Part_I/Solved/portfolio_planner_part_1.ipynb), and explain the following:

* When dealing with datetime indexes, make sure to sort the DataFrame by index in ascending order, so as to arrange the dates chronologically from past to present. This is particularly important when employing time-series functions such as `pct_change`.

  ![portfolio-planner-part-1-combine-sort-df](Images/portfolio-planner-part-1-combine-sort-df.png)

* Annualized volatility is calculated by multiplying standard deviation by the square root of the number of trading days in a year (252 days). Using the `sort_values` function quickly sorts each stock from least volatile to most volatile.

  ![assess-riskiness](Images/assess-riskiness.png)

* Portfolio weights represent the percentage of allocated capital to each stock. For example, a weight of 0.5 indicates that a single stock will be allocated 50% of the capital within the portfolio. The sum of the weights should always equal 1.

* The `dot` function multiplies the weights by the daily return of each column (four weights, four stocks) and sums the total for each row.

  ![portfolio-planner-part-1-weights](Images/portfolio-planner-part-1-weights.png)

* Cumulative returns indicate the total return profit or loss from a percentage standpoint. Multiplying an initial investment of $10,000 by the series of cumulative returns outputs a trend over time of cumulative profit or loss.

  ![portfolio-planner-cumulative-returns](Images/portfolio-planner-cumulative-returns.png)

  ![plot-cumulative-profit-loss](Images/plot-cumulative-profit-loss.png)

Ask if there are any questions before moving on.

### 16. Students Do: Portfolio Planner Part 2 (20 mins)

**Corresponding Activity:** [09-Stu_Portfolio_Planner_Part_II](Activities/09-Stu_Portfolio_Planner_Part_II)

In this activity, students will work in pairs to continue from where they left off in Part 1 of their portfolio evaluation. In this next part, students will evaluate correlations and Sharpe ratios of the 10 stocks, and then filter by only minimally-correlated and high positive Sharpe ratio stocks. They will also set equal-weighted portfolio allocations to those remaining stocks and perform an analysis of a $10,000 investment in the portfolio over time. Finally, they will compare the $10,000 investment in the portfolio to other $10,000 investments in lesser-optimized portfolios.

**File:** [portfolio_planner_part_2.ipynb](Activities/09-Stu_Portfolio_Planner_Part_II/Unsolved/portfolio_planner_part_2.ipynb)

**Instructions:** [README.md](Activities/09-Stu_Portfolio_Planner_Part_II/README.md)

### 17. Instructor Do: Review Portfolio Planner, Part 2 (5 min)

In this section, review the solution to the previous activity, Portfolio Planner, Part 2.

**File:** [portfolio_planner_part_2.ipynb](Activities/09-Stu_Portfolio_Planner_Part_II/Solved/portfolio_planner_part_2.ipynb)

Open the solution, [portfolio_planner_part_2.ipynb](Activities/09-Stu_Portfolio_Planner_Part_II/Solved/portfolio_planner_part_2.ipynb), and explain the following:

* Filter the 10 stocks to just the least-correlated stocks and stocks with the highest Sharpe ratios. This is to maximize diversification of the portfolio—and, therefore, minimize overall volatility—and maximize the risk-to-returns ratio of the optimized portfolio.

* Stock correlation describes the linear relationship between the returns of two stocks, and indicates whether returns of both stocks tend to move in tandem (high correlation), inversely (negative correlation), or randomly (no correlation).

  * The `corr` function used in conjunction with the `heatmap` function from the `seaborn` library makes it easy to spot the highly correlated stocks.

  * In this case, the daily returns of `BK` and `WRK` appear to be the most consistently and highly correlated with the other stocks and can be dropped from the DataFrame.

  ![part-2-correlation](Images/part-2-correlation.png)

* Unlike volatility, which measures risk, Sharpe ratios describe the riskiness of stocks relative to their returns. Therefore, Sharpe ratios measure risk-to-reward and indicate value-driven investments. The `mean` and `std` functions are used to calculate the Sharpe ratios of stocks.

  ![part-2-sharpe-ratios](Images/part-2-sharpe-ratios.png)

* An equal-weighted portfolio consists of the same weight for every stock in the portfolio (totaling 1). For example, an equal-weighted stock portfolio of five stocks would have weights of 0.2, 0.2, 0.2, 0.2, and 0.2 for each stock.

  ![part-2-equal-weighted](Images/part-2-equal-weighted.png)

* The overlay chart of a $10,000 investments in each corresponding portfolio over time describes the following:

  * The minimally-correlated and Sharpe ratio optimized portfolio performs the best of the four portfolios, consistently achieving higher returns with minimized volatility.

    * The minimally-correlated (diversified) portfolio performs the second worst of the four portfolios; it manages to minimize volatility, but at the expense of higher returns.

  * The original, unoptimized portfolio performs the second best of the four portfolios; it achieves higher returns but at the expense of more volatility. Returns increased more quickly, but also fell more quickly—notice the dip in early 2019.

  * The risk-optimized portfolio performs the worst of the four portfolios, achieving minimal volatility but at the expense of returns.

  ![part-2-overlay](Images/part-2-overlay.png)

Ask if there are any questions before moving on.

### 18. Instructor Do: Decompress (5 min)

Spend this time letting students share their thoughts about this class, and also offer some encouraging words to boost motivation.

Start by giving students positive feedback.

* Students have come a long way in this Pandas unit!

* Not only have they learned how to use the Pandas library, but they have begun to perform analysis and apply investment strategies like professional investors.

Survey the class to get a sense of how they are feeling at this point in the unit and course overall. Are there any concepts that are still giving them trouble? Students should feel challenged but not lost.

Ask students questions such as the following:

* What activity was the most enjoyable to complete? The most fulfilling?

* What activity was the most stressful or difficult? Why?

* Did today's lesson flow well and make sense?

Remind students that mastery doesn't happen in a day. Practice makes perfect!

---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
