'use strict';

function reverse (str) {
  var reversed = "";

  for (var i = str.length; i > 0; i -= 1) {
    reversed += str[i - 1];
  }

  return reversed;
}
