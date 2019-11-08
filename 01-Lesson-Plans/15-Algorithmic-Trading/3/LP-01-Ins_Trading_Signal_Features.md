### 1. Instructor Do: Random Forest Trading (15 min)

In this activity, students will learn how to generate a set of trading signal derived from raw BTC/USD data that will be used as features to train a Random Forest machine learning model that will autonomously make predictions and corresponding trades.

**File:** [random_forest_trading.ipynb](Activities/01-Ins_Random_Forest_Trading/Solved/random_forest_trading.ipynb)

First, quickly introduce the following:

* Now that students have learned to generate trading signals, backtest their trading strategies, and evaluate their results, it is now time to incorporate machine learning into the mix! Students will now have the opportunity to use a machine learning model (Random Forest) to correctly predict next day positive or negative returns based off of multiple trading signals.

* The Random Forest model will require multiple features, or in this case, multiple trading signals to train itself on. Therefore, students will learn to generate multiple trading signals using various technical indicators such as an exponential moving average of closing prices, exponential moving average of daily return volatility, and Bollinger Bands, which is are a set of lines representing a (positive and negative) standard deviation away from a simple moving average (SMA) of the asset's closing price.

Then, open the solution file and discuss the following:

* As always, before proceeding to generating the multiple features or trading signals of the Random Forest model, the following will first have to be done: importing the relevant libraries, reading in the data as a Pandas DataFrame, and preparing/cleaning the data.

  ```python
  # Import libraries and dependencies
  import pandas as pd
  import numpy as np
  from pathlib import Path
  %matplotlib inline
  ```

  ```python
  # Set path to CSV and read in CSV, then set index as `Timestamp`
  csv_path = Path('../Resources/kraken_btc_1hr.csv')
  btc_df=pd.read_csv(csv_path)
  btc_df
  ```

  ```python
  btc_df.set_index(pd.to_datetime(btc_df['Timestamp'], infer_datetime_format=True), inplace=True)
  btc_df.drop(columns=['Timestamp'], inplace=True)
  btc_df
  ```

* Then, in order to calculate the exponential moving average of daily return volatility (2nd trading signal), we will of course need prepare the DataFrame by calculating the daily returns of BTC/USD closing prices. Using the `dropna` function to drop any rows with NA values is a generally good practice.

  ```python
  # Drop NAs and calculate daily percent return
  btc_df['daily_return'] = btc_df['Close'].dropna().pct_change()
  btc_df
  ```

* Now that the data is prepared, it is now time to move onto generating the multiple trading signals! Students should draw from their experiences from the previous unit 15 lessons where they generated a dual moving average crossover trading signal, as the process is similar.

* In contrast to a simple moving average (SMA), an exponential moving average (EMA) represents a moving average with more weight or focus given to the most recent of prices. Therefore, a short window EMA describes "faster" price action than its long window EMA or "slower" counterpart. The logic then dictates such that when the fast EMA is greater than the slow EMA, a long trade opportunity exists, as price action should rise in the short-term, while a short trade opportunity arises for the opposite scenario in which the slow EMA is greater than the fast EMA.

  * Students should be aware that these trading signals will incorporate a long, short, or hold strategy (rather than just long or hold, or short or hold), which is why the `crossover_signal` is calculated as the result of adding both the `crossover_long` and `crossover_short` signals together.

    ```python
    btc_df['crossover_signal'] = btc_df['crossover_long'] + btc_df['crossover_short']
    ```

    ![ema](Images/ema.png)

    ![ema-plot](Images/ema-plot.png)

* Similarly, an exponential moving average of daily return volatility gives more weight to the most recent of daily returns. Therefore, when a short window EMA or fast EMA of daily return volatility is greater than a long window or slow EMA of daily return volatility, the crossover suggests that a short opportunity exists where daily return volatility is expected to rise. This is because during times of rising price volatility, there often exists a negative price bias (selling) and vice versa for when daily return volatility is expected to fall (buying).

  ![ema-std](Images/ema-std.png)

  ![ema-std-plot](Images/ema-std-plot.png)

* Lastly, a Bollinger Band describes a middle, upper, and lower band, in which the middle is a simple moving average (SMA) of closing prices, while the upper and lower bands describe the rolling standard deviation above and below the SMA, respectively. Therefore, when the asset closing price is less than the lower band, a long opportunity exists as the signal suggests that the price action will tend to move upwards and more in line with where the price *should* be (within the negative standard deviation). A short opportunity exists for the opposite scenario in which the asset closing price is greater than the upper band, suggesting that the price action will tend to move lower and within the positive standard deviation.

  ![bollinger-band.png](Images/bollinger-band.png)

  ![bollinger-band-plot.png](Images/bollinger-band-plot.png)

At the end of the discussion, ask students whether or not they understand what the trading signals are suggesting. This is important as these trading signals will end up training the Random Forest model, therefore it is crucial for them to understanding the basis upon which the model will be trained.
