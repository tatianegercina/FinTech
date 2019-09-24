### 8. Student Do: The Big Short Part II (15 mins)

In this activity, students will now take the Short Position Dual Moving Average Crossover trading strategy they made in the previous student activity and now run a backtest to quantify the performance of their trading strategy.

**Files:**

* [the_big_short.ipynb](Activities/05-Stu_Backtesting/Unsolved/the_big_short_part_2.ipynb)

* [vnq.csv](Activities/05-Stu_Backtesting/Resources/vnq.csv)

**Instructions:** [README.md](Activities/05-Stu_Backtesting/README.md)

---

### 9. Instructor Do: The Big Short Part II Review (10 mins)

**File:** [the_big_short.ipynb](Activities/03-Backtesting/Solved/the_big_short_part_2.ipynb)

Open the solution file and review the following:

* The plot of the Short Position Dual Moving Average Crossover trading strategy showed that it was possible to *make* money from shorting VNQ (a real estate ETF) stock during the financial recession in 2008. Now, through backtesting the particular strategy, we will be able to see *how much* money can be made.

  ![short-dual-ma-crossover-plot2](Images/short-dual-ma-crossover-plot2.png)

* Because short positions involve selling shares and then buying them back later, the `share_size` should be a negative number rather than a positive number.

  ```python
  share_size = -500
  ```

* As a result of the negative `share_size` number, the following calculations show that an active share size position will be defined as -500, and that entry and exit positions in the short trading strategy will involve selling shares (a negative number) followed by purchasing shares (a positive number).

  ```python
  # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
  signals_df['Position'] = share_size * signals_df['Signal']

  # Find the points in time where a 500 share position is bought or sold
  signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
  ```

  ![short-dual-ma-backtesting-positions](Images/short-dual-ma-backtesting-positions.png)

* The calculations for portfolio holdings and show that as the stock price decreases, the value of the portfolio holdings increase (become less negative).

  ```python
  # Multiply share price by entry/exit positions and get the cumulatively sum
  signals_df['Portfolio Holdings'] = signals_df['Close'] * signals_df['Entry/Exit Position'].cumsum()
  ```

  ![short-portfolio-holdings](Images/short-portfolio-holdings.png)

* When shorting a stock, it is beneficial to sell the stock at a high price and buy (or cover as they say in the industry) the shares at a low price, resulting in a positive differential. This is why the portfolio cash increases when the algorithm shorts VNQ stock at a high and covers the shares at a low.

  ```python
  # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
  signals_df['Portfolio Cash'] = initial_capital - (signals_df['Close'] * signals_df['Entry/Exit Position']).cumsum()
  ```

  ![short-portfolio-cash](Images/short-portfolio-cash.png)

* After calculating the portfolio holdings and portfolio cash, calculating the total portfolio value is as simple as adding the portfolio holdings and portfolio cash together.

  ```python
  # Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
  signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
  ```

  ![short-portfolio-total](Images/short-portfolio-total.png)

* The portfolio daily returns can then be calculated using the `pct_change` function on the total portfolio value, while the portfolio cumulative returns can then be calculated using the resulting portfolio daily returns and the `cumprod` function.

  ```python
  # Calculate the portfolio daily returns
  signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

  # Calculate the cumulative returns
  signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
  ```

  ![short-portfolio-returns](Images/short-portfolio-returns.png)

* Finally, plotting the Short Position Dual Moving Average crossover trading strategy against its backtesting results show that the algorithm would have *made* money by shorting VNQ stock during the 2008 financial crisis and by approximately $6,500 on an initial capital allocation of $100,000. Specifically, the ending portfolio value for the algorithm was $106,587.2295 and results in cumulative returns of 6.5872%.

  ![short-dual-ma-crossover-plot3](Images/short-dual-ma-crossover-plot3.png)

  ![short-backtest-results](Images/short-backtest-results.png)
