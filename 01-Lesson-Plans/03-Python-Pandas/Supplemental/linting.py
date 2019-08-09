# Import Pandas and NumPy libraries
import pandas as pd
import numpy as np

# Creating a Pandas Series
my_list = [100, 200, 400, 600, 900]
my_series = pd.Series(my_list)
my_series

# Accessing specific values within Series
print(my_series[1])  # will print 200
print(my_series[3])  # will print 600

# Creating a Pandas DataFrame by passing in a LIST OF DICTIONARIES
# Each value in the list is a dictionary
# Imagine that each dictionary represents a row of data in our eventual dataframe
# Each dictionary should have the same keys, since these keys dictate the column headers of our dataframe
my_list = [{"id": 1, "name": "Bob", "account_balance": 500.14},
           {"id": 2, "name": "Amanda", "account_balance": 300.42},
           {"id": 3, "name": "Jill", "account_balance": 943.54},
           {"id": 4, "name": "Dylan", "account_balance": 112.53},
           {"id": 5, "name": "Alex", "account_balance": 895.51}]

my_df_1 = pd.DataFrame(my_list)
my_df_1

# Re-create the previous Pandas DataFrame, passing in a DICTIONARY WITH LISTS
# The keys of the dictionary represent the column headers of our eventual dataframe
# The lists contain the data for each column
my_dict = {"id": [1, 2, 3, 4, 5],
           "name": ["Bob", "Amanda", "Jill", "Dylan", "Alex"],
           "account_balance": [500.14, 300.42, 943.54, 112.53, 895.51]}

my_df_2 = pd.DataFrame(my_dict)
my_df_2

# Select a single column from a dataframe by passing in the column's name into square brackets
my_df_2["account_balance"]

# You can also select a single column and assign it to another variable
names_col = my_df_2["name"]
names_col

# Now names_col contains only the "names" column
print(names_col[1])

# Select multiple columns from a dataframe by passing in a list of the names of the columns
my_df_2[["name", "account_balance"]]

# Create a new DataFrame that represents purchase data from an online retailer
my_dict_2 = {"order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
             "price": [13.50, 9.99, 12.00, 29.99,
                       14.99, 7.99, 3.49, 10.00,
                       9.99, 17.99, 20.00, 21.00, 14.99],
             "purchase_category": ["Apparel", "Sports", "Toys",
                                   "Apparel", "Apparel", "Household",
                                   "Household", "Toys", "Sports",
                                   "Sports", "Apparel", "Household", "Apparel"],
             "clicked_ad": [True, True, False, True, False,
                            True, True, False, False, True,
                            True, True, False]}

purchase_df = pd.DataFrame(my_dict_2)
purchase_df

# To return ALL ROWS and COLUMN 2 (order_id)
# The colon before the comma in .iloc[] means we want ALL rows
# The 1 after the comma means we want the column at index 1
purchase_df.iloc[:, 1]

# To return ROWS 1 THROUGH 4 (including 4), and ALL COLUMNS
purchase_df.iloc[0:4, :]

# To returns ROWS 2, 3, AND 5, and COLUMNS 2 THROUGH 4 (including 4)
purchase_df.iloc[[1, 2, 4], 1:4]

# Create a new dataframe
example_dict = {"first_name": ["Bill", "James", "Tyler", "Matt", "Jon"],
                "last_name": ["Smith", "Alvarez", "Dant", "May", "Livingston"],
                "age": [25, 34, 52, 26, 43],
                "credit_score": [721, 683, 761, 641, 602]}

credit_df = pd.DataFrame(example_dict)
credit_df

# Set the row index to be the first_name
credit_df = credit_df.set_index("first_name")
credit_df

# Now, we can filter this dataframe using .loc[]
# Return data for James' and Tyler's rows, ALL COLUMNS included
credit_df.loc[["James", "Tyler"], :]

# Return rows from Bill to Matt (including Matt), and only the age and credit_score columns
credit_df.loc["Bill":"Matt", ["age", "credit_score"]]

# Return all rows, only the credit_score column
credit_df.loc[:, "credit_score"]

# Use the purchase_df dataframe created above
# Show the first 5 rows of data using .head()
# .head() is great for getting a taste of the data you're dealing with
purchase_df.head()

