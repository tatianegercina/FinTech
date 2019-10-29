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

* In order to push data through to the scatter plot, the Stream object houses an `emit` function that pushes a DataFrame with similar structure to the bound Stream DataFrame object, which is then used to update the scatter plot. In this case, a loop from 1 to 20 is performed in which for every loop, a DataFrame is created with the value `i` and pushed via the Stream object to the scatter plot. The result is a scatter plot that streams its data points from 1 to 20.

  ![stream-emit](Images/stream-emit.gif)

* In addition, hvplot allows for a `backlog` parameter that creates a rolling window for streaming data. In this case, the data is streamed to the scatter plot ranging from 1 to 100; however, the use of the`backlog` parameter sets a rolling window of 10 data points in the scatter plot.

  ![stream-emit-rolling](Images/stream-emit-rolling.gif)

* Lastly, the Stream library can be used to stream data received from an external API, such as the Kraken exchange via the ccxt library. In this case, a Stream DataFrame object is created and bound to the Stream object with a structure set to a DataFrame with the column `close`. Then, in a continuous while loop, data is pulled from Kraken and a DataFrame with a similar structure to the Stream DataFrame object is pushed via the `emit` function. The result is a line chart that continually streams BTC/USD pricing data.

  ![stream-kraken-data](Images/stream-kraken-data.gif)

Ask any questions before moving on.
