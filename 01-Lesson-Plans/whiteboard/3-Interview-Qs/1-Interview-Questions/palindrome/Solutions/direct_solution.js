'use strict';

function isPalindrome (string) {
    return string.split('').reverse().join('') === string;
}