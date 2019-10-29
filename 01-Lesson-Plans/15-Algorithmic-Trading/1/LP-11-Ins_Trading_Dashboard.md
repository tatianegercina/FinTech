### 11. Everyone Do: Trading Dashboard (20 min)

In this activity, instructors will walk students through creating a trading dashboard with Panel using the evaluation metrics generated from prior activities. At this point in time, students should already have exposure to creating dashboards using Panel.

The purpose of this activity is to show students how to create a trading dashboard using the already shown (Unit 6) Panel dashboard library. In particular, students will once again define rows, columns, and tabs, as well as serve the trading dashboard as an actual web application.

**Files:** [trading_dashboard.ipynb](Activities/08-Ins_Trading_Dashboard/Solved/trading_dashboard.ipynb)

Before moving onto the walk through, quickly review the following:

* What is Panel?

  **Answer:** Panel is a high-level dashboarding library that allows a user to create custom interactive web apps and dashboards by connecting user-defined widgets, plots, images, tables, or text. In addition, Panel works with other visualization libraries such as Plotly Express or Hvplot via extensions.

* What is a dashboard?

  **Answer:** A dashboard is an information management tool that organizes, stores, and displays important information from multiple data sources into one, easy-to-access place.

* Why use a dashboard?

  **Answer:** Having a single interactive interface for key information and visualizations allows a user to monitor the health of an existing process, business function, or application, and therefore aids in measuring performance and identifying any discrepancies that may arise.

Open the solution file and and highlight the following:

* Make sure to import the necessary libraries and dependencies in order to use the Panel dashboard and Hvplot visualizations. The `pn.extension()` function automatically detects the need for Panel to load additional extensions; in this case, Panel will load the extension for Hvplot.

  ```python
  import panel as pn
  import hvplot
  import hvplot.pandas
  pn.extension()
  ```

* Before creating the Panel dashboard, we will need to first define the visualizations that will be shown. Therefore, using the DataFrames containing evaluation metrics generated from previous activities, we can create interactive hvplot tables that allow for sorting of columns (ascending or descending) and row selection (selecting one or multiple rows).

  ![hvplot-price-chart](Images/hvplot-price-chart.png)

  ![hvplot-evaluation-metrics](Images/hvplot-evaluation-metrics.png)

* After generating the visualizations that will be added to the Panel dashboard, the next step is to assign the visualizations as rows, columns, and tabs to the Panel dashboard using the Panel `Row`, `Column`, and `Tabs` functions.

  ```python
  # Create rows
  price_chart_row = pn.Row(price_chart)
  portfolio_evaluation_row = pn.Row(portfolio_evaluation_table)
  trade_evaluation_row = pn.Row(trade_evaluation_table)

  # Create columns
  portfolio_column = pn.Column('# Portfolio Evaluation Metrics', price_chart_row, portfolio_evaluation_row)
  trade_column = pn.Column('# Trade Evaluation Metrics', trade_evaluation_row)

  # Create tabs
  trading_dashboard = pn.Tabs(
      ("Portfolio Metrics", portfolio_column),
      ("Trade Metrics", trade_column)
  )
  ```

* Lastly, the `servable` function then serves or initializes the dashboard. There are two ways to use the `servable` function, either in a Jupyter notebook file where the dashboard is displayed within the notebook file itself, or using the terminal command `panel serve --show trading_dashboard.ipynb` which actually creates a web application of the dashboard via the default localhost port 5006.

  ![panel-trading-dashboard-servable](Images/panel-trading-dashboard-servable.png)

  ![panel-trading-dashboard-servable-localhost](Images/panel-trading-dashboard-servable-localhost.png)

Ask if there are any questions before moving forward.
