# Picture Perfect

It's time to put some finishing touches to your masterpiece to make it picture perfect. Using the customization attributes and options demonstrated by the instructor, curate your visualizations. Make sure to assess each plot for opportunities of aesthetic improvement.

## Instructions

1. Open the [starter file](Unsolved/Core/picture_perfect.ipynb), and use the `rot` function to make the x axis more legible.

2. Use the  `opts(yformatter=)` option to format y axis labels.

3. Add a title to all of your visualizations.

4. Invert any bar chart visualizations using dates so that data over time is seen horizontally rather than vertically. Hint: date values will be on the y axis.

5. Increase the height or width of any plots rendered too small.

If you complete the activity early, continue on to the optional challenge section.

### Challenge

hvPlot also offers color customization. Follow the below steps to add additional customizations.

1. Change the background color of a plot using `opts(bgcolor=)` option.

2. Use the `opts(hover_line_color=)` option to change the color of a line or bar when hovering.

3. Change the color of a line chart or the outline of each bar in a bar chart using the `opts(line_color=)` option.

### Hint

The `opts` function can be used customize composite plot (i.e `(plot_state_avgs * plot_2015_2016 * plot_2010_2014).opts(width=900)`)

The [hvPlot documentation](https://hvplot.pyviz.org/user_guide/Customization.html) can be referenced for additional details regarding options and how they work.
