# 6.2 Lesson Plan: Plotting with Plotly Express

## Overview

By the end of this class, students will have added another PyViz visualization technology to their skillsets. Today's lesson focuses on **Plotly Express**, a visualization module built on top of **Plotly**. Like hvPlot, **Plotly Express** is an interactive plotting library that supports PyViz and Pandas.

Students are learning **Plotly Express** because it has risen to be an industry standard among data scientists and analysts. **Plotly Express** offers advanced statistical plots, like **parallel categories** and **parallel coordinates**, which many other plotting interfaces do not (i.e. hvPlot). Having knowledge and experience with **Plotly Express** will give students an upper-hand in the job market, and it will enable them to create visualizations and reports that are on the same caliber as data scientists.

## Class Objectives

By the end of class, students will be able to:

* Define common uses cases for Plotly Express

* Set up Plotly Express Environment

* Complete Plotly Interactive Plots

* Store MapBox API key as environment variable and authenticate

* Integrate MapBox API with Plotly

* Construct Map Plot Visualizations

## Instructor Notes

* Prepare for the lesson by running the code examples and reviewing the lectures before class. Today's lesson will include using **Plotly Express** and **Mapbox**, a mapping API/development kit used for visualizing geospatial data, so make sure the appropriate plugins and API keys have been set up.

* Because this lesson is using an API, make sure to sign up for a Mapbox API key using this [link](https://account.mapbox.com/auth/signup/). Create a `keys.sh` file to store your API key, and source it so that it is callable in Python. You can add the source command to your `bash_profile` or `bashrc` file in your home directory.

* Throughout the day, reinforce to students the importance and power of interactive plotting. The widgets, automatic color formatting and skins, and plot types can all be accessed and manipulated with ease. The plots being created by **Plotly Express** would have taken someone in the past hours to create. **Plotly Express** does it in seconds.

* Keep pacing in mind while progressing through the day. Give students the opportunity to ask questions. When necessary, ask students to save questions to the review sessions. Encourage students to collaborate on activities.

* Be mindful of the class pacing; the pace should feel urgent, but not rushed. Check for understanding regularly, and circulate the classroom with the TAs during activities to offer your assistance. Stick to the Time Tracker as closely as possible. Encourage students who are confused to attend office hours.

* Slack out the PyViz install guide to students so that they have ample time to install/confirm installation of **Plotly Express** and its Jupyter plugin.

* Due to the amount of content that needs to be covered in this lesson, there will be no class time dedicated to system checks. Communicate to students that they must have **Plotly Express** installed and running prior to coming to class. Any challenges/issues should be worked out with a TA.

* Have your TAs keep track of time with the Time Tracker.

## Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson 6.2 Slides]().

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 mins)

**Files:**

* [Welcome-slides]()

Welcome students back! Indicate that today will start day 2 of interactive visualizations using PyViz.

Begin the class explaining to students that **hvPlot** is not the only visualization package that can be used to create interactive visualizations.

* **Plotly Express** is a package similar to **hvPlot**, offering many of the same plots as **hvPlot** (i.e. bar, line, scatter, etc.) but more as well (i.e. **Parallel Coordinates** and **Parallel Categories plots**).

* **Plotly Express** is a favorite among the data science and web-based data visualization communities.

* **Plotly Express** is a leader in data visualization and supports multiple programming languages, like Python, JavaScript, and R.

* Emphasize that **Plotly Express** offers advanced statistical and financial charts that technologies are lacking in technologies like **hvPlot**.

* Indicate that by the end of this class, students will have learned how to create visualizations using **Plotly Express** and have gained knowledge and skills that data scientists and analysts are using in the industry today.

