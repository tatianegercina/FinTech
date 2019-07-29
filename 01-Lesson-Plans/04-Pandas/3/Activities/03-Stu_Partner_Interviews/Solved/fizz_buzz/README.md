# FizzBuzz

Write a script that prints the numbers 1 to 100 in the console. But for multiples of three, print `Fizz` and for multiples of five, print `Buzz`. For numbers which are multiples of both three and five, print `FizzBuzz`.

## Notes to the Interviewer

This is a common screening question. There is no need to drill your candidate on details with this problem.

## Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Does the order in which we check if our number is a multiple of 3, 5, or both matter?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For:**

    * **Candidate Explains Solution**

      * It does matter, The candidate should be able to reason through why, if you raise this during the Sketch phase, or explain the error in their code, if you raise it during the Discussion phase.

## Hints

Remember the Python `%` modulo operator!

## Solution

### Modulo If-Else Statements

The solution is simply to check that the current number is a multiple of both 3 and 5; then check whether the number is a multiple of 3; then check whether the number is a multiple of 5; and then just print the number if all else is false.
