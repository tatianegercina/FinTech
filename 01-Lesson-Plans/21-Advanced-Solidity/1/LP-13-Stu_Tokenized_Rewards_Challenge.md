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

### 14. Instructor Do: Challenge Review / Recap (10 min)

**Files:**

* [ArcadeTokenRewards.sol](Activities/13-Stu_Tokenized_Rewards_Challenge/Solved/ArcadeTokenRewards.sol)

Open the solution and explain the following:

* In our spend function, we calculate the fee by performing `uint fee = msg.value.mul(fee_rate).div(10000)`.
  This calculates a percentage of the `msg.value` by using the basis points formula.

* We calculate the token reward amount by multiplying the `msg.value` by the reward as so: `uint reward = msg.value.mul(reward_rate)`.

* We then add the rewards to the balance of the user by running `balances[msg.sender] = balances[msg.sender].add(reward)`.

* Next, we transfer the `msg.value` minus the fee to the `recipient` using `recipient.transfer(msg.value.sub(fee))`.

* Finally, we transfer the remaining `fee` value by running `owner.transfer(fee)`.

Ask the students the following questions:

* Why might we want to implement a reward system like this?

  * **Answer:** You could incentivize loyal users to return to your Arcade or business.

  * **Answer:** You generate capital from small fees that allow you to further develop your business.

  * **Answer:** This works much like an annual credit card fee would, but instead collects passively.

  * **Answer:** You only need to write the contract once, then you have the reward system in place. Less infrastructure cost for the business.

* What are some downsides to this system?

  * **Answer:** Some users won't be willing to pay an extra fee. In that case you may be able to remove it applicable for your business model.

  * **Answer:** Users have to pay extra gas to run the `spend` function vs paying Ether directly.

  * **Answer:** It may be difficult to come up with a viable rewards system that works for your business.

Ask for any remaining questions before moving on.

### 15. Instructor Do: Homework Demo (10 min)

This section is reserved for the homework demo. Take some time to review the homework with the class.

- - -

### End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
