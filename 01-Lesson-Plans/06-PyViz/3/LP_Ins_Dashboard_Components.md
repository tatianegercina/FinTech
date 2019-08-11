### 5. Instructor Do: Panel Dashboard Components (5 mins) (Critical)

In this activity, students receive a demonstration of how to use and customize Panel's dashboard components.

**Files:**

* [panel_components.ipynb](Activities/05-Ins_Dashboard_Components/Solved/panel_components.ipynb)

Navigate to the 6.3 slides, and highlight the following:

* Dashboard components are used to create the overall layout and structure of a **Panel** dashboard. Dashboard component are what allow media to be rendered on a **Panel** dashboard.

  * Dashboard components are essentially objects that hold/store the content being visualized on the Panel dashboard.

* Panel dashboards have two main components: **panes** and **panels** (rows, columns, and tabs).

* **Pane** and **panel** objects work in same way in the sense that they wrap around pre-existing objects (plots, text, html). Each specific media type will have a helper function that can be used to convert the content to a Panel object.

  * For example, there is a `panel.pane.Plotly` function that will create a Plotly pane. There is also `panel.pane.Markdown`.

  * Each **pane** type has its own set of **Panel** functions and customization attributes (i.e. height, width, etc).

Open the solution file, and conduct a dry walk through. Emphasize the following:

* In order to customize and embed content on a **Panel** dashboard, the object storing the content must first be converted to a Panel object: either a pane or panel.

* The `panel.pane` function can be used to explicitly wrap the original object (i.e. Plotly plot) in a Panel **pane** object.

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

* To determine what type of Panel object is at hand, the `panel.pprint` function can be executed against the Panel object. The `panel.pprint` function will return the object type (i.e. Plotly figure, hvPlot figure, PNG image, etc).

  ```python
  # Print the type of object
  pane.pprint()
  ```

  ```
  Plotly(Figure)
  ```

If time remains, reinforce the following key points:

* Reinforce to students that in order to display and interact with content on a Panel dashboard, the content must be converted to a **Panel** object. Once content is in a Panel **pane** object, the rendered content (i.e. plot, image, html, markdown, etc.) can be accessed and called with Panel.

* Panel **panes** and **panels** are similar objects except **panels** are sub-components (rows, columns, and tabs). Rows, columns, and tabs will be explored in an upcoming activity.

Ask if there are any questions before moving forward.
