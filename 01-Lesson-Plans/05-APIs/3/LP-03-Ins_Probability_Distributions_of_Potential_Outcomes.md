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

* Leveraging the `value_counts` function via the Pandas DataFrame allows for counting the occurrences of the different heads-to-tails combinations of every simulation.

  ![coin-flip-value-counts](Images/coin-flip-value-counts.png)

* Performing a `value_counts` function on every column (or simulation) in the DataFrame and specifying the `heads` key of the returned Series object produces a list of landed heads per simulation.

  ![coin-flip-value-counts-key](Images/coin-flip-value-counts-key.png)

* Creating a DataFrame from the list of heads per simulation and using the `plot` function with the `kind` parameter set to `hist` produces a histogram that showcases the frequency distribution of landed heads.

* Remember that a histogram is not a bar graph; frequency values in histogram bars are determined by the area (length * width) of the bar, not by the height of the bar. This is because histograms deal with the frequency of values associated with *ranges* of numbers or *bins* rather than a single datapoint. The following histogram shows one can expect approximately `2` occurrences out of `5` simulations where total heads flipped were between `4-5`.

  ![coin-flip-5-simulations](Images/coin-flip-5-simulations.png)

* Without manually setting the `bins` parameter for a histogram, the plot defaults to `10` bars between the minimum and maximum datapoints provided. Sometimes this creates ranges deviating from what is being simulated. Therefore manually setting the `bins` parameter ensures that the histogram properly represents the edges of each bin, in this case bin edges of `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`. 

  ![coin-flip-5-simulations-bins-off](Images/coin-flip-5-simulations-bins-off.png)

  ![coin-flip-5-simulations-bins](Images/coin-flip-5-simulations-bins.png)

* Setting the `density` parameter to `True` for the histogram plot function creates a frequency density histogram which can be used to showcase the probability distribution of potential outcomes. In this case, it can be interpreted that for an experiment of `5` simulations of `10` coin flips, we can expect approx `40%` of our simulations to land `4` heads out of `10` coin flips.

  ![coin-flip-density-histogram](Images/coin-flip-density-histogram.png)

* Unfortunately, the probability distribution of potential outcomes generated for a small number of simulations should not be trusted. This is because a small number of simulations cannot test every possible outcome and therefore may generate biased results that are not indicative of the true nature of the random process in the long-term. Therefore, increasing the simulation count to `100` provides a more reliable and continuous range of probable outcomes.

  ![coin-flip-100-simulations](Images/coin-flip-100-simulations.png)

*   