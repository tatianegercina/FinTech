### 7. Instructor Do: Dashboard Components (Panels) (10 mins) (Critical)

By the end of this activity, students will have learned how to create and use Panel **panel** objects to create rows, columns, and tabs for dashboard Panels.

**Files:**

* [dashboard_panels.ipynb](Activities/07-Ins_Dashboard_Components_Panels/Solved/dashboard_panels.ipynb)

Indicate to students that this next activity will focus on creating **panel** objects and using them to create a dashboard layout.

Navigate to the 6.3 slides, and highlight the following:

* Panel **panels** are similar to **pane** objects, except **panels** have a structure.

* **Panels** can consist of **rows**, **columns**, and/or **tabs**. **Rows**, **columns**, and **tabs** all serve as storage mechanisms for media types. For example, a Plotly figure stored as a **pane** can be inserted into a **row**.

* **Rows**, **columns**, and **tabs** are all list objects and operate similarly to Python lists. This means list functions (i.e. add, remove, etc.) can be used to add, remove, and update content.

Open the starter file, and conduct a dry walk through of how to create and use Panel **panels**:

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

* **Tabs** organize components as selectable tabs. **Tabs** are an alternative to putting content in a horizontal or vertical container. **Tabs** allow one dashboard to have multiple reports/views into hte data. Each **tab** could represent a different data set, plot, and/or analytic objective. Tabs are created using the `panel.Tabs` function.

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
