### 4. Instructor Do: Going Live with CCXT (5 min)

In this section, students will become familiar with the expansive CCXT library which abstracts upon a collection of available cryptocurrency exchange APIs and provides unified functions to simplify API calls when switching from different cryptocurrency exchange APIs. In particular, students will work with the Kraken API and extract both historical and current price data.

**File:** [ccxt.ipynb](Activities/03-Ins_Going_Live/Solved/ccxt.ipynb)

Open the solution file and review the following:

* Because CCXT is a collection of multiple APIs under the hood, when choosing to connect to a particular exchange such as Kraken, the credentials for that particular exchange must be set. In this case, the public and private keys for the Kraken API are imported from the `KRAKEN_PUBLIC_KEY` and `KRAKEN_SECRET_KEY` environment variables and set to the `kraken` class of the CCXT library.

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

* In most cases, CCXT requires that a user must load the list available markets and trading symbols prior to accessing other API functions for an exchange. This can be set either explicitly or automatically by CCXT when it detects that a user has not initiated the `load_markets` function when the first unified API call is made.

  ![kraken-cryptos](Images/kraken-cryptos.png)

* After loading the market data for the Kraken exchange and importing the data as a Pandas DataFrame, a quick print of the column values shows that there are (as of this writing) 110 available cryptocurrencies for trading on the Kraken exchange.

  ![kraken-crypto-symbols](Images/kraken-crypto-symbols.png)

* The `fetch_ohlcv` function can be used to fetch the candlestick bar data for `BTC/USD`, which returns a list of lists containing records with `timestamp`, `open`, `high`, `low`, `close`, and `volume` data points. As a result, when importing data into a Pandas DataFrame, column names will need to be specified according to the structure dictated by the CCXT documentation.

  ![kraken-btc-usd-historical-prices](Images/kraken-btc-usd-historical-prices.png)

  ![ohlcv-structure](Images/ohlcv-structure.png)

Answer any questions before moving on.
