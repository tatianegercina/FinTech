# BRAIN DUMP

# Students will have to somehow "join" the two following datasets to get the corresponding description and cost of each item.
# Then use the cost of each item to calculate the net profit per order.
# Lastly, students should be able to identify the following...

#   1.) The most profitable item - MAX(Profit x Quantity).
#   2.) The least profitable item - MIN(Profit x Quantity).
#   3.) The most popular item - MAX(Quantity).
#   4.) THe least popular item - MIN(Quantity).
#   3.) The average sale of each order - AVG(Order Revenue).
#   4.) The total revenue of orders - SUM(Order Profit).
#   6.) The average sale of each order per party-size

# One Order consists of multiple line items (one to many relationship)
#

#(Simplified) Income statement for Ramen Rocks, Inc. For the Year of 2018

#Revenue					352,432
#Cost of Goods Sold		     87,598
#Gross profit 			    264,834
#Operating Expenses		    123,000
#Net Profit 				141,834

#-------------------------------------------
#Product_ID | Product_Name | Description | Category | Cost
#-------------------------------------------
#1 | Takoyaki |
#2 | Dumplings |

#1 | Coca-Cola  | Drink | 0.25
#2 | Green Tea  | Drink | 0.10
#3 | Bubble Tea | Drink | 1.00


# Have students analyze customer party-size with profitability in regards to potential future expansion into a new location.
# They could analyze new rent and overhead costs.
# For example, are two-party
# Perhaps tie in some NPV type stuff!
# Assumption is made that each entree represents a customer or if no entree then at least bought one item


#-----------------------------------------------------------------
#Order_ID | Date | Credit_Card_Number | Product_ID | Category | Quantity | Price
#-----------------------------------------------------------------
#
#1 | 1/1/2018 |

#--------------------------------------------------------------------------------------------------------------------------------------------

