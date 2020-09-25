## 4.1 Lesson Plan: Investing Like the Pros

### Overview

Today’s class will focus on analyzing the performance of groups of stocks, otherwise known as portfolios. Stock portfolios proportion capital among several stocks to minimize risk. To create an optimal portfolio that maximizes returns while minimizing risk, it’s necessary to analyze the average return and risk of the portfolio overall and the correlations between stocks. In this lesson, students will learn how to analyze correlations between stocks, calculate rolling statistics and beta of stocks, optimize a portfolio, and compare portfolio performance.

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

* Be aware that students may be confused about the differences between correlation and beta. Both measure relationships between variables; but while correlation measures the linear relationship between two variables, beta measures the unit-driven relationship between two variables (Stock A returns vs. Stock B returns). Be sure to explain these concepts clearly, and allow time for students to ask questions.

* When explaining the notion of rolling statistics and how they benefit in identifying statistical trends, emphasize the comparison of the original data trend against the smoothed trend of the rolling statistic (mean or standard deviation).

* When discussing portfolio characteristics—namely, risk, return, and correlation—explain the concepts in terms of money. For example, if you start with $10,000, how would a poorly optimized portfolio compare with one that is not?

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [4.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2f56d5fa-30a1-4faf-b2af-aaa800fbbb53) Note that this video may not reflect the most recent lesson plan.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/12R6JD6VwF7xqWWM5DEKbtGHDOUO8tZ-W-fyW5NEUsfo/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Introduce today's lesson and get students amped on what they're about to learn—today they'll genuinely leverage Pandas to create insightful financial analyses.

Welcome to the third day of Pandas! Open the slideshow and introduce the concepts that will be covered, highlighting the following:

* In the previous two classes, we focused on Pandas basics and single stock evaluation. Today, you will transition into analyzing groups of stocks (stock portfolios) to achieve the best risk-to-reward ratio for your investments.

* The focus of this lesson is on using Pandas to make more informed—and better!—investments. Get excited, as you will learn and use techniques used by financial analysts, quantitative traders, and portfolio managers. 

* Prepare to test yourselves mentally, as you go from analyzing a single variable to analyzing an amalgamation of variables with relationships to one another.

* Get pumped up! Today is the day you'll truly begin leveraging the power of Pandas to create insightful analyses that can benefit your skills in financial analysis and investing.

---

### 2. Instructor Do: Introduction to Portfolios and Correlation (15 min)

In this activity, you will use a discussion format to introduce stock portfolios and some of the particular regulations in Canada for FinTech companies. This activity also introduces students to the concept of correlation, or the positive or negative relationship between two variables.

**Files:**

* [correlation.ipynb](Activities/01-Ins_Correlation/Solved/correlation.ipynb)

* [drowning.csv](Activities/01-Ins_Correlation/Resources/drowning.csv)

* [ice_cream.csv](Activities/01-Ins_Correlation/Resources/ice_cream.csv)

Open the lesson slides, move to the "Introduction to Portfolios" section and review the following Q&A with students:

* What is an investment portfolio?

  **Answer:** An investment portfolio is the grouping of various financial assets such as equities, bonds, commodities, and private investments, or the grouping of a single type of financial asset, such as equity.

* What is a stock portfolio?

  **Answer:** It's is an investment portfolio consisting of only equity. A stock portfolio includes multiple stocks ranging from some or all the eleven sectors of the equity market: financials, utilities, consumer discretionary, consumer staples, energy, health care, industrials, technology, telecom, materials, and real estate.

* Why are stock portfolios better than single stock investments?

  **Answer:** Single stock investments are risky as they represent the "all eggs in one basket" problem. If the performance of a single stock fails, then so does the entirety of one's investment (as it is tied only to that particular stock). However, by grouping multiple stocks, the risk is minimized, or spread throughout the portfolio. While a single stock might fail, others can continue to succeed.

* What is a stock market index?

  **Answer:** Similar to a stock portfolio, a stock market index is a collection of stocks used to gauge the performance of a particular area within the stock market. For example, a popular stock market index is the S&P TSX 60, a collection of 60 large companies listed on the Toronto Stock Exchange which serves as a general health indicator of the overall Canadian stock market.

