### 16. Instructor Do: Sharpe Ratios (5 mins)

**Files:**

* [sharpe_ratios.py](Activities/16-Ins_Sharpe_Ratios/Solved/sharpe_ratios.py)

Now that students have been taught how to assess and identify risk and investment performance, they are now prepared to learn how to adjust trade patterns to adjust for risk-reward.

Open the 4.2 slides, and provide an overview of what `sharpe ratios` are and how they are calculated.

* Sharpe ratios are used to help compare rate of return for an investment with its risk. Sharpe ratios shed light on the potential of profits even with risk involved.

* Sharpe ratios measure the excess return for each deviation. This will identify, in the wake of risk, how much profit is left to be gained.

* Sharpe ratios are calculated by subtracting the `return of portfolio` from the investment's `risk-free rate`. The difference is than divided by the `standard deviation`.

  Sharpe Ratios = <img src="https://latex.codecogs.com/gif.latex?\frac{R_{p}-R_{f}}{\sigma_{p}}$" title="\frac{R_{p}-R_{f}}{\sigma_{p}}$" />

Open the solution, and live code how to calculate and plot sharpe ratios:

* Sharpe ratios are commonly used to indicate whether or not an investment is a good decision. While standard deviation illustrates how far an investment has deviated from its average, sharpe ratios uses standard deviation to illustrate the relationship between standard deviation and risk-reward. Sharpe ratios enables investors to judge whether or not an investment is a good decision. Sharpe ratios adjust for risk, making them a valuable indicator of asset performance.

  ```python
  # Calculate Sharpe Ratio
  sharpe_ratios = (all_portfolios_returns.mean() * 252) / (all_portfolios_returns.std() * np.sqrt(252))
  sharpe_ratios
  ```

  ![sharpe_ratios.png](Images/sharpe_ratios.png)

* The ratio of return-to-risk can be used to determine which stocks and/or portfolios have out-done the others. The higher the `sharpe ratio`, the better the investment. The `plot` function can be used to visually compare `sharpe ratios`.

  ```python
  # Plot sharpe ratios
  sharpe_ratios.plot(kind="bar", title="Sharpe Ratios")
  ```

  ![sharpe_ratios_plot.png](Images/sharpe_ratios_plot.png)
