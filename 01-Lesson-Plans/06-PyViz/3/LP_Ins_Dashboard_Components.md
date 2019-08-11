### 5. Instructor Do: Panel Dashboard Components - Panes (5 mins) (Critical)

In this activity, students receive a demonstration of how to use and customize Panel's dashboard components.

**Files:**

* [panel_components.ipynb](Activities/05-Ins_Dashboard_Components/Solved/panel_components.ipynb)

Navigate to the 6.3 slides, and highlight the following:

* Panel dashboards are broken down into components. These components include panes and panels (rows, columns, and tabs).

* Dashboard components are used to create the overall layout and structure of a Panel dashboard. Dashboard component are what allow Panel to render plots, markdown, html, etc.

* Dashboard components are essentially objects that hold/store the content being visualized on the Panel dashboard.

Open the solution file, and conduct a dry walk through. Emphasize the following:

* In order to customize and embed content on a Panel dashboard, the object storing the content must first be converted to a Panel pane. The `panel.pane` function can be used to wrap the original object (i.e. Plotly plot) in a Panel **pane** object.

  ```python
  import pandas as pd
  import numpy as np
  import panel as pn
  import plotly.express as px
  pn.extension('plotly')

  # Define function to create plot
  housing_transactions = pd.DataFrame({
      "years": np.random.randint(2010,2019,100),
      "sales": np.random.randint(53,500,100),
      "foreclosures": np.random.randint(10,147,100)}).sort_values(['years','sales'])

  # Create plot
  plot = px.scatter(housing_transactions, x='sales',
                                        y='foreclosures',
                                        color='years',
                    title='Alleghany, PA Housing Transactions')

  # Wrap Plotly object in Panel Pane
  pn.pane.Plotly(plot)
  ```

* Once content is in a Panel **pane** object, Panel can be used to customize the entirety of the pane using pane options. These include

  * TBD

  * TBD
