### 13. Instructor Do: Conditionals in Solidity (10 min)

In this demonstration we will be discussing how conditionals in Solidity are formatted differently from Python.
To show this, we will be reviewing basic logical operators and control flow to build a basic `TradeController` contract that tracks trades on the Ethereum blockchain.

Explain trade controllers to the class: 

* Say you want to build a basic trade controller that will signal whether or not we should be buying, selling or holding based on a designated price.
  We're not going to use complex logic, just buy low and sell high.
  The main goal is to understand the differences in syntax for conditionals.

We are going to start by defining a `uint` called `previous_price`, and a `string` called `trade_type`.

```solidity
pragma solidity ^0.5.11;

contract TradeController {
    uint previous_price;
    string trade_type;
}
```

* Make note that we are using `uint` for our prices and balances. This is because we'll always be dealing with positive numbers, never negative balances or prices.

Next, show the class how to define a function called `makeTrade`.
We will be passing a `uint` to `makeTrade` that represents the `current_price` of an asset:

```solidity
pragma solidity ^0.5.11;

contract TradeController {

    uint previous_price;
    string trade_type;

    function makeTrade(uint current_price) public {
    }
}
```

* This `makeTrade` function accepts a `uint` that represents the current price of the asset.

Now let's add a basic conditional to check if the `current_price` we are attempting to trade at is less than the `previous_price` that we traded at:

```solidity
function makeTrade(uint current_price) public {
    if (current_price < previous_price) {
            trade_type = "Buy";
            previous_price = current_price;
    }
}
```

* Just like Python, in Solidity an `if statement` is the keyword `if` followed by a condition that evaluates to `true` or `false`.
  However unlike Python, in Solidity, the conditions are contained inside parenthesis.

* Take note that just like when we define the body of a function in Solidity the body of an `if statement` is also contained in curly brackets.

* Now that we have a value for what the `current_price` is, we can compare that to the `previous_price` to determine whether or not we should buy.

* If the `current_price` is lower than `previous_price`, we set the `trade_type` to the `string` "Buy".

* In the final line inside the `if statement`, we update the `previous_price` to the `current_price` we just traded at to compare against next time.

Add a new `bool` parameter called `buy_anyway` to the `makeTrade` function.
Place `|| buy_anyway` at the end of the condition to allow it to return `true` even if the current price is more expensive than the previous trade price.

```solidity
function makeTrade(uint current_price, bool buy_anyway) public {
    if (current_price < previous_price || buy_anyway) {
            trade_type = "Buy";
            previous_price = current_price;
    }
}
```

* What if we want to buy anyway, regardless of the previous price? This would be a perfect use case for our `||` (or) operator.

* First, we add a new `bool` parameter called `buy_anyway` -- when we set this to `true`, we can override the price check in the `if` statement
  by saying `|| buy_anyway`. In plain English, this `if` statement now says "if the current_price is less than the previous_price, or buy_anyway is set to true, then continue."

* In Python most logical operators are defined keywords in plain English like `and`, `or`, `not`.
  However in Solidity (and many other languages) we have symbols like `&&`, `||`, `!`, repsectively.

Add an `else if` with a condition to check if the `current_price` is less than the `previous_price` so that we know when to sell.

```solidity
function makeTrade(uint current_price, bool buy_anyway) public {
    if (current_price < previous_price || buy_anyway) {
            trade_type = "Buy";
            previous_price = current_price;
    } else if (current_price > previous_price){
            trade_type = "Sell";
            previous_price = current_price;
    } else {
           trade_type = "Hold";
    }
}
```

* If the `current_price` is more than the the `previous_price` and we do not want to `buy_anyway` then we are going to sell, so we move to the `else if`.

* If the first two conditions evaluate to `false` then we are going to set the `trade_type` to hold because we can not currently buy or sell.

Now it's time for the students to use some conditionals in Solidity!
