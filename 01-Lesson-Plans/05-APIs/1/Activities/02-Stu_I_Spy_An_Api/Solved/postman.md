## I Spy, an API

1. Get `GOOG` stock data using `Quandl API`.

    ```
    GET https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json
    ```

    ![quandl_goog.png](../Images/quandl_goog.png)

2. Extract `GDP` data for the `US` using `World Bank API`.

    ```
    http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json
    ```

    ![world_bank_adp.png](../Images/world_bank_adp.png)

3. Identify the current `Bitcoin` price using `Coinbase API`.

    ```
    https://api.coinbase.com/v2/prices/BTC-USD/buy?format=json
    ```

    ![coin_base_btc.png](../Images/coin_base_btc.png)

4. Get `GOOG` stock data in `CSV` format using `Quandl API`. Take note of how the change in URL alters the format (json vs csv) of the data returned by the API.

    ```
    https://www.quandl.com/api/v3/datasets/WIKI/GOOG.csv
    ```

    ![quandl_goog_csv.png](../Images/quandl_goog_csv.png)
