## 6.1 Lesson Plan: PyViz Formation

### Overview

In today's class, students will learn how to use hvPlot to create interactive visualizations for data exploration and analysis. They'll also be introduced to PyViz, a visualization ecosystem built for Python development, with a focus on the differences and advantages of using interactive plotting technologies (like hvPlot) over technologies that provide static plots (e.g., Pandas and Matplotlib).

The goal of this lesson is to educate students on how revolutionary interactive plots are, and enable them to create their own interactive visualizations for self-service data analysis and data exploration. Most importantly, today's class will teach students how to tell and interpret stories through data.

### Class Objectives

By the end of class, students will be able to:

* Comprehend the why, what, and how of data visualization

* Explain the use cases for different visualization libraries

* Describe the PyViz origin story

* Set up the PyViz ecosystem

* Create interactive charts using hvPlot

* Master hvPlot widgets for data exploration

* Compose and overlay visualizations using hvPlot

* Customize and interpret data visualizations

---

### Instructor Notes

* As a reminder, slack out the [PyViz Installation Guide](../Supplemental/PyVizInstallationGuide.md). Tell students that they should already have PyViz installed for class today, and to use office hours to debug any problems.

* Welcome to the first day of programming with PyViz and interactive plotting! You will guide students through a series of increasingly complex activities, which serve as the foundation for the next class, as well as the homework. Today's class should feel like an evenly paced introduction to PyViz that both challenges students and engages them with relatable use cases.

* Today's class will introduce students to what PyViz is, fundamental PyViz concepts and technologies within the ecosystem, and factors that make interactive plotting different from static plotting.

* Look for opportunities to include real-world examples in your lectures to make concepts more concrete and relatable for students. Feel free to draw upon your own experience using interactive visualization technologies in the professional world.

* The financial focus for this unit is the real estate market. Real estate is a great domain for this type of lesson because real estate data is easily visualized with map charts. Visualizations can also help analysts scour through listings to find ideal property locations and sales.

  * Make sure to emphasize the real-world use cases of visualizing real estate, such as finding the best place to move to, since some students may not find the real estate market as exciting as the stock market.

* A key component of today's class will be getting students to not only create visualizations, but to explore their visualizations using widgets. Therefore, each assignment will serve two purposes: coding the visualization, and analyzing the visualization to make key insights about the data.

* Remember that the purpose of today's class isn't just to teach students how to make interactive plots, but how to use them in order to tell stories, which users can take a deep dive into with the interactive widgets provided by PyViz's technologies.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [6.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=10e96d93-f5d1-4563-910f-aab600c8d69d) Note that this video may not reflect the most recent lesson plan.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 6.1 Slides](https://docs.google.com/presentation/d/1xl16wzFm4AY7W2zcU5f3GYPuwOVBgbmsoB9npYUrxtg/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 min)

Welcome to Unit 6! This unit is dedicated to teaching students all they need to know about data visualization using the PyViz visualization platform.

Open the slideshow, navigate to the PyViz section, and highlight the following:

* Visualizations have already been used in class (Matplotlib plots). However, these visualizations have been static. While static visualizations are helpful in displaying data, the data cannot be interacted with or explored in the same way. For this reason, students will learn how to create interactive plots.

* To create interactive plots, users must access visualization libraries and packages that offer interactive visualizations. Otherwise, visualizations have to be coded manually, which can be extremely cumbersome.

* PyViz is a data visualization ecosystem made specifically for Python. PyViz itself works as a wrapper around these various technologies.

  * Example visualization technologies included with PyViz are hvPlot, Plotly Express, and Panel.

* PyViz aims to provide a single stop-and-shop space for all data visualization needs.

* The creators of PyViz recognized that one technology or package cannot solve all data visualization needs. PyViz was created to provide developers with a platform that enables more than one data visualization package to be used for a project.

* Interactive visualizations:

    * Allow data to be explored and analyzed in the most efficient and effective manner for human eyes.

    * Give users the ability to pan, zoom, and filter data elements and values.

    * Include functionality that allows data to be sorted off different values with a single click.

End by telling students that gone are the days where simple line, bar, and histogram charts satisfied data visualization and data analysis needs. Students will now learn how to create interactive and innovative visualizations.

