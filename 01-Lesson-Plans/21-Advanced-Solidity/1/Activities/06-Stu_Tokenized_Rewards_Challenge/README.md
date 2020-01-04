# Tokenized Rewards System Challenge

In this activity, you will create a system very similar to credit card reward points with your `ArcadeToken`.

You will create a new function to your token called `spend` that allows users to spend regular Ether with your contract.

In your `spend` function, you will take a very small "microtransaction" fee and forward the rest of the Ether to the recipient.

In exchange for the small fee (or even no fee, if you so desire), you will reward tokens based on a multiplier (say, 3 tokens rewarded for every wei spent).

This will create an incentive for your loyal customers to continue returning to your Arcade (or whatever business you can think of) to spend their tokens and generates capital passively for you to continue improving the Arcade. This works like a credit card fee but instead collects fees passively instead of annually.

This same model can apply for any rewards system and can be customized to the use case, so long as the incentive configuration can benefit both parties.

## Instructions

* Below the `symbol` and `exchange_rate` variable definitions, add the following variable:

  * A `uint public` called `fee_rate` -- this will be set to a number of "basis points."

  * Since Ethereum does not fully support floating-point (decimal) numbers, we have to use basis points to calculate our percent.

  * `1` basis point = `0.01%`. You can calculate a percentage by using the formula `basis_points.mul(some_number).div(10000)`.

    For example: `250 basis points * $100 / 10000` is equal to `$2.5` or 2.5%

    Here's a handy chart for easy reference:

    Basis Points | Percentage
    ---------|----------
    1 | 0.01%
    5 | 0.05%
    10 | 0.1%
    50 | 0.5%
    100 | 1%
    1000 | 10%
    10000 | 100%

  * Assuming this, set your `fee_rate` to equal the number of basis points you'd like to charge per transaction. This will be calculated in our `spend` function later.

  * For example, set `fee_rate` to `25` to charge `0.25%` per transaction. Make sure the fee is reasonable!

* Next, add a `uint public reward_rate` below the `fee_rate` and set this to equal the number of tokens to reward per wei spent.

  * For example, set `fee_rate` to `3` to reward 3 tokens per wei spent.

* Add a new `public payable` function called `spend` to your contract.

  * Set the parameter of this function to be a payable recipient address.

* In your `spend` function, perform the following actions:

  * Set a new `uint fee` to equal the percentage calculation using the basis points formula. You can do this by multiplying the `msg.value` with the `fee_rate` and dividing by `10000`.

  * Calculate a new `uint reward` by multiplying `msg.value` with the `rewards_rate`.

  * Now, add the reward to the balance of the `msg.sender` by setting the `balances[msg.sender]` to equal `balances[msg.sender]` plus the reward.

  * Time to transfer some Ether. First, `.transfer` the `msg.value` **minus** the `fee` to the `recipient`. This will forward all of the Ether except the fee.

  * Finally, `.transfer` the `fee` to the `owner`. After this, there should be no remaining Ether left to spend, and the token rewards and fees will have been distributed!

  * **Remember** to use **SafeMath** for **all** math operations!

* Congratulations! You have successfully built a rewards system that can be used in many different businesses. Take the rest of the time to deploy and test your contract features.

## Challenge

* If time remains, try to replace the hardcoded variables at the top of the contract with a constructor to allow for deploying this rewards system anywhere.

* Customize the rewards incentive structure to fit different use cases you can imagine.

## Hints

* If you would like to know more about how basis points work, visit [Investopedia](https://www.investopedia.com/terms/b/basispoint.asp) for more information.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
