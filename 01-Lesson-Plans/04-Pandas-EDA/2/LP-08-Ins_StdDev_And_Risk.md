### 8. Instructor Do: Standard Deviation & Risk (10 mins)

* **Files:**

  * [Lesson 4.2 slides](LINK TO GOOGLE SHEETS!)

This lesson will introduce students to some basic descriptive statistics than are commonly used on finance to assess risk. Open the lesson slide deck and introduce students to mean, mode, median, and standard deviation by highlighting the following:

* Descriptive statistics are used to describe and understand the features of a specific dataset set by giving short summaries about the sample and measures of the data. Together with simple graphics analysis, they form the basis of virtually every quantitative analysis of data.

* Descriptive statistics are split into measures of central tendency and measures of variability.

* The measurements of central tendency are the mean, mode and median.

  * The **mean**, also known as **average** or **arithmetic mean**, is the central value of a discrete set of numbers, it's calculated by the sum of the value dived by the number o values. Show the mean formula to the class.

    $$
    \overline{x}=\frac{1}{n}\left ( \sum_{i=1}^{n} x_{i} \right )=\frac{x_{1}+x_{2}+ \cdots x_{n}}{n}\\
    \begin{array}{l}{\text { where: }} \\ {\overline{x}=\text { the mean of all data points }} \\ {n=\text { the number of data points }}  \\ {x_{i}=\text { the } i^{\text { th }} \text { data point }} \end{array}
    $$

  * The **mode** is the most frequently occurring number value among a discrete set of numbers, it's found by collecting and organizing data in order to count the frequency of each result.

  * The **median** sometimes could have a similar value as the mean, however it's calculation is different, this central tendency measure is the middle number in a sorted list of numbers.

* The measures of variability are the variance and the standard deviation.

  * The **variance** measures how spread are numbers in a dataset. It's used to understand how far each number in the dataset is from mean. The variance is calculated is calculated by taking the differences between each number in the dataset and the mean, the differences are squared to make them positive and the sum of the squares is divided by the number of values in the set. Show the variance formula to the class.

    $$
    \sigma^{2}=\frac{\sum_{i=1}^{n}\left(x_{i}-\overline{x}\right)^{2}}{n}\\
    \begin{array}{l}{\text { where: }} \\ {\sigma^{2}=\text { the variance }} \\ {x_{i}=\text { the } i^{\text { th }} \text { data point }} \\ {\overline{x}=\text { the mean of all data points }} \\ {n=\text { the number of data points }}\end{array}
    $$

  * The **standard deviation** is a measure of variability and is used on finance to assess risk. It's calculated as the square root of variance by determining the variation between each data point relative to the mean.

  $$
  \begin{array}{l}{ \sigma =\sqrt{\frac{\sum_{i=1}^{n}\left(x_{i}-\overline{x}\right)^{2}}{n-1}}} \\ {\text { where: }} \\ \sigma=\text{The standard deviation} \\ {x_{i}=\text {Value of the } i^{t h} \text { point in the data set }} \\ {\overline{x}=\text { The mean value of the data set }} \\ {n=\text { The number of data points in the data set }}\end{array}
  $$
