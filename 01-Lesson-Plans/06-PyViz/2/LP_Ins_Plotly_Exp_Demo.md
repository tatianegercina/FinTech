### 4. Instructor Do: Plotly Express Demo (5 mins)

By the end of this activity, students will have received a direct, live coding demonstration of creating **Plotly Express** plots. The goal is to demonstrate to students the ease and efficiency of creating plots using the **Plotly Express** `iplot` plotting interface.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/choose-maryland-compare-counties-quality-of-life-78090/resource/affe2417-de10-42cd-90cd-9dd9447d6de5).

**Files:**

* [plotly_demo.ipynb](Activities/04-Ins_Plotly_Exp_Demo/Unsolved/plotly_demo.ipynb)

Communicate to students that working with **Plotly Express** is going to be similar to working with all of the other plotting APIs covered in this class so far. The only difference is the type of charts and underlying technology used to create those charts.

Open the starter file provided, and live code how to create a **scatter** plot using **Plotly Express**.

* Import the **Plotly Express** library, and prepare the data set. Because **Plotly Express** abstracts over Pandas (like hvPlot), data for visualization should be stored in a Pandas DataFrame.

  ```python
  import plotly_express as px
  import pandas as pd

  # Read in data
  md_housing_sales = pd.read_csv(Path('../Resources/maryland_sales_data.csv'))
  md_housing_sales.head()
  ```

* Create a **scatter** plot using the Maryland Real Estate housing sales data. Correlate average sale price to cost of living index to confirm that average sale price will increase exponentially with cost of living index, as expected.

  * Use **Cost of Living Index** as `x`.

  * Use **Average Sale Price** as `y`.

  * Control the size of the circles by setting size to equal **Number of Housing Units Sold**.

  * Color code the plot by **Country**.

  ```python
  # Create scatter plot comparing average sale price and cost of living index
  px.scatter(md_housing_sales,
            x='Cost of Living Index',
            y='Average Sale Price',
            size='Number of Housing Units Sold',
            color='County')
  ```

    ![plotly_scatter.png](Images/plotly_scatter.png)

  * Create another **scatter** plot comparing cost of living index to number of housing units sold to determine if higher cost of living index can be correlated to the number of sales.

    * Use **Cost of Living Index** as `x`.

    * Use **Number of Housing Units Sold** as `y`.

    * Use **Average Sale Price** to determine the size of the data circles.

    * Color code the plot by **Country**.

  ```python
  # Create scatter plot comparing number of housing units sold with cost of living index
  px.scatter(md_housing_sales,
            x='Cost of Living Index',
            y='Number of Housing Units Sold',
            size='Average Sale Price',
            color='County')
  ```

    ![plotly_scatter_2.png](Images/plotly_scatter_2.png)

Use the **Plotly Express** interactivity features and widget bar to interact with the visualization.

  * Hover over the circles to review actual data

  * Use the **zoom** widget to zoom in on counties with a cost of living index between 100 and 110.

      ![plotly_interaction.gif](Images/plotly_interaction.gif)

If time remains, ask students some of the following guided questions:

* What story does these visualizations tell about the real estate market in Maryland?

  * **Answer** The higher the cost of living, the higher number of housing units sold. More homes are being sold in areas with a higher cost of index, which can be related to the quality of the homes, population size of the counties, etc. It also shows that more and more individuals are gravitating towards the areas with higher cost.

* Which country could be an up and coming area real-estate opportunity? Why?

  * **Answer** Baltimore City. Baltimore city has an average real-estate sale price of less than 200k, and the cost of living index is only 1.3% higher. This county has the cheapest prices with decent sales volume. Because of the number of sales, it seems the market is active with buying opportunity. While it might be too late to get involved, it's definitely a hot spot.

Ask if there are any questions, and then move onto the student activity.
