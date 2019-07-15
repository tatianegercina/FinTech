'use strict';

function rmax (list, max) {
  // if this is the first function call, set max = list[0]
  if (max === undefined)
    max = list[0];

  console.log(`Current list: [${list}]`)
  console.log(`Current max: ${max}`)
  // Grab the next element to compare to
  var next = list[0];

  // Save maximum-seen-so-far
  if (list.length === 0) {
    console.log('list.length is 0! Returning largest element found so far.')
    return max;
  }
  else if (next > max) {
    max = next;
  }

  // Return the result of calling rmax on the REST of the array!
  return rmax (list.slice(1), max);
}
