# Plotting Relocation

Your parents are considering relocating to another state because of the rising hospital costs in New Jersey for Diabetes care. One of their main considerations is moving to a location where there is low cost offerings for diabetes services.

Using hvPlot, analyze and plot the provided hospital claims data. Use the widgets to explore the data and get specific detail about each state and provider. Make sure to perform all analysis using the visualization and supporting widgets.

## Instructions

1. Open the [starter file](Unsolved/plotting_relocation.ipynb), and filter the `hospital_data` for **DRG Definition** `638 - DIABETES W CC`. `638 - DIABETES W CC` is the diagnostic code for Diabetes conditions with complications or co-morbidities.

2. Get an understanding of NJ costs by filtering the by **Provider State** of `NJ`.

3. Using the filtered hospital data for `638 - DIABETES W CC`, identify the average of all payments by **Provider State**. Then, sum by **Average Total Payments**. Hint: Use Pandas `groupby` function.

4. Plot the aggregated data using `hvplot.bar` function. Explore the unsorted data using the **pan** and **zoom** widgets. Zoom in and out to get better clarity on the data.

5. Sort the underlying visualization data from lowest to highest average total payments. Identify the 10 states with the lowest Diabetes diagnostic costs.

6. Use the **box zoom** widget to zoom in on all states with total average payments less than $2000.

7. Reset the visualization and use the **pan** widget to see the highest point of the visualization. Then, use the **box zoom** or **wheel zoom** widgets to zoom in on the data.

8. Identify the 10 states with the highest total average payments for Diabetes diagnostic services.

9. Use the **Save** widget to save your visualizations.
