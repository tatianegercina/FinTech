# Trading Log

In this activity, Karen -- an equity trader -- has been tracking her profits/losses over the course of the last 30 days. She wants to make it simpler for herself to quickly analyze her ongoing performance as she continues to log her profits/losses every day. Understanding her profits/losses everyday will allow Karen to begin evaluating her performance for all trades at monthly, weekly, and daily, as well as across time. Help Karen create a program to analyze her results.

## Instructions

Using the [starter-file](Unsolved/trading_log.py) provided, walk through the following steps:

* Create a for loop over the `trading_pnl` list object and cumulatively sum up the `total` profits/losses and the `count` of actual trading days.

* Use an if-else statement to calculate the `maximum` and `minimum` profit/loss values. In other words, find the numerical value of the best and worst trading day.

* Create additional lists `profitable_days` and `unprofitable_days` and use if-else statements to group daily trading values into each corresponding list.

* Determine the following...

  * Number of total trading days

  * Total profits/losses

  * Daily average profit/loss

  * Worst loss

  * Best Gain

  * Number of profitable days

  * Number of unprofitable days

  * Percentage of profitable days

  * Percentage of unprofitable days

  * Print the values of only profitable days

  * Print the values of only unprofitable days

## Hints

Use the below formulas:

* Number of total trading days = Length of `trading_pnl`

* Profit = `trading_pnl` value is greater than 0

* Loss = `trading_pnl` value is less than 0

* Total Profits/Losses = Sum of `trading_pnl`

* Daily Average Profit/Loss = Total Profits/Losses divided by number of total trading days

* Worst Loss = Smallest number in `unprofitable_days`

* Best Gain = Largest number in `profitable_days`

* Percentage of profitable days = Number of profitable days divided by number of total trading days, multiplied by 100

Your results should look similar to the following:

```
---------Summary Statistics----------
Number of Total Days: 20
Number of Profitable Days: 13
Number of Unprofitable Days: 7
Percentage of Profitable Days: 65.0%
Percentage of Unprofitable Days: 35.0%
-------------------------------------
Profitable Days: [352, 252, 354, 56, 123, 254, 325, 47, 321, 123, 133, 613, 232]
Unprofitable Days: [-224, -544, -650, -43, -123, -151, -311]
-------------------------------------
Total Profits/Losses: 1139
Daily Average: 56.95
Worst Loss: -650
Best Gain: 613
```

Refer to this [article](https://www.investopedia.com/terms/p/plstatement.asp) for more information regarding profit/loss statements.