# Menu for the ramen shop (exported to a CSV for student use)
menu = {
	"appetizers" : {
			"edamame" : {
				"description" : "boiled soybeans, maldon sea salt",
				"price" : 4,
				"cost" : 1
			},
			"house salad" : {
				"description" : "mixed greens, cherry tomatoes, cucumber, house ginger dressing",
				"price" : 4,
				"cost" : 2
			},
			"cucumber sunomono salad" : {
				"description" : "cucumber, ponzu dressing, pickled ginger sproud, sesame seeds",
				"price" : 5,
				"cost" : 2
			},
			"hiyashi wakame seaweed salad" : {
				"description" : "sweet soy-marinated wakame seaweed threads, pickled ginger sprout, sesame seeds",
				"price" : 5,
				"cost" : 2	
			},
			"agedashi tofu" : {
				"description" : "tempura battered tofu, katsuobushi, tsuyu broth, scallions",
				"price" : 5,
				"cost" : 2
			},
			"hiyayakko tofu" : {
				"description" : "chilled soft tofu, house shoyu, katsuobushi, ginger, scallions",
				"price" : 5,
				"cost" : 2
			},
			"pork floss bao" : {
				"description" : "two steamed buns, minced lean slow braised niman, ranch pork belly, cucumbers, sriracha mayo",
				"price" : 4,
				"cost" : 2
			},
			"kakuni bao" : {
				"description" : "two steamed buns, chopped fatty slow braised niman ranch pork belly, cucumbers, house bao sauce",
				"price" : 6,
				"cost" : 3
			},
			"edamame fried gyoza (vegan)" : {
				"description" : "six crispy fried edamame and cabbage pot stickers; ponzu rayu dipping sauce",
				"price" : 6,
				"cost" : 3
			},
			"fried gyoza" : {
				"description" : "six cripsy fried pork and vegetable pot stickers; ponzu rayu dipping sauce",
				"price" : 6,
				"cost" : 6
			},
			"takoyaki" : {
				"description" : "six octopus-filled fried fritters, kewpie mayo, okonomi sauce, aonori, katsuobushi, nori",
				"price" : 6,
				"cost" : 3
			},
			"rock shrimp tempura" : {
				"description" : "deep fried tempura battered rock shrimp, sriracha mayo, nisume sauce, aonori, scallions",
				"price" : 6,
				"cost" : 3
			},
			"soft-shell crab tempura" : {
				"description" : "single deep fried soft-shell crab, tsuyu dipping broth",
				"price" : 6,
				"cost" : 3
			},
			"ebi katsu shrimp bao" : {
				"description" : "two steamed buns, panko-crusted fried shrimp patties, yuzu-kosho mayo, aonori, scallions",
				"price" : 6,
				"cost" : 3
			}
	},
	"entree" : {
			"nagomi shoyu" : {
				"description" : "shoyu seasoned clear double stock (organic chick broth + house dashi); slow braised niman ranch pork belly, hanjuku tamago, nori, menma, scallions",
				"price" : 11,
				"cost" : 5
			},
			"shio ramen" : {
				"description" : "sea salt seasoned clear double stock (organic chicken broth + house dashi); slow braised niman ranch pork belly, hanjuku tamago, kikurage, nori, scallions",
				"price" : 11,
				"cost" : 5
			},
			"spicy miso ramen" : {
				"description" : "house togarashi miso blend + niman ranch pork bone stock; slow braised niman ranch pork belly, hanjuku tamago, kikurage, nori, scallions",
				"price" : 12,
				"cost" : 5
			},
			"vegetarian spicy miso" : {
				"description" : "house togarashi miso blend + vegan dashi; tempura fried tofu, sweet corn, edamame, kikurage, nori, scallions; organic soy milk upon request",
				"price" : 12,
				"cost" : 5
			},
			"miso crab ramen" : {
				"description" : "house miso crab blend + vegan dashi; slow braised niman ranch pork belly, crab meat, hanjuku tamago, kikurage, nori, scallions",
				"price" : 12,
				"cost" : 6
			},
			"soft-shell miso crab ramen" : {
				"description" : "house miso crab blend + vegan dashi; fried whole soft-shell crab, hanjuku tamago, kikurage, nori, scallions",
				"price" : 14,
				"cost" : 7
			},
			"tori paitan ramen" : {
				"description" : "rich, shoyu seasoned double stock (organic chicken broth + house dashi); slow braised niman ranch pork belly, hanuku tamago, kikurage, nori, scllaions",
				"price" : 13,
				"cost" : 6
			},
			"tonkotsu ramen" : {
				"description" : "rich, shoyi seasoned niman ranch pork bone stock; slow braised niman ranch pork belly, hanjuku tamago, kikurage, nori, spring radish, scallions",
				"price" : 13,
				"cost" : 6
			},
			"burnt garlic tonkotsu ramen" : {
				"description" : "rich, shoyi and burnt garlic seasoned niman ranch pork bone stock; slow braised niman ranch pork belly, hanjuku tamago, kikurage, sweet corn, nori, scallions",
				"price" : 14,
				"cost" : 6
			},
			"vegetarian curry + king trumpet mushroom ramen" : {
				"description" : "house curry blend + vegan dashi; fried king trumpet mushroom, tempura fried tofu, mung bean sprouts, kikurage, nori, scallions",
				"price" : 13,
				"cost" : 7
			},
			"truffle butter ramen" : {
				"description" : "rich, shoyu seasoned niman ranch prok bone stock; truffle compound butter, slow braised niman ranch pork belly, kikurage, sweet corn, nori, scallions",
				"price" : 14,
				"cost" : 7
			}
	},
	"drinks" : {
			"green tea" : {
				"description" : "green tea",
				"price" : 2.50,
				"cost" : 1,
			},
			"coke" : {
				"description" : "Coca Cola soda",
				"price" : 2,
				"cost" : 1
			}	
	},
	"desserts" : {
			"black sesame ice cream" : {
				"description" : "house-made black sesame ice cream, valrhona chocolate threads, complimentary hojicha",
				"price" : 5,
				"cost" : 2
			},
			"matcha ice cream" : {
				"description" : "house-made matcha ice cream, white chocolate pearls; complimentary hojicha",
				"price" : 5,
				"cost" : 2
			},
			"mango mochi ice cream" : {
				"description" : "two rice-cake bonbons filled with strawberry ice cream; complimentary hojicha",
				"price" : 5,
				"cost" : 2
			},
			"strawberry mochi ice cream" : {
				"description" : "two rice-cake bonbons filled with strawberry ice cream; complimentary hojicha",
				"price" : 5,
				"cost" : 2
			},
			"black sesame creme brulee": {
				"description" : "house made black sesame infused creme brulee; complimentary hojicha",
				"price" : 6,
				"cost" : 3
			}
	}
}

import numpy as np
import csv
import pandas as pd
from pandas.io.json import json_normalize

# Set date range of test data
start_date = '1/1/2017'
end_date = '1/7/2017'

# Create list of dates from start_date to end_date
date_range = pd.date_range(start_date, end_date)

# Calculate number of days
day_count = len(date_range)

# Print number of days to generate test data for
print("\nGenerating test data for", str(len(date_range)), "days...\n")



# Create a random sample of 0 (min) to n (max) customers for each day 
customers = np.random.randint(0, 100, day_count)

# Create lists from the menu items
category_list = list(menu.keys())

appetizer_list = list(menu['appetizers'].keys())
entree_list = list(menu['entree'].keys())
drink_list = list(menu['drinks'].keys())
desserts_list = list(menu['desserts'].keys())


