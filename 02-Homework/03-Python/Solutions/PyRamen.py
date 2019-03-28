
# Note, this homework could also use the menu data in the form of dicts / JSON structure to keep things more dynamic (key vs. index number)
# Will students have knowledge of nested JSON objeects at this point? If so, menu hierarchy could be item = { 'category' : '<category', desc... }

import csv
import pprint as pp 
import pandas as pd
from pathlib import Path


def sum_field(report, field):
	"""
	Summarize a specific field for every key in the report dictionary and return the total.

	Keyword arguments:
	report -- dict object
	field -- the column looking to perform the operation on
	"""

	total = 0

	for key in report:

		total += report[key][field]

	return total

def avg_field(report, field):
	"""
	Average a specific field for every key in the report dictionary and return the average.

	Keyword arguments:
	report -- dict object
	field -- the column looking to perform the operation on
	"""

	total = 0

	for key in report:

		total += report[key][field]

	avg = round(total / len(report), 2)

	return avg

def min_field(report, field):
	"""
	Find the minimum for a specific field key in the report dictionary, return the minimum and the associated key.

	Keyword arguments:
	report -- dict object
	field -- the column looking to perform the operation on
	"""

	minimum = None
	min_key = None

	for key in report:

		if not minimum:

			minimum = report[key][field]

		elif report[key][field] < minimum:

			minimum = report[key][field]
			min_key = key

	return minimum, min_key

def max_field(report, field):
	"""
	Find the maximum for a specific field key in the report dictionary, return the maximum and the associated key.

	Keyword arguments:
	report -- dict object
	field -- the column looking to perform the operation on
	"""

	maximum = None
	max_key = None

	for key in report:

		if maximum is None:

			maximum = report[key][field]

		elif report[key][field] > maximum:

			maximum = report[key][field]
			max_key = key

	return maximum, max_key	



menu_filepath = Path('Resources/menu.csv')
sales_filepath = Path('Resources/testdata_730_days.csv')


# List object to hold our menu data
menu = []

# Dict obejct to hold our key-value pairs of items and metrics
report = {}

# item	category	description	price	cost
# Read in the menu data
with open(menu_filepath) as menu_file:
	reader = csv.reader(menu_file)

	# Skip header of menu data
	next(reader)

	for row in reader:
		menu.append(row)


# Line_Item_ID	Date	Credit_Card_Number	Quantity	Menu_Item
# Open the csv file and load it in as a csv.reader object
with open(sales_filepath) as csvfile:
	reader = csv.reader(csvfile, delimiter=',')

	# Skip header of sales data
	next(reader)

	row_count = 0

	# Loop over every row in the csv file
	for row in reader:
		print()
		print(row)

		#
		count = 0
		revenue = 0
		cogs = 0
		profit = 0

		# If the item value not in the report, add it as a new entry with initialized metrics
		# Naming convention allows the keys to be ordered in logical fasion, count, revenue, cost, profit
		if row[4] not in report.keys():
			report[row[4]] = {
				"01-count" : 0,
				"02-revenue" : 0,
				"03-cogs" : 0,
				"04-profit" : 0
			}

		# For every row in our sales data, loop over the menu records to determine a match  
		for record in menu:

			# If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
			if row[4] == record[0]:

				# Sales Data
				# Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
				line_item_id = row[0]
				date = row[1]
				cc_number = row[2]
				quantity = int(row[3])
				menu_item = row[4]

				# Menu Data
				# Item,Category,Description,Price,Cost
				item = record[0]
				category = record[1]
				description = record[2]
				price = int(record[3])
				cost = int(record[4])
				profit = (price - cost)

				# Print out matching menu data 
				print(f"Does {row[4]} equal {record[0]}? WE HAVE A MATCH!!!")
				print(f"   Item: {item}")
				print(f"   Category: {category}")
				print(f"   Price: ${price}")	
				print(f"   Cost: {cost}")
				print(f"   Profit: ${profit}")	

				# Cumulatively add up the metrics for each item key
				report[row[4]]['01-count'] += quantity
				report[row[4]]['02-revenue'] += (price * quantity)
				report[row[4]]['03-cogs'] += cost
				report[row[4]]['04-profit'] += profit

			else:
				print("Does", row[4], "equal", record[0], "? WA WA, NO MATCH")

		row_count += 1

fields = ['01-count', '02-revenue', '03-cogs', '04-profit']


# Print total number of records in sales data
print()
print("Total Number of Records:", row_count)
print()

# Let's visualize the report so far
for key, value in report.items():
	print(key, value)


# Calculate the SUM, AVG, MAX, and MIN for each field of every item in the report
print()
for field in fields:
	print(field, "SUM", sum_field(report, field))
	print(field, "AVG", avg_field(report, field))
	print(field, "MAX", max_field(report, field))
	print(field, "MIN", min_field(report, field))

print()

# What item is the most popular?
# What item is the least popular?
# What item is the most profitable?
# What item is the least profitable?
# What items are underperforming?
# What items are overperforming?


# Find items that are performing above or below the average profitability
under_performing = []
over_performing = []

for item in report:

	if report[item]['04-profit'] < avg_field(report, '04-profit'):

		under_performing.append(item)

	elif report[item]['04-profit'] > avg_field(report, '04-profit'):

		over_performing.append(item)

print("Most Popular:", max_field(report, '01-count'))
print("Least Popular:", min_field(report, '01-count'))
print("Most Profitable:", max_field(report, '04-profit'))
print("Least Profitable:", min_field(report, '04-profit'))
print("Overperforming Items:", over_performing)
print("Underperforming Items:", under_performing)
print()