# Note that .describe() will only return summary statistics for your numeric columns
# In this case, statistics for order_id and price columns are returned
purchase_df.describe()

# Return the mean of the price column
purchase_df["price"].mean()

# Return the sum of all values in the order_id column
purchase_df["order_id"].sum()

# These values can also be assigned to variables
mean_price = purchase_df["price"].mean()
sum_order_id = purchase_df["order_id"].sum()

mean_price + sum_order_id

# Returns unique values in the purchase_category column
unique_pcat = purchase_df["purchase_category"].unique()
print(unique_pcat)
print(unique_pcat[2])

# Returns the value counts of each unique value in the purchase_category column
print(purchase_df["purchase_category"].value_counts())

# Create a new DataFrame that represents a dirty purchase data set from an online retailer
dirty_dict = {"order_id": [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13],
              "price": [13.50, 9.99, 12.00, 29.99,
                        14.99, 7.99, None, 10.00,
                        9.99, 17.99, 20.00, 21.00, 14.99, 14.99],
              "purchase_category": ["Apparel", "Sports", "Toys",
                                    "Apparel", "Apparel", "Household",
                                    "Household", "Toys", "Sports",
                                    "Sports", "Apparel", "Household", "Apparel", "Apparel"],
              "clicked_ad": [True, True, False, True, False,
                             True, True, False, False, True,
                             True, True, False, False]}

dirty_purchase_df = pd.DataFrame(dirty_dict)
dirty_purchase_df

# Retrieving DataFrame data types
dirty_purchase_df.dtypes

# Identifying Series count
dirty_purchase_df.count()

# Identifying frequency values
dirty_purchase_df['purchase_category'].value_counts()

# Checking for null
dirty_purchase_df.isnull()

# Determining number of nulls
dirty_purchase_df.isnull().sum()

# Determining percentage of nulls
dirty_purchase_df.isnull().mean() * 100

# Cleanse nulls from DataFrame by filling na
dirty_purchase_df['order_id'] = dirty_purchase_df['order_id'].fillna(0)
dirty_purchase_df

# Cleaning nulls from DataFrame by dropping
dirty_purchase_df.dropna(inplace=True)
dirty_purchase_df

# Confirm null records have been dropped
dirty_purchase_df.isnull().sum()

# Checking duplicates
dirty_purchase_df.duplicated()

# Cleansing duplicates
dirty_purchase_df.drop_duplicates(inplace=True)

# Converting `order_total` from `object` to `float`
dirty_purchase_df['order_id'] = dirty_purchase_df['order_id'].astype('int')
dirty_purchase_df

# Confirming conversion worked as expected
dirty_purchase_df.dtypes

import pandas as pd

# Create a dataframe to demonstrate grouping

raw_dict = {"Vehicle Type": ["Car", "Car", "SUV", "Car", "Truck", "Truck", "SUV", "Truck", "Car", "SUV", "SUV", "Truck"],
            "Manufacturer": ["Ford", "GM", "Ford", "Chevy", "Ford", "Chevy", "GM", "GM", "Ford", "Chevy", "GM", "Chevy"],
            "Owner": ["Bob", "Andrew", "Sally", "Amanda", "Bill", "Mike", "Lindsey", "Kristen", "Matt", "Anna", "Jon", "Erin"],
            "Horsepower": [265, 190, 240, 350, 365, 400, 275, 300, 185, 280, 310, 240],
            "Torque (lb-ft)": [270, 215, 203, 350, 415, 275, 290, 190, 280, 305, 250, 290],
            "Fuel Economy (mpg)": [25, 27, 22, 31, 19, 17, 23, 18, 27, 21, 19, 18]}
vehicles_df = pd.DataFrame(raw_dict)
vehicles_df

# Group vehicles_df by the "Vehicle Type" column
grouped_vehicles_df = vehicles_df.groupby("Vehicle Type")

# Note that the "GroupBy" object by itself is not particularly useful
print(grouped_vehicles_df)

# Use the `count` function to count the number of values from each column for each grouped `Vehicle Type`.
grouped_vehicles_df.count()

