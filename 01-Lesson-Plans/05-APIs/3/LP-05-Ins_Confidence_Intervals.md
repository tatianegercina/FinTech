### 5. Instructor Demo: Confidence Intervals (0:10 mins)

In this activity, students are introduced to confidence intervals, which in the context of Monte Carlo simulations, are value ranges of potential outcomes with a particular probability of occurring. Confidence intervals in combination with Monte Carlo simulations are useful when trying to predict the likelihood of an outcome falling within a specific range.

**Files:**

* [coin_flip_confidence_intervals.ipynb](Activities/03-Ins_Confidence_Intervals/Solved/coin_flip_confidence_intervals.ipynb)

Walk through the solution and highlight the following:

* In the context of general statistics, a confidence interval is a value range of a frequency distribution that contains a specific percentage of the overall sample (or data set). For example, a `95%` confidence interval would be a range of values of which `95%` of all data points in the sample are contained. The image below expresses the x-axis as the range of values that deviate from the mean (standard deviation).

  ![confidence-interval-probability-distribution](Images/confidence-interval-probability-distribution.png)

* In the context of Monte Carlo simulations, a confidence interval is a value range of a frequency distribution that contains a specific percentage of all potential outcomes. For example, a `90%` confidence interval would be a range of values of which `90%` of all potential outcomes of the Monte Carlo simulation are contained. Therefore, confidence intervals used with frequency distributions of Monte Carlo simulations calculate the range of potential outcomes and their probabilities of occurring. For example, one could analyze the frequency distribution of potential stock price trajectories and determine that "there is a `90%` chance that the stock price will be between `$10` and `$20` next week."

* In order to create a confidence interval, the upper and lower bounds of the confidence interval need to be set as a quantile or percentile range of the frequency distribution.

* A quantile is a measurement in which a frequency distribution is divided into equal groups, thus each group contain an equal fraction of the total sample. Often times, quantiles are expressed in `100` equal parts, otherwise known as *percentiles*. For example, a student in the 95th percentile of height for his school is as tall as or taller than `95%` of the students at the school.

* The `quantile` function for `pandas` DataFrames takes in a range of values that represent the lower and upper bounds of the confidence interval. The `numeric_only` parameter set to `True` ensures the quantiles are computed on numeric only values. In this case, quantiles of `0.05` and `0.95` are values where landing `2` heads is only greater than `5%` of all simulated outcomes whereas landing `8` heads is greater than `95%` of all simulated outcomes.

  ![coin-flip-quantile-function](Images/coin-flip-quantile-function.png)

* The `pyplot` class from the `matplotlib` library contains a `axvline` function that allows for setting upper and lower bounds to a confidence interval on a plot. The `color` parameter sets the color of the line.

  ![coin-flip-confidence-interval](Images/coin-flip-confidence-interval.png)

* The `90%` confidence interval calculated suggests that if a coin were to be flipped `10` times, there is a `90%` chance of the coin landing somewhere between `2-8` heads. This is because the confidence interval encapsulates `90%` of the frequency distribution (the area of the bars in the histogram) of simulated results.
