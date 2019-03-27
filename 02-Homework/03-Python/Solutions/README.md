# PyRamen

![ramen.jpg](Images/ramen.jpg)

## Background

Welcome to Ichiraku Ramen! 

Opening up a ramen shop has always been your dream and it's finally been realized --- you're closing out on your second year of sales! Like last year, you need to analyze your business' financial performance by cross-referencing your sales data with your internal menu data to figure out revenues and costs for the year. 

This year, you also want to analyze how well your business did on a per product basis (as you have several choices of ramen) in order to better understand what products are doing well, poorly, and ultimately which products should potentially be removed or changed. You tried doing this type of per product analysis last year in Excel; unfortunately however, you were not able to keep your reports up-to-date with your current sales data.

Therefore, the necessity requires innovation. As you have more and more customers, and thus more and more data to process, you will need a tool that takes you beyond Excel and will allow you to automate your calculations in a manner that scales out with your business. 

Hence, the use of Python! Python gives you a wide range of capabilities when handling data by harnessing the power of low-level Python data structures and high-level development libraries, all the while supporting the automation and scalability needs for a growing enterprise.

In this homework assignment, you will need to:

1. [Read the Data](#Read-in-the-Data)
2. [Manipulate the Data](#Group-the-Data)
3. [Analyze the Data](#Analyze-the-Data)

- - -

## Instructions

### Read the Data

First things first, you'll need to read in your two datasets: `menu_data.csv` and `sales_data.csv`

* Define a `read_csv` function that...
  * Takes in a file path as a parameter
  * Opens the specified file path as a CSV
  * Skips the header
  * Loops over the rest of the rows and appends every row to a new list object 
  * Returns the list object containing all rows of the CSV file
* Call your newly defined function `read_csv` on your `menu_data.csv` and `sales_data.csv` and assign the return values to the variables `menu` and `sales`

### Manipulate the Data

Now that you've read your two datasets in Python, you can begin manipulating both datasets to generate a report that showcases on a per product basis...

  * `01-count` - the total quantity for each ramen type
  * `02-revenue` - the total revenue for each ramen type
  * `03-cogs` - the total cost of goods sold for each ramen type 
  * `04-profit` - the total profit for each ramen type
    

You'll need to 'join' your datasets by the common `item` in order to pull the `price` and `cost` from the menu data to calculate the above four metrics.
Therefore...

* Loop through every `item` in `sales`
* Create a nested loop by looping through every `item` in `menu`, for every `item` in `sales` 
* Do a quick check to see if the `item` in `sales` is already a key in the report dict object, if not add the item as a key initialized with
  the four metrics above (set them equal to 0)
* If the `item` in sales is equal to the `item` in `menu`, capture the `quantity` from the sales data, `price`, and `cost` from the menu data, and calculate the `profit` for each item.
  Add the values to the corresponding item in the report.
* The report should output each ramen type as the keys and `01-count`, `02-revenue`, `03-cogs`, and `04-profit` metrics as the values for every ramen type.

### Analyze the Data

Now that we have our data in a per-product format, let's perform some field-level calculations that allow us to answer questions like...

  * What item is the most popular?
  * What item is the least popular?
  * What item is the most profitable?
  * What item is the least profitable?
  * What items are underperforming?
  * What items are overperforming? 

* Create the following functions that take in the report and field of choice as parameters, and returns the calculations for that particular field of all keys in the report.
  * `sum_field(report, field)` - summarize up the values of the specified field for every key
  * `avg_field(report, field)` - average the values of the specified field for every key
  * `min_field(report, field)` - find the minimum of the values of the specified field for every key
  * `max_field(report, field)` - find the maximum of the values of the specified field for every key
* Print out the six questions and corresponding answers.


## Extension Activities

* Potential Ideas
  * Sensitivity Analysis
  * Monthly/Yearly Profit Reports
  * Generate Income Statement

- - -

## Resources

* [Stack Overflow](https://www.stackoverflow.com) - A wealth of community-driven questions and answers, particularly effective for IT solution seekers
* [Python Basics](https://pythonbasics.org/) - Contains example materials and exercises for the Python 3 programming language
* [Python Documentation](https://docs.python.org/3/) - Official Python documentation

- - -

## Hints and Considerations

* TBD

- - -

## Submission

* Create a Python file (ex. python_hw.py)
* Write out your results to a report.csv file
* Submit the link to your GitHub repo to Bootcamp Spot.