# Use the `mean` function to calculate the mean from the values of `Fuel Economy (mpg)` for each grouped `Vehicle Type`.
grouped_vehicles_df["Fuel Economy (mpg)"].mean()

# Use the `max` function to calculate the max from each column and use the `loc` function to filter and return the max values from columns `Horsepower` to `Torque (lb-ft).
grouped_vehicles_df.max().loc[:, "Horsepower":"Torque (lb-ft)"]

# Use the `min` function to calculate the min from each column and use the `loc` function to filter and return the max values from columns `Horsepower` to `Torque (lb-ft).
min_power_tq = grouped_vehicles_df.min().loc[:, "Horsepower":"Torque (lb-ft)"]
min_power_tq

# Proving that the result of running data functions on "GroupBy" objects is a dataframe
type(min_power_tq)

# Group vehicles_df by both Manufacturer AND Vehicle Type
grouped_vehicles_df_2 = vehicles_df.groupby(["Manufacturer", "Vehicle Type"])

# Get averages
grouped_vehicles_df_2.mean()

# First, let's see what the unaltered vehicles_df looks like
vehicles_df

# Now, let's sort this dataframe by the "Fuel Economy (mpg)" column
vehicles_df.sort_values("Fuel Economy (mpg)")

# Sort DESCENDING by the "Fuel Economy (mpg)" column
vehicles_df.sort_values("Fuel Economy (mpg)", ascending=False)

# Creating a new dataframe from the result of running .sort_values()
sorted_df = vehicles_df.sort_values("Fuel Economy (mpg)")
sorted_df.head()

# Run the .reset_index() on the sorted dataframe
# Pass in drop=True to prevent appending a new column with the old indexes to the dataframe
sorted_df = sorted_df.reset_index(drop=True)
sorted_df.head()

# Create the dataframe containing purchase data
purchase_dict = {"Customer ID": [123, 757, 985, 907, 642, 754, 396, 278],
                 "Order Price": [9.99, 15.00, 7.99, 25.00, 18.00, 31.00, 29.99, 17.99],
                 "Category": ["Clothes", "Electronics", "Toys", "Toys", "Clothes", "Toys", "Electronics", "Clothes"]}

purchase_df = pd.DataFrame(purchase_dict)
purchase_df

# Create the dataframe containing email list data
email_dict = {"Customer ID": [123, 147, 278, 396, 421, 642, 754],
              "Name": ["Jill", "Tony", "Sarah", "Bill", "Erin", "Tyler", "Amanda"],
              "Email Address": ["jill29@gmail.com", "tony@yahoo.com", "sarah.b@gmail.com", "bill93@gmail.com", "erinm@yahoo.com", "tyler@aol.com", "amanda72@gmail.com"]}

email_df = pd.DataFrame(email_dict)
email_df

# Concatenate the `purchase_df` with the `email_df` by row axis and perform an inner join
inner_row_concat_df = pd.concat([purchase_df, email_df], axis="rows", join="inner")
inner_row_concat_df

# Concatenate the `purchase_df` with the `email_df` by row axis and perform an outer join
outer_row_concat_df = pd.concat([purchase_df, email_df], axis="rows", join="outer", sort=False)
outer_row_concat_df

# Concatenate the `purchase_df` with the `email_df` by column axis and perform an inner join
inner_column_concat_df = pd.concat([purchase_df, email_df], axis="columns", join="inner")
inner_column_concat_df

# Concatenate the `purchase_df` with the `email_df` by column axis and perform an outer join
outer_column_concat_df = pd.concat([purchase_df, email_df], axis="columns", join="outer")
outer_column_concat_df

# First, call vehicles_df to examine it
vehicles_df

# Create bins and bin labels for the Horsepower column
hp_bins = [180, 200, 350, 400]
hp_labels = ["Slow", "Decent", "Fast"]

# Bin the Horsepower column
# cut() returns a Pandas Series containing each of the binned column's values translated into their corresponding bins
pd.cut(vehicles_df["Horsepower"], hp_bins, labels=hp_labels)

# We can append our bins to vehicles_df
vehicles_df["Speed"] = pd.cut(vehicles_df["Horsepower"], hp_bins, labels=hp_labels)
vehicles_df

