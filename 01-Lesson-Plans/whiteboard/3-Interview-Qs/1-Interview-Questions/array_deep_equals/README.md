# Array Deep Equals

## Problem

Suppose you have two arrays with the same contents.

```
var first = [1, 2, 3];
var second = [1, 2, 3];
```

1. What happens when you test if these arrays are equal using `==`? Using `===`? Is this what you expect?

2. Write a function that tests if the contents of two arrays are equal.

### Notes to the Interviewer

When you compare two arrays with `==` or `===`, as in `first === second`, JavaScript checks if `first` refers to the _same array_ as `second`—it does **not** check if `first` contains the same elements.

The test in this snippet evaluates to true:

```
// first and second refer to the same array...
var first = second = [1, 2, 3];

// ...So they test equal!
first === second; // true
```

...But if we want to compare the _contents_ of two arrays, we have to write our own function to do so.

### Prompts from the Interviewer

* **Prompt**: Can you explain why `first === second` returns false?

  * **Look For**

    * **Candidate Thinks Out Loud**

      * Some strong candidates will know the answer immediately.

      * Strong candidates who don't know the answer immediately will raise a few possibilities. Example good answers include:

        * `first` and `second` might refer to different objects; or

        * JavaScript somehow isn't checking the contents of `first` and `second`.

    * **Note**: Before moving on, tell the candidate that the reason `first` and `second` aren't equal is because they are different objects.

* **Prompt**: If we write a function to check when two arrays are equal, when do we want it to return `true` and `false`?

  * **Ask If**: Ask this question if your candidate has trouble restating the problem and/or making sense of how to approach it.

  * **Ask During**: Restate the Problem, Solution Sketch

  * **Look For**

    * **Candidate Explains Solution Behavior**

      * Candidates should be able to explain that a properly implemented function will return `true` if every element in the two arrays is equal, and `false` otherwise.

* **Prompt**: How would this function determine if each element in the two arrays is equal?

  * **Ask If**: Ask this question if your candidate can explain when the function should return `true`, but can't explain how it would work.

  * **Ask During**: Solution Sketch

  * **Look For**:

    * **Candidates Explain Steps**

      * Candidates should explain that the function should use a loop to check if every element in each of the two arrays is equal.

      * Strong candidates might point out that we can first check if the arrays triple-equal each other, and/or check their lengths. These are also valid steps.

* **Prompt**: Does your function work as expected if its arguments contain arrays?

  * **Ask If**: Ask this question if your candidate successfully implements a function that returns `true` when passed `first` and `second`.

  * **Ask During**: Implementation Discussion

  * **Look For**:

    * **Candidates Explain Shortcomings**

      * Solutions that use `===` to check if each element in the two arrays is equal will fail for arrays that contain other arrays.

      * Strong candidates will explain that we can solve this problem by checking if the elements we're comparing are arrays and, if so, calling our equals method recursively.

* **Prompt**: Does your function work as expected if its arguments contain objects?

  * **Ask If**: Ask this question if your candidate successfully implements a function that returns `true` when passed nested arrays.

  * **Ask During**: Implementation Discussion

  * **Look For**:

    * **Candidates Explain Shortcomings**

      * Solutions that deal with the special case of nested arrays will fail if they contain objects, for reasons similar to those that cause it to fail for nested arrays—we can't use `==` or `===` to compare objects in JavaScript.

  * **Note**

    * After your candidate explains that their function will _not_ handle objects:

      * Reassure them that they will not need to implement a function that compares objects.

      * Instruct them to "pretend" they have a function that does this, called `checkObjectEquals`, and to update their code to use it.

### Notes

Strong candidates will note that even some solutions that properly handle nested arrays and objects will fail for nested arrays that contain equal elements but in different orders. For example:

```
var first = [1, 2, 3];
var second = [2, 1, 3];

deepEquals(first, second); // false
```

This is often exactly what we want, but it's worthwhile to note this behavior explicitly.

### Solution

The solution is available in [deepEquals.js](Solved/deepEquals.js).
