### 12. Student Do: Extending Plotting (15 mins)

Students complete a Bag of Tricks activity where they create a dashboard that contains map visualizations and hvPlot composed plots. The goal of this activity is to reinforce to students that Panel can support all the visualizations that have been created in class so far.

Data for this activity was retrieved from [ucr.fbi.gov](https://ucr.fbi.gov/crime-in-the-u.s/2015/crime-in-the-u.s.-2015/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2015.xls/view).

**Instructions:**

* [README.md](Activities/12-Stu_Panel_Extensions/README.md)

**Files:**

* [extending_plotting.ipynb](Activities/12-Stu_Panel_Extensions/Unsolved/extending_plotting.ipynb)

### 13. Instructor Do: Extending Plotting Activity Review (10 mins)

Students will participate in a facilitated discussion guided by the instructor. The focus of the discussion will be how multiple technologies can be integrated and embedded on a singular dashboard to create a reporting platform.

**Files:**

* [extending_plotting.ipynb](Activities/12-Stu_Panel_Extensions/Solved/extending_plotting.ipynb)

Open the solution and explain the following:

* Panel supports a number of different visualization extensions. This includes Plotly, hvPlot/Holoviews, and Matplotlib. In order to use an extension, a call has to be made to the `panel.extension` function. The name of the extension (i.e. **plotly**) will need to be passed to the function.

  * If an extension is not specified, certain Panel **panes/panels** will not render.

  ```python
  pn.extension('plotly')
  ```

* Panel **panels** can be used to display visualization plots of different types made by different technologies. For example, a Plotly map plot could be added to the same column or row as an hvPlot scatter plot. The focus of Panel **panels** is to give developers the ability to group plots and other media types into a single container.

  ```python
  # Create panels to structure the layout of the dashboard
  geo_column = pn.Column("## Population and Crime Geo Plots", population_plot, crime_plot)
  scatter_column = pn.Column("## Correlation of Population and Crime Plots", population_violence, violent_murder)
  ```
  ![panel_column_integration.png](Images/panel_column_integration.png)

* The best way to create a dahsboard layout is to strategically group media types into containers.

  * Plots of the same type can be added to the same column/row, and plots of different types can be added to different tabs.

  * Furthermore, plots that serve one specific analytic objective could be rendered on one tab together, while other analytic use cases could be maintained in other tabs.

  ```python
  crime_pop_dashboard = pn.Tabs(
    ("Geospatial", geo_column),
    ("Correlations", scatter_column))

  crime_pop_dashboard
  ```

  ![panel_tabs.png](Images/panel_tabs.png)

  ![population_crime_dashboard.gif](Images/population_crime_dashboard.gif)

* Integrating Panel columns and tabs with PyViz visualizations creates a dashboard that allows users to analyze a number of visualizations at one time from a one-stop shop.

If time remains, ask students the following review questions:

* What's the underlying Pythonic structure for Panel **panels**?

  * **Answer** List data structure

* If I wanted to add an object to a row after the row object has been declared, can I?

  * **Answer** Yes, the row `append` function can be used to insert the new object

* Why do extensions have to be specified when working with **Panel**?

  * **Answer** Because **Panel** supports a wide range of visualization technologies. Each technology has its own approach to rendering plot look and feel/skins, widgets, etc. In order to preserve the integrity of the visualizations created by each technology, Panel uses extensions to render the visualization objects.

Ask for any remaining questions before moving on.
