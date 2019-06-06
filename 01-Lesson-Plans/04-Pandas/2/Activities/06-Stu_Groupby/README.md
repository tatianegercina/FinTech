# Crypto Circus!

The cryptocurrency market has experienced yet another wave of activity. Everyone's talking about Bitcoin and Ethereum. Close friends and family are bombarding you with questions, requests for information, and advice regarding investing. You even overheard an older couple talking about DOGE coin. It's been quite the circus. However, it's been two years since you last looked at your holdings on Binance, and your knowledge of trends is lacking.

Conduct a price analysis to assess average, high, and low prices for each cryptocurrency. Determine whether or not crypto performance in the past two years has warranted future investment. Analyze data for Bitcoin, Ethereum, Bitcoin Cash, Ripple, and Litecoin.

## Instructions

Using the [starter file](Unsolved/crypto_circus.ipynb) and the NASDAQ historical stock [data](Resources/crypto_data.csv), complete the following steps:

1. Load CSV data into Pandas using `read_csv`. 

2. Assign the index as Series `data_date`. Be sure to provide the `parse_dates` and `infer_datetime_format` arguments.

3. Clean missing values. Drop columns `data_time` and `timestamp`.

4. Plot grouped data on the same chart and return `data_priceUsd`.

5. Calculate `average` price across two years for each `cryptocurrency`.

6. Calculate `max` price across two years for each `cryptocurrency`.

7. Calculate `min` price across two years for each `cryptocurrency`.

8. Answer the following questions: 

    * Which coin would you recommend investing in?

    * Which coin had the largest swing in prices?

- - - 
© 2019 Trilogy Education Services
