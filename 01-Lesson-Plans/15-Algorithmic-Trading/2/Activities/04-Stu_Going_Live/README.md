# Going Live with CCXT

Now that you have access to the Kraken cryptocurrency exchange, modify your algorithmic trading framework to read in historical pricing data from Kraken rather than a local CSV file; select the daily historical closing prices of BTC/USD.

## Instructions

Using the [starter file](Unsolved/ninja_trader_v2.py), complete the following steps:

1. Import the ccxt and os libraries.

2. Identify the `fetch_data` function as the framework component that will need to be modified.

3. Replace the underlying read CSV functionality for the `fetch_data` function with the ability to read historical pricing data from Kraken.

    1. Import your Kraken environment variables and set up the credentials for the Kraken class of the ccxt library.

    2. Fetch daily candlestick bar data from `BTC/USD` using the `fetch_ohlcv` function of the ccxt library.

    3. Import the data as a Pandas DataFrame and set the columns to 'timestamp', 'open', 'high', 'low', 'close', 'volume'.

    4. Create a new 'date' column by converting the epoch timestamp to a date using the `to_datetime` function and `unit` parameter.

    5. Set the BTC/USD historical prices DataFrame as the return object of the `fetch_data` function.

## Challenge

1. Modify the `share_size` variable of the `execute_backtest` function to calculate the available share size based on the initial capital divided by the first closing price of BTC/USD, rounded down to the nearest integer.

## Hint

Make sure that while you are modifying the underlying code for the `fetch_data` function, you are not disrupting the high-level input/output workflow of the trading framework.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.