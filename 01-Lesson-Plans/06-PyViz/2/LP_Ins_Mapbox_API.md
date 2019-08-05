### 15. Instructor Do: Mapbox API Demo (10 mins) (Critical)

In this activity, students will sit through a demonstration of how to use the Mapbox API with Plotly Express.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/500-cities-local-data-for-better-health-fc759).

**Files:**

* [plotly_maps.ipynb](Activities/15-Ins_Mapbox_Demo/Solved/plotly_maps.ipynb)

Open the starter file, and live code the following. Make sure to highlight the discussion points while coding.

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
