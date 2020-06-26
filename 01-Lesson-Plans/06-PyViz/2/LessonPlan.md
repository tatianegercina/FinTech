## 6.2 Lesson Plan: Plotting with Plotly Express

### Overview

By the end of this class, students will have added another PyViz visualization technology to their skillsets. Today's lesson focuses on **Plotly Express**, a visualization module built on top of **Plotly**. Like hvPlot, Plotly Express is an interactive plotting library that supports PyViz and Pandas.

Students are learning Plotly Express because it has risen to be an industry standard among data scientists and analysts. Plotly Express offers advanced statistical plots, like **parallel categories** and **parallel coordinates**, which many other plotting interfaces do not (e.g., hvPlot). Having knowledge and experience with Plotly Express will give students an upper hand in the job market, and it will enable them to create visualizations and reports that are on the same caliber as those by data scientists.

### Class Objectives

By the end of class, students will be able to:

* Define common uses cases for Plotly Express

* Set up a Plotly Express environment

* Complete Plotly interactive plots

* Store MapBox API key as an environment variable and authenticate

* Integrate MapBox API with Plotly

* Construct map plot visualizations

### Instructor Notes

* Prepare for the lesson by running the code examples and reviewing the lectures before class. Today's lesson will include using Plotly Express and Mapbox, a mapping API/development kit used for visualizing geospatial data, so make sure the appropriate plugins and API keys have been set up.

