### 18. Instructor Do - Plotting with Flair (5 mins) (Optional)

In this optional activity, the instructor demonstrates to students how to create additional hvPlot types, such as **scatter** and **area** plots.

**Files:**

* [Slides]()

* [plotting_with_flair.ipynb](Activities/10-Ins_Plotting_with_Flair/Unsolved/plotting_with_flair.ipynb)

Explain to students that **line** and **bar** plots are just the tip of the iceberg in terms of what hvPlot supports.

* hvPlot also offers **area** and **scatter** plots, just to name two more. These plots are essential when visualizing and analyzing categorical/dimensional data at multivariate levels. An example would be considering real estate metric data across time, in terms of sales, foreclosures, and pending escrows.

* Because these plots support comparative analysis, they can be considered as more advanced than the standard **line** and **bar** plots. Adding these to any report would add extra visual and statistical flair.

Open the starter file, and live code the following. Make sure to highlight the corresponding discussion points during the demonstration.

* **Area** plots are a great way to visualize multivariate time analysis, time-series relationships, and progression over time. In addition to change over time, **area** charts also communicate the volume associated with trends and change over time. Whenever data needs to be analyzed over time, the `hvplot.area` function can be used to plot, visualize, and analyze the data.

  ```python
  import pandas as pd, numpy as np
  import hvplot.pandas

  # Prep data
  df  = pd.DataFrame({
    "foreclosed":np.random.randint(0,32,50),
    "sold":np.random.randint(0,32,50),
    "escrow":np.random.randint(0,32,50),
    "year":np.random.randint(2010,2019,50)}).sort_values('year')

  # Area plot
  df.hvplot.area(
    x='year',
    y=['foreclosed','sold','escrow'],
    xlabel='Year',
    ylabel='Total',
    title='2019 VA Q1 Real Estate Metrics',
    stacked=True)
  ```

  ![area_plot.png](Images/area_plot.png)

* **Scatter** plots are a commonly used for showing how one data point is affected by another. For example, a real estate analyst might want to assess the correlation between number of foreclosures and houses currently in escrow across years. The `hvplot.scatter` function can help with visualizing the correlation. Execute the `hvplot.scatter` function against a Pandas DataFrame.

  ```python
  # Scatter Plot
  df.hvplot.scatter(
    x='foreclosed',
    y='escrow',
    xlabel='Foreclosed',
    ylabel='Escrow',
    c='year',
    cmap='viridis',
    colorbar=True,
    title='2019 VA Q1 Real Estate Metrics'
  )
  ```

  ![scatter_plot.png](Images/scatter_plot.png)

Ask for any questions, and then move onto the next activity.
