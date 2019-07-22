### 21. Instructor Do: Plotting with Flair (5 mins) (Optional)

In this optional activity, the instructor demonstrates to students how to create other hvPlot types, such as **scatter** and **area** plots.

**Files:**

* [plotting_w_flair.ipynb](Activities/21-Plotting_w_Flair/Unsolved/plotting_w_flair.ipynb)

Open the starter file, and live code the following. Make sure to highlight the corresponding discussion points during the demonstration.

* hvPlot comes with a wide array of supported plot types. **Line** and **bar** charts are the common charts used. However, there are also **scatter**, **area**, just to name a couple.

* Creating a **scatter** plot works the same as any other plot. Execute the `hvplot` function against a DataFrame, and the data will be visualized. The `kind` attribute should be used to specify scatter.

  ```python
  import pandas as pd, numpy as np
  import hvplot.pandas
  dates = pd.date_range('1/1/2000', periods=1000)
  va_foreclosures_by_year  = pd.DataFrame(np.random.randn(1000, 1), index=idx, columns=list('num_foreclosures'))
  ```
