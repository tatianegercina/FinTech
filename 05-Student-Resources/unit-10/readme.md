## FAQs

## Unit 10: Time Series
[What's the point of using `datetime` objects?](#whats-the-point)<br>
[How do you convert objects to `datetime`?](#how-do-you-convert-objects-to-datetime)<br>
[How do you access `datetime` objects?](#how-do-you-access-datetime-objects)<br>

#### What's the point of using `datetime` objects?
Humans can look at a date and instantly know how to categorize it - day, month, year, etc. - but computers look at dates see just another line of text, and will interpret that text as `strings`.  This can make cleaning, prepping and plotting data very difficult.  That's where time series functionality comes into play.  Casting your date `strings` to `datetime` translates them for your code, allowing the code to interpret and categorize dates the same way you do.  For example, let's take a DataFrame of Jeopardy questions from the last 35 seasons.  In the following example, the data is read in via `.read_csv()`, but the dates are read in as `strings` by default.  You can see the dates are not categorized, but rather they are plotted in the order they appear in the data:

<img src='Resources/str_plot.png' width=400><br>

In the next example, the dates are parsed and converted to `datetime` objects.  The dates are now being categorized properly and are listed in the correct order automatically:

<img src='Resources/datetime_plot.png' width=600><br>

#### How do you convert objects to `datetime`?
Converting objects to `datetime` can be tricky.  If using pandas, its best to handle the conversion upon reading in of data.  The syntax to handle the conversion from `read_csv()` is:

```python
df = pd.read_csv('jeopardy.csv', parse_dates=True)
```
This converts each object to a `datetime` object.  Alternatively, you can also set the index as the date column for ease of plotting:
```python
df = pd.read_csv('jeopardy.csv', parse_dates=True, index_col='air_date)
```
#### How do you access `datetime` objects?
There are numerous ways to access `datetime` objects.  One of the benefits of using these data types, is the added functionality they provide for analysing data, not just with plotting but with cleaning and aggregating.  Using our Jeopardy example, we can access different episodes using different date calls:
<details>
<summary>To access rows by a particular year:</summary>

![year_df](Resources/year_df.png)
</details>
<details>
<summary>To access rows by a particular year and month:</summary>

![year_month_df](Resources/year_month_df.png)
</details>

<details>
<summary>To access rows by a particular year, month, and day:</summary>

![year_month_day_df](Resources/year_month_day_df.png)
</details>
<details>
<summary>To access a range of dates by year:</summary>

![year_month_day_df](Resources/range_year_df.png)
</details>
<details>
<summary>To access a range of dates by year and month:</summary>

![year_month_day_df](Resources/range_year_month_df.png)
</details>
<details>
<summary>To access a range of dates by year, month and day:</summary>

![year_month_day_df](Resources/range_year_month_day_df.png)
</details>

#### How do you group time series data?
Grouping time series data is important for plotting and analysis.  The `.resample()` method allows grouping by multiple categories.  Similar to the `.groupby()` function, an aggregation method must be used to show the grouped data.  For example, we can group the mean jeopardy point values by year using the following code:

<img src= Resources/resample_Y_df.png width=325><br>

The data can then be plotted:

<img src= Resources/resample_Y_plot.png width=425><br>

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

#### Why do we smooth our time series data?

Smoothing time series data helps clean out the 'noise' so we can better spot trends.  For example, to capture a true long-term trend in retail sales, it would be necessary to clean out the seasonal fluctuations in the data.  We know sales will spike in retail around the holidays each year, so that seasonal spike would need to be smoothed out so we can see the underlying trend.

#### What are some methods for smoothing time series data?

Some of the methods we learn in class are exponentially weighted moving average (EWMA), Hodrick-Prescott filter.

<details>
<summary>Simple Moving Average:</summary>

In a simple moving average, the mean is calculated on a specified number of data points to the get the trend line.  For example, using our Jeopardy data, we would get the simple moving average of the point values by calculating the mean of every 5 values, moving down 1 with each calculation. could be take on every 5 data points to get a moving (also known as rolling) average.  Using our Jeopardy data, lets visualize a simple moving average:

![simple_ma_gif](Resources/simple_ma_gif.gif)

Using our Jeopardy data, we'll calculate the simple moving average values for the `value` column and place them in a new column called `moving avg`.  The moving average values are calculated using the `.rolling()` function, with a `window` parameter of 5 set.  The `window` parameter is the number of time points to include in the mean calculation.  For our example, we'll use a window of 5:
```python
df['moving avg']=df['value'].rolling(window=5).mean()
```
![simple_ma_df](Resources/simple_ma_df.png)
</details>

<details>
<summary>Exponentially Weighted Moving Average (EWMA):</summary>

EWMA is a moving average technique that applies more weight to recent data. To obtain the EWMA with pandas, the `.ewm()` function is called. The weight you wish to apply can is supplied with the `halflife` parameter.  The `halflife` is how how long it takes a weight to reach 1/2 of its original weight. Using this method, the lower the `halflife`.  Half life can be visualized as follows:
![ewma_gif](Resources/ewma_gif.gif)

The function itself is called like this:
```python
df['ewma']=df['value'].ewm(halflife=3).mean()
```
![ewma_df](Resources/ewma_df.png)


</details>

<details>
<summary>Hodrick Prescott Filter:</summary>
The Hodrick Prescott filter separates your data into trend and noise, and converts them into two pandas Series.  These series can be placed into a DataFrame, or plotted directly allowing for easy visualization.

For this example, we'll use Tesla stock price data from the last 10 years:

![TSLA_df](Resources/TSLA_df.png)

Next we'll import the Hodrick Prescott filter from the `statsmodels` library and use it to separate the noise from the trend:
```python
import statsmodels.api as sm
noise, trend = sm.tsa.filters.hpfilter(df['Open'])
```
This data can then easily be plotted by using the `plot()` pandas function:

![TSLA_noise](Resources/TSLA_noise.png)
![TSLA_trend](Resources/TSLA_trend.png)


</details>
