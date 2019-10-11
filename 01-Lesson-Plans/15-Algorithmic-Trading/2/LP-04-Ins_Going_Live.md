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

* The `fetch_ohlcv` function can be used to fetch the candlestick bar data for `BTC/USD`, which returns a list of lists containing records with `timestamp`, `open`, `high`, `low`, `close`, and `volume` data points. As a result of the lack of key-value pairs, when importing data into a Pandas DataFrame, column names will need to be specified according to the structure dictated by the CCXT documentation.

  ![kraken-btc-usd-historical-prices](Images/kraken-btc-usd-historical-prices.png)

  ```python
  [
    [
        1504541580000, // UTC timestamp in milliseconds, integer
        4235.4,        // (O)pen price, float
        4240.6,        // (H)ighest price, float
        4230.0,        // (L)owest price, float
        4230.7,        // (C)losing price, float
        37.72941911    // (V)olume (in terms of the base currency), float
    ],
    ...
  ]
  ```

* The `timestamp` data from the `fetch_ohlcv` function is returned in *Epoch time* or *Unix time* format, which is the number of seconds (or in this case milliseconds) since the origin point in time known as the *Unix epoch*. Therefore, in order to convert epoch timestamps to a readable date format, the `to_datetime` function with the `unit` parameter should be used.

  ![convert-epoch-timestamp-ms](Images/convert-epoch-timestamp-ms.png)

* In order to fetch the latest pricing data for `BTC/USD`, the `fetch_ticker` function should be used. Make sure to drop the `info` column as the subsequent import to a Pandas DataFrame will produce multiple records due to the nested object nature of the `info` column, and in this case only one record is desired.

  ![kraken-btc-usd-current-price](Images/kraken-btc-usd-current-price.png)

  ```python
  {
    'symbol':        string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
    'info':        { the original non-modified unparsed reply from exchange API },
    'timestamp':     int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
    'datetime':      ISO8601 datetime string with milliseconds
    'high':          float, // highest price
    'low':           float, // lowest price
    'bid':           float, // current best bid (buy) price
    'bidVolume':     float, // current best bid (buy) amount (may be missing or undefined)
    'ask':           float, // current best ask (sell) price
    'askVolume':     float, // current best ask (sell) amount (may be missing or undefined)
    'vwap':          float, // volume weighed average price
    'open':          float, // opening price
    'close':         float, // price of last trade (closing price for current period)
    'last':          float, // same as `close`, duplicated for convenience
    'previousClose': float, // closing price for the previous period
    'change':        float, // absolute change, `last - open`
    'percentage':    float, // relative change, `(change/open) * 100`
    'average':       float, // average price, `(last + open) / 2`
    'baseVolume':    float, // volume of base currency traded for last 24 hours
    'quoteVolume':   float, // volume of quote currency traded for last 24 hours
  }
  ```

* To view the list of available functions for an exchange, display the results of the `has` instance variable from the current exchange object. Functions are indicated as available based on a Boolean such as True or False.

  ![exchange-has](Images/exchange-has.png)

* While today's lesson only focuses on fetching pricing data from the Kraken API, the CCXT library also allows a user to perform tasks such as checking account balances/status, fetching any open orders, or even placing and executing trades.

  **Note:** The following functions return minimal/empty datasets due to the fact that the Kraken account used in this lesson is not funded with capital.

  ![additional-functions](additional-functions.png)

Answer any questions before moving on.
