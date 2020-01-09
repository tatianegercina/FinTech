## FAQs

## Unit 03: Python/Pandas
[Why is it called Pandas?](#why-is-it-called-pandas)<br>
[How do you access a column?](#how-do-you-access-a-column)<br>
[Why do I keep getting a key error?](#why-do-i-keep-getting-a-key-error)<br>
[What is a DataFrame axis?](#what-is-a-dataframe-axis)<br>
[What is the difference between a Series and a DataFrame?](#what-is-the-difference-between-a-series-and-a-dataframe)<br>
[Why do my Dataframe changes disappear when I move to the next cell in Jupyter?](#why-do-my-dataframe-changes-disappear-when-i-move-to-the-next-cell-in-Jupyter)<br>
[How do you loop through a DataFrame?](#how-do-you-loop-through-a-dataframe)<br>
[Why must I apply a function to a groupby object in order to output a DataFrame?](#why-must-i-apply-a-function-to-a-groupby-object-in-order-to-output-a-dataframe)<br>
[What does this error mean: `TypeError: unsupported operand type`?](#what-does-this-error-mean-typeerror-unsupported-operand-type)<br>
#### Why is it called pandas?
According to *Python for Data Analysis*, written by Pandas inventor himself, Wes McKinney, the name pandas "is derived from panel data, an econometrics term for multidimensional structured data sets, and Python data analysis itself"(McKinney, 2013).

#### How do you access a column?
To access a column in your DataFrame you call the DataFrame variable plus the column using either bracket or dot notation.  For example, lets use the following DataFrame named `cylons`:

![Cylon DF](Resources/Cylon_DF.PNG)<br>

you would access the `Model_Number` column as follows:

![Cylon DF](Resources/Cylon_Series.PNG)<br>

#### Why do I keep getting a key error?
If Pandas throws a key error at you, it can be really frustrating, especially when you just *know* you've typed in a value that is in the key.  If this happens during the accessing of a column, try running the df.columns function to get a screen print of all the column names.  You might have an invisible space or escaped line in the column name that doesn't show up during normal printing, that will show up when this function is used.  In some cases you might be using a function that defaults to the row axis instead of the column axis.  In that situation you will get an error like: `KeyError: "['X'] not found in axis"`.  In that situation, yes the key exists but that function isn't looking for the column keys, but rather a row value.

#### What is a DataFrame axis?
A DataFrame axis is simply the column headers or the row index positions.  This image helps to visualize it:

![Cylon DF Axes](Resources/Cylon_Axes.png)<br>


#### What is the difference between a Series and a DataFrame?
A DataFrame is a 2D matrix object holding rows and columns.  A Series is a 1D object, much like an array, though it can have an index.  When a single column is extracted from a DataFrame, it is a Series object.  The following image shows a Series object extracted from our cylons DataFrame:

![Cylon DF Series](Resources/Cylon_Series.PNG)<br>


#### Why do my Dataframe changes disappear when I move to the next cell in Jupyter?

When a DataFrame is stored in a variable, it is a one time snapshot of the DataFrame at the time of storage.  If you make changes to the DataFrame, you must either store the new DataFrame in a new variable, overwrite the old DataFrame variable name, or use the `inplace = True` argument in the function parameters.  For example, the following code will only populate a change for the [notebook cell in which it is located:  `cylon_df.rename({'Model_Number': 'Model#'}).  But by adding an `inplace=True` parameter, the change will stay:  `cylon_df.rename(columns={'Model_Number': 'Model#'}, inplace=True)`.  An equivalent method is to reassign the value and call it: `cylon_df = cylon_df.rename(columns={'Model_Number': 'Model#'})`.

#### How do you loop through a DataFrame?

There are multiple methods to achieve this task.  For a super efficient method see our example below.  To see other methods, check out this great [Medium article](https://medium.com/@rtjeannier/pandas-101-cont-9d061cb73bfc).

You can loop through our Cylon_DF using `.loc` as follows:

```python
for i in cylon_df.index:
        print(cylon_df.loc[i,'Alias'])
        print(cylon_df.loc[i, 'Model#'])
```
In this example `.loc() searches for `i`, which represents the contents of each cell, and then the column name that is passed, both in brackets.

#### Why must I apply a function to a groupby object in order to output a DataFrame?

The groupby function puts all elements of a certain category together by finding each unique value in the column specified and converting that to a new index.  If you were to group our cylons_df by the `Model#` but not apply a function to it, the code can run the grouping, but it doesn't know what to do with the other columns.  There would only a new index, with extraneous data that doesn't fit the new index lenght or match up in anyway.  By applying a function, such as `.count()`, the code can perform an aggregation on the other columns and keep them in the object.  For example, if we run `cylons_df.groupby('Model#').count()`, our DataFrame index is converted into the unique values of cylon model numbers, and then the other data is counted based on how many there are of each model number.

![Cylon DF Groupby](Resources/Cylon_Groupby.PNG)<br>

#### What does this error mean: `TypeError: unsupported operand type`?

Have you ever gotten an error similar to this:  `TypeError: unsupported operand type(s) for +: 'int' and 'str'`?  If so, its because you were trying to combine data of different types, and Python doesn't like that! Let's take the following code, where we are trying to concatenate a string the end of an integer to make a new sentence:
```python
for x in cylon_df['Model#']:
    print(str(x) + ' is the best!')
```
This would throw the following error:
```python
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
And the TypeError will typicall tell you what two datatypes you are trying to combine, as in the above code snippet.  To get around this, we just have to alter these data types to make them play nice!  To do that we can change our integer to a string as follows:
```python
for x in cylon_df['Model#']:
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




#### Sources
McKinney, W. (2013) *Python for Data Analysis.* O'Reilly Media, Inc, USA.