Ask for any questions before proceeding.

---

### 2. Instructor Do: Review Homework (10 min)

Transition into a demonstration of the types of visualizations that can be made using PyViz by previewing the homework.  

**Files:**

* [Homework Instructions](https://github.com/coding-boot-camp/FinTech-Lesson-Plans/blob/master/02-Homework/06-PyViz/Instructions/README.md)

* [Homework Dashboard Solution](https://github.com/coding-boot-camp/FinTech-Lesson-Plans/blob/master/02-Homework/06-PyViz/Solutions/dashboard.ipynb)

* [Homework Rental Analysis Solution](https://github.com/coding-boot-camp/FinTech-Lesson-Plans/blob/master/02-Homework/06-PyViz/Solutions/rental_analysis.ipynb)

Navigate to the Unit 6 Homework instructions, and communicate the following:

* This week’s homework focuses on visualizing and analyzing real estate data to identify the best properties in Toronto.

* The homework includes using hvPlot and Plotly Express to create interactive data visualizations. These data visualizations will then be integrated with Panel in order to create a digital dashboard that contains multiple tabs.

* Creating interactive data visualizations allows the consumer of the data to explore the data and find structure, patterns, and insights that are important to them.

* In an investment scenario, offering a way to explore the real estate market interactively gives the investor the power to find properties that are of particular interest to them. In scenarios like these, it is the visualizations that help users make decisions.

Demo the homework solution by giving students a preview of the solution.

![homework_demo](Images/homework_demo.gif)

Ask the students for any questions before moving forward.

---

### 3. Instructor Do: Intro to PyViz (5 min)

Students will now be introduced to PyViz with a facilitated instructor-led discussion. This will focus on the advantages of PyViz over individual technologies (HoloViews, Matplotlib, D3.js, etc.).

Communicate to students that the Python environment is packed with a number of different visualization technologies that are all wrapped together into one platform, called PyViz.

Go to the slideshow, navigate to the PyViz Instructor Demo slide, and highlight the following:

* PyViz is a data visualization ecosystem that gives developers an easy way to access multiple data visualization libraries at one time.

* Each visualization technology in the PyViz ecosystem has the power and features to provide standalone visualizations. Each technology also has its strengths and weaknesses, which will be explored later.

* PyViz’s platform allows the integration of different visualization technologies to create dashboards (which can be done with PyViz’s Panel software). This is pivotal for FinTech, as PyViz provides all the necessary tools needed to create financial dashboards for personal and corporate use.

* For FinTech, using PyViz means you have access to your standard plots as well as finance specific plots, like candlestick charts. Another benefit of PyViz is that the sheer number of plotting technologies means that there's a greater chance of users finding the visualizations they need.

Facilitate discussion by asking the following questions:

* Let’s say I just wanted to use Matplotlib and HoloViews. Why not just download those technologies specifically, rather than installing PyViz?

  * **Answer:** Matplotlib and HoloViews may not satisfy all of the visualization tools required. For example, Matplotlib and HoloViews provide visualizations, but they do not offer a way to create a dashboard. Installing PyViz will ensure all viable technologies are accessible.

  * **Answer:** Installing PyViz instead of just the individual technologies would mean that you’d get access to the individual technologies, as well as the integration architecture that PyViz uses to integrate the libraries.

* What other environment have we worked in that resembles the PyViz environment?

  * **Answer:** The Anaconda environment.

Ask if there are any questions before moving on.

---

### 4. Instructor Do: Intro to HvPlot (5 min)

Students will now participate in a lecture on what hvPlot is, and its data visualization offerings.

Go to the slideshow, navigate to the hvPlot section, and introduce students to the world of hvPlot interactive graphs!

* Explain to students that hvPlot is a technology that brings plots to life.

* HvPlot abstracts over Python visualization libraries like Matplotlib, Pandas, and Streamz. The abstraction allows hvPlot to utilize the standalone plotting mechanisms of these technologies.

* HvPlot provides the FinTech industry with a new way of interacting with financial data. Instead of analyzing ledgers, finance professionals can just explore an interactive plot and digest large datasets visually.

* This abstraction also allows hvPlot to transform the static plots (e.g., Matplotlib plots) into interactive sandboxes for data exploration and analysis. HvPlots allow for:

  * panning

  * zooming

  * hovering

  * clicking

  * filtering

Encourage students to review some of the [example plots](https://hvplot.pyviz.org/) on their own time. Make sure to slack out this link.

```text
https://hvplot.pyviz.org/
```

If time remains, review some of the common hvPlot charts and their interactive features. Highlight the following:

* Line plots

  ![hv_plot_1.PNG](Images/hv_plot_1.PNG)

* Streamz

  ![hv_plot_2_streamz.PNG](Images/hv_plot_2_streamz.PNG)

* Geospatial

  ![hv_plot_3_geo_views.PNG](Images/hv_plot_3_geo_views.PNG)

* Network

  ![hv_plot_4_networkx.PNG](Images/hv_plot_4_networkx.PNG)

Ask for any questions and then continue on to the next activity.

---

### 5. Instructor Do: HvPlot Demo (10 min)

Students will now be introduced to a working demo of hvPlot.

**Files:**

* [hvPlot.ipynb](Activities/01-Ins_hvPlot_Demo/Unsolved/hvPlot.ipynb)

Open the [starter file](Activities/01-Ins_hvPlot_Demo/Unsolved/hvPlot.ipynb), and live code the following:

* The hvPlot library has to be imported into the Python environment. HvPlot offers a library called **hvPlot.Pandas** that integrates hvPlot with Pandas DataFrame API. This allows Pandas DataFrames to be visualized using hvPlot.

  ```python
  import hvplot.pandas
  ```

* The great thing about hvPlot being abstracted over Pandas is that the two technologies share plotting interfaces.

* Emphasize to students that even though hvPlot uses the function `hvplot` and not Pandas `plot`, the `hvplot` function actually makes reference to the Pandas `plot` interface. This allows for hvPlots to be created and manipulated in the same ways as Pandas plots (including plot attributes), just with an interactive component.

* The `hvPlot` function is used to create a standard hvPlot chart. For example, when applied against a DataFrame containing cumulative returns for five different tickers, hvPlot would create a visualization using the metadata and data from the DataFrame. The user needs no configuration.

  ```python
  # Data Prep
  df_idx = pd.date_range('1/1/2018', periods=1000)
  df = pd.DataFrame(
    np.random.randn(1000,4),
    index=df_idx,
    columns=('APPL','GOGLE','AMMD','BCOIN')
  ).pct_change()

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

* The `hvPlot` function also has a `bar` attribute for visualization of categorical data. It works the same as the `line` attribute, but it creates a bar visualization rather than a line. It is important to note to students that bar plots require categorical data, and not just time series data. Bar plots need to compare the x-axis against the y-axis.

  ```python
  # Data Prep
  df = pd.DataFrame(
    {'ticker':['APPL','GOGLE', 'AMMD','BCOIN'],
    'daily_return':(4.50,10,33.0,55.25)}
  )

  # Use hvplot.bar() to create bar plot with categorical data
  df.hvplot.bar(x='ticker', y='daily_return', xlabel='Ticker', ylabel='Daily Return', rot=90)
  ```

  ![hvplot_bar.png](Images/hvplot_bar.png)

If time remains, choose either the line or bar visualization, and demonstrate to students how to use hvPlot's interactive features. Highlight the following:

* Hover over a data point to highlight hover interaction. Explain that hovering allows users to hone in on the plot value being observed.

* Click and drag the visualization to pan to the left and right. Communicate that visualization panning allows for data to be analyzed across time more effectively.

* Select an element on the legend to filter it out. Show that this allows data to be hidden as needed. With just one click, data can be curated to specific analytic needs on the fly.

  * Emphasize to students that this is incredibly difficult to do with standard plotting packages like Pandas or Matplotlib. Getting these out-of-the-box features with hvPlot is not just powerful, its groundbreaking! It would take longer to code the filter than it would a user clicking the legend.

  * Static visualizations require the underlying data to be changed in order for a visualization to be updated; with interactive visualizations, data can be filtered on demand.

* Indicate to students that these are just two ways to interact with hvPlots. HvPlot also provides widgets to interact with the data. These will be reviewed later in the day.

Ask students if they have any questions before moving onto the next activity.

---

### 6. Student Do: Plotting a Visual Takeover (15 min)

For this activity, students will revisit plots they made earlier using Matplotlib and recreate them as hvPlots. This bridge assignment aims to demonstrate the similarities between the hvPlot plot API and Matplotlib's API.

**Instructions:**

* [README.md](Activities/02-Stu_Plotting_Visual_Takeover/README.md)

**Files:**

* [plotting_visual_takeover.ipynb](Activities/02-Stu_Plotting_Visual_Takeover/Unsolved/Core/plotting_visual_takeover.ipynb)

---

### 7. Instructor Do: Plotting a Visual Takeover Activity Review (10 min)

**Files:**

* [plotting_visual_takeover.ipynb](Activities/02-Stu_Plotting_Visual_Takeover/Solved/Core/plotting_visual_takeover.ipynb)

Open the solution and conduct a dry walkthrough while explaining the following:

* The hvPlot library can be used to create interactive plot visualizations.

* HvPlot has attributes that can be used to create line and bar plots explicitly. If an explicit declaration is not desired, the `hvplot` function can be used.

  ```python
  # Plot a hvplot bar and line charts of the top 20 market cap companies
  top_20_market_cap.hvplot()
  top_20_market_cap.hvplot.line(title='Top 20 Market Cap Companies (in billions)')
  top_20_market_cap.hvplot.bar(title='Top 20 Market Cap Companies (in billions)')
  ```

  ![hvplot_plot.png](Images/hvplot_plot.png)

  ![hvplot_bar_market_cap.png](Images/hvplot_bar_market_cap.png)

* Ask students if anyone completed the challenge portion of the assignment. Let students know that scatter plots can be created with the following code:

    ```python
    # Plot a scatter plot using hvplot function to display the relationship between price vs. earnings/share
    sp500_companies_csv.hvplot(kind='scatter', x='Earnings/Share', y='Price')
    ```
  ![hvplot_scatter.png](Images/hvplot_scatter.png)

If time remains, transition into a small review session. Ask the following guided questions:

* How do hvPlots differ from Pandas and Matplotlib?

  * **Answer:** HvPlot visualizations are interactive rather than static. They also come equipped with widgets that allow users to manage how they want to interact with the data.

* What are examples of ways in which a user can interact with an hvPlot visualization?

  * **Answer:** Zooming, panning, hovering, filtering

* Since Matplotlib or Pandas and hvPlot-plotting APIs work the same way, is hvPlot reinventing the wheel by maintaining their visualization technology?

  * **Answer:** No. HvPlot abstracts over Pandas or Matplotlib, and inherits the objects and attributes already created by these technologies. HvPlot leverages existing code rather than creating new code from scratch.

Ask for any remaining questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: HvPlot Widgets (10 min)

By the end of this activity, students and the instructor will have deep-dived into the different interactions possible with hvPlots. While students may have used some of the widgets already, this activity will serve as a formal review of each button and interaction.

**Files:**

* [hvplot_widgets.ipynb](Activities/03-Ins_hvPlot_Widgets/Solved/hvplot_widgets.ipynb)

Navigate to the slides section titled "Interactive Visualizations" and use them to briefly explain the following:

* Interactive visualizations are charts and graphs that can be manipulated by user interaction. Example interactions include clicking, panning, and zooming, all of which come out of the box with hvPlot.
 
* The widget bar will be present for all plots created using the `hvplot` function.

  ![hvplot_widget.png](Images/hvplot_widget.png)

* The hvPlot widget bar gives users the ability to choose how they want to interact with the data.

* The widgets bar includes buttons for the following interactions:

  * panning

  * box zoom

  * wheel zoom

  * save visualization

  * hover

* Panning allows users to move the data on the screen in all directions. This is particularly valuable when trying to view data across time, outlying data points, or even high volume. Instead of having to zoom out to see all data, panning brings data into the forefront of the visualization as needed.

  ![hvplot_pan.gif](Images/hvplot_pan.gif)

* The box zoom interaction zooms into data points based on a selection drawn.

  ![hvplot_box_zoom.gif](Images/hvplot_box_zoom.gif)

* Wheel zoom works similarly to box zoom; however, the click wheel is used to magnify data points.

  ![hvplot_wheel_zoom.gif](Images/hvplot_wheel_zoom.gif)

* Another way to interact with visualizations is to save them. HvPlot allows visualizations to be saved as PNG files for later use.

  ![hvplot_save.gif](Images/hvplot_save.gif)

* Hovering is also a key interaction. Hovering over a value in a visualization shows the actual value for that data point.

  ![hvplot_hover.gif](Images/hvplot_hover.gif)

* HvPlot also includes a reset widget button, which resets all visualization interactions. If the visualization was previously zoomed in at 110%, the reset would bring the zoom percentage back to 100%.

  ![hvplot_reset.gif](Images/hvplot_reset.gif)

* Explain to students that widget activities can be combined. Clicking pan, wheel, and hover buttons enables users to pan, zoom, and get details by hovering all at the same time.

  * Point out to students that certain widgets cannot be used with other widgets. For example, users cannot pan and box zoom at the same time. One action has to occur first, and then the second widget option can be chosen.

  ![hvplot_all_actions.png](Images/hvplot_all_actions.gif)

Transition into a live demo of the above information by opening the [solution file](Activities/03-Ins_hvPlot_Widgets/Solved/hvplot_widgets.ipynb)
 and walking students through how to manipulate hvPlots by using the widgets bar.

Ask for any questions before moving on.

---

### 10. Student Do: HvPlot Widgets (15 min)

In this activity, students will play around with the hvPlot widgets to get more accustomed to the different types of interactions supported with hvPlots. Students will use hvPlot visualizations to explore hospital claims data and answer a few basic questions about the data.

**Instructions:**

* [README.md](Activities/04-Stu_hvPlot_Widgets/README.md)

**Files:**

* [hvplot_widgets.ipynb](Activities/04-Stu_hvPlot_Widgets/Unsolved/hvplot_widgets.ipynb)

---

### 11. Instructor Do: HvPlot Widgets Activity Review (10 min)

For this activity, the instructor will lead a facilitated review. Emphasis is placed on what each widget does, and how widgets can be used in conjunction with one another to take a deep dive into data analysis and exploration.

Data for this activity was retrieved from [data.cms.gov](https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/97k6-zzx3).

**Files:**

* [hvplot_widgets.ipynb](Activities/04-Stu_hvPlot_Widgets/Solved/hvplot_widgets.ipynb)

Engage students in a review discussion by asking the following questions:

* HvPlots have six standard widgets. One of them is pan. What are the other five widgets?

  * **Answer:** Box zoom, wheel zoom, save, refresh, and hover.

* Name some of the advantages to using hvPlot over a plotting API like Matplotlib or Pandas.plot?

  * **Answer:** Visualizations are interactive rather than static.

  * **Answer:** HvPlot dynamically handles data, so the best visualizations can be created. The `hvPlot` function figures out the best way to visualize the data on its own. This might mean a line vs. bar plot.

* Sometimes the text on display can be hard to read. Labels can become illegible, depending on the amount of data being plotted. What's the best way to take a deep dive into the data and improve clarity and understanding?

  * **Answer:** Use the zoom widgets. This will limit the amount of data displayed on the screen, which will magnify the x-axis and y-axis values. This differs from static plots, because static plots would require the width of the plot to be manipulated.

  ![enlarging_text.gif](Images/enlarging_text.gif)

Ask for any remaining questions before moving on.

---

### 12. Instructor Do: Composing Plots (10 min)

This activity teaches students how to create plot layouts and overlay visualizations to create a centralized location for comparative data analysis. By the end of the activity, students will have received a dry walkthrough demo on how to combine two plot objects to create a plot with subplots.

**Files:**

* [composing_plots.ipynb](Activities/05-Ins_Composing_Plots/Solved/composing_plots.ipynb)

Go to the slideshow, navigate to the Composing Plots instructor demo section, and highlight the following:

* One of the most valuable and powerful features that hvPlot provides is the ability to compose multiple visualizations.

* Composing plots is a quick and easy way to create a plot with subplots.

* Plots can be composed and overlaid by using the `+` and `*` operators. HvPlot handles formatting and creates the layout for the new visualization, deciding the best way to visualize the data.

Open the starter file and facilitate a dry walkthrough demonstration of composing plots using the `+` and `*` operators.

* One way to compose plot objects is to use the `+` layout operator. The layout operator will place two plots side by side. HvPlot is so powerful and cutting edge that plots of different types can be composed.

  ```python
  # Compose plots using + operator
  total_payment_by_state.hvplot.bar() + sorted_data.hvplot.line()
  ```

  ![compose_layout.png](Images/compose_layout.png)

* Plots can also be overlaid using the `*` operator, which places the two plots along the same axis. For example, if one wanted to analyze Average Total Payments in relation to Average Medicare Payments, plots representing both per state could be composed in one plot. Note to students that labels should be used when overlaying plots; labels will identify which plot is which.

  * Even plots of different types can be overlaid (e.g., line and bar). HvPlot will align the data from both plots along the same axis.

```python
payment_by_state_med = procedure_699_charges[['Average Medicare Payments','Provider State']]
total_payment_by_state_med = payment_by_state_med.groupby('Provider State').sum()
sorted_data_med = total_payment_by_state_med.sort_values('Average Medicare Payments')
sorted_data.hvplot() * sorted_data_med.hvplot()
```

![compose_overlay.png](Images/compose_overlay.png)

* Once the plots have been composed, users can interact with both (sub) plots with a single widget bar.

  ![single_widget_bar.gif](Images/single_widget_bar.gif)

Answer any questions before moving on to the next activity.

---

### 13. Student Do: Composing Masterpieces (10 min)

In this activity, students will use information they learned in the instructor demo to customize hvPlots, using a range of options to customize the color, labels, and axis alignments.

Circulate through the room while students work. If there is a student who completes the activity first or seems to be helping peers, ask if they'd like to volunteer to do a dry walkthrough for the review activity.

Encourage any students who finish early to help their classmates with one-on-one troubleshooting.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/usda-rural-development-single-family-section-502-direct-active-loans-by-congressional-dist).

**Instructions:**

* [README.md](Activities/06-Stu_Composing_Masterpieces/README.md)

**Files:**

* [composing_masterpieces.ipynb](Activities/06-Stu_Composing_Masterpieces/Unsolved/composing_masterpieces.ipynb)

---

### 14. Instructor Do: Composing Masterpieces Activity Review (10 min)

The instructor will ask a student volunteer to conduct a dry walkthrough of the Composing Masterpieces solution.

**Files:**

* [composing_masterpieces.ipynb](Activities/06-Stu_Composing_Masterpieces/Solved/composing_masterpieces.ipynb)

Initiate the review session by asking the student volunteer to conduct a dry walkthrough. If no student was identified, conduct a dry walkthrough yourself. If the student needs help facilitating the review, ask guided questions such as:

* How many different ways can you compose plots? What are the operators?

  * **Answer:** Two. `+` and `*`.

* What does the `+` operator do?

  * **Answer:** It creates a layout where each plot is placed adjacent to the other.

* What does the `*` operator do?

  * **Answer:** It overlays plots where each plot is placed along the same axis.

* How many widget bars are created when plotting? One, or one for each plot?

  * **Answer:** One.

Make sure the the following points are highlighted during the walkthrough: 

* The `+` operator is used to compose plots adjacent to each other. This creates a single plot that contains more than one visualization.

  ```python
  # Slice data for Total Average Loan Amount by 2015-2016 and 2010-2014 date ranges
  loan_data_range_1 = loan_data['2015 - 2016']
  loan_data_range_2 = loan_data['2010 - 2014']
  loan_data_range_grp = loan_data_range_1.sort_values()
  loan_data_range_grp_2 = loan_data_range_2.sort_values()

  # Plot data for date ranges
  plot_2015_2016 = loan_data_range_grp.hvplot(label='2015 - 2016')
  plot_2010_2014 = loan_data_range_grp_2.hvplot(label='2010 - 2014')

  # Compose plots
  plot_2015_2016 + plot_2010_2014
  ```

  ![compose_layout.png](Images/compose_layout.png)

* The `*` operator is used to overlay plots along the same axis. This results in one plot with multiple subplots, rather than plots that are adjacent to another (like when using the `+` operator).

  ```python
  # Overlay plots
  plot_state_avgs * plot_2015_2016 * plot_2010_2014
  ```

  ![compose_overlay.png](Images/compose_overlay.png)

* When plots are composed, only one widget menu is provided. This single menu can be used to control each of the plots.

  ![single_widget_bar.gif](Images/single_widget_bar.gif)

Ask for any remaining questions before moving on.

---

### 15. Instructor Do: Visualization Options (10 min) (Critical)

The goal of this activity is to provide students with a dry walkthrough demonstration of how to use hvPlot plot attributes and options to customize the look and feel of visualizations. This activity will enable students to perfect their visualizations by fine-tuning details such as axis labels, and to create attractive color themes and effects.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/real-estate-sale-history-06c8f).

**Files:**

* [viz_options.ipynb](Activities/07-Ins_Viz_Options/Solved/viz_options.ipynb)

Open the starter file, and perform a dry walkthrough of the solution, highlighting the following:

* HvPlots do not always come out perfect. Customization options give users the ability to customize the look and feel of their visualizations.

  ```python
  # Read in data, filter, and slice
  home_sale_prices = pd.read_csv('../Resources/housing_sale_data.csv',index_col='salesHistoryKey')
  home_sale_prices = home_sale_prices[home_sale_prices['saleDate'] > '2019-06-01'][home_sale_prices['saleDate'] < '2019-06-31']

  # Slice data
  sale_prices_by_year = home_sale_prices[['saleAmt','saleDate']].groupby('saleDate').mean().sort_values('saleDate')

  # Plot data without rotation
  sale_prices_by_year.hvplot.bar(x='saleDate',y='saleAmt')
  ```

  ![hvplot_oob_issues.png](Images/hvplot_oob_issues.png)

* Working with large amounts of data will often make axis labels impossible to read. The `rot` attribute allows users to customize label angles to make reading labels easier. The `rot` attribute accepts an integer value that indicates the angle at which x-axis labels should be rotated.

  ```python
  # Plot data with rotation
  sale_prices_by_year.hvplot.bar(x='saleDate',y='saleAmt', rot=90)
  ```

  ![plot_no_rot.png](Images/plot_no_rot.png)

  ![plot_with_rot.png](Images/plot_with_rot.png)

* Axes labels can be configured to be formatted in a specific way. The `opts(xformatter)` and `opts(yformatter)` allows users to specify string (e.g., `%.2f`) or NumberFormatter formatting objects.

  ```python
  # Use string formatting to show no decimal places for saleAmt
  sale_prices_by_year.hvplot.bar(
    x='saleDate',
    y='saleAmt',
    rot=90).opts(yformatter='%.0f')
  ```

  ![hvplot_formatter.png](Images/hvplot_formatter.png)

* Titles can be added to visualizations using the `opts(title)` parameter.

  ```python
  # Set title
  sale_prices_by_year.hvplot.bar(
    x='saleDate',
    y='saleAmt',
    rot=90).opts(
      title='Arlington, VA Housing Sale Prices June 2016'
    )
  ```

  ![opt_title.png](Images/opt_title.png)

If time remains, discuss how to use the `opts` function to switch the x and y axes.

* The `invert_axes` option is used to change the orientation of a visualization. For example, showing a bar chart with bars moving horizontally rather than vertically.

  ```python
  # Invert axes
  sale_prices_by_year_title.opts(invert_axes=True)
  ```

  ![plot_invert.png](Images/plot_invert.png)

Slack out the [hvPlot customization](http://holoviews.org/user_guide/Customizing_Plots.html) link. The site lists all of the options available in hvPlot. Encourage students to review the list of options.

* Customizing plots -> http://holoviews.org/user_guide/Customizing_Plots.html

Ask if there are any more questions. Then, continue to the student challenge activity.

---

### 16. Student Do: Picture Perfect (15 min)

By the end of this activity, students will employ hvPlot customization attributes and options to perfect and add finishing touches to their visualizations.

Make sure to slack out to students the [hvPlot customization](https://hvplot.pyviz.org/user_guide/Customization.html) documentation, so they have a complete list of all options available.

**Instructions:**

* [README.md](Activities/08-Stu_Picture_Perfect/README.md)

**Files:**

* [picture_perfect.ipynb](Activities/08-Stu_Picture_Perfect/Unsolved/Core/picture_perfect.ipynb)

---

### 17. Student Do: Picture Perfect Activity Review (10 min)

For this activity, students will participate in a five-minute turn and teach to showcase their final, customized visualizations.

**Files:**

* [picture_perfect.ipynb](Activities/08-Stu_Picture_Perfect/Solved/Core/picture_perfect.ipynb)

Instruct students to turn and find a partner to demo their visualizations and customizations. Encourage students to teach each other different tricks and shortcuts they may have learned along the way, as well as to provide constructive criticism to help make the visualizations more appealing and insightful.

Emphasize to students that the activity should focus on how they used the `opts` function and other customization attributes to perfect their visualizations. Use the below discussion points and questions to guide the review session, when or if needed.

* The `opts` function

* Customizing x and y axes

  ![format_axes.png](Images/format_axes.png)

If time remains, ask students the following review questions:

* If you were to categorize the different types of customizations covered, what would the categories be?

  * **Answer:** Label, axes, color, and orientation.

* What is the argument to the `rot` function?

  * **Answer:** The angle of the x-axis labels. This could be 90, 45, etc.

* Can composed plots be customized?

  * **Answer:** Yes. Composed plots can be customized with the `opts` function. The composing operation will have to be placed within parentheses for the `opts` function to take effect.

Ask for any remaining questions before moving on.

---

### 18. Instructor Do: Recap (5 min)

Today has been a whirlwind of visualizations. Now it's time to take a load off and reflect on what was learned.

Explain to students that interactive plots have made data analysis and interpretation significantly easier. Financial data is always changing, especially over time.

* Being able to interact and explore data with a plot makes it easier to spot changes and trends in data.

* With technologies like hvPlot, instead of financial analysts and investors receiving snapshots of data frozen in time, they can now get interactive plots that allow them to get a closer look at the data.

Facilitate a recap discussion with students by asking some of the following questions:

* In what ways will interactive visualizations help with data analysis?

  * **Answer:** Interactive visualizations provide real-time data manipulation and exploration capabilities. This cuts back on the time and lines of code needed to filter, and slice and dice the data for data exploration.

  * **Answer:** A challenge with static charts is that it's difficult to zoom in on, or highlight, a specific data point or range of data points. Interactive visualizations make zooming in on data points easy.

* What are three things that you learned today about hvPlot or interactive visualizations?

  * **Answer:** HvPlot offers all the same features and functionality provided in Matplotlib and Pandas Plot API.

  * **Answer:** HvPlot abstracts over the common data visualization packages. This allows hvPlots to be created and customized, similar to other plots.

  * **Answer:** Interactive visualizations include the ability to zoom, pan, filter, get hover hints, and save visualizations.

* Why bother creating interactive visualizations when Matplotlib and Pandas have already created usable visualization technologies?

  * **Answer:** Interactive visualizations come with their own swagger, such as 3D graphs, color gradients, and custom widgets.

  * **Answer:** Interactive visualizations take data analysis, exploration, and reporting to the next level by providing an opportunity for on-the-fly data changes and manipulations. One user can zoom in to see just a segment of the data, while another user can zoom out to get a holistic, comprehensive view. Coding changes are not necessary.

  * **Answer:** Matplotlib and Pandas Plot API are valuable, but the static plots make it difficult to analyze data at different levels of granularity. When working with static plots, underlying data needs to be manipulated for any change to take place on the visualization. Interactive visualizations allow users to change the data being displayed by filtering, zooming, panning, etc.

If time remains, emphasize one last time the importance of interactive visualizations.

* Communicate to students that with the rise of data science and data-driven industries, interactive visualizations will become a data world staple.

* Explain that as data volumes increase, users will need interactive visualizations to help shift and parse through countless data points. Interactive visualizations empower users to dive deep into data in order to find new and unique structures and patterns that would have required large data dumps otherwise.

* Highlight that without interactive visualizations, users are stuck trying to analyze data in charts and graphs that are too small and static to glean insight from.

* Inform students that interactive data visualization careers are trending; many companies are looking for developers who can wrangle data, as well as create fun and attractive visualizations.

Ask for any remaining questions before ending the class.

## End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
