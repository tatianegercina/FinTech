# Buy Low Sell High

## Problem

Xena is an amateur day trader. Her portfolio consists of IAG. IAG is a mineral exploration company. Xena believes IAG has opportunity based on a gut feeling she has. Xena bought 10000 shares of IAG at $1.45 per share at 10 am on 12/12/15. She ended up selling it 20 minutes later at $1.74 making a $2900 profit. Xena just made 2 months of rent in 20 minutes.

These were all the prices of IAG on 12/12/15 during a one hour period in chronological order:

`$1.42, $1.32, $1.45, $1.20, $1.34, $1.74, $1.10, $1.89, $1.42, $1.90`

Write an efficient function that takes an array of stock prices in chronological order. The function should determine the largest profit possible during that period if someone bought the stock at the lowest price and sold it at the highest.

You must buy before you sell—no shorting.

### Notes to the Interviewer

Remember—you are concerned more with the candidate's ability to _communicate_ their approach than with the correctness of their solution.

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: What happens if the price _decreases_ all day?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Discusses Possibilities**. As examples, you could throw an error; return "No Profit"; or report the minimum loss (best approach).

      * The best candidates will discuss multiple possibilities; explain one; and explain their choice.

      * Such a discussion and explanation is better than immediately stumbling on the best approach.

    * **Candidate Explains Best Approach**. The best solution is to report the minimum loss.

      * The best candidates will explain why—because we should keep track of my how much money we _lose_, even if there's no way for us to _win_.

* **Prompt**: What happens if I pass an array with just one element?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Asks for Input**. The best candidates ask if they can assume a certain array length.

    * **Candidate Explains Best Approach**. Passing an array with a single element breaks solutions that don't check the incoming array's length.

      * The best candidates explain that they should `return` or `throw` (better) for arrays of length 1.

* **Prompt**: Is this the fastest solution?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Explains Shortcomings**. Good candidates who can't find the fast solutions explain that their nested loop is slow, and point it out as a point for optimization.

    * **Candidate Explains Alternatives**. Good candidates who can't implement the fast solutions explain how they might work at a conceptual level, or pseudocode it.

    * **Candidate Explains Optimality**. Candidates who find the fast solutions explain why their solution is optimal.

    * **Candidate Implements Alternatives**. The best candidates explain why the slow solution is suboptmal; explain better alternatives; and implement them.

### Hints

* Can we simply take the difference between the maximum and minimum elements?

  * We can't, because we can't guarantee that the maximum element occurs _after_ the minimum.

* Is it correct to loop through the entire array twice?

  * Not if the inner loop always starts at `0`.

  * Nested loops are correct only if the inner loop (with index `j`) starts at the index after that maintained by the outer loop (with index `i`).

* Can we loop through the array just once, and keep track of the maximum profit and minimum price we've seen _so far_?

  * **Follow-Up**. How do we know if we've found a new maximum profit?

  * **Follow-Up**. How do we know if we've found a new minimum price?

### Solutions

#### Brute Force | O(n^2)

[The slow, brute force solution](Solved/bruteForce.js) is to check every possible pair, and return the maximum. It is _correct_, but slow. It is, however, perfectly acceptable for candidates to start here.

#### Greedy Linear Search | O(n)

The best possible solution is to scan the array once, keeping track of the maximum profit identified so far and the minimum price. This solution is available in [linearScan.js](Solved/linearScan.js).
