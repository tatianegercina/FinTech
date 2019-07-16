'use strict';

function maximin (arr) {
  var minimum = maximum = arr[0];

  for (var i = 0; i < arr.length; i += 1) {
    var candidate = arr[i];

    if (candidate > maximum)
      maximum = candidate;
    if (candidate < minimum)
      minimum = candidate;
  }

  return [minimum, maximum];
}