# Binning adds a new wrinkle to our data, allowing for more vigorous analysis
# For example, we can now group by our bins
grouped_speed_vehicles_df = vehicles_df.groupby("Speed")
grouped_speed_vehicles_df[["Horsepower", "Torque (lb-ft)"]].mean()

# Import external library
from pathlib import Path

# Use the pathlib library to set the Path
sp500_csv_path = Path("Resources/sp500.csv")

# Read CSV without setting a header
sp500_df = pd.read_csv(sp500_csv_path, header=None)
sp500_df.head()

# Read CSV and set the header
sp500_df = pd.read_csv(sp500_csv_path)
sp500_df.head()

# Read CSV and set formatted `Date` column as index
sp500_df = pd.read_csv(sp500_csv_path, index_col="Date", infer_datetime_format=True, parse_dates=True)
sp500_df.head()

# The `pct_change` function easily calculates daily returns for a DataFrame
sp500_daily_returns = sp500_df.pct_change()
sp500_daily_returns.head()

# The `cum_prod` function cumulatively multiplies each preceding number by the next until the end of the series of data points
# Doing so allows us to calculate the cumulative returns from the daily returns
sp500_cumulative_returns = (1 + sp500_daily_returns).cumprod() - 1
sp500_cumulative_returns.head()

# Enable the matplotlib property to allow diagrams to display in Jupyter Notebook
%matplotlib inline

# Plot the S&P 500 daily returns and set the figure size
sp500_daily_returns.plot(figsize=(10, 5))

# Plot the S&P 500 cumulative returns
sp500_cumulative_returns.plot()

# Daily Standard Deviations
sp500_daily_std = sp500_daily_returns.std()
sp500_daily_std.head()

# Calculate the annualized standard deviation (252 trading days)
sp500_annualized_std = sp500_daily_std * np.sqrt(252)
sp500_annualized_std.head()

# Calculate the annualized sharpe ratio
sp500_sharpe_ratio = sp500_daily_returns.mean() * 252 / (sp500_daily_returns.std() * np.sqrt(252))
sp500_sharpe_ratio

# Calculate the a rolling 180-day rolling mean or moving average
sp500_df.rolling(window=180).mean().plot()

# Calculate the a rolling 180-day rolling standard deviation
sp500_df.rolling(window=180).std().plot()

# Set figure of the daily closing prices of Tesla
ax = sp500_df.plot()

# Plot 180-Day Rolling Mean on the same figure
sp500_df.rolling(window=180).mean().plot(ax=ax)

# Set the legend of the figure
ax.legend(["SP500", "SP500 30 Day Mean"])

# Read in another CSV
amd_csv_path = Path("Resources/amd.csv")
amd_df = pd.read_csv(amd_csv_path, index_col="Date", infer_datetime_format=True, parse_dates=True)

# Use the `concat` function to combine the two DataFrames by matching indexes (or in this case `Month`)
combined_df = pd.concat([amd_df, sp500_df], axis="columns", join="inner")

# Rename columns
combined_df.columns = ['AMD', 'SP500']
combined_df.head()

# Use the `corr` function to calculate correlations
correlation = combined_df.corr()

# Use the `pct_change` function to calculate daily returns of closing prices for each column
combined_daily_returns = combined_df.pct_change()
combined_daily_returns.head()

# Calculate covariance of all daily returns of AMD vs. S&P 500
covariance = combined_daily_returns['AMD'].cov(combined_daily_returns['SP500'])
covariance

# Calculate variance of all daily returns of AMD vs. S&P 500
variance = combined_daily_returns['SP500'].var()
variance

# Calculate beta of all daily returns of AMD
amd_beta = covariance / variance
amd_beta

# Calculate Portfolio Returns with an equal amount of each stock
weights = [0.5, 0.5]

portfolio_returns = combined_daily_returns.dot(weights)
portfolio_returns.head()

# Use the `plot` function to visualize daily portfolio returns
portfolio_returns.plot()

# Use the `cumprod` function to generate cumulative portfolio returns from daily portfolio returns
cumulative_portfolio_returns = (1 + portfolio_returns).cumprod() - 1
cumulative_portfolio_returns.head()

# Use the `plot` function to visualize daily portfolio returns
cumulative_portfolio_returns.plot()
