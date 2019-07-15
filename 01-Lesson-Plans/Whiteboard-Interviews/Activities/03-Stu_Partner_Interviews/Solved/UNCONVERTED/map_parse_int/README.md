# The `map` & `parseInt` Puzzle

### Problem

Consider this line of JavaScript.

```
  ["1", "2", "3"].map(parseInt);
```

1. what do you expect this line of code to do? Explain your logic.

2. Run this snippet. What output do you get? Is this what you expected?

3. It's not immediately clear why we get this output. How would you go about figuring out what's wrong?

4. What would you search for if you could use Google?

5. Do you think you can explain what's going on?

### Notes to the Interviewer

Students must be familiar with `map` before they  can tackle this problem. Be sure to verify that your candidate knows this method before proceeding with this question.

As this is such an open-ended question, you will not be able to grade your candidate's ability to restate the problem; sketch a solution; etc. Rather, you will evaluate how well they communicate with you, and their tenacity in uncovering a solution. If your candidate cannot provide the answer to any of the below prompts within a couple of minutes, feel free to simply provide the answer as a free hint. Again, you are evaluating how well they communicate, and how vigorously they approach the problem with the information available—not whether they are able to solve it without aid.

Finally, it is worthwhile to let your candidate know that they are not expected to solve this problem on their own, but rather, that you will be solving this problem _together_. This helps set expectations and alleviate nerves.

### Prompts from the Interviewer

* **Prompt**: What does `map` do? What does it take as its first argument?

  * **Ask If**: Ask if your candidate has trouble explaining what this snippet does.

  * **Look For**

      **Candidate Explains `map`**.

    ```
      * `map` is a method on arrays that executes a callback on every element of the array.

      * In this case, we've passed `parseInt` as our callback, so we expect the snippet to run `parseInt` on every number in the array `[1, 2, 3]`.
    ```

Most candidates' first response to Question 3 will be to use `console.log` in some capacity, but we can't do that with this function.

* **Prompt**: Using `console.log` is a good instinct, but using it isn't straightforward. Do you see why?

  * **Ask If**: Most candidates' first response to Question 3 will involve `console.log` in some capacity, but we can't do that here.

  * **Note**: If your candidate cannot provide a response, feel free to give the answer as a free hint.

  * **Look For**

    * **Candidate Explains Why `console.log` is Unavailable**.

      * We can't use `console.log` because we pass the function `parseInt` to `map`. Since it's a built-in method, we can't insert a `console.log` statement inside of it to see what's going on.

      * In addition, we can't

      * Either response is acceptable.

      * Many candidates will not know of JavaScript's recursion ceiling. Take the opportunity to inform them.

* **Prompt**: We can still use `console.log` if we think a little bit. Can you think of how to use an anonymous function and the `arguments` variable to figure out what `map` passes to its callback?

  * **Ask If**: Ask as a follow-up to the previous question or hint.

  * **Look For**

    * **Candidate Considers Approaches**.

      * Candidates should realize that they can pass an anonymous function that `console.log`s the `arguments` object to `map`. This reveals what arguments `map` passes to its callback function.

* **Prompt**: Now that you know what `map` passes to its callback function, can you figure out how it calls `parseInt`? In other words, what does the function call to `parseInt` look like—`parseInt(number)`, or something else? Be sure to keep in mind how `map` works.

  * **Ask If**: Ask as a follow-up to the previous question.

  * **Look For**

    * **Candidate Explains Function Call**.

      * `map` works by calling a callback on every element of the array we call it on.

      * In this case, we're calling `parseInt` on every element of the array `[1, 2, 3]`.

      * But we know that the `arguments` `map` passes includes stuff other than the number, so the function call looks like: `parseInt(number, something, something_else)`

* **Prompt**: So far, we've determined that `map` gives `parseInt` three different arguments. Use Google to look up the documentation for `map` and `parseInt`, so you can find out which arguments `map` passes to its callback, and which arguments `parseInt` accepts.

  * **Look For**

    * **Candidate Finds — Reads Documentation**. MDN has good documentation for [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=example) and [parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt).

      * Candidates should find that `map` passes three arguments to its callback: The current element of the array; the index of that element in the array; and the array itself.

      * Candidates should find that `parseInt` accepts two arguments: A string to parse, and a base to parse against.

* **Prompt**. Given what you know about how `map` calls `parseInt`, what do you think is happening in our code snippet?

  * **Look For**

    * **Candidate Connects `map`'s Arguments with `parseInt`'s Arguments**

      * Candidates should be able to explain that `parseInt` interprets some of the arguments that `map` passes as a _base_ to parse against.

      * In particular, `map` passes the index of the current element to `parseInt`, which it uses as a base. So, our function calls look like:

  ```
  ["1", "2", "3"].map(parseInt);

  parseInt(1, 0); // First call: Returns 1
  parseInt(2, 1); // Second call: Returns NaN
  parseInt(3, 2); // Third call: Returns NaN
  ```

* **prompt**. Now that you've seen all the moving pieces, try to explain this code snippet using the information you've found so far.

  * **Look For**

    * **Candidate Coherently Synthesizes Information**. Candidates should be able to explain the major points of the problem.

      * The `map` function is a method on arrays that executes a callback on every element in the array it is called on.

      * The `parseInt` function converts a string to an integer.

      * In this case, we expect `map` to run `parseInt` on each string in the array, and convert them into integers.

        * In particular, we expect `["1", "2", "3"].map(parseInt)` to output `[1, 2, 3]`.

        * But instead, we get `[1, NaN, NaN]`.

      * SInce `parseInt` is a built-in function, we can't drop a `log` statement inside of it to see what's going on.

      * But, we can use an anonymous function to figure out what arguments `map` is passing to `parseInt`.

        * In this case, we find that `map` passes _three_ arguments to its callback: The current element, the index of the current element, and the array itself.

      * So, while we expected `map` to run `parseInt` on _just_ each string in the array, it instead runs `parseInt(string, index)`.

      * According to the documentation, `parseInt` takes an optional second argument, which tells it how to parse the string it's passed.

      * The problem in our snippet is that the `parseInt` callback uses the `index` as a base, so it doesn't return as expected.

- - -
