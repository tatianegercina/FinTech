### 1. Instructor Do - Welcome (5 mins)

**Files:**

* slides

Welcome to Unit 6! Unit 6 is dedicated to introducing and teaching students all they need to know about data visualization using the PyViz visualization platform.

Navigate to the 6.1 slides, and highlight the following:

* Visualizations have already been used in class (Matplotlib plots). However, these visualizations have been static. While static visualizations are help in displaying data, the data cannot be interacted or explored in the same way. For this reason, students will learn how to create interactive plots.

* In order to create interactive plots, users need to be able to access visualization libraries and packages that offer interactive visualizations. Otherwise, the visualizations would have to be coded manually, which can be extremely cumbersome.

* PyViz is a data visualization ecosystem made specifically for Python. PyViz itself works as a wrapper around these various technologies
  * Example visualization technologies included with PyViz are hvPlot, Plotly Express, and Panel.

* PyViz aims to provide a single stop-and-shop space for all data visualization needs.

* The creators of PyViz recognize that one technology or package cannot solve all data visualization needs, and so, the creators have created PyViz as a means to provide developers with a platform that enables more than one data visualization package being used for a project.

Transition into a demonstration of the types of visualizations that can be made using PyViz:
Interactive visualizations allow data to be explored and analyzed in the most efficient and effective manner for human eyes.

* Interactive visualizations give users the ability to pan, zoom, and filter data elements and values

* Interactive visualization also include functionality that allows data to be sorted off of different values based off of a simple click

End the module communicating to students that gone are the days where simple line, bar, and histogram charts satisfied data visualization and data analysis needs. Students will now learn how to create interactive and innovative visualizations that satisfy data exploration AND data analysis needs.

Ask for any questions before proceeding.

- - -

### 2. Instructor Do - Review Homework (5 mins)

This activity involves a quick demo and review of the homework.

**Files**

* Homework Instructions

* Homework Solution

Navigate to the Unit 6 Homework Instructions, and communicate the following to the students:

* This week’s homework focuses on visualizing and analyzing real estate data to identify the best properties in the San Francisco region.

* The homework includes using hvPlot and Plotly Express to create interactive data visualizations. These data visualizations will then be integrated with Panel in order to create a digital dashboard that contains multiple tabs.

* Creating interactive data visualizations allows the consumer of the data to explore the data and find structure, patterns, and insights that are important to them.

* In an investment scenario, offering a way to explore the real estate market interactively gives the investor the power to find properties that are of particular interest to them. In scenarios like these, it is the visualizations that help users make decisions.

Demo the homework solution by giving the students a preview of the solution.

Ask the students for any questions before moving forward.

- - -

### 3. Instructor Do: Intro to PyViz (10 minutes)

Students will be introduced to PyViz by way of a facilitated discussion led by the instructor. The discussion will focus on the advantages of using PyViz rather than individual technologies (i.e. Holoviews, Matplotlib, d3.js, etc.).

**Files:**

* Slides

Communicate to students that the Python environment comes packed with a number of different visualization technologies that have all been wrapped together into one platform called PyViz.

Navigate to the 6.1 slides, and highlight the following:

* PyViz is a data visualization ecosystem that gives developers an easy way to access multiple data visualization libraries at one time.

* Each visualization technology in the PyViz ecosystem has the power and features to provide stand-alone visualizations. Each technology also has its strengths and weaknesses, which will be explored later.

* PyViz’s platform allows for different visualization technologies to be integrated with one another to create dashboards (which can be done with PyViz’s Panel software).

Facilitate discussion by asking the following questions:

* Let’s say I just wanted to use Matplotlib and Holoviews. Why not just download those technologies specifically rather than installing PyViz?

  * **Answer** Matplotlib and Holoviews may not satisfy all of the visualization needs required. For example, Matplotlib and Holoviews provide visualizations, but they do not offer a way to create a dashboard. Installing PyViz will ensure all viable technologies are accessible.

  * **Answer** Installing PyViz instead of just the individual technologies would mean that you’d get access to the individual technologies, as well as the integration architecture that PyViz uses to integrate the libraries.
* What other environment have we worked in that resembles the PyViz environment?

  * **Answer** The Anaconda environment

Ask if there are any questions; then, move onto the next module.

- - -

### 4. Instructor Do - PyViz Demo (10 minutes)

By the end of this activity, students will have a solid understanding of how to install PyViz and import it into a development environment.

**Files**

* [Slides]()

* [PyViz Installation Guide]()

Navigate to the 6.1 slides, and highlight the following:

* As an ecosystem, PyViz had a number of packages that can be used to create data visualizations.

* Each of the technologies in the ecosystem are accessed with the PyViz package. They don't have to be installed individually.

* In order to get access to these packages, the PyViz package has to be downloaded and installed correctly.

  ![pyviz_ecosystem.png](Images/pyviz_ecosystem.png)

