# Unit 2 | Homework Assignment: Automate Your Day Job with Python

## Background

You've made it! It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete **two** Python activities, PyBank and PyRamen. Both activities present a real-world situation in which your newfound Python skills will come in handy. These activities are far from easy, though, so expect some hard work ahead!

## Before You Begin

1. Create a new GitHub repo called `python-homework`. Then, clone it to your computer.

2. In your local git repository, create a directory for both of the Python activities. Use folder names that correspond to the activities: **PyBank** and **PyRamen**.

3. In each folder you just created, add a new file called `main.py`. This will be the main script to run for each analysis.

4. Push the above changes to GitHub.

## PyBank

![Revenue](Images/revenue-per-lead.jpg)

In this activity, you are tasked with creating a Python script for analyzing the financial records of your company. You will be provided with a financial dataset in this file: [budget_data.csv](PyBank/Resources/budget_data.csv). This dataset is composed of two columns, Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of Profit/Losses over the entire period

  * The average of the changes in Profit/Losses over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

Your resulting analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

Your final script should print the analysis to the terminal and export a text file with the results.

## PyRamen

![ramen.jpg](Images/ramen.jpg)

## Background

Welcome to Ichiban Ramen!

Opening a ramen shop has always been your dream, and now it's finally been realized––you're closing out on your second year of sales! Like last year, you need to analyze your business's financial performance by cross-referencing your sales data with your internal menu data to figure out revenues and costs for the year. 

This year, you also want to analyze how well your business did on a per-product basis (as you have several choices of ramen) in order to better understand which products are doing well, which are doing poorly, and, ultimately, which products may need to be removed or changed. 

You tried doing this type of per-product analysis last year in Excel, but you were not able to keep your reports up-to-date with your current sales data. Therefore, you need to innovate. With more customers and more data to process, you'll need a tool that will allow you to automate your calculations in a manner that scales with your business.

Enter Python! Python provides a wide range of capabilities for handling data, harnessing the power of low-level Python data structures and high-level development libraries, all the while supporting the automation and scalability needs for a growing enterprise.

In this homework assignment, you will need to:

