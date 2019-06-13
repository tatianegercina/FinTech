### 5. Instructor Demo: Confidence Intervals (0:10 mins)

In this activity, students are introduced to confidence intervals, which in the context of Monte Carlo simulations, are value ranges of potential outcomes with a particular probability of occurring. Confidence intervals in combination with Monte Carlo simulations are useful when trying to predict the likelihood of an outcome falling within a specific range.

**Files:**

* [coin_flip_confidence_intervals.ipynb](Activities/03-Ins_Confidence_Intervals/Solved/coin_flip_confidence_intervals.ipynb)

Walk through the solution and highlight the following:

* Often times in statistics, there is a disconnect between the results of a sample dataset and attempting to imply the results of a sample to the overall population. For example, analyzing the average height of `20` students at a school to assume the average height of the entire population of students at the school would be an erroneous assumption. Therefore, confidence intervals suggest a range of values where there is a `X%` chance that the true expected value would lie within the specified range. In this case, a `95%` confidence interval may suggest that there is a `95%` chance that the true average height of students would range in height between `4` ft and `6 ft`, or in other words, the `95%` of the expected height of students should lie within the range of `4` ft and `6 ft`.

  ![confidence-interval-probability-distribution](Images/confidence-interval-probability-distribution.png)

* There is a tradeoff between the confidence, or likelihood of occurrence, of the expected result and the range of the upper and lower bounds of the confidence interval; the `X%` of the confidence interval suggests how wide or narrow the value range is. A `90%` confidence interval will have a narrower range, and therefore is less confident than a `95%` confidence interval with a larger range.

* In the context of Monte Carlo simulations, a confidence interval is a value range of a frequency distribution that contains a specific percentage of all potential outcomes. For example, a `90%` confidence interval would be a range of values of which `90%` of all potential outcomes of the Monte Carlo simulation are contained. Therefore, confidence intervals used with frequency distributions of Monte Carlo simulations calculate the range of potential outcomes and their probabilities of occurring. For example, one could analyze the frequency distribution of potential stock price trajectories and determine that "there is a `90%` chance that the stock price will be between `$10` and `$20` next week."

* In order to create a confidence interval, the upper and lower bounds of the confidence interval need to be set as a quantile or percentile range of the frequency distribution.

* A quantile is a measurement in which a frequency distribution is divided into equal groups, thus each group contain an equal fraction of the total sample. Often times, quantiles are expressed in `100` equal parts, otherwise known as *percentiles*. For example, a student in the 95th percentile of height for his school is as tall as or taller than `95%` of the students at the school.

* The `quantile` function for `pandas` DataFrames takes in a range of values that represent the lower and upper bounds of the confidence interval. The `numeric_only` parameter set to `True` ensures the quantiles are computed on numeric only values. In this case, quantiles of `0.05` and `0.95` are values where landing `2` heads is only greater than `5%` of all simulated outcomes whereas landing `8` heads is greater than `95%` of all simulated outcomes.

  ![coin-flip-quantile-function](Images/coin-flip-quantile-function.png)

* The `pyplot` class from the `matplotlib` library contains a `axvline` function that allows for setting upper and lower bounds to a confidence interval on a plot. The `color` parameter sets the color of the line.

  ![coin-flip-confidence-interval](Images/coin-flip-confidence-interval.png)

* The `90%` confidence interval calculated suggests that if a coin were to be flipped `10` times, there is a `90%` chance of the coin landing somewhere between `2-8` heads. This is because the confidence interval encapsulates `90%` of the frequency distribution (the area of the bars in the histogram) of simulated results.