Transition to the dry walkthrough of the installation guide, and highlight the following:

* To install PyViz, PyViz dependencies will need to be downloaded. This includes nodejs5 and dpm.

  ```shell
  pip install nodejs
  pip install npm
  ```

* The actual PyViz packages will need to be installed after all dependencies have been acquired. The key packages are Plotly Express and Panel.

  ```shell
  conda install -c hvplot
  conda install -c plotly_express
  conda install -c pyviz panel
  ```

* After the package have been installed, the Jupyter extensions need to be set up as well. Installing these extensions will ensure the interactive visualizations are accessible and viewable in JupyterLab.

  ```shell
  jupyter labextension install @jupyterlab/plotly-extension
  jupyter labextension install @pyviz/jupyterlab_pyviz
  ```

Before finishing the activity, reassure students and let them know that time has been set aside during the next activity to debug/troubleshoot any environment issues.

Ask students if they have any questions before moving forward.

- - -

### 5. Students Do: System Check (10 minutes)

In this activity, students will work in pairs to confirm everyone has PyViz installed.

Instructor and TAs should circulate to provide assistance to anyone who experienced environment issues when installing PyViz. At this time, the instructor should find a group and ask if they'd like to volunteer to quickly summarize the install process, time permitting.

**Files**

* [PyViz Install Guide]()

* [README.md](Activities/05-Stu_System_Check/README.md)

If time remains after students have completed the check, ask for the chosen group to summarize the install process. Use the below question as a starting point:

* What are the required steps for setting up Panel? For example, the first step is to ensure all dependencies have been installed and the conda environment updated. What's next?

  * **Answer** The second step is to install the PyViz packages. These can be done using the `conda install` or  `pip install` commands. The packages that need to be downloaded are:

    * Plotly Express

    * Jupyter Lab extension for Plotly Express

    * PyViz with Panel

    * Jupyter Lab extension for PyViz

Ask if there are any questions before moving on.

- - -

### 6. Instructor Do: Intro to hvPlot (5 minutes)

Students participate in a formal lecture regarding what hvPlot is and what it has to offer in terms of data visualization.

**Files**

* [Slides]()

Navigate to the 6.1 slides, and introduce students to the world of hvPlots interactive graphs!

* Explain to students that hvPlot is a technology that brings plots to life.

* hvPlot abstracts over Python visualization libraries like Matplotlib, Pandas, and Streamz. The abstraction allows hvPlot to utilize the stand-alone plotting mechanisms of these technologies.

* This abstraction also allows hvPlot to transform the static plots (i.e. Matplotlib plots) into interactive sandboxes for data exploration and analysis. hvPlots allow for:

  * Panning

  * Zooming

  * Hovering

  * Clicking

  * Filtering

