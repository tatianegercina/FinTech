# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""


# @TODO: Define a function to sum the values of a specific field
def sum_field(report, field):

# @TODO: Define a function to calculate the average of the values of a specific field
def avg_field(report, field):

# @TODO: Define a function to find the minimum value of a specific field
def min_field(report, field):

# @TODO: Define a function to find the maximum value of a specific field
def max_field(report, field):



# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('')
sales_filepath = Path('')

# @TODO: Initialize list object to hold our menu data
menu = []

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# item,category,description,price,cost
# @TODO: Read the menu data into the menu list



# Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
# @TODO: Open the csv file and load it in as a csv.reader object

    # @TODO: Skip header of sales data


    # @TODO: Loop over every row in the csv file

        # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
        # @TODO: Initialize sales data variables

        # @TODO:
        # If the item value not in the report, add it as a new entry with initialized metrics
        # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit


        # @TODO: For every row in our sales data, loop over the menu records to determine a match


            # Item,Category,Description,Price,Cost
            # @TODO: Initialize menu data variables



            # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


                # @TODO: Print out matching menu data


                # @TODO: Cumulatively add up the metrics for each item key


# @TODO: Print total number of records in sales data


# Let's visualize the report so far
for key, value in report.items():
    print(key, value)
print() # Adds a space between the end of the program and the console input

# @TODO:
# Find items that are performing above or below the average profitability
# and append to corresponding list
under_performing = []
over_performing = []

# @TODO: Write out report to a text file (won't appear on the command line output)
