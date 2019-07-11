# Curried Sum

## Problem

Write a function that adds two numbers, and can be called either of two ways:

```
sum(2, 3); // 5
sum(2)(3); // 5
```

### Notes to the Interviewer

Most candidates probably aren't familiar with the machinery required to solve this problem. This is intentional—the purpose of this problem is not to test your candidate's familiarity with javaSCript, but rather to test how well they can explain the problem and use hints from the interviewer.

Many students won't make it through the entire problem. **This is okay**. Again, the most important piece is that they are able to think through and explain the problem, and discuss it with the interviewer. This problem is specifically designed to force students to work with their interviewer on a problem whose solution they probably can't implement, but which they can probably solve conceptually if they stay calm and communicate with the interviewer.

Make sure you don't allow the student to begin implementing the solution until they've explained at least the first three prompts—in particular, until they've articulated the following points:

1. `sum` either returns a result immediately, or returns a function;
2. `sum` decides which of these to do by checking if it got two arguments, as in `sum(2, 3)`, or one argument, as in `sum(2)`.
3. When we call it like `sum(2)`, `sum` returns a function that "remembers" the `2`.

### Prompts from the Interviewer

Most students are likely to need at least one hint from the interviewer to solve this problem.

* **Prompt**: Can you explain what this function does if we pass two arguments "normally"? That is, if we call it like `sum(2, 3)`?

  * **Ask During**: Restate the Problem

  * **Look For**

    * **Candidate Discusses Possibilities**. As examples, you could throw an error; return "No Profit"; or report the minimum loss (best approach).

      * The best candidates will discuss multiple possibilities; explain one; and explain their choice.

      * Such a discussion and explanation is better than immediately stumbling on the best approach.

* **Prompt**: Can you explain what's happening if we pass arguments the second way? that is, if we call it like `sum(2)(3)`?

  * **Ask During**: Restate the Problem

  * **Look For**

    * **Candidate Reasons Through Syntax**. The best candidates will see that the second set of parentheses—in this case, the `(3)`—indicates a function call.

      * Once they've gotten this far, you are free to confirm the answer for the candidate: "When we call it the second way, `sum` returns a function, which we call with `3`."

  * **Hints**

    * Imagine we could do: `var y = sum(2)`. Then, `sum(2)(3)` is the same as `y(3)`. What's happening when we write `y(3)`?

      * The correct response is: We're calling `y` as a function.

      * **Follow-Up**. If we're calling `y` as a function, and `y = sum92)`, what does `sum(2)` do?

* **Prompt**: How does `sum` know whether to return a result immediately—as in `sum(2, 3)`—or to return a function—as with `sum(2)`?

  * **Ask During**: Restate the Problem

  * **Look For**

    * **Candidate Explains Behavior**. The best candidates will explain that `sum` returns directly when we pass two arguments, and returns a function when we pass only `1`.

      * Once the candidate has gotten this far, you should ask if they know how to check how many arguments a function has received. If not, let them know that it's okay, and you'll tell them how once they begin to implement the solution.

* **Prompt**: You've explained everything you need to solve the problem. Using what you've explained, how would you pseudo-code a solution?

  * **Ask During**: Solution Sketch

  * **Look For**

    * **Candidate Sketches Conceptual Solution**. Good candidates will be able to produce pseudo-code that solves the problem at a high level. It would look something like:


```
function sum first_numner, second_number
  if (sum received two arguments)
    return first_number + second_number
  else if (sum received one argument)
    return function that takes a second number, and adds it to the first_number
```

* **Prompt**: Your pseudocode is correct. I'll help you with the implementation details, since your conceptual solution is spot-on. Which parts do you not know how to translate to JavaScript?

  * **Ask During**: Implementation

  * **Look For**

    * **Candidate Specifically Identifies Required Input**. The best candidates will be able to identify and articulate what they don't know. For example, "I don't know how to check how many arguments I've received", or, "I understand why I need to return a function, but don't know how to write it.

      * Most students will need help counting arguments and implementing the function in the `else if` branch.

        * `arguments`: Explain that all functions have a variable called `arguments`, which is like an array. Explain that `arguments.length` tells us how many arguments we passed the function.

        * `function (second_number)`: Explain that, when we write the function to return, we want to write it so that it accepts a number, and adds it to the `first_number` we received.

          * Explain that we can still see `first_number` inside of this function. This is the crucial point.

  * **Notes**: If your candidate makes it this far but chokes on implementation, they've still done quite well, and still earns a 3 for all fields on the rubric except for implementation and implementation discussion.

### Solutions

The [solution for this exercise is actually rather short](Solved/sum.js). Encourage your candidate to study how functions can return other functions—this is an advanced but extremely important feature of JavaScript.
