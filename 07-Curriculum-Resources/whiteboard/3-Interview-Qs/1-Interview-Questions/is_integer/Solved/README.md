# Solution Sketch

The below pseudocode expresses a robust algorithm for determining if an input is an integer and, if so, returning the integer itself. It's acceptale if your candidates solution looks more like English than this, as long as it expresses similar logic.

Note that we've "used" many functions that we haven't written. Since we're _designing_ a solution, this is okay—we want to express what a solution _must_ do. We can worry about the details of actually doing it later.

```
function isInteger argument
  if (argument is a number) {
    var decimal = check_if_argument_has_decimal_points(argument)

    if (decimal) {
      return false
    }
    else {
      return true
    }
  }

  if (argument is not a string) {
    return false
  }

  if (argument is a string) {
    var invalid = check_if_argument_has_letters_or_punctuation(argument)

    if (invalid) {
      return false
    } else {
      var valid = check_if_argument_contains_numbers(argument)

      if (valid) {
        return as number(argument)
      }
    }
  }
```