# We assume all customers purchase an Entree, and all customers who purchase an Entree have a chance of getting an add-on item from the menu or nothing at all (as in "just water with my dinner please!").
addon_categories = list(menu.keys())

addon_categories.remove("entree")
addon_categories.append("nothing")
print(addon_categories)



# Print distribution of customers over date range
print("Number of customers over the course of", day_count, "days:\n", customers, "\n")

# Set day counter and record counter (we start rec_num = 1 so that the first record has a Line_Item_Id = 1)
day = 0
rec_num = 1

# Create an empty list to hold our test data records
record_holder = []

# Loop until we reach the last day in the date range
while day < day_count:

	print("Today is " + (date_range[day].strftime("%m-%d-%Y")))
	print("   We had " + str(customers[day]) + " customers that day.")

	customer_count = 0
	while customer_count < customers[day]: 

		# Randomize the values for the below fields
		credit_card = np.random.randint(0000000000000000, 9999999999999999, 1, dtype=np.int64)
		entree = np.random.choice(entree_list, 1)
		quantity = np.random.choice(5, 1, p=[0, 0.8, 0.1, 0.05, 0.05])

		# Assumption is made that each customer always orders at least an Entree
		record = {
			"Line_Item_ID" : rec_num,
			"Date" : date_range[day].strftime("%m-%d-%Y"),
			"Credit_Card_Number" : credit_card[0],
			"Quantity" : quantity[0],
			"Menu_Item" : entree[0]
		}
		print("      ", record)

		record_holder.append(record)

		category = np.random.choice(addon_categories, 1, p=[0.2, 0.2, 0.1, 0.5])
		
		if category[0] != "Nothing":

			rec_num += 1

			add_record = {
				"Line_Item_ID" : rec_num,
				"Date" : date_range[day].strftime("%m-%d-%Y"),
				"Credit_Card_Number" : credit_card[0],
				"Quantity" : quantity[0],
				"Menu_Item" : entree[0]
			}

			print("      ", add_record)

			record_holder.append(add_record)


		customer_count += 1
		rec_num += 1

	day += 1

	print("        We have", rec_num - 1, "records so far.")

# Set output filepath
output_file_path = "testdata_" + str(day_count) + "_days.csv"

# Set the headers for the sales test data and the menu data
sales_header = ["Line_Item_ID", "Date", "Credit_Card_Number", "Quantity", "Menu_Item"]
menu_header = ["price", "cost", "description"]

print("\nWriting data to CSV... ", output_file_path)

# Write menu data to CSV (we will have to normalize the data)
# Currently not the most elegant and will need to be more dynamic in the future
# But it solves the use case for now
try:
	menu_record_holder = []
	menu_header = ["item", "category", "description", "price", "cost"]

	with open("menu.csv", 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(menu_header)
		
		for category in menu:

			for item in menu[category]:
				
				menu_record = []

				# I swap the sequence between item and category because I want item as the first column for when the students perform a join on the item name
				menu_record.append(item)
				menu_record.append(category)
				

				for attribute in menu[category][item]:

					menu_record.append(menu[category][item][attribute])

				menu_record_holder.append(menu_record)

		# I know this is redundant but for now it helps the code to be more understandable. I generate records and put them in a holder, then iterate over the holder and write each row
		for record in menu_record_holder:
			writer.writerow(record)

except IOError:
	print("I/O Error")

# Write test data to CSV
try:
	with open(output_file_path, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=sales_header, delimiter=',')
		writer.writeheader()
		for record in record_holder:
			writer.writerow(record)
except IOError:
	print("I/O Error")





# Scrap code to be recycled


# record_holder = []




# party_list = [1,2,3,4,5,6,7,8,9,10]




# print(date_range[0].strftime("%Y-%m-%d"))


# party_size = np.random.choice(party_list, record_count, p=[0.1, 0.3, 0.1, 0.3, 0.05, 0.05, 0.025, 0.025, 0.025, 0.025])
# 
# credit_card = np.random.randint(0000000000000000, 9999999999999999, record_count)

# print(customers_per_day)

# row_num = 0
# i = 0
# j = 1
# # Loop through the desired range of record creation with (record_count + 1) to offset the range function behavior
# # where iterations go 'up to' the ending range parameter.
# while i < len(date_range):


	
# 	while j < customers_per_day[i]:



# 		print("       " + str(record))

# 		j += 1
# 	# print(customer_count)
# 	# print("About to print records " + str(row_num) + " to " + str(row_num + customer_count))
# 	# for i in range(row_num, row_num + customer_count):
# 	# 	print("RECORD", i, customer_count)
# 	i += 1
		
# 	# row_num = row_num + customer_count
# 	# print("row_num", row_num)
    

#  #    print(record['Category'])
#  #    record_holder.append(record)

# 	# #for j in range(0)


#print(record_holder)






