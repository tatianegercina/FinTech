# Monte Carlo Dashboard Web App

Congratulations! REMAX has gotten back to you regarding your application, and they've offered you a job! Your role, if you accept it, will be as a per diem (as needed) Business Intelligence Analyst. In this role, you will write programs and create visualizations for dashboards, as well as create reports for the executive team. REMAX will use your visualizations and reports to decide which markets and properties to get involved in.

Your first assignment on the job is to create a dashboard that will simulate the number of housing sales and/or foreclosures for a particular property type in the state of Connecticut. The technical lead has already developed the code. All you have to do is create the dashboard.

Create a Panel dashboard using the Monte Carlo simulation code and plots provided. Make sure to format the layout of the dashboard in a way that will promote insight and decision making. Then, deploy the dashboard as a web app.

## Instructions

1. Create a Panel `column` object and store it in a variable called `tab_1_columns`. Put variables `interactive_return_range` and `interactive_plot` into the column. 

   **Hint:** Add Markdown header text to indicate what each variable is.

2. Create a Panel `row` component and store it in `tab_2_row`. Store variables `simulated_ending_prices_plot` and `simulated_ending_prices_hist` in it.

3. Create a another Panel `column` component and store it as `tab_2_columns`. Add in `confidence_intervals` and `tab_2_row` to the column.

4. Create a Panel `tab` object and store it in a variable called `dashboard`. The first object in the tab should be `tab_1_columns`. The second object should be `tab_2_columns`. Give each of the objects in the `tab` a label.

   **Hint:** ```("Interactive Returns", tab_1_columns)```

5. Call the `servable` function using the `dashboard` object created in step 4.

6. Open up a terminal. Execute the `panel serve` command and pass the Jupyter Notebook as an argument. 

   **Hint:** Use the absolute path for file or relative path.

7. Use the URL provided in the logs from `panel serve` to open the dashboard as a web app!

8. Take the time to explore and appreciate your dashboard.
