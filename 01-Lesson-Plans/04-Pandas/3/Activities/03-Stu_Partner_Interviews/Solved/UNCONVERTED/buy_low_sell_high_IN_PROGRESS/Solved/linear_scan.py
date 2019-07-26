def find_best_sale(prices):

    if list_param.length < 2:
        print("Cannot buy and sell with less than two prices.")

    # Initialize the low and high prices
    lowest_price = 0
    highest_price = 0

    # Iterate over each price in the prices list
    for price in prices:

        #
        if lowest_price == 0 and highest_price == 0:
            lowest_price = price
            highest_price = price
        elif






function findBestSale (array) {
  if (array.length < 2)
    throw Error ("Can't buy/sell in one minute.");

  var max_profit = array[1] - array[0],
    lowest_price = array[0];

  for (var i = 1; i < array.length; i += 1) {
    if (array[i] - lowest_price > max_profit) {
      max_profit = array[i] - lowest_price;
    }
    else if (array[i] < lowest_price) {
      lowest_price = array[i];
    }
  }

  return max_profit;
}
