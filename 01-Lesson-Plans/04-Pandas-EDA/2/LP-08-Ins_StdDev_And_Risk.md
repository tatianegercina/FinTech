### 8. Instructor Do: Standard Deviation & Risk (10 mins)

* **Files:**

  * [Lesson 4.2 slides](LINK TO GOOGLE SHEETS!)
  * [08-Ins_StdDev_And_Risk.ipynb](Activities/08-Ins_StdDev_And_Risk/Solved/08-Ins_StdDev_And_Risk.ipynb)

This lesson will introduce students to some basic descriptive statistics than are commonly used on finance to assess risk. Open the lesson slide deck and introduce students to mean, mode, median, and standard deviation by highlighting the following:

* Descriptive statistics are used to describe and understand the features of a specific dataset set by giving short summaries about the sample and measures of the data. Together with simple graphics analysis, they form the basis of virtually every quantitative analysis of data.

* Descriptive statistics are split into measures of central tendency and measures of variability.

* The measurements of central tendency are the mean, mode and median.

  * The **mean**, also known as **average** or **arithmetic mean**, is the central value of a discrete set of numbers, it's calculated by the sum of the value dived by the number o values. Show the mean formula to the class.

    ![Mean formula](Images/mean_formula.png)

  * The **mode** is the most frequently occurring number value among a discrete set of numbers, it's found by collecting and organizing data in order to count the frequency of each result.

  * The **median** sometimes could have a similar value as the mean, however it's calculation is different, this central tendency measure is the middle number in a sorted list of numbers.

* The measures of variability are the variance and the standard deviation.

  * The **variance** measures how spread are numbers in a dataset. It's used to understand how far each number in the dataset is from mean. The variance is calculated is calculated by taking the differences between each number in the dataset and the mean, the differences are squared to make them positive and the sum of the squares is divided by the number of values in the set. Show the variance formula to the class.

    ![Variance formula](Images/variance_formula.png)

  * The **standard deviation** is a measure of variability and is used on finance to assess risk. It's calculated as the square root of variance by determining the variation between each data point relative to the mean.

    ![Standard deviation formula](Images/std_dev_formula.png)

Emphasize that the basic definition of risk is the chance that an investment’s actual return will be different from what was expected; standard deviation is one common way to measure risk, thant's why it's important to understand this concept.

* The tradeoff between risk and return could be analyzed as the balance between the lowest possible risk and the highest possible return, in terms of standard deviation, a higher standard deviation means a higher level of risk, as well as a higher potential return, and vice versa as can be seen on the image bellow.
  ![Standard Deviation (Risk) and Return Tradeoff](Images/risk_return_tradeoff.png)

Explain to the class that despite every formula can be coded as a python function we are going to use the built-in stats formulas of Pandas.

Now it's time to show descriptive stats and risk analysis in action using Pandas, open the [08-Ins_StdDev_And_Risk.ipynb](Activities/08-Ins_StdDev_And_Risk/Solved/08-Ins_StdDev_And_Risk.ipynb) notebook and explain the following:

* The dataset that is going to be analyzed contains stock prices from top tech companies along 2018.

  ![Raw data from tech companies stock prices](Images/tech_stocks_raw_dataframe.png)

* In order to assess risk and calculate descriptive statistics, the `date` column should be defined as the index.

  ![Setting date column as index](Images/tech_stocks_date_index.png)

* The first step towards analyzing risk will be to visually understand the risk using a box plot. On this plot it can be seen that Amazon (AMZN) it's the riskier stock due to data is more spread since it has a highest standard deviation, in contrast Microsoft (MSFT) the less riskier stock.

  ![Tech stocks box plot](Images/tech_stocks_boxplot.png)

* Before calculating the standard deviation, the mean, median and mode are calculated using the DataFrame built-in function. Note at the mode that each stock will have several modes on the results.

  ![Mean, median and mode](Images/tech_stocks_mean_median_mode.png)

* The daily standard deviation is calculated by simply using the `std()` function of the DataFrame.

  ![Daily standard deviation](Images/tech_stocks_daily_std_dev.png)

* Based in the daily standard deviation, looking the maximum and minimum values we can find the riskier and the less riskier stock respectively.

  ![The riskier and less riskier stock](Images/tech_stock_riskier_less_riskier.png)

* Finally the annualized standard deviation is calculated by multiplying the daily standard deviation by the squared root of the total of trading days (252 in the USA).

  ![Annual risk calculation](Images/tech_stocks_annual_risk.png)
