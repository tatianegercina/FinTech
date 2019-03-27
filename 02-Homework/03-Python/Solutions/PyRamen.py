
# Note, this homework could also use the menu data in the form of dicts / JSON structure to keep things more dynamic (key vs. index number)
# Will students have knowledge of nested JSON objeects at this point? If so, menu hierarchy could be item = { 'category' : '<category', desc... }

import csv
import pprint as pp 
import pandas as pd


def sum_field(report, field):

	total = 0

	for key in report:

		total += report[key][field]

	#print(field, total)
def sum_field(report, field):
    total = 0
    for key in report:
        total += report[key][field]
    return total

def avg(report, field):

	total = 0

	for key in report:

		total += report[key][field]

	avg = round(total / len(report), 2)

	#print(field, avg)
	return avg

def min(report, field):

	minimum = None
	min_key = None

	for key in report:

		if minimum is None:

			minimum = report[key][field]

		elif report[key][field] < minimum:

			minimum = report[key][field]
			min_key = key

	#print(field, minimum)
	return minimum, min_key

def max(report, field):

	maximum = None
	max_key = None

	for key in report:

		if maximum is None:

			maximum = report[key][field]

		elif report[key][field] > maximum:

			maximum = report[key][field]
			max_key = key

	#print(field, maximum)
	return maximum, max_key	






menu = []

# item	category	description	price	cost
# Read in the menu data
with open("menu.csv") as menu_file:
	reader = csv.reader(menu_file)

	# Skip header of menu data
	next(reader)

	for row in reader:
		menu.append(row)

#print(menu)

# Buckets to hold our data
report = {}

# report['count'] = 0
# report['revenue'] = 0
# report['avg'] = 0
# report['max'] = 0
# report['min'] = 0

from pathlib import Path
filepath = Path('Resources/testdata_730_days.csv')

# Line_Item_ID	Date	Credit_Card_Number	Quantity	Menu_Item
# Open the csv file and load it in as a csv.reader object
with open(filepath) as csvfile:
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
				profit += (price - cost)

				print(f"Does {row[4]} equal {record[0]}? WE HAVE A MATCH!!!")
				print("Item:", item)
				print("Category:", category)
				...

				report[row[4]]['01-count'] += quantity
				report[row[4]]['02-revenue'] += (price * quantity)
				report[row[4]]['03-cogs'] += cost
				report[row[4]]['04-profit'] += profit

				print(f"Count so far: {count}")
				print("   Revenue so far: $" + str(revenue))	
				print("   Cost so far: $" + str(cost))
				print("   Net profit so far: $" + str(profit))	

			else:
				print("Does", row[4], "equal", record[0], "? WA WA, NO MATCH")

		row_count += 1

fields = ['01-count', '02-revenue', '03-cogs', '04-profit']





# Print total number of records in sales data
print("\n")
print("Total Number of Records:", row_count)
print("\n")

# Let's visualize the report so far
for key, value in report.items():
	print(key, value)


# Calculate the SUM, AVG, MAX, and MIN for each field of every item in the report
print("\n")
for field in fields:
	print(field, "SUM", sum(report, field))
	print(field, "AVG", avg(report, field))
	print(field, "MAX", max(report, field))
	print(field, "MIN", min(report, field))

print("\n")

# What item is the most popular?
# What item is the least popular?
# What item is the most profitable?
# What item is the least profitable?
# What items are underperforming?
# What items are overperforming?

under_performing = []
over_performing = []

for item in report:

	if report[item]['04-profit'] < avg(report, '04-profit'):

		under_performing.append(item)

	elif report[item]['04-profit'] > avg(report, '04-profit'):

		over_performing.append(item)

print("Most Popular:", max(report, '01-count'))
print("Least Popular:", min(report, '01-count'))
print("Most Profitable:", max(report, '04-profit'))
print("Least Profitable:", min(report, '04-profit'))
print("Overperforming Items:", over_performing)
print("Underperforming Items:", under_performing)

# Pandas makes our lives easier
print("\n")
df = pd.DataFrame(report)
df_transposed = df.T
print(df_transposed)
#print(df_transposed['01-count'].sum())








