'use strict';

function is_palindrome (str) {
  // Get the front of the word
  var front = str.split('')
                .splice(0, str.length / 2)
                .join(''),

  // Get the back of the word, and reverse it
  // for comparison to the front.
  back = str.split('')
           .slice(Math.ceil(str.length / 2), str.length)
           .reverse()
           .join('');

  console.log(front, back);
  return front === back;
}
