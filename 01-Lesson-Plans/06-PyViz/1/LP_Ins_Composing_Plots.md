### 18. Instructor Do: Composing Plots (5 mins)

By the end of this activity, students will have received a dry walkthrough demo on how to combine two plot objects to create a plot with subplots. This activity will teach students how to create plot layouts and overlay visualizations to create a centralized location for comparative data analysis.

**Files:**

* [Slides]()

* [composing_plots.ipynb](Activities/18-Ins_Composing_Visualizations/Solved/composing_plots.ipynb)

Navigate to the 6.1 unit slides, and highlight the following:

* One of the most powerful and valuable features that hvPlot provides is the ability to compose multiple visualizations.

* Composing plots is a quick and easy way to create a plot with subplots.

* Plots can be composed/overlayed by using the `+` and `*` operators. hvPlot handles formatting and creating the layout for the new visualization, deciding the best way to visualize the data.

Open the starter file and facilitate a dry walkthrough demonstration of composing plots using the `+` and `*` operators.

* One way to compose plot objects is to use the `+` layout operator. The layout operator will place two plots side by side. hvPlot is so powerful and cutting edge that plots of different types can be composed.

  ```python
  # Compose plots using + operator
  total_payment_by_state.hvplot.bar() + sorted_data.hvplot.line()
  ```

  ![compose_plots_layout.png](Images/compose_plots_layout.png)

* Plots can also be overlayed using the `*` operator, which places the two plots along the same axis. For example, if one wanted to analyze **Average Total Payments** in relation to **Average Medicare Payments**, plots representing both per state could be composed into one plot. Note to students that labels should be used when overlaying plots; labels will identify which plot is which.

  ```python
  payment_by_state_med = procedure_699_charges[['Average Medicare Payments','Provider State']]
  total_payment_by_state_med = payment_by_state_med.groupby('Provider State').sum()
  sorted_data_med = total_payment_by_state_med.sort_values('Average Medicare Payments')
  sorted_data.hvplot() * sorted_data_med.hvplot()
  ```

  ![overlay_plots.png](Images/overlay_plots.png)

* Even plots of different types can be overlayed (i.e. line and bar). hvPlot will align the data from both plots along the same axis.

  ![overlay_plots_diff_type.png](Images/overlay_plots_diff_type.png)

* Once the plots have been composed, users can interact with both (sub) plots with a single widget bar. It's important to note that when using the widget bar with a `+` composed plot, both charts are affected by the widget action. The goal is to view both plots, as well as the data points, side by side, especially when comparing datasets. This is perfect because instead of having to perform the same action (i.e. zoom) for both plots, the action only needs to happen once.

  ![inteacting_w_composed.gif](Images/inteacting_w_composed.gif)

Ask and answer any students questions. Then, move onto the next activity.
