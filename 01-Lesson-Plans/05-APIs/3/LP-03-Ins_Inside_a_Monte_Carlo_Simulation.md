This activity introduces students to how a simple Monte Carlo simulation could look. In particular, this activity showcases a technical example of the Monte Carlo simulation stated in the previous activity.

**Files:**

* [coin_flip_simulation.ipynb](Activities/01-Ins_Inside_a_Monte_Carlo_Simulation/Solved/coin_flip_simulation.ipynb)

Walk through the solution and highlight the following:

* Monte Carlo simulations deal with predicting potential outcomes of a random process. Therefore, make sure to import the `random` class from the `numpy` library.

  ```
  # Import libraries and dependencies
  from numpy import random 
  import pandas as pd
  %matplotlib inline
  ``` 

* A coin is flipped 10 times for each trial or simulation. Therefore, there is a `50%` chance for the coin to land on heads and a `50%` chance for the coin to land on heads. That is why the `random` class from the Numpy library is used to generate integers `0` or `1`. If `0`, then the coin flip is considered heads, otherwise if `1`, the coin flip is considered tails.

* Return random integers from low (inclusive) to high (exclusive).