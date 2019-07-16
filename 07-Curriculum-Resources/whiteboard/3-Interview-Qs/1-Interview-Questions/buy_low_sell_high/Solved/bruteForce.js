'use strict';

function findBestSale (array) {
  // Initialize a maximum profit
  var max_profit = array[1] - array[0];

  // Loop through array, beginning with first price
  for (var i = 0; i < array.length; i += 1) {

    // Loop through every later price, and keep track of the maximum
    for (var j = i; j < array.length; j += 1) {
      var candidate_price = array[j] - array[i];

      if (max_profit < candidate_price) {
        max_profit = candidate_price;
      }
    }
  }

  // Return the maximum profit we've found so far
  return max_profit;
}