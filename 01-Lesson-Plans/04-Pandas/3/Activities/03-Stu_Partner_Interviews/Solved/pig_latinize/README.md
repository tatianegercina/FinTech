# Pig Latinize

Write a function that translates a text to Pig Latin.

In case you've never heard of this silly language, to translate a word from English to Pig Latin, you move the first letter to the end of the word, and then ad _ay_. So, "fish" in Pig Latin is "ish-f-ay".

```python
pig_latinize("fish")
# ishfay
pig_latinize("your car is very nice")
# ouryay arcay siay eryvay icenay
```

## Notes to the Interviewer

Most candidates should be able to solve the basic problem of translating a word to Pig Latin. The real "meat" of this question is the fact that there are several edge cases to consider, such as how to preserve capitalization and handle punctuation. The purpose of this question is to prepare your candidate for situations where interviewers gradually make problems harder.

## Prompts from the Interviewer

* **Prompt**: How would you write a function that translates a single word into Pig Latin?

  * **Follow-Up**: Keep in mind that there's a simple formula for this.

  * **Ask If**: Ask this question if your candidate is unsure of where to start.

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For:**

    * **Candidate Sketches Solution**.

      * Candidates should be able to explain that it is sufficient to write a function that accepts a single word; moves its first letter to the end of the world; and adds _ay_ to the end.

* **Prompt**: How would you write a function that runs this function on every word in a sentence?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Sketches Solution**.

      * There are a couple of legitimate solutions to this problem.

      * Candidates can translate a sentence by using a `for` loop on every word in the sentence.

      * Alternatively, candidates can use `map` to run their function on every word in the sentence.

* **Prompt**: Does your function deal with words that contain capital letters?

  * **Ask If**: Ask if your candidate successfully implements a function that translates a sentence into Pig Latin.

  * **Ask During**: Implementation Discussion

  * **Look For**

    * **Candidate Brainstorms Alternatives**.

      * There are different ways to deal with this problem. One could simple throw out the capital letter and low-case the word; retain the original capital letter; or capitalize the first letter of the new Pig Latin word, for instance.

      * The best candidates will mention at least two alternatives, and ask the interviewer for input.

      * For our purposes, the best solution is to capitalize the first letter of the new Pig Latin word, and lowercase the rest of it.

        * If your candidate suggests this, let them know that this is the right choice.

        * If your candidate makes other suggestions but misses this one, simply let them know that their suggestions were good, but that this is the imlementation you're looking for.

    * **Note**: You don't need your candidate to implement this, yet—the conceptual solution is enough for now. When your candidate gets the answer, or when you reveal it, explain this, and move on to the next prompt.

* **Prompt**: How would you deal with punctuation? For example, does your function properly deal with `"fish."`?

  * **Ask During**: Implementation Discussion

  * **Look For**

    * **Candidate Brainstorms Solutions**.

      * One way to solve this problem is to remember the punctuation mark and then append it to end of the translated word.

  * **Note**: If your candidate identifies legitimate solutions for the past two prompts, they are free to try to implement them. These are relatively difficult implementations, however, so they are free to

## Solution

The [solution](Solved/pig_latin.py) strips the given string of any punctuation and adds the first letter and 'ay' to the end of every word in the string.
