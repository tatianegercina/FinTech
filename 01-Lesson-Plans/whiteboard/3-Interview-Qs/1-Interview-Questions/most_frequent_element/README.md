# Most Frequent Element

### Problem

Write a function that finds the most frequent element in an array.

```
find_most_frequent_element([1, 2, 2, 3]) // 2
```

### Notes to the Interviewer

N/A.

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Does your approach work if two elements appear the same number of times, as in `[1, 2, 2, 3, 3]`?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Discusses Shortcomings**.

      * Certain implementations will return _one_ of the most frequently occurring elements, but not _all_ of them.

        * Strong candidates will explain that properly dealing with the case of multiple frequent elements requires a _loop_ that collects every element that occurs `max` number of times. In the example above (`[1, 2, 2, 3, 3]`), this loop would identify every element occurring twice: `2` and `3`.

* **Prompt**: How does your solution behave if every element occurs the same number of times?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Asks for Input**.

      * There multiple legitimate ways to deal with this. One could:

        * Return every element; or

        * Return some value indicating that there is no "most frequent".

      * Both are valid solutions, but the latter is arguably better.

      * Strong candidates will choose one, but explain the tradeoffs between the two choices; _or_, ask the interviewer what they prefer.

### Hints

* Does your solution change if the input array is unsorted?

  * It shouldn't. A properly implemented solution should work on unsorted arrays.

### Solutions

#### Complete Solution

A complete solution should return all elements that occur `max` number of times, rather than just one of the most frequently occurring elements. For example, `find_most_frequent_element([1, 2, 2, 3, 3])` should return both `[2, 3]` as opposed to just `2` or `3`.

[The reference solution](Solved/find_most_frequent_element.js) always returns an array of most frequently occurring elements. If there is only one, this means it returns an array of one element. This is a conscious design decision, and is something strong candidates will discuss.

This solution runs in `O(n)` time with `O(n)` extra space.
