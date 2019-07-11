# Counting Letters

## Problem

Write a function that counts how many times each letter in a string occurs.

For example:

```
var letter_counts = count_letters("Example sentence");

console.log(letter_counts['e']); // 5
```

Your function should be case-insensitive. In other words, 'E' and 'e' should both increment the count for the letter 'e'.

### Notes to the Interviewer

There are multiple solutions to this problem, but we are particularly interested in students identifying **objects** as the appropriate datatype for this problem.

### Prompts from the Interviewer

* **Prompt**: Is your function case-insensitive? That is, does it treat 'E' and 'e' the same way?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Discusses Possibilities**

      * Candidates should identify whether their function appropriately deals with capitalization.

        * Most commonly, this entails calling `toLowerCase` on the sentence.

* **Prompt**: Consider the example snippet, where we run the `count_letters` function on `"Example sentence"`. What happens if we write `letter_counts['z']`?

  * **Follow-Up**: How should your function deal with this?

  * **Ask During**: Implementation Discussion

  * **Look For**

    * **Candidate Explains Implementation**

      * Candidates should accurately explain how their solution behaves in this case.

    * **Candidate Discusses Alternatives**

      * If you ask the follow-up question, candidates should suggest different ways to deal with cases like this.

        * Strong interviewers will explain different approaches and then ask the interviewer for input.

      * Reasonable answers include simply returning `undefined`, or modifying the function so as to return `0`.

### Solution

One solution for this exercise is available in [count_letters.js](Solved/count_letters.js).