1. [Read the Data](#Read-in-the-Data)

2. [Manipulate the Data](#Group-the-Data)

3. [Analyze the Data](#Analyze-the-Data) (Challenge)

- - -

## Instructions

### Read the Data

Complete the following:

* Read in `menu_data.csv` as a list object. (This way, you can cross-reference your menu data with your sales data as you read in your sales data in the coming steps.) 

    * Use a `with` statement and the `csv` module to begin reading `menu_data.csv`

    * Take in a file path as a parameter.

    * Open the specified file path as a CSV. 

    * Skip the header. 

    * Loop over the rest of the rows and append every row to a new `menu` list object. (In this case, it will be a list of lists.) 
  
* Set up the same process to read in `sales_data.csv`. However, instead of appending every row of the menu data to a new list object, here you will need to perform conditionals to evaluate every row of the sales data, and then group the sales data in a new `report` dictionary. (In this case, it will be a dict of dicts.)

### Manipulate the Data

Generate a `report` dictionary that showcases the business on a per-product basis by calculating the following: 

* `01-count`: the total quantity for each ramen type

* `02-revenue`: the total revenue for each ramen type

* `03-cogs`: the total cost of goods sold for each ramen type 

* `04-profit`: the total profit for each ramen type
    
Join the datasets by the common `item` in order to pull the `price` and `cost` from the menu data and calculate these four metrics.

Complete the following:

* Loop through every `item` in `sales`.

* Create a nested loop by looping through every `item` in `menu`, for every `item` in `sales`. 

* Do a quick check to see if the `item` in `sales` is already a key in the report dict object. If it isn't, add the item as a key initialized with the four metrics above. (Set them equal to 0.)

* If the `item` in sales is equal to the `item` in `menu`, capture the `quantity` from the sales data, find the `price` and `cost` from the menu data, and calculate the `profit` for each item.

* Add the values to the corresponding item in the report.

* The report should output each ramen type as the keys and `01-count`, `02-revenue`, `03-cogs`, and `04-profit` metrics as the values for every ramen type.
  
  ```
  spicy miso ramen {'01-count': 9238, '02-revenue': 110856.0, '03-cogs': 46190.0, '04-profit': 64666.0}
  tori paitan ramen {'01-count': 9156, '02-revenue': 119028.0, '03-cogs': 54936.0, '04-profit': 64092.0}
  truffle butter ramen {'01-count': 8982, '02-revenue': 125748.0, '03-cogs': 62874.0, '04-profit': 62874.0}
  tonkotsu ramen {'01-count': 9288, '02-revenue': 120744.0, '03-cogs': 55728.0, '04-profit': 65016.0}
  vegetarian spicy miso {'01-count': 9216, '02-revenue': 110592.0, '03-cogs': 46080.0, '04-profit': 64512.0}
  shio ramen {'01-count': 9180, '02-revenue': 100980.0, '03-cogs': 45900.0, '04-profit': 55080.0}
  miso crab ramen {'01-count': 8890, '02-revenue': 106680.0, '03-cogs': 53340.0, '04-profit': 53340.0}
  nagomi shoyu {'01-count': 9132, '02-revenue': 100452.0, '03-cogs': 45660.0, '04-profit': 54792.0}
  soft-shell miso crab ramen {'01-count': 9130, '02-revenue': 127820.0, '03-cogs': 63910.0, '04-profit': 63910.0}
  burnt garlic tonkotsu ramen {'01-count': 9070, '02-revenue': 126980.0, '03-cogs': 54420.0, '04-profit': 72560.0}
  vegetarian curry + king trumpet mushroom ramen {'01-count': 8824, '02-revenue': 114712.0, '03-cogs': 61768.0, '04-profit': 52944.0}
  ```

- - -

## Challenge

### Analyze the Data

Now that we have our data in a per-product format, let's perform some field-level calculations that allow us to answer the following questions. 

**Summary Statistics:**

* What is the total number of ramen bowls sold?

* What is the total revenue generated?

* What is the total cost of goods sold?

* What is the net profit generated?

**Average Statistics:**

* How many ramen types are there?

* What is the average number of ramen bowls sold per ramen type?

* What is the average revenue per ramen type?

* What is the average cost of goods sold per ramen type?

* What is the average profit per ramen type?

**Min/Max Statistics:**

* What item is the most popular?

* What item is the least popular?

* What item generated the most revenue?

* What item generated the least revenue?

* What item is the most costly?

* What item is the least costly?

* What item is the most profitable?

* What item is the least profitable?

**Filter Items:**

* What items are underperforming?

* What items are overperforming? 

To answer these questions, do the following:

* Create the following functions that take in the report and field of choice as parameters, and then return the calculations for that particular field of all keys in the report.

  * `sum_field(report, field)`: Summarize the values of the specified field for every item in the report.

  * `avg_field(report, field)`: Average the values of the specified field for every item in the report. 

  * `min_field(report, field)`: Find the minimum of the values of the specified field for every item in the report. 

  * `max_field(report, field)`: Find the maximum of the values of the specified field for every item in the report

Your report details should look similar to the following:

  ```text
  Ramen Analysis Report
  -----------------------------
  Summary Statistics:

  Total Number of Ramen Sold: 100,106 bowls
  Total Revenue Generated: $1,264,592.0
  Total Cost of Goods Sold: $590,806.0
  Net Profit Generated: $673,786.0

  Average Statistics:

  Number of Ramen Types: 11
  Average Number Sold per Ramen Type: 9,100.55 bowls
  Average Revenue Generated per Ramen Type: $114,962.91
  Average Cost of Goods Sold per Ramen Type: $53,709.64
  Average Net Profit Generated per Ramen Type: $61,253.27

  Min/Max Statistics:

  Most Popular: (9288, 'tonkotsu ramen')
  Least Popular: (8824, 'vegetarian curry + king trumpet mushroom ramen')
  Most Revenue Generating: (127820.0, 'soft-shell miso crab ramen')
  Least Revenue Generating: (100452.0, 'nagomi shoyu')
  Most Costly: (63910.0, 'soft-shell miso crab ramen')
  Least Costly: (45660.0, 'nagomi shoyu')
  Most Profitable: (72560.0, 'burnt garlic tonkotsu ramen')
  Least Profitable: (52944.0, 'vegetarian curry + king trumpet mushroom ramen')

  Filter Items:

  Overperforming Items: ['spicy miso ramen', 'tori paitan ramen', 'truffle butter ramen', 'tonkotsu ramen', 'vegetarian spicy miso', 'soft-shell miso crab ramen', 'burnt garlic tonkotsu ramen']
  Underperforming Items: ['shio ramen', 'miso crab ramen', 'nagomi shoyu', 'vegetarian curry + king trumpet mushroom ramen']
  ```
- - -

## Resources

* [Stack Overflow](https://www.stackoverflow.com): A wealth of community-driven questions and answers, particularly effective for IT solution seekers.

* [Python Basics](https://pythonbasics.org/): Contains example materials and exercises for the Python 3 programming language.

* [Python Documentation](https://docs.python.org/3/): Official Python documentation

- - -

## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down you tasks into discrete mini-objectives. This will be a _much_ better course of action than attempting to Google search for a miracle.

* As you will discover, for some of these activities, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct as data analysts is often to head straight to Excel, creating scripts in Python can provide us with more robust options for handling "big data."

* Your scripts should work for each dataset provided. Run your script for each dataset separately to make sure that the code works for different data.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

* Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." Come prepared to show your effort and thought patterns, we'll be happy to help along the way.

* Always commit your work (and do it often!) and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

- - -

## Submission

* Upload homework files to your GitHub repo.

* Submit the link to your GitHub repo on Bootcamp Spot.

---

© 2019 Trilogy Education Services
