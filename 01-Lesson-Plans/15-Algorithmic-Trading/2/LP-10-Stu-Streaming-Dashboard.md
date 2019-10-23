### 9. Instructor Do: Streaming Data with Streamz (15 mins)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to show students how to update a visualization as data continues to flow without the need for re-constructing the visual component each time.

**File:** [streamz.ipynb](Activities/08-Ins_Streaming/Solved/streamz.ipynb)

Open the solution file and discuss the following:

* First and foremost, we will need to import the necessary libraries and dependencies in order to properly stream data.

  ```python
  import os
  import ccxt
  import pandas as pd
  import hvplot.streamz
  from streamz import Stream
  from streamz.dataframe import DataFrame
  ```

* The Streamz library supports streaming data from a Pandas DataFrame and includes a custom Stream DataFrame object that can bind Stream objects to itself. The `example` parameter sets the structure of the Stream DataFrame object, and similar to a normal DataFrame, hvplot can be called on the Stream DataFrame to generate a visualization such as a scatter plot.

  ![stream-dataframe](Images/stream-dataframe.png)

* Hvplot will bind the streamz buffer to the chart. Emitting a dataframe to the stream will add that data to the plot. Not sure what the upper limit it, but at 10000 iterations, it seems to accumulate all of the points. Not sure if there is an integer limit or a memory limit.
