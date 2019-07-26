def calculate_best_trade(prices):

    # Initialize desired number of shares
    num_shares = 10000

    # Initialize time interval
    time_interval = 5

    # Initialize the low and high prices
    min_price = 0
    max_price = 0

    # Initialize index variables
    index = 0
    min_price_index = 0
    max_price_index = 0

    # Iterate over each price in the prices list
    for price in prices:

        # Check to see if current prices is the first entry
        # If so, set the min and max prices and indexes as the first entry
        if min_price == 0 and max_price == 0:
            min_price = price
            max_price = price
            min_price_index = index
            max_price_index = index
        # Check if price is less than the min price
        # If so, set the min price and index to the current price
        elif price < min_price:
            min_price = price
            min_price_index = index
        # Check if price is greater than the max price
        # If so, set the max price and index to the current price
        elif price > max_price:
            max_price = price
            max_price_index = index

        # Iterate the index by 1 in preparation for the next loop
        index += 1

    # Calculate the profit of the trade and round to two decimal places
    profit = round((max_price - min_price) * num_shares, 2)

    # Calculate the duration of the trade
    duration = (max_price_index - min_price_index) * time_interval

    # Return both variables
    return profit, duration

# List of stock prices for IAG between 10 AM and 11 AM (5 minute interval)
prices = [1.42, 1.32, 1.45, 1.20, 1.34, 1.74, 1.10, 1.89, 1.42, 1.90, 1.80, 1.85]

# Call the function
best_profit, duration = calculate_best_trade(prices)

# Print the results of the function
print(f"The best profit is ${best_profit}, which took approximately {duration} minutes.")
