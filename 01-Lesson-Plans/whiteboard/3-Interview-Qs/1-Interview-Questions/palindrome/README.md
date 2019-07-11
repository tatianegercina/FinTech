# Palindrome

### Problem

Write a function that determines if its string argument is a palindrome.

### Notes to the Interviewer

Remember—you are concerned more with the candidate's ability to _communicate_ their approach than with the correctness of their solution. For the purposes of this exercise, both provided solutions are equally acceptable.

If your candidate finds a solution quickly, make them work towards one of the solutions that they did _not_ discover.

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Are there any disadvantages to recursion?

  * **Ask If**: Only ask this question if the candidate implements a recursive function.

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Explains Shortcomings**. There is an upper limit on how many recursive calls JavaScript can handle. Calling a recursive function on a large enough string will break your code.

      * The best candidates will acknowledge this, and explain that such a string is unlikely in the "real world".

      * Some candidates will explain that this is not an issue with ES6.

      * Either response is acceptable.

      * Many candidates will not know of JavaScript's recursion ceiling. Take the opportunity to inform them.

* **Prompt**: Is this the only solution?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Discusses Alternatives**. Strong candidates will identify multiple solution approaches, but it's okay if they don't see more than one.

      * What you want to see is that the candidate **explains alternative approaches**, or **justifies why no alternative exists**.

### Hints

* Write down a palindrome. Can you point out which parts are equal?

  * **Follow-Up**. How would you check if those parts are equal?

* Can you think of a way to check if the front of the word is equal to the back of the word?

  * This is a fairly revealing hint. Only provide it if necessary.

### Solutions

#### Direct Solution

The simplest solution is simply to use the definition of a palindrome: If a string is equal to its reverse, return true. Otherwise, return false.

```
function palindrome (str) {
  if (str == str.split('').reverse().join(''))
    return true;
  else
    return false;
}
```

#### Array Solution

Another, less elegant, solution is to check that the first half of a string is equal to the reverse of the second half. In other words, `abba` is a palindrome because the first half, `ab`, is equal to the second half, `ba`, in _reverse_: `ab`. This is the [split solution](Solutions/split_solution.js).

#### Recursive Solution

A final solution is to check that the input string satisfies the basic property of a palindrome—that its first letter is equal to its last letter—and, if so, recursively check that the same is true for the substring that remaisn after removing the first and last letters. This is the [recursive solution](Solutions/recursive_solution.js).
