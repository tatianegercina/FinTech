### 4. Students Do: Diversification (20 mins)

**Instructions:**

* [README.md](Activities/04-Stu_Correlation/README.md)

**Files:**

* [market_analysis.ipynb](Activities/04-Stu_Correlation/Unsolved/diversification.ipynb)

### 5. Instructor Do: Diversification (5 mins)

**Files:**

* [diversification.ipynb](Activities/04-Stu_Correlation/Solved/diversification.ipynb)

Open the solution and explain the following:

* Remember that the `corr` function compares values from each column-to-column pair. Therefore, make sure that the DataFrame is properly formatted on a column-by-column basis for analysis.

  ![formatted-dataframe](Images/formatted-dataframe.png)

* When viewing a correlation table, it's difficult to distinguish lower values from higher values. Therefore, using the `heatmap` function from the `seaborn` library makes it much easier to discern differences by using color gradients.

  ![correlation-table](Images/correlation-table.png)

  ![correlation-heatmap](Images/correlation-heatmap.png)

* Use the `vmin` and `vmax` parameters to the `heatmap` function to modify the scale of the heatmap. Correlation values range from `-1` to `0` to `+1` therefore the scale of the heatmap will need to reflect accordingly. 

  ![correlation-heatmap-scaled](Images/correlation-heatmap-scaled.png)

* Looking at the heatmap, it would appear as though AMD stock appears to be the least correlated out of any of the other semiconductor stocks. Therefore, AMD stock would be the best semiconductor stock to add to the existing portfolio.

  ![correlation-heatmap-amd](Images/correlation-heatmap-amd.png)