* Why do stock market indexes matter?

  **Answer:** Stock market indexes, like the S&P TSX 60, serve as general health indicators for particular areas in the stock market. They are also used as benchmarks to compare performances of portfolios. For example, how does the performance of one's stock portfolio compare to that of the S&P TSX 60 or the general stock market?

Continue the presentation by moving to the "Correlation" section of the slideshow, and highlight the following:

* **Correlation** is the measure of a positive, negative, or neutral (random) relationship between two variables. For example, there is often a positive correlation between height and weight; that is, as your height increases, you tend to weigh more.

* Two given variables may have a positive or negative correlation.

  * A **positive correlation** is a relationship between two variables where one variable decreases as the other variable decreases or one variable increases while the other increases.

  * A **negative correlation** is a relationship between two variables in which one variable increases as the other decreases, and vice versa.

* Regardless of two variables that may be correlated, be aware that correlation doesn't mean causation, as you will see in this next demo.

Open the unsolved version of the Jupyter notebook, live code the solution and highlight the following:

* In this demo, we will verify if there is any correlation between ice cream sales and drowning incidents.

* We will start this demo by reading the ice cream sales data and the drowning incident data into two DataFrames and setting the `Month` column as the index.

  ![correlation_data](Images/correlation_data.png)

* Before verifying the correlation between these two variables, we will concatenate both DataFrames.

  ![correlation_concat_data](Images/correlation_concat_data.png)

* Now, we will plot the data from the concatenated DataFrame. When comparing the line trend of ice cream sales to drowning incidents, it is difficult to detect a relationship between the two variables.

  ![line-chart](Images/line-chart.png)

* However, if we use a scatter plot and set the _x_ and _y_ axes to the corresponding DataFrame columns, the relationship becomes more apparent.

  ![scatterplot](Images/scatterplot.png)

* Pandas provides the `corr` function to calculate and output a matrix of correlation values for each column-to-column pair of a DataFrame. Correlation values range from `-1` to `+1`.

  * `-1` indicates a negative relationship: variables move inversely to one another.

  * `0` indicates a neutral relationship: variables have no relationship and move randomly.

  * `+1` indicates a positive relationship: variables move in tandem with one another.

* As you can observe, although it sounds crazy, there is a positive correlation between these two variables.

  ![correlation.png](Images/correlation.png)

* Pandas doesn't offer a plot to visualize correlation, so we will use `Seaborn`, a popular Python data visualization library that is built into Anaconda to create a heat map plot. In later units, we will learn about even more advanced plotting libraries.

* The `heatmap` function from the `Seaborn` library colour codes the different variations in a correlation table. This is particularly useful when there are many variables in a correlation table.

* When you are plotting correlations, it's useful to set the parameters `vmin=-1` and `vmax=1` to set a suitable range for the colour map.

  ![correlation_seaborn.png](Images/correlation-seaborn.png)

* Remember: Correlation does not imply causation!

  * Although `Ice Cream Sales` has a positive correlation of `0.819404` with `Drowning Incidents`, this does not mean that buying more ice cream causes people to drown; it merely means that there is a positive relationship between the numbers.

  * Chances are there is another factor at play that results in this positive correlation. One possibility is that as the temperature rises during the summer months, people tend to eat more ice cream, and go swimming.

Explain to students that **Regression analysis** is a method we'll learn in a later unit that can measure multiple relationships at the same time (e.g., the effect of both weather and income on ice cream sales). This explanation may not solve our problem of confusing correlation with causation, but it will help us better tease out economic relationships from multiple influences. Close this activity by asking the following question:

* How do these concepts apply to stock investments?

  **Answer:** Investigating the correlations of returns among stocks in a portfolio can help analysts properly diversify their portfolios and mitigate risk and volatility.

  Non-correlated stocks in a portfolio tend to cancel out large swings in volatility; one stock may increase in price, while another may decrease in price, rather than all stocks increasing or all stocks decreasing.

Answer any questions before moving on.

---

### 3. Student Do: Diversification (15 min)