* Because this lesson is using an API, make sure to sign up for a Mapbox API key using this [link](https://account.mapbox.com/auth/signup/). Create a `.env` file to store your API key, and use `python-dotenv` to make it callable in Python.

* Throughout the day, reinforce to students the importance and power of interactive plotting. The widgets, automatic color formatting and skins, and plot types can all be accessed and manipulated with ease. The plots being created by Plotly Express would have taken someone in the past hours to create. Plotly Express does it in seconds.

* Keep pacing in mind while progressing through the day. Allow students to ask questions. When necessary, ask students to save questions for the review sessions. Encourage students to collaborate on activities.

* The pace should feel urgent, but not rushed. Check for understanding regularly, and circulate the classroom with the TAs during activities to offer your assistance. Stick to the Time Tracker as closely as possible. Encourage confused students to attend office hours.

* Slack out the PyViz install guide to students so that they have ample time to install and confirm the installation of Plotly Express and its Jupyter plugin.

* If students have issues with plots rendering blank in the Jupyter Lab preview, have them refer to the [troubleshooting section](../Supplemental/PyVizInstallationGuide.md#troubleshooting) of the PyViz Installation Guide.

* Due to the amount of content that needs to be covered in this lesson, there will be no class time dedicated to system checks. Communicate to students that they must have Plotly Express installed and running before coming to class. Any challenges or issues should be worked out with a TA.

* Have your TAs keep track of time with the Time Tracker.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [6.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5be4b5c1-1085-4071-8236-aab80143e360) Note that this video may not reflect the most recent lesson plan.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson 6.2 Slides](https://docs.google.com/presentation/d/19qivsXUwDt_RDsHQ3qRJzgSXlDLEOJmsXpPqSFhxG9A/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

**Files:**

Welcome students back! Indicate that today will start day 2 of interactive visualizations using PyViz.

Begin the class explaining to students that **hvPlot** is not the only visualization package that can be used to create interactive visualizations.

* Plotly Express is a package similar to hvPlot, offering many of the same plots as hvPlot (bar, line, scatter, etc.) but more as well (e.g., parallel coordinates and parallel categories plots).

* Plotly Express is a favorite among the data science and web-based data visualization communities.

* Plotly Express is a leader in data visualization and supports multiple programming languages, like Python, JavaScript, and R.

* Emphasize that Plotly Express offers advanced statistical and financial charts that technologies are lacking in technologies like hvPlot.

* Indicate that by the end of this class, students will have learned how to create visualizations using Plotly Express and have gained knowledge and skills that data scientists and analysts are using in the industry today.

If time remains, provide students with some sample visualizations of the types of plots being made with Plotly Express. Use this [site](https://plot.ly/python/plotly-express/#visualize-distributions) for examples.

* Use the left navigation pane, and select the following pages. Remember to highlight and focus on how Plotly's unique plot types work toward telling a story.

  * [Scatter and Line Plots](https://plot.ly/python/plotly-express/#scatter-and-line-plots)

  * [Visualize Distributions](https://plot.ly/python/plotly-express/#visualize-distributions)

  * [Ternary Visualizations](https://plot.ly/python/plotly-express/#ternary-coordinates)

  * [Maps](https://plot.ly/python/plotly-express/#maps)

Ask if there are any questions before moving on.

- - -

### 2. Instructor Do: Plotly Express Demo (10 min)

**Corresponding Activity:** [01-Ins_Plotly_Exp_Demo](Activities/01-Ins_Plotly_Exp_Demo)

By the end of this activity, students will have received a live coding demonstration of creating Plotly Express plots. The goal is to demonstrate to students the ease and efficiency of creating plots using the Plotly Express **scatter** plot interface.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/choose-maryland-compare-counties-quality-of-life-78090/resource/affe2417-de10-42cd-90cd-9dd9447d6de5).

**Files:**

* [plotly_demo.ipynb](Activities/01-Ins_Plotly_Exp_Demo/Unsolved/plotly_demo.ipynb)

Navigate to the 6.2 slides, and quickly highlight the following:

* Plotly Express works much like hvPlot, giving users a simple `plot` based interface that allows developers to create and customize interactive visualizations.

* Plotly Express is packaged and powered by the Plotly library, an open-source graphing library for Python.

* In addition to the chart types we've already seen (e.g., scatter, line, and bar), Plotly Express includes charting types such as parallel coordinates and parallel categories, plot types that are useful when visualizing correlations and the relationships between data points.

    ![example_plotly_plots_3.gif](Images/example_plotly_plots_3.gif)

    ![example_plotly_plots_4.gif](Images/example_plotly_plots_4.gif)

Communicate to students that working with Plotly Express is going to be similar to working with all of the other plotting APIs covered in this class so far. The only difference is the type of charts and underlying technology used to create those charts.

Open the starter file provided and live code, creating a scatter plot using Plotly Express.

* Import the Plotly Express library, and prepare the dataset because Plotly Express abstracts over Pandas (like hvPlot), data for visualization should be stored in a Pandas DataFrame.

  ```python
  import plotly_express as px
  import pandas as pd

  # Read in data
  md_housing_sales = pd.read_csv(Path('../Resources/maryland_sales_data.csv'))
  md_housing_sales.head()
  ```

* Create a scatter plot using the Maryland real estate housing sales data. Correlate average sale price to the cost of living index to confirm that average sale price will increase exponentially with the cost of living index, as expected.

  * Use Cost of Living Index as `x`.

  * Use Average Sale Price as `y`.

  * Control the size of the circles by setting the size to equal Number of Housing Units Sold.

  * Color code the plot by County.

  ```python
  # Create scatter plot comparing average sale price and cost of living index
  px.scatter(md_housing_sales,
            x='Cost of Living Index',
            y='Average Sale Price',
            size='Number of Housing Units Sold',
            color='County')
  ```

    ![plotly_scatter.png](Images/plotly_scatter.png)

* Create another scatter plot comparing the cost of living index to the number of housing units sold to determine if the higher cost of living index can be correlated to the number of sales.

  * Use **Cost of Living Index** as `x`.

  * Use **Number of Housing Units Sold** as `y`.

  * Use **Average Sale Price** to determine the size of the data circles.

  * Color code the plot by **County**.

  ```python
  # Create scatter plot comparing number of housing units sold with cost of living index
  px.scatter(md_housing_sales,
            x='Cost of Living Index',
            y='Number of Housing Units Sold',
            size='Average Sale Price',
            color='County')
  ```

    ![plotly_scatter_2.png](Images/plotly_scatter_2.png)

Use the Plotly Express interactivity features and widget bar to interact with the visualization.

  * Hover over the circles to review actual data

  * Use the **zoom** widget to zoom in on counties with a cost of living index between 100 and 110.

      ![plotly_interaction.gif](Images/plotly_interaction.gif)

If time remains, ask students some of the following questions:

* What story do these visualizations tell about the real estate market in Maryland?

  * **Answer** The higher the cost of living, the higher the number of housing units sold. More homes are being sold in areas with a higher cost of the index, which can be related to the quality of the homes, the population size of the counties, etc. It also shows that more and more individuals are gravitating toward the areas with higher cost.

* Which county could be an up-and-coming real-estate opportunity? Why?

  * **Answer** Baltimore City. Baltimore City has an average real-estate sale price of less than $200,000, and the cost of living index is only 1.3% higher. This county has the lowest prices with decent sales volume. Because of the number of sales, it seems the market is active with buying opportunities. While it might be too late to get involved, it's definitely a hot spot.

Ask if there are any questions, and then move on to the student activity.

- - -

### 3. Students Do: Plotting with Plotly (10 min)

**Corresponding Activity:** [02-Stu_Plotting_w_Plotly](Activities/02-Stu_Plotting_w_Plotly)

Students complete an activity where they create scatter plots using Plotly Express. This activity will reinforce to students that while Plotly Express has the same plotting APIs as other technologies, Plotly Express's provides their own flavors and twists.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/allegheny-county-mortgage-foreclosure-records).

**Instructions:**

* [README.md](Activities/02-Stu_Plotting_w_Plotly/README.md)

**Files:**

* [plotting_w_plotly.ipynb](Activities/02-Stu_Plotting_w_Plotly/Unsolved/Core/plotting_w_plotly.ipynb)

- - -

### 4. Instructor Do: Plotting with Plotly Activity Review (10 min)

Students and instructors participate in a dry walkthrough of the solution for the previous activity.

**Files:**

* [plotting_w_plotly.ipynb](Activities/02-Stu_Plotting_w_Plotly/Solved/Core/plotting_w_plotly.ipynb)

Open the solution and conduct a dry walkthrough.

* Plotly Express can be used to create scatter plots. This can be done by making a call to the `scatter` function.

  ```python
  # Read in data
  foreclosures = pd.read_csv(Path('../../Resources/allegheny_foreclosures.csv'),
                            infer_datetime_format= True,
                            parse_dates=True,
                            index_col='filing_date')

  # Slice data and group
  foreclosures_grp = foreclosures[['municipality','amount']].groupby([
      foreclosures.index.year,'municipality']).count().reset_index()
  foreclosures_grp.head()

  # Create scatter plot
  px.scatter(foreclosures_grp,
            x='municipality',
            y='amount',
            color='filing_date')
  ```

    ![plotly_example_scatter.png](Activities/02-Stu_Plotting_w_Plotly/Images/plotly_example_scatter.png)

Explore the data with the students. Encourage students to follow along and complete the same interactions.

* Zoom in on the municipalities with the highest number of foreclosures.

  ![explore_highest_foreclosures.gif](Images/explore_highest_foreclosures.gif)

* Zoom in on the City of Clairton data points. Use the box select widget to highlight only the City of Clairton data (which will also fade out any other data points reflected at the time). Deep dive into the data for 2014.

  * Communicate to students that interactive visualizations allow users to get a closer look into outlying data points, which could communicate a need for further investigation and data exploration to understand the outlier better. The City of Clairton data for 2014 is one such example. This data could be considered an outlier or data quality issue, either way the visualization shows us that we need to take a closer look.

  * Without the ability to interact with data points via technologies like Plotly Express, spotting outliers could be like spotting a needle in a haystack. The process would be less efficient and arguably less effective.

  ![explore_outlier.gif](Images/explore_outlier.gif)

Ask for any remaining questions before moving on.

- - -

### 5. Instructor Do: Parallel Coordinate Plot (10 min) (Critical)

**Corresponding Activity:** [03-Ins_Parallel_Coordinate](Activities/03-Ins_Parallel_Coordinate)

In this activity, students are introduced to one of the more advanced statistical plots that Plotly has to offer: the parallel coordinate plot. This will be a completely new plot for students, not having been seen in Pandas, Matplotlib, or hvPlot.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/2011-housing-market-typology-a6419).

**Files:**

* [parallel_coordinate.ipynb](Activities/03-Ins_Parallel_Coordinate/Solved/parallel_coordinates.ipynb)

Open the solved solution file and conduct a dry walkthrough. While walking through the solved file, highlight the below discussion points. Make sure to place particular emphasis on the what and why of parallel coordinate plots so students understand their use case and when they should be applied.

Walkthrough the syntax required to create a parallel coordinate plot:

* The parallel coordinate plot can be created using the `parallel_coordinates` function.

  ```python
  import plotly.express as px
  import pandas as pd
  from pathlib import Path

  # Read in data
  typology = pd.read_csv(Path('../Resources/housing_market_typology.csv'))[:30].sort_values('blockGroup')

  # Create Parallel Coordinates plot
  px.parallel_coordinates(typology, color='blockGroup')
  ```

  ![parallel_coordinates.gif](Images/parallel_coordinates.gif)

* Communicate that parallel coordinate plots allow for multiple variables to be represented in parallel to one another. This is particularly valuable when tracing the relationships between variables and how each variable relates to and affects the other.

* By sorting the axes and filtering values, analysts can cluster attributes to assess relationships and trends.

  * For example, sorting so that **vacantLots** and **sales20092010** are adjacent allows one to see how the number of vacant lots affects the number of sales for that block.

  * An assessment of vacantLots, **unitsPerSquareMile**, and **foreclosures** reveals that if there are more vacant lots on a block, there will be fewer units per square mile and fewer sales.

Reinforce to students that parallel coordinate plots are used to visualize multivariate analysis by providing example use cases.

* Another use case for a parallel coordinate plot would be analyzing the quality of a diamond. Variables of interest would be cut, carats, clarity, and price. Parallel coordinates would show how any of these attributes can affect the other.

Break down the anatomy of the plot, emphasizing the components below.

* Point out the verticals on the plot. Each vertical represents a different variable. Because each variable can have a different range of numeric values, the scale of each vertical is specific to that variable. This would mean each vertical could have a different scale.

* Point out the colored lines on the plot. A line is used to represent a row from the DataFrame. A line will connect each attribute for that given row, which enables analysts to spot trends and track the related attributes and values.

  * Each line is color-coded to help assist in tracing the relationships. This is especially valuable when going from looking at data from a row point of view to looking at a visualization.

Ask if there are any questions before moving on.

- - -

### 6. Student Do: Plotting in Parallel (15 min)

**Corresponding Activity:** [04-Stu_Parallel_Coordinates](Activities/04-Stu_Parallel_Coordinates)

Students complete a bridge activity where they revisit a previously used dataset that was visualized using scatter plots. Students now visualize the data using a parallel coordinates plot.

This will be the students' first time working with parallel coordinate plots. Instruct TAs to circulate to provide assistance. Encourage students who finish early to assist their classmates.

**Instructions:**

* [README.md](Activities/04-Stu_Parallel_Coordinates/README.md)

**Files:**

* [plotting_in_parallel.ipynb](Activities/04-Stu_Parallel_Coordinates/Unsolved/Core/plotting_in_parallel.ipynb)

- - -

### 7. Instructor Do: Parallel Coordinates Activity Review (5 min)

**Files:**

* [plotting_in_parallel.ipynb](Activities/04-Stu_Parallel_Coordinates/Solved/Core/plotting_in_parallel.ipynb)

Kick off the review session by asking some of the questions below.

* What's the function used to create a parallel coordinate plot?

  * **Answer:** `plotly.express.parallel_coordinates()`

* What's the difference between a scatter plot and a parallel coordinate plot?

  * **Answer:** Scatter plots visualize the relationship between two data points as an intersection. Parallel coordinate plots visualize the relationship between two data points as parallel axes.

  * **Answer:** **Scatter plots** inherently use two axes. Whereas, parallel coordinates are built for multivariate analysis and can have 2-plus axes.

* In terms of interaction, which plot do you feel allows you to gain more value from the interaction?

  * **Answer:** The parallel coordinate plot offers limited opportunities for interaction, which makes the scatter plot more fitted for interacting with plots. However, parallel coordinate plots structurally allow for relationships to be traced more effectively and efficiently.

* What is the difference between the types of interactions provided by these different plots?

  * **Answer:** Parallel coordinate plots can only be sorted and filtered/highlighted. Scatter plots can be zoomed, panned, filtered, etc.

If time remains, open the solution, and highlight the following:

* Parallel coordinate plots present plot axes in a parallel fashion. This allows data points to be traced from one variable to the next.

  * Increases and decreases can be visually spotted by the lines that connect data points to one another. This structure allows variables to be analyzed in relation to another.

  ![parallel_relationships.gif](Images/parallel_relationships.gif)

Ask for any remaining questions before moving on.

- - -

### 8. Break (15 min)

- - -

### 9. Instructor Do: Parallel Categories (10 min) (Critical)

**Corresponding Activity:** [05-Ins_Parallel_Categories](Activities/05-Ins_Parallel_Categories)

In this activity, students continue learning about more advanced statistical plots, like the parallel categories plot by way of an instructor demo. The instructor will demonstrate to students how to create a parallel categories plot, as well as highlight the differences between parallel categories and parallel coordinates.

**Files:**

* [parallel_categories.ipynb](Activities/05-Ins_Parallel_Categories/Solved/parallel_categories.ipynb)

Navigate to the 6.2 slides, and highlight the following:

* Whereas parallel coordinate plots are used for multivariate analysis and mapping relationships between variables, parallel categories plots are used to perform **multidimensional** analysis.

  * An example of multidimensional analysis would be looking at sales and foreclosures data by housing type, region, and the number of units. Housing type, region, and the number of units would be good dimensions to consider.

* **Dimensions** are considered to be categories**. **Parallel categories plots focus on connecting the dots between each category and assessing the nuances per category and the impact of categories on other categories.

Open the [starter file](Activities/05-Ins_Parallel_Categories/Solved/parallel_categories.ipynb), and live code the following:

* Parallel categories plots can be created using the `parallel_categories` function.

  ```python
  # Prep Data
  housing_type= ['Single Family','Multi-Family','Apartment']
  region= ['North East','Tri-State']
  prop_size= ['Large','Medium','Small']

  df = pd.DataFrame({
      "sold": np.random.randint(999, 1002, 30),
      "year": np.random.randint(2010, 2019, 30),
      "type": np.random.choice(housing_type, 30),
      "region": np.random.choice(region, 30),
      "prop_size": np.random.choice(prop_size, 30)}).sort_values(['year',
                                                                  'type',
                                                                  'region',
                                                                  'prop_size'])
  df.head()
  ```

  ![parallel_categories.png](Images/parallel_categories.png)

* To make sure plots are structured the correct way, use the `dimensions` parameter to hard code what the dimensions should be.

  ```python
  px.parallel_categories(df, dimensions=['type','region','prop_size'], color='year',
                        color_continuous_scale=px.colors.sequential.Inferno)
  ```

* The labels parameter can be used to customize the labels shown on the plot. It will also add a highlight feature to the label names so they can be read.

  ```python
  # Plot data using parallel_categories
  px.parallel_categories(df, dimensions=['type','region','prop_size'], color='year',
                        color_continuous_scale=px.colors.sequential.Inferno,
                        labels={
                            'type': 'Type of Dwelling',
                            'region': 'Region',
                            'prop_size': 'Property Size'})
  ```

* Similar to parallel coordinates plot, the parallel categories plot axes can be sorted by clicking and dragging to the desired location.

  ![sort_categories.gif](Images/sort_categories.gif)

- - -

### 10. Student Do: Categorical Property Evaluation (15 min)

**Corresponding Activity:** [06-Stu_Categorical_Evaluation](Activities/06-Stu_Categorical_Evaluation)

Students complete an activity and code out a parallel categories plot. Students will use the plot to visualize the dimensions and categories evaluated during real estate property assessments.

Encourage students to work in teams and collaborate on the information-seeking process. Indicate that even when working in teams, each student will still need to complete the activity.

* Instruct the TAs to circulate to provide the teams with any troubleshooting assistance.

Additionally, keep an eye out during the activity for students who finish early. Find a student volunteer who is willing to present and describe the story being told by the documentation. Explain to the volunteer that they will have to present their plot to the class and tell the story of the data by interacting with the plot.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/allegheny-county-property-assessments).

**Instructions:**

* [README.md](Activities/06-Stu_Categorical_Evaluation/README.md)

**Files:**

* [Categorical_Evaluation.ipynb](Activities/06-Stu_Categorical_Evaluation/Unsolved/categorical_evaluation.ipynb)

- - -

### 11. Students Do: Categorical Property Evaluation Activity Review (10 min)

This activity involves student volunteering to tell the story of Alleghany property assessments. A student will present the parallel categories plot from the student activity and provide some findings regarding dimensional patterns.

This activity is a revised version of the turn and teach activity type; however, instead of students working as teams, one student will lead the teaching.

**Files:**

* [categorical_property_evaluation.ipynb](Activities/06-Stu_Categorical_Evaluation/Solved/categorical_evaluation.ipynb)

Open the solution and ask the student that volunteered to present the plot and relay their findings. Use the below discussion points to help facilitate the review.

* The parallel categories plot is created using the `parallel_categories` function provided with **Plotly.express** package.

    ```python
    # Plot data
    px.parallel_categories(data, dimensions=['USEDESC','TOTALROOMS','BEDROOMS','FULLBATHS'], color='LOCALTOTAL')
    ```

    ![stu_parallel_categories.png](Images/stu_parallel_categories.png)

* Since parallel categories plots involve multidimensional analysis, dimensions can be specified using the `dimensions` attribute.

  ![stu_parallel_categories_dimensions.png](Images/stu_parallel_categories_dimensions.png)

* The line coloring of the plot can be changed using the `color` attribute. This will help spot trends in the data.

  ![stu_parallel_categories_color.png](Images/stu_parallel_categories_color.png)

If time remains, initiate the storytelling piece of the review by asking the student some of the following guided questions:

* Are there any identifiable patterns at the dimension level?

  * **Answer:** Most sales were single-family homes

  * **Answer:** Most homes have three bedrooms.

* How many bedrooms and full bathrooms do single-family homes tend to have commonly?

  * **Answer:** Three bedrooms one bath.

* What type of patterns can be seen when correlating the total number of rooms and bedrooms?

  * **Answer:** The homes that have evaluated at the highest local price are the ones that have twice as many total rooms as bedrooms.

  * **Answer:** Housing value is more affected by the total number of rooms and bedrooms than full baths.

* Is there an identifiable story being told through the data? What is the story?

  * **Answer:** Total number of rooms, bedrooms, and bathrooms are all used to assess a property and its value. The more rooms and bedrooms, the higher the sale price. Most single-family homes being assessed in Allegheny County 2019 have around six total rooms, three bedrooms, and one full bath.

  * **Answer:** The houses evaluated at the highest costs tend to have more than five total rooms.

- - -

### 12. Instructor Do: Mapbox API Demo (10 min) (Critical)

**Corresponding Activity:** [07-Ins_Mapbox_Demo](Activities/07-Ins_Mapbox_Demo)

In this activity, students observe a demonstration of how to use the Mapbox API with Plotly Express.

To complete this activity, a Mapbox API will be required. A personal key can be obtained by signing up [here](https://account.mapbox.com/auth/signup/).

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/500-cities-local-data-for-better-health-fc759).

**Files:**

* [plotly_maps.ipynb](Activities/07-Ins_Mapbox_Demo/Unsolved/plotly_maps.ipynb)

Navigate to the 6.2 slides, and highlight the following:

* Mapbox API is an open-source API that gives developers a range of mapping visualizations and functions that enable the creation of interactive map plots.

* Mapbox API is democratizing the map services industry (e.g., navigation and cartography), similar to how Plaid is doing this for FinTech.

* Mapbox offers three main services: maps, navigation, and search.

  * These services come with handy tools, such as map styles and vectors, map images and datasets, and live location.

Open the starter file, and live code the following. Make sure to have your Mapbox API key handy. Highlight the discussion points while coding:

* Plotly Express has an integration endpoint specific for Mapbox API. This allows Plotly to use the Mapbox Maps API in order to create interactive map visualizations. Plotly Express comes with functions designed specifically for interacting with Mapbox.

  * Plotly's integration with Mapbbox makes it extremely convenient to use; no other imports are required. All that is needed is the Plotly Express library.

* The Mapbox API uses API keys to monitor API requests. The Mapbox API key needs to be set up as an environment variable. The `os.getenv` function can then be used to retrieve the key within Python code.

  ```python
  # Read the Mapbox API key
  load_dotenv()
  map_box_api = os.getenv("mapbox")
  ```

* Once the environment variable is ready and available in Python, it can be registered with Plotly. Plotly provides a function to do this: `set_mapbox_access_token`.

  * Because Plotly Express will broker the client-server relationship, the Mapbox API key has to be set/registered with Plotly Express.

  ```python
  px.set_mapbox_access_token(map_box_api)
  ```

* After the token is set with the `set_mapbox_access_token`, the Plotly Express mapbox plot functions can be used to create geographic plots.

Demonstrate how to create a map scatter plot using the Plotly Express `scatter_mapbox` function.

* The `scatter_mapbox` function can be used to create a scatter plot that is overlaid on top of a map (provided by Mapbox). This allows for scatter plot data to be analyzed in reference to geographical location.

```python
# Read in data
df = pd.read_csv(Path("../Resources/population_counts.csv")).drop_duplicates()
data_to_plot = df[["Year", "PopulationCount", "Latitude", "Longitude"]]
filtered_data = df[df["StateDesc"] == "California"]

# Plot Data
map = px.scatter_mapbox(
    filtered_data,
    lat="Latitude",
    lon="Longitude",
    size="PopulationCount",
    color="CityName",
    zoom=4
)

# Display the map
map.show()
```

  ![scatter_map_plot.gif](Images/scatter_map_plot.gif)

* It's important to note that map plots can be a little more memory intensive than the plots we are used to.

  * Datasets should be filtered and aggregated to the highest level of granularity possible (without jeopardizing reporting context) so that plots do not take long to load.

  * Sampling techniques (e.g., visualizing only top *n* items) to help reduce the amount of data being reflected on the visualization. These approaches will preserve reporting integrity.

Note to students that when datasets become too large to manage or reduce, technologies like [Datashader](http://datashader.org) can also be considered. Datashader specializes in turning large volumes of data into visualizations.

* Encourage students to look into technologies like Datashader outside of class.

Ask for any questions before moving onto the student activity.

- - -

### 13. Students Do: Mapping Adventures (15 min)

**Corresponding Activity:** [08-Stu_Mapping_Adventures](Activities/08-Stu_Mapping_Adventures)

Students repeat the steps demonstrated by the instructor in order to create their own Plotly Mapbox scatter plots. Students will integrate Plotly and Mapbox to create their first geographical visualizations.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/areas-of-interest-gis).

**Instructions:**

* [README.md](Activities/08-Stu_Mapping_Adventures/README.md)

**Files:**

* [mapping_adventures.ipynb](Activities/08-Stu_Mapping_Adventures/Unsolved/Core/mapping_adventures.ipynb)

- - -

### 14. Instructor Do: It's a Map Plot Activity Review (10 min)

This review activity will consist of two parts. The first part will be a dry walkthrough of the Mapping Adventures student assignment. The second will consist of a facilitated discussion and student presentation of the top places they'd go to for Harold's birthday.

**Files:**

* [mapping_adventures.ipynb](Activities/08-Stu_Mapping_Adventures/Solved/Core/mapping_adventures.ipynb)

Open the solution and conduct a dry walkthrough:

* The marriage between Plotly Express and Mapbox has enabled developers to create interactive map visualizations.

* Using Mapbox's API, Plotly can render geographic plots, such as the scatter mapbox plot. The scatter mapbox plot is the classic scatter plot overlaid on top of a map.

  ![plotting_adventures.gif](Images/plotting_adventures.gif)

* The scatter mapbox plot can be created using the `scatter_mapbox` function. The function has three key parameters: DataFrame, latitude field, and longitude field. Color is also an acceptable argument, which accepts a DataFrame column as its value.

  ![scatter_mapbox.png](Images/scatter_mapbox.png)

Next, transition into the presentation portion of the review.

* Ask if any students would like to present the three places they'd choose to go to. If no one volunteers to present, go around the room round-robin style in place of volunteers.

Ask for any remaining questions before moving on.

- - -

### 15. Students Do: A Cartographer's Expedition (20 min)

**Corresponding Activity:** [08-Stu_Mapping_Adventures](Activities/08-Stu_Mapping_Adventures)

Students create map plots to embark on a virtual expedition through New York City to various places of interest.

Indicate to students that they should work in teams of two or three to plan the trip together.

**Instructions:**

* [README.md](Activities/09-Stu_Cartographers_Expedition/README.md)

**Files:**

* [cartographers_expedition.ipynb](Activities/09-Stu_Cartographers_Expedition/Unsolved/cartographers_expedition.ipynb)

- - -

### 16. Instructor Do: A Cartographers Expedition Activity Review (10 min)

In this activity, student groups will present their maps and expeditions to the rest of the class.

**Files:**

* [cartographers_expedition.ipynb](Activities/09-Stu_Cartographers_Expedition/Solved/cartographers_expedition.ipynb)

Start the activity review by asking if there is a group that wants to volunteer to present their expedition first. Then, ask the following questions. If time remains, ask for a second group to also present.

* Ask the group to present their maps and to relay their full expedition.

  * **Answer:** Airport -> Aqueduct Race Track -> Astoria Park -> Fort Totten -> Juniper Valley Park -> Madison Square

* Sometimes, it's difficult to get a good understanding of whether or not two locations are close to each other. Were there any instances where you had to re-choose locations due to them being too far away?

  * **Answer:** Yes. When picking locations at random, it was hard to determine which points would be close to each other.

* What are some programmatic approaches to making sure locations are close to each other?

  * **Answer:** The data could be sorted by latitude and longitude.

  * **Answer:** Data could have been sliced by borough first, and then places chosen from there.

* What guided your final decision on locations?

  * **Answer:** Locations were chosen based on categorical type and proximity. Locations of type garden, park, and square were chosen for a specific experience.

* Were the geographic scatter plots helpful in understanding the distribution of places of interest throughout New York City? How did the visual help cement the image?

  * **Answer:** Yes, the plots were helpful. By color-coding by **PlaceType**, it was easy to see the clusters of each type of place. This helped outline the trek through the boroughs. It was also helpful in noticing trends in the positioning of certain locations (e.g., Ellis and Liberty islands are in the same place, and the forts all seem to be north of Manhattan).

If time remains, ask students to summarize three things they've learned today.

* **Answer:** Parallel coordinates and categories plots use vertical axes to visualize multivariate analysis and variable relationships.

* **Answer:** Map plots can be used to visualize clusters of data points geographically.

* **Answer:** Parallel coordinates and categories plots allow users to visualize correlations but also reorganize variables in order to get a better sense of multivariate relationships.

Ask for any remaining questions before ending the class.

### End Class

- - -

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
