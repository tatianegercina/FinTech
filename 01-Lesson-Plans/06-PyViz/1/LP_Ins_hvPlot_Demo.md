### 10. Instructor Do: hvPlot Demo (5 mins)

**Files:**

* [hvPlot.ipynb](Activities/10-Ins_hvPlot_Demo/Solved/hvPlot.ipynb)

Open the starter file, and live code the following:

  * The **hvPlot** library has to be imported into the Python environment. hvPlot offers a library called **hvPlot.Pandas** that integrates hvPlot with Pandas DataFrame API. This allows Pandas DataFrames to be visualized using hvPlot.

    ```python
    import hvPlot.Pandas
    ```

  * The `hvPlot` function is used to create a standard hvPlot chart. For example, when applied against a DataFrame containing cumulative returns for five different tickers, hvPlot would create a visualization using the metadata and data from the DataFrame. No configuration is needed by the user.

  ```python
  import pandas as pd, numpy as np
  df_idx = pd.date_range('1/1/2018', periods=1000)
  df = pd.DateFrame(np.random.randn(1000,4),index=df_idx, columns=('APPL','GOGLE','AMMD','BCOIN')).cumsum()

  df.hvPlot()
  ```

* Similar to the `Pandas.plot` API, the `hvPlot` function comes with a `line` attribute. The `line` attribute explicitly specifies to hvPlot that the visualization should be a line chart. The `line` attribute has 4 commonly used parameters:

  * X axis and label

  * Y axis and label

  ```python
  df.hvplot.line(
        "year",
        "cumsum",
        xlabel="Year",
        ylabel="Cumulative Return"
    )
  ```

* The `hvPlot` function also has a `bar` attribute. It works the same as the `line` attribute, but it creates a **bar** visualization rather than **line**.

  ```python
  df.hvplot.bar(
        "year",
        "cumsum",
        xlabel="Year",
        ylabel="Cumulative Return"
    )
  ```

Choose either the line or bar visualization, and demonstrate to students how to use hvPlot's interactive features. Highlight the following:

* Click and drag the visualization to pane to the left and right. Communicate that visualizations panned, allowing for data to be analyzed across time more effectively and efficiently.

* Select an element on the legend to filter it out. Show that this allows data to be hidden as needed. This allows data to be curated to specific analytic needs on a case by case basis.

Ask students if they have any questions before moving onto the next activity.
