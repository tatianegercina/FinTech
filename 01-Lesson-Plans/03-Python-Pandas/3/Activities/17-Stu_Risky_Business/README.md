# Risky Business

Harold has been participating in some risky business. He recently became seriously involved in the cryptocurrency market and has seen some good returns. Harold's recent returns has him strutting around the office like he's the best trader. He even had the audacity to bet you $5 that his portfolio returns are better than yours.

Using standard deviation and sharpe ratios, do the following:

* Identify which cryptos have the greatest risk-to-reward ratio.

* Determine which portfolio (yours or Harold's) has made the most smart investments.

* Identify which cryptocurrencies have the greatest Sharpe ratios (risk/reward).

## Instructions

Using the [starter file](Unsolved/Core/risky_business.ipynb) and the data in the [Resources](Resources) folder, complete the following steps:

1. Load CSV data into Pandas using `read_csv` for each file and remove any null values using `dropna`.

2. Calculate daily returns for each portfolio.

3. Concat both DataFrames containing daily returns into one DataFrame.

4. Calculate standard deviation for the combined DataFrame.

5. Calculate the Sharpe ratios by computing the quotient of `annualized average return` and `annualized standard deviation`.

6. Plot the Sharpe ratios using a bar chart.

7. Answer the following questions:

    * How many smart investments did Harold make compared to risky investments? How many did you make?

    * Which cryptos have been the smartest investments?

### Challenge

Calculate the Sharpe ratio for your entire portfolio. Then, use a comparison operator to see which portfolio has the greatest risk-to-reward ratio.

1. Calculate annualized `std dev` for each portfolio.

2. Calculate the Sharpe ratio for each crypto in each portfolio.

3. Average the Sharpe ratios calculated above.

  **Hint:** `harold_sharpe_ratios.mean()`

4. Determine if Harold's portfolio's Sharpe ratio average is greater than your own. **Hint:** Use a comparison operator to compare Sharpe ratio averages.

5. Determine which portfolio is the smartest investment, based on risk-to-reward ratio.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
