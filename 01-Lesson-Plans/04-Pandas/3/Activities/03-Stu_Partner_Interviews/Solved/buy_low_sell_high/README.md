# Buy Low Sell High

Xena is an amateur day trader who is day trading IAG, a mineral exploration company. On 12/12/15 @ 10 AM, Xena believed IAG was a buying opportunity and bought 10000 shares at $1.42 per share and ended up selling it an hour later (11 AM) at $1.85 per share, generating a profit of $4300. Although a fantastic trade in and of itself, Xena wants to know if she could have possibly made more money.

These were all the prices of IAG at 5-minute intervals on 12/12/15 between the hours of 10 AM and 11 AM:

`$1.42, $1.32, $1.45, $1.20, $1.34, $1.74, $1.10, $1.89, $1.42, $1.90, $1.80, $1.85`

Write an efficient function that takes a list of stock prices in chronological order and finds the best trade by calculating the max profit through the determination of the minimum (buy) and maximum (sell) stock prices.

## Notes to the Interviewer

Remember—you are concerned more with the candidate's ability to *communicate* their approach than with the correctness of their solution.

## Potential Prompts for the Interviewee

The interviewer may use these prompts to invoke additional problem-solving for the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: What happens if the price _decreases_ all day?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For:**

    * **Candidate Discusses Possibilities**.

      * As examples, you could throw an error; return "No Profit"; or report the minimum loss (best approach).

      * The best candidates will discuss multiple possibilities; explain one; and explain their choice.

      * Such a discussion and explanation is better than immediately stumbling on the best approach.

    * **Candidate Explains Best Approach**.

      * The best solution is to report the minimum loss.

      * The best candidates will explain why—because we should keep track of my how much money we _lose_, even if there's no way for us to _win_.

* **Prompt**: What happens if I pass a list with just one element?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For:**

    * **Candidate Asks for Input**.

      * The best candidates ask if they can assume a certain list length.

    * **Candidate Explains Best Approach**.

      * Passing a list with a single element breaks solutions that don't check the incoming list's length.

      * The best candidates explain that they should print an error for lists of less than length 2.

* **Prompt**: Is this the fastest solution?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For:**

    * **Candidate Explains Shortcomings**.

      * Good candidates who can't find the fast solutions explain that their nested loop is slow, and point it out as a point for optimization.

    * **Candidate Explains Alternatives**.

      * Good candidates who can't implement the fast solutions explain how they might work at a conceptual level, or pseudocode it.

    * **Candidate Explains Optimality**.

      * Candidates who find the fast solutions explain why their solution is optimal.

    * **Candidate Implements Alternatives**.

      * The best candidates explain why the slow solution is sub-optimal; explain better alternatives; and implement them.

## Hints

* Is it correct to loop through the entire list twice?

  * Only if we are looking to compare every combination of share prices.

* Can we loop through the list just once, and keep track of the maximum profit and minimum price we've seen _so far_?

  * **Follow-Up**. How do we know if we've found a new maximum profit?

  * **Follow-Up**. How do we know if we've found a new minimum price?

## Solutions

## Brute Force

[The brute force solution](Solved/brute_force.py) is to check every possible pair, calculate the max difference between share prices, and calculate and return the maximum profit. Although correct and perfectly acceptable for candidates to start here, this solution is slow compared to other alternatives.

## Linear Scan

[The linear scan solution](Solved/linear_scan.py) is to scan the list once and keep track of the minimum and maximum share prices, and then perform a single calculation at the end to calculate and return the max profit.
