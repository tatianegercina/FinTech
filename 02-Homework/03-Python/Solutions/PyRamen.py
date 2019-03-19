import csv

print("\n")

# Read in the menu data
with open("menu.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',')

	for row in reader:
		print(row)


print("\n")

# Read in the sales data
with open("testdata_7_days.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',')

	for row in reader:
		print(row)