Encourage students to review some of the [example plots](https://hvplot.pyviz.org/) on their own time. Make sure ot slack out this link.

  ```
https://hvplot.pyviz.org/
  ```

If time remains, review some of the common hvPlot charts and their interactive features. Highlight the following:

  ![hv_plot_1.PNG](Images/hv_plot_1.PNG)

  ![hv_plot_2_streamz.PNG](Images/hv_plot_2_streamz.PNG)

  ![hv_plot_3_geo_views.PNG](Images/hv_plot_3_geo_views.PNG)

  ![hv_plot_4_networkx.PNG](Images/hv_plot_4_networkx.PNG)

Ask if there are any questions. Then, continue to the next activity.

- - -

### 7. Instructor Do: hvPlot Demo (5 minutes)

**Files:**

* [hvPlot.ipynb](Activities/07-Ins_hvPlot_Demo/Unsolved/hvPlot.ipynb)

Open the [starter file](Activities/07-Ins_hvPlot_Demo/Unsolved/hvPlot.ipynb), and live code the following:

  * The **hvPlot** library has to be imported into the Python environment. hvPlot offers a library called **hvPlot.Pandas** that integrates hvPlot with Pandas DataFrame API. This allows Pandas DataFrames to be visualized using hvPlot.

    ```python
    import hvplot.pandas
    ```

  * The great thing about **hvPlot** being abstracted over Pandas is that the two technologies share plotting interfaces. This marriage is the definition of not reinventing the wheel.

    * Emphasize to students that even though hvPlot uses the function `hvplot` and Pandas `plot`, the `hvplot` function actually references the Pandas `plot` interface. This allows for hvPlots to be created and manipulated in the same ways as Pandas plots (including plot attributes), just with an interactive component.

  * The `hvPlot` function is used to create a standard hvPlot chart. For example, when applied against a DataFrame containing cumulative returns for five different tickers, hvPlot would create a visualization using the metadata and data from the DataFrame. No configuration is needed by the user.

    ```python
    # Data Prep
    df_idx = pd.date_range('1/1/2018', periods=1000)
    df = pd.DataFrame(np.random.randn(1000,4),index=df_idx, columns=('APPL','GOGLE','AMMD','BCOIN')).pct_change()

    # Use hvplot() function to plot data
    df.hvplot()
    ```

    ![hvplot_line.png](Images/hvplot_line.png)

* Similar to the `Pandas.plot` API, the `hvPlot` function comes with a `line` attribute. The `line` attribute explicitly specifies to hvPlot that the visualization should be a line chart.

    ```python
    # Use hplot.line to create line plot
    df.hvplot.line(
        xlabel="Year",
        ylabel="Daily Return"
    )
    ```

* The `hvPlot` function also has a `bar` attribute for visualization of categorical data. It works the same as the `line` attribute, but it creates a **bar** visualization rather than **line**. It is important to note to students that bar plots require categorical data and not just time series data. Bar plots need to compare the **x** axis against **y**.

    ```python
    # Data Prep
    df = pd.DataFrame({'ticker':['APPL','GOGLE', 'AMMD','BCOIN'], 'daily_return':(4.50,10,33.0,55.25)})

    # Use hvplot.bar() to create bar plot with categorical data
    df.hvplot.bar(x='ticker', y='daily_return', xlabel='Ticker', ylabel='Daily Return', rot=90)
    ```

    ![hvplot_bar.png](Images/hvplot_bar.png)

If time remains, choose either the line or bar visualization, and demonstrate to students how to use hvPlot's interactive features. Highlight the following:

* Hover over a data point to highlight hover interaction. Explain that hovering allows users to hone in on the plot value being observed.

* Click and drag the visualization to pane to the left and right. Communicate that visualizations panned, allowing for data to be analyzed across time more effectively and efficiently.

* Select an element on the legend to filter it out. Show that this allows data to be hidden as needed. With just a click, data can be curated to specific analytic needs on the fly, on a case by case basis.

  * Emphasis to students that this is incredibly difficult to do with standard plotting packages like Pandas and Matplotlib. Having this type of functionality included out of the box with hvPlot is not only powerful but ground breaking! It would take longer to code the filter than it would a user clicking the legend.

  * Static visualizations require the underlying data to be changed in order for a visualization to be updated; with interactive visualizations, data can be filtered on demand.

* Indicate to students that these are just two ways to interact with hvplots. Hvplot also provides widgets to interact with teh data. These will be reviewed later in the day.

Ask students if they have any questions before moving onto the next activity.

- - -

### 8. Students Do: Plotting a Visual Takeover (15 minutes)

In this activity, students re-visit plots they made earlier in the class using Matplotlib and they re-create them as hvplots. This bridge assignment aims to demonstrate the similarities between hvplot plot API and Matplotlib's.

**Instrutions**

* [README.md](Activities/08-Stu_Plotting_Visual_Takeover/README.md)

**Files**

* [plotting_visual_takeover.ipynb](Activities/08-Stu_Plotting_Visual_Takeover/Unsolved/Core/plotting_visual_takeover.ipynb)

- - -

### 9. BREAK (15 minutes)

- - -

### 10. Instructor Do: Plotting a Visual Takeover Activity Review (5 minutes)

**Files:**

* [plotting_visual_takeover.ipynb](Activities/08-Stu_Plotting_Visual_Takeover/Solved/Core/plotting_visual_takeover.ipynb)

Open the solution, and conduct a dry walkthrough of the solution while explaining the following:

* The hvplot library can be used to create interactive plot visualizations.

* hvplot has attributes that can be used to explicitly create line and bar plots. If an explicit declaration is not desired, the `hvplot` function can be used.

  ```python
  # Plot a hvplot bar chart of the top 20 market cap companies
  top_20_market_cap.hvplot()
  top_20_market_cap.hvplot.line(title='Top 20 Market Cap Companies (in billions)')
  top_20_market_cap.hvplot.bar(title='Top 20 Market Cap Companies (in billions)')
  ```

  ![hvplot_plot.png](Images/hvplot_plot.png)

  ![hvplot_bar_market_cap.png](Images/hvplot_bar_market_cap.png)

If time remains, transition into a small review session. Ask the following guided questions:

* How do hvplots differ from Panads/Matplotlib?

  * **Answer** hvplot visualizations are interactive rather than static. THey also come equipped with widgets that allow users to manage how they want to interact with the data.

* What are example ways in which a user can interact with an hvplot visualization?

  * **Answer** Zooming, panning, hovering, filtering

* Since Matplotlib/Pandas and hvplot plotting APIs work the same way, is hvplot reinventing the wheel by maintaining their own visualization technology?

  * **Answer** No. hvplot abstracts over Pandas/Matplotlib and inherits the objects and attributes already created by these technologies. hvplot leverages pre-existing code rather than creating new code from scratch.

Ask for any remaining questions before moving on.

- - -
