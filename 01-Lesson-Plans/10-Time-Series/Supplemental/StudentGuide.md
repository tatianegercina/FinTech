# Unit 10: Time Series

## FAQs

<details>
<summary>What's the point of using `datetime` objects?</summary>

Humans look dates and instantly know how to categorize them - day, month, year, etc.  Your code look at dates see just another line of text, and will interpret that text as `strings`.  This can make cleaning, prepping and plotting data very difficult.  That's where time series functionality comes into play.  Casting your date `strings` to `datetime` type translates them for your code, allowing the code to interpret and categorize dates the same way you do.  For example, let's plot some Jeopardy data from the last 35 seasons.  In the following example, the data is read in via `.read_csv()`, but the dates are read in as `strings` by default.  You can see the dates are not categorized, but rather they are plotted in the order they appear in the data:

<img src='Images/str_plot.png' width=400><br>

In the next example, the dates are parsed and converted to `datetime` objects.  The dates are now being categorized properly and are listed in the correct order automatically:

<img src='Images/datetime_plot.png' width=400><br>
</details>
<details><summary>How do you convert objects to `datetime`?</summary>
Converting objects to `datetime` can be tricky.  If using pandas, its best to handle the conversion upon reading in of data.  The syntax to handle the conversion from `read_csv()` is:

```python
df = pd.read_csv('jeopardy.csv', parse_dates=True)
```
This converts each object to a `datetime` object.  Alternatively, you can also set the index as the date column for ease of plotting:
```python
df = pd.read_csv('jeopardy.csv', infer_datetime_format=True, parse_dates=True, index_col='air_date)
```
</details>
<details><summary>
How do you access `datetime` objects?</summary>

There are numerous ways to access `datetime` objects.  One of the benefits of using these data types is the added functionality they provide for analyzing data, not just with plotting but with cleaning and aggregating.  Using our Jeopardy example, we can access different episodes using different date calls:

<blockquote>
<details>
<summary>To access rows by a particular year:</summary>

![year_df](Images/year_df.png)
</details>
<details>
<summary>To access rows by a particular year and month:</summary>

![year_month_df](Images/year_month_df.png)
</details>

<details>
<summary>To access rows by a particular year, month, and day:</summary>

![year_month_day_df](Images/year_month_day_df.png)
</details>
<details>
<summary>To access a range of dates by year:</summary>

![year_month_day_df](Images/range_year_df.png)
</details>
<details>
<summary>To access a range of dates by year and month:</summary>

![year_month_day_df](Images/range_year_month_df.png)
</details>
<details>
<summary>To access a range of dates by year, month and day:</summary>

![year_month_day_df](Images/range_year_month_day_df.png)
</details>
</blockquote>

</details>

<details><summary>
How do you group time series data?</summary>
Grouping time series data is important for plotting and analysis.  The `.resample()` method allows grouping by multiple categories.  Similar to the `.groupby()` function, an aggregation method must be used to show the grouped data.  For example, we can group the mean Jeopardy point values by year using the following code:

<img src= Images/resample_Y_df.png width=325><br>

The data can then be plotted:

<img src= Images/resample_Y_plot.png width=425><br>

The following is a non-exhaustive list of many `.resample()` frequency aliases:

| Alias       | Frequency Description                   |
|-------------|-----------------------------------------|
| `D`         | Calendar day                            |
| `W`         | Weekly                                  |
| `M`         | Month end                               |
| `SM`        | Semi-month end  (15th & month end)      |
| `BM`        | Business month end                      |
| `MS`        | Month start                             |
| `SMS`       | Semi-month start  (1st and 15th)        |
| `BMS`       | Business month start                    |
| `Q`         | Quarter end                             |
| `BQ`        | Business quarter end                    |
| `QS`        | Quarter start                           |
| `BQS`       | Business quarter start                  |
| `A`         | Year end                                |
| `BA`, `BY`  | Business year end                       |
| `AS`, `YS`  | Year start                              |
| `BAS`, `BYS`| Business year start                     |
| `BH`        | Business hour                           |
| `H`         | Hourly                                  |
| `T`, `min`  | Minutes                                 |
| `S`         | Seconds                                 |
| `L`, `ms`   | Milliseconds                            |
| `U`, `us`   | Microseconds                            |
| `N`         | Nanoseconds                             |
</details>
<details><summary>
Why do we smooth our time series data?</summary>

