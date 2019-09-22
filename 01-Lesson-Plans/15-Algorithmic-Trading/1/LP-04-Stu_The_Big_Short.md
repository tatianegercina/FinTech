### 5. Student Do: The Big Short (15 mins)

In this activity, students will take what they've learned about generating trading signals and implementing a corresponding trading strategy, and instead now perform the inverse: create a trading strategy that profits off of price declines by shorting (selling) and covering (buying) the stock.

**Files:**

* [the_big_short.ipynb](Activities/03-Stu_Trading_Signals/Unsolved/the_big_short.ipynb)

* [vnq.csv](Activities/03-Stu_Trading_Signals/Resources/vnq.csv)

**Instructions:** [README.md](Activities/03-Stu_Trading_Signals/README.md)

---

### 6. Instructor Do: The Big Short Review (10 mins)

**File:** [the_big_short.ipynb](Activities/03-Stu_Trading_Signals/Solved/the_big_short.ipynb)

Open the solution file and review the following:

* Be mindful when dealing with time series data, it is sometimes important to view the entirety of the data in the DataFrame. Therefore, using the pandas `set_option` function allows users to extend the maximum rows and columns a Pandas DataFrame will display.

  ```python
  pd.set_option('display.max_rows', 2000)
  pd.set_option('display.max_columns', 2000)
  pd.set_option('display.width', 1000)
  ```

* Generating a short position dual moving average crossover trading signal involves calculating a short window rolling moving average and a long window rolling moving average of closing prices, defining logic for an active trade signal as 1 when the short MA crosses under the long MA and 0 when the short MA crosses above the long MA, and calculating the points at which a entry or exit position should be made as 1 or -1.

  ![short-dual-ma-crossover](Images/short-dual-ma-crossover.png)

* Similar to a long position dual moving average crossover trading signal, the `where` function defines the logic for when a short moving average is less than the long moving average, issue a value of 1; when a short moving average is greater than the long moving average, issue a value of 0. Values are assigned to data points starting from an offset equal to the length of the short moving average window, as moving average calculations will be null prior to that point (not enough data points to perform the rolling mean calculation).

  ```python
  signals_df['Signal'][short_window:] = np.where(signals_df['SMA50'][short_window:] < signals_df['SMA100'][short_window:], 1.0, 0.0)
  ```

* The `diff` function calculates the difference in active vs. non-active trading periods suggested by the short position trading signal, 1 or 0. Therefore, values defined for specific entry and exit points become 1 or -1.

  ![short-entry.png](Images/short-entry.png)

  ![short-exit.png](Images/short-exit.png)

* Plotting the closing prices of VNQ, a 50-day moving average, and a 100-day moving average overlaid with marker symbols indicating short position entry and exit trades shows that if you had an algorithm utilizing a short position dual moving average crossover strategy during the 2008 recession, you would have *made* money rather than *lose* money like most other investors during tha time.

  ![short-dual-ma-crossover-plot](Images/short-dual-ma-crossover-plot.png)
