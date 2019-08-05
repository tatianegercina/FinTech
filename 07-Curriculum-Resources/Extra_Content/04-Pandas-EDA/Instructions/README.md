# Unit 4 Assignment - Exploratory Data Analysis

![EDA](Images/Replaceme.png)

## Background

Pack your bags! It's time to do some exploratory data analysis! Remember that the goal of EDA is to gain intuition about your data and generate ideas, observations, and questions that you can further explore with formal analysis. In this homework, you will be analyzing a year's worth of LendingClub data. LendingClub offers peer-to-peer lending services and graciously provides their lending data for free online. All sorts of useful information can be deciphered from this data, but the first step is to get a general understanding of the structures, relationships, and patterns in the data. This is where EDA with Pandas comes in!

In this homework assignment, you will be accomplishing three main tasks:

1. [Data Preparation](#Data-Preparation)
2. [Data Exploration](#Data-Exploration)
3. [Data Communication](#Data-Communication)

- - -

### Instructions

#### Data Preparation

Create a data preparation notebook to do all of the initial data wrangling in. There are four zipped csv files provided that contain quarterly data for 2018 from LendingClub. Your task is to combine, transform, clean, and output a cleaned csv file. You will use this cleaned csv file in the next data exploration section.

#### Data Exploration

Create a notebook for exploratory data analysis to gain intuition about the variables, relationships, and structures in the data. Use the cleaned CSV data and apply the exploratory analysis and visualization techniques from class to better understand and summarize the quantitative and qualitative data. Remember that EDA is not only useful for data intuition, but it can help identify questions and hypothesis that can be further explored.

Use EDA techniques from class to answer at least 3 of the following questions (support your answers with code, visualizations, and written observations from exploring the data):

* What are the typical and atypical values?
* What are the outliers?
* What values are missing or are wrong?
* What is the shape of the data (variance, skew, distribution)?
* What are relationships, patterns, or structure that you see?
* What are the most important or interesting factors?

#### Data Communication

Create a summary report in markdown that highlights all of the interesting variables, outliers, relationships, and structure that was identified during the EDA process. Include screenshots of any charts, plots, or tables that help explain the data. Be sure to include any deep analysis that you might have explored after the initial EDA. This report should help others better understand the data in a concise format. Add this markdown file to the root of your github repository.

Create a binder link to each of your notebooks and add the link to your README.md file. This will allow other users to reproduce your work and experiment with your code in their own environment.

- - -

### Resources

The [Pandas Visualization Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html) is a great reference for plotting and charting with Matplotlib through the Pandas interface.

[Binder](https://mybinder.org/) can be used to add share a reproducible and live version of your analysis notebook. This is a great way to allow others to test and experiment with your code. Create a binder link to the notebooks on your Github repository and add the link to your README.md file.

- - -

### Hints and Considerations

Pandas will read and write compressed (zipped) csv files, so it is highly recommended to leave the files in their zipped state. The official Pandas docs for [to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) has information on the compression parameter to write the file as a zipped csv.

- - -

### Submission

* Create a Jupyter Notebook and host the notebook on Github.

* Include a README.md file that summarizes your assumptions and findings.

* Create a binder link to your Jupyter notebooks and add the binder link to your README.md file.

* Submit the link to your Github project to Bootcampspot.
