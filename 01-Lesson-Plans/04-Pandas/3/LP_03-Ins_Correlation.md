### 2. Instructor Do: Correlation (10 mins)

This activity introduces the student to the concept of correlation, or the positive or negative relationship between two variables. Two datasets have been chosen to showcase the example of correlation: ice cream sales and drowning incidents.

**Files:**

* [correlation.ipynb](Activities/03-Ins_Correlation/Solved/correlation.ipynb)

Walk through the solution and highlight the following:

* What is correlation?

  > Correlation is the measure of either a positive, negative, or netural (random) relationship between two variables. For example, there is often a positive correlation with height vs. weight (as you grow in height you tend to weigh more).

* When comparing the line trend of ice cream sales to drowning incidents, it is much harder to detect a relationship between the two. Therefore, use a scatterplot and set the `x` and `y` axis to the corresponding DataFrame columns. With a scatterplot, the relationship becomes much more apparent.

  ![line-chart](Images/line-chart.png)
  ![scatterplot](Images/scatterplot.png)

* Use the `corr` function to calculate and output a matrix of correlation values for each column-to-column pair of a DataFrame. Correlation values range from `-1` to `0` to `+1`, where `-1` indicates a negative relationship (variables move inversely to one another), `0` indicates a neutral relationship (variables have no relationship and move randomly), and `+1` indicates a positive relationship (variables move in tandem with one another). 

  ![correlation.png](Images/correlation.png)

* Remember that correlation does not imply causation! Although `Ice Cream Sales` has a positive correlation of `0.819404` with `Drowning Incidents` it does not mean that buying more ice cream causes people to drown. It merely states that there is a positive relationship between the numbers. Chances are, there is another factor at play which makes these two variables so positively correlated. One guess could be as temperatures increase (summer months) people tend to eat more ice cream and go swimming. 

* In order to determine causation, regression analysis should be used where the premise is to find out how x predicts y.  