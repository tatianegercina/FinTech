### 2. Instructor Do: Intro to Panel (5 mins) (Critical)

**Files:**

* [Slides]()

Continue the discussion about Panel by highlighting the rise of Panel.

* Digital dashboards have become a staple in the tech world. Dashboards are being used to visualize personal finance, company performance and revenue, and even election results/predictions.

* Dashboards typically were created using visualization technology specific stacks, like those associated with Cognos, Tableau, and Qlik.

* Panel, a PyViz dashboarding package, has altered the data visualization arena by providing a programmatic way to easily create dashboards.

* Panel's integration with PyViz has made it a highly valuable skill in analytics, as well as a staple in the Python data visualization ecosystem.

* Panel allows data scientists and analysts to create and manage dashboards in the same environment they are completing development, using one technology stack. One developer can use the same technology to create both a data pipeline and dashboard visualizations for the data.

  * PyViz removes the need to use another technology stack for dashboards/visualizations (i.e Tableau).

Walk through some of these [example](https://gapminder.pyviz.demo.anaconda.com/app) dashboards. Use the below discussion points to guide the walk through.

* PyViz comes with widgets and plugins that allow it to render plots and visualizations from other technologies, like Pandas, Matplotlib, and Plotly. This enables developers to build visualizations in the appropriate technologies and then display them all in one, centralized location with a Panel dashboard.

  ![panel_wrapper.png](Images/panel_wrapper.png)

* Interact with the plots on the website. Use the widget bar to pan, zoom, etc. Emphasize to students that all plotting interactions and widgets can still be used even when plots are rendered with Panel as a dashboard.

  ![panel_interact.gif](Images/panel_interact.gif)

* Explain that this is what makes Panel such a heavy hitter. Pre-existing plots can be embedded within Panel dashboard, and all functionality will be preserved.

If time remains, show students the [NYC taxi trips](https://nyc-taxi.pyviz.demo.anaconda.com/dashboard) dashboard, a geospatial map reporting on taxi routes, pick up and drop off locations, and trips by the hour.

* Interact with the visualization using the widget bar (i.e. pan, zoom, hover, etc). Ask students the following question:

  * Jupyter Lab and Panel can both render interactive plots. In what ways do these technologies differ?

    * **Answer** Jupyter Lab renders locally, whereas Panel can render plots over the internet.

  * Ask students what the value is behind having a dashboard that opens over the internet rather than just locally.

    * **Answer** More users can access and leverage the dashboard.
