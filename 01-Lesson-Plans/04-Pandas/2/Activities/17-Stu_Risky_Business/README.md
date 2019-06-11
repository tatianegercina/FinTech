# Risky Business

Harold's been participating in some risky business. He recently became seriously involved in the cryptocurrency market and has seen some good returns. Harold's recent returns has him strutting around the office like he's the best trader. He even had the audacity to bet you $5 that his portfolio returns are better than yours.

Using standard deviation and sharpe ratios, identify which cryptos have the greatest risk/reward ratio. Then, determine which portfolio (yours or Harold's) has made the most smart investments. Also identify which cryptocurrencies have the greatest sharpe ratios (risk/reward).

## Instructions

Using the [starter file](Unsolved/Core/risky_business.ipynb) and the data in the Resources folder, complete the following steps:

1. Load CSV data into Pandas using `read_csv` for each file.

2. Calculate `daily returns` for each portfolio.

3. Concat both DataFrames containing daily returns into one DataFrame.

4. Calculate `std dev` for combined DataFrame.

5. Calculate sharpe ratio by computing the quotient of `annualized average return` and `annualized standard deviation`.

6. Plot the sharpe ratios using a bar chart.

7. Answer the following questions:

    * How many smart investments did Harold make compared to risky investments? How many did you make?

    * Which cryptos have been the smartest investments?

### Challenge

Calculate the sharpe ratio for your entire portfolio rather than for each crypto. Then, use a comparison operator to see which portfolio has the greatest risk-to-reward ratio.

1. Calculate annualized `std dev` for each portfolio.

2. Calculate the sharpe ratio for each crypto in each respective portfolio.

3. Average the sharpe ratios calculated above.

    Hint: `harold_sharpe_ratios.mean()`

4. Determine if Harold's portfolio's sharpe ratio average is greater than your own by using a comparison operator to compare sharpe ratio averages.

5. Determine which portfolio is the smartest investment, based on risk-to-reward ratio.

- - -

© 2019 Trilogy Education Services
