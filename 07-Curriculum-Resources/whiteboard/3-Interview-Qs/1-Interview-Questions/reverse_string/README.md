# Reverse String

### Problem

Write a function that returns the reverse of an input string. It should work thus:

```
reverse('foobar') // 'raboof'
```

### Notes to the Interviewer

It is correct to accomplish this using `split`, `reverse`, and `join`. If your candidate does so, however, try to hint them towards the iterative solution, as well.

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: How would you do this without calling `split`, `reverse`, or `join`?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Discusses Possibilities**.

      * Strong candidates explain that this can be done with a `for` loop that starts at the back of the string.

* **Prompt**: What are the advantages and disadvantages to each approach?

  * **Ask If**: Ask if your candidate finds both the solution using `split` and `reverse`, and the iterative solution.

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Weighs Options**.

      * The best candidates explain that the option using native methods (`split`, etc.) is _more readable_ than the `for` loop.

      * Strong candidates explain that the `for` loop is (probably) faster.

* **Prompt**: Without implementing anything, can you describe how do this without creating a new string?

  * **Ask During**: Implementation Discussion

  * **Ask If**: Ask if candidate successfully implements an iterative method with a `for` loop.

  * **Look For**:

    * **Candidate Discusses Alternative**

      * The best candidates describe their solution approach as if they had been posed a new interview problem—e.g., they restate the problem; sketch an approach; etc.

      * In this case, one could walk pointers from the front _and_ back of the word, and swap each letter "in place". This doesn't work so well in JavaScript as in, say, C, so we're less concerned with the correct answer than with the candidate's confidently discussing the problem.

### Hints

* Write down a string and do this by hand. Can you pseudocode what you just did?

### Solutions

#### Iterative Approach | O(n)

A simple solution is simply to use a `for` loop to read the input string from the back, and build a new string with each letter you find as you go. This is the [iterative solution](Solutions/iterative_solution.js).

#### Array Solution

Another solution is to use the built-in `split`, `reverse`, and `join` methods. This is the [array solution](Solutions/array_solution.js).