If time remains, provide students with some sample visualizations of the types of plots being made with **Plotly Express**. Use this [site](https://plot.ly/python/plotly-express/#visualize-distributions) for examples.

* Use the left navigation pane, and select the following pages. Remember to highlight and focus on how Plotly's unique plot types work towards telling a story.

  * [Scatter and Line Plots](https://plot.ly/python/plotly-express/#scatter-and-line-plots)

  * [Visualize Distributions](https://plot.ly/python/plotly-express/#visualize-distributions)

  * [Ternary Visualizations](https://plot.ly/python/plotly-express/#ternary-coordinates)

  * [Maps](https://plot.ly/python/plotly-express/#maps)

Ask if there are any questions before moving on.

- - -

### 2. Instructor Do: Plotly Express Demo (10 mins)

By the end of this activity, students will have received a live coding demonstration of creating **Plotly Express** plots. The goal is to demonstrate to students the ease and efficiency of creating plots using the **Plotly Express** **scatter** plot interface.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/choose-maryland-compare-counties-quality-of-life-78090/resource/affe2417-de10-42cd-90cd-9dd9447d6de5).

**Files:**

* [plotly_demo.ipynb](Activities/01-Ins_Plotly_Exp_Demo/Unsolved/plotly_demo.ipynb)

Navigate to the 6.2 slides, and quickly highlight the following:

* **Plotly Express** works much like hvPlot, giving users a simple `plot` based interface that allows developers to create and customize interactive visualizations.

* **Plotly Express** is packaged and powered by the **Plotly** library, an open source graphing library for Python.

* In addition to the chart types we've already seen (i.e. scatter, line, and bar), **Plotly Express** also includes charting types such as **Parallel Coordinates** and **Parallel Categories**, plot types that are useful when visualizing correlations and the relationships between data points.

    ![example_plotly_plots_3.gif](Images/example_plotly_plots_3.gif)

    ![example_plotly_plots_4.gif](Images/example_plotly_plots_4.gif)

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

- - -

### 3. Students Do: Plotting with Plotly (10 mins)

Students complete a MSMD activity where they create **scatter** plots using **Plotly Express**. This activity will reinforce to students that while **Plotly Express** has the same plotting APIs as other technologies, **Plotly Express'** provides their own flavor and twist.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/allegheny-county-mortgage-foreclosure-records).

**Instructions:**

* [README.md](Activities/02-Stu_Plotting_w_Plotly/README.md)

**Files:**

* [plotting_w_plotly.ipynb](Activities/02-Stu_Plotting_w_Plotly/Unsolved/Core/plotting_w_plotly.ipynb)

- - -

### 4. Instructor Do: Plotting with Plotly Activity Review (10 mins)

Students and instructor participate in a dry walk through of the solution for the previous activity.

**Files:**

* [plotting_w_plotly.ipynb](Activities/02-Stu_Plotting_w_Plotly/Solved/Core/plotting_w_plotly.ipynb)

Open the solution, and conduct a dry walk through.

* **Plotly Express** can be used to create **scatter** plots. This can be done by making a call to the `scatter` function.

  ```python
  # Read in data
  foreclosures = pd.read_csv(Path('../../Resources/alleghany_foreclosures.csv'),
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

  * Communicate to students that the City of Clairton data for 2014 could be considered an outlier or data quality issue. Interactive visualizations allow users to get a closer look into outlying data points, which could communicate a need for further investigation/data exploration to better understand the outlier.

  * Without the ability to interact with data points via technologies like **Plotly Express**, spotting outliers could be like spotting a needle in a haystack. The process would be less efficient and arguably less effective.

  ![explore_outlier.gif](Images/explore_outlier.gif)

Ask for any remaining questions before moving on.

- - -

### 5. Instructor Do: Parallel Coordinate Plot (10 mins) (Critical)

In this activity, students are introduced to one of the more advanced, statistical plots that Plotly has to offer: the **Parallel Coordinate** plot (by way of an instructor demo). This will be a completely new plot for students, not having been seen in Pandas, Matplotlib, or hvPlot.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/2011-housing-market-typology-a6419).

**Files:**

* [parallel_coordinate.ipynb](Activities/03-Parallel_Coordinate/Solved/parallel_cooridnate.ipynb)

Open the solved solution file and conduct a dry walk through. While walking through the solved file, highlight the below discussion points. Make sure to place particular emphasis on the **what** and **why** of **Parallel Coordinate** plots so that they understand their use case and when they should be applied.

Walk through the syntax required to create a parallel coordinate plot:

* The **Parallel Coordinate** plot can be created using the `parallel_coordinates` function.

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

* Communicate that **Parallel Coordinate** plots allow for multiple variables to be represented in parallel to one another. This is particularly valuable when tracing the relationships between variables and how each variable relates to/affects the other.

* By sorting the axes and filtering values, analysts can cluster attributes to assess relationships and trends.

  * For example, sorting so that **vacantLots** and **sales20092010** are adjacent allows one to see how the number of vacant lots affects the number of sales for that block.

  * An assessment of **vacantLots**, **unitsPerSquareMile**, and **foreclosures** reveals that if there are more vacant lots on a block, there will be fewer units per square mile and fewer sales.

Reinforce to students that **Parallel Coordinate** plots are used to visualize multivariate analysis by providing example use cases.

* Another use case for **Parallel Coordinates** plot would be analyzing the quality of a diamond. Variables of interest would be cut, carat, clarity, and price. **Parallel Coordinates** would show how any of these attributes can affect the other.

Break down the anatomy of the plot, emphasizing the components below.

* Point out the verticals on the plot. Each vertical represents a different variable. Because each variable can have a different range of numeric values, the scale of each vertical is specific to that variable. This would mean each vertical could have a different scale.

* Point out the colored lines on the plot. A line is used to represent a row from the DataFrame. A line will connect each attribute for that given row, which enables analysts to spot trends and track the related attributes/values.

  * Each line is color coded to help assist in tracing the relationships. This is especially valuable when going from looking at data from a row point of view to looking at a visualization.

Ask if there are any questions before moving on.

- - -

### 6. Student Do: Plotting in Parallel (15 mins)

Students complete a bridge activity where they revisit a previously used data set that was visualized using scatter plots. Students now visualize the data using a **parallel coordinates** plot.

This will be the students' first time working with **parallel coordinate** plots. Instruct TAs to circulate to provide assistance. Encourage students who finish early to assist their classmates.

**Instructions:**

* [README.md](Activities/04-Stu_Parallel_Coordinates/README.md)

**Files:**

* [plotting_in_parallel.ipynb](Activities/04-Stu_Parallel_Coordinates/Unsolved/Core/plotting_in_parallel.ipynb)

- - -

### 7. Instructor Do: Parallel Coordinates Activity Review (5 mins)

**Files:**

* [plotting_in_parallel.ipynb](Activities/04-Stu_Parallel_Coordinates/Solved/Core/plotting_in_parallel.ipynb)

Kick off the review session by asking some of the below guided questions.

* What's the function used to create a **parallel coordinate** plot?

  * **Answer** `plotly.express.parallel_coordinates()`

* What's the difference between a **scatter plot** and **parallel coordinate** plot?

  * **Answer** **Scatter plots** visualize the relationship between two data points as an intersection. **Parallel coordinate** plots visualize the relationship between two data points as parallel axes.

  * **Answer** **Scatter plots** inherently use two axes. Whereas **parallel coordinate** are built for multivariate analysis and can have 2+ axes.

* In terms of interaction, which plot do you feel allows you to gain more value from interaction?

  * **Answer** The **parallel coordinate** plot offers limited opportunities for interaction, which makes the **scatter plot** more fitted for interacting with plots. However, **parallel coordinate** plots structurally allow for relationships to be traced more effectively and efficiently.

* What is the difference between the types of interactions provided by these different plots?

  * **Answer** **Parallel coordinate** plots can only be sorted and filtered/highlighted. **Scatter plots** can be zoomed, panned, filtered, etc.

If time remains, open the solution, and highlight the following:

* Parallel Coordinate plots present plot axes in a parallel fashion. This allows data points to be traced from one axes/variable to the next.

  * Increases and decreases can be visually spotted by the lines that connect data points to one another. This structure allows variables to be analyzed in relation to another.

  ![parallel_relationships.gif](Images/parallel_relationships.gif)

Ask for any remaining questions before moving on.

- - -

### 8. Instructor Do: Parallel Categories (10 mins) (Critical)

In this activity, students continue learning about more advanced, statistical plots, like the **Parallel Categories** plot by way of an instructor demo. The instructor will demonstrate to students how to create a **parallel categories** plot, as well as highlight the differences between **parallel categories** and **parallel coordinates**.

**Files:**

* [parallel_categories.ipynb](Activities/05-Ins_Parallel_Categories/Solved/parallel_categories.ipynb)

Navigate to the 6.2 slides, and highlight the following:

* Whereas **parallel coordinate** plots are used for multivariate analysis and mapping relationships between variables, **parallel categories** plots are used to perform **multidimensional** analysis.

  * An example of multidimensional analysis would be looking at sales and foreclosures data by housing type, region, and number of units. Housing type, region, and number of units would be good dimensions to consider.

* **Dimensions** are considered to be **categories**. **Parallel categories** plots focus on connecting the dots between each category and assessing the nuances per category, as well as the impact of categories on other categories.

Open the [starter file](Activities/05-Ins_Parallel_Categories/Solved/parallel_categories.ipynb), and live code the following:

* Parallel categories plots can be created using the `parallel_categories` function.

  ```python
  # Prep Data
  housing_type= ['Single Family','Multi-Family','Apartment']
  region= ['North East','Tri-State']
  prop_size= ['Large','Medium','Small']

  df= pd.DataFrame({
      "sold":np.random.randint(999,1002,30),
      "year":np.random.randint(2010,2019,30),
      "type": np.random.choice(housing_type, 30),
      "region": np.random.choice(region, 30),
      "prop_size": np.random.choice(prop_size, 30)}).sort_values(['year','type','region','prop_size'])
  df.head()
  ```

  ![parallel_categories.png](Images/parallel_categories.png)

* To make sure plots are structured the correct way, use the `dimensions` parameter to hard code what the **dimensions** should be.

  ```python
  px.parallel_categories(df, dimensions=['type','region','prop_size'], color='year',
                        color_continuous_scale=px.colors.sequential.Inferno)
  ```

* The labels parameter can be used to customize the labels shown on the plot. It will also add a highlight feature to the label names so they can be read.

  ```python
  px.parallel_categories(df, dimensions=['type','region','prop_size'], color='year',
                        color_continuous_scale=px.colors.sequential.Inferno,
                        labels={'type':'Type of Dwelling', 'region':'Region', 'prop_size':'Property Size'})
  ```

* Similar to parallel coordinates plot, the **parallel categories** plot axes can be sorted by clicking and dragging to the desired location.

  ![sort_categories.gif](Images/sort_categories.gif)

- - -

### 9. Break (15 mins)

- - -

### 10. Student Do: Categorical Property Evaluation (15 mins)

Students complete a MSMD activity and code out a **parallel categories** plot. Students will use the plot to visualize the dimensions/categories evaluated during real estate property assessments.

Encourage students to work in teams and collaborate on the information seeking process. Indicate that even when working in teams each student will still need to complete the activity.

* Instruct the TAs to circulate to provide the teams with any troubleshooting assistance.

Additionally, keep an eye out during the activity for students who finish early. Find a student volunteer who is wiling to present and describe the story being told by the documentation. Explain to the volunteer that they will have to present their plot to the class and tell the story of the data by interacting with the plot.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/allegheny-county-property-assessments).

**Instructions:**

* [README.md](Activities/06-Stu_Categorical_Evaluation/README.md)

**Files:**

* [Categorical_Evaluation.ipynb](Activities/06-Stu_Categorical_Evaluation/Unsolved/categorical_evaluation.ipynb)

- - -

### 11. Students Do: Categorical Assessments Activity Review (10 mins)

This activity involves a student volunteering to tell the story of Alleghany property assessments. A student will present the parallel categories plot from the student activity, and provide some findings regarding dimensional patterns.

This activity is a revised version of the turn and teach activity type; however, instead of students working as teams, one student will lead the teaching.

**Files:**

* [categorical_property_evaluation.ipynb](Activities/06-Stu_Categorical_Evaluation/Solved/categorical_evaluation.ipynb)

Open the solution and ask the student volunteer to present the plot and relay their findings. Use the below discussion points to help facilitate the review.

* The **parallel categories** plot is created using the `parallel_categories` function provided with **Plotly.express** package.

    ```python
    # Plot data
    px.parallel_categories(data, dimensions=['USEDESC','TOTALROOMS','BEDROOMS','FULLBATHS'], color='LOCALTOTAL')
    ```

    ![stu_parallel_categories.png](Images/stu_parallel_categories.png)

* Since **paralell categories** plots involve multidimensional analysis, dimensions can be specified using the `dimensions` attribute.

  ![stu_parallel_categories_dimensions.png](Images/stu_parallel_categories_dimensions.png)

* The line coloring of the plot can be changed using the `color` attribute. This will help spot trends in the data.

  ![stu_parallel_categories_color.png](Images/stu_parallel_categories_color.png)

If time remains, initiate the story telling piece of the review by asking the student some of the following guided questions:

* Are there any identifiable patterns at the dimension level?

  * **Answer** Most sales were single family homes

  * **Answer** Most homes have 3 bedrooms.

* How many bedrooms and full bathrooms do single family homes tend to commonly have?

  * **Answer** Three bedrooms one bath.

* What type of patterns can be seen when correlating **total number of rooms** and **bedrooms**?

  * **Answer** The homes that have evaluated at the highest local price are the ones that have twice as many total rooms as bedrooms.

  * **Answer** Housing value is more affected by **total number of rooms** and **bedrooms** than **full baths**.

* Is there an identifiable story being told through the data? What is the story?

  * **Answer** Total number of rooms, bedrooms, and bathrooms are all used to assess a property and its value. The more rooms and bedrooms, the higher the sale price. Lastly, most single family homes being assessed in Allgehany county 2019 have around 6 total rooms, 3 bedrooms, and 1 full bath.

  * **Answer** The houses evaluated at the highest costs tend to have more than 5 total rooms,

- - -

### 12. Instructor Do: Mapbox API Demo (10 mins) (Critical)

In this activity, students will sit through a demonstration of how to use the Mapbox API with Plotly Express.

In order to complete this activity, a Mapbox API will be required. A personal key can be obtained by signing up [here](https://account.mapbox.com/auth/signup/).

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/500-cities-local-data-for-better-health-fc759).

**Files:**

* [plotly_maps.ipynb](Activities/07-Ins_Mapbox_Demo/Unsolved/plotly_maps.ipynb)

Navigate to the 6.2 slides, and highlight the following:

* MapBox API is an open source API that gives developers a range of mapping visualizations and functions that enable the creation of interactive map plots.

* MapBox API is democratizing the map services industry (e.g. navigation and cartography), similar to how Plaid is doing for FinTech.

* MapBox offers three main services: maps, navigation, and search.

  * These services come with handy tools, such as map styles and vectors, map images and data sets, and live location.

Open the starter file, and live code the following. Make sure to have your Mapbox API key handy. Highlight the discussion points while coding:

* Plotly Express has an integration endpoint specific for Mapbox API. This allows Plotly to use the Mapbox maps API in order to create interactive map visualizations. Plotly Express comes with functions designed specifically for interacting with MapBox.

  * Plotly's integration with Mapbbox makes it extremely convenient to use; no other imports are required. All that is needed is the Plotly Express library.

* The Mapbox API uses API keys to monitor API requests. The Mapbox API key needs to be set up as an environment variable. The `os.getenv` function can then be used to retrieve the key within Python code.

  ```python
  # Extract token
  mapbox_token = os.getenv("MAPBOX_API_KEY")
  ```

* Once the environment variable is ready and available in Python, it can be registered with Plotly. Plotly provides a function to do this: `set_mapbox_access_token`.

  * Because Plotly Express will broker the client-server relationship, the Mapbox API key has to be set/registered with Plotly Express.

  ```python
  px.set_mapbox_access_token(mapbox_token)
  ```

* After the token is set with the `set_mapbox_access_token`, the Plotly Express mapbox plot functions can be used to create geographic plots.

Demonstrate how to create a map scatter plot using the Plotly Express `scatter_mapbox` function.

* The `scatter_mapbox` function can be used to create a scatter plot that is overlayed on top of a map (provided by Mapbox). This allows for scatter plot data to be analyzed in reference to geographical location.

  ```python
  # Read in data
  df = pd.read_csv(Path('../Resources/population_counts_reduced.csv')).drop_duplicates()
  data_to_plot = df[['Year','PopulationCount','Latitude','Longitude']]
  filtered_data = df[df['StateDesc'] == 'California']

  px.scatter_mapbox(filtered_data, lat='Latitude', lon='Longitude',
                  size='PopulationCount', color='CityName')
  ```

  ![scatter_map_plot.gif](Images/scatter_map_plot.gif)

* It's important to note that map plots can be a little memory intensive than the plots we are used to.

  * Data sets should be filtered and aggregated to the highest level of granularity possible (without jeopardizing reporting context) so that plots do not take long to load.

  * Sampling techniques (i.e. visualizing only top n items) to help reduce the amount of data being reflected on the visualization. These approaches will preserve reporting integrity.

Note to students that when data sets become too large to manage or reduce, technologies like [Datashader](http://datashader.org) can also be considered. Datashader specializes in turning large volumes of data into visualizations.

* Encourage students to look into technologies like Datashader outside of class.

Ask for any questions before moving onto the student activity.

- - -

### 13. Students Do: Mapping Adventures (15 mins)

Students repeat the steps demonstrated by the instructor in order to create their own PlotLy/MapBox scatter plots. Students will integrate Plotly and MapBox to create their first geographical visualizations.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/areas-of-interest-gis).

**Instructions:**

* [README.md](Activities/08-Stu_Mapping_Adventures/README.md)

**Files:**

* [mapping_adventures.ipynb](Activities/08-Stu_Mapping_Adventures/Unsolved/Core/mapping_adventures.ipynb)

- - -

### 14. Instructor Do: It's a Map Plot Activity Review (10 mins)

This review activity will consist of two parts. The first part will be a dry walk through of the Mapping Adventures student assignment. The second will consist of a facilitated discussion/student presentation of the top places they'd go to for Harold's birthday.

**Files:**

* [mapping_adventures.ipynb](Activities/08-Stu_Mapping_Adventures/Solved/Core/mapping_adventures.ipynb)

Open the solution and conduct a dry walk through:

* The marriage between Plotly Express and Mapbox has enabled developers to create interactive map visualizations.

* Using Mapbox's API, Plotly can render geographic plots, such as the **scatter mapbox** plot. The **scatter mapbox** plot is the classic scatter plot overlayed on top of a map.

  ![plotting_adventures.gif](Images/plotting_adventures.gif)

* The **scatter mapbox** plot can be created using the `scatter_mapbox` function. The function has three key parameters: DataFrame, **latitude** field, and **longitude** field. **Color** is also an acceptable argument, which accepts a DataFrame column as its value.

  ![scatter_mapbox.png](Images/scatter_mapbox.png)

Next, transition into the presentation portion of the review.

* Ask if there are any students who would like to present the three places they'd choose to go to. If no one volunteers, go around the room round robin.

  * **Answer** Prospect park, botanic garden, and botanic garden.

Ask for any remaining questions before moving on.

- - -

### 15. Students Do: A Cartographer's Expedition (20 mins)

Students create map plots to visualize/embark on a virtual expedition through NYC to various places of interest.

Indicate to students that they should work in teams of 2-3 to plan the trip together.

**Instructions:**

* [README.md](Activities/09-Stu_Cartographers_Expedition/README.md)

**Files:**

* [cartographers_expedition.ipynb](Activities/09-Stu_Cartographers_Expedition/Unsolved/cartographers_expedition.ipynb)

- - -

### 16. Instructor Do: A Cartographers Expedition Activity Review (5 mins)

In this activity, student groups will present their maps and expeditions to the rest of the class.

**Files:**

* [cartographers_expedition.ipynb](Activities/09-Stu_Cartographers_Expedition/Solved/cartographers_expedition.ipynb)

Start the activity review by asking if there is a group who wants to volunteer to present their expedition first. Then, ask the following questions. If time remains, ask for a second group to also present.

* Ask the group to present their maps and to relay their full expedition.

  * **Answer** Airport -> Aqueduct Race Track -> Astoria Park -> Fort Totten -> Juniper Valley Park -> Madison Square

* Sometimes it's difficult to get a good understanding of whether or not two locations are close to one another. Were there any instances where you had to re-choose locations due to them being too far away?

  * **Answer** Yes. When picking locations at random, it was hard to determine which points would be close to one another.

* What are some programmatic approaches to making sure locations are close to one another?

  * **Answer** The data could be sorted by latitude and longitude.

  * **Answer** Data could have been sliced by borough first, and then places chosen from there.

* What guided your final decision on locations?

  * **Answer** Locations were chosen based off of categorical type and proximity. Locations of type garden, park, and square were chosen for a specific experience.

* Were the geographic scatter plots helpful in understanding the distribution of places of interest throughout NYC? How did the visual help cement the image?

  * **Answer** Yes, the plots were helpful. By color coding by **PlaceType**, it was easy to see the clusters of each type of place. This helped outline the trek through the boroughs. It was also helpful in noticing trends in positioning of certain locations (i.e. Ellis and Liberty Island are in same place and the forts all seem to be north of Manhattan.

Ask for any remaining questions before moving on.

- - -

### 17. Instructor Do: Recap (5 mins)

In this activity, students recap the knowledge and skills learned during the day. Students can ask questions, or he instructor can ask guided questions to facilitate the recap.

**Files:**

* [Slides]()

Congratulate students on taking their plotting skills to the next level. Communicate the following:

* **Plotly Express** is a technology commonly used by data scientists and programmers for data visualization needs.

* Plotly is incredibly versatile and supports multiple programming languages (i.e. R, JavaScript, Python). This makes it highly desired skill by employers.

Ask students if they have any questions about the material covered in today's lesson.

* Use this time to answer as many questions as possible.

* Once time is up, encourage students to attend office hours or reach out to the TAs if they have any additional questions.

If students do not have any questions, ask them the following guided questions:

* Ask students to summarize some of the differences between hvPlot and **Plotly Express**.

  * **Answer** hvPlot offers an easy way to overlay/compose plots. **Plotly Express** offers parallel categories and coordinate plots. **Plotly Express** also has integration with Mapbox API.

Communicate to students that the visualizations they've created so far, and their notebooks in general, could be viewed as reports that provide or answer a specific  request for information or data need. Another type of visualization is a dashboard.

* If reports are different than dashboards, what is a dashboard?

  * **Answer** A dashboard is an interactive visualization tool that can be dynamically manipulated to show data.

* What makes a dashboard starkly different than a report?

  * **Answer** Dashboards often contain live data rather than static data (like with a report). This allows data to be real time. Dashboards are also sometimes made up of multiple reports.

  * **Answer** Reports provide a view into raw data. Reports help visualize underlying data and spot trends. Dashboards present data within a specific context/reporting agenda, and the data is often curated to report on specific KPIs.

If time remains, ask students to summarize three things they've learned today.

* **Answer** **Parallel coordinates** and **categories** plots use vertical axes to visualize multivariate analysis and variable relationships.

* **Answer** **Map** plots can be used to visualize clusters of data points geographically.

* **Answer** **Parallel coordinates** and **categories** plots allow users to visualize correlations but also reorganize variables in order to get a better sense of multivariate relationships.

Ask if there are any questions before moving forward.

## End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
