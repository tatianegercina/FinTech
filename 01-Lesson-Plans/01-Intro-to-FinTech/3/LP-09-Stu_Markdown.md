### 9. Students Do: Git Welcome (15 mins)

In this activity, students visually enhance their README files for their GitHub repositories by adding additional markdown features.

**Instructions:**

* [README.md](Activities/03-Stu_Markdown/README.md)

### 10. Instructor Do: Git Welcome (5 mins)

Open the solution and explain the following:

* The `pandas` library comes built-in with certain matplotlib functions such as `plot`; however, the standalone `matplotlib` library provides the robustness required for altering a plot and setting the lower and upper bounds of a confidence interval. Therefore, make sure to import the `pyplot` class from the `matplotlib` library.

  ```python
  # Import libraries and dependencies
  import matplotlib.pyplot as plt
  from numpy import random
  import pandas as pd
  %matplotlib inline
  ```

* In order to know the range of data points that contain a specific percentage of all data points in the sample, generating a frequency distribution is a pre-requisite to defining a confidence interval.

  ![archery-probability-distribution](Images/archery-probability-distribution.png)

* Because the mean of a normal distribution is considered to be at the `50th` quantile, confidence intervals are usually set around the mean or `0.50` quantile. Therefore, a `95%` confidence interval would have quantiles set at `0.025` and `0.975` rather than something like `0.05` and `1.00`.

  ![archery-quantiles](Images/archery-quantiles.png)

* The `95%` confidence interval suggests that there is about a `95%` chance of the archer hitting the target `0-3` times out of `5` shots. Marking the confidence interval over the probability distribution histogram shows that the area of the bars within the lower and upper bounds approximate to about `95%`.

  ![archery-confidence-interval](Images/archery-confidence-interval.png)