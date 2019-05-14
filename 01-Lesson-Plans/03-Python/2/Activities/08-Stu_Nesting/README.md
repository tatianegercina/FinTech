# Weekly Gains

In this activity, the stock markets have already been closed since 4 PM and the time is slowly creeping by to 5 PM on a Friday. Unfortunately, as his job entails, Harold needs to close out another week of gathering stock data so as to calculate a report of the weekly gains of his list of stocks.

Usually Harold performs this task by manually looking up the stock price records for the new day, adding them to his weekly list of stocks, and then running his calculations; however, he now wonders if there is an easier (and quicker) way to do all of this so that he can go home earlier on Fridays.

Help Harold by creating a program to automate his data gathering process, and even better, his weekly gain calculations.

## Instructions

Using the [starter-file](Unsolved/Core/weekly_gains.py) provided, walk through the following steps:

  * Use the `new_records` dictionary to add each new stock ticker record to the corresponding list of records in the `historical_stock_data` dictionary. Appended stock ticker records will need to be in the following format: `[date, open, high, low, close]`.

  * You have two choices to do so:

    1. Create a list object for each new stock ticker record in the `new_records` dictionary in the above sequence and manually append each list to the corresponding list of stock ticker records in the `historical_stock_data` dictionary.

    2. Loop through the `new_records` dictionary and append a new stock ticker record to each corresponding ticker in the `historical_stock_data` dictionary.

  * Print out the modified `historical_stock_data` dictionary.

    ```python
    # Print out the modified 'historical_stock_data' dictionary
    print(historical_stock_data)
    ```

    ```
    {'AAPL': [['04-17-2019', 199.54, 203.38, 198.61, 203.13], ['04-18-2019', 199.46, 201.37, 198.56, 199.25], ['04-19-2019', 198.58, 199.85, 198.01, 199.23], ['04-20-2019', 199.2, 200.14, 196.21, 198.87], [['04-21-2019', 200.85, 201.0, 198.44, 198.95]], ['04-21-2019', 200.85, 201.0, 198.44, 198.95]], 'MU': [['04-17-2019', 43.2, 43.53, 42.79, 43.4], ['04-18-2019', 43.36, 44.05, 42.76, 43.15], ['04-19-2019', 42.26, 42.93, 42.08, 42.76], ['04-20-2019', 42.17, 42.23, 41.2, 41.82], [['04-21-2019', 42.85, 43.2, 41.81, 42.01]], ['04-21-2019', 42.85, 43.2, 41.81, 42.01]], 'AMD': [['04-17-2019', 27.6, 27.88, 27.34, 27.68], ['04-18-2019', 28.21, 28.27, 27.22, 27.49], ['04-19-2019', 27.72, 28.18, 27.49, 27.93], ['04-20-2019', 27.8, 27.84, 26.96, 27.33], [['04-21-2019', 28.21, 28.38, 27.66, 27.85]], ['04-21-2019', 28.21, 28.38, 27.66, 27.85]], 'TWTR': [['04-17-2019', 34.67, 34.86, 34.32, 34.4], ['04-18-2019', 34.73, 34.9, 34.2, 34.48], ['04-19-2019', 34.84, 34.99, 34.23, 34.46], ['04-20-2019', 34.38, 35.03, 34.34, 34.71], [['04-21-2019', 34.67, 34.83, 34.11, 34.37]], ['04-21-2019', 34.67, 34.83, 34.11, 34.37]]}
    ```

## Challenge

Calculate the weekly gains for each stock ticker and assign to a `results` dictionary for each stock ticker.

  * Loop through every key-value pair in the `historical_stock_data` dictionary

  * Set the last and first record closing prices: `ending_weekly_close` and `beginning_weekly_close`

  * Calculate the `ticker_weekly_close = ending_week_close - beginning_week_close) / beginning_week_close * 100`. Round to the nearest 2 decimal places.

  * Set the `ticker_weekly_close` to the corresponding ticker in the `results` dictionary.

## Hints

Your results should look similar to the following:

  ```
  {'AAPL': -2.06, 'MU': -3.2, 'AMD': 0.61, 'TWTR': -0.09}
  ```
