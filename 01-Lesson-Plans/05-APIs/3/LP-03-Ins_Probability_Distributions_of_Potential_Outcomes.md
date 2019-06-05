### 3. Instructor Demo: Probability Distribution of Potential Outcomes (0:10 mins)

Monte Carlo Simulations seek to explain the probability of potential outcomes of a randomly occuring event. Therefore, this activity provides a hands-on approach to introducing students to what a simple Monte Carlo simulation could look like and how to interpret the results.

**Files:**

* [coin_flip_simulation.ipynb](Activities/01-Ins_Inside_a_Monte_Carlo_Simulation/Solved/coin_flip_simulation.ipynb)

Walk through the solution and highlight the following:

* Monte Carlo simulations deal with predicting potential outcomes of a random process. Therefore, make sure to import the `random` class from the `numpy` library that allows for randomizing a particular code process.

  ```python
  # Import libraries and dependencies
  from numpy import random 
  import pandas as pd
  %matplotlib inline
  ``` 

* A coin is flipped 10 times for each trial or simulation. Therefore, there is a `50%` chance for the coin to land on heads and a `50%` chance for the coin to land on heads. The `random` class from the `numpy` library is used to randomly choose between the two outcomes: heads or tails. 

  ```python
  # Set number of simulations and coin flips
  num_simulations = 20
  num_flips = 10

  # Set a list acting as a coin
  coin = ["heads", "tails"]

  # Create an empty DataFrame to hold simulation results
  monte_carlo = pd.DataFrame()

  # Run n number of simulations
  for n in range(num_simulations):

      # Set an empty list to hold flip results
      flips = []

      # Flip the coin several times
      for i in range(num_flips):
          # Random int: 0 or 1
          coin_flip = random.choice(coin)

          # Append flip result to list
          flips.append(coin_flip)

      # Append column for each simulation and flip results
      monte_carlo[f"Simulation {n}"] = pd.Series(flips)

  # Print the DataFrame
  monte_carlo
  ```

  ![coin-flip-dataframe](Images/coin-flip-dataframe.png)

* The `randint` function from the `numpy` library returns random integers from low (inclusive) to high (exclusive). Therefore, the parameters `(0,2)` returns integers `0` or `1`.

* Simulations are run for every 10 flips of the coin. Therefore, the resulting heads-to-tail combinations for each simulation are saved.

  ```python
  # Set number of simulations and coin flips
  num_simulations = 10
  num_flips = 10

  # Set list
  tuples = []

  # Run n number of simulations
  for n in range(num_simulations):
    
      # Set variables
      num_heads = 0
      num_tails = 0
    
      # Print simulation 
      print(f"Simulation: {n+1}")
    
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
    
      # Set tuple
      tuple = (num_heads, num_tails)
    
      # Append tuple to tuples list
      tuples.append(tuple)

  # Print results
  print("-----------------------------------")    
  print(f"Results: {tuples}")
  ```

  ```
  Results: [(6, 4), (7, 3), (4, 6), (7, 3), (5, 5), (4, 6), (5, 5), (6, 4), (7, 3), (6, 4)]
  ```

* Leveraging the `value_counts` function by setting the results of the simulation to a Pandas DataFrame allows for counting the occurrences of the different heads-to-tails combinations.

  

* Dividing the frequency distribution of heads-to-tails combinations by the number of simulations performed shows the probability distribution of the potential outcomes for 10 simulations of flipping a coin 10 times. Notice the heads-to-tail combination of `(5,5)` is one of the least likely outcomes, yet we would expect it to be the highest probable outcome (50% heads, 50% tails) -- what gives? This is because a small number of simulations provides a limited number of data points that may or may not be reliable in the long-run.

  ![coin-flip-10-simulations](Images/coin-flip-10-simulations.png)

* Increasing the number of simulations to `100` produces a different probability distribution of potential head-to-tails combinations with `(5,5)` moving closer to being the most probable outcome as we would expect. 

  ![coin-flip-100-simulations](Images/coin-flip-100-simulations.png)

* Increasing the number of simulations to `1000` produces a (yet again) different probability distribution of potential head-to-tails combinations with `(5,5)` having the highest probability of occurring as should be expected. This is because a higher amount of simulations produce more reliable results in the long-run.

  ![coin-flip-1000-simulations](Images/coin-flip-1000-simulations.png)
