'use strict';

function sum (x, y) {
  if (arguments.length >= 2)
    return x + y;
  else if (arguments.length === 1)
    return function (z) {
      return x + z;
    };
}
