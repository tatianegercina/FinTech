### 2. Instructor Do: Intro to Plotly Express (5 mins)

In this activity, the instructor will engage the students with a facilitated discussion regarding **Plotly Express** and its common charting types. This activity will serve as the foundation for identifying visualization use cases that would require one to use a technology like **Plotly Express** rather than **hvPlot**.

**Files:**

* [Slides]()

Navigate to the 6.2 slides, and highlight the following:

* **Plotly Express** works much like hvPlot, giving users a simple `plot` based interface that allows developers to create and customize interactive visualizations.

* **Plotly Express** is packaged and powered by the **Plotly** library, an open source graphing library for Python.

* **Plotly Express** is a high level wrapper abstracted over **Plotly**, simplifying the work needed to create a visualization. **Plotly** has a range of plot and chart types, skins, and colors, which **Plotly Express** is able to leverage. **Plotly** is teh engine that generates **Plotly Express** figures.

* **Plotly Express** provides a simple `iplot` interface that can be used to create complex charts. Similar to the `hvplot` function, the `iplot` function accepts arguments that allow the visualizations to be customized.

Give students a preview of what can be created with **Plotly Express** by visiting the [Github page](https://plot.ly/python/plotly-express/) and showing students some examples of **Plotly Express** visualizations. All images have been retrieved from the [Plotly Express](https://plot.ly/python/plotly-express/) website. Make sure to highlight the following:

  * **Plotly Express** also comes with its own version of the standard plot types (i.e. scatter and line plots).

    ![example_plotly_plots.png](Images/example_plotly_plots.png)

    ![example_plotly_plots_2.png](Images/example_plotly_plots_2.png)


  * In addition to the chart types we've already seen (i.e. scatter, line, and bar), **Plotly Express** also includes charting types such as **Parallel Coordinates** and **Parallel Categories**, plot types that are useful when visualizing correlations and the relationships between data points.

    ![example_plotly_plots_3.gif](Images/example_plotly_plots_3.gif)

    ![example_plotly_plots_4.gif](Images/example_plotly_plots_4.gif)

Ask students to take a guess at the differences between parallel categories/coordinate plots and scatter plots.

  * **Answer** **Parallel Coordinates and Categories plots** are better when comparing multidimensional data that has high dimensionality. The more dimensions, and the greater the volume in those dimensions, the more applicable **Parallel Coordinates and Categories** are.

  * Where **scatter** plots compare X and Y as a perpendicular intersection (90 degree angle), **Parallel Coordinates and Categories** plots place X and Y axes parallel to one another, which allows points from X to be mapped linearly to Y.

If time remains, preview some of the other plots to the students, such as:

  * Density Contour

  * Density Heatmap

  * Maps

Ask for any questions, and then more onto the next activity.
