### 9. Instructor Demo: Beta (10 mins)

**Files:**

* [beta.py](Activities/09-Beta/Solved/beta.py)

Walk through the solution and explain the following:

* What is covariance?

  > Covariance is a measure of the directional relationship between two variables. For example, covariances between two financial assets such as stock returns would imply that both stock returns would move together with a positive covariance and move inversely with a negative covariance.

  ![covariance.png](Images/covariance.png)

* What is variance?

  > Variance is a measurement of the spread between each number in a data set compares to the overall mean. It is calculated by taking the differences between each number in the data set and the mean, squaring the differences and dividing the sum of the squares by the number of values in the set.

  ![variance.png](Images/variance.png)

* What is the difference between covariance and variance?

  > Covariance refers to the measure of the directional relationship between two random variables while variance refers to the spread of a data set around its mean value.

* What is the difference between covariance and correlation?

  > Covariance is a measure of correlation. Correlation describes the directional relationship between two variables in a unit-free manner, while covariance describes the directional relationship between two variables with consideration for the type of data used (in this case, daily return values).

* What is beta?

  > Beta is the measure of the volatility of an individual stock in comparison to the volatility of the entire market.

  ![beta.png](Images/beta.png)

* What is the difference between beta and correlation?

  > Beta tries to measures the effect of one variable impacting the other variable. Correlations measure the possible frequency of similarly directional movements without considerations of cause and effect. Beta is the slope of the two variables. Correlation is the strength of that linear relationship.

* It's often a good practice to plot the progression of beta values for a stock over time using rolling windows to see it's historical volatility relative to the market.

  ![rolling-beta.png](Images/rolling-beta.png)

