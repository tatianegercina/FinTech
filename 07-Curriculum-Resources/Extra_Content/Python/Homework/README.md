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
