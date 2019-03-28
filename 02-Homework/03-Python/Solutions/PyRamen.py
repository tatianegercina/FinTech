
import csv
import pprint as pp
from pathlib import Path


def sum_field(report, field):
	"""
	Summarize a column of data.

	Args:
		report (dict): The report dictionary.
		field (str): The column to perform the operation on.

	Returns:
		A sum total for the requested field (column) in the report.
	"""

	total = 0
	for key in report:
		total += report[key][field]
	
	return total

def avg_field(report, field):
	"""
	Average a column of data.

	Args:
		report (dict): The report dictionary.
		field (str): The column to perform the operation on.

	Returns:
		A calculated average for the requested field (column) in the report.
	"""

	total = 0
	for key in report:
		total += report[key][field]
	
	avg = round(total / len(report), 2)
	return avg

def min_field(report, field):
	"""
	Find the minimum and associated key of a column of data.

	Args:
		report (dict): The report dictionary.
		field (str): The column looking to perform the operation on.
	
	Returns:
		The minimum for the requested field (column) in the report and the associated key.
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
	Find the maximum and associated key of a column of data.

	Args:
		report (dict): The report dictionary.
		field (str): The column looking to perform the operation on.

	Returns:
		The maximum for the requested field (column) in the report and the associated key.
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

# Set file paths for menu_data.csv and sales_data.csv
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

		# Sales Data
		# Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
		line_item_id = row[0]
		date = row[1]
		cc_number = row[2]
		quantity = int(row[3])
		sales_item = row[4]

		# If the item value not in the report, add it as a new entry with initialized metrics
		# Naming convention allows the keys to be ordered in logical fasion, count, revenue, cost, profit
		if sales_item not in report.keys():
			report[sales_item] = {
				"01-count" : 0,
				"02-revenue" : 0,
				"03-cogs" : 0,
				"04-profit" : 0
			}

		# For every row in our sales data, loop over the menu records to determine a match  
		for record in menu:

			# Menu Data
			# Item,Category,Description,Price,Cost
			item = record[0]
			category = record[1]
			description = record[2]
			price = float(record[3])
			cost = float(record[4])
			profit = (price - cost)


			# If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
			if sales_item == item:

				# Print out matching menu data 
				print(f"Does {sales_item} equal {item}? WE HAVE A MATCH!!!")
				print(f"   Item: {item}")
				print(f"   Category: {category}")
				print(f"   Price: ${price}")	
				print(f"   Cost: ${cost}")
				print(f"   Profit: ${profit}")	

				# Cumulatively add up the metrics for each item key
				report[sales_item]['01-count'] += quantity
				report[sales_item]['02-revenue'] += (price * quantity)
				report[sales_item]['03-cogs'] += cost
				report[sales_item]['04-profit'] += profit

			else:
				print("Does", sales_item, "equal", record[0], "? WA WA, NO MATCH")

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

# Find items that are performing above or below the average profitability
under_performing = []
over_performing = []

for item in report:

	if report[item]['04-profit'] < avg_field(report, '04-profit'):

		under_performing.append(item)

	elif report[item]['04-profit'] > avg_field(report, '04-profit'):

		over_performing.append(item)

print("Ramen Analysis Summary")
print("-----------------------------")
print("Most Popular:", max_field(report, '01-count'))
print("Least Popular:", min_field(report, '01-count'))
print("Most Profitable:", max_field(report, '04-profit'))
print("Least Profitable:", min_field(report, '04-profit'))
print("Overperforming Items:", over_performing)
print("Underperforming Items:", under_performing)
print()







