'use strict';

function pig_latinize_word (word) {
  return word.slice(1) + word[0] + "ay";
}

function pig_latinize (sentence) {
  var words = sentence.split(' '),
    sentence = [];

  for (var i = 0; i < words.length; i += 1) {
    sentence.push(pig_latinize_word(words[i]));
  }

  return sentence.join(' ');
}

/*******************************************************************************
 * The below details are not necessary for this problem's solution, but are
 * included for completeness.
/******************************************************************************/

function pig_latinize_text (text) {
  return text.split(' ').map(pig_latinize_word_and_preserve_extras).join(' ');
}

/**
 * This version of pig_latinize_word properly handles caps and punctuation.
 */

function pig_latinize_word_and_preserve_extras (word) {
  return preserve_caps(pig_latinize_word_and_preserve_punctuation(word));
}

function pig_latinize_word_and_preserve_punctuation (word) {
  return shift(word.slice(1) + word[0] + "ay");
}

/******************************************************************************/

function was_capitalized (word) {
  return /[A-Z]/.test(word);
}

function preserve_caps (word) {
  if (was_capitalized(word)) {
    word = word.toLowerCase();

    return word[0].toUpperCase() + word.slice(1);
  }
  else {
    return word;
  }
}

/******************************************************************************/

/**
 * Puts punctuation marks in the right place.
 */
function splice (word, index) {
  var beginning = word.slice(0, index);
  var rest = word.slice(index + 1, word.length);

  return beginning + rest + word[index];
}

/**
 * Makes sure final punctuation appears in the right place.
 */
function shift (word) {
  var occurrence = word.search(/[,;:!.?]/);

  if (occurrence === -1) {
    return word;
  }
  else {
    return splice(word, occurrence);
  }
}
