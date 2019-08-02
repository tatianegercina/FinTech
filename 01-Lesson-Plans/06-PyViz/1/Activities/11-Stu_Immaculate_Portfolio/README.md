# Immaculate Portfolio

Your interview with REMAX is just three days away! Take a moment to review your current portfolio, and identify any remaining finishing touches that might be valuable to add. Take into consideration color schemes, types of plots used, and even the orientation of the plots (i.e. `inverted=True`).

Also, add in **scatter** and **area** plots to provide a glimpse into the quantitative numbers over time, as well as to show your understanding of more advanced, statistical based reporting paradigms.

Remember--this portfolio could be the make it or break it for this interview. Really make your portfolio stand out, and use your own personality and style to make the portfolio represanative of you and your analytic style/brand.

## Instructions

1. Review the pre-existing plots, and make sure all necessary aesthetic changes have been made.

  * Take into consideration labels

  * Format all numbers to appropriate decimal places

  * Add titles to every plot

2. Change the line color on plot `plot_2010_2014`.

3. Slice the `loans_data` DataFrame for Series **2017** and **2015 - 2016**. Store the output as `correlation_data`.

4. Run `reset_index` function against `correlation_data` to remove **State Code** index and make it available as a field. Hint: correlation_data.reset_index().

5. Create a **scatter** plot using the reset `correlation_data` DataFrame. This will create a correlation visualization outlining the effect of **2015 - 2016** data on **2017** data.

  * x = `2015 - 2016`

  * y = `2017`

  * c = `State Code`

6. Customize the **scatter** plot using the customization attributes or `opts` function to add finishing touches. Make sure to include a **colorbar**, as well as a **title** and **formatted** axes labels and ticks.

7. Using the code provided for `tri_state_loan_data`, create an **unstacked area** plot to view loan amount progression across time for the tri-state region. Use customization features to add finishing touches.

### Challenge

If you finish the activity early, circle back and consider changing the colors of your plots. Implement your own color scheme.

### Hint

Plot colors can be customized using the `opts(line_color=)` option. This will work for all plot types. Refer to the [documentation](https://hvplot.pyviz.org/user_guide/Customization.html) if additional assistance is needed.
