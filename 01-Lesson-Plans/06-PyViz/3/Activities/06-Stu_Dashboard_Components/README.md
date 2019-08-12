# Dashboard Components

It's time to get some experience working with PyViz objects in Panel. Use the knowledge and skills learned from the instructor demo to create a Plotly plot and convert it to a Panel **pane** object.

If time remains, complete the challenge activity by converting an hvPlot to a Panel **pane** figure.

## Instructions

1. Open the starter file, and use the provided data to create a Plotly plot.

2. Wrap the code to create the Plotly plot into a function.

3. Use the `panel.interact` function to render the plot with an interaction widget bar.

4. Use the `panel.pane.Plotly` function to convert the Plotly plot to a Panel Plotly figure.

5. Use the `panel.pprint` function to ensure the Plot has been converted to the appropriate **pane** type.

### Challenge

1. Use the provided data to create a hvPlot plot.

2. Use the `panel.panel` helper function to convert the hvPlot to the appropriate Panel component.

3. Use `panel.pprint` function to return the object type (i.e. either Pane or Panel).

### Hint

When unsure what `panel.pane` function to use, use the `panel.panel` helper function. The function will infer the appropriate Panel component type and also handle the conversion.
