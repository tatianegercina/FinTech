### 5. Instructor Demo: Confidence Intervals (0:10 mins)

In this activity, students are introduced to confidence intervals, which are value ranges of a frequency distribution that encapsulate a portion (or all) of the overall sample.  Therefore, in the context of Monte Carlo simulations, confidence intervals determine the range of potential outcomes and their probability of occurring.

**Files:**

* [coin_flip_confidence_interval.ipynb](Activities/03-Ins_Confidence_interval/Solved/coin_flip_confidence_interval.ipynb)

Walk through the solution and highlight the following:

* A confidence interval is a value range of a frequency distribution that contains a specific percentage of the overall sample (or dataset). For example, a `90%` confidence interval would be a range of values of which `90%` of all datapoints in the sample is contained.

* Confidence intervals with Monte Carlo simulations are useful in that they determine the range of potential outcomes and their probabilites of occurring.

* In order to create a confidence interval, the upper and lower bounds of the confidence interval need to be set as a quantile or percentile range of the frequency distribution.

* A quantile is a measurement in which a frequency distribution is divided into equal groups, thus each group contain an equal fraction of the total sample. Often times, quantiles are expressed in `100` equal parts, otherwise known as *percentiles*. For example, a student in the 95th percentile of height for his school is as tall as or taller than `95%` of students at the school.

* The `quantile` function for `pandas` DataFrames takes in a range of values that represent the lower and upper bounds of the confidence interval. The `numeric_only` parameter set to `True` ensures the quantiles are computed on numeric only values.

  ![coin-flip-quantile-function](Images/coin-flip-quantile-function.png)

* The `pyplot` class from the `matplotlib` library contains a `axvline` function that allows for setting upper and lower bounds to a confidence interval on a plot. The `color` parameter sets the color of the line.

  ![coin-flip-confidence-interval](Images/coin-flip-confidence-interval.png)