Smoothing time series data helps clean out the 'noise' so we can better spot trends.  For example, to capture a true long-term trend in retail sales, it would be necessary to clean out the seasonal fluctuations in the data.  We know sales will spike in retail around the holidays each year, so that seasonal spike would need to be smoothed out so we can see the underlying trend.
</details>
<details><summary>
What are some methods for smoothing time series data?</summary>

Some of the methods for smoothing time series data are simple moving average, exponentially weighted moving average (EWMA) and Hodrick-Prescott filter.
<blockquote>
<details>
<summary>Simple Moving Average:</summary>

In a simple moving average, the mean is calculated on a specified number of data points to the get the trend line.  For example, using our Jeopardy data, we would get the simple moving average of the point values by calculating the mean of every 5 values, moving down 1 with each calculation.  Using our Jeopardy data, lets visualize a simple moving average:

![simple_ma_gif](Images/simple_ma_gif.gif)

Now let's calculate the simple moving average values for the `value` column and place them in a new column called `moving avg`.  The moving average values are calculated using the `.rolling()` function, with the parameter `window` set to 5.  The `window` parameter is the number of time points to include in the mean calculation...
```python
df['moving avg']=df['value'].rolling(window=5).mean()
```
![simple_ma_df](Images/simple_ma_df.PNG)
</details>

<details>
<summary>Exponentially Weighted Moving Average (EWMA):</summary>

EWMA is a moving average technique that applies more weight to recent data. To obtain the EWMA with pandas, the `.ewm()` function is called. The weight you wish to apply is supplied with the `halflife` parameter.  The `halflife` is how long it takes a weight to reach half of its original weight. Using this method, the lower the `halflife` the move weight is placed on the most recent time periods.  Half life can be visualized as follows:
![ewma_gif](Images/ewma_gif.gif)

The function itself is called like this:
```python
df['ewma']=df['value'].ewm(halflife=3).mean()
```
![ewma_df](Images/ewma_df.PNG)


</details>

<details>
<summary>Hodrick Prescott Filter:</summary>
The Hodrick Prescott filter separates your data into trend and noise, and converts them into two Pandas Series.  These Series can be placed into a DataFrame, or plotted directly allowing for easy visualization.

For this example, we'll use Tesla stock price data from the last 10 years.  The date column will be converted to `datetime` type upon reading the csv which gives us full `datetime` functionality, and displays our charts appropriately:

![TSLA_df](Images/TSLA_df.PNG)

Next we'll import the Hodrick Prescott filter from the `statsmodels` library and use it to separate the noise from the trend:
```python
import statsmodels.api as sm
noise, trend = sm.tsa.filters.hpfilter(df['Open'])
```
This data can then be easily plotted by using the `plot()` pandas function:

![TSLA_noise](Images/TSLA_noise.PNG)

![TSLA_trend](Images/TSLA_trend.PNG)
</blockquote>
</details>
</details>
<details><summary>
What are the basics of stationarity and non-stationarity?</summary>

This is an important concept because certain models require stationary data and others require non-stationary data.  Simply put - stationary data has no trend and non-stationary data does.

Sometimes it can be difficult to visually determine whether the data is stationary or not.  In these cases the Augmented Dickey-fuller (`adfuller()`) test can be implemented.  The 2nd line of the `adfuller()` output is the p-value.  If the p-value is greater than 0.05 then the data is non-stationary.

<img src='Images/TSLA_adfuller.PNG' width=500><br>
</details>
<details><summary>
How do you convert non-stationary data to stationary?</summary>

If you determine your data is non-stationary, but you need to be, it can be converted by applying either `.pct_change()` or `.diff.()` to your target column:

<img src='Images/diff_pct_chg1.PNG' width=600><br>

The `.pct_change()` method will show the percentage change between values, while the `.diff()` method will subtract the values to get the difference:

<img src='Images/diff_pct_chg2.PNG' width=500><br>
</details>
<details><summary>
Which models use stationary data and which use non-stationary data?</summary>

