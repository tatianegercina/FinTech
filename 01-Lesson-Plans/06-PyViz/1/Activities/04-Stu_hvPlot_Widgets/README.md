# Plotting Relocation

Your parents are considering relocating to another state because of the rising hospital costs in New Jersey for diabetes care. One of their main considerations is moving to a location where there is low cost offerings for diabetes services.

Using hvPlot, analyze and plot the provided hospital claims data. Use the widgets to explore the data and get specific detail about each state and provider. Make sure to perform all analysis using the visualization and supporting widgets.

## Instructions

1. Open the [starter file](Unsolved/hvplot_widgets.ipynb), and group the filtered hospital data by **Average Total Payments** and **Provider State**. Then, sum by **Average Total Payments**. Hint: Use Pandas `groupby` function.

2. Plot the aggregated data using `hvplot.bar` function. Explore the unsorted data using the **pan** and **zoom** widgets to find the costs for the state of **New Jersey**. Zoom in and out of the data to get a better understanding of costs for different states.

    ![exploring_nj_data.gif](Images/exploring_nj_data.gif)

3. Sort the underlying visualization data from lowest to highest average total payments. Identify the 10 states with the **lowest** diabetes diagnostic costs.

    ![exploring_lowest_states.gif](Images/exploring_lowest_states.gif)

4. Use the **box zoom** widget to zoom in on **all states** with total average payments **less than $2,000**.

    ![exploring_less_than.gif](Images/exploring_less_than.gif)

5. Reset the visualization and use the **pan** widget to see the highest point of the visualization. Then, use the **box zoom** or **wheel zoom** widgets to zoom in on the data.

    ![exploring_most_expensive.gif](Images/exploring_most_expensive.gif)

6. Identify the 10 states with the **highest total average payments** for diabetes diagnostic services.

7. Use the **Save** widget to save your visualizations.



- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