In this practical financial use case, students will apply the concept of correlation to diversify a portfolio. In order to create a diversified portfolio that minimizes long-term volatility and risk, stocks within the portfolio should be as non-correlated as possible. Students need to find the stock with returns that are least correlated to the returns of stocks in an existing portfolio.

**Files:**

* [market_analysis.ipynb](Activities/02-Stu_Correlation/Unsolved/diversification.ipynb)

* [BMO.csv](Activities/02-Stu_Correlation/Resources/BMO.csv)

* [CNQ.csv](Activities/02-Stu_Correlation/Resources/CNQ.csv)

* [CVE.csv](Activities/02-Stu_Correlation/Resources/CVE.csv)

* [ENB.csv](Activities/02-Stu_Correlation/Resources/ENB.csv)

* [IMO.csv](Activities/02-Stu_Correlation/Resources/IMO.csv)

* [IPL.csv](Activities/02-Stu_Correlation/Resources/IPL.csv)

* [TRP.csv](Activities/02-Stu_Correlation/Resources/TRP.csv)

**Instructions:**

* [README.md](Activities/02-Stu_Correlation/README.md)

---

### 4. Instructor Do: Review Diversification (10 min)

In this section, you will review the solution to the Diversification activity with students.

**Files:**

* [market_analysis.ipynb](Activities/02-Stu_Correlation/Solved/diversification.ipynb)

* [BMO.csv](Activities/02-Stu_Correlation/Resources/BMO.csv)

* [CNQ.csv](Activities/02-Stu_Correlation/Resources/CNQ.csv)

* [CVE.csv](Activities/02-Stu_Correlation/Resources/CVE.csv)

* [ENB.csv](Activities/02-Stu_Correlation/Resources/ENB.csv)

* [IMO.csv](Activities/02-Stu_Correlation/Resources/IMO.csv)

* [IPL.csv](Activities/02-Stu_Correlation/Resources/IPL.csv)

* [TRP.csv](Activities/02-Stu_Correlation/Resources/TRP.csv)

Open the solution file, live code the solution, and explain the following:

* When investing, diversification of stock portfolios is an important strategy, as total capital is proportioned among several stocks, thereby minimizing risk by preventing the "all eggs in one basket" dilemma. It is important to analyze the average return and risk of the portfolio overall, as well as the correlation between stocks (how much one stock price changes with or against another).

* The first step towards helping Harold decide which energy stock to include in the portfolio is to load the data files, concatenate all the data in a single DataFrame, and calculate the daily returns using the `pct_change` function.

  ![diversifications_daily_returns](Images/diversifications_daily_returns.png)

* The `corr` function compares values from each column-to-column pair. When viewing a correlation table with many variables, it's difficult to distinguish lower values from higher values.

  ![correlation-table](Images/correlation-table.png)

* The `heatmap` function from the `Seaborn` library makes it easier to discern differences by using colour gradients.

  ![correlation-heatmap](Images/correlation-heatmap.png)

* Use the `vmin` and `vmax` parameters with the `heatmap` function to modify the scale of the heatmap. Correlation values range from `-1` to `0` to `+1`. Therefore, the scale of the heatmap needs to reflect this.

  ![correlation-heatmap-scaled](Images/correlation-heatmap-scaled.png)

* Look at the heatmap and cross-reference the correlation table. It appears that the `ENB` stock seems to be the least correlated with the energy stocks. Therefore, the `ENV` stock would be the best energy stock to add to the existing portfolio.

  ![correlation-heatmap-focus](Images/correlation-heatmap-focus.png)

  ![correlation-table-focus](Images/correlation-table-focus.png)

Answer any questions before moving on.

---

### 5. Instructor Do: Rolling Statistics (10 min)

This section focuses on the concept of rolling statistics, in which a series of a particular metric is calculated over a shifting window of time. Rolling statistics help view the change or progression of a particular metric over time and, therefore, aid in identifying statistical trends.

**Files:**

* [rolling_statistics.ipynb](Activities/03-Ins_Rolling_Statistics/Solved/rolling_statistics.ipynb)

* [tsla_historical.csv](Activities/03-Ins_Rolling_Statistics/Resources/tsla_historical.csv)

