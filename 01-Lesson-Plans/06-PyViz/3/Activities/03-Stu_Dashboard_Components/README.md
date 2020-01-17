# No Pane, No Gain

It's time to get some experience working with PyViz objects in Panel. Panes are the fundamental building block of any Panel Dashboard, and without Panes, there can be no dashboard, which means no value-added. Use the knowledge and skills learned from the instructor demo to convert a Plotly plot to a Panel **pane** object.

If time remains, complete the challenge activity by converting an hvPlot to a Panel object as well.

## Instructions

### Create Pane Using Interact Function

1. Open the starter file, and wrap the logic used to create `metro_prop_sale` in a function named `create_parallel_categories_plot`. `create_parallel_categories_plot` should accept an argument called `number_of_records`.

2. Have `create_parallel_categories_plot` function return `metro_prop_sale`.

3. Make a call to function `create_parallel_categories_plot`, and pass the integer 30 as the argument.

4. Use the `interact` function to create an interactive widget **pane**. Pass `create_parallel_categories_plot` function to `interact.` Set `number_of_records` to equal 30.

   **Hint:** interact(function_name, function_parameter=30).

### Create Pane Using panel.pane.Plotly Function

5. Manually convert the `metro_prop_sale` object to a **pane** using the `panel.pane.Plotly` function to convert.

   **Hint:** You will need to use the `create_parallel_categories_plot(30)` function. Store this as `plot_panel`.

6. Use the `panel.pprint` function to ensure the `plot_panel` object is a **pane**.

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
