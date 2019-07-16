# Global var

### Problem

Consider the following snippet of JavaScript.

```
for (var i = 0; i < 5; i += 1) {
  setTimeout(function () {
      console.log(i);
    }, i * 1000);
}
```

1. What do you expect this code to do?

2. What will this log, and why?

3. How can you "fix" this code, if you expected it to behave differently than it did?

### Notes to the Interviewer

Candidates are _not_ allowed to run this code immediately. They must first state what they believe the code will log; justify their belief; and only proceed to the console after the interviewer gives the go-ahead.

The strongest candidates will immediately give the correct answer and explanation. Good candidates will give an incorrect answer at first, but be able to explain the code's behavior after running it. Failing to properly explain the behavior even after executing the snippet, or having to execute the snippet prior to being able to formulate an answer, indicates that the candidate must review [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope) and [hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting).

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: How can you get this code to behave as you would expect it to?

  * **Ask If**

    * Ask if the student states that the code looks like it should print `1, 2, 3, 4, 5` after `1, 2, 3, 4, 5` seconds, respectively.

    * If the student immediately explains what the code will _actually_ do, ask how they would make it print the numbers 1 - 5.

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Identifies Possibilities**.

      * Strong candidates will explain that we can achieve the "expected" behavior by using an IIFE (see soltion).

      * Strong candidates with exposure to ES6 will explain that we can achieve the "expected" behavior by using `let` in place of `var` in the `for` loop. It is acceptable if candidates do not identify this possibility.

### Hints

* What is the value of `i` when the callbacks to `setTimeout` run?

### Solutions

#### Use `let`

The [simplest solution](Solved/let_solution.js) leverages the `let` keyword from ES6.

#### IIFE

The [classical solution](Solved/closure_solution.js) uses an IIFE to bind the value of `i` on each iteration to each callback's closure.

- - -
