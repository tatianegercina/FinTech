### 13. Instructor Do: Trading Dashboard Deployment

In this section, students will become familiar with the expansive CCXT library, which provides an API for over 120 cryptocurrency exchanges. In particular, students will work with the Kraken API and extract both historical and current price data.

**File:** [ccxt_demo.ipynb](Activities/03-Ins_Going_Live/Solved/ccxt_demo.ipynb)

Open the solution file and review the following:

* CCXT provides a common API for over 120 cryptocurrency exchanges.

* To use a specific exchange, the API keys for that exchange must be set. In this example, the Kraken exchange is used and requires those keys to be exported before running the notebook.

  ```python
  # Import environment variables
  kraken_public_key = os.getenv('KRAKEN_PUBLIC_KEY')
  kraken_secret_key = os.getenv('KRAKEN_SECRET_KEY')
  ```

  ```python
  # Set the public and private keys for the API
  exchange = ccxt.kraken({
    'apiKey': kraken_public_key,
    'secret': kraken_secret_key,
  })
  ```

* The Kraken exchange requires a list of markets and trading symbols to be loaded to use the API functions. This can be done manually using the `load_markets` function or implicitly upon the first call to the API.

  ![kraken-cryptos](Images/kraken-cryptos.png)

* The columns of the DataFrame show the symbols available for trading on the Kraken exchange.

  ![kraken-crypto-symbols](Images/kraken-crypto-symbols.png)

* To view the list of available functions for an exchange, display the results of the `has` instance variable from the current exchange object. Functions are indicated as available based on a Boolean such as True or False.

  ![exchange-has](Images/exchange-has.png)

* The `fetch_ohlcv` function can be used to fetch the candlestick data (open, high, low, close, and volume prices) for `BTC/USD`.

  ```python
  historical_prices = exchange.fetch_ohlcv("BTC/USD", "1d")
  ```

* When loading this OHLC data into a Pandas DataFrame, the columns will also need to be specified.

  ![kraken-btc-usd-historical-prices](Images/kraken-btc-usd-historical-prices.png)

* CCXT provides all timestamps in milliseconds. This can be converted to a DatetimeIndex in Pandas using the `to_datetime` function.

  ```python
  historical_prices_df["date"] = pd.to_datetime(
      historical_prices_df["timestamp"], unit="ms"
  )
  ```

Take a moment to explain the differences in evaluating a trading strategy and going live with a strategy. Highlight the following points:

* Evaluating a trading strategy often requires backtesting the strategy using historical data and evaluating the strategy based on the performance of the model on historical prices.

* Once the strategy has been validated, the algorithm can be executed in a live trading environment. In this live trading environment, it is common to only fetch the prices at the minimal interval required to make a decision. Evaluation metrics and performance can then be updated with each incremental new data point.

* CCXT provides methods to fetch current prices and statistics for individual currencies. This current data can be used to make a trading decision in a live algorithmic trading environment.

* In this example, the `fetch_ticker` function is used to retrieve the latest pricing data for `BTC/USD`.

  ```python
  current_price = exchange.fetch_ticker('BTC/USD')
  ```

* The `info` column contains the original exchange API data that usually just be treated as duplicate information and deleted.

  ```python
  del current_price['info']
  ```

Explain that while today's lesson only focuses on fetching pricing data from the Kraken API, the CCXT library also allows a user to perform tasks such as checking account balances/status, fetching any open orders, or even placing and executing trades.

  **Note:** The following functions return minimal/empty datasets due to the fact that the Kraken account used in this lesson is not funded with capital.

  ![additional-functions](Images/additional-functions.png)

Answer any remaining questions before moving on.
