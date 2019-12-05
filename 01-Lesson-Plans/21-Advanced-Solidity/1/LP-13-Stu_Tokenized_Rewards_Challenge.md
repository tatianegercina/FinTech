### 13. Students Do: Tokenized Reward System Challenge (20 min)

In this activity, students will take some time to work on a "tokenized reward system" challenge.

Students will modify their `ArcadeToken` to distribute tokens as a reward for spending Ether with the contract.

The new `spend` function will collect a small transaction fee for the owner (say, `0.25%`) and reward points to the user in exchange (say, 3 tokens for every wei spent).

Clarify the activity a bit to the students:

* In this activity we will incentivize loyal Arcade to users to collect `ARCD` tokens passively during regular Ether transactions that can later be used in the Arcade.

* We will alter our contract to provide a system similar to credit card points that can be redeemed for cashback, in-store credits, etc. by adding a new function
  called `spend` that will collect a small transaction fee to the `owner` and forward the rest of the Ether to a `recipient`.
  Then, the contract will reward X amount of points for every wei spent.

* Say we actually ran an Arcade, or some other store or service. Loyal Arcade customers can spend their Ether with our contract and redeem the tokens back at the Arcade!

* The contract owner collects a small Ether fee passively in return for the rewarded tokens, so capital is generated to provide these benefits.
  You could configure the reward system however you'd see fit.

Send out the instructions to the students and have TAs circulate the class. Remind students to use SafeMath operations!

**Instructions:**

* [README.md](Activities/13-Stu_Tokenized_Rewards_Challenge/README.md)

**Files:**

* [ArcadeTokenRewards.sol](Activities/13-Stu_Tokenized_Rewards_Challenge/Unsolved/ArcadeTokenRewards.sol)

Note: since Solidity does not support floating point numbers (decimals), a formula is provided in the instructions to calculate percentages from "basis points."

`1` basis point = `0.01%`. You can calculate a percentage by using `basis_points * some_number / 10000`.

For example: `250 basis points * $100 / 10000` is equal to `$2.5` or 2.5%

Here's a handy chart for easy reference (also provided to the students):

Basis Points | Percentage
---------|----------
1 | 0.01%
5 | 0.05%
10 | 0.1%
50 | 0.5%
100 | 1%
1000 | 10%
10000 | 100%

Ensure students are applying this formula if they decide to use percentages in their rewards system.
