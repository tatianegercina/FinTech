### 4. Students Do: Free Throw Simulation (15 mins)

In this activity, students execute a Monte Carlo simulation to analyze the probability distribution of free throws made (out of 10 shots) for a player with a `70%` accuracy and determine the likelihood of the player making `9-10` free throws in a single session.

**Instructions:**

* [README.md](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/README.md)

**Files:**

* [free_throw_simulation.ipynb](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/Unsolved/free_throw_simulation.ipynb)

### 5. Instructor Do: Review Free Throw Simulation (5 mins)

**Files:**

* [free_throw_simulation.ipynb](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/Solved/free_throw_simulation.ipynb)

Open the solution and explain the following:

* The process of executing a Monte Carlo simulation remains similar even for a different use case (free throws vs. coin flips). At it's core, the basis of Monte Carlo simulations is iteration (running tests/simulations) and saving the results of a random process. Thus, expect the programmatic structure of `for` loops and potentially nested `for` loops.

  ```python
  # Set number of simulations and free throws
  num_simulations = 1000
  num_throws = 10

  # Set a list object acting as a throw: made basket or missed basket
  throw = ["made", "missed"]

  # Create an empty DataFrame to hold simulation results
  monte_carlo = pd.DataFrame()

  # Run n number of simulations
  for n in range(num_simulations):

      # Print simulation iteration
      print(f"Running Simulation {n+1}...")
    
      # Set an empty list to hold throw results
      throws = []

      # Shoot the ball `10` times
      for i in range(num_throws):
          # Randomly choose between `made` and `missed` with a `70%` chance to 
          # make the throw and a `30%` chance the throw is missed
          free_throw = random.choice(throw, p=[0.7, 0.3])
        
          # Print throw result
          print(f"  Throw {i+1}: {free_throw}")

          # Append throw result to list
          throws.append(free_throw)

      # Append column for each simulation and throw results
      monte_carlo[f"Simulation {n}"] = pd.Series(throws)

  # Print the DataFrame
  monte_carlo
  ```

* The `choice` function from the `random` class of the `numpy` library has a `p` parameter that allows for setting a non-uniform probability to events. In this case, a player has a `70%` chance of making a shot and consequently a `30%` chance of missing the shot. Therefore, the `choice` function below reflects this.

  ```python
  # Set a list object acting as a throw: made basket or missed basket
  throw = ["made", "missed"]
  # Randomly choose between `made` and `missed` with a `70%` chance to 
  # make the throw and a `30%` chance the throw is missed
  free_throw = random.choice(throw, p=[0.7, 0.3])
  ```

* Because the random process has non-uniform probability (`70%` chance to make a shot and `30%` chance to miss a shot) the corresponding frequency and probability distributions of made free throws show that a majority of the distribution lies within the `7, 8, 9, and 10` range, while the rest of the distribution is spread out within the `0, 1, 2, 3, 4, 5, 6`. Unlike the bell-curve of a normal distribution, this is called a skewed (in this case left-scewed) distribution.

  ![free-throws-frequency-distribution](Images/free-throws-frequency-distribution.png)

  ![free-throws-probability-distribution](Images/free-throws-probability-distribution.png)

