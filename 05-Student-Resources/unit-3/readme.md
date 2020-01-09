## FAQs

## Unit 03: Python/Pandas
[Why is it called Pandas?](#why-is-it-called-pandas)<br>
[How do you access a column?](#how-do-you-access-a-column)<br>
[Why do I keep getting a key error?](#why-do-i-keep-getting-a-key-error)<br>
[What is a DataFrame axis?](#what-is-a-dataframe-axis)<br>
[What is the difference between a Series and a DataFrame?](#what-is-the-difference-between-a-series-and-a-dataframe)<br>


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




### Sources
McKinney, W. (2013) *Python for Data Analysis.* O'Reilly Media, Inc, USA.
