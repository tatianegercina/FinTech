* In this case, in order to activate the shorting feature of the trading model, it is necessary to replace the predicted values from 0 to -1. This is because in the following line for calculating cumulative returns of the trading model, the predicted value needs to be a negative number when multiplying against a negative daily return to produce a positive result. Otherwise, predicted values being just 0 or 1 would employ a long-hold strategy rather than the long-short-hold strategy desired.

  ![replace-predicted-values](Images/replace-predicted-values.png)

  ```python
  # Calculate cumulative return of model and plot the result
  (1 + (results['Return'] * results['Predicted Value'])).cumprod().plot()
  ```

* Calculating the cumulative returns of the model by multiplying the daily returns (actual results) against the predicted values shows that the model would have unfortunately lost money from 09-15-2019 to 09-25-2019 trading on BTC/USD hourly prices. This is to be expected, however, as the process for training and using a trading model can be straightforward, but the ability to create a sophisticated trading model that outperforms markets is not--otherwise, there would be no more finance jobs as machines would run the markets!

  ![Images/model-cumulative-returns-plot.png](Images/model-cumulative-returns-plot.png)

* Finally, backtesting the performance of the trading model by multiplying its cumulative returns against an initial capital allocation of $100,000 merely serves to visualize its performance in terms of capital.

  ![model-cumulative-returns-plot-backtest](Images/model-cumulative-returns-plot-backtest.png)
