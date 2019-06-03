### 3. Instructor Demo: Inside a Monte Carlo Simulation (0:05 mins)

This activity introduces students to how a simple Monte Carlo simulation could look. In particular, this activity showcases a technical example of the Monte Carlo simulation stated in the previous activity.

**Files:**

* [coin_flip_simulation.ipynb](Activities/01-Ins_Inside_a_Monte_Carlo_Simulation/Solved/coin_flip_simulation.ipynb)

Walk through the solution and highlight the following:

* Monte Carlo simulations deal with predicting potential outcomes of a random process. Therefore, make sure to import the `random` class from the `numpy` library.

  ```python
  # Import libraries and dependencies
  from numpy import random 
  import pandas as pd
  %matplotlib inline
  ``` 

* A coin is flipped 10 times for each trial or simulation. Therefore, there is a `50%` chance for the coin to land on heads and a `50%` chance for the coin to land on heads. That is why the `random` class from the Numpy library is used to generate integers of `0` or `1`. If `0`, then the coin flip is considered heads, otherwise if `1`, the coin flip is considered tails.

  ```python
  # Flip a coin: heads or tails
  for i in range(num_flips):
      # Random int: 0 or 1
      coin_flip = random.randint(0,2)

      # Logic to determine head or tails
      if coin_flip == 0:
          result = "heads"
          num_heads+=1
      elif coin_flip == 1:
          result = "tails"
          num_tails+=1
        
      # Print trial
      print(f"  Flip {i+1}: {result}")

  # Print number of heads and tails for the simulation
  print("  -----------------------------------")
  print(f"  Number of Heads: {num_heads}")
  print(f"  Number of Tails: {num_tails}")
  ```

  ```
  Simulation: 1
  Flip 1: tails
  Flip 2: heads
  Flip 3: tails
  Flip 4: tails
  Flip 5: heads
  Flip 6: heads
  Flip 7: heads
  Flip 8: heads
  Flip 9: tails
  Flip 10: heads
  -----------------------------------
  Number of Heads: 6
  Number of Tails: 4
  ```

* The `randint` function from the `numpy` library returns random integers from low (inclusive) to high (exclusive). Therefore, the parameters `(0,2)` returns integers `0` or `1`.

* 