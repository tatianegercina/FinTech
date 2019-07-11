'use strict';

function palindrome (str) {
  // Palindromes with an odd number of letters eventually recurse on
  // a string of length 1. Palindromes with an even number of lettrs
  // eventually recurse on a string of length 0.
  if (str.length === 1 || str.length === 0)
    return true;
  else if (str[0] === str[str.length - 1])
    return palindrome(str.slice(1, str.length - 1));
  else
    return false;
}
