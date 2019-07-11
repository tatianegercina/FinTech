'use strict';
def find_best_sale(prices):
    # Initialize a maximum profit
    max_profit = prices[1] - prices[2]

    # Loop through prices, beginning with the first price
    for open_price in prices:

        # Loop through every later price, and keep track of the difference
        for close_price in prices:

            # Calculate the price difference
            price_difference = close_price - open_price

            if max_profit < price_difference:
                max_profit = price_difference

    return max_profit
