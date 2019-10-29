### 11. Students Do: The Big Short Part III (15 mins)

Now that students have developed a Short Dual Moving Average trading strategy and backtested their strategy against historical VNQ prices, students can now calculate the portfolio and trade evaluation metrics to ascertain the performance of their short strategy.

**Instructions:** [README.md](Activities/07-Stu_Evaluations/README.md)

**Files:** [the_big_short_part_3.ipynb](Activities/07-Stu_Evaluations/Unsolved/the_big_short_part_3.ipynb)

---

### 12. Instructor Do: The Big Short Part III Review (10 mins)

**Files:**

* [the_big_short_part_3.ipynb](Activities/07-Stu_Evaluations/Solved/the_big_short_part_3.ipynb)

Open the solution, and explain the following:

* Portfolio evaluation metrics should be used to gauge algorithm performance. Commonly used metrics include cumulative returns, annualized returns, annual volatility, Sharpe ratio, and Sortino ratio.

  ![portfolio-evaluation-metrics.png](Images/portfolio-evaluation-metrics.png)

* Remind students that even though algorithms can perform more effectively and efficiently than humans (without emotional or mental fatigue), algorithms still need to be evaluated for performance. This will ensure the algorithm is trading with the most optimal configurations.

* Explain that the common practice is to have the algorithm calculate and monitor evaluation metrics to help making decisions regarding when to buy and sell. This removes the need for manual calculations, and it also provides the opportunity for the evaluation metrics to be tracked in real time as stock prices fluctuate and trades are executed.

* Per-trade evaluation metrics show a more granular approach to assessing the performance of the overall portfolio. Previously, it was shown that the short strategy increased the initial capital allocation from $100,000 to $106,587.2295; by looking at the per-trade evaluation metrics, we can see how each trade propelled the total portfolio value to the ending value of $106,587.2295.

  ![per-trade-evaluation-code](Images/per-trade-evaluation-code2.png)

  ![per-trade-evaluation-dataframe](Images/per-trade-evaluation-dataframe2.png)

Dedicate the remaining time to student questions. Encourage students to ask any questions regarding the different evaluation metrics, how they're used, or why they are used.

* Pull up the [evaluations calculation guide](../Supplemental/EvaluationsCalculationGuide.md) as an anchor for the question session. This will give students the ability to call out specific aspects of the metrics that may be confusing or unclear.

Ask for any remaining questions before moving on.
