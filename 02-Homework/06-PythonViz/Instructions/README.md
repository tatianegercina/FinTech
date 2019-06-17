# Unit 6 Assignment - Pythonic Monopoly
![San Francisco Park Reading](Images/san-francisco-park-reading.jpg)

*[San Francisco Park Reading by Juan Salamanca](https://www.pexels.com/photo/park-san-francisco-reading-61109/) | [Free License](https://www.pexels.com/photo-license/)*

## Background

Harold just became so popular on the firm so his manager asked him to lead the real state brand new division. He is asked to decide where in San Francisco it’s worth to invest on buying properties for rental by maximizing the company’s revenue in the short (5 years) and long (10 years) term. Harold is also asked to present their results and insights on a very creative and visually attractive manner for potential investors. Harold decide to use his brand new python plotting skills to create meaningful data visualizations.

In this homework assignment, you will help Harold accomplish the following tasks:

1. [Generate stand-alone plots using `matplotlib`, `PyViz` and `Plotly Express`.](#Stand-Alone-Plots)
2. Create a dashboard using the DataViz Panel and combining plots from different libraries on the same visualization.

---

## Files

* [sfo_neighborhoods_census_data.csv](../Data/sfo_neighborhoods_census_data.csv)
* [neighborhoods_coordinates.csv](../Data/neighborhoods_coordinates.csv)
* [Plots Generator Starter Notebook](Resources/plots_generator.ipynb)
* [Pythonic Monopoly Dashboard Starter Notebook](Resources/pythonic_monopoly_dashboard.ipynb)

## APIs

* You will need to create a free account at [mapbox](https://www.mapbox.com/) for creating maps visualization with Plotly Express.

## Instructions

### Stand-Alone Plots

In order to convince potential investors the first step is to understand the available data, so on this section you will use your skills on the different python plotting libraries you learned to answer the following questions:

* Use `matplotlib` to create a plot that show the average housing units in San Francisco from 2010 to 2016. What kind of plot could be the best fit for this purpose?
* Now use your `PyViz` super powers to create the following plots:
  * Create a two series line plot to show how the average gross rent and the sale price per square foot has evolved from 2010 to 2016.
  * In order to understand how the sale price per square foot has evolved from 2010 to 2016, Harold asked you to create a *dynamic plot* that should allow the people to select any single neighborhood in San Francisco to analyze the data individually.
  * Alina, one of the most influential investors, is interested on buying properties on the most expensive neighborhoods of San Francisco since she believed those places will be the more profitable in the long term. Create a plot that show the average sale price per square foot for the top 10 most expensive neighborhoods.
* Finally use `Plotly Express` to create the following data visualizations to support the decisions that investors should make.
  * Your plot for the top 10 expensive neighborhoods was good to start, but Alina wants additional information. Harold suggested to create two new plots, a`parallel coordinates` plot to represent the relationship between the average sale price per square foot, housing units and gross rent; as well as a `parallel categories` plot to analyze the same variables by neighborhood. Harold just has never created this kind of plots, but you accepted the challenge to create them.
  * Among investors there are some foreign people that are not familiar with San Francisco, so you decide to create a scatter map plot. Using your `mapbox` API create a `scatter mapbox` plot to show the location of all neighborhoods in San Francisco by coloring the points according to the average gross rent and sizing them according to the average sale price per square foot.
