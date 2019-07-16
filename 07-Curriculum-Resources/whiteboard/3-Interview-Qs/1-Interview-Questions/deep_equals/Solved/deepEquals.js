'use strict';

function deepEquals (array1, array2) {
  if (array1 === array2) {
    return true;
  }
  else if (array1.length !== array2.length) {
    return false;
  }
  else {

    var equals = true;

    for (var i = 0; i < array1.length; i += 1) {
      var current_element1 = array1[i];
      var current_element2 = array2[i];

      // if both elements are arrays, check for equality recursively
      if (Array.isArray(current_element1) && Array.isArray(current_element2)) {
        equals = deepEquals(current_element1, current_element2);
      }

      // return false if any pair of elements is found not to be equal
      else if (current_element1 !== current_element2) {
        return false;
      }
    }

    return equals;
  }
}
