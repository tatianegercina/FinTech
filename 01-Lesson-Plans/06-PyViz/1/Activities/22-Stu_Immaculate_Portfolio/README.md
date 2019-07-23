# Immaculate Portfolio

Your interview with REMAX is just three days away! Take a moment to review your current portfolio, and identify any remaining finishing touches that might be valuable to add. Take into consideration color schemes, types of plots used, and even the orientation of the plots (i.e. `inverted=True`).

Also, add in an **area** and **scatter** plot to provide a glimpse into the quantitative numbers over time, as well as to show your understanding of more advanced, statistical based reporting paradigms.

## Instructions

1. Slice the `loans_data` DataFrame for Series **2017** and **2015 - 2016**. Store the output as `correlation_data`.

2. Run `reset_index` function against `correlation_data` to remove **State Code** index and make it available as a field. Hint: correlation_data.reset_index().

3. Plot the reset `correlation_data` using a **scatter** plot. This will create a visualization that trends the effect 2015 - 2016 aver loan amounts ahd on 2017 loans, if any. Hint: **State Code** should be the `c` value.

4. Don't forget to make your new visualizations picture perfect! Ensure that all visualizations have:

  * A title

  * Readable x and y axes labels and ticks

  * Formatted values

  * Color theme

  * Hover color changes

### Challenge

1. Slice the `loan_data` DataFrame, and calculate the standard deviation of average loan amounts for each date range (i.e. **Total Average Loan Amount**, **2015 - 2016**, and **2010 - 2014**). Store the returned floats into three separate variables.
