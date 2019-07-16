# SumPair

## Problem

Given two input values:

* An array of integers of finite length, sorted in ascending order, of which numbers can repeat,
* A sum which is an integer number greater than 0

Find the first 2 values in the array which added to each other would equal to the sum given.

**Bonus**: 
  Find all the pairs in the array which added to each other would equal to the sum given.

## Example 

Given the values:

```js
const input = [1, 2, 3, 4, 5, 6];
const result = 8;
```

The first pair `2` + `6` will satisfy the result `8`.

For the bonus question, pairs `2` + `6` and `3` + `5` will satisfy the result.

### Notes to the Interviewer

There are multiple solutions to this problem, but we are particularly interested in students solve this problem using only one loop and optimise the code with performance in mind.

What happens if there are 2 sets of numbers that satisfy the result? Finding the first match would be sufficient for this problem. You can have the student brainstorm about what needs to be done to find all the matches (bonus question).

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Does the order in given input array matter?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Explains Solution**. It does not matter, The candidate should be able to reason through why, if you raise this during the Sketch phase, or explain the error in their code, if you raise it during the Discussion phase.

### Solution

The solution for this exercise is available in [sumPair.js](Solved/sumPair.js).
