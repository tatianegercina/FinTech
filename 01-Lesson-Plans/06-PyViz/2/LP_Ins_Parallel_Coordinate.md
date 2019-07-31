### 7. Instructor Do: Parallel Coordinate Plot (10 mins) (Critical)

In this activity, students are introduced to one of the more advanced, statistical plots that Plotly has to offer: the Parallel Coordinate plot (by way of an instructor demo). This will be a completely new plot for students, not having been seen in Pandas, Matplotlib, or hvPlot.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/2011-housing-market-typology-a6419).

**Files:**

* [parallel_coordinate.ipynb](Activities/07-Parallel_Coordinate/Solved/parallel_cooridnate.ipynb)

Open the solved solution file and conduct a dry walk through. While walking through the solved file, highlight the below discussion points. Make sure to place particular emphasis on the **what** and **why** of parallel coordinate plots so that they understand their use case and when they should be applied.

Walk through the syntax required to create a parallel coordinate plot:

* The Parallel Coordinate plot can be created using the `parallel_coordinates` function.

  ```python
  import plotly.express as px
  import pandas as pd

  # Read in data
  typology = pd.read_csv('../Resources/housing_market_typology.csv')[:30].sort_values('blockGroup')

  # Create Parallel Coordinates plot
  px.parallel_coordinates(typology, color='blockGroup')
  ```

  ![parallel_coordinates.gif](Images/parallel_coordinates.gif)

* By sorting the axes and filtering values, analysts can cluster attributes to assess relationships and trends.

  * For example, sorting so that **vacantLots** and **sales20092010** are adjacent allows one to see how the number of vacant lots affects the number of sales for that block.

  * An assessment of **vacantLots**, **unitsPerSquareMile**, and **foreclosures** reveals that if there are more vacant lots on a block, there will be fewer units per square mile and fewer sales.

Explain to students that parallel coordinate plots are used to visualize multivariate analysis. This type of analysis is best suited when there are more than two variables.

* An example use case for Parallel Coordinates plot would be analyzing the quality of a diamond. Variables of interest would be cut, color, carat, clarity, and price. Parallel Coordinates would show how any of these attributes can affect the other.

* Communicate that Parallel coordinate plots allow for multiple variables to be represented in parallel to one another. This is particularly valuable when tracing the relationships between variables and how each variable relates to/affects the other.

  * Continuing with the previous example, this would mean each type of car would have it's own vertical, and each vertical would be aligned in parallel. Relationships between each car would be identified by a line that connects each data point.

* Break down the anatomy of the plot, emphasizing the components below.

  * Point out the verticals on the plot. Each vertical represents a different variable. Because each variable can have a different range of numeric values, the scale of each vertical is specific to that variable. This would mean each vertical could have a different scale.

  * Point out the colored lines on the plot. A line is used to represent a row from the DataFrame. A line will connect each attribute for that given row, which enables analysts to spot trends and track the related attributes/values.

    * Each line is color coded to help assist in tracing the relationships. This is especially valuable when going from looking at data from a row point of view to looking at a visualization.

Ask if there are any questions before moving on.