Open the lesson slides, move to the "Rolling Statistics" section, and explain the following:

* A **rolling statistic** is a metric calculated over the range of a shifting, or rolling, window. For example, a 7-day rolling mean of 14 days' worth of closing prices for a stock would calculate the mean of the closing prices for days 1–7, days 2–8, days 3–9, and so on.

* Some commonly used rolling statistics are rolling averages (otherwise known as simple moving averages), and rolling standard deviations.

* Rolling statistics help demonstrate the progression, or change, of a particular metric over time. For example, calculating the average closing price of one year's worth of stock data will output a single metric, the average closing price for the year. But a rolling 7-day mean will give you the change in weekly average closing prices over the year.

Close the presentation, open the unsolved version of the Jupyter notebook, and live code the demo by highlighting the following:

* In this demo, we will analyze historical stock data from Tesla Inc. (`TSLA`) to calculate rolling statistics in Python.

* When you read time series data into a Pandas DataFrame, it's important to set the date as an index and to sort the index in ascending order.

  ![rolling_stats_read_data](Images/rolling_stats_read_data.png)

* When we plot the daily closing prices, we can see a general trend of the prices with several spikes.

  ![rolling_stats_daily_prices](Images/rolling_stats_daily_prices.png)

* Rolling statistics tend to smooth out the trend of the initial dataset. This allows for a more general or holistic analysis of a dataset, rather than focusing on every twist and turn of the data.

* Rolling statistics factor in the progression of time. Therefore, a rolling 7-day window makes sense to smooth out the trend when looking at a short-term, weekly investment scope. Two valuable metrics to calculate in rolling statistics are the mean, and the standard deviation.

  ![rolling_stats_7_days](Images/rolling_stats_7_days.png)

* For a mid-term investment scope, we may compute the rolling statistics with a 30-day window.

  ![rolling_stats_30_days](Images/rolling_stats_30_days.png)

* However, if you are investing for the long-term, a rolling 180-day window might make more sense.

  ![rolling_stats_180_days](Images/rolling_stats_180_days.png)

* Comparing different scopes of time can sometimes reveal insights that would not have been found otherwise.

* For example, consider the 30-day rolling standard deviation as compared to the 180-day standard deviation of TSLA stock.

* Remember that standard deviation/volatility is how far data points deviate from the mean; this does not necessarily need to be negative.

* While there was a spike in volatility on a monthly scale in late 2018, over six months, the highest spike in volatility was in late 2016, when the stock skyrocketed.

Explain to students that overlaying a rolling statistic trend on top of the original data trend makes this feature easier to spot.

Highlight to students that it's possible to overlay two plots using Pandas. The first plot is assigned to a variable that is commonly named as `ax`. When the second plot is created, the `ax` parameter of the `plot` function is set as the variable where the first plot was stored (e.g. `ax=ax`).

![rolling-statistic-overlay](Images/rolling-statistic-overlay.png)

Answer any questions before moving on.

---

### 6. Student Do: Simple Moving Averages (15 mins)

In this activity, students will calculate multiple windows of rolling statistics, such as moving averages and rolling standard deviations, to identify trends in average price and volatility/risk that can provide insight to the investment decisions concerning a particular stock.

**Files:**

* [simple_moving_averages.ipynb](Activities/04-Stu_Rolling_Statistics/Unsolved/simple_moving_averages.ipynb)

* [shop.csv](Activities/04-Stu_Rolling_Statistics/Resources/shop.csv)

**Instructions:**

* [README.md](Activities/04-Stu_Rolling_Statistics/README.md)

---

### 7. Instructor Do: Review Simple Moving Averages (10 min)

In this section, review the solution to the previous activity, Simple Moving Averages.

* [simple_moving_averages.ipynb](Activities/04-Stu_Rolling_Statistics/Solved/simple_moving_averages.ipynb)

* [shop.csv](Activities/04-Stu_Rolling_Statistics/Resources/shop.csv)

Open the solution file and highlight the following:

* The first step to helping Harold decide if Shopify Inc. is worth a long-term investment is to load the data into a DataFrame and plot the daily closing prices.

  ![shop_rolling_stats_data](Images/shop_rolling_stats_data.png)

