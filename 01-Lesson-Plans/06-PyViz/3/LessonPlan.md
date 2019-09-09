## 6.3 Lesson Plan: Dashboarding 101

### Overview

In previous classes, students have used static and interactive plots to visualize and communicate financial data. In this lesson, students will leverage pre-existing plots for a Panel dashboard. Students will integrate visualizations and design the layout of a real estate dashboard.

Panel is one of the libraries included in the PyViz package. Panel is used to create dashboards for information visualization. One of the things that makes Panel special is that it has support for Python (dashboards can be created using Python), as well as the common visualization packages used in the Python ecosystem.

By the end of class, students will be competent in creating and using Panel objects to create dashboards to visualize financial data sets that lend insight to financial trends. Panel will be a key skill for students to have; dashboards are one of the primary mechanisms used to communicate and distribute financial records/ledgers, progress, etc. Knowing Panel will enable students to create dashboards and reports as needed.

### Class Objectives

By the end of class, students will be able to:

* Explain what Panel is and its value in relation to data visualization.

* Explain Panel’s role within the PyViz ecosystem.

* Design and develop a Panel dashboard layout using row, column, and tab objects.

* Understand how Panel extensions are used to enable interactivity and plugin integration.

* Integrate Plotly and hvPlot with Panel dashboard using Panel extensions.

* Explain the role of Bokeh in Panel dashboards.

* Deploy a Bokeh server to host Panel dashboard.

### Instructor Notes

* Prepare for the lesson by running the code examples and reviewing the lectures before class. This lesson will be using **Panel**, a library included in the PyViz package. Make sure Panel has been installed and is ready for use. Consult the [PyViz Installation Guide](../Supplemental/PyVizInstallationGuide.md) for help with installation.

* Throughout the lesson, emphasize the importance of dashboards to FinTech. Dashboards offer FinTech a new platform for information and data visualization. Dashboards allow finance professionals to monitor and visualize data trends and changes over time. For example, dashboards are used by investment bankers to track and monitor stocks and trades. They also enable  banking consumers to understand and consume their financial data more efficiently. Moreover, dashboards allow account owners a visual of their spending habits (i.e., bills, groceries, entertainment, shopping, etc.). Be mindful of your machine's resource consumption while running the dashboards. Because the server used to host Panel dashboards as web apps are spun up locally, your machine will have to execute the code and host the web app.

* Be mindful of the class pacing; the pace should feel urgent, but not rushed. Check for understanding regularly, and circulate the classroom with the TAs during activities to offer your assistance. Stick to the Time Tracker as closely as possible. Encourage students in need of support to attend office hours.

* Encourage students to work in pairs or groups on in-class activities to help facilitate discussions as well as troubleshooting. Collaborative exercises such as student-led activity reviews and discussions are built into this lesson.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [6.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=305e7537-e3c7-432a-bc99-aabf00dfdc9b) Note that this video may not reflect the most recent lesson plan.


### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 6.3 Slides](https://docs.google.com/presentation/d/18tMXiNivZRYdFxi4GWCX81Zp_fvh7HDFrNXRqFV-rvg/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (10 mins)

**Files:**

