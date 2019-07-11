'use strict';

function find_most_frequent_element (arr) {
  var occurrences = count_occurrences(arr);

  var highest_frequency = get_highest_frequency(occurrences);

  return collect_most_frequent_elements(occurrences, highest_frequency);
}

// Collect every item in the input array that appears with highest_frequency.
// There might be more than one--consider: [1, 2, 2, 3, 3]
function collect_most_frequent_elements (occurrences, highest_frequency) {
  var most_frequent_elements = [],
    entries = Object.entries(occurrences);

  for (var i = 0; i < entries.length; i += 1) {
    if (entries[i][1] == highest_frequency)
      most_frequent_elements.push(entries[i][0]);
  }

  return most_frequent_elements;
}

// Create an object that counts how many times each element in the input array
// appears
function count_occurrences (arr) {
  var obj = {};

  for (var i = 0; i < arr.length; i += 1) {
    var key = String(arr[i]);

    if (!(obj[key]))
      obj[key] = 1;
    else
      obj[key] += 1;
  }

  return obj;
}

// Get largest number of times an item appeared in the input array
function get_highest_frequency (occurrences) {
  return Math.max(...Object.values(occurrences));
}
