### 18. Students Do: Cryptocurrencies Price Analysis (20 mins)

In this activity, students will use historical cryptocurrency data for 5 cryptocurrencies and track returns over time. The objective of the assignment is for the students to learn how to marry the skills they learned throughout the day: reading in CSVs, cleaning data, calculating returns, and visualizing financial data. Students will ultimately create a chart that pinpoints trends in cryptocurrency market performance across one year and two year intervals.

Encourage students to work with a partner on this activity.

**Files:**

* [blast_from_the_past.ipynb](Activities/19-Stu_Cryptocurrencies/Unsolved/blast_from_the_past.ipynb)

**Instructions:**

* [README.md](Activities/19-Stu_Cryptocurrencies/README.md)

### 19. Instructor Do: Review Cryptocurrencies (5 mins)

**Files:**

* [blast_from_the_past.ipynb](Activities/19-Stu_Cryptocurrencies/Solved/blast_from_the_past.ipynb)

Walkthrough the solution and go over the following discussion points:

* Before using data, data will need to be assessed for quality issues, and then cleaned.

  ```python
  crypto_data.isnull().mean() * 100
  crypto_data.isnull().sum()
  crypto_data = crypto_data.dropna()
  crypto_data['data_date'] = pd.to_datetime(crypto_data['data_date'], infer_datetime_format=False).dt.date
  ```

* The `read_csv` function does not require an index to be specified upon reading of the file. There are instances where an index cannot be specified until after data has been cleaned and wrangled.

  ```python
  # Cast data_date to Date
  crypto_data['data_date'] = pd.to_datetime(crypto_data['data_date'], infer_datetime_format=False).dt.date

  # Set index using `data_date`
  crypto_data.set_index(crypto_data['data_date'], inplace=True)
  ```

  ![LP_Stu_Crypto_SetIndexClean.png](Images/LP_Stu_Crypto_SetIndexClean.png)

* The data for each crypto is eventually sliced and then stored into another DataFrame. A subset of a DataFrame's data can be sliced and stored as its own DataFrame. Taking a slice of a data enables analysis to be performed solely on that subset of the data. Once the subsets have been transformed as needed, they can be merged or joined with other DataFrames or plotted in one chart.

  ```python
  # Slice data into subsets for each crypto
  bitcoin_daily_subset = crypto_data[crypto_data['cryptocurrency'] == 'bitcoin']
  ethereum_daily_subset = crypto_data[crypto_data['cryptocurrency'] == 'ethereum']
  bitcoin_cash_daily_subset = crypto_data[crypto_data['cryptocurrency'] == 'bitcoin-cash']
  ripple_daily_subset = crypto_data[crypto_data['cryptocurrency'] == 'ripple']
  litecoin_daily_subset = crypto_data[crypto_data['cryptocurrency'] == 'litecoin']
  ```

* Once the data is sliced, daily returns can be calculated for each respective crypto using the `pct_change` function. The `pct_change` function will compare each record's `data_priceUsd` value with the value of the previous row. If there is no row to compare to, a null/NaN value will be returned.

  ```python
  # Execute pct_change function
  bitcoin_daily_returns = bitcoin_daily_subset.pct_change()
  ethereum_daily_returns = ethereum_daily_subset.pct_change()
  bitcoin_cash_daily_returns = bitcoin_cash_daily_subset.pct_change()
  ripple_daily_returns = ripple_daily_subset.pct_change()
  litecoin_daily_returns = litecoin_daily_subset.pct_change()
  ```

  ![LP_Stu_Crypto_Calculate_Returns.png](Images/LP_Stu_Crypto_Calculate_Returns.png)

* A plot can be built using more than one DataFrame. In order to do so, the first plot created must be passed to each subsequent plot as an `ax` (axes) object.

  ```python
  # Plot 5 returns DataFrames in same chart
  crypto_portfolio_returns = bitcoin_daily_returns.plot()
  ethereum_daily_returns.plot(ax=crypto_portfolio_returns)
  bitcoin_cash_daily_returns.plot(ax=crypto_portfolio_returns)
  ripple_daily_returns.plot(ax=crypto_portfolio_returns)
  litecoin_daily_returns.plot(ax=crypto_portfolio_returns)
  crypto_portfolio_returns.legend(["bitcoin", "ethereum", "bitcoin-cash","ripple","litecoin"]);
  ```

  ![LP_Stu_Crypto_MultiDFPlot.png](Images/LP_Stu_Crypto_MultiDFPlot.png)

* Plot legends can be configured using the `legend` function. The function accepts a list of strings to use as the legend labels. The `legend` function is used to ensure the plot legend is intuitive and within context.

  ```python
  crypto_portfolio_returns.legend(["bitcoin", "ethereum", "bitcoin-cash","ripple","litecoin"])
  ```

  ![LP_Stu_Crypto_Legend.png](Images/LP_Stu_Crypto_Legend.png)

### 20. Decompress

Before ending class, leave some encouraging remarks, and give students a space to vocalize their thoughts.

* Give students positive feedback; ensure them that they are all doing great. Not only have they learned Python, but now they've learned Pandas and have begun automating portfolio performance evaluation. They're one step closer to their goal of being masters of FinTech automation.

* Ask students the following questions:

  * What activity was the most enjoyable to complete The most fulfilling?

  * What's the most stressful thing about programming?

  * What took you the most time to figure out?

  * Did you come across any shortcuts or unique ways to do things while completing the activities?

* Underscore that the students have been doing excellent at learning both financial and technical concepts. This is not an
easy feat. It takes skill, intellect and abstract thinking, and perseverance to make it this far. They should all pat themselves on the back.

* Underscore that the students have come a long way. Last week they learend Python. Now they're integrating Pandas and Matplotlib into their Python programs. Next they'll start using more advanced Financial calculations and functions, and eventually move onto working with APIs.

* Let the students know that office hours are available for anyone who might have additional questions; would like to review more; or would like to just talk Python, Pandas, Financial Portfolios, and/or FinTech!

### End Class