* The `rolling` function and the `window` parameter set the time window for the calculated metric, which in this case is the average, or mean, for 20-day, 50-day, and 100-day windows.

  ![rolling-mean-calculation](Images/rolling-mean-calculation.png)

* When overlaying the plot of daily closing prices for `SHOP` with its simple moving averages, you can see the ways in which larger rolling time windows smooth data and show general trends, as opposed to smaller rolling time windows, that showcase more volatility.

  ![sma-overlay](Images/sma-overlay.png)

* When overlaying the plot of daily closing prices for `SHOP` with its rolling standard deviations, you can see the differences in volatility for different periods.

  ![std-overlay](Images/std-overlay.png)

* Because the desire is to invest long term in Shopify, the `SMA100` and `STD100` should hold more emphasis. Based on the chart overlays, although there was a recent price uptrend earlier in 2019, long-term volatility has been high for the entirety of 2019. Therefore, it may best to hold off on investing long term in Shopify for now.

Answer any questions before moving on.

---

### 8. Instructor Do: Beta (10 min)

In this activity, students will be introduced to the concept of beta and how it is used to determine the relative *unit-driven* performance of one variable to another. For example, calculating the beta value of a stock's returns relative to the returns of the overall market.

**Files:**

* [beta.ipynb](Activities/05-Ins_Beta/Solved/beta.ipynb)

* [amzn_data.csv](Activities/05-Ins_Beta/Resources/amzn_data.csv)

* [sp500_data.csv](Activities/05-Ins_Beta/Resources/sp500_data.csv)

Open the lesson slides, move to the "Beta" section, and highlight the following:

* Before we start using beta, there are two concepts we need to review: covariance and variance.

* What is covariance?

  * **Covariance** is a measure of the directional relationship between two variables. For example, the covariance between two financial assets, such as stock returns, would imply that both stock returns would move together with a positive covariance and move inversely with a negative covariance.

* What is variance?

  * **Variance** is the measurement of how far numbers in a dataset are spread about their mean. For example, let's say Stock A has an average price of $50 but varies in price as low as $5 and as high as $90. However, Stock B averages $50 but differs in price as low as $40 and as high as $60. Stock A has a higher variance than Stock B.

* What is the difference between covariance and variance?

  * **Answer:** Variance looks at one variable, measuring the range in which that variable’s values may take. By contrast, covariance looks at the variance of two variables and studies how those two variables vary together.

    Conceptually, covariance is similar to correlation: the difference is that covariance values are usually too difficult to interpret (other than being positive or negative), whereas correlation is a standardized value (regardless of data type) that ranges from `-1` to `+1`.

* How do covariance and variance relate to beta?

  * **Beta** uses covariance and variance to calculate the relative volatility of an individual stock's returns in comparison to the volatility of the overall market's returns.

* The value of beta can be interpreted as follows:

  * `β = 1` exactly as volatile as the market
  * `β >1` more volatile than the market
  * `β < 1 > 0` less volatile than the market
  * `β = 0` uncorrelated to the market
  * `β < 0` negatively correlated to the market

* A company with a higher beta has greater risk, and also greater expected returns.

Close the lesson slides and explain to students that you will now show them how to compute beta using Python.

Open the unsolved version of the Jupyter notebook and highlight the following:

* For this demo, we will use data from the stock price of Amazon and the S&P 500 index.

* First, we load the data with the closing prices of Amazon and the S&P 500 index.

  ![beta_read_data](Images/beta_read_data.png)

* Next, we concatenate the data and calculate the daily returns using the `pct_change` function.

  ![beta_prepare_data](Images/beta_prepare_data.png)

* Since we want to compute the beta of Amazon's stock in comparison with the S&P 500 index, the first step is to calculate the variance of the S&P 500 index. We use the `var` function from Pandas.

  ![variance.png](Images/variance.png)

* Next, we calculate the covariance of Amazon returns in contrast to the S&P 500 index. We use the `cov` function from Pandas.

  ![covariance.png](Images/covariance.png)

* To compute the value of beta, we divide the covariance over the variance.

  ![beta_value](Images/beta_value.png)

