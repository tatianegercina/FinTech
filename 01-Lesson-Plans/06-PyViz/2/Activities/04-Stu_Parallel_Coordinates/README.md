# Plotting in Parallel

It's been about a week since your last interview with REMAX, and you're still waiting to hear back regarding an offer. In anticipation of the REMAX offer, you've been doing a lot of research about data visualization and the different types of statistical plots.

During your research, you came across a plot you've only seen offered with **Plotly Express**: the **parallel coordinate** plot. Your research has shown you that parallel coordinate plots are great for performing an impact analysis, which is key when assessing trends in the real estate market.

While you're waiting to hear back from REMAX, use the Alleghany County sales and foreclosures data sets to get some practice using parallel coordinate plots. Then, analyze the key performance indicators for real estate in parallel.

## Instructions

1. Open the [starter file](Unsolved/Core/plotting_in_parallel.ipynb), and concatenate the `sales_grp_cnt` and `foreclosures_grp_cnt` DataFrames. Concatenate on `axis=1`. Hint: drop nulls and reset the index after concatenating. Name this object `sales_foreclosures_cnt`.

2. Rename the columns for both `sales_grp_cnt` and `foreclosures_grp_cnt`.

3. Concatenate `sales_grp_cnt` and `foreclosures_grp_cnt`. Concatenate where `axis=1`. Hint: Don't forget to drop nulls and reset the index.

4. Plot `sales_foreclosures_cnt`. Set the color to be based on the Series `index`.

5. Sort the axes so that `index` axes are in the middle of `num_sales` and `num_foreclosures`.

6. Explore the data and understand the relationship between the number of sales, number of foreclosures, and the year.

### Challenge

If time remains, complete the challenge activity below.

1. Return to the `sales` DataFrame, and calculate the sum total of all sales and foreclosures by year. The output should be two DataFrames, one that contains the total dollar amount of housing sales and the other with a total dollar amount of foreclosures.

2. Rename the columns for both DataFrames to `amount_from_sales` and `amount_from_foreclosures`.

3. Plot the data using the Plotly Express `parallel_coordinates` plot.

    ![sort_axes.gif](Images/sort_axes.gif)

### Hint

Use the `reset_index` function whenever an index field needs to be manipulated or displayed on a plot.

Dropping nulls after concatenation will ensure that data relationships are preserved. This will ensure partial data is not being reported on.



© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
