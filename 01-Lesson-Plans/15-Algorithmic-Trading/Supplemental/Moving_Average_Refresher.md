
<H1>Moving Average Refresher</H1>
<details>
<summary>Simple Moving Average (SMA):</summary>
<hr>

In a simple moving average, the mean is calculated on a specified number of data points to the get the trend line.  Short-term and long-term moving averages are simply moving averages with a shorter and longer time window respectively.  For example, in the following sample data, we would get the simple moving average of a time period of 5 by calculating the mean of every 5 values, moving down 1 with each calculation:

![simple_ma_gif](Images/simple_ma_gif.gif)
</details>
<br>
<details>
<summary>Exponentially Weighted Moving Average (EWMA):</summary>
<hr>

EWMA is a moving average technique that applies more weight to recent data. To obtain the EWMA with pandas, the `.ewm()` function is called. The weight you wish to apply is supplied with the `halflife` parameter.  The `halflife` is how long it takes a weight to reach half of its original weight. Using this method, the lower the `halflife` the move weight is placed on the most recent time periods.  Half life can be visualized as follows:
![ewma_gif](Images/ewma_gif.gif)

The column is added to a sample DataFrame using the function below:
```python
df['ewma']=df['value'].ewm(halflife=3).mean()
```
![ewma_df](Images/ewma_df.PNG)

</details>
