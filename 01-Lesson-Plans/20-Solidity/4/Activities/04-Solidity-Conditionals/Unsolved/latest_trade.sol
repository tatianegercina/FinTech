/*
1. Use the `latest_trade.sol` file to create a contract named `TradeController` that contains:

    * An unsigned integer variable `previous_price`.

    * A string variable `trade_type`.

2. Add a public function named `makeTrade` to the `LatestTrade` contract as follows:

    * Define an unsigned integer `current_price` as the unique function's parameter.

    * Into the body of the function, use an `if` statement to check if the input parameter `current_price` is
      less than the contract variable `current_price`, if so, set the `trade_type` string variable as "Buy"
      and set the `previous_price` to the `current_price`.

3. Modify the `makeTrade` function of the `LatestTrade` contract as follows.

    * Add a boolean variable `buy_anyway` as the second parameter.

    * Use and `OR ( || )` clause within the `if` statement to check if it's true that the `current_price` is
      less that `previous_price` or `buy_anyway` is true.

    * Add an `else if` statement to check if the `current_price` is greater than the `previous_price`, if so,
      set the `trade_type` to "Sell" and the `previous_price` equal to the `current_price`.

    * Add an `Else` statement to set the `trade_type` to "Hold" in case the previous conditions were false.
*/