* In this case, since beta is greater than `1`, we may conclude that the Amazon stock is more volatile than the market; although we may have a higher risk, we would have a return of 133% over the typical market return.

* A good practice is to plot the progression of beta values for a stock over time using rolling windows to see its historical volatility relative to the market.

  ![rolling-beta.png](Images/rolling-beta.png)

* Beta and correlation seem to be similar since both metrics contrast two variables. However, there is a difference between beta and correlation.

* Beta measures the impact of one variable on another variable. Correlations measure the possible frequency of similar directional movements without consideration for cause and effect.

* To have a better understanding of this difference, we will use the `Seaborn` library to plot the difference between beta and correlation.

  ![beta-vs-correlation.png](Images/beta-vs-correlation.png)

* Beta is the slope of the two variables. Correlation is the strength of that linear relationship.

* We can also contrast the numerical values of beta and the correlation between Amazon and the S&P 500 index.

  ![beta_vs_correlation](Images/beta_vs_correlation.png)

* Note that the beta value and the correlation do **not** match! Beta is a measure of volatility relative to the market. We would conclude that this stock is approximately 33% more volatile than the market (beta of 1.329). The correlation is an indication of the extent of the linear relationship between `AMZN` and the `S&P500`.

Ask if there are any questions before moving on.

---

### 9. BREAK (15 min)

---

### 10. Student Do: Beta Comparisons (15 min)

In this activity, students will apply their knowledge of rolling statistics and beta to plot the 30-day rolling betas of a group of stocks. The goal is to determine the most conservative stock choice or the stock with the lowest beta.

**Files:**

* [beta_comparisons.ipynb](Activities/06-Stu_Beta/Unsolved/beta_comparisons.ipynb)

* [fb_data.csv](Activities/06-Stu_Beta/Resources/fb_data.csv)

* [snap_data.csv](Activities/06-Stu_Beta/Resources/snap_data.csv)

* [sp500_data.csv](Activities/06-Stu_Beta/Resources/sp500_data.csv)

* [twtr_data.csv](Activities/06-Stu_Beta/Resources/twtr_data.csv)

**Instructions:**

* [README.md](Activities/06-Stu_Beta/README.md)

---

### 11. Instructor Do: Review Beta Comparisons (10 min)

In this section, review the solution to the previous activity, Beta Comparisons.

**Files:**

* [beta_comparisons.ipynb](Activities/06-Stu_Beta/Solved/beta_comparisons.ipynb)

* [fb_data.csv](Activities/06-Stu_Beta/Resources/fb_data.csv)

* [snap_data.csv](Activities/06-Stu_Beta/Resources/snap_data.csv)

* [sp500_data.csv](Activities/06-Stu_Beta/Resources/sp500_data.csv)

* [twtr_data.csv](Activities/06-Stu_Beta/Resources/twtr_data.csv)

Open the solved version of the Jupyter notebook, live code the solution, and explain the following:

* The first step is to read in the data from the CSV files and combine the DataFrames for each social media stock and the S&P 500 into a single DataFrame.

  ![stu_beta_data_read](Images/stu_beta_data_read.png)

* Once the data is combined, it's easier to calculate the daily returns for each stock; simply call the `pct_change` function on the combined DataFrame.

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

Answer any questions before moving on.

---

### 12. Instructor Do: Portfolio Returns (10 min)

This section focuses on calculating returns for a group of stocks, or stock portfolios. Students should understand that portfolios of stocks are used by investors to manage and diversify risk. Defining a portfolio with varying capital allocations of stocks allows an investor to control and adjust their risk.

**Files:**

* [portfolio_returns.ipynb](Activities/07-Ins_Portfolio_Returns/Solved/portfolio_returns.ipynb)

* [emb_historical.csv](Activities/07-Ins_Portfolio_Returns/Resources/emb_historical.csv)

* [imo_historical.csv](Activities/07-Ins_Portfolio_Returns/Resources/imo_historical.csv)

Open the lesson slides, move to the "Portfolio Returns" section and highlight the following:

* The purpose of a portfolio is to control the amount of risk and diversity in an investment.

* Portfolio returns can be calculated using a dot product function, which multiplies allocated weights to each stock return.

