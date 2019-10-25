### 11. Students Do: Evaluations (15 mins)

Students complete a MSMD activity where they create a function to calculate portfolio evaluation metrics for their backtesting data. The activity is aimed to get students thinking about how the calculation of evaluation metrics can be incorporated into algorithmic training.

**Instructions:** [README.md](Activities/07-Stu_Evaluations/README.md)

**Files:** [trade_evaluations.ipynb](Activities/07-Stu_Evaluations/Unsolved/trade_evaluations.ipynb)

---

### 12. Instructor Do: Evaluations Activity Review (10 mins)

**Files:**

* [trade_evaluations.ipynb](Activities/07-Stu_Evaluations/Solved/trade_evaluations.ipynb)

Open the solution, and explain the following:

* Evaluation metrics should be used to gauge algorithm performance. Commonly used evaluation metrics include cumulative returns, annualized returns, annual volatility, Sharpe ratio, and Sortino ratio.

  ![eval_metrics_function.png](Images/eval_metrics_function.png)

* Remind students that even though algorithms can perform more effectively and efficiently than humans (without emotional or mental fatigue), algorithms still need to be evaluated for performance. This will ensure the algorithm is trading with the most optimal configurations.

* Explain that the common practice is to have the algorithm calculate and monitor evaluation metrics to help making decisions regarding when to buy and sell. This removes the need for manual calculations, and it also provides the opportunity for the evaluation metrics to be tracked in real time as stock prices fluctuate and trades are executed.

* Per-trade evaluation metrics can also be calculated by iterating over the DataFrame containing backtested signal data and calculating the difference between the exit portfolio holding and the entry portfolio holding values.

  ![per-trade-evaluation-code](Images/per-trade-evaluation-code.png)

  ![per-trade-evaluation-dataframe](Images/per-trade-evaluation-dataframe.png)

Dedicate the remaining time to student questions. Encourage students to ask any questions regarding the different evaluation metrics, how they're used, or why they are used.

* Pull up the [evaluations calculation guide](../Supplemental/EvaluationsCalculationGuide.md) as an anchor for the question session. This will give students the ability to call out specific aspects of the metrics that may be confusing or unclear.

Ask for any remaining questions before moving on.
