# Group Dynamics

The cryptocurrency market has experienced yet another wave of activity. Everyone's talking about Bitcoin and Ethereum. Close friends and family are bombarding you with questions, requests for information, and investing advice. However, it's been two years since you last looked at your holdings on Binance, and your knowledge of current-day crypto trends is lacking.

It's time you brushed up on the price dynamics of each crypto. Conduct a price analysis for Bitcoin, Ethereum, Bitcoin Cash, Ripple, and Litecoin to assess average, high, and low prices for each cryptocurrency. Determine whether or not crypto performance in the past two years warrants future investment.

## Instructions

Using the [starter file](Unsolved/group_dynamics.ipynb) and the historical stock [data](Resources/crypto_data.csv), complete the following steps:

1. Load CSV data into Pandas using `read_csv`.

2. Assign the index as series `data_date`. Be sure to provide the `parse_dates` and `infer_datetime_format` arguments.

3. Clean missing values. Drop columns `data_time` and `timestamp`.

4. Plot grouped data on the same chart and return `data_priceUsd`.

5. Calculate `average` price across two years for each `cryptocurrency`.

6. Calculate `max` price across two years for each `cryptocurrency`.

7. Calculate `min` price across two years for each `cryptocurrency`.

8. Answer the following questions:

    * Which coin would you recommend investing in?

    * Which coin had the largest swing in prices?

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