* Now, we will calculate portfolio returns using Python and all the metrics we have learned up to date.

Open the unsolved version of the Jupyter notebook to live code the solution. Cover the following points as you walk through the file:

* In this demo, we will compare the closing prices of two energy stocks listed in the S&P TSX 60 index: Enbridge Inc. (`ENB`) and Imperial Oil Limited (`IMO`).

* To calculate portfolio returns, each stock's closing prices are added as a column to the final portfolio DataFrame.

  ![portfolio-dataframe.png](Images/portfolio-dataframe.png)

* Portfolio daily returns are first calculated individually with `pct_change`. The total portfolio return is calculated using the weighted average (how much of each stock contributes to the total portfolio).

* Portfolio weights represent the percentage of allocated capital to each stock. For example, a weight of `0.5` indicates that a single stock will be allocated `50%` of the capital within the portfolio. The sum of the weights should always equal `1`.

  ![portfolio-returns.png](Images/portfolio-returns.png)

* The portfolio returns can also be calculated using a dot product, which is just a shortcut for the previous calculation. This can be handy for large portfolios with a lot of weights.

  ![dot-product.png](Images/dot-product.png)

* Annualized volatility is calculated by multiplying standard deviation by the square root of the number of trading days in a year (252 days).

  ![ins_portfolio_volatility](Images/ins_portfolio_volatility.png)

* The higher a portfolio's volatility means more risk but potentially higher returns.

* The purpose of a portfolio is to control the amount of risk and diversity in an investment. In the following example, `ENB` has more volatility than `IMO`, so changing the weights of the portfolios may affect the returns.

  * The `cumprod` function computes the cumulative returns to indicate the total return profit or loss from a percentage standpoint. Multiplying an initial investment of $10,000 by the series of cumulative returns outputs a trend over time of cumulative profit or loss.

  ![risk-management.png](Images/risk-management.png)

Ask if there are any questions before moving on.

---

### 13. Student Do: Portfolio Planner (30 min)

This activity is a two-part mini-project where you will work in pairs to research a group of 10 stocks and perform an analysis of a $10,000 investment in the portfolio over time.

**Files:**

* [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner/Unsolved/portfolio_planner_part_1.ipynb)

* [portfolio_planner_part_2.ipynb](Activities/08-Stu_Portfolio_Planner/Solved/portfolio_planner_part_2.ipynb)

* [bk_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/bk_data.csv)

* [jnj_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/jnj_data.csv)

* [mu_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/mu_data.csv)

* [sbux_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/sbux_data.csv)

* [wdc_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/wdc_data.csv)

* [fang_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/fang_data.csv)

* [luv_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/luv_data.csv)

* [nke_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/nke_data.csv)

* [t_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/t_data.csv)

* [wrk_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/wrk_data.csv)

**Instructions:**

* [README.md](Activities/08-Stu_Portfolio_Planner/README.md)

---

### 14. Instructor Do: Review Portfolio Planner (10 min)

In this section, you will review the solution to the previous activity.

**Files:**

* [portfolio_planner_part_1.ipynb](Activities/08-Stu_Portfolio_Planner/Solved/portfolio_planner_part_1.ipynb)

* [portfolio_planner_part_2.ipynb](Activities/08-Stu_Portfolio_Planner/Solved/portfolio_planner_part_2.ipynb)

* [bk_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/bk_data.csv)

* [jnj_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/jnj_data.csv)

* [mu_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/mu_data.csv)

* [sbux_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/sbux_data.csv)

* [wdc_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/wdc_data.csv)

* [fang_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/fang_data.csv)

* [luv_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/luv_data.csv)

* [nke_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/nke_data.csv)

* [t_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/t_data.csv)

* [wrk_data.csv](Activities/08-Stu_Portfolio_Planner/Resources/wrk_data.csv)

Open the solved version of the Jupyter notebook for Part 2, and conduct a dry walkthrough review, explaining in the following:

* We will start by reviewing Part 1.

* The first step in helping Harold analyze these 10 stocks is to load the data into a DataFrame for each data file.

  ![portfolio_data](Images/portfolio_data.png)

