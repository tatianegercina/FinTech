### 3. Instructor Demo: Probability Distribution of Potential Outcomes (0:10 mins)

Monte Carlo Simulations seek to explain the probability of potential outcomes for a randomly occuring event. Therefore, this activity provides a hands-on approach to introducing students to what a simple Monte Carlo simulation could look like and how to interpret the results.

**Files:**

* [coin_flip_simulation.ipynb](Activities/01-Ins_Inside_a_Monte_Carlo_Simulation/Solved/coin_flip_simulation.ipynb)

Walk through the solution and highlight the following:

* This solution represents a technical example to the Monto Carlo simulation use case presented in the previous activity (coin flip simulation). Therefore, the program flips a coin `10` times for `5` simulations to determine the frequency distribution of heads landed per simulation and the corresponding probability distribution of landing varying numbers (or ranges) of heads.

* Make sure to import the `random` class from the `numpy` library which allows for randomizing a particular code process.

  ```python
  # Import libraries and dependencies
  from numpy import random 
  import pandas as pd
  %matplotlib inline
  ``` 

* The `choice` function from the `random` class is used to randomly choose between the two outcomes of a coin: heads or tails. 

  ```python
  # Print simulation iteration
  print(f"Running Simulation {n+1}...")
    
  # Set an empty list to hold flip results
  flips = []

  # Flip the coin several times
  for i in range(num_flips):
      # Random int: 0 or 1
      coin_flip = random.choice(coin)
      
      # Print flip result
      print(f"  Flip {i+1}: {coin_flip}")

      # Append flip result to list
      flips.append(coin_flip)
  ```

  ![coin-flip-results](Images/coin-flip-results.png)

* The resulting heads and tails outputs for each simulation of `10` coin flips are saved as individual columns to a Pandas DataFrame.

  ```python
  # Append column for each simulation and flip results
  monte_carlo[f"Simulation {n}"] = pd.Series(flips)
  ```

  ![coin-flip-dataframe](Images/coin-flip-dataframe.png)

* The following is a holistic view of the example Monte Carlo simulation program -- see, it's not that bad!

  ```python
  # Set number of simulations and coin flips
  num_simulations = 5
  num_flips = 10

  # Set a list object acting as a coin: heads or tails
  coin = ["heads", "tails"]

  # Create an empty DataFrame to hold simulation results
  monte_carlo = pd.DataFrame()

  # Run n number of simulations
  for n in range(num_simulations):

      # Print simulation iteration
      print(f"Running Simulation {n+1}...")
    
      # Set an empty list to hold flip results
      flips = []

      # Flip the coin several times
      for i in range(num_flips):
          # Random int: 0 or 1
          coin_flip = random.choice(coin)
        
          # Print flip result
          print(f"  Flip {i+1}: {coin_flip}")

          # Append flip result to list
          flips.append(coin_flip)

      # Append column for each simulation and flip results
      monte_carlo[f"Simulation {n}"] = pd.Series(flips)

  # Print the DataFrame
  monte_carlo
  ```

* Leveraging the `value_counts` function by setting the results of the simulation to a Pandas DataFrame allows for counting the occurrences of the different heads-to-tails combinations.

  

* Dividing the frequency distribution of heads-to-tails combinations by the number of simulations performed shows the probability distribution of the potential outcomes for 10 simulations of flipping a coin 10 times. Notice the heads-to-tail combination of `(5,5)` is one of the least likely outcomes, yet we would expect it to be the highest probable outcome (50% heads, 50% tails) -- what gives? This is because a small number of simulations provides a limited number of data points that may or may not be reliable in the long-run.

  ![coin-flip-10-simulations](Images/coin-flip-10-simulations.png)

* Increasing the number of simulations to `100` produces a different probability distribution of potential head-to-tails combinations with `(5,5)` moving closer to being the most probable outcome as we would expect. 

  ![coin-flip-100-simulations](Images/coin-flip-100-simulations.png)

* Increasing the number of simulations to `1000` produces a (yet again) different probability distribution of potential head-to-tails combinations with `(5,5)` having the highest probability of occurring as should be expected. This is because a higher amount of simulations produce more reliable results in the long-run.

  ![coin-flip-1000-simulations](Images/coin-flip-1000-simulations.png)