ARMA models assume stationarity.

ARIMA does not assume stationarity.

ARIMA will convert your data to stationary and then execute the function.  ARMA requires that you supply stationary data from the start.
</details>
<details><summary>
What is the point of ACF and PACF?</summary>

ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function) help to determine the number of lags that are important in the correlation of a dataset.  This lag number is important for autoregressive models, such as ARMA and ARIMA.  Lags can be thought of as a unit of time - it's the measure of distance (in time) that the data point corresponds to.  ACF and PACF determine the correlation of data between those time points.

Below you can see the autocorrelation plotted with `.plot_acf()`, using the same weather example from class.  Significant lags exist at particular hours (lags).  You would expect that the temperature at hour (lag) 12 on one day will be closely correlated to the temperature at hour (lag) 12 on the next day, and so on.

<img src='Images/ac04.png' width=450><br>

Using partial autocorrelation, you can dive even deeper. PACF allows you to see not just which lags are correlated, but which ones have the heaviest effect on all the others. We run the `.pacf_plot()` function with the parameter `zero=False`. This ignores the first lag because the correlation of something with itself is always equal to 1. Now we can see that lags 1 and 2 account for the biggest impact on the the next hours' temperature. A big effect also occurs at lag 24, because a new day begins. This means that the temperatures for that hour are heavily dependent on the temperatures from 1-2 lags (one to two hours) ago, and what the temperature was at the same time of day, but the day before. Remember, lag is just another word for your time interval! In this case, hours.

```python
plot_pacf(df.Temperature, lags=48, zero=False)
```

<img src='Images/ac05.png' width=460><br>

</details>
<details><summary>
How do I determine the order numbers for ARMA and ARIMA models?</summary>

The ARMA and ARIMA models require an `order` parameter.  For ARMA, this parameter is a list of 2 values, the first being the AR (autoregressive) order, and the second being the MA (moving average) order.  For ARIMA, this parameter is a list of 3 values, the first is AR order, the 2nd is the difference order, and the 3rd is the MA order.  Because ARIMA models do not assume stationarity, the model must difference the values to obtain stationarity.  This value dictates the amount to difference the values.

The AR order number is the number of critical lags.  The lag number can be obtained from your PACF analysis.  The MA order number is the moving average window.  Determining the AR order on our Tesla stock data might look something like this:

Our PACF plot, shows two significant lags, and thus our AR order value would be 2:

![TSLA_pacf](Images/TSLA_pacf.PNG)
</details>
<details><summary>
What is .reshape() and why do I have to use it?</summary>

When working with Pandas, we often pass Series objects into our model.  The shape of values in a Pandas Series object is a 1d array.  This has to be converted into a 2d array which is essentially an array of arrays - or list of lists. .  This is done using the `.reshape()` function.  The matrix values we desire are passed into this function.  In the following example we reshape our list into a 2d array using `.reshape(3,4)`, where 3 is the number of lists and 4 is the number of values in each list:

![2d_arrayImages](Images/2d_array.PNG)

Many models require the 2d array to be formatted such that each value is in a list by itself. If we were inserting the above sample data into a model, it would be converted using `.reshape(-1,1)`, where -1 indicates an unknown number of rows, and 1 indicates the number of values in each list.  The -1 will allow the function to generate the amount of rows necessary to hold the data.  The output looks like this:

![2d_array_reshape](Images/2d_array_reshape.PNG)

</details>
<details><summary>
What is .get_dummies() and why do I have to use it?</summary>

This function can convert your categorical data into numerical binary format.  This is especially important when working with certain types of models, because categorical data cannot be read by the model.  If you want to give your model categorical data such as False/Positive, Male/Female, or Buy/Sell, it will need to be converted into binary so the computer can understand it.  The `get_dummies()` function does this by splitting the categorical column of data into multiple columns of separate data with a 1 or 0 representation.  Lets encode the category column of our Jeopardy data using `get_dummies()`:

![get_dummies1](Images/get_dummies1.PNG)

You can see below that the categories have been converted into separate columns with a 1 or 0 representation, marking whether this data did or did not have this category:

![get_dummies2](Images/get_dummies2.PNG)
</details>

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
