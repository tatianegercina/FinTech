## 4.3 Lesson Plan - Stock Portfolios

---

### Overview

Today's class will focus on the notion of analyzing the performance of not just a single stock, but groups of stocks together -- otherwise known as a portfolio of stocks. Stock portfolios are an important strategy in the realm of investing as total capital is proportioned among several stocks, thereby minimizing risk by preventing the "all eggs in one basket" dilemma. However, in order to create an optimal portfolio that maximizes returns while minimizing risk, it's necessary to not only analyze the average return and risk of the portfolio overall, but also the correlation between stocks as well (how much one stock price changes with or against another). This lesson will teach students how to analyze the correlations of stocks against one another, calculate rolling statistics and volatility (beta) of stocks together, and optimize the composition of a portfolio and compare the performance against other portfolios.

### Class Objectives

By the end of class, students will be able to:

* Describe the benefits of Pandas over spreadsheets to manipulate data on financial use cases.
* Explain what a dataframe is and how it differs from a series.
* Create dataframes from CSV files and becoming confident using the basic commands to manipulate them.
* Demonstrate the ability to clean data using the dataframe built-in commands.
* Manipulate with confidence indexes on dataframes.
* Describe the basic theory and calculations of returns using Pandas.
* Create basic data visualizations with Pandas built-in functions to present preliminary results.

### Instructor Notes

* After learning how to create basic scripts with Python, students are eager to start doing financial analysis beyond the capabilities of Microsoft Excel. In this lesson, students will discover an amazing library for financial analysis that has many benefits over using Excel. Learning about these features and seeing how easy it is to use them will be very exciting for students.

* Students will focus on the basics of Pandas and then learn how to apply Pandas to calculate and visualize daily returns. Not all students may have the financial background to understand returns, so leverage the finance savvy students to help their partners when they get stuck. Be sure to spend extra time explain the returns calculations as they will use this for the remainder of the week.

* Indexing might be challenging for students, so live coding the examples and spending extra time in the review may be necessary to help them understand the fundamentals. Encourage students to practice these techniques after class to gain mastery.

* Data cleaning is an art and not an exact science, so this class focuses on common data cleaning techniques. Each dataset will have unique characteristics and may or may not need the same cleaning steps, but these techniques will help them with most of their data cleaning challenges.

If there are some curious students who want to learn more, [feel free to slack out this link](https://www.kaggle.com/chrisbow/kernels?sortBy=relevance&group=everyone&search=Cleaning+data+with+Python&page=1&pageSize=20&userId=1541110) with some guides and challenges to learn more about data cleaning using Python.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students to the first Pandas day, Today they will start discovering one of the most powerful libraries on python to analyse and manipulate data, so remark to the class that using Pandas is one of the most important superpowers as FinTech professionals.

Mention to the class the fact that Pandas was created by [Wes McKinney](https://en.wikipedia.org/wiki/Wes_McKinney) to offer a high performance and flexible tool for performing quantitative analysis on financial data.

Explain that Pandas provides many advantages over Excel through it's data structures and built-in functions for analyzing data.

Explain to students that they have already installed Pandas through Anaconda, so they don't need to install additional libraries by now. However, if they have issues running Pandas then they can use a free notebook by [Google Colab](https://colab.research.google.com/) and troubleshoot their installation with a TA during a break or office hours.
