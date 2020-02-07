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
<summary><strong>To access rows by a particular year:</strong></summary>

![year_df](Resources/year_df.png)
</details>
<details>
<summary><strong>To access rows by a particular year and month:</strong></summary>

![year_month_df](Resources/year_month_df.png)
</details>

<details>
<summary><strong>To access rows by a particular year, month, and day:</strong></summary>

![year_month_day_df](Resources/year_month_day_df.png)
</details>
