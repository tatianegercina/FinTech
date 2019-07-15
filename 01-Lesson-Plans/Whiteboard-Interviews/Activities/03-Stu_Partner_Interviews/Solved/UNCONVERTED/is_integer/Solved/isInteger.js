// Remember--the goal is to design a robust solution, not necessarily implement
// one. Don't worry if the regex is new. what matters is that your design
// includes much of what is explained in the comments.
function isInteger(argument) {
  // First, check if the argument is an integer.
  if (typeof argument === "number") {
    return isInteger(String(argument));
  }

  // Then, verify that the argument is a string
  if (!(typeof argument === "string")) {
    return false;
  }

  // Next, we'll check if there are letters or common punctuation in the input.
  // Return false if so, because such an input can't be an integer.
  // You can read more about Regex Patterns later https://www.regexbuddy.com/regex.html
  if (/([a-zA-z]|[.,()[!?&\]:;])/.test(argument)) {
    return false;
  }

  // Otherwise, make sure it contains numbers, and cast it to Number.
  // You can read more about RegEx Patterns here https://www.regexbuddy.com/regex.html
  if (/\d/.test(argument)) {
    return Number(argument);
  }
}
