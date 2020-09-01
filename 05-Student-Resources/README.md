# Student FAQ

We know how many different questions can pop up during the course of this class, especially with such a scope of technologies covered. This FAQ is intended to answer many common questions asked by students during this course. We hope you find it useful!

If you think of other potential questions to add, please let us know! We are always looking for more feedback. Feel free to log an issue or a pull request with your desired additions.

# Unit 1: Intro to FinTech

## Helpful Links

* [Git/Github](https://github.com/Multishifties/No-Nonsense-Github-Project)

* [Visual Git Guide](http://marklodato.github.io/visual-git-guide/index-en.html)

---

## Unit 1 FAQs

<details>
<summary>Where can I get started with learning Git?</summary>

Start with our pre-work, which has two modules with video tutorials and activities that can help out with the foundations of working with Git:
[Bootcamp Pre-work](https://coding-bootcamp-fintech-prework.readthedocs-hosted.com/en/latest )

Conveniently, GitHub has their own set of guides to help break down how to use the program:
[GitHub Guides](https://guides.github.com/)

Additionally, if you find videos helpful in your learning process, this is roughly an hour of video designed to cover the fundamentals of Git and GitHub:
[No Nonsense Github Videos](https://github.com/Multishifties/No-Nonsense-Github-Project)

Finally, we have a handy visual Git reference guide located here:
[Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html)

</details>

<details>
<summary>Where can I get a simple, yet comprehensive beginner summary for Markdown?</summary>

Right here! Try this [Markdown Guide!](https://www.markdownguide.org/cheat-sheet/)

</details>

<details>
<summary>How does the instructor execute computer commands so quickly?</summary>

The answer is simple - keyboard shortcuts.  You may not have needed them before - but in coding, they'll be one of your new best friends.  Check out these keyboard shortcut cheatsheets to help you get started:

[Mac](Resources/mac-shortcuts.md)

[Windows](Resources/windows-shortcuts.md)

</details>

<details>
<summary>Why do I need a virtual environment?</summary>

Virtual environments can be compared to different user profiles on one computer. You might share a computer in your home with your family, but you might not have the same programs installed as your 5 year old son, or the same bookmarked pages as your teenaged daughter. When you are ready to the use the computer, you simply log in and all your personal settings are there waiting for you.

In a similar way, virtual environments create a personalized space for your project within your computer.  For example, you might be working on a project with your group during project week that needs certain packages that you don't typically need in the everyday course of class.  You also notice that one of the necessary packages doesn't work with your version of Python and you need a downgraded version.  You would create a virtual environment to download only the packages needed for the project and could set that virtual environment to run the needed version of Python.  Because of your virtual environment you won't need to downgrade your Python package across the board, but only for the project you need it for.

Another important reason for using virtual environments is for deployment purposes. If you have an application you wish to deploy, you wouldn't want unneeded code packages installed with it. This will slow down the application and cause deployment errors.  Having a virtual environment will self contain only what is needed for the application.

</details>

<details>
<summary>Where can I find out more about FinTech and stay up to date on FinTech news?</summary>

As with most topics, there are numerous resources for gaining more information and all are just a Google search away!  But to get you started on your journey, here are a few web resources that we like:

[FinTech Weekly](https://www.fintechweekly.com/)

[TechCrunch](https://techcrunch.com/tag/fintech/)

[Coin Telegraph](https://cointelegraph.com/)

[FinTech Futures](https://www.fintechfutures.com/)

[IT World Canada](https://www.itworldcanada.com/)

[Digital Finance Institute](https://www.digitalfinanceinstitute.org/)

[Canadian FinTech Market Map](https://www.pwc.com/ca/en/industries/technology/canadian-fintech-market-map.html)

[Status of The Canadian FinTech Landscape (CFA Montréal)](https://www.cfamontreal.org/static/uploaded/Files/Presentation/19-02-07-David_Nault_Rendez-Vous-Fintech_CFA-Montreal.pdf)

[FinTech Study (Competition Bureau Canada)](https://www.competitionbureau.gc.ca/eic/site/cb-bc.nsf/eng/04319.html)

[Toronto Finance International FinTech Strategy](https://tfi.ca/tfi-initiatives/fintech)

[FinTech Canada Conference](https://www.fintechcanada.com/)

[Canadian FinTech & AI Awards](http://www.fintechawards.org/)

[The Canada FinTech Forum](https://www.forumfintechcanada.com/)

[Canadian FinTech Summit](https://fintechsummit.ca/)

</details>

---
## Unit 2: Financial Programming with Python

### Helpful Links

* [Python - Beginner](https://www.learnpython.org/)

* [Python Scripting](https://automatetheboringstuff.com/)

* [Python f-strings](https://www.python.org/dev/peps/pep-0498/)

* [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

* [Python CSV Module](https://docs.python.org/3/library/csv.html)

* [Git/GitHub](https://github.com/Multishifties/No-Nonsense-Github-Project)

* [Visual Git Guide](http://marklodato.github.io/visual-git-guide/index-en.html)

* [Python 3's f-Strings](https://realpython.com/python-f-strings/)

* [Anaconda Install Guide](AnacondaInstallGuide.md)

- - -
### Unit 2 FAQs


<details>
<summary>What's the relevance of Python?</summary>
Python is the primary language that we will be using in this course. It's a semantic language which makes it easier to read and understand, and the reliance on indentation makes the organized structure quicker to grasp. With this language, we'll be able to dive into a slew of libraries that will make solving complex data problems more simple.

</details>
<details><summary>What's up with this crazy indentation?</summary>
With Python, indentation is more than just organization and readability. Python's functionality actually depends on proper indentation!

In this snippet, we're using indentation to tell our code where our for loops begin and end. In Python, indenting creates blocks of code that work together. Similarly, indenting backwards tells the program when to end a loop.

```python
for x in range(10):
    print(x)

for x in range(20, 30):
    print(x)
```

The code you will write in Python will eventually be seen by someone else. Focusing on organization and readability is important because you want colleagues to be able to read your code. If your code is poorly organized it will be difficult to read later on.



</details>
<details><summary>How do list comprehensions work?</summary>
In a list comprehension, you are writing a for loop in a concise format that outputs a list object.  It can be confusing because the variable is repeated twice.  What the code is saying is: for each item in my old list, add that item to my new list.

For example:

Input:
```Python
old_list = range(10)
new_list = [item for item in old_list]
    print(new_list)
```
Output:
```Python

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</details>
<details><summary>How are variables assigned with a for loop?</summary>
Typically a for loop is iterating over an object and extracting each of the next smallest objects.  The variable is established after the word `For`. If your variable is `letter` and your object is `name` then Python finds the next smallest item in the `name` object you are iterating over and assigns `letter` to each of them.


Input:
```Python
name = 'Elliot'
for letter in name:
  print(letter)
```
Ouput:
```Python
E
l
l
i
o
t
```

In the example of a list of strings, the next smallest items are the individual strings:


Input:
```Python
name_list = ['Elliot' ,'Darlene', 'Angela', 'Shayla']
for name in name_list:
  print(name)
```
Output:
```Python
Elliot
Darlene
Angela
Shayla
```


</details>
<details><summary>How does slicing work?</summary>
Slice notation allows you to extract certain information from a list.  The syntax is `a[start:stop:step]`, with `step` being an optional component.  If a start number is ommited, it is assumed to be zero.  If a stop number is ommitted, it is assumed to be one more than the index number of the last item in the data.  In the following examples ommitting the stop number is the equavilient of using the number 4, because there are only 4 items (0, 1, 2, 3) in the list.

Given the following list:
`name_list = ['Elliot' ,'Darlene', 'Angela', 'Shayla']`

Input: `name_list[:]` OR `name_list[0:4]`

Both have the same output:
```Python
['Elliot' ,'Darlene', 'Angela', 'Shayla']
```

Input: `name_list[0:2]`

Output is first two names:
```Python
['Elliot' ,'Darlene']
```

Input: `name_list[2:4]`

Output is last two names:
```Python
['Angela', 'Shayla']
```

Input: `name_list[0:4:2]` OR `name_list[:4:2]` OR `name_list[::2]`


All three have the same output - every other name, starting with the first name:
```Python
['Elliot', 'Angela']
```

For more information check out this [Stack Overflow post](https://stackoverflow.com/questions/509211/understanding-slice-notation)

</details>
<details><summary>How do you access values in a nested dictionary?</summary>

Think of a dictionary like an assembled puzzle.  To get one of the pieces out of the puzzle, you have to deconstruct the puzzle by breaking apart the larger chunks and then the smaller chunks.  If you have a list of two dictionaries, you must first extract the dictionary you want, then you can extract the value you want.

In the following list of dictionaries lets access the 2nd pilot of the Galactica:
```Python
battlestars =
[{'Ship': 'Pegasus',
  'Commander': 'Admiral Helena Cain',
  'Pilots': ['Whiplash', 'Thumper']},
 {'Ship': 'Galactica',
  'Commander': 'Admiral William Adama',
  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}]
```
Our list contains two dictionaries, with the Galactica being in the 2nd one.
![Alt Text](Images/battlestar_dictionary.gif)

So we first call our list object (`battlestars`), then the index position of our 2nd dictionary - `1`.

```Python
battlestars[1]
```
Which gives us:
```Python
{'Ship': 'Galactica',
  'Commander': 'Admiral William Adama',
  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}
```

Now that we have the dictionary we want, we can call the key we want.
![Alt Text](Images/galactica_dictionary.gif)


We need to get information on pilots, so we call the 'Pilots' key:
```Python
battlestars[1]['Pilots']
```
Which gives us:
```Python
['Starbuck', 'Apollo', 'Helo', 'Athena']
```

Now we have extracted a list of pilots.  We just need to use the index position of the Pilot we want to finish up.  We want the 2nd pilot in the list, so we call position 1:

```Python
battlestars[1]['Pilots'][1]
```

Which gives us:
```Python
'Apollo'
```
</details>
<details><summary>How can tabular data be accessed to faciliate exploration in Python?</summary>

Tabular data is data in the form of a table with rows, columns and values.  Spreadsheets and CSV files are a very well-known forms of tabular data.  This format makes it simple to find values, but how do we manipulate those values using Python?  The data must be 'read into' a program.

Python has a CSV module with a `reader()` function that allows for the 'reading in' or 'parsing' of csv tabular data into your python code.  The data is stored in a variable that can be interated over using a for loop, thereby extracting the data within.

To open our sample `battlestar.csv` file, and then designate each column as a variable we would do the following:

  ```Python
alias = []
model_number = []
with open('auditingprojects/battlestar.csv', 'r') as file:
    csvfile = csv.reader(file, delimiter=',')
    for row in csvfile:
        alias.append(row[0])
        model_number.append(row[1])
```
When we say for `row` in `file`, we are literally storing a row in the spreadsheet in the variable `row` during each loop:<br>
![Alt Text](Images/cylon_rows.gif)

To get the columns we use indexing:<br>
![Alt Text](Images/cylon_columns.gif)

In this way, the `alias` variable now holds `row[0]` - the first column and all its row values.  And the `model_number` variable now holds `row[1]` - the second column and all its row values.

</details>
- - -

---
## Unit 3 | 4: Python and Pandas

### Helpful Links

* [Pandas Tutorials](https://chrisalbon.com/)

* [Pandas Documentation](http://pandas.pydata.org/)

* [Pandas Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

* [Visual Guide to Joins](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)

* [Pandas Merging](https://pandas.pydata.org/pandas-docs/stable/merging.html)

* [Anaconda Install Guide](AnacondaInstallGuide.md)
- - -

### Additional Course Resources

### Unit 3 | 4 FAQs

<details><summary>Why is it called pandas?</summary>
According to *Python for Data Analysis*, written by Pandas inventor himself, Wes McKinney, the name pandas "is derived from panel data, an econometrics term for multidimensional structured data sets, and Python data analysis itself"(McKinney, 2013).

</details>
<details><summary>How do you access a column?</summary>
To access a column in your DataFrame you call the DataFrame variable plus the column by using either bracket or dot notation.  For example, lets use the following DataFrame named `cylons`:

![Cylon DF](Images/Cylon_DF.PNG)<br>

you would access the `Model_Number` column as follows:

![Cylon DF](Images/Cylon_Series.PNG)<br>

</details>
<details><summary>Why do I keep getting a key error?</summary>
If Pandas throws a key error at you, it can be really frustrating, especially when you just *know* you've typed in a value that is in the key.  If this happens during the accessing of a column, try running the df.columns function to get a screen print of all the column names.  You might have an invisible space or escaped line in the column name that doesn't show up during normal printing, that will show up when this function is used.  In some cases you might be using a function that defaults to the row axis instead of the column axis.  In that situation you will get an error like: `KeyError: "['X'] not found in axis"`.  In that situation, yes the key exists but that function isn't looking for the column keys, but rather a row value.

</details>
<details><summary>What is a DataFrame axis?</summary>
A DataFrame axis is simply the column headers or the row index positions.  This image helps to visualize it:

![Cylon DF Axes](Images/Cylon_Axes.png)<br>


</details>
<details><summary>What is the difference between a Series and a DataFrame?</summary>
A DataFrame is a 2D matrix object holding rows and columns.  A Series is a 1D object, much like an array, though it can have an index.  When a single column is extracted from a DataFrame, it is a Series object.  The following image shows a Series object extracted from our cylons DataFrame:

![Cylon DF Series](Images/Cylon_Series.PNG)<br>

</details>
<details><summary>Why do my Dataframe changes disappear when I move to the next cell in Jupyter?</summary>

When a DataFrame is stored in a variable, it is a one time snapshot of the DataFrame at the time of storage.  If you make changes to the DataFrame, you must either store the new DataFrame in a new variable, overwrite the old DataFrame variable name, or use the `inplace = True` argument in the function parameters.  For example, the following code will only populate a change for the [notebook cell in which it is located:  `cylons.rename({'Model_Number': 'Model#'})`.  But by adding an `inplace=True` parameter, the change will say:  `cylons.rename(columns={'Model_Number': 'Model#'}, inplace=True)`.  An equivalent method is to reassign the value and call it: `cylons = cylons.rename(columns={'Model_Number': 'Model#'})`.

</details>
<details><summary>How do you loop through a DataFrame?</summary>

There are multiple methods to achieve this task.  For a super efficient method see our example below.  To see other methods, check out this great [Medium article](https://medium.com/@rtjeannier/pandas-101-cont-9d061cb73bfc).

You can loop through our cylons DataFrame using `.loc` as follows:

```python
for i in cylons.index:
        print(cylons.loc[i,'Alias'])
        print(cylons.loc[i, 'Model#'])
```
In this example `.loc()` searches for `i`, which represents the contents of each cell, and then the column name that is passed, both in brackets.
</details>
<details><summary>Why must I apply a function to a groupby object in order to output a DataFrame?</summary>

The groupby function puts all elements of a certain category together by finding each unique value in the column specified and converting that to a new index.  If you were to group our cylons_df by the `Model#` but not apply a function to it, the code can run the grouping, but it doesn't know what to do with the other columns.  There would be a new index, with extraneous data that doesn't fit the new index length or match up in anyway.  By applying an aggregation function, such as `.count()`, the code can perform an aggregation on the other columns and keep them in the object.  For example, if we run `cylons_df.groupby('Model#').count()`, our DataFrame index is converted into the unique values of cylon model numbers, and then the other data is counted based on how many there are of each model number.

![Cylon DF Groupby](Images/Cylon_Groupby.PNG)<br>

</details>
<details><summary>What does this error mean: `TypeError: unsupported operand type`?</summary>

Have you ever gotten an error similar to this:  `TypeError: unsupported operand type(s) for +: 'int' and 'str'`?  If so, its because you were trying to combine data of different types, and Python doesn't like that! Let's take the following code, where we are trying to concatenate a string to the end of an integer to make a new sentence:
```python
for x in cylons['Model#']:
    print(x + ' is the best!')
```
This would throw the following error:
```python
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
The TypeError will typically tell you what two datatypes you are trying to combine, as in the above code snippet.  So to fix our error, we just have to alter these data types to make them play nice!  To do that we can change our integer to a string as follows:
```python
for x in cylons['Model#']:
    print(str(x) + ' is the best!')
```
Now when we run the code, we get the result we are looking for:
```python
6 is the best!
6 is the best!
6 is the best!
6 is the best!
6 is the best!
6 is the best!
6 is the best!
3 is the best!
3 is the best!
```

</details>


#### Sources:
McKinney, W. (2013) *Python for Data Analysis.* O'Reilly Media, Inc, USA.

---
## Unit 04: Pandas
#### When should we use Pandas versus just using Python?
Python is a scripting language, while Pandas is a library that works on top of Python and makes data manipulation easier.

Libraries are pre-written collections of code that make it easier to unlock the capabilities of a programming language. Someone else already did a ton of hard work to create these libraries and make your life easier and your workflow more efficient.

It would be a slog to manually go through all of your data with vanilla Python. Pandas makes this process much quicker.


---
## Unit 05: APIs
#### How do I differentiate between the client and the server?
The web applications we build in class (and all other web apps) will live on a server, which is basically a gigantic computer or network of computers. When a user goes into their browser and types in an address, the server sends information to the user's computer, or the client.

Basically: Clients request from the server, and the server returns a response.

#### Where can I find more information on how to use these APIs?
Each API is a pre-written set of code that helps you interact with somebody elses information. Every API will come with its own set of documentation, and much like with a library, you will have to dive into it! There should be a developer section on each site that will explain the service and any potential limitations.

Any time we work with an API, it's a good idea to have the documentation ready and refer to it frequently. This is all part of the process when it comes to picking up and familiarizing yourself with new technologies.


---
## Unit 06: Data Visualization
#### What is the relevance of Data Visualization?
Your stakeholders and clients will typically be much more able to understand your projections and analytics if there are compelling and visually interesting graphics that go along with them. Raw numbers may give information, but taking that data and creating visualizations is what tells a compelling story.

# Unit 10: Time Series

## Unit 10 FAQs

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

# Unit 11: Classification

## Helpful Links
### The Confusion Matrix and Other Metrics

*  Additional Confusion Matrix Code Examples over at [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

*  [Walkthrough](https://www.kaggle.com/diegosch/classifier-evaluation-using-confusion-matrix) of a Model Using and Interpreting a Confusion Matrix

### Machine Learning with Imbalanced Data

* Imbalanced Learning Package [Documentation](https://imbalanced-learn.readthedocs.io/en/stable/index.html)

* Another Applied [Walkthrough](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets) Using the imbalanced-learn Package


---

## Additional Course Resources

*  An [interview](https://insights.som.yale.edu/insights/will-machine-learning-transform-finance) with the head of machine learning at Goldman Sachs (an investment bank) on how ML is transforming finance.

* An Example of Applying Binary Classification ML Models to [Trading Currencies.](http://nrl.northumbria.ac.uk/34544/1/Evaluating%20machine%20learning.pdf)
  *  This paper, published in Expert Systems, looks at dozens of different ML models, including logistic regression trees, setting up a binary classification problem (i.e., up or down days, y = '0' or '1') in order to trade currencies. A few models perform poorly, but some generate average returns as high as 20% per year.

*   Quantitative asset management has only recently been applying machine learning, but is [realizing big benefits from doing so.](https://dachxiu.chicagobooth.edu/download/ML.pdf)
    *  This paper from academics at The University of Chicago and AQR (a large quantitative hedge fund manager) compare the performance of traditional statistical models used to forecast stock returns to the performance when deploying machine learning techniques (including random forests, but also many of the techniques we’ll learn in subsequent units). While dense, consider reading if you’re interested in a detailed contrast between traditional methods for forecasting stock returns and those involving machine learning.

## Unit 11 FAQs

<details>
<summary>What is the difference between supervised learning and unsupervised learning?</summary><br>
<blockquote>
<details>
<summary>Supervised Learning</summary><br>

Supervised machine learning uses labeled data with input variables (feature data) and output variables (target data) and uses the feature data to predict the target data. Because the data is labeled, the outcome is known. This data can be fed to the model, and if the model guesses incorrectly, the error can be used to fine tune the model until it makes highly accurate guesses.<br>

An example of this is using tuning forks to tune a piano. Tuning forks produce very precise tones. These tones are your known output. You can press a piano key and compare the piano's tone (model output) to the tuning fork (known y value). If the piano's tone is too low then you can tighten the piano wire to make the piano better at matching the tuning fork. This process of adjusting the model to make the output match the known output is essentially supervised learning.
<br>
</details>
<details>
<summary>Unsupervised Learning</summary><br>

Unsupervised learning models are given only input variables and must work to make connections to the data without predicting a labeled target. These types of models are often clustering models that uncover connections in the data and group all the features into classes accordingly.<br>
<br>
An example of unsupervised learning would be to use website purchase data to group customers into two classes based on their spending habits. This clustering might reveal that class 1 more spends more with a coupon incentive, while class 2 spends more on targeted advertising on social media.
</details>

</blockquote>
</details>

<details>
<summary>How is Training and Testing Data Utilized?</summary><br>

When working with models, data is divided into training and testing sets. The training set is used to teach (supervise!) the model so it learns how the input data is connected to the output data and can make predictions. The testing data set is used to validate how well the model performs on data it has not seen before, by running the model on the testing feature data, and comparing it's predictions to the testing target data.<br>

</details>


<details>
<summary>What is the difference between linear regression and logistic regression?</summary>

Though both use regression techniques, linear and logistic regressions are designed for two different types of data. If the values you are predicting are continuous, then linear regression is the correct model. If your values are categorical, then logistic regression is the correct model.
</details>

<details>
<summary>What is the difference between continuous and categorical data?</summary>
<blockquote>
<details>
<summary><strong>Continuous Data</strong></summary>
Continous data is quantitative data that can be any number with infinite possibilities.

Examples of continuous data include:

- House prices:  $152,500, $378,935, $598,214, $95,290, $1,293,488
- Population: 10,573; 192,568; 1,024,692; 5,288; 25,049
- Age: 5, 19, 98 56, 40
- Grades: 95, 80, 99, 70, 65

</details>
<details>
<summary><strong>Categorical Data</strong></summary>
Categorical data can be classified into specific groups.

Examples of categorical data include:
- Male, Female
- Yes, No
- Positive, Negative
- Good, Bad, Neutral
- Snickers, Milky Way, Twix
- Soccer, Hockey, Baseball, Basketball, Lacrosse
</details>
</blockquote>
</details>

<details>
<summary>Why am I getting a value error for continuous data?</summary>

Are you running a Logistic Regression model and keep getting an error like the one below?

![continuous err](Images/continuous_err.PNG)

This error means you are giving non-categorical data to your Logistic Regression model. Logistic Regression models use categorical data and cannot compute continuous data.

</details>

<details>
<summary>How do you preprocess data for classification?</summary>
Most categorical data is text-based and must be converted to numerical so that computations can be ran. For example, if your categories are male and female, you could convert them to 0 and 1. Scikit-learn offers functions that can handle this conversion simply. Two options are `LabelEncoder()` and `OneHotEncoder()`.

<blockquote>
<details>
<summary><strong>Preprocessing Target Data</strong></summary>

Using `LabelEncoder()` from scikit-learn, we can convert categorical data to numerical. We begin with a simple DataFrame showing 6 countries:

![country_df1](Images/country_df1.PNG)

Then we import `LabelEncoder` from sklearn.preprocessing, after which we instantiate the `LabelEncoder()` object, then run a `.fit()` followed by `.transform()`. The results are stored in a new variable `encoded_y` and inserted into the DataFrame.

```python
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
encoder.fit(df.Country)
encoded_y = encoder.transform(df.Country)
df['Encoded'] = encoded_y
```
Now you can see that the encoded values are numerical representations of the original countries:

![country_df2](Images/country_df2.PNG)

</details>

<details>
<summary><strong>Preprocessing Feature Data</strong></summary>

There are situations when using `Labelencoder()` is not appropriate. If you are encoding target values (the values you wish to predict), then using the label encoder is great, however, if you are encoding feature values, this method can cause accidental bias in your model prediction. This is because the numerical representations of the data will be interpreted as values by the model. A category of 5 will be given more weight than a category of 1. This is where the `.get_dummies()` pandas function used in Unit 10 comes into play. The function works by splitting the categorical column of data into multiple columns of separate data with a 1 or 0 representation. In the below example we use `.get_dummies()` to convert the same country data as before:

```python
encoded_data = pd.get_dummies(df.Country, columns='Country')
```
![country_df3](Images/country_df3.PNG)
</details>
<details>
<summary><strong>Scaling Feature Data</strong></summary>
In our previous example, we converted feature data to binary to avoid introducing bias into the model. For the same reason, we should scale data that have large numerical variance between features, so that all features are weighted the same. For example, let's suppose that our country DataFrame also includes an average number of children, average life expectancy, and average salary by country. The average number of children is a very small number compared to average life expectancy, which is a very small number compared to the average salary by country. These values vary greatly and need to be scaled, because the higher numbers may result in more weight bias.

![country_df4](Images/country_df4.PNG)

Using the `StandardScaler()` from scikit-learn, we will scale the data. First we instantiate the `.StandardScaler()` instance, then fit it to the data, then transform the data and show it in a new DataFrame:

```python
data_scaler = StandardScaler()
data_scaler.fit(df)
data_scaled = data_scaler.transform(df)
```
The new DataFrame shows the scaled data in place of the former values. Now all the values are standardized:

![country_df5](Images/country_df5.PNG)

</details>
</blockquote>
</details>

<details>
<summary>How does `train_test_split()` work?</summary>

The `train_test_split()` function makes splitting data for testing easy!  The function outputs four sets of data points - two sets each of target and feature data where one set is for training, and one set is for testing. This is why the variables that define the function are typically `X_train, X_test, y_train, y_test`. The most important parameters of the function are the `X` and `y`. During preprocessing, we separate our data into the feature data, or `X`, and the target data - `y`.

The `y` data are the values we wish to predict, and the `X` data are the values we use to influence our predictions. If our data is stored in a DataFrame, we just break it out and store it in variables. The values we wish to predict are stored as `y` and the features we are using to make our predictions are stored as `X`. We then feed these into the `train_test_split()` function.

Other parameters include: `stratify`, `test_size`, `train_size`, `random_state`, and `shuffle`.

If the `y` values consists of binary data (for example, male/female), and 25% of those values are male, and 75% of those values are female, then setting the `stratify` parameter to `y` will ensure the test and train data have the same ratio of male to female as the entire data set.

The specific `test_size` and `train_size` can also be set to override the default sizes. The default for these parameters will select sizes that complement the data set. The defaults can be overridden using either `int` or `float` values. If the parameter is set to `int`, then this will indicate a specific sample size you wish to include in the test or train set. If the parameter is set to `float` then it will indicate a percentage of the total dataset you wish to include in the test or train set.

When using the `shuffle` parameter, the data is shuffled (randomized) prior to being divided into train and test sets.

When using this function, the data is split each time randomly; however, if the `random_state` parameter is set, the same random split will be selected each time. To use this parameter, any number can be used as the `random_state` as long as it is used each time you run the model. Using this parameter will always ensure the same split is obtained even if `shuffle` is set to `True`.

An example of implementing a `train_test_split()` instance is as follows:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, shuffle=True)
```

</details>

<details>
<summary>What is the difference between True/False Positives and True/False Negatives?</summary>
Keeping track of the differences between these four can be a mind-bender. It often makes more sense when thought of as a medical test.<br>
<br>
For example, let's say you tested positive for flu, but you did not have it - this would be a False Positive.<br>
<br>
When applying these terms to machine learning, where the values we are predicting are usually more than just true or false and are less applicable to our daily lives as is medical testing, their meaning can become abstract. Here is a quick reference for keeping them straight. In our example, the model is predicting whether a color will be blue, green, or purple.

<blockquote>
<details>
<summary><strong>Terminology</strong></summary>
The True/False part of our terminology means that the test predicted either correctly (true) or incorrectly (false). The Postive/Negative part of the term means that the test was predicting the presence (positive) or absence (negative) of something.
</details>
<details>
<summary><strong>True Positive</strong></summary>
I thought you were green and I was right!

**OR**

The model predicted this value as green and it is correct.
</details>
<details>
<summary><strong>False Positive</strong></summary>
I thought you were green and I was wrong!

**OR**

The model predicted this value as green and it was incorrect.
</details>
<details>
<summary><strong>True Negative</strong></summary>
I thought you were not green and I was right!

**OR**

The model predicted this value was not green; it was correct.

</details>
<details>
<summary><strong>False Negative</strong></summary>
I thought you were not green and I was wrong!

**OR**

The model predicted this value was not green and it was incorrect.
</details>
</details>

<details>
<summary>How are precision and accuracy different?</summary>

Precision and accuracy are qualitative descriptions of measure of distances between data points.

Precision is a measure of how close elements are to each other. Accuracy is a measure of how close items are to the target. The following image helps to visualize this:
<img src='Images/acc_prec.png' width = 650>
</details>

<details>
<summary>How are bias and variance different?</summary>

Bias and variance are related to precision and accuracy. While precision and accuracy are *qualitative* terms describing agreement between a prediction and the target, bias and variance are *quantitative* terms describing that agreement.

Specifically, bias is the value of the difference between the target and the average of the predictions. Variance is the value of the difference between the values themselves. For example, let's say we are predicting the final exam grade for a student, and the actual grade is 90.

- **Scenario 1** - Our model predicts the values 97, 80, 95, and 92. The average is 91, so this scenario has a postive bias of 1, and a high variance, since the distance between the values is large.

- **Scenario 2** - Our model predicts the values 89, 88, 92, and 91. The average is 90, so this scenario has a bias of zero and very low variance, since the distance between the values is small.

To build on the imagery from precision and accuracy:

<img src='Images/bias_var.png' width = 650>

For more information on bias, variance and how they work together to make predictions, check out [this video from StatQuest](https://www.youtube.com/watch?v=EuBBz3bI-aA).

</details>
<details>
<summary>How do you use a confusion matrix?</summary>

<blockquote>
<details>
<summary><strong>Layout</strong></summary>
The basic layout of a confusion matrix is the actual values are listed along an axis, and predicted values are listed along the opposite axis.

![confusion1](Images/conf_matrix1.gif)
</details>
<details>
<summary><strong>Precision</strong></summary>
Precision is the measurement of how many positively predicted values were actually correct. For example, if our model was predicting colors - blue, green and purple, precision would be the measurement of how many times the model predicted purple and the actual value was also purple.

The formula for precision is TP / (TP + FP).

![confusion3](Images/conf_matrix3.gif)
</details>

<details>
<summary><strong>Recall</strong></summary>
Recall is the measurement of how many times a value was predicted and was also incorrect. For example, if our model was predicting colors - blue, green, and purple, recall would be the measurement of how many times green was predicted incorrectly.

The formula for recall is TP / (TP + FN).

![confusion2](Images/conf_matrix2.gif)
</details>
</details>

<details>
<summary>What is the point of using ensemble learning?</summary>

Ensemble learning is a method where multiple models are combined into one powerful predictor. In classification instances, the different models might make a final prediction by calculating which class had the most votes or predictions. In regression instances,  the mean of all results is typically taken and then offered as the final prediction.
</details>

<details>
<summary>How do I know if my data is imbalanced and why should I care?</summary>

An easy way to check for imbalanced data is to use the `Counter()` function. Passing your data through this function will count how many of each unique variable exist in the data.

The usage syntax is below:

```python
from collections import Counter
Counter(y_train)
```

Example output is:
```python
Counter({0: 11832, 1: 462})
```

We can tell this data is imbalanced because one of the values is represented over 11,000 times, and the other value is represented under 500 times.

It's important to check for imbalanced data because models will show bias to the values that appear more commonly, causing them to be predicted more often than the less commonly appearing values. This can cause issue with the accuracy of the model not only because the model fails to predict the minority classes correctly, but also because the skewed number of data points for the majority class will make the model **appear** more accurate when it is actually not.

As an example, let's use our color classes from before. If we train our model on 90 greens, 5 blues, and 5 purples, and it predicts green for each of them because of the bias. In this case, the accuracy will look great at 90% - even though it can't predict the other colors. Were that model to be implemented on a new data set, with 45 blues, 45 purples, and 10 greens, then it would guess the greens correct but not the blues and purples, resulting in only a 10% accuracy using the same model.

<img src="Images/bad_accuracy.png" width=600>
</details>

<details>
<summary>How do I manage imbalanced data?</summary>
The methods for correcting imbalanced data are oversampling, undersampling, and combination sampling. With oversampling, we increase the amount of data in the minority class. With undersampling, we decrease the amount of data in the majority class:

![sampling](Images/sampling.gif)

There are imports available from the Imbalanced Learn (`imblearn`) library that make these methods simple.

<blockquote><details>
<summary><strong>Oversampling</strong></summary>
The oversampling method involves adding data to the minority class so that the two classes are equal. Two methods for this are random oversampling and Synthetic Minority Oversampling Technique (SMOTE).
<blockquote><details>
<summary><strong>Random Oversampling</strong></summary>
Random oversampling duplicates the existing minority class data randomly until it is equally proportional to the majority class.

To utilize `imblearn` for random oversampling, we call the code as follows:

```python

from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

```
</details>
<details>
<summary><strong>SMOTE</strong></summary>
SMOTE works by adding generated synthetic (fake) data in a way that closely mimicks the existing minority class until the majority and minority classes are proportional.

To utilize `imblearn` for SMOTE, we call the code as follows:

```python

from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=1, ratio=1.0)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

```
</details>
</blockquote>
</details>
<details>
<summary><strong>Undersampling</strong></summary>
Undersampling is done by removing data from the majority class until the minority and majority are proportional. This is only feasible if there is still enough data to effectively train the model after removal. Two methods for undersampling are random undersampling and cluster centroid undersampling.
<blockquote><details>
<summary><strong>Random Undersampling</strong></summary>
Random undersampling removes the existing majority class data until it is equally proportional to the minority class.

To utilize `imblearn` for random undersampling, we call the code as follows:

```python

from imblearn.under_sampling import RandomUnderSampler
ros = RandomUnderSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

```
</details>
<details>
<summary><strong>Cluster Centroid Undersampling</strong></summary>
Cluster centroid undersampling works by using Kmeans to cluster the majority data into a quantity of clusters that is equal to the rows of minority data. The method then takes the mean value (centroid) of each cluster to establish a new list of majority data that is now equal to the length of the list of minority data. For example, if you have 10,000 rows of majority data and 300 rows of minority data, this method will make 300 clusters of majority data, and take their mean to establish 300 rows of new data that are respresentative of the majority class.

To utilize `imblearn` for cluster centroid undersampling, we call the code as follows:

```python
from imblearn.under_sampling import ClusterCentroids
cc = ClusterCentroids(random_state=1)
X_resampled, y_resampled = cc.fit_resample(X_train, y_train)
```
</details>
<blockquote>
</details>
<details>
<summary><strong>Combination Sampling</strong></summary>
Combination sampling takes from both sides. Because oversampling can lead to noisy data, and undersampling is not always feasible due to dataset size, a combination strategy may be worthwhile.
<blockquote>
<details>
<summary><strong>SMOTEENN</strong></summary>

One method for combination sampling is SMOTEEN (Synthetic Minority Oversampling Technique Edited Nearest Neighbors). This method initially oversamples using SMOTE but then undersamples by removing outliers from the data using a variation of K-Nearest Neighbors to remove data points that are surrounded by the opposite class.

The code to utilize this method is:

```python
from imblearn.combine import SMOTEENN

sm = SMOTEENN(random_state=1)
X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
```
</details>
</blockquote>
</details>
</blockquote>
</details>

---

# Unit 12: Natural Language Processing

### Helpful Links

* This online version of the NLTK book, [*Natural Language Processing with Python – Analyzing Text with the Natural Language Toolkit*](https://www.nltk.org/book/), is a great reference for all things NLTK.

* An excellent starter resource on spaCy: [*spaCy 101: Everything you need to know*](https://spacy.io/usage/spacy-101).

* The [Word Cloud](https://amueller.github.io/word_cloud/) documentation has everything from command-line interface tools to gallery examples of how to make your own, unique word cloud.
---

### Additional Course Resources

* [NLP installation guide](nlp-env-install-guide.md)

---

### Unit 12 FAQs

<details>
<summary>What is Natural Language Processing?</summary><br>

Natural language processing is a field focused on the goal of having computers interact with (understand and generate) natural (human) language.

Examples include:
* A spell Checker.

* Talking to digital assistants such as Alexa, Siri or Google Assistant.

* Voice-to-text on mobile devices.

Computer language is very specific; its unambiguous, literal, methodical, and mathematical. Human language is quite the opposite. Words can share multiple meanings when used in different contexts, despite being spelled the same or sounding the same.

When translating words between languages, the direct word-for-word translation will often sound nonsensical because the order of the words and cultural idioms vary. Even different dialects of the same language can have words or sayings that mean different things depending on your geography.

NLP allows us to process human language and text so that it can be used in machine learning and software applications.

</details>
<details>
<summary>What is Tokenization and why do I need it?</summary><br>

Tokenization is the process of breaking apart language into smaller pieces. A document of text could be tokenized into sentences, the sentences could be tokenized into words or phrases, or a word could be tokenized into characters. Tokens can then be counted, grouped, sorted, and further processed to help us better understand the content of the text. A simple example of tokenization is using Python's `.split()` function to split a sentence into a list of words using the whitespace as a delimiter.

<blockquote>
<details><summary>Word Tokenization</summary><Br>

In the following example we'll use `.split()` and the space delimiter to tokenize our sentence:

![sentence](Images/sentence_split.PNG)

This method works ok, but NLP can become much trickier than breaking down a sentence by a single delimiter. You might need to write code that breaks down an entire text into whole phrases on multiple delimiters. Because of this, we can use the Natural Language ToolKit (NLTK) platform to perform our tokenizing. NLTK provides libraries and tools that help with NLP tasks such as text processing. Let's tokenize the same sentence using NLTK's tokenizer, `word_tokenizer()`:

![sentence1](Images/sentence_tokens.PNG)

This method allows us to handle complex situations such as punctuation. We can also use regular expressions to customize our tokenizer further. This gives us much more flexibility to concisely deliver the intended outcome regardless of how complex the text might be.
</details>
<details><summary>Sentence Tokenization</summary><br>

Sentences can also be tokenized.  In the following example, we'll tokenize a short text into sentences.  First we use `.split()` and the period delimiter:


![sentence3](Images/sentence_sent_split.PNG)

This works ok, but what if we have a more complex text? What if our text has exclamation points or question marks? Or, even trickier, what if our text contains periods that do not denote the end of a sentence, but rather some other punctuation, like the period after *Mr.* or *Mrs.*? To work with this type of text, NLTK offers the `sent_tokenizer()`.  It works much like the `word_tokenizer`, but breaks apart text as sentence chunks, and is smart enough to know where the sentence breaks should be.  An example of using `sent_tokenzier` is as follows:

![sentence4](Images/sentence_sent_tokens.PNG)

</details>
</blockquote><br>
</details>

<details>
<summary>What are Stopwords?</summary><br>

Stopwords are considered words that hold no relevance to the outcome. In the English language, words like, _is_, _the_, and  _it_ are considered extraneous. They are words that are used in proper grammar, but they hold no bearing on the meaning of the sentence. As part of preprocessing or cleaning data for NLP, it's important to remove these words so that unnecessary bias doesn't weigh our model down. NLTK has built-in lists of stopwords in multiple languages and provides methods for extracting these words simply.
<blockquote>
<details><summary>Examples of Stopwords:</summary><br>

We can view the built-in list of English stopwords like this:

![stopwords_english](Images/stopwords_english.PNG)

Similarly, you can invoke other languages. For example, here we look at French stopwords:

![stopwords_french](Images/stopwords_french.PNG)
</details>
<details><summary>Usage:</summary><br>

Once we have our stopwords, we can remove them using a for loop. First, we store our stopwords as a set in a variable. The `set` data structure creates an unordered list with duplicates removed. Sets make it easy to compare the contents of lists to find their differences:

```python
sw = set(stopwords.words('english'))
```
We can then run a for loop with this list to remove the stopwords:

![sentence_stopwords](Images/sentence_sw.PNG)

</details>
<details><summary>Custom Stopwords:</summary><br>

In certain cases, we may have additional words we need to remove. Let's suppose the words `Dylan` and `Eli` are not necessary for our NLP work, and we wish to add them to our stopwords. We can add these words to our stopwords list as follows:

```python
sw = set(stopwords.words('english'))
updated_sw = sw.union({'Dylan', 'Eli'})
```
We can then run a for loop with this new list to remove the stopwords, which now include `Dylan` and `Eli`. As you can see in our output, this was successful:

![sentence_stopwords](Images/sentence_new_sw.PNG)
</details>
</blockquote><br>
</details>

<details>
<summary>What is Regex and how is it used?</summary><br>

<blockquote>
<details>
<summary>What it is:</summary><br>

Regex stands for *regular expression*, and it allows us to search for text using very specific patterns. It can be intimidating at first glance, but it's well worth the little study and persistence required to conquer it, especially in cases of NLP usage. Consider using the find and replace option in your Word processor - it works great for finding specific text, but what if your query is more complex?  Perhaps you are looking for someone's name, and you can only remember that the last name ends with *b*. Regex lets you find that!

</details>

<details>
<summary>How it's used:</summary><br>

Before we tokenize, we use regex to get clean token data. Let's apply regex to the following sentence: *"Dylan and Eli love playing video games. They have lots of favorites."*

First, we import the `re` python module, and compile with the pattern we are searching for. In this case, we are searching for any character that is not a letter. The `^` symbol indicates *not*. `A-Z` and `a-z` indicate any upper or lower case letter, and the empty `space` at the end indicates a `space`. When we compile using `^A-Za-Z `, we are looking for any character that is not an upper or lower case letter, or a space. We then use `.sub` to substitute something new in the place of any matches. In the example below, we are substituting `''` (which is essentially nothing) for any matches, which results in the deletion of that character:

<img src='Images/sentence_regex1.PNG' width=700>

Then we can tokenize our sentence, leaving us with clean token data that has no non-alphanumeric characters:

<img src='Images/sentence_regex2.PNG' width=600>

</details>

<details>
<summary>How to learn more:</summary><br>

Here are some great resources to get you started:

* For a gentle introduction from Python click [here.](https://docs.python.org/3/howto/regex.html#regex-howto)

* For an intro with practice prompts, try [this *Google for Education* module.](https://developers.google.com/edu/python/regular-expressions)

* For a quick glance cheat sheet click [here.](https://www.debuggex.com/cheatsheet/regex/python)

* For hands-on practice click [here](http://play.inginf.units.it/#/) or [here.](https://www.hackerrank.com/domains/regex)

</details>
</blockquote><br>

</details>

<details>
<summary>What is Lemmatization and why do I need it?</summary><br>

Lemmatization is the process of decomposing a word to its root; for example, the lemmatized word *busiest* would have a root of *busy*. NLTK provides in-built functionality for this process. The default for this function is to convert plural nouns to singular, but verbs and adjectives can also be converted. To use the function, we import the module and instantiate the object as follows:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
```

We can then call on the function by using the method `.lemmatize()`. In the following example we will lemmatize the sentence:  *"Dylan and Eli love playing video games. They have lots of favorites."*. The tokenized form of this sentence is as follows:
```python
['dylan',
 'eli',
 'love',
 'playing',
 'video',
 'games',
 '.',
 'lots',
 'favorites',
 '.']
```
To properly lemmatize the `sentence_tokenized` object:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = []
for word in sentence_tokenized:
    word = lemmatizer.lemmatize(word)
    result.append(word)
```
You can see in the following image, that compared to the original output, the new output has converted all plural words to singular:

<img src = 'Images/lemmatize_sentence.png' width = 400>

A more concise way to generate this new list is with a list comprehension. The results are the same:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = [lemmatizer.lemmatize(word) for word in sentence_tokenized]
```
</details>

<details>
<summary>What are N-grams and why do I need them?</summary><br>

<blockquote>
<details>
<summary>What they are:</summary><br>

Ngrams are word groupings that are grouped by **N** number of words. For example, let's use part of our original sentence object: *Dylan and Eli love playing video games.* If we grouped this sentence into bigrams (groups of 2 words), the division would be:

*Dylan and*,<br>
*and Eli*,<br>
*Eli love*,<br>
*love playing*,<br>
*playing video*,<br>
*video games.*<br>

</details>
<details>
<summary>How to find them programmatically:</summary><br>

To get the ngram count of a text using NLTK, we must first tokenize our text using `word_tokenizer`:

Input:
```python
from nltk.tokenize import word_tokenize

sentence = 'Dylan and Eli love playing video games.'
sentence = word_tokenize(sentence)
print(sentence)
```

Output:
```python
['Dylan',
 'and',
 'Eli',
 'love',
 'playing',
 'video',
 'games',
 '.']
```

We can then use NLTK to work with ngrams as follows:

Input:
```python
from nltk.util import ngrams
from collections import Counter

Counter(ngrams(sentence, n=2))
```
Output:
```python
Counter({('Dylan', 'and'): 1,
         ('and', 'Eli'): 1,
         ('Eli', 'love'): 1,
         ('love', 'playing'): 1,
         ('playing', 'video'): 1,
         ('video', 'games'): 1,
         ('games', '.'): 1,
```

The output is a dictionary of values that hold our two word combinations and the number of times those two words appear together.
</details>
<details>
<summary>Why they're important:</summary><br>

Ngrams give NLP models more predictive power by revealing the context of words through analysis of their patterns. Humans innately understand the context of language by processing a sentence as we hear it.  We can tell by tone and inflection if the statement is a question or exclamation, and we can tell by word placement if a statement is positive or negative.  Ngrams give computers a similar ability by looking at groups of words. For example, let's use the following sentence: *Let's hammer out the details.*. The bigrams for the sentence are:

*Let's hammer*,<br>
*hammer out*,<br>
*out the*,<br>
*the details*<br>

Ngrams give context to this statement by looking at how the meaning changes when words are grouped in certain ways. The word *hammer* in this instance has bigrams of *Let's hammer* and *hammer out*.  The words *Let's* and *out* gives context that *hammer* in this instance is being used as a verb. The bigrams *hammer out* and *the details* might also tell our model that the word *hammer* is not being used literally, but rather in a context of clarification.

If instead, our sentence was *I need the hammer*, then having the word *the* preceding the word *hammer* will give the context that hammer in this case is a noun.  Were the sentence *Let's hammer out the details...not!*, then the word *not* would negate the sentence and also hint at sarcasm.  Both examples show how a slight change in pattern and word order can alter the entire context of a sentence.  Ngrams help models pick up on these cues.





</details>
</blockquote><br>

</details>

<details>
<summary>What is a corpus?</summary><br>

In linguistics and NLP, _corpus_ refers to a collection of texts that may be formed of a single language of texts or can span multiple languages. It can be thought of as a dataset that is specific to NLP tasks. Corpora are vital for NLP, as they are used for benchmarking a model's performance, NLP testing, and because effective NLP requires large quantities of text-based data that include as many words as possible. The larger the corpus (dataset), the more likely low-frequency words are to be included in the text.

There are numerous well-known corpora used in NLP, some are general for language-based applications, and some are more specialized for task-specific applications. For example, when working on sentiment analysis projects, you could use the IMDB Reviews or Yelp Reviews corpora.

For more info on corpora, how they work in NLP and where you can find corpora to use in your own projects click [here.](https://devopedia.org/text-corpus-for-nlp)

</details>

<details>
<summary>What is TF-IDF?</summary><br>

Term Frequency * Inverse Document Frequency, or TF-IDF for short, is a weighting factor intended to measure how important a word is to a document in a corpus. It is calculated by combining the Term Frequency (TF) and the Inverse Document Frequency (IDF) to get a weighted value.

Term frequency (TF) is the count of the word in a document of the corpus. Inverse document frequency (IDF) is the number of documents the word appears in throughout the corpus. An increase in TF will make the TF-IDF score go higher, because the more often a word is counted, it can be considered to be more relevant. An increase in IDF will make the TF-IDF score go lower, because the more often a word appears throughout all the documents, it is considered more common and irrelevant.

The higher the TF-IDF score, the more common the word, the lower the TF-IDF score, the more unique (relevant) the word.
<blockquote>

For example:

If the word ***play*** appears **500** times in my **10,000** word document then the TF is high:  **`500 / 10,000 = 0.05`**.

If I have **10,000** documents and ***video*** only appears in **10** of them, then IDF is low: **`LOG(10,000 / 10) = 3`**

In this example, the TF-IDF is: **`0.05 * 3 = 0.15`**.

In the following list of words with TF-IDF values, the word *games* has the highest score, meaning it is a more relevant word than *play* or *video*.

|Word|TF-IDF|
| :----: | :----: |
|*play*|0.15|
|*video*|0.32|
|*games*|0.47|

</blockquote><br>
</details>

<details>
<summary>What is the difference between NLTK and spaCy?</summary><br>

The primary difference between NLTK and spaCy is that NLTK uses a rule-based approach, and spaCy uses a statistical-based approach.

With a rule-based approach, the model deterministically draws conclusions from the text using the rules of the selected language. With NLTK, the word *sick* is negative based on rules that dictate that relationship. With a statistical approach, machine learning can be used to make decisions using the context of the text. SpaCy might notice that the word *sick* is used in a context that implies a positive relationship; for example, *That steak was grilled to perfection! It was sick!*

Additionally, NLTK was built with research and education in mind. It's a great resource for exploring your text data and conducting analyses; however, all data is represented as strings, which can make it more difficult to work with on a larger scale. SpaCy was built with production performance in mind and tends to be faster than NLTK. All data with SpaCy are represented as objects, and more task-based functionality is provided.

</details>
<details>
<summary>What is the difference between POS Tagging and Dependency Parsing?</summary><br>

Part of speech tagging (POS tagging) is the process of labeling each word or token in a sentence as its part of speech (noun, verb, adjective), while dependency parsing takes those words and determines the relationships between each. Dependency parsing is the step that comes after POS tagging.

If we were to POS tag and dependency parse the following sentence:
`'Dylan and Eli love video games.'`, the results would look like this:
<img src='Images/sentence_dependencies.PNG' width = 900>

</details>

# Unit 13: AWS-Cloud

### Helpful Links

* For an simple explanation of how k-means works, click [here.](https://www.youtube.com/watch?v=4b5d3muPQmA)

* Click [here](https://www.youtube.com/watch?v=FgakZw6K1QQ) for an easy to understand video on how PCA works.

* Click [here](https://d1.awsstatic.com/whitepapers/aws-overview.pdf) for a thorough whitepaper from Amazon Web Services describing what cloud computing is and what role their tools play.

* If you're wondering how all the AWS services can work together in a real-world scenario, the video series [*This is My Architecture*](https://aws.amazon.com/this-is-my-architecture/?tma.sort-by=item.additionalFields.airDate&tma.sort-order=desc) is a great place to start. Each video provides a 5 - 10 minute interview with a real company, where they explain their actual workflow using AWS services.

* A great FAQ for AWS IAM Resources is located [here.](https://aws.amazon.com/iam/faqs/)

* For an easy to understand SageMaker Deep Dive video series, click [here.](https://www.youtube.com/playlist?list=PLhr1KZpdzukcOr_6j_zmSrvYnLUtgqsZz)

* [This](https://docs.aws.amazon.com/lex/latest/dg/examples.html) guide from AWS is a handy reference for Lex bot deployments.

* For AWS examples of Lex bots click [here.](https://docs.aws.amazon.com/lex/latest/dg/examples.html)

---

### Additional Course Resources

* [Creating and Activating an AWS Account](1-Create-and-Activate-an-AWS-Account.md)

* [AWS Free Tier Info](AWS-Free-Tier.md)

* [Deloitte Chat Bot Guide](deloitte-nl-fsi-chatbots-adopting-the-power-of-conversational-ux.pdf)

---

### Unit 13 FAQs

<details>
<summary>What is the difference between supervised learning and unsupervised learning?</summary><br>
<blockquote>
<details>
<summary>Supervised Learning</summary><br>

Supervised machine learning uses labeled data with input variables (feature data) and output variables (target data) and uses the feature data to predict the target data. Because the data is labeled, the outcome is known. This data can be fed to the model, and if the model guesses incorrectly, the error can be used to fine tune the model until it makes highly accurate guesses.<br>

An example of this is using tuning forks to tune a piano. Tuning forks produce very precise tones. These tones are your known output. You can press a piano key and compare the piano's tone (model output) to the tuning fork (known y value). If the piano's tone is too low then you can tighten the piano wire to make the piano better at matching the tuning fork. This process of adjusting the model to make the output match the known output is essentially supervised learning.
<br>
</details>
<details>
<summary>Unsupervised Learning</summary><br>

Unsupervised learning models are given only input variables and must work to make connections to the data without predicting a labeled target. These types of models are often clustering models that uncover connections in the data and group all the features into classes accordingly.<br>
<br>
An example of unsupervised learning would be to use website purchase data to group customers into two classes based on their spending habits. This clustering might reveal that class 1 more spends more with a coupon incentive, while class 2 spends more on targeted advertising on social media.
</details>

</blockquote>
</details>
<details>
<summary>How is Training and Testing Data Utilized?</summary><br>

When working with models, data is divided into training and testing sets. The training set is used to teach (supervise!) the model so it learns how the input data is connected to the output data and can make predictions. The testing data set is used to validate how well the model performs on data it has not seen before, by running the model on the testing feature data, and comparing it's predictions to the testing target data.<br>

</details>

<details>
<summary>What is KMeans?</summary><br>

<blockquote>
<details>
<summary>What it is:</summary><br>

K-means is a popular unsupervised machine learning algorithm  for clustering data. It attempts to divide the data up into a number of clusters referred to as `k`. It can then compare a new data point to the centers of these existing clusters to see which cluster the new point is closest to. The new point can then be labeled as belonging to that closest data cluster.

![k-means](Images/k-means.gif)


The following video from StatQuest on YouTube provides an excellent, easy to understand explanation of the process: [K-means Clustering.](https://www.youtube.com/watch?v=4b5d3muPQmA)
</details>

<details>
<summary>How do you determine the `k` number of clusters?</summary><br>

There are several ways to deterimine the best number of clusters for your model. For our class, we use the elbow method. The elbow method takes into account a range of values for `k` and plots their inertia, inertia being how far the clusters expand from the centroid. This number should be as low as possible, while still encompassing an adequate nubmer of clusters. The lower number indicates tightly packed clusters. When these values are plotted on a line chart, a bend should form where the optimal value of `k` is located. This bend incates the point at which adding clusters does not greatly improve the inertia, thus the smallest amount of clusters with the best inertia.

In the below elbow chart, the bend occurs at 3, meaning this is the optimal value for `k` for this example:

![elbow chart](Images/elbow_chart.png)
</details>

<details>
<summary>How to use the code:</summary><br>

The elbow chart can be plotted as follows:

```python
import pandas as pd
from sklearn.cluster import KMeans

inertia = []
k = list(range(1, 11))
# Looking for the best k
for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(df_iris)
    inertia.append(km.inertia_)
    elbow_data = {
  "k": k,
  "inertia": inertia
}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.plot(x="k", y="inertia", title="Elbow Curve", xticks=k)
```
Once you have the number for `k`, you can call the Kmeans function and set the `n_clusters` to your `k` value as follows:

```python
model = KMeans(n_clusters=3, random_state=5)
model.fit(your_df)
```

</details>

</blockquote>
</details>

<details>
<summary>What is Principal Component Analysis and when should I use it?</summary><br>

Principal Component Analysis (PCA) is a statistical method of dimensionality reduction that can reduce the features of your data set, while still keep the majority of the pertinent information. The variables in your dataset are replaced with the principal component variables, which are essentially a recombination of the initial information that represents the most important data. PCA can be used when the dataset is quite large and reducing the features would speed up the machine learning model. It can also be used to plot your data when there are too many features to feasibly plot. For a great video on how this process actually works, click [here](https://www.youtube.com/watch?v=FgakZw6K1QQ)

PCA can be imported from sci-kit learn as follows:

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
new_data_pca = pca.fit_transform(old_data)
```

</details>
<details>
<summary>What is the cloud?</summary><br>

The cloud is an abstract term for accessing computing power online from a machine other than your own. When you save files to the cloud, it really just means you're saving your files on a machine (server) located somewhere else, but that can be accessed anywhere via the internet. These servers are located on server farms where thousands of computers are operating simultaneously to provide computing services via *"the cloud"*.

Storage such as Google Drive is a popular cloud computing product, but there are many others. Amazon Web Services (AWS) currently provides over 175 services on the cloud. Examples include; Sagemaker - which allows you to run juypter notebooks on the cloud, Lex - which allows you build conversational interfaces (chatbots) and run them in the cloud, and Relational Database Service (RDS), which allows you to connect to a database via the cloud.

For a full list of AWS services click [here.](https://aws.amazon.com/products/)

<blockquote>
<details>
<summary>Types of cloud services:</summary><br>

Cloud services can be divided into 4 general categories:

**Infrastructure as a service (IaaS):** Online services that provide APIs to access different infrastructures such as servers, virtual machines, storage, load balancers, or network interfaces (e.g., [Azure Virtual Machines](https://azure.microsoft.com/en-us/services/virtual-machines/)).

**Platform as a service (PaaS):** Provides a platform that allow customers to develop, run, and manage applications without the complexity of building and maintaining their own physical infrastructure (e.g., [Amazon Web Services](https://aws.amazon.com/)).

**Software as a service (SaaS):** Refers to a software licensing and delivery model where software is licensed on a subscription basis and is centrally hosted (e.g., [Microsoft Office 365](https://www.office.com/)).

**Function/code as a service (FaaS):** Also known as serverless computing, it offers a remote procedure call that enables the deployment of individual functions in the cloud that run in response to events (e.g., [AWS Lambda](https://aws.amazon.com/lambda/)).

</details>
</blockquote>
</details>


<details>
<summary>What is AWS?</summary><br>

AWS is a cloud computing platform provided by Amazon, offering over 175 different services via the cloud. AWS is trusted by large companies and individual users alike to provide scalable, flexible computing power that is both cost effective and secure. You might be surprised to know that many companies, including Netflix, use AWS for all their tech needs, including database and storage.

Because the infrastructure is already in place, companies can easily scale up as needed without a huge up-front investment, and because they offer flexible usage options there is a cost appropriate option for everyone.

</details>

<details>
<summary>What is an IAM Role?</summary><br>

AWS Identity and Access Management (IAM) allows you to securely control the acces of others to your AWS resources. By creating an IAM User you are granting others secure access to your account without actually giving them your password. After creating the user, a role can be assigned to the user that defines and resticts that access as you wish. An IAM role defines *who* can do *what* to your AWS resources, and *when* they can do it. [This](https://aws.amazon.com/iam/faqs/) document from AWS contains some great frequently asked questions about the IAM service.

</details>

<details>
<summary>What are S3 buckets?</summary><br>

Simple Storage Service, or S3 as its commonly known, is one of the most popular AWS services and was also one of first to be introduced, launching back in 2006. S3 offers secure object storage in the cloud for anything from csv files to images and can be scaled as needed. S3 can be used for anything from simple image hosting for your website, to connecting to data directly for database applications or analytics.

Much like using virtual file folders on your own machine to store and organize your files, an S3 bucket is simply where your objects are stored on S3.

</details>
<details>
<summary>What is Boto3?</summary><br>

Boto3 is considered a Software Development Kit (SDK) for AWS. SDKs are similar to Application Programming Interfaces (APIs) in that they both allow the user to interact with a platform, however SDKs are built to interact with a specific platform, where APIs are typically used to allow platforms to interact with each other. Boto3 allows Python developers to work with various AWS resources outside of the AWS console, by programming those resources with code.

A popular application of Boto3 is working with the contents of S3 buckets. Boto3 is used to access those contents via Python code, and then you can manipulate the contents as you normally would - for example you might use Boto3 inside a Jupyter Notebook to load CSVs from an S3 bucket and then proceed to work with those CSVs with Pandas.

The [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is a great starting point for working with this SDK. It describes the usage of the SDK and provides tutorials for implementing it with various AWS resources.

</details>
<details>
<summary>What is Sagemaker?</summary><br>

When it comes to Amazon Sagemaker - think Jupyter Notebook for Machine Learning!  Amazon Sagemaker is a fully managed machine learning IDE, which is essentially a cloud instance of Jupyter Notebook, optimized for machine learning purposes. Each Sagemaker instance can connect to your data in the cloud via S3 buckets or your preferred storage. The instance is pre-loaded with commonly used machine learning algorithms such as XGBoost and K-means, and can automatically hypertune them, making it easy to train and test your data, as well as get powerful predictions.

The ability to deploy machine learning models in the cloud is very important for many models, for example recommendation models that are gathering your viewing data on Amazon while you shop and then making recommendations to you. Models like that need to be deployed and active constantly to be effective. Sagemaker has built-in components that allow for easy deployment of your model via endpoints, which allow for real time use based on real time user input and data.

AWS has several great resources to learn more about Sagemaker.

For a real world application nusing AWS workflows check out [this](https://www.youtube.com/watch?v=gYXqv1UxW3Y) video. They also have an informative Sagemaker blog [here](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/sagemaker/) and an easy to understand Sagemaker Deep Dive video series [here](https://www.youtube.com/playlist?list=PLhr1KZpdzukcOr_6j_zmSrvYnLUtgqsZz).

Additionally the AWS Sagemaker SDK docs are a great place to take your own deep dive: [Sagemaker SDK Docs.](https://sagemaker.readthedocs.io/en/stable/)

</details>


<details>
<summary>What is Amazon Lex?</summary><br>

To understand Amazon Lex, its important to first understand what a conversational user interface is. A conversational user interface - commonly known as a chatbot - is an application that allows human-like interaction with computers. Rather than just point and click, we can now communicate with computers using human langauge.

Though the idea of conversational user interfaces has been around for a very long time - think *Space Odyssey: 2001* and *HAL* - its only been in the recent past that NLP technology has become advanced enough to make practical applications of the tech a reality. In fact, conversational AI has become so advanced that it can update in real time and change its responses to adapt to the conversation as it unfolds.

Amazon Lex allows you to develop your own chatbots, harnessing the same tech that Amazon's Alexa uses, resulting in a powerfully accurate, state-of-the-art conversation interface that can be deployed to almost any platform, including Facebook Messenger and Slack. And, like most AWS services, its fully managed, so it scales on its own. So as users increase, there is no need to scale up - the infrastructure is already in place. You just pay for what you use. To learn more about Amazon Lex, check out their informative [FAQ](https://aws.amazon.com/lex/faqs/?nc=sn&loc=6). To get more information on deploying your own converational user interface using Lex, check out our [deployment guide](Deploying-Lex-Bot-to-Slack.md) and the AWS Lex examples provided [here.](https://docs.aws.amazon.com/lex/latest/dg/examples.html)

</details>

---
# Unit 14: Deep Learning

## RNN LSTM for Time Series

* [How to Develop LSTM Models for Time Series Forecasting](https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/)

* [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)

## RNN LSTM for NLP

* [How to Use Word Embedding Layers for Deep Learning with Keras](https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/)

* [How does Keras 'Embedding' layer work?](https://stats.stackexchange.com/questions/270546/how-does-keras-embedding-layer-work)

* [tf.keras.layers.Embedding](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding?version=stable)

* [Text classification with preprocessed text: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification)

* [Understanding LSTM and a Quick Implementation for Sentiment Analysis in Keras](https://towardsdatascience.com/understanding-lstm-and-its-quick-implementation-in-keras-for-sentiment-analysis-af410fd85b47)

* [Research paper: Learning Word Vectors for Sentiment Analysis](http://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf)

* [Research paper: Financial Sentiment Lexicon Analysis](https://www.researchgate.net/publication/324957692_Financial_Sentiment_Lexicon_Analysis)

* [Research paper: Comparative Study of Sentiment Analysis with Product Reviews Using Machine Learning and Lexicon-Based Approaches](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1051&context=datasciencereview)

* [Research paper: Comparison of VADER and LSTM for Sentiment Analysis](https://www.ijrte.org/wp-content/uploads/papers/v7i6s/F03040376S19.pdf)

* [Research paper: Application of Sentiment Lexicons on Movies Transcripts to Detect Violence in Videos](https://thesai.org/Downloads/Volume10No2/Paper_47-Application_of_Sentiment_Lexicons_on_Movies.pdf)

## Tuning RNN LSTM Models

* [How to use Different Batch Sizes when Training and Predicting with LSTMs](https://machinelearningmastery.com/use-different-batch-sizes-training-predicting-python-keras/)

* [How to Tune LSTM Hyperparameters with Keras for Time Series Forecasting](https://machinelearningmastery.com/tune-lstm-hyperparameters-keras-time-series-forecasting/)

## ROC Curve and AUC

* [Understanding AUC - ROC Curve](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)

* [Classification: ROC Curve and AUC - Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

* [Sci-kit learn roc_curve documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)

### Unit 14 FAQs

<details>
<summary>What are Neural Networks and what does the Perceptron have to do with it?</summary><br>

Neural networks are a set of algorithms that are modeled after the human brain - essentially a network of artificial neurons designed to recognize patterns and interpret sensory data through machine perception, labeling, or by clustering raw input. Neural networks complete this task with layers of neurons. Data goes into a layer, where mathematical computation is completed, then those results are fed into the next layer.

The original neural network and building block for modern neural networks is the perceptron. The perceptron is essentially a single neural network unit or neuron. Created by Frank Rosenblatt in 1958 and further developed in 1969 by Marvin Minsky and Seymour Papert, it's the most basic model of an artificial neuron, taking inputs, applying weights, and calculating a binary-weighted sum prediction. Neural networks are composed of groups of these neurons, called layers.

![perceptron](Images/harsh_perceptron.png)

</details>

<details>
<summary>Are Neural Networks considered supervised learning or unsupervised learning?</summary><br>
Neural networks can fall into both categories! Neural networks can run unsupervised learning jobs such as mapping out patterns in text for NLP, or for clustering algorithms. They can also be used for supervised learning jobs such as image classification and object detection.<br>

<br>
<blockquote>
<details>

<summary>Supervised Learning</summary><br>

Supervised machine learning uses labeled data with input variables (feature data) and output variables (target data). It uses the feature data to predict the target data. Because the data is labeled, the outcome is known. This data can be fed to the model, and if the model guesses incorrectly, the error can be used to fine-tune the model until it makes highly accurate guesses.<br>

An example of this is using tuning forks to tune a piano. Tuning forks produce very precise tones. These tones are your known output. You can press a piano key and compare the piano's tone (model output) to the tuning fork (known y value). If the piano's tone is too low, then you can tighten the piano wire to make the piano better at matching the tuning fork. This process of adjusting the model to make the output match the known output is essentially supervised learning.

<br>
</details>
<details>
<summary>Unsupervised Learning</summary><br>
Unsupervised learning models are given only input variables and must work to make connections to the data without predicting a labeled target. These types of models are often clustering models that uncover connections in the data and group all the features into classes accordingly.<br>
<br>
An example of unsupervised learning would be to use website purchase data to group customers into two classes based on their spending habits. This clustering might reveal that class 1 more spends more with a coupon incentive, while class 2 spends more on targeted advertising on social media.
</details>

</blockquote><br>
</details>

<details>
<summary>Why do I need activation, loss, and optimizer functions?</summary><br>

<blockquote>
<details>
<summary>Activation Functions</summary><br>

Activation functions are really just math functions that allow us to adjust the linearity of the model. Data is complex and often has non-linear relationships between the inputs and the outputs. Changing the activation function to non-linear functions like ReLU allow us to build neural networks that can adapt to non-linear data.

Some of the most popular activation functions include sigmoid, tanh, and relu. A full list of activation functions provided by keras can be found [here.](https://keras.io/activations/)
</details>

<details>
<summary>Linear and non-linear data</summary>

Linearity is the property of data that allows it to be visually depicted as a straight line. When plotted, a linear dataset will appear to move in one direction, in a relatively straight line as seen below:

<img src=Images/linear-data.png width=400>

Conversely, a nonlinear dataset will appear to be anything other than a straight line. It might be a bell curve, jagged line or haphazard as seen in the example below:

<img src=Images/non-linear-data.png width=400>

Data points in a linear data set are proportionally separate with constant correlation, whereas non-linear data is disparately proportional with varying correlation.

Linear data is much easier to predict that non-linear data, because the trend is always present, moving in the same direction, however, neural networks are specially equipped to work with non-linear data, due in many parts to non-linear activation functions.

</details>
<details>
<summary>Loss Functions and Optimizers</summary><br>

Loss functions measure how far the model is deviating from the expected result - the higher the number, the more deviation, meaning poor performance. Optimizer functions help the loss functions minimize their error by updating the weights used in the model according to the loss. Optimizer functions fine-tune your model by using the loss function as a guide to keep it moving in the right direction. If the loss is going up, the optimizer needs to readjust the weights.

A simple way to visualize loss functions and optimizers is to picture yourself riding a horse. The horse may start to drift or find its own path, but you can use the reins to guide the horseback to the correct path. In this example, your eyes are the loss function. You can see the correct path, so you know when the model (the horse) starts to drift off course. Loss functions are just telling you how far off your model is from where you want it to be.

The horse reins are like the optimizer. The optimizer is what takes the feedback from the loss function and updates the model to make it better match your desired outcome. For example, if you see (loss function) that the horse is drifting to the right of the correct path (error), you can pull to the left to correct the course (optimizer).

Some popular loss functions include mean squared error (MSE) and categorical cross-entropy. Popular optimizer functions include Adam and Adadelta. A full list of loss functions and optimizer functions provided by Keras can be seen [here](https://keras.io/losses/) and [here,](https://keras.io/optimizers/) respectively.

 A great medium article on the topic can be viewed [here.](https://medium.com/datadriveninvestor/overview-of-different-optimizers-for-neural-networks-e0ed119440c3)

</details>
</blockquote><br>
</details>

<details>
<summary>How do I choose the best activation, loss and optimizer functions?</summary><br>

Choosing the right function for your model is a great opportunity to have some fun with your code through experimentation! Building neural networks is part science and part art, so choosing these functions is typically the result of much testing with different options to find the best result.

</details>

<details>
<summary>What is a Deep Neural Network?</summary><br>

Deep Neural Networks are neural networks that have more than one hidden layer. One can visualize this by thinking of a network of connected perceptrons, or a multi-layer perceptron. With Deep Neural Networks, there is an input layer and an output layer, but between the two are multiple hidden layers running sophisticated computations to produce more refined output. A layer is a set of neurons and is visualized by showing a column of those neurons and how they feed into the next column - or layer. Below is an image of a basic deep neural network, they can be, and often are, much more complex. To visualize even more types of deep neural nets and their structures, visit the [Tensorflow Playground.](https://playground.tensorflow.org/)


![deep net](Images/nnet.png)

</details>

<details>
<summary>What is difference in Recurrent Neural Networks (RNNs) and Long-Short-Term Memory Recurrent Neural Networks (LSTM-RNNs)?</summary><br>

A Recurrent neural network (RNN) is a type of deep neural network that can remember the past and update its results based on that information. RNNs are called recurrent, because they cycle the information they receive through the layers more than once, effectively accessing their 'memory' to update their decisions based on the past. This is the opposite of standard Articifical Neural Networks (ANNs) that utilize a feedforward method where the inputs are passed through each layer only once, in a unilateral direction, and then outputted.

While RNNs do well with short sequences of data, they can be overwhelmed and struggle to learn long sequences. This is because they have no way to sort out what information is important and what information isn't important over long periods of time. For example, suppose you wanted to build a machine learning model that could predict when you would want a snack. What you had for breakfast this morning may impact your hunger level for the day, but what you ate for breakfast 3 years ago may no longer be relevant to predicting today's snack time. This can pose an issue for scenarios such as time series analysis on large time windows.

LSTM-RNN can help resolve this problem by practicing a more expansive yet more selective memory. The LSTM-RNN can predict which values are ok to forget and which it needs to hold on to so that longer time windows can be analyzed.

</details>

<details>
<summary>How are Neural Networks constructed using Keras?</summary><br>

Using Keras makes building Neural Networks relatively simple. In the following example, we'll build a simple deep neural network. We begin by importing the models needed to run the algorithms.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
```

Next we define our model by instantiating the `Sequential()` object, then we add our first hidden layer by calling the `.add()` method on our model object and inserting a `Dense()` layer with the proper variables:

```python
model = Sequential()
model.add(Dense(units=10, input_dim=5, activation='relu'))
```
In the above code snippet, we added '5' neurons to the hidden layer via the `units` parameter. We also gave `5` to our `input_dim` parameter and assigned the activation function `relu` to our `activation` parameter. The `input_dim` is always the starting number of inputs. The `units` parameter can vary.

In the below code snippet, we add a second hidden layer to the model, making this a deep neural network - notice we do not have to resupply the `input_dim`:

```python
model.add(Dense(units=15, activation='relu'))
```

Next, the output layer is added - notice we can specify a different activation function if we choose, and that the `units` are specified as `1` this time because this is the output layer, where a final prediction will be generated:

```python
model.add(Dense(units=1, activation="linear"))
```
Now that the model is built, a summary can be displayed by accessing the `.summary` method on the model as follows:

<img src=Images/model_summary.PNG width=475>

To continue the process, the model is compiled and fit to the data (trained). To compile the model we run `.compile()` on our model and specify a loss function, an optimizer, and also a metrics output to measure the accuracy. To fit the model, we run `.fit()`, providing the feature and target data, the data split to make validation results on, and the number of epochs. Remember, epochs is just another way of saying iterations, or the number of times we run the training:

```python
model.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])
model.fit(X, y, validation_split=0.3, epochs=200)
```
Depending on the loss function and metrics designated, the output of fitting the model will resemble the following:

<img src=Images/epochs.PNG width=500>

To use the model to make predictions you can call `.predict()` on scaled feature data as follows:

```python
predictions = model.predict(X_test_scaled)
```
</details>

<details>
<summary>What are ROC curve and AUC?</summary><br>

The ROC curve and AUC are used to visualize the performance of a classification model. ROC stands for Receiver Operating Characteristic, and AUC stands for Area Under the ROC Curve. The two methods are combined onto a single chart to produce the visualization.

The Roc Curve, on its own, shows how the model performed by measuring the recall (See below for a quick refresher on recall) and false positive rate (FPR). A ROC curve is seen in the below image:

<img src=Images/roc-curve.png width = 350>

Because interpreting the ROC Curve is difficult, the AUC calculation comes into play. The AUC measures the area that falls under the curve on a scale of 0 to 1. If the model is 100% wrong, then the AUC is 0. If the model is 100% right, then the AUC is 1. An example of this final visualization is seen in the below image:

![ROC/AUC](Images/roc-curve-rnn-lstm.png)

<blockquote>
<details>
<summary><strong>Recall</strong></summary>
Recall is the measurement of how many times a value was predicted and was also incorrect. For example, if our model was predicting colors - blue, green, and purple, recall would be the measurement of how many times green was predicted incorrectly.

The formula for recall is TP / (TP + FN).

</details>
</blockquote><br>
</details>


<details>
<summary>How is Training and Testing Data Utilized?</summary><br>

When working with models, data is divided into training and testing sets. The training set is used to teach (supervise!) the model, so it learns how the input data is connected to the output data and can make predictions. The testing data set is used to validate how well the model performs on data it has not seen before, by running the model on the testing feature data, and comparing it's predictions to the testing target data.<br>

</details>
<details>
<summary>How does `train_test_split()` work?</summary><br>

The `train_test_split()` function makes splitting data for testing easy! The function outputs four sets of data points - two sets each of target and feature data where one set is for training, and one set is for testing. This is why the variables that define the function are typically `X_train, X_test, y_train, y_test`. The most important parameters of the function are the `X` and `y`. During preprocessing, we separate our data into the feature data, or `X`, and the target data - `y`.

The `y` data are the values we wish to predict, and the `X` data are the values we use to influence our predictions. If our data is stored in a DataFrame, we just break it out and store it in variables. The values we wish to predict are stored as `y` and the features we are using to make our predictions are stored as `X`. We then feed these into the `train_test_split()` function.

Other parameters include: `stratify`, `test_size`, `train_size`, `random_state`, and `shuffle`.

If the `y` values consist of binary data (for example, male/female), and 25% of those values are male, and 75% of those values are female, then setting the `stratify` parameter to `y` will ensure the test and train data have the same ratio of male to female as the entire data set.

The specific `test_size` and `train_size` can also be set to override the default sizes. The default for these parameters will select sizes that complement the data set. The defaults can be overridden using either `int` or `float` values. If the parameter is set to `int`, then this will indicate a specific sample size you wish to include in the test or train set. If the parameter is set to `float` then it will indicate a percentage of the total dataset you wish to include in the test or train set.

When using the `shuffle` parameter, the data is shuffled (randomized) prior to being divided into train and test sets.

When using this function, the data is split each time randomly; however, if the `random_state` parameter is set, the same random split will be selected each time. To use this parameter, any number can be used as the `random_state` as long as it is used each time you run the model. Using this parameter will always ensure the same split is obtained even if `shuffle` is set to `True`.

An example of implementing a `train_test_split()` instance is as follows:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, shuffle=True)
```

</details>


<details>
<summary>How do you preprocess data for neural networks?</summary><br>

Preprocessing data for neural networks involves converting categorical data to numerical and scaling numerical data with high variance. Categorical data is text-based and must be converted to numerical so that computations can be ran. Numerical data with high variance can inadvertently introduce bias to the model.

<blockquote>
<details>
<summary>Preprocessing Categorical Data</summary><br>

Using `OneHotEncoder()` from scikit-learn, we can convert categorical data to numerical. We begin with a simple DataFrame showing 6 countries:

![country_df1](Images/country_df1.PNG)

Then we import `OneHotEncoder` from sklearn.preprocessing, after which we instantiate the `OneHotEncoder()` object, then run a `.fit()` followed by `.transform()`. The results are stored in a new variable `encoded_y`.

Now you can see that the encoded values are numerical representations of the original countries:

<img src= Images/OneHotEncode.PNG width = 400>

</details>


<details>
<summary>Scaling Feature Data</summary><br>
In an effort to avoid introducing bias to the model, we should scale data that have large numerical variance between features, so that all features are weighted the same. For example, let's suppose that our country DataFrame also includes an average number of children, average life expectancy, and average salary by country. The average number of children is a very small number compared to average life expectancy, which is a very small number compared to the average salary by country. These values vary greatly and need to be scaled, because the higher numbers may result in more weight bias.

![country_df4](Images/country_df4.PNG)

Using the `StandardScaler()` from scikit-learn, we will scale the data. First we instantiate the `.StandardScaler()` instance, then fit it to the data, then transform the data and show it in a new DataFrame:

```python
data_scaler = StandardScaler()
data_scaler.fit(df)
data_scaled = data_scaler.transform(df)
```
The new DataFrame shows the scaled data in place of the former values. Now all the values are standardized:

![country_df5](Images/country_df5.PNG)

</details>
</blockquote><br>
</details>

<details><summary>
What is .reshape() and why do I have to use it?</summary><br>

When working with Pandas, we often pass Series objects into our model. The shape of values in a Pandas Series object is a 1d array. This has to be converted into a 2d array, which is essentially an array of arrays - or list of lists. This is done using the `.reshape()` function. The matrix values we desire are passed into this function. In the following example, we reshape our list into a 2d array using `.reshape(3,4)`, where 3 is the number of lists, and 4 is the number of values in each list:

![2d_arrayImages](Images/2d_array.PNG)

Many models require the 2d array to be formatted such that each value is in a list by itself. If we were inserting the above sample data into a model, it would be converted using `.reshape(-1,1)`, where -1 indicates an unknown number of rows, and 1 indicates the number of values in each list. The -1 will allow the function to generate the number of rows necessary to hold the data. The output looks like this:

![2d_array_reshape](Images/2d_array_reshape.PNG)

</details>

----

# Unit 15: Algorithmic Trading

### Helpful Links

* For a recorded demo of a trading signal activity from class, click [here.](Activities_walkthrough.md)

---

### Additional Course Resources

* [Asyncio Streamz Installation Guide](Asyncio_Streamz_Install_Guide.md)

* [CCXT Installation Guide](CCXT_Install_Guide.md)

* [Evaluation Metrics Calculations Cheat Sheet](EvaluationsCalculationGuide.md)

---

### Unit 15 FAQs

<details>
<summary>What is Algorithmic Trading and why do I need to understand it?</summary><br>

Algorithmic trading is the trading of stocks using automated computer generated buy/sell decisions. This type of trading is becoming more and more popular in the FinTech world largely because it can be backtested with historical and current data to prove profitability and for its ability to mitigate profit loss due to human error. Some algorithmic trading strategies use the technology to inform their end decisions, while others run on auto-pilot - predicting and executing trades autonomously.

Algorithmic trading bots consist of three components:
- Signals:  Information that is useful for predicting the asset movement (such as performance and evaluation metrics, public sentiment).
- Entry Rules:  A decision rule telling you when to buy an asset (such as when a signal reaches a pre-specified, high enough level).
- Exit Rules:  A decision rule telling you when to sell or dispose of an asset (such as when a signal reaches a pre-specified, low enough level).
</details>
<details>
<summary>What is the difference between technical analysis and fundamental analysis?</summary><br>

The two major schools of thought in trading analysis are technical and fundamental analysis. They are both beneficial techniques used to develop trading strategies, however the methods of each are quite different.
<blockquote>

<details>
<summary>Technical Analysis</summary><br>

Technical analysis is used to determine the value of a stock based only on the patterns and trends in its price movements and volume. Examples of technical analysis methods are Moving Averages and Bollinger Bands. Technical analysts look for known patterns in the trend lines these methods produce, such as pennants, flags and wedges. Using these patterns, they attempt to predict the stock's future movements. For an overview list of technical indicator patterns, check out [this](https://www.investopedia.com/articles/technical/112601.asp) Investopedia article.

<br>
</details>
<details>
<summary>Fundamental Analysis</summary><br>

Fundamental analysis attempts to determine the value of a stock based on qualitative factors like management style and business model, quantitative factors such as balance sheet numbers, and even emotional and subjective factors like public sentiment. Fundamental analysts create complicated mathmatical forecasting models based on these factors, making many assumptions and applying different weights to various factors.

<br>
</details>

</blockquote><br>
</details>

</details>
<details>
<summary>What is the difference between technical indicators and trading signals?</summary><br>

Technical indicators are metrics used to evaluate stock price movements, while trading signals are the point at which those indicators suggest a time to buy or sell. A good trading strategy will utlize both as one plays off the other.

<blockquote>
<details>
<summary>Technical Indicators</summary><br>

Falling under the umbrella of technical analysis, a technical indicator is a data-driven metric that uses trading data such as closing price and volume to analyze the short or long-term price movements occurring over a specified period. For example, a 20-day simple moving average is a technical indicator representing a rolling 20-day mean of a stock's closing prices.

<br>
</details>
<details>
<summary>Trading Signals</summary><br>

A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security (such as a stock) at that point in time.

<br>
</details>

</blockquote><br>
</details>

</details>
<details>
<summary>What is the difference between a long and short strategy?</summary><br>

Both long and short strategies are attempts at profitting off the buying and selling of financial assets, however the methods of profitting are quite different.

A long strategy is perhaps the most simple to understand and the most commonly used. Going long is the classic - *buy low and sell high* strategy most of us are accustomed to when we think of profitting on a sale. To use this strategy the asset is purchased at the lowest price and sold at the highest price, the profit is the difference.

A short strategy is much more difficult to conceptualize. To short a stock or financial asset, is to make a profit off the decline in value, which seems counterintuitive to many of us at first glance. To better understand, let's use an example scenario.
<blockquote><br>

Let's say that Bob owns 100 shares of *World's Best Co. Inc.* and they are each valued at $100, making their total value $10,000.

You've been researching the *World's Best Co. Inc.* and you've found some information that leads you to believe its not really the best after all, and that its stock is well over-valued at $100 per share. You think its overvalued enough that the price is going to tank. You ask to borrow Bob's shares, and he agrees, temporarily transferring ownership of the shares to you (kind of like renting a home is the temporary transfer of many ownership rights). Now that you own the shares, even though it's temporary, you can sell them!  You sell all 100 shares for $100 each for a $10,000 cash injection - Nice job!

Not long after you do this, the price per share does in fact tank - down to $25 per share. You can now buy another 100 shares of the stock yourself on the open market at a total price of $2,500 to replace the borrowed stock you sold. Just in time too, because you are scheduled to return Bob's 100 shares to him tomorrow per your contract agreement!  You transfer all 100 shares of stock back to Bob, while keeping the $7,500 profit you made on the sale!

You may wonder, what's in it for Bob?  Don't worry - Bob will you charge you interest and fees on the renting of his stock, after all, its a risk to him to rent it out in case you don't return it. But this is one of many reasons why shorting a stock can be both risky and profitable.<br>
<br>

</blockquote><br>
</details>
<details>
<summary>How do I use a Dual Moving Average Crossover?</summary>
<font size = "2">

_For ease of explanation, this example will use a **long strategy**. For a refresher on the difference between **long and short strategies**, see the above section on **_long/short strategy_** in this FAQ._</font>

<blockquote>
<details>
<summary>What it is:</summary><br>
The dual moving average crossover utilizes short and long term simple moving averages. When these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other. The value at the time of the crossover is considered the crossover point - a type of technical indicator.
<br>
Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!
<br>

<br>
</details>
<details>
<summary>How to use it:</summary><br>

If the short-term moving average line goes above the long-term moving average line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the short-term moving average line dips below the long-term moving average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the dual moving average lines and the crossover points, indicating entry (buy signal) and exit (sell signal) points:

<img src=Images/dual_ma_cross.png width=700><br>
</details>
<details>
<summary>How to create it:</summary><br>

The dual moving average crossover can be created by using Pandas functionality. In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.

<img src=Images/signals_df.PNG width=150>
<blockquote><br>
<details>
<summary>Step One: Signal, STMA, and LTMA Columns</summary><br>

First we initialize a `Signals` column, then create our short and long term moving average columns using the `.rolling()` and `.mean()` methods:

```python
# Set the short window and long windows
short_window = 50
long_window = 100

# Generate the short and long moving averages (50 and 100 days, respectively)
signals_df['Signal'] = 0.0
signals_df['SMA50'] = signals_df['Close'].rolling(window=short_window).mean()
signals_df['SMA100'] = signals_df['Close'].rolling(window=long_window).mean()

signals_df.tail()
```
<img src=Images/signals_df_sma.PNG width=250>
<br>

</details><br>
<details>
<summary>Step Two: Creating the Signal Values</summary><br>

Next we create the signals themselves using `np.where()`. The code begins at the start of the short rolling window because the values prior to that are null. We accomplish this by slicing the column with a colon after the short_window variable: `signals_df[short_window:]`. The complete code loos like this:
```python
# Generate the trading signal (1 or 0) to when the short window is less than the long
# Note: Use 1 when the SMA50 is less than SMA100 and 0 for when it is not.
signals_df["Signal"][short_window:] = np.where(
    signals_df["SMA50"][short_window:] < signals_df["SMA100"][short_window:], 1.0, 0.0
)
```
Don't let the above code confuse you!  It is simply checking if the STMA is smaller than the LTMA and inserted a 1 if it is. A small snippet of the values generated can be seen below:

<img src=Images/signals_df_values.PNG width=350>
</details><br>
<details>
<summary>Step Three: Creating the Entry/Exit Points</summary><br>

The next step is to take the `.diff()` of the `Signals` column and add it to the DataFrame. Remember, `.diff` just subtracts one cell from the previous and provides the difference:

<img src=Images/signals_df_diff.PNG width=350>
</details><br>
<details>
<summary>Step Four: Visualizing the Indicators</summary><br>

Finally, the entry/exit points can be visualized using the following code:
```python
# Visualize exit position relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
    color='red',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize entry position relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
    color='green',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize close price for the investment
security_close = signals_df[['Close']].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize moving averages
moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(xaxis=None)
```
<img src=Images/signals_df_plot.PNG width=800>

</details>
</blockquote><br>
</details>

</blockquote><br>
</details>
</details>
<details>
<summary>How do I create and use Exponential Weighted Moving Average (EWMA) Crossovers?</summary>
<font size = "2">

_For ease of explanation, this example will use a **long strategy**. For a refresher on the difference between **long and short strategies**, see the above section on **_long/short strategy_** in this FAQ._</font>
<blockquote>
<details>
<summary>What it is:</summary><br>

The EWMA crossover works in much the same way as the dual moving average crossover, except instead of a simple moving average, it utilizes short and long term exponentially weighted moving averages. Because the most recent prices are more heavily weighted and because the smaller window has less time included, the short term EWMA is considered a fast moving trend line with more momentum than its long term EWMA counterpart.

These two variables are subsequently referred to as a *fast close* for short term EWMA and a *slow close* for long term EWMA. Much like the dual moving average crossover, when these two trend lines are plotted, they will move in the same direction on the chart and will eventually cross over each other. The value at the time of the crossover is considered the crossover point - a type of technical indicator.<br>

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!

<br>
</details>
<details>
<summary>How to use it:</summary><br>

If the fast close trend line goes above the slow close trend line, the indicator suggests that the price will be rising higher than the historical average in the short term.

If the fast close trend line dips below the slow close trend average line, the indicator suggests that the price will be dropping lower than the historical average in the short term.

In the following candlestick chart for Bitcoin, you can see the exponentially weighted moving average lines and the crossover points, indicating entry (buy signal) and exit (sell signal) points:

<img src=Images/dual_ewma_cross.png width=700><br>
</details>
<details>
<summary>How to create it:</summary><br>

The exponentially weighted moving average crossover can be created by using Pandas functionality. In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices.
```python
import numpy as np
import Pandas as pd
import hvplot.Pandas
from pathlib import Path
```
<img src=Images/signals_ewm_df.PNG width=150>
<blockquote><br>
<details>
<summary>Step One: Signal, Fast_Close, and Slow_Close Columns</summary><br>

First we initialize a `Signal` column, then create our short and long term moving average columns using the `.ewm()` and `.mean()` methods:

```python
# Set the short window and long windows
fast_close = 1
slow_close = 10

# Generate the fast and slow close exponentially weighted moving averages (1 and 10 days, respectively)
signals_df['Fast_Close'] = signals_df['Close'].ewm(halflife=short_window).mean()
signals_df['Slow_Close'] = signals_df['Close'].ewm(halflife=long_window).mean()
signals_df['Signal'] = 0.0

signals_df.tail()
```
<img src=Images/signals_df_ema.PNG width=250>
<br>

</details><br>
<details>
<summary>Step Two: Creating the Signal Values</summary><br>

Next we create the signals themselves using `np.where()`. The code begins at the start of the fast_close window because the values prior to that are null. We accomplish this by slicing the column with a colon after the short_window variable: `signals_df[short_window:]`. The complete code looks like this:
```python
# Generate the trading signal (1 or 0) to when the fast_close is less than the slow_close
# Note: Use 1 when the fast_close is less than the slow_close and 0 for when it is not.
signals_df["Signal"][short_window:] = np.where(
    signals_df["fast_close"][short_window:] < signals_df["slow_close"][short_window:], 1.0, 0.0
)
```
Don't let the above code confuse you!  It is simply checking if the fast close price is smaller than the slow close price and inserting a 1 if it is.

</details><br>
<details>
<summary>Step Three: Creating the Entry/Exit Points</summary><br>

The next step is to take the `.diff()` of the `Signals` column and add it to the DataFrame. Remember, `.diff` just subtracts one cell from the previous and provides the difference:

<img src=Images/signals_df_ewm_diff.PNG width=350>
</details><br>
<details>
<summary>Step Four: Visualizing the Indicators</summary><br>

Finally, the entry/exit points can be visualized using the code below. You'll notice there are many more entry/exit points than with the DMAC. This is because (in this case) the exponentially weighted moving averages uses shorter windows (1 and 10 days, versus 50 and 100), which causes the signals to respond to recent price action faster:
```python
# Visualize exit position relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
    color='red',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize entry position relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
    color='green',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize close price for the investment
security_close = signals_df[['Close']].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400)

# Visualize exponentially weighted moving averages
moving_avgs = signals_df[['Fast_Close', 'Slow_Close']].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(xaxis=None)
```
<img src=Images/signals_df_ewm_plot.PNG width=800>

</details>
</blockquote><br>
</details>
</blockquote><br>

</details>
<details>
<summary>How do I create and use Bollinger Bands?</summary>
<font size = "2">

_For ease of explanation, this example will use a **long strategy**. For a refresher on the difference between **long and short strategies**, see the above section on **_long/short strategy_** in this FAQ._</font>

<blockquote>
<details>
<summary>What it is:</summary><br>

Bollinger Bands are a set of lines representing a positive and negative standard deviation away from the simple moving average (SMA) of the asset's closing price.<br>

These lines create _bands_ that move across the plot, creating an area of empty space. The area within this space represents where the closing price _should_ tend to be. The entry/exit signals are generated when the closing price trend line moves out of that area and dips either below or above the bottom and top barriers of the bands.

Check out the [moving average refresher](Moving_Average_Refresher.md) if you need a quick refresh on how moving averages work!

<br>
</details>
<details>
<summary>How to use it:</summary><br>

When the closing price trend line moves below the lower band, a long (buy) opportunity exists as the signal suggests that the price action will tend to move upwards and more in line with where the price _should be_ (within the standard deviation area of the bands).

When the closing price trend line moves above the upper band, a short (sell) opportunity exists as the signal suggests that the price action will tend to move lower and more in line with where the price _should be_ (within the standard deviation area of the bands).

<img src=Images/Boll-Bands.PNG width=700><br>

</details>
<details>
<summary>How to create it:</summary><br>

The dual moving average crossover can be created by using Pandas functionality. In the following steps we'll start with a simple example DataFrame with a datetime index and column of closing stock prices. We will also need to import the following dependences:
```python
import numpy as np
import Pandas as pd
import hvplot.Pandas
from pathlib import Path
```

<img src=Images/signals_bb_df.PNG width=150>
<blockquote>
<details>
<summary>Step One: Generate the daily return column:</summary><br>

We begin by adding a column to hold our daily return values:

```python
# Drop NAs and calculate daily percent return
btc_df['daily_return'] = btc_df['Close'].dropna().pct_change()
btc_df
```
<img src=Images/bb_df.PNG width=500>

</details>

<details>
<summary>Step Two: Generate the values used to create bands:</summary><br>

Next, we generate the values that are subsequently used to create the bands themselves. We use a rolling standard deviation to do this, after which the upper and lower bounds of the bands are creating by adding or substracting the mid_band from the standard deviation respectively:

```python
# Drop NAs and calculate daily percent return
btc_df['daily_return'] = btc_df['Close'].dropna().pct_change()
btc_df# Set Bollinger band window
bollinger_window = 20

# Calculate rolling mean and standard deviation
btc_df['bollinger_mid_band'] = btc_df['Close'].rolling(window=bollinger_window).mean()
btc_df['bollinger_std'] = btc_df['Close'].rolling(window=20).std()

# Calculate upper and lowers bands of Bollinger band
btc_df['bollinger_upper_band']  = btc_df['bollinger_mid_band'] + (btc_df['bollinger_std'] * 1)
btc_df['bollinger_lower_band']  = btc_df['bollinger_mid_band'] - (btc_df['bollinger_std'] * 1)
```

<img src=Images/bb_bands_df.PNG width=500>

</details>
<details>
<summary>Step Three: Plot the bands!</summary><br>

We can finally plot our Bollinger bands as follows:

```python
btc_df[['Close','bollinger_mid_band','bollinger_upper_band','bollinger_lower_band']].plot(figsize=(20,10))
```
<img src=Images/bb_df_plot.PNG width=800>

</details>
</details>
</blockquote><br>

</details>
<details>
<summary>What is back testing and how do I use it?</summary><br>

The term sounds more complicated that it actually is - backtesting is simply the testing of your trading strategy using historical data in a simulated scenario. The results indicate how much the gains and losses **_would_** have been if the strategy had been implemented on a dummy portfolio of predetermined share size with a dummy capital amount of a predetermined size. There's no set rule for what share size or capital amount to backtest with, but in the example below, `500` is chosen for the portfolio size and `$100,000` is chosen for the available capital.

For an example of back test simulation check out the steps below:

<blockquote>
<details>
<summary>Step One: </summary><br>

To conduct the simulation in Jupyter, the portfolio size and capital amount are set in variables so they can be easily inserted to our code:
```python
# Set initial capital
initial_capital = float(100000)
# Set the share size
share_size = 500
```
The portfolio size, or *position*, is set in a column titled `Position` and is coded to equal `500` when the crossover signal is 1 by multipying our share size by the signal:
```python
# Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
signals_df['Position'] = share_size * signals_df['Signal']
```
This inserts a column as seen below:

<img src=Images/active-positions.png>
</details>
<details>
<summary>Step Two: </summary><br>

Next, a column is inserted indicating the share size purchase or sale, depending on the entry/exit points. If there is an entry point, the share size is  `500`. If there is an exit point, the share size is `-500`. This is creating by running `.diff()` on the `Position` column.

```python
# Find the points in time where a 500 share position is bought or sold
signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
```

This inserts a column as seen below:

<img src=Images/active-positions_diff.png>
</details>
<details>
<summary>Step Three: </summary><br>

Next, the column `Portfolio Holdings` is inserted to represent the cumulative investment in the chosen stock over time. These values are obtained by multiplying the closing prices of the stock by the cumulative sum for entry/exit positions of 500 shares - or in this case the `Entry/Exity Position` column:

```python
# Multiply share price by entry/exit positions and get the cumulatively sum
signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()
```
This inserts a column as seen below:

<img src=Images/active-positions_holdings.png>

</details>
<details>
<summary>Step Three: </summary><br>

We now add another new column to represent the remaining cash value of our capital as we make our psuedo investments. To calculate this value, we subtract the `initial_capital` from the product of the `close` prices and the cumulative sum of the `Entry/Exit Position`:

```python
# Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
```
This inserts a column as seen below:

<img src=Images/active-positions_cash.png>

</details>
<details>
<summary>Step Four: </summary><br>

Next, we add the values of the `Portfolio Cash` column to the values of the `Portfolio Holdings` column to create a new column of values - `Portfolio Total`. This column represents the total value of the portfolio over time.

```python

# Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
```
This inserts a column as seen below:

<img src=Images/active-positions_total.png>

</details>
<details>
<summary>Step Five: </summary><br>

The final step before plotting is to generate the daily and cumulative returns. The `Portfolio Daily Returns` column is populated by using `.pct_change()` on the `Portfolio Total` column. This converts the daily portfolio value to daily portfolio returns. The `Portfolio Cumulative Returns` column is populated using `cumprod()` on the newly generated `Portfolio Daily Returns` column. This means that we convert those daily portfolio returns to a cumulative performance index, which makes it easy to see total performance over time and total dollars made. 
```python
# Calculate the portfolio daily returns
signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

# Calculate the cumulative returns
signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
```
This inserts columns as seen below:

<img src=Images/active-positions_returns.png>

</details>
<details>
<summary>Step Six: </summary><br>

Finally, we can visualize the simulation and thus the overal success or failure of our strategy by plotting the values.

```python
# Visualize exit position relative to total portfolio value
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Portfolio Total'].hvplot.scatter(
    color='red',
    legend=False,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize entry position relative to total portfolio value
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Portfolio Total'].hvplot.scatter(
    color='green',
    legend=False,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize total portfolio value for the investment
total_portfolio_value = signals_df[['Portfolio Total']].hvplot(
    line_color='lightgray',
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Overlay plots
portfolio_entry_exit_plot = total_portfolio_value * entry * exit
portfolio_entry_exit_plot.opts(xaxis=None)
```
The above code generates a chart like the one below. This allows us to visualize our simulation. We can see our entry/exit points in red/green respectively, and we can see the trend line of the value of the portfolio rise over time. This particular simulation increased the initial capital from $100,000 to a total portfolio value of $132,975:

<img src=Images/sim_visualization.PNG>

</details>

</blockquote><br>
</details>
</details>
<details>
<summary>What are evaluation metrics used for?</summary><br>

Evaluation metrics are calculations used to assess the value of trades. Used in conjunction with your trading algorithms, they can be used to analyze it's performance and plan for needed adjustments. In class we cover the following evaluation metrics:

- **Cumulative Return:** the total/aggregated amount of gains and losses for an investment. Cumulative return is typically measured over an extended time period.

- **Annual Return:** a time-weighted annual percentage representing the return on an investment over a year.

- **Annual Volatility:** the annualized degree of variation in trading prices over time. Volatility is measured by standard deviation.

- **Sharpe Ratio:** The return on an investment compared to its risk. Measured by the difference between the return on investment and the risk-free return, all divided by standard deviation. Is often used as an annual performance measure, but can be measured over any period of time.

- **Downside Deviation/Return:** The measure of risk for returns that are below the minimum acceptable return (usually below zero, or negative).

- **Sortino Ratio:** The ratio of investment return to harmful volatility. Similar to Sharpe Ratio, but instead focuses on downside deviation rather than the standard deviation.

A cheat sheet to these calculations can be seen [here.](EvaluationsCalculationGuide.md)

</details>

<details>
<summary>Why do I need a framework?</summary><br>

A framework is much like a template for your code. It's a programming technique that organizes code into a workflow that can easily be reused and applied to different scenarios. Just as a library like Pandas can provide prebuilt code to be easily inserted into your program, the framework provides prebuilt structure and organization into which that code can be inserted. The code inside the framework can be easily changed to fit new data, but the flow of the code remains the same.

The trading framework we build in class provides a work flow for building an entire dashboard to visualize a trading strategy. The code inside the framework can be swapped out to accompodate new data, but the work flow remains the same so that when the dashboard is generated all of its components created and can be populated.

</details>

<details>
<summary>What does it mean to persist data and why is it important?</summary><br>

Data persistence is the concept of saving data to a database to have a reliable copy of data that is persisted rather than transiently stored as in-memory data structures.

Persisting data is generally a best practice as it provides a method for data recovery should an application ever fail; data stored in transient in-memory data structures will be lost forever if the application itself terminates. Also, persisting data to a database allows for separate data analysis to be done at a later time, if desired.

</details>

<details>
<summary>What is a pre-trained model and how do I implement one?</summary><br>

Just as we can persist data using a database for longetivity and reuse, we can persist models for the same reasons. When a model is persisted, it is referred to as pre-trained. Pre-trained models have been created, configured, and fitted to data then saved for later use. The models can be loaded as any file can be loaded, using the right modules of course.

This saves us the time consuming process of splitting our data for training and testing, then fitting the model. If it has been done once, and a successful combination has been found, the model can be saved and reused later.

There are many ways to persist your model, however in class we use a library called `joblib`. To save the model we utilize the following code:

```python
from joblib import dump
dump(model, 'your_model.joblib')
```

Once the model is saved, we can load it whenever we need to use it. We load the model as follows:

```python
from joblib import load
model = load('your_model.joblib')
```

Once the model is loaded, predictions can be made as normal:

```python
predictions = model.predict(X_test)
```
</details>


<details>
<summary>Help, I need a time series refresher!</summary><br>

It's important to convert dates into time series when working with python and Pandas. For a quick refresher on reading time series data into a Pandas DataFrame, see below. for a full refresher, head back to the [Unit 10 - Time Series FAQ.](../../10-Time-Series/Supplemental/StudentGuide.md)

<blockquote>
<details><summary>How do you convert objects to `datetime`?</summary>

Converting objects to `datetime` can be tricky. Using Pandas, the conversion can be handled upon reading in of data. The syntax to handle the conversion from `read_csv()` is:

```python
df = pd.read_csv('your_data.csv', parse_dates=True)
```
This converts each object to a `datetime` object. Alternatively, you can also set the index as the date column for ease of plotting:
```python
df = pd.read_csv('your_data.csv', infer_datetime_format=True, parse_dates=True, index_col='Date')
```

</details>
</blockquote>
<br>
</details>
<br>

---

# Unit 18: Blockchain

## Helpful Links

<details><summary>Blockchain</summary>

* https://www.investopedia.com/terms/b/blockchain.asp
</details>

<details><summary>Nodes</summary>

* https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f
</details>
<details><summary>Blockchain Wallets</summary>

* https://www.investopedia.com/terms/b/blockchain-wallet.asp

* https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a
</details>
<details><summary>Digital Signature</summary>

* https://www.instantssl.com/digital-signature

* https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5
</details>
<details><summary>Hash</summary>

* https://www.investopedia.com/terms/h/hash.asp
</details>
<details><summary>Blockchain Mining</summary>

* https://www.bitcoinmining.com/
</details>
<details><summary>Consensus Algorithms</summary>

* https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm
</details>
<details><summary>Proof of Authority</summary>

* https://www.binance.vision/blockchain/proof-of-authority-explained
</details>
<details><summary>Proof of Work</summary>

* https://en.bitcoin.it/wiki/Proof_of_work
</details>
<details><summary>Proof of Stake</summary>

* https://www.investopedia.com/terms/p/proof-stake-pos.asp
</details>

## Additional Course Resources


* [Blockchain Installation Guide](blockchain-install-guide.md)

* [Blockchain Terminology Guide](Blockchain-Terminology-Guide.md)


### Unit 18 FAQs
<details><summary>What is Blockchain?</summary><br>

A blockchain is a type of database that stores an ever-growing list of records, called blocks, that are linked together cryptographically with hashing. Hashing, though similar to encryption is fundamentally different in that it cannot be decrypted - it is a one way scrambling of a message to produce a unique string of characters. This hash string is what links each list of records to the one previous.

The lists of records (blocks), are stored in a distributed manner, meaning that exact copies of all records are stored across all machines (called nodes) that access the network. Combined with hashing, this makes the blockchain extremely trustworthy, as the records are very difficult to alter. Not only does the hashing form a layer of protection, but even if one record is changed, because there are so many duplicates, its easy to prove that the information was altered.

<img src= Images/BlockChain_info.png width=800>

</details>
<details><summary>Why do we need blockchain?</summary><br>

We need blockchain because It solves the fundamental problem of trust between organizations and their affiliated parties, eg (Citizens, Customers, Vendors).

This is achieved thanks to the methodologies in **The Five Pillars of Blockchain**:

<blockquote>
<details><summary>Open</summary><br>

- Openness means that the system is designed to incentivize users to keep it open. The internet is an example of this - it is built on open protocols that anyone can learn and contribute to.

  - Anyone can access the source code and create a project from it, therefore developer access is high.

  - Anyone can access the chain and participate in the ecosystem.

  - Anyone can access the services the blockchain offers.


</details>
<details><summary>Borderless</summary><br>

- Borderless means the network is completely without geographical or political borders.
- To be borderless, the network needs to be decentralized. This means there is **no** central party that holds control of the network.
- Since the blockchain is synchronized onto every device that helps maintain it (called nodes), it lives everywhere.

</details>
<details><summary>Neutral</summary><br>

- Neutral means that the protocol does not discriminate against any user, whether human or machine.

- The blockchain is agnostic to users, regardless of political or social status, or geographic location.

- Open blockchain networks are also governed in a neutral fashion, with many using the blockchain itself for voting on the next network upgrades.
</details>
<details><summary>Censor Resistant</summary><br>

- Decentralized Blockchains are highly resistant to censorship and authoritarian control.

- This means that people suffering in nations that have high censorship can still find a way to use these systems to reach out and to bypass the oppression.

- For example:

  - Blockchain is being used currently around the world to avoid censorship or hyperinflation in many countries.

  - It has been said that blockchain and crypto can be seen as an insurance policy against a dystopian future.

  - Money is often compared to a form of speech. These are systems where this form of expression cannot be censored.

</details>
<details><summary>Public</summary><br>

- Open/Public blockchains are separate from the state and thus well-suited for public affairs.

- Some Blockchains can be private - these are suited to military or government work, where confidentiality is required. This is at least until zero-knowledge proof technology that allows for total privacy on a public blockchain is further developed to scale.

- This separation of state and money is a first in history. It is similar to the separation of church and state to allow for religious freedom; only this allows for monetary freedom.

- These public systems are built by the people, for the people, and are governed by the people.
</details>
</blockquote><br>
</details>

<details><summary>If the blockchain is decentralized, where is it stored?</summary><br>

The blockchain is stored in many remote locations called **nodes**. These nodes are simply computers that log onto the network and store a copy of the blockchain. Anyone can join the network and become a node with their personal computer. This is one of the reasons why the Blockchain is considered open and neutral.

Some nodes are online all the time, constantly downloading new transactions. Others sync up to the system when they log on and update their records to include those newly added.

For more information on nodes, take a look at [this article](https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f).

</details>

<details><summary>What is cryptography and why is relevant to Blockchain?</summary><br>

Cryptography is the science of using math to secure data so that third parties cannot decipher it or tamper with it. There are many types of cryptographic functions, such as hashing, encryption, digital signatures, and other data integrity checks. Each serve a different specific purpose, and when combined together correctly, form highly secured systems.

</details>
<details><summary>What is a hash and why do I need it?</summary><br>

A hash is a one way function that provides a digital fingerprint of data. Hashing is a key component of security on the blockchain, as this is what is used to 'chain' each block (list of records) to the last block. These hashes must match or the block cannot be proven as trustworthy and added to the official blockchain (ledger or list of blocks/records).

A hash function takes an input of any length and turns it into a fixed length scrambled alphanumeric string - regardless of the input contents, or length of characters. The resulting hash cannot be decrypted, as hashing is a one-way function. A hash can be used as a "fingerprint" for any kind of data.

For example the following two input strings result in different output hash strings that are the same length:

### Hash #1
<blockquote>

input = `'Hashing is super fun'`<br>
ouput =  `'82197c1b5722865cf1a98a3a6edc1c35cad6264f2247d9b90713c40344e91722'`<br>
length = `64`
</blockquote>

### Hash #2
<blockquote>

input = `'Hashing is super fun!`<br>
output = `'1e56ea7198cfad7774adf89b32459914b6c165ba19d2e44f28f907384623d15b'`<br>
length = `64`

</blockquote>

Notice that even though we only changed the input very slightly, we got a completely different hash!

The same logic applies for any other type of data. If you download a piece of software from a website that provides the hash of the file, and want to verify that the file you downloaded was exactly what you expected, you could run the same hashing algorithm on the file to verify that you get the **exact** same hash as the website listed. Even if one single bit changed in the file you downloaded, the resulting hash would be dramatically different.
Though the inputs are different lengths and characters, the outputs are both 64 characters long.

Hashing algorithms are complex, but thankfully we don't have to write the algorithms themselves, as there are plenty that have alrady been generated that can be used. Python includes an in-built hashing library called hashlib that includes some of the most popular hashing functions.

For more on hashing, check out [this](https://www.investopedia.com/terms/h/hash.asp) *Investopedia* article.
</details>
<details><summary>What is a Public Key, Private Key and Nonce?</summary><br>

**Public Key** - A public key is a key that is provided publicly to others to use in conjunction with another person's private key to decrypt and encrypt messages securely.

**Private Key** - A private key is a key that is kept secret. It can be used in conjunction with another person's public key to encrypt and decrypt messages with assymetric cryptography or it can be shared with another person so that they might decrypt your symmetric cryptography message.

**Nonce** - A nonce is a number used once. It can be added to cryptographic methods to increase security by introducing an element of randomness.

The uses of these terms is explained in more detail in the next question: *What is the difference between Symmetric and Asymmetric Cryptography?*.

</details>

<details><summary>What is the difference between Symmetric and Asymmetric Cryptography, and how is it related to nonce and digital signatures?</summary><br>

Symmetric cryptography means "one key" to "one lock" -- hence the "symmetry." Asymmetric cryptography doesn't just use one key like symmetric, but now it splits up the key into a "keypair" -- a public key and a private key, or "two keys" to "one lock".

With symmetric cryptography, the private key is shared between the parties in need of the message. The key encrypts and decrypts the message.

Asymmetric cryptography uses a public key *and* a private key to encrypt/decrypt messages.

To **encrypt** and send a message:
-- The sender must have their own private key, and the _recipient's_ public key.

To **decrypt** a received message:
-- The recipient must have their own private key, and the _sender's_ public key

Using a nonce with this method can increase security by adding an element of randomness. The Nonce, _number used once_, is used to make the resulting encrypted message different regardless of the same input, which makes it harder to analyze the output for patterns. If employing the nonce method with your cryptographic algorithm, it would be required to regenerate the same results again later or to decrypt data properly.

Digital signatures are the use of a private key to digitally 'sign' a document. To sign a document digitally, one must use their private key to "sign" the data which produces a string of alphanumeric characters. This string is the "signature". The recipient of the document can then use the public key of the signer to verify that the signature and document was not tampered with.

To read more about digital signatures, click [here](https://www.instantssl.com/digital-signature) and [here](https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5).

</details>

<details><summary>What are consensus algorithms?</summary><br>

Consensus algorithms in blockchain are methods to allow the network to reach agreement (consensus!) on whether a block can be trusted and thus added to the chain. Because blockchains are decentralized, no one person can be trusted to make this decision, so concensus algorithms are used. These algorithms typically use some type of collateral structure to determine trustworthiness. For more information on consensus algorithms in general, check out [this article](https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm).

The three main types of consensus algorithms that we cover in class are:

<blockquote>

<details><summary>Proof of Authority</summary><br>

- This algorithm deviates somewhat from the decentralized nature of blockchains in that there are designated entities that validate the blocks. PoA is almost always used for test networks and not for production.
- With this algorithm, the entities put their reputation on the line as collateral and must typically be voted in.
- For more information on *PoA*, check out [this article](https://www.binance.vision/blockchain/proof-of-authority-explained).
</details>

<details><summary>Proof of Work</summary><br>

- Used by Bitcoin and many other well known Blockchains, *Proof of Work* was the first consensus algorithm used in a public blockchain, and is where the term *mining* originated.
- To malicously attack a blockchain using *PoW*, one would need to use 51% of the computational power that the network uses. This strongly disincentivizes attacking the network.
- With this algorithm, the entities put their computational resources on the line as collateral.
- For more information on *PoW*, check out [this article](https://en.bitcoin.it/wiki/Proof_of_work).
</details>
<details><summary>Proof of Stake</summary><br>

- Developed as alternative to the resource intensive *PoW* algorithm, this method validates blocks based on a monetized stake in the network.
- To malicously attack a blockchain using *PoS*, one would need to hold 51% of the monetary power that the network holds. This strongly disincentivizes attacking the network.
- With this algorithm, the entities put their cryptocurrency on the line as collateral.
- For more information on *PoS*, check out [this article](https://www.investopedia.com/terms/p/proof-stake-pos.asp).
</details>
</blockquote>
</details>
<details><summary>What 'puzzle' is the Proof of Work algorithm solving?</summary><br>

When a block (or collection of records), is 'mined' - meaning validated and added to the chain - a miner will have solved a very difficult mathematical puzzle to do so. With many puzzles, there is some bit of logic involved, however with bitcoin mining, the puzzle is completely random. Essentially the puzzle is solved by finding the Nonce that, when added to the hash of the block itself, will produce a **new** hash with a predetermined number of leading zeros.

Solving the puzzle of which nonce will produce a new hash with **n** number of leading zeros is based solely on trial and error. Because of this it can be quite time intensive to decipher. Large quantities of electricity and computational power are used. This is why the winner of the nonce lottery receives a block reward for solving the puzzle and is the basis for the *Proof of Work* consensus algorithm.
</details>


<details><summary>What is the difference between a node and a miner?</summary><br>

Both miners and nodes are computers. A computer can serve as both miner and node - however they perform different functions. A node is a computer that stores a copy of the blockchain. A miner is a computer that works to solve the puzzle that will allow the a block of transactions to be validated and added to the network of nodes.

To learn about mining, click [this link](https://www.bitcoinmining.com/).

To learn more about nodes, click [this link](https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f).

</details>

<details><summary>What is a digital Blockchain wallet?</summary><br>

A digital, or blockchain, wallet is simply an asymmetric keypair that act as "keys" to your funds that are on the blockchain. It also serves as a place where you can view and send transactions.

Much like a debit card does not hold your actual money, but the access to it, a blockchain wallet holds the access to your funds but not the actual funds. The actual funds live on the blockchain.

For more reading on blockchain wallets, check out these articles from [investopedia](https://www.investopedia.com/terms/b/blockchain-wallet.asp) and [uncoin](https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a).

</details>

<details><summary>What is a Block explorer and how do I use it?</summary><br>

A block explorer is a tool that allows you to search transactions on a particular blockchain. Just as you might use a search engine to search topics online, the block explorer allows you to search blocks on the blockchain. With a block explorer you can see various data about the block and drill down into the specifics. For example on Etherscan, a block explorer for Ethereum, you can find information such as:

* Block Height (block number on the chain)
* Transaction Hash
* From and To Address
* Entity that mined the block
* Block Reward
* Difficulty
* Gas

</details>

<details><summary>Where can I get a quick summary of Blockchain Terminology?</summary>

For a quick run down of all the terms we cover in Unit 18, check out [this terminology guide](Blockchain-Terminology-Guide.md).
</details>

---

# Unit 19: Blockchain Transactions

## Symmetric vs. Asymmetric Encryption

* https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences

* https://support.microsoft.com/en-us/help/246071/description-of-symmetric-and-asymmetric-encryption

## Blockchain Wallets

* https://www.investopedia.com/terms/b/blockchain-wallet.asp

* https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a

## Digital Signature

* https://www.instantssl.com/digital-signature

* https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5

## Hash

* https://www.investopedia.com/terms/h/hash.asp

## BIP

* * https://en.bitcoin.it/wiki/Bitcoin_Improvement_Proposals

## BIP32

* https://bitcoin.org/en/glossary/hd-protocol

* https://www.w3.org/2016/04/blockchain-workshop/interest/robles.html

* https://github.com/WebOfTrustInfo/rwot1-sf/blob/master/topics-and-advance-readings/hierarchical-deterministic-keys--bip32-and-beyond.md

* https://en.bitcoin.it/wiki/Deterministic_wallet

## BIP39

* https://wiki.trezor.io/Developers_guide-Cryptography

## BIP44

* https://stackoverflow.com/questions/50394722/how-to-create-own-multi-currency-crypto-wallet

* https://wiki.trezor.io/Cryptocurrency_standards#BIP44_-_Multi-account_hierarchy_for_deterministic_wallets

---

# Unit 20: Solidity

## Variables and Parameters

* Local and State Solidity Variables and Use of Parameters: https://www.bitdegree.org/learn/solidity-variables

* Local variable and state variable, and the difference between them: https://ethereum.stackexchange.com/questions/25554/local-variable-and-state-variable-and-the-difference-between-them

* Why constant variables inside functions fail to compile in Solidity?: https://ethereum.stackexchange.com/questions/51366/why-constant-variables-inside-functions-fail-to-compile-in-solidity

## Control Structures

* Control Structures in Ethereum: https://medium.com/@k3no/control-structures-in-ethereum-3f2d4149b84a

* What difference between if and require in solidity: https://ethereum.stackexchange.com/questions/60585/what-difference-between-if-and-require-in-solidity

## Books

* Building Ethereum Dapps, Roberto Infante, Manning Publications: https://www.manning.com/books/building-ethereum-dapps.

## Resources

* Ethereum for Developers: https://ethereum.org/developers/#getting-started

---

# Unit 21: Advanced Solidity

## Tokenomics

* [Tokenomics. Thomas Power & Sean Au. Packt Publishing](https://www.oreilly.com/library/view/tokenomics/9781789136326/)

* [Three Definitions of Tokenomics](https://www.coindesk.com/three-definitions-tokenomics)

* [What is Tokenomics? Ultimate Investor's Guide - Part 1](https://blockgeeks.com/guides/what-is-tokenomics/)

* [What is Tokenomics? Ultimate Investor's Guide - Part 2](https://blockgeeks.com/guides/what-is-tokenomics-part-2/)

## Key Concepts

* [Tokens Definition from OpenZeppelin](https://docs.openzeppelin.com/contracts/2.x/tokens)

* [Token vs Coin: What’s the Difference?](https://www.bitdegree.org/tutorials/token-vs-coin/)

* [Fungibility](https://en.wikipedia.org/wiki/Fungibility)

* [List of ERC-20 Tokens](https://etherscan.io/tokens)

* [Stablecoin definition from Investopedia](https://www.investopedia.com/terms/s/stablecoin.asp)

* [Basis Points (BPS) definition from Investopedia](https://www.investopedia.com/terms/b/basispoint.asp)

## Ethereum

* [Ethereum Improvement Proposals](https://eips.ethereum.org/)

* [Online list of ERCs](https://eips.ethereum.org/erc)

* [Crowdsales in Ethereum](https://docs.openzeppelin.com/contracts/2.x/crowdsales)

## Smart Contract Vulnerabilities

* [Smart Contract Weakness Classification (SWC) Registry](https://swcregistry.io/)

* [SWC coverage and status](https://mythx.io/swc-coverage/)

## Mapping Types

* [Mapping Types Documentation](https://solidity.readthedocs.io/en/v0.6.0/types.html#mapping-types)

* [How does Mapping in solidity work?](https://ethereum.stackexchange.com/questions/9893/how-does-mapping-in-solidity-work)

* [Solidity - A Deep Explanation of Mappings Part 1](https://youtu.be/VyAMoo1Sz4I)

* [Solidity - A Deep Explanation of Mappings Part 2](https://youtu.be/zDhJbwMUKIQ)

## OpenZeppelin

* [Getting Started with OpenZeppelin](https://docs.openzeppelin.com/contracts/2.x/)

* [OpenZeppelin SafeMath Documentation](https://docs.openzeppelin.com/contracts/2.x/api/math#SafeMath)

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.