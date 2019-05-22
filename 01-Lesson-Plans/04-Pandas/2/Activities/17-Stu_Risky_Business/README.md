## Risky Business!

Harold's been participating in some risky business. He recently got seriously involved in the cryptocurrency market and has seen some good returns. Harold's recent returns has him strutting around the office like he's the best trader. He even had the audacity to bet you five dollars that his portfolio returns are better than yours.

Using `standard deviation` and `sharpe ratios`, identify which cryptos have the greatest risk/reward ratio. Then, determine which portfolio (yours or Harold's) has made the most smart investments. Also identify which cryptocurrencies have the greatest `sharpe ratios` (risk/reward).

## Instructions

Using the [starter-file](Unsolved/Core/risky_business.ipynb) provided, and the data provided in the `Resources` folder, complete the following steps:

1. Load CSV data into Pandas using `read_csv` for each file.

2. Calculate `daily returns` for each portfolio.

3. Concat both DataFrames containing daily returns into one DataFrame.

4. Calculate `std dev` for combined DataFrame.

5. Calculate `sharpe ratio` by computing the quotient of `annualized average return` and `annualized standard deviation`.

6. Plot `sharpe ratios` using a bar chart.

7. How many smart investments did Harold make compared to risky investments? How many did you make?

8. Which cryptos have been the smartest investment?

### Challenge

Calculate the sharpe ratio for your entire portfolio rather than for each crypto. Then, use a comparison operator to see which portfolio has the greatest risk to reward ratio.

1. Calculate `std dev` for the entirety of each portfolio.

2. Compare Harold's portfolio's `std dev` with your own.

3. Calculate `sharpe ratio` for each portfolio.

4. Compare Harold's portfolio's sharpe ratio with your own to determine if his is greater.

5. Which portfolio is the smartest investment, based off of risk to reward ratio?
