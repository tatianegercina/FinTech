# PyRamen

![ramen.jpg](Images/ramen.jpg)

## Background

Welcome to Ichiraku Ramen! Opening up a ramen shop has always been your dream and it's finally been realized --- you're closing out on your second year of sales!
Like last year, you need to analyze your business' financial performance by cross-referencing your sales data with your internal menu data to figure out revenues
and costs for the year. This year, you also want to analyze how well your business did on a per product basis (as you have several choices of ramen) in order to 
better understand what products are doing well, poorly, and ultimately which products should potentially be removed or changed. You tried doing this type of per
product analysis last year in Excel, but doing so required a lot of manual intervention and frankly is not as kept up-to-date with your ever growing sales data.

Therefore, the necessity requires innovation. You need to perform this level of analysis to keep your menu adaptable and in-tune with your customers' tastes but
you also realize that going the route of Excel to perform your analysis, while possible, is inconvenient and not a viable long-term solution, especially as your 
business grows (as does your responsibilities!). You need a tool that will allow you to automate your calculations and do so in a manner that scales out with your
business as you have more and more customers, and thus more and more data to process. 

Hence, the use of Python! Python should give you the functionality that you need to perform and automate low-level data manipulation as well as provides the 
scalability attirbutes required for a growing enterprise. 

In this homework assignment, you will need to:

1. [Read in the Data](#Read-in-the-Data)
2. [Group the Data](#Group-the-Data)
3. [Analyze the Data](#Analyze-the-Data)

- - -

## Instructions

### Read in the Data
* Preprocess the raw dataset prior to fitting the model.
* Perform feature selection and remove unnecessary features.
* Use `MinMaxScaler` to scale the numerical data.
* Separate the data into training and testing data.

### Group the Data

* Use `GridSearch` to tune model parameters.
* Tune and compare at least two different classifiers.

### Analyze the Data

Compare the performance of two or more classifiers to determine the best model performance.

- - -

## Resources

* [Exoplanet Data Source](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)

* [Scikit-Learn Tutorial Part 1](https://www.youtube.com/watch?v=4PXAztQtoTg)

* [Scikit-Learn Tutorial Part 2](https://www.youtube.com/watch?v=gK43gtGh49o&t=5858s)

* [Grid Search](https://scikit-learn.org/stable/modules/grid_search.html)

- - -

## Hints and Considerations

* Start by cleaning the data, removing unecessary columns, and scaling the data.

* Try a simple model first, and then tune the model using `GridSearch`.

- - -

## Submission

* Create a Jupyter Notebook and host the notebook on GitHub.

* Include a README.md file that summarizes your assumptions and findings.

* Submit the link to your GitHub project to Bootcamp Spot.