# Unit 6 Assignment - Pythonic Monopoly

![San Francisco Park Reading](Images/san-francisco-park-reading.jpg)

*[San Francisco Park Reading by Juan Salamanca](https://www.pexels.com/photo/park-san-francisco-reading-61109/) | [Free License](https://www.pexels.com/photo-license/)*

## Background

Harold just became so popular on the firm so his manager asked him to lead the real state brand new division. He is asked to decide where in San Francisco it’s worth to invest on buying properties for rental by maximizing the company’s revenue in the short (5 years) and long (10 years) term. Harold is also asked to present their results and insights on a very creative and visually attractive manner for potential investors. Harold asked you to use your brand new python plotting skills to create meaningful data visualizations.

In this homework assignment, you will help Harold accomplish the following tasks:

1. [Generate stand-alone plots using `matplotlib`, `hvPlot` and `Plotly Express`.](#Stand-Alone-Plots)
2. [Create a dashboard web application using the `DataViz Panel` and `Bokeh Server` by combining plots from different libraries on the same visualization.](#Dashboard-Visualization-Web-Application)

---

## Files

* [sfo_neighborhoods_census_data.csv](../Data/sfo_neighborhoods_census_data.csv)
* [neighborhoods_coordinates.csv](../Data/neighborhoods_coordinates.csv)
* [Plots Generator Starter Notebook](Resources/plots_generator.ipynb)
* [Pythonic Monopoly Dashboard Starter Notebook](Resources/pythonic_monopoly_dashboard.ipynb)

## Instructions

### Stand-Alone Plots

In order to convince potential investors the first step is to understand the available data, so in this section you will use your skills on the different python plotting libraries you learned to answer the following questions:

* Start by using `matplotlib` to create the following plots:
  * Create a plot that shows the average housing units in San Francisco from 2010 to 2016. What kind of plot could be the best fit for this purpose?
  * Create two line plots to show how the average gross rent and the sale price per square foot has evolved from 2010 to 2016.
* Now use your `hvPlot` super powers to create the following plots:
  * In order to understand how the sale price per square foot has evolved from 2010 to 2016, Harold asked you to create a *dynamic line plot* that should allow the people to select any single neighborhood in San Francisco to analyze the data individually.
  * Alina, one of the most influential investors, is interested on buying properties on the most expensive neighborhoods of San Francisco since she believed those places will be the more profitable in the long term. Create a plot that show the average sale price per square foot for the top 10 most expensive neighborhoods.

Your plot for the top 10 expensive neighborhoods was a good starting point, but Alina wants additional information. Harold suggested to create two new plots, a`parallel coordinates` plot to represent the relationship between the average sale price per square foot, housing units and gross rent; as well as a `parallel categories` plot to analyze the same variables by neighborhood. Harold just has never created this kind of plots, but you accepted the challenge to create them.

* Use `Plotly Express` to create the `parallel coordinates` and `parallel categories` plots to support the decisions that investors should make.

### Dashboard Visualization Web Application

The final step on finishing this assignment to present the analysis results to investors is to assemble all your plots on a dashboard.

* Reusing the code from the previous section, create function to create each plot. If you decide to go on the [Challenge](#Challenge) also include the map on the dashboard.
* Create a tabbed dashboard with the following sections:
  * _Welcome tab_: On this tab include a welcome text depicting the what purpose of the dashboard, if you worked on the Challenge, also include the `scatter_mapbox()` plot below the text, if you didn't include an image instead.
  * _Yearly Market Analysis tab_: This tab will contain the three plots you created with `matplotlib`.
  * _Neighborhood Analysis tab_: You should include on this tab the two plots you created with `hvPlot`.
  * _Parallel Plots Analysis tab:_: Finally this tab will include the two parallel plots you created using `Plotly Express`.
* You can create a draft dashboard using Jupyter notebooks before creating the python script to launch the web application with the `Bokeh Server`.
* Feel free to design the dashboard's layout at your convenience by combining the Column, Row and Tabs layout objects.

### Challenge

Among investors there are some foreign people that are not familiar with San Francisco, so you decide to create a [scatter map plot](https://www.plotly.express/#Maps) using `Plotly Express`.

* On this plot show the location of all neighborhoods in San Francisco by coloring the points according to the average gross rent and sizing them according to the average sale price per square foot.
* For this activity you will find the latitude and longitude of the center point of each neighborhood on the CSV file entitled `neighborhood_coordinates.csv`. Part of this challenge is to combine this information with the average values of *sales price price for square foot* and *gross rent* for each neighborhood.
* If you have time, try to modify the data to create an animated map using the `Year` as `animated_frame` property on the scatter map plot.
* In order to create maps visualizations using Plotly Express, you will need to create an account at [mapbox](https://www.mapbox.com/) and create an [access token](https://docs.mapbox.com/help/how-mapbox-works/access-tokens/#creating-and-managing-access-tokens).
* Once you create your access token, open the `mapbox_token` text file, delete all the text an paste your token instead.

### Submission

* Complete the *Plots Generator Jupyter Notebook*.
* Complete the *Pythonic Monopoly Jupyter Notebook*.
* Create a python script to launch the dashboard visualization as a web application using the `Bokeh Server`.
* You should not submit your `mapbox` access token.
