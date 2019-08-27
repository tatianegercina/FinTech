## 15.1 Lesson Plan: Algorithmic Trading

---

### Overview

Today's class will introduce students to a powerful, open-source analytics library called Pandas, which is built into and runs on a Python environment. Pandas is a software library designed specifically for data analytics and time series analysis, which are useful features for quantitative analytics. In this lesson, students will learn how to use Pandas to create and manipulate DataFrames, locate data with indexing, clean data, create basic data visualizations, and conduct quantitative analysis to automate financial tasks. By the end of class, students should understand how Pandas is used to perform everyday financial analysis, including calculating daily returns over time.

### Class Objectives

By the end of class, students will be able to:

* Describe the benefits of Pandas over spreadsheets to manipulate data for financial use cases.

* Explain what a DataFrame is and how it differs from a series.

* Create DataFrames from CSV files and use basic commands to manipulate them.

* Clean data using built-in commands of DataFrames.

* Manipulate data using DataFrame indexes.

* Describe the basic theory and calculations of returns using Pandas.

* Create basic data visualizations with Pandas' built-in plotting functions.

### Instructor Notes

* Today’s lesson is students’ introduction to Pandas. Students may be confused as to why they are using Pandas now, having just learned Python. Focus on helping them understand the relationship between Python and Pandas, and how it makes sense at this point to transition to Pandas. Discuss Pandas from a Pythonic point of view and emphasize that Pandas is written in Python. Underscore the fact that Pandas is Python code that a user wrote for the purpose of financial analytics; instead of hoarding their code in the depths of a hard drive, the creators packaged up the functions and made them available to the public.

* This lesson first covers technical concepts like reading in CSV files and checking for nulls, and then progresses to more advanced skills such as calculating daily and cumulative investment returns. Keep in mind that not all students have a finance background and, as such, may not understand returns right away. Leverage the knowledge of finance-savvy students in the class and encourage them to help their partners if they get stuck. Be sure to allow enough time for students to ask questions at the end of each section.

* Keep in mind that some students may be confused by the concept of return on investment (ROI) but hesitant to vocalize their uncertainty. Encourage students to work in groups so that they can make sense of the activity and concepts together. TAs should circulate the classroom to assist groups, and you should make yourself available for financial or technical questions. Finally, consider asking the finance-savvy students to provide clarity and assistance for students who need help.

* The activities in this lesson focus on developing and honing skills that are critical for succeeding in this course as well as performing day-to-day tasks within the FinTech professional world. Therefore, encourage students to practice these skills outside of class to gain mastery.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 3.2 Slides](https://docs.google.com/presentation/d/1KWphsqwNlAQGcLf2glW4096Jmnm_xS5pfmfguOsIFJU/edit#slide=id.g59b0dc3b18_0_96).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class and Introduction to Pandas (5 min)

In this section, you will give students a brief history of Pandas and an overview of its advantages, as well as explain why it's useful for FinTech professionals.

Welcome students to the first day of Pandas. Explain why students are learning it and provide a brief history.

* Pandas is currently one of the most powerful libraries in Python. Because of this, it is one of the most important superpowers students can have as FinTech professionals. Instead of reinventing the wheel and writing their own code, students will be able to leverage Pandas' repository of functions.

* Pandas was created by Wes McKinney to offer a flexible, high-performance tool for conducting quantitative analysis of financial data. Since 2008, Pandas has been used to manipulate, analyze, and visualize financial data.

* If Python was compared to a garage, Pandas would be the sleek Tesla parked inside. The owner can choose to leverage the speed, power, and efficiency of their Tesla and take it for a spin, or the owner could walk to their destination. While walking would produce the same result as using the Tesla, it would require extra labor and take more time. This lesson will teach students how skillfully utilize the sleek Tesla sitting in their garage. 

Transition to covering the advantages of Pandas.

* Pandas provides many advantages over Excel due to its data structures and built-in functions for analysis.

* Pandas doesn't require users to memorize formulas. Common financial calculations and formulas are made available to Pandas users as functions.

* Pandas offers functions that ensure data is clean and ready for analytic use.

* Pandas functions range from simple arithmetic to complex statistics. This allows users to automate most, if not all, financial calculations. Instead of writing the formula in a cell or calculating by hand, users just need to make a function call (e.g., `pct_change` to calculate daily returns for an investment).

Explain to students that they have already installed Pandas through Anaconda, so they don't need to install additional libraries. However, if they have issues running Pandas, they can use a free notebook by [Google Colab](https://colab.research.google.com/) and troubleshoot their installation with a TA during a break or office hours.

Review the [instructions](../../../02-Homework/04-Pandas/Instructions/README.md) for the homework assignment. Focus on getting students excited about learning Pandas by previewing the skills and work they will accomplish by the end of the week. Emphasize calculating investment returns/profit over time, as well as plot visualizations.
