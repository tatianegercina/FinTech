### 4. Students Do: Free Throw Simulation (15 mins)

In this activity, students execute a Monte Carlo simulation to analyze the probability distribution of free throws made (out of 10 shots) for a player with a `70%` accuracy and determine the likelihood of the player making `9-10` free throws in a single session.

**Instructions:**

* [README.md](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/README.md)

**Files:**

* [free_throw_simulation.ipynb](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/Unsolved/free_throw_simulation.ipynb)

### 5. Instructor Do: Review Free Throw Simulation (5 mins)

**Files:**

* [free_throw_simulation.ipynb](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/Solved/free_throw_simulation.ipynb)

Open the solution and explain the following:

* Remember that the `corr` function compares values from each column-to-column pair. Therefore, make sure that the DataFrame is properly formatted on a column-by-column basis for analysis.

  ![formatted-dataframe](Images/formatted-dataframe.png)

* When viewing a correlation table, it's difficult to distinguish lower values from higher values when there are many variables present. Therefore, using the `heatmap` function from the `seaborn` library makes it much easier to discern differences by using color gradients.

  ![correlation-table](Images/correlation-table.png)

  ![correlation-heatmap](Images/correlation-heatmap.png)

* Use the `vmin` and `vmax` parameters to the `heatmap` function to modify the scale of the heatmap. Correlation values range from `-1` to `0` to `+1` therefore the scale of the heatmap will need to reflect accordingly.

  ![correlation-heatmap-scaled](Images/correlation-heatmap-scaled.png)

* Looking at the heatmap and cross-referencing the correlation table, it would appear as though AMD stock appears to be the least correlated out of any of the other semiconductor stocks. Therefore, AMD stock would be the best semiconductor stock to add to the existing portfolio.

  ![correlation-heatmap-focus](Images/correlation-heatmap-focus.png)
  
  ![correlation-table-focus](Images/correlation-table-focus.png)

* Before moving on, ask the students if they have any questions regarding correlation and portfolio diversification.