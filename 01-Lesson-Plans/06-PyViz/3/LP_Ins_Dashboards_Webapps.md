### 14. Instructor Do: Dashboards as Web Applications (10 mins) (Critical)

Students learn how to transform their Jupyter notebook dashboards into a **web app**. The instructor will demonstrate how to use the `servable` command to execute and run the dashboard on a server. The instructor will use the same dashboard created from the previous activity.

**Files:**

* [dashboard_webapps.ipynb](Activities/14*Ins_Dashboard_Webapps/Unsolved/dashboard_webapps.ipynb)

Navigate to the 6.3 slides, and communicate the following:

* One of the advantages of using Panel for dashboarding is that Panel dashboards can be deployed as web apps: dashboard applications that are accessible over the internet rather than just in a Jupyter notebook. This means that any Jupyter notebook containing a Panel object can be deployed as its own independent **web app**.

* Panel is equipped with a `servable` function that spins up a **Bokeh** server and launches the Jupyter notebook code as a **web app**. Even though the **web app** will use the code from the Jupyter notebook, the **web app** will only display the Panel object being rendered.

Open the starter file, and live code how to run a Panel dashboard as a **web app**.

* In order to deploy the notebook and dashboard as **web app**, a Panel object has to be ran as a servable object. This can be achieved using the `servable` function.

  ```python
  # Execute Panel dashboard using servable function
  crime_pop_dashboard.servable()
  ```

  ![servable.png](Images/servable.png)

* It's important to note that while within a Jupyter Notebook, the `servable` function will only render the Panel object in a Jupyter cell. However, when ran from the command line or a shell script, the `servable` function within the notebook will signal to Panel that a **web app** needs to be spun up.

  * The `servable` function can be considered as a flag that tells Panel what Panel object to render as a **web app**.

* Once the Panel object has been tagged as servable, the `panel serve` command can be executed from a CLI to spin up a **Bokeh** server and deploy the specified Panel object as a **web app**.

  ```shell
  panel serve dashboard_webapps.ipynb
  ```

  ![panel_serve.png](Images/panel_serve.png)

* The web app can be accessed using the url returned from the `panel serve` CLI command. Enter the URL in a browser, and watch your dashboard load. Note that when the dashboard loads, it will load without all of the code and Jupyter cells. Only the dashboard content will be displayed.

If time remains, ask the following guided question:

* In what ways can Panel dashboards add value to the Financial industry?

  * **Answer** Panel dashboards give financial companies the opportunity to retire one*off/adhoc reports. Instead of distributing financial reports via email and making graphs and pivot tables in Excel, all reporting can be migrated to Panel dashboards, executed as **web apps**, and made accessible company wide.

  * **Answer** Panel's interactive dashboards offer financial companies the opportunity to analyze and gain insights from data using an interactive platform. Instead of analyzing financial reports that contain static/stale data, finance professionals can just access a dashboard to get access to the most latest data.

Ask if there are any questions before moving on.