* After reading in the data, combine the data from all the DataFrames into a single DataFrame. When dealing with datetime indexes, be sure to sort the DataFrame by index in ascending order, to arrange the dates chronologically from past to present. This is particularly important when employing time-series functions such as `pct_change`.

  ![portfolio_data_combined](Images/portfolio_data_combined.png)

* Annualized volatility is calculated by multiplying standard deviation by the square root of the number of trading days in a year (252 days). Using the `sort_values` function quickly sorts each stock from least volatile to most volatile.

  ![assess-riskiness](Images/assess-riskiness.png)

* Portfolio weights represent the percentage of allocated capital to each stock. For example, a weight of `0.5` indicates that a single stock will be allocated `50%` of the capital within the portfolio. The sum of the weights should always equal `1`.

* The five stocks with the highest volatility are dropped to continue the analysis of the stocks.

  ![portfolio_drop_five](Images/portfolio_drop_five.png)

* The `dot` function multiplies the weights by the daily return of each column (four weights, four stocks) and sums the total for each row.

  ![portfolio-planner-part-1-weights](Images/portfolio-planner-part-1-weights.png)

* Cumulative returns indicate the total return profit or loss from a percentage standpoint. Multiplying an initial investment of $10,000 by the series of cumulative returns outputs a trend over time of cumulative profit or loss.

  ![portfolio-planner-cumulative-returns](Images/portfolio-planner-cumulative-returns.png)

* In Part 2, we filter the 10 stocks to just the non-correlated stocks, and stocks with positive Sharpe ratios. This is to maximize the diversification of the portfolio—and, therefore, minimize volatility—and maximize the risk-to-returns ratio of the optimized portfolio.

* We start Part 2 by re-calculating daily returns as the DataFrame was modified in Part 2.

  ![portfolio_reset_daily_returns](Images/portfolio_reset_daily_returns.png)

* Stock correlation describes the linear relationship between the returns of two stocks, and indicates whether returns of both stocks tend to move in tandem, inversely, or randomly (no correlation).

* The `corr` function used in conjunction with the `heatmap` function from the `Seaborn` library makes it easy to spot the highly correlated stocks.

  ![part-2-correlation](Images/part-2-correlation.png)

* In this case, the daily returns of `FANG` and `JNJ` appear to be highly correlated and can be dropped from the DataFrame.

  ![portfolio_drop_two](Images/portfolio_drop_two.png)

* Unlike volatility, which measures risk, Sharpe ratios describe the riskiness of stocks relative to their returns. Therefore, Sharpe ratios measure risk-to-reward and indicate value-driven investments. The `mean` and `std` functions are used to calculate the Sharpe ratios of stocks.

  ![part-2-sharpe-ratios](Images/part-2-sharpe-ratios.png)

* We drop the three stocks with a negative Sharpe ratio since it either means the risk-free rate is higher than the portfolio's return, or the portfolio's return is expected to be negative.

  ![portfolio_drop_three](Images/portfolio_drop_three.png)

* An equal-weighted portfolio consists of the same weight for every stock in the portfolio (totalling `1`). For example, an equal-weighted stock portfolio of five stocks would have weights of `0.2`, `0.2`, `0.2`, `0.2`, and `0.2` for each stock.

  ![part-2-equal-weighted](Images/part-2-equal-weighted.png)

* The overlay chart of a $10,000 investment in each corresponding portfolio over time describes the following:

  * The non-correlated, Sharpe ratio optimized portfolio performs the best of the four portfolios, consistently achieving higher returns with minimized volatility.
  
  * The original, unoptimized portfolio performs the second-best of the four portfolios; it achieves higher returns but at the expense of more volatility. Returns increased more quickly, but also fell more quickly—notice the dip in early 2019.
  
  * The non-correlated (diversified) portfolio performs the second-worst of the four portfolios; it manages to minimize volatility, but at the expense of higher returns.

  * The risk-optimized portfolio performs the worst of the four portfolios, achieving minimal volatility, but at the expense of returns.

  ![part-2-overlay](Images/part-2-overlay.png)

Remind students that mastery doesn't happen in a day. Practice makes perfect!

Answer any questions before ending the class.

---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
