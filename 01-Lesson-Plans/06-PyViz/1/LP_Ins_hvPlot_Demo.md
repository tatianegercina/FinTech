### 10. Instructor Do: hvPlot Demo (5 minutes)

**Files:**

* [hvPlot.ipynb](Activities/10-Ins_hvPlot_Demo/Unsolved/hvPlot.ipynb)

Open the [starter file](Activities/10-Ins_hvPlot_Demo/Unsolved/hvPlot.ipynb), and live code the following:

  * The **hvPlot** library has to be imported into the Python environment. hvPlot offers a library called **hvPlot.Pandas** that integrates hvPlot with Pandas DataFrame API. This allows Pandas DataFrames to be visualized using hvPlot.

    ```python
    import hvplot.pandas
    ```

  * The `hvPlot` function is used to create a standard hvPlot chart. For example, when applied against a DataFrame containing cumulative returns for five different tickers, hvPlot would create a visualization using the metadata and data from the DataFrame. No configuration is needed by the user.

    ```python
    # Data Prep
    df_idx = pd.date_range('1/1/2018', periods=1000)
    df = pd.DataFrame(np.random.randn(1000,4),index=df_idx, columns=('APPL','GOGLE','AMMD','BCOIN')).pct_change()

    # Use hvplot() function to plot data
    df.hvplot()
    ```

    ![hvplot_line.png](Images/hvplot_line.png)

* Similar to the `Pandas.plot` API, the `hvPlot` function comes with a `line` attribute. The `line` attribute explicitly specifies to hvPlot that the visualization should be a line chart.

    ```python
    # Use hplot.line to create line plot
    df.hvplot.line(
        xlabel="Year",
        ylabel="Daily Return"
    )
    ```

* The `hvPlot` function also has a `bar` attribute for visualization of categorical data. It works the same as the `line` attribute, but it creates a **bar** visualization rather than **line**. It is important to note to students that bar plots require categorical data and not just time series data. Bar plots need to compare the **x** axis against **y**.

    ```python
    # Data Prep
    df = pd.DataFrame({'ticker':['APPL','GOGLE', 'AMMD','BCOIN'], 'daily_return':(4.50,10,33.0,55.25)})

    # Use hvplot.bar() to create bar plot with categorical data
    df.hvplot.bar(x='ticker', y='daily_return', xlabel='Ticker', ylabel='Daily Return', rot=90)
    ```

    ![hvplot_bar.png](Images/hvplot_bar.png)

If time remains, choose either the line or bar visualization, and demonstrate to students how to use hvPlot's interactive features. Highlight the following:

* Hover over a data point to highlight hover interaction. Explain that hovering allows users to hone in on the plot value being observed.

* Click and drag the visualization to pane to the left and right. Communicate that visualizations panned, allowing for data to be analyzed across time more effectively and efficiently.

* Select an element on the legend to filter it out. Show that this allows data to be hidden as needed. This allows data to be curated to specific analytic needs on a case by case basis.

* Indicate to students that these are just two ways to interact with hvplots. Hvplot also provides widgets to interact with teh data. These will be reviewed later in the day.

Ask students if they have any questions before moving onto the next activity.
