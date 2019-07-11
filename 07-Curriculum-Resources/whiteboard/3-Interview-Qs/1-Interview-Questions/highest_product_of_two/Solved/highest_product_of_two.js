'use strict';

function highest_product_of_two (arr) {
  var highest = highest_product_of_two = -Infinity,
      lowest = Infinity;

  for (var i = 0; i < arr.length; i += 1) {
    var current = arr[i];

    if (i >= 1) {
      var candidate = Math.max(highest * current, lowest * current);

      if (candidate > highest_product_of_two) {
        highest_product_of_two = candidate;
      }
      if (candidate < lowest) {
        lowest = candidate;
      }
    }

    if (current > highest) {
      highest = current;
    }
    if (current < lowest) {
      lowest = current;
    }
  }

  return highest_product_of_two;
}
