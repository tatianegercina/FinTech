# NPV - Net Present Value

* What is NPV?

  > NPV or Net Present Value gets its name from the fact that it compares the initial investment of a project to the sum of all the present values of the subsequent projected cash flows. Therefore, positive NPV values indicate a project that is profitable and should be considered; negative NPV values indicate a project that is not profitable and should not be considered.

In this activity, you will conduct financial analysis on three potential company projects that are categorized as conservative, neutral, and aggressive. Each scenario requires an initial investment to undertake the project in order to generate the resulting cash flows for the following 4 years.

Use the NPV function from the NumPy library to calculate the NPV values for each project scenario, and determine the scenario that has the highest NPV value, 
or the project that is the optimal choice.

## Instructions

* Using the [starter-file](Activities/06-Stu_Imports/Unsolved/net_present_value.py) provided, complete the following steps.

  1. Import the NumPy library

  2. Call the NumPy NPV function for each of the project scenarios. 

  3. Assign the return values to a corresponding scenario key in a `npv_dict` dictionary.

  4. Print out the project scenario that holds the max NPV value from the `npv_dict` dictionary.

* Your results should look similar to the following:

  ```
  {'conservative': 267.94617853971704, 'neutral': 401.91926780957544, 'aggressive': 285.8923570794341}
  The optimal project scenario to undertake is 'neutral' with a NPV of 401.91926780957544
  ```

## Challenge

* Use a for loop and an if-else conditional to calculate the max NPV value and associated key from the `npv_dict` dictionary. Doing so avoids the need to manually choose the project scenario that has the max NPV value.

* Your results should look similar to the following:

  ```
  conservative 267.94617853971704
  neutral 401.91926780957544
  aggressive 285.8923570794341
  ---------------------------------------------------------
  The project scenario with the max NPV value is 'neutral' with a NPV of 401.91926780957544
  ```

## Hints

* Remember that NPV is the difference between the sum of all present values of future cash flows minus the absolute value of the initial investment!