* [welcome-slides](https://docs.google.com/presentation/d/18tMXiNivZRYdFxi4GWCX81Zp_fvh7HDFrNXRqFV-rvg/edit?usp=sharing)

Welcome back! Today marks the last unit of the PyViz Data Visualization unit. Today's lesson will take data visualizations to the next level and will focus on using Panel, a PyViz technology, to create dashboards.

Explain to students that dashboards are data platforms that host multiple reports and visualizations. Dashboards take data reporting to the next level by projecting curated and tailored charts and visualizations that measure performance and corresponding KPIs.

Emphasize that creating a dashboard is different from creating a report.

* Reports are used to help visualize underlying data and enable users to perform their own analysis of the data.

* Dashboards are used to consume data tailored to a specific reporting need. The reporting need will typically satisfy a business objective or evaluate performance based off of certain indicators.

* Dashboards can be used to consolidate multiple reports into one view. Structuring reports as parts of dashboards helps to create a robust reporting platform based off of a digital dashboard.

Describe Panel as an open-source Python library that allows users to integrate widgets, plots, images, and text into a single dashboard. Panel empowers and enables Python developers to create dashboards using a language they already know: Python.

* Panel offers a one-stop shop for data visualization (curated to a specific reporting objective) where users leverage data visualizations and reports to evaluate KPIs.

* Indicate that Panel supports integration with each of the plotting libraries learned so far (i.e., Pandas, Matplotlib, hvPlot, Plotly).

- - -

### 2. Instructor Do: Intro to Panel (10 mins) (Critical)

**Files:**

* [Slides](https://docs.google.com/presentation/d/18tMXiNivZRYdFxi4GWCX81Zp_fvh7HDFrNXRqFV-rvg/edit#slide=id.g480f0dd0a7_0_19)

Continue the discussion about Panel by highlighting the rise of Panel.

* Digital dashboards have become a staple in the tech world. Dashboards are being used to visualize personal finance, company performance and revenue, and even election results/predictions.

* Dashboards typically were created using visualization technology specific stacks, like those associated with Cognos, Tableau, and Qlik.

* **Panel**, a PyViz dashboard package, has altered the data visualization arena by providing a programmatic way to easily create dashboards. Now Python developers can create their own dashboards without having to learn a new technology stack specific for visualization (i.e., Cognos and Tableau). Panel also allows Python developers to be competitive in the visualization job market, which has been primarily reserved for visualization developers.

  * Imagine combining **Panel** with other FinTech technologies, such as **Plaid**. A Python developer could use **Plaid** to get financial data, and then the developer could aggregate and summarize the data with a **Panel** dashboard. This unique marriage of **Panel** and **Plaid** is only possible because **Panel** supports Python.

* Panel's integration with PyViz has made it a highly valuable skill in analytics, as well as a staple in the Python data visualization ecosystem. Dashboards are currently being used to drive business decisions, track and monitor KPIs, and improve operational processes.

* Panel allows data scientists and analysts to create and manage dashboards in the same environment they are completing development, using one technology stack. One developer can use the same technology to create both a data pipeline and dashboard visualizations for the data.

  * PyViz removes the need to use another technology stack for dashboards/visualizations (i.e., Tableau).

Walkthrough some of these [example](https://gapminder.pyviz.demo.anaconda.com/gapminders) dashboards, using the following discussion points to guide the walkthrough:

* PyViz comes with widgets and plugins that allow it to render plots and visualizations from other technologies, like Pandas, Matplotlib, and Plotly. This enables developers to build visualizations in the appropriate technologies and then display them all in one, centralized location with a Panel dashboard.

  ![panel_wrapper.png](Images/panel_wrapper.png)

* Interact with the plots on the website. Use the widget bar to pan, zoom, etc. Emphasize to students that all plotting interactions and widgets can still be used even when plots are rendered with Panel as a dashboard.

  ![panel_interact.gif](Images/panel_interact.gif)

* Explain that this is what makes Panel such a heavy hitter. Pre-existing plots can be embedded within Panel dashboard, and all functionality will be preserved.

If time remains, show students the [NYC taxi trips](https://nyc-taxi.pyviz.demo.anaconda.com/dashboard) dashboard, a geospatial map reporting on taxi routes, pick up and drop off locations, and trips by the hour.

* Interact with the visualization using the widget bar (i.e., pan, zoom, hover, etc). Ask students the following question:

  * Jupyter Lab and Panel can both render interactive plots. In what ways do these technologies differ?

    * **Answer:** Jupyter Lab renders locally, whereas Panel can render plots over the internet.

  * Ask students what the value is behind having a dashboard that opens over the internet rather than just locally.

    * **Answer:** More users can access and leverage the dashboard.

Ask for any questions before moving forward.

- - -

### 3. Instructor Do: Getting Started with Panel (10 mins)

Students will receive a small demo on how to use Panel at a high level.

**Files:**

* [getting_started_panel.ipynb](Activities/01-Ins_Getting_Started_Panel/Solved/getting_started_panel.ipynb)

Open the solved file, and give students a high level run down of how Panel works. Begin by showing students how to prep **Panel** within Jupyter Lab:

* Panel can be imported into Python using the import command.

  ```python
  import panel as pn
  ```

* Panel comes equipped with its own set of libraries, functions, and widgets. An example library is the `panel.interact` library.

  ```python
  from panel.interact import interact
  from panel import widgets
  ```

* When working with Panel in Jupyter Lab, the Jupyter Lab Panel plugin is required. The plugin can be activated using the `extension` command. If the extension is not activated, Panel objects will not render in Jupyter Lab.

  ```python
  pn.extension()
  ```

Walk students through how the `interact` function is used to create quick and easy widget UI controls:

* A commonly used **Panel** function is `panel.interact`. `interact` allows users to create widget UI controls to manipulate function parameters.

  * These parameter widgets provide a convenient and easy way for users to change the values populating the visual, which is extremely handy when completing impact analysis.

  * The **Panel** parameter widget bar will only appear if a function was passed that accepts parameters. If a function without parameters is passed to the `interact` function, the `interact` function will execute, but it will not provide the widget bar.

  * It's important to note that this parameter widget is an added benefit provided by Panel. Not all dashboarding technologies provide this convenient feature.

    ![interact_data_struct.gif](Images/interact_data_struct.gif)

* Most Panel interact function accepts other functions as arguments. This is because the **interact** widget was designed from a functional programming point of view. This approach heavily relies on developers passing functions to functions, which allows Panel to dynamically render content and plots based off of user input/interaction.

  * Imagine creating a dashboard reporting on housing sales by city across 10 years. Instead of having all 10 years of data for every city shown on a plot, you might want to limit the data to a specific year. A **Panel** select list could be used to select the year to report on.

    ```python
      # Define function to choose a year
      def choose_year(year):
          return year
    ```

    ```python
    # Declare one list of years to be used in a Panel select list
    list_of_years = ['2019','2018','2017','2016','2015']
    interact(chooseYear, x=list_of_years)
    ```

    ```python
    # Declare a second list of years to be used in a Panel select list
    list_of_years_2 = ['2014','2013','2012','2011','2010']
    interact(chooseYear, x=list_of_years)
    ```

    ![interact_data_struct_2.gif](Images/interact_data_struct_2.gif)

In addition to Python data structures, the `interact` function can be used with plots. Discuss how **Panel** can be used with plots.

* When used with plots, `interact` will still need to be passed a function that will render the plot.

* **Panel** will then create UI widgets to allow users to dynamically change parameters. An example would be plotting housing transactions data where the number of records plotted is parameterized. The `interact` function will create a widget that allows users to change configure the number of records being plotted.

  ```python
  # Define function to create plot
  def plot_housing_tx(number_of_sales):
      housing_transactions = pd.DataFrame({
      "years": np.random.randint(2010,2019,number_of_sales),
      "sales": np.random.randint(53,500,number_of_sales),
      "foreclosures": np.random.randint(10,147,number_of_sales)}).sort_values(['years','sales'])

      return housing_transactions.hvplot.scatter(x='sales',
                                      y='foreclosures',
                                      c='years',
                                      colormap='viridis',
                                              title='Alleghany, PA Housing Transactions')

  # Render plot with Panel interactive widget
  interact(plot_housing_tx, number_of_sales=100)
  ```

  ![interact_plot.gif](Images/interact_plot.gif)

Ask if students have any questions before continuing.

- - -

### 4. Instructor Do: Panel Dashboard Components (Panes) (10 mins) (Critical)

In this activity, students receive a demonstration of how to use and customize Panel's dashboard components.

**Files:**

* [panel_components.ipynb](Activities/02-Ins_Dashboard_Components/Solved/panel_components.ipynb)

Navigate to the 6.3 slides, and highlight the following:

* Dashboard components are used to create the overall layout and structure of a **Panel** dashboard. Dashboard components are what allow media to be rendered on a **Panel** dashboard.

  * Dashboard components are essentially objects that hold/store the content being visualized on the Panel dashboard.

* Panel dashboards have two main components: **panes** and **panels** (rows, columns, and tabs).

* **Pane** and **panel** objects work in the same way, in the sense that they wrap around pre-existing objects (plots, text, html). Each specific media type will have a helper function that can be used to convert the content to a Panel object.
* For example, there is a `panel.pane.Plotly` function that will create a Plotly pane. There is also `panel.pane.Markdown`.

* Each **pane** type has its own set of **Panel** functions and customization attributes (i.e., height, width, etc).

Open the solution file, and conduct a dry walkthrough. Emphasize the following:

* In order to customize and embed content on a **Panel** dashboard, the object storing the content must first be converted to a Panel object: either a pane or panel.

* The `panel.pane` function can be used to explicitly wrap the original object (i.e., Plotly plot) in a Panel **pane** object.

  ```python
  import pandas as pd
  import numpy as np
  import panel as pn
  import plotly.express as px
  pn.extension('plotly')

  # Define function to create plot
  housing_transactions = pd.DataFrame({
      "years": np.random.randint(2010, 2019, 100),
      "sales": np.random.randint(53, 500, 100),
      "foreclosures": np.random.randint(10, 147, 100)}).sort_values(['years', 'sales'])

  # Create plot
  plot = px.scatter(housing_transactions, x='sales',
                  y='foreclosures',
                  color='years',
                  title='Alleghany, PA Housing Transactions')

    # Create plot
    plot = px.scatter(housing_transactions, x='sales',
                                          y='foreclosures',
                                          color='years',
                                          title='Alleghany, PA Housing Transactions')

    # Wrap Plotly object by explicitly declaring Panel pane
    pn.pane.Plotly(plot)
  ```

  ![plot_as_pane.png](Images/plot_as_pane.png)

* If ever unsure whether or not an object should be wrapped as a **pane** or **panel**, the `panel.panel` helper function can be used to identify the appropriate **pane** or **panel** library to use. `panel.panel` will render the same object as `panel.pane`.

  * Not all objects can be rendered as a Panel **pane**. Some objects, like hvPlots, have to be rendered as **panel**, which is similar to a **pane** but with additional row/column structuring.

  ```python
  # Wrap Plotly object by using panel.panel helper function
  pn.panel(plot)
  ```

  ![plot_as_panel.png](Images/plot_as_panel.png)

* To determine what type of Panel object is at hand, the `panel.pprint` function can be executed against the Panel object. The `panel.pprint` function will return the object type (i.e., Plotly figure, hvPlot figure, PNG image, etc).

  ```python
  # Print the type of object
  pane.pprint()
  ```

  ```
  Plotly(Figure)
  ```

If time remains, reinforce the following key points:

* Reinforce to students that in order to display and interact with content on a Panel dashboard, the content must be converted to a **Panel** object. Once content is in a Panel **pane** object, the rendered content (i.e., plot, image, html, markdown, etc.) can be accessed and called with Panel.

* Panel **panes** and **panels** are similar objects except **panels** are sub-components (rows, columns, and tabs). Rows, columns, and tabs will be explored in an upcoming activity.

Ask if there are any questions before moving forward.

- - -

### 5. Student Do: No Pane, No Gain (15 mins)

In this activity, students complete a MSMD activity where they create a Plotly plot and convert it to a Panel **pane**. The goal of this activity is to reinforce to students the importance of Panel **panes** and their role in the dashboard creation process.

**Instructions:**

* [README.md](Activities/03-Stu_Dashboard_Components/README.md)

**Files:**

* [no_pane_no_gain.ipynb](Activities/03-Stu_Dashboard_Components/Unsolved/no_pane_no_gain.ipynb)

- - -

### 6. Instructor Do: No Pane, No Gain Activity Review (10 mins)

The instructor will conduct a dry walkthrough of the solution to highlight the different approaches that can be taken to create a **pane** object.

**Files:**

* [no_pane_no_gain.ipynb](Activities/03-Stu_Dashboard_Components/Solved/no_pane_no_gain.ipynb)

Open the solution, and explain the following:

* There are two ways in which a Panel **pane** can be created. One way is to use panel helper functions like `interact` and `panel.panel`, which converts media types to Panel **panes**. `interact` does this specifically so that it can create an interactive widget.

  * Ask students the following question: What is the purpose behind the `interact` function? What does it do?

    * **Answer** The `interact` function creates an interaction sliding widget that serves as a way for users to customize data presented on a plot. The `interact` widget is an alternative to hardcoding argument values, and it serves as a separate mechanism for getting user input.

  * In order for panel to create the interaction widget, it has to convert the plot to a **pane** object. The `interact` function handles this conversion behind the scenes.

  ```python
  # Use interact function to create interaction widget
  interact(create_parallel_categories_plot, number_of_records=30)
  ```

  ![panes_with_interact.gif](Images/panes_with_interact.gif)

* Another method used to create Panel **panes** is to use the media-specific pane functions (i.e., panel.pane.Plotly). These functions will execute a process dedicated to converting that media type into a Panel **pane**.

  ```python
  # Use panel.pane.Plotly function to convert plot to pane
  plot_panel = pn.pane.Plotly(create_parallel_categories_plot(30))
  plot_panel
  ```

  ![panel_pane_plotly.png](Images/panel_pane_plotly.png)

* To confirm the **pane** type, the Panel `pprint` function can be used. The function will return the **pane** type (i.e., Plotly figure).

  ```python
  # Check the pane type using the pprint() function
  plot_panel.pprint()
  ```

  ![pprint.png](Images/pprint.png)

* Explain that an alternative to using the media-specific pane function is to use the `pn.panel` helper function. Plots and other media types are passed to this function as arguments. The function will then infer the type of **pane** to create.

Ask for any remaining questions before moving on.

- - -

### 7. Instructor Do: Dashboard Components (Panels) (10 mins) (Critical)

By the end of this activity, students will have learned how to create and use Panel **panel** objects to create rows, columns, and tabs for dashboard Panels.

**Files:**

* [dashboard_panels.ipynb](Activities/04-Ins_Dashboard_Components_Panels/Solved/dashboard_panels.ipynb)

Indicate to students that this next activity will focus on creating **panel** objects and using them to create a dashboard layout.

Navigate to the 6.3 slides, and highlight the following:

* Panel **panels** are similar to **pane** objects, except **panels** have a structure.

* **Panels** can consist of **rows**, **columns**, and/or **tabs**. **Rows**, **columns**, and **tabs** all serve as storage mechanisms for media types. For example, a Plotly figure stored as a **pane** can be inserted into a **row**.

* **Rows**, **columns**, and **tabs** are all list objects and operate similarly to Python lists. This means list functions (i.e., add, remove, etc.) can be used to add, remove, and update content.

Open the starter file, and conduct a dry walkthrough of how to create and use Panel **panels**:

* **Rows** can be created to list components/media in a horizontal container. Row objects can contain different media types, such as Markdown language or different types of plots.

* The `panel.Row` function is used to create a **row**. The function accepts media types as arguments. The function will align all content horizontally.

  ```python
  import pandas as pd
  import numpy as np
  import panel as pn
  from panel.interact import interact
  import plotly.express as px
  import hvplot.pandas
  pn.extension('plotly')

  housing_transactions = pd.DataFrame({
    "years": np.random.randint(2010, 2019, 100),
    "sales": np.random.randint(53, 500, 100),
    "foreclosures": np.random.randint(10, 147, 100)}).sort_values(['years', 'sales'])

  # Create scatter plot
  scatter_plot = px.scatter(
      housing_transactions,
      x='sales',
      y='foreclosures',
      color='years',
      title='Alleghany Sales/Foreclosures Correlation'
  )

  # Create bar plot
  transactions_by_year = housing_transactions.groupby('years').sum().reset_index()
  bar_plot = px.bar(transactions_by_year, x='years', y='sales', title='Alleghany Sales by Year')

  # Create row
  row = pn.Row(scatter_plot, bar_plot)
  row
  ```

  ![panel_row.png](Images/panel_row.png)

* **Columns** are similar to **rows**, except content is aligned in a vertical container. The `panel.Column` function can be used to align content in a vertical fashion. For example, the **row** object previously created could be added to a column that also includes Markdown headers.

  ```python
  # Create column using Markdown and row object
  column = pn.Column(
      '# Alleghany, PA Real Estate Visualizations',
      '## Sales and Foreclosures',
      row)
  column
  ```

  ![panel_column.png](Images/panel_column.png)

* **Tabs** organize components as selectable tabs. **Tabs** are an alternative to putting content in a horizontal or vertical container. **Tabs** allow one dashboard to have multiple reports/views into the data. Each **tab** could represent a different data set, plot, and/or analytic objective. Tabs are created using the `panel.Tabs` function.

  ```python
  # Create tabs
  tabs = pn.Tabs(
      ("Correlations", scatter_plot),
      ("Time Series", bar_plot))
  tabs
  ```

  ![panel_tabs.png](Images/panel_tabs.png)

End the activity by explaining to students that **tabs** can consist of **rows** and **columns**. Combining these objects allow developers to create customized layouts for dashboarding and reporting purposes.

Ask if there are any questions before moving forward.

- - -

### 8. Student Do: The Judge's Panel (15 mins)

Students complete a Find the Path activity where they execute insert, update, and remove operations on Panel **panels**.

Since students have not been taught how to manipulate **panels** using insert, update, and remove functions, make sure to circulate with TAs to provide assistance. Also encourage students to work together in pairs of two.

**Instructions:**

* [README.md](Activities/05-Stu_Dashboard_Panels/README.md)

**Files:**

* [judges_panel.ipynb](Activities/05-Stu_Dashboard_Panels/Unsolved/judges_panel.ipynb)

- - -

### 9. Instructor Do: Judge's Panel Activity Review (10 mins)

**Files:**

* [judges_panel.ipynb](Activities/05-Stu_Dashboard_Panels/Solved/judges_panel.ipynb)

Open the solution and explain the following:

* **Rows**, **columns**, and **tabs** are used to create a dashboard layout in Panel. Media/content can be added to each of these objects using the standard Python list functions, such as `append`.

* Row objects insert content into a horizontal container, allowing each object to be placed adjacent to the other. The `pn.Row` function can be used to create this horizontal container.

  ```python
  # Put parallel plots in a single row
  row_of_parallel = pn.Row(parallel_categories, parallel_coordinates)
  ```

  ![panel_row.png](Images/panel_rows.png)

* Column objects store content into a vertical container. Column panels work just like **row** objects, except data is stored vertically rather than horizontally.

  ```python
  # Insert row_of_parallel and row_of_Bar into a column object with Markdown text
  plots_as_column = pn.Column("# Alleghany Real Estate Dashboard", row_of_parallel, row_of_bar)
  plots_as_column
  ```

  ![panel_column.png](Images/panel_columns.png)

* Tab objects allow media/content to be segmented into different views. Tabs are a key feature that allow dashboards to have more than one report. Each tab can be considered a report or view, and each view can have its own reporting/analytic approach for gaining insights.

  ```python
  # Create tabs
  tabs = pn.Tabs(
      ("All Plots", plots_as_column),
      ("General Plots", row_of_bar),
      ("Statistical Plots", row_of_parallel)
  )
  tabs
  ```

  ![panel_tab.gif](Images/panel_tab.gif)

Ask for any remaining questions before moving on.

- - -

### 10. BREAK (40 mins)

- - -

### 11. Instructor Do: Panel Extensions (5 mins)

In this activity, the instructor leads a facilitated discussion on Panel **extensions**. The goal of this lesson is to get students thinking about what gives Panel the ability to render content from so many different technologies. This activity will solely be a discussion; there is no code.

**Files:**

* [Slides](https://docs.google.com/presentation/d/18tMXiNivZRYdFxi4GWCX81Zp_fvh7HDFrNXRqFV-rvg/edit#slide=id.g5f381b25f9_2_134)

Navigate to the 6.3 slides, and highlight the following:

* Panel supports a wide range of visualization technologies. Support for these technologies are managed by Panel **extensions**.

* Panel supports a number of extensions, including Plotly, Bokeh, and Matplotlib. Extensions give Panel the ability to display and use content created by other technologies.

* Each Panel extension has its own unique features and color schemes. There are also features that are shared across extensions. For this reason, multiple extensions may need to be specified if a dashboard leverages more than one technology (i.e., Plotly and Matplotlib).

* By specifying the extension, multiple media types can be combined to create an informative and insightful dashboard.

* Panel **extensions** are specified using the `extension` function. The `extension` function will load in the corresponding plugin so that content produced by the technology can be rendered and used by Panel.

  ```python
  pn.extension('plotly')
  ```

* Ask students: Panel supports more than one extension being used. How would I tell Panel that I want to use more than one extension?

  * **Answer:** Pass the `extension` function a list of **extensions**. This will initialize each of the listed plugins and allow Panel to display the content as expected.

    ```python
    pn.extension('plotly','bokeh')
    ```

* Communicate to students that not all technologies require an **extension** be specified. For example, when working with Matplotlib, all that is required is a call to the `extension` function. Arguments do not have to be specified.

  ```python
  pn.extension()
  ```

Ask if there are any questions before continuing.

- - -

### 12. Student Do: Extending Plotting (15 mins)

Students complete a Bag of Tricks activity where they create a dashboard that contains map visualizations and hvPlot composed plots. The goal of this activity is to reinforce to students that Panel can support all the visualizations that have been created in class so far.

Data for this activity was retrieved from [ucr.fbi.gov](https://ucr.fbi.gov/crime-in-the-u.s/2015/crime-in-the-u.s.-2015/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2015.xls/view).

**Instructions:**

* [README.md](Activities/06-Stu_Panel_Extensions/README.md)

**Files:**

* [extending_plotting.ipynb](Activities/06-Stu_Panel_Extensions/Unsolved/extending_plotting.ipynb)

- - -

### 13. Instructor Do: Extending Plotting Activity Review (10 mins)

Students will participate in a dry walkthrough and facilitated discussion guided by the instructor. The focus of the discussion will be how multiple technologies can be integrated and embedded on a singular dashboard to create a reporting platform.

**Files:**

* [extending_plotting.ipynb](Activities/06-Stu_Panel_Extensions/Solved/extending_plotting.ipynb)

Open the solution and explain the following:

* Panel supports a number of different visualization extensions. This includes Plotly, hvPlot/Holoviews, and Matplotlib. In order to use an extension, a call has to be made to the `panel.extension` function. The name of the extension (i.e., **plotly**) will need to be passed to the function.

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

* The best way to create a dashboard layout is to strategically group media types into containers.

  * Plots of the same type can be added to the same column/row, and plots of different types can be added to different tabs.

  * Furthermore, plots that serve one specific analytic objective could be rendered on one tab together, while other analytic use cases could be maintained in other tabs.

  ```python
  crime_pop_dashboard = pn.Tabs(
    ("Geospatial", geo_column),
    ("Correlations", scatter_column))

  crime_pop_dashboard
  ```

  ![panel_dashboard_tabs.png](Images/panel_dashboard_tabs.png)

  ![population_crime_dashboard.gif](Images/population_crime_dashboard.gif)

* Integrating Panel columns and tabs with PyViz visualizations creates a dashboard that allows users to analyze a number of visualizations at one time from a one-stop shop.

If time remains, ask students the following review questions:

* What's the underlying Pythonic structure for Panel **panels**?

  * **Answer:** List data structure

* If I wanted to add an object to a row after the row object has been declared, can I?

  * **Answer:** Yes, the row `append` function can be used to insert the new object

* Why do extensions have to be specified when working with **Panel**?

  * **Answer:** Because **Panel** supports a wide range of visualization technologies. Each technology has its own approach to rendering plot look and feel/skins, widgets, etc. In order to preserve the integrity of the visualizations created by each technology, Panel uses extensions to render the visualization objects.

Ask for any remaining questions before moving on.

- - -

### 14. Instructor Do: Dashboards As Web Applications (10 mins) (Critical)

Students learn how to transform their Jupyter notebook dashboards into a **web app**. The instructor will demonstrate how to use the `servable` command to execute and run the dashboard on a server. The instructor will use the same dashboard created from the previous activity.

**Files:**

* [dashboard_webapps.ipynb](Activities/07-Ins_Dashboard_Webapps/Unsolved/dashboard_webapps.ipynb)

Navigate to the 6.3 slides, and communicate the following:

* One of the advantages of using Panel for dashboarding is that Panel dashboards can be deployed as web apps: dashboard applications that are accessible over the internet, rather than just in a Jupyter notebook. This means that any Jupyter notebook containing a Panel object can be deployed as its own independent **web app**.

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

* The web app can be accessed using the URL returned from the `panel serve` CLI command. Enter the URL in a browser, and watch your dashboard load. Note that when the dashboard loads, it will load without all of the code and Jupyter cells. Only the dashboard content will be displayed.

If time remains, ask the following guided question:

* In what ways can Panel dashboards add value to the financial industry?

  * **Answer:** Panel dashboards give financial companies the opportunity to retire one*off/ad hoc reports. Instead of distributing financial reports via email and making graphs and pivot tables in Excel, all reporting can be migrated to Panel dashboards, executed as **web apps**, and made accessible company wide.

  * **Answer:** Panel's interactive dashboards offer financial companies the opportunity to analyze and gain insights from data using an interactive platform. Instead of analyzing financial reports that contain static/stale data, finance professionals can simply utilize a dashboard to access to the latest data.

Ask if there are any questions before moving on.

- - -

### 15. Student Do: Monte Carlo Dashboard Web App (15 mins)

Students complete a Bag of Tricks activity where they revisit simulations and use Monte Carlo to predict housing sales prices over the next 10 years. Monte Carlo output will be visualized on a dashboard so that insights and decisions can be made based off of the predictions.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/real-estate-sales-2001-2016).

**Instructions:**

* [README.md](Activities/08-Stu_Dashboard_Webapps/README.md)

**Files:**

* [monte_carlo_dashboard.ipynb](Activities/08-Stu_Dashboard_Webapps/Unsolved/monte_carlo_dashboard.ipynb)

- - -

### 16. Instructor Do: Monte Carlo Dashboard Web App Activity Review (10 mins)

The instructor and students will review the Monte Carlo Dashboard web app activity with a facilitated discussion. The focus will be on exploring what students found useful, and which features from which technology were the most valuable.

**Files:**

* [monte_carlo_dashboard.ipynb](Activities/08-Stu_Dashboard_Webapps/Solved/monte_carlo_dashboard.ipynb)

Communicate to students that this activity review will be focused on discussing the benefit and usefulness of Panel dashboards, from their point of view.

* Explain to students that creating a report in Jupyter Notebook is much different from deploying a dashboard as a web app. Ask students: Which approach do they feel is more valuable? What are the pros and cons?

  * **Answer:** Creating a dashboard is better for visualizing and interpreting data in order to make data-driven decisions.

  * **Answer:** Creating a report in Jupyter Notebook is easier than creating a dashboard. Reports don't need as much attention and detail when it comes to layouts. With a dashboard, rows, columns, and tabs have to be manipulated.

  * **Answer:** Dashboard web apps don't offer the code used to create the visualization. This is a limitation for technical audiences who would be interested in seeing the code associated with the output.

* Panel comes equipped with a range of features, including interactive widget bars. What is the purpose behind widget bars?

  * **Answer:** Panel's widget bar allows users to manipulate and change the underlying data being presented. This is an incredibly powerful tool, especially since most interactive and static plots do not offer this capability. By being able to control data values, users can actually perform impact analysis on the fly and make decisions based off of the results of the interaction.

* When running the `servable` and `panel serve` commands, Panel spins up a Bokeh server to host the dashboard. This deploys the dashboard as a web app. What are some of the performance considerations to keep in mind when doing this?

  * **Answer:** The Bokeh server is run locally, and so all dashboard operations are going to use local resources. This could result in large amounts of CPU and RAM being consumed. This could impact load performance.

* Panel components share the same operations as Python lists. How did it feel having the ability to control rows, columns, and tabs in the same way as a list?

  * **Answer:** Being able to control what items went into a row, column, and tab made it extremely convenient to create the dashboard. Panel dashboard components take out all of the work required to make an aesthetically pleasing web app. Gone are the days where one has to worry about margins and relative positioning.

* In many companies, backend developers work with visualization developers to create dashboards and reports. Backend developers will work with languages like Python and visualization developers will use a separate visualization technology stack (i.e., Cognos, Tableau, etc). How does it feel knowing that you can now do both jobs with just your Python experience?

  * **Answer:** It is empowering and increases job placement opportunities.

  * **Answer:** It is comforting to know that my Python skills allow me to create an end-to-end process that includes data wrangling, data analysis, and data visualization.

Finish the day off communicating to students that they have exponentially increased their exposure and understanding of the PyViz ecosystem.

* They can now use Pandas, Matplotlib, hvPlot, and Plotly to create visualizations, and they can use these visualizations for a reporting platform, much in the same way that data analysts and data scientists are doing in the field.

* Emphasize that all executive teams need dashboard and reporting infrastructure to make decisions and drive business. The programming and visualization skills will make students competitive candidates in the job market.

If time remains, ask students to consider how they want to use interactive plotting technologies and Panel dashboards in the future. Have volunteers communicate their aspirations.

Congratulate students again, and end class by encouraging students to reach out with any questions and to attend office hours.

### 17. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35 minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings

### End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
