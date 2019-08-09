### Instructor Do: Time Series Decomposition (0:10)

* **File:**

  [decomposition.ipynb](decomposition.ipynb)

* Open [slide #1](tbd).

* Define time series decomposition to the class:

  * In a nutshell, it is separating time series data into useful and less useful components.

  * The useful components can be used to observe patterns and to make predictions.

* Open [slide #2] and list the components of time series decomposition:

  * Level: What is the average value of the series?

  * Trend: Is there an overall direction of movement?

  * Seasonality: Do patterns occur in cycles?

  * Residual: How much noise exists in the data?

* Open [notebook](tbd) and explain that it is a chart of monthly liquor sales in the United States between 1980 and 2007.

  * ![Images/decomposition01.png](Images/decomposition01.png)

* Ask ask students to describe what they see:

  * There is an overall increase in sales over the years.

  * Spikes in sales also appear regularly.

  * As expected, the pattern is not perfectly regular.

* Show the next image in the notebook:

  ![Images/decomposition02.png](Images/decomposition02.png)

  * It plots liquor sales data from a 26-month period.

  * It shows a sales spike during each holiday season.

* Next, explain that the code below decomposes the liquor sales data.

  ```python
  decomposed = seasonal_decompose(df['liquor_sales'], model='multiplicative')
  ```

  * The model is specified as multiplicative because the seasonal flunctation (the spikes) increases with the series.

* Explain that the time series is decomposed visually by the library:

  ![Images/decomposition03.png](Images/decomposition03.png)

  * The `observed data` panel is decomposed into the next three elements.

  * An upward trend is observed in the data.

  * A seasonality is also observed.

  * The residual components are the leftovers when trend and seasonality are removed.

* Finally, explain that the library used in the notebook is more useful as an illustrative tool than a predictive tool. We will cover such tools during this week.
