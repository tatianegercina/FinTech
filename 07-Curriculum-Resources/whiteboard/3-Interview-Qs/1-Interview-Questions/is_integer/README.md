# isInteger

### Problem

Sketch and, if time allows, implement a robust function that checks if a given string input is an integer and, if possible, parses it.

By _robust_, we mean that your function should intelligently handle common error cases, such as the user passing completely invalid string arguments (`"not a number at all"`); values that aren't integers (`"-Infinity"`); and such.

You are encoruaged to spend most of your time for this problem planning your solution, accounting for edge cases, etc. A strong understanding of the solution and thorough pseudocode is worth more than a correct implementation for this problem.

Don't use `parseInt`.

### Notes to the Interviewer

If your candidate gets stuck, remind them that this problem is chiefly about _designing_ a solution that works, not implementing one. Let them know that they're allowed to "do" things that they might not know how to actually code—such as "check if there are periods in the string"—and that they should be creative _without_ necessarily thinking about the code.

### Prompts from the Interviewer

* **Prompt**: Start by defining what an integer is. What kinds of numbers _aren't_ integers? What other kinds of input aren't integers?

  * **Follow-Up**: How should your code deal with those inputs?

  * **Ask During**: Solution Sketch

  * **Ask If**: Ask this question to candidates who have trouble getting started on the question on their own.

  * **Look For**

    * **Candidate Answers Prompt**

      * Candidates should explain that an integer is a positive or negative whole number, like `1` or `0`, but _not_ like `3.14` or `2.718`.

      * Candidates should explain that other inputs—strings, arrays, objects, etc.—should cause the function to return `false`.

* **Prompt**: What do you think your function should do if your user passes something that is obviously not an integer, like `"Starbucks"`?

  * **Ask During**: Solution Sketch

  * **Candidate Suggests Alternatives**

    * THe most sensible behavior would be to return `false` or throw an error.

    * In this case, it makes the most sense for us to return `false`.

    * Rate your candidate's performance on this prompt based on whether they make more than one suggestion, and ask the Interviewer which they'd prefer.

* **Prompt**: Think of the different kinds of inputs that aren't integers. How can you tell they aren't integers? Don't worry about what you know how to code; just focus on solving the problem.

  * **Follow-Up**: Feel free to explain your solution in plain English—"check if the input is X or Y" is acceptable.

  * **Ask During**: Solution Sketch

  * **Candidate Explains Solution**

    * There are many legitimate answers to this question. common and easy-to-understand approaches include:

      * First, check if the input is a string. If not, return `false`.

      * Next, check if the string contains any punctuation or letters. If so, return `false`.

      * Finally, make sure the string contains numbers. If so, return the string as a number.

* **Prompt**. What should your function do if the user passes an integer, like `12`? Does your function do this?

  * **Ask During**: Solution Sketch

  * **Candidate Explains Shortcomings**

    * Some canidates will propose solutions that do in fact solve this problem.

    * The solution above, however, does _not_ behave properly for integer inputs. We would have to add a step:

      * First, check if the number contains any decimals.

        * If so, return false. Otherwise, return the number.

### Notes

Note that students are _not_ graded on their implementation. Rather, they are graded on their ability to think through the problem and its edge cases, and come up with pseudo-code—or even more generally, a solution sketch—that solves the problem.

### Solution

An example sketch is available in the [solution sketch README](Solved/README.md). An example imlementation is available in [isInteger.js](Solved/isInteger.js).
