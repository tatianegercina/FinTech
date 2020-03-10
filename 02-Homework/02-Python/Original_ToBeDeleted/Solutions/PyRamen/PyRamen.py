# -*- coding: UTF-8 -*-
"""PyRamen Homework Solution."""

# Import libraries and dependencies
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath) as menu_file:
    reader = csv.reader(menu_file)

    # Skip header of menu data
    next(reader)

    # Iterate over each row after the header
    for row in reader:
        menu.append(row)

# Read in the sales data into the sales list
with open(sales_filepath) as sales_file:
    reader = csv.reader(sales_file)

    # Skip header of sales data
    next(reader)

    # Iterate over each row after the header
    for row in reader:
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object
for row in sales:
    print()
    print(row)

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    quantity = int(row[3])
    sales_item = row[4]

    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sales_item not in report.keys():
        report[sales_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # For every row in our sales data, loop over the menu records to determine a match
    for record in menu:

        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
        item = record[0]
        price = float(record[3])
        cost = float(record[4])

        # Calculate profit of each item in the menu data
        profit = price - cost

        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sales_item == item:

            # Print out matching menu data
            print(f"Does {sales_item} equal {item}? WE HAVE A MATCH!!!")
            print(f"   Item: {item}")
            print(f"   Price: ${price}")
            print(f"   Cost: ${cost}")
            print(f"   Profit: ${profit}")

            # Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity

        # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print("Does", sales_item, "equal", record[0], "? WA WA, NO MATCH")

    # Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
print()
print("Total Number of Records:", row_count)
print() # Adds a space between the end of the program and the console input

# Write out report to a text file (won't appear on the command line output)
with open("report.txt", "w") as txt_file:
    for key, value in report.items():

        line = f"{key} {value}\n"
        txt_file.write(line)
