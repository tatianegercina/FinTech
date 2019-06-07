### 6. Students Do: Archery Target Hits (15 mins)

In this activity, students execute a Monte Carlo simulation to analyze the probability distribution of potential hits (out of `5` shots) of a target for a beginner archer with a `20%` accuracy and determine the range of hits for the archer that has a `95%` chance of happening in a single session.

**Instructions:**

* [README.md](Activities/04-Stu_Confidence_Intervals/README.md)

**Files:**

* [archery_target_hits.ipynb](Activities/04-Stu_Confidence_Intervals/Unsolved/archery_target_hits.ipynb)

### 7. Instructor Do: Review Free Throw Simulation (5 mins)

**Files:**

* [archery_target_hits.ipynb](Activities/04-Stu_Confidence_Intervals/Solved/archery_target_hits.ipynb)

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

  ![archery-frequency-distribution](Images/archery-frequency-distribution.png)