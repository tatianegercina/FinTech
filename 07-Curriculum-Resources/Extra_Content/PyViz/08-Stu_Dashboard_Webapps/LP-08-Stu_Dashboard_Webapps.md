### 15. Student Do: Monte Carlo Dashboard Web App (15 mins)

In this activity, students will revisit simulations and use Monte Carlo to predict housing sales prices over the next 10 years. Monte Carlo output will be visualized on a dashboard so that insights and decisions can be made based on the predictions.

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

  * **Answer:** Panel's widget bar allows users to manipulate and change the underlying data being presented. This is an incredibly powerful tool, especially since most interactive and static plots do not offer this capability. By being able to control data values, users can perform an impact analysis on the fly and make decisions based on the results of the interaction.

* When running the `servable` and `panel serve` commands, Panel spins up a Bokeh server to host the dashboard. This deploys the dashboard as a web app. What are some of the performance considerations to keep in mind when doing this?

  * **Answer:** The Bokeh server is run locally, and so all dashboard operations are going to use local resources. This could result in large amounts of CPU and RAM being consumed. This could impact load performance.

* Panel components share the same operations as Python lists. How did it feel having the ability to control rows, columns, and tabs in the same way as a list?

  * **Answer:** Being able to control what items went into a row, column, and tab made it extremely convenient to create the dashboard. Panel dashboard components take out all of the work required to make an aesthetically pleasing web app. Gone are the days where one has to worry about margins and relative positioning.

* In many companies, backend developers work with visualization developers to create dashboards and reports. Backend developers will work with languages like Python, and visualization developers will use a separate visualization technology stack (i.e., Cognos, Tableau, etc.). How does it feel knowing that you can now do both jobs with just your Python experience?

  * **Answer:** It is empowering and increases job placement opportunities.

  * **Answer:** It is comforting to know that my Python skills allow me to create an end-to-end process that includes data wrangling, data analysis, and data visualization.

Finish the day off, communicating to students that they have exponentially increased their exposure and understanding of the PyViz ecosystem.

* They can now use Pandas, Matplotlib, hvPlot, and Plotly to create visualizations, and they can use these visualizations for a reporting platform, much in the same way that data analysts and data scientists are doing in the field.

* Emphasize that all executive teams need a dashboard and reporting infrastructure to make decisions and drive business. Programming and visualization skills will make students competitive candidates in the job market.

If time remains, ask students to consider how they want to use interactive plotting technologies and Panel dashboards in the future. Have volunteers communicate their aspirations.

Congratulate students again, and end class by encouraging students to reach out with any questions and to attend office hours.
