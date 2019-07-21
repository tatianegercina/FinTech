### 18. Instructor Do: Visualization Options (5 mins) (Critical)

The goal of this activity is to provide students with a dry walkthrough demonstration of how to use hvPlot plot attributes and options to customize the look and feel of visualizations. This activity will enable students to perfect their visualizations by fine tuning details such as axis labels, as well as create attractive color themes and effects.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/real-estate-sale-history-06c8f).

**Files:**

* [Slides]()

* [viz_options.ipynb](Activities/18-Ins_Viz_Options/Solved/viz_options.ipynb)

Open the starter file, and perform a dry walkthrough of the solution, highlighting the following:

* hvPlots do not always come out perfect. Customization options give users the ability to customize the look and feel of their visualizations.

  ```python
  # Read in data, filter, and slice
  home_sale_prices = pd.read_csv('../Resources/housing_sale_data.csv',index_col='salesHistoryKey')
  home_sale_prices = home_sale_prices[home_sale_prices['saleDate'] > '2019-06-01'][home_sale_prices['saleDate'] < '2019-06-31']

  # Slice data
  sale_prices_by_year = home_sale_prices[['saleAmt','saleDate']].groupby('saleDate').mean().sort_values('saleDate')

  # Plot data without rotation
  sale_prices_by_year.hvplot.bar(x='saleDate',y='saleAmt')
  ```

  ![hvplot_oob_issues.png](Images/hvplot_oob_issues.png)

* Working with large amounts of data will often make axis labels impossible to read. The `rot` attribute allows users to customize label angles to make reading labels easier. The `rot` attribute accepts an integer value that indicates the angle at which **x axis** labels should be rotated.

  ```python
  # Plot data with rotation
  sale_prices_by_year.hvplot.bar(x='saleDate',y='saleAmt', rot=90)
  ```

  ![plot_no_rot.png](Images/plot_no_rot.png)

  ![plot_with_rot.png](Images/plot_with_rot.png)

* Axes labels can be configured to be formatted in a specific way. The `opts(xformatter)` and `opts(yformatter)` allows users to specify string (i.e. `%.2f`) or NumberFormatter formatting objects.

  ```python
  # Use string formatting to show no decimal places for saleAmt
  sale_prices_by_year.hvplot.bar(x='saleDate',y='saleAmt', rot=90).opts(yformatter='%.0f')
  ```

  ![hvplot_formatter.png](Images/hvplot_formatter.png)

* Titles can be added to visualizations using the `opts(title)` parameter.

  ```python
  # Set title
  sale_prices_by_year.hvplot.bar(x='saleDate',y='saleAmt', rot=90).opts(title='Arlington, VA Housing Sale Prices June 2016')
  ```

  ![opt_title.png](Images/opt_title.png)

* The `invert_axis` option is used to change the orientation of a visualization. An example of this would be showing a bar chart with bars moving horizontally rather than vertically.

  ```python
  # Invert axes
  sale_prices_by_year_title.opts(invert_axes=True)
  ```

  ![plot_invert.png](Images/plot_invert.png)

Slack out the [hvPlot customization](http://holoviews.org/user_guide/Customizing_Plots.html) link. The site lists all of the options available in hvPlot. Encourage students to review the list of options.

* Customizing plots -> http://holoviews.org/user_guide/Customizing_Plots.html

Ask if there are any more questions. Then, continue to the student challenge activity.
