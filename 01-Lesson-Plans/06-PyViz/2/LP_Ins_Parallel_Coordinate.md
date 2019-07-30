### 7. Instructor Do: Parallel Coordinate Plot (10 mins) (Critical)

In this activity, students are introduced to one of the more advanced, statistical plots that Plotly has to offer: the Parallel Coordinate plot (by way of an instructor demo). This will be a completely new plot for students, not having been seen in Pandas, Matplotlib, or hvPlot.

**Files:**

* [parallel_coordinate.ipynb](Activities/07-Parallel_Coordinate/Solved/parallel_cooridnate.ipynb)

Open the solved solution file, and demonstrate to students a parallel coordinate plot. While walking through the solved file, highlight the below discussion points. Make sure to place particular emphasis on the **what** and **why** of parallel coordinate plots so that they understand their use case and when they should be applied.

* Explain to students that parallel coordinate plots are used to visualize multivariate analysis. This type of analysis typically includes more than two variables. What's important to note is that the variables should be of the same categorical class, meaning each variable has the same attributes.

  * A good example of variables with the same attributes would be three different types of cars: Ford Mustang, Chevy Cobolt, and Dodge Dart. Attributes of interest for analysis might be average miles per galloon or average yearly sales, which could be plotted with a Parallel Coordinate plot.

* Communicate that Parallel coordinate plots allow for multiple variables to be represented in parallel to one another. This is particularly valuable when tracing the relationships between variables and how each variable relates to/affects the other.

  * Continuing with the previous example, this would mean each type of car would have it's own vertical, and each vertical would be aligned in parallel. Relationships between each car would be identified by a line that connects each data point.

* Break down the anatomy of the plot, emphasizing the below points.

  * Point out the verticals on the plot. Each vertical represents a different variable. Because each variable can have a different range of numeric values, the scale of each vertical is specific to that variable. This would mean each vertical could have a different scale.

  * Point out the colored lines on the plot. A line is used to connect data points of the same record. For example, average sale records for three different types of cars for the year of 2019 would be connected by the same line. The values for 2018 would be connected by a different line.

    * Each line is color coded to help assist in tracing the relationships. This is especially valuable when going from looking at data from a row point of view to looking at a visualization.
