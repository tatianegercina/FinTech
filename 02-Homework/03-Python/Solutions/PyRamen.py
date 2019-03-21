
# Note, this homework could also use the menu data in the form of dicts / JSON structure to keep things more dynamic (key vs. index number)
# Will students have knowledge of nested JSON objeects at this point? If so, menu hierarchy could be item = { 'category' : '<category', desc... }

import csv
import pprint as pp 

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

filepath = "testdata_7_days.csv"

# Line_Item_ID	Date	Credit_Card_Number	Quantity	Menu_Item
# Open the csv file and load it in as a csv.reader object
with open(filepath) as csvfile:
	reader = csv.reader(csvfile, delimiter=',')

	# Skip header of sales data
	next(reader)

	row_count = 0

	# Loop over every row in the csv file
	for row in reader:
		print("\n")
		print(row)

		#
		count = 0
		revenue = 0
		cogs = 0
		profit = 0

		# If the item value 
		if row[4] not in report.keys():
			report[row[4]] = {
				"count" : 0,
				"revenue" : 0,
				"cogs" : 0,
				"profit" : 0
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

				print("Does", row[4], "equal", record[0], "? WE HAVE A MATCH!!!")
				print("   Item:", item, "\n   Category:", category, "\n   Description:", description, "\n   Price:", price, "\n   Cost:", cost)

				profit += (price - cost)

				report[row[4]]['count'] += quantity
				report[row[4]]['revenue'] += (price * quantity)
				report[row[4]]['cogs'] += cost
				report[row[4]]['profit'] += profit

				print("   Count so far:", str(count))
				print("   Revenue so far: $" + str(revenue))	
				print("   Cost so far: $" + str(cost))
				print("   Net profit so far: $" + str(profit))	

			else:
				print("Does", row[4], "equal", record[0], "? WA WA, NO MATCH")

		row_count += 1

print("\n")
print("row_count ", row_count)
pp.pprint(report)











