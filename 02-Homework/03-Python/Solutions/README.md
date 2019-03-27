# PyRamen

![ramen.jpg](Images/ramen.jpg)

## Background

Welcome to Ichiraku Ramen! 

Opening up a ramen shop has always been your dream and it's finally been realized --- you're closing out on your second year of sales! Like last year, you need to analyze your business' financial performance by cross-referencing your sales data with your internal menu data to figure out revenues and costs for the year. 

This year, you also want to analyze how well your business did on a per product basis (as you have several choices of ramen) in order to better understand what products are doing well, poorly, and ultimately which products should potentially be removed or changed. You tried doing this type of per product analysis last year in Excel; unfortunately however, you were not able to keep your reports up-to-date with your current sales data.

Therefore, the necessity requires innovation. As you have more and more customers, and thus more and more data to process, you will need a tool that takes you beyond Excel and will allow you to automate your calculations in a manner that scales out with your business. 

Hence, the use of Python! Python should give you the functionality that you need to perform and automate data manipulation. Python also  provide the scalability attributes required for a growing enterprise.

In this homework assignment, you will need to:

1. [Read in the Data](#Read-in-the-Data)
2. [Group the Data](#Group-the-Data)
3. [Analyze the Data](#Analyze-the-Data)

- - -

## Instructions

### Read in the Data
* Read in the `menu_data.csv` and append every menu item to a `list` object.
* Create a report `dict` object to hold each ramen type as a `key` with every
  key having `values` `01-count`, `02-revenue`, `03-cogs`, `04-profit`. 


### Group the Data

* Read in the `sales_data.csv` and use an `if` statement with a `for` loop 
  to match every transaction item to a corresponding menu item to grab the 
  sale transaction's `quantity` and the item's `price` and `cost`.
* Place every item as a `key` to the report `dict`, and if it already exists 
  cumulatively sum up `quantity` as `01-count`, `price` as `02-revenue`, 
  `cost` as `03-cogs` and use (`price` - `cost`) to calculate `04-profit`.

### Analyze the Data

* Create a `sum()`, `avg()`, `min()`, and `max()` function that will return
  the metric for every item and field of choice. For the `min()` and `max()`
  function, return the corresponding `key` as well.
* Find and print out the following:

	* What item is the most popular?
	* What item is the least popular?
	* What item is the most profitable?
	* What item is the least profitable?
	* What items are underperforming?
	* What items are overperforming? 

## Extension Activities

* Potential Ideas
  * Sensitivity Analysis
  * Monthly/Yearly Profit Reports
  * Generate Income Statement

- - -

## Resources

* [Stack Overflow](https://www.stackoverflow.com) - A wealth of community-driven questions and answers, particularly effective for IT solution seekers.
* [Python Basics](https://pythonbasics.org/) - Contains example materials and exercises for the Python 3 programming language.
* [Python Documentation](https://docs.python.org/3/) - Official Python documentation.

- - -

## Hints and Considerations

* TBD

- - -

## Submission

* Create a Python file (ex. <file_name>.py)
* Write out your results to a report.csv file
* Submit the link to your GitHub project to Bootcamp Spot.