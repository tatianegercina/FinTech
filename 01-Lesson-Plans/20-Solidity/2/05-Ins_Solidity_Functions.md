### 5. Instructor Do: Solidity Functions (10 min)

In this demonstration instructor will show the various nuances of functions in Solidity,such as specifying the return type and public/private modifiers.

Open [Remix](http://remix.ethereum.org) and create a new file called `LatestTrade.sol`.

* Let's say you are a famous crypto trader and wanted to publish your latest buy order at the price that you bought at.
  You want to be able to crytographically prove that it was you that made that recommendation so you're going to build
  a smart contract to publish your latest trade to the blockchain.

Type the following contract boilerplate:

```solidity
contract LatestTrade {
    string coin = "BTC";
    uint price;
    bool is_buy_order;
}
```

* First we are defining a `string` with the default text "BTC" that will be used to store the last coin that we purchased.

* Next we are defining a `uint` with the name `price`. This will be used to store the last price that we bought the coin for.

* Lastly, we are going to define a boolean (true/false value) called `is_buy_order`.
  If the order is a buy order we will set this to `true`. If it is a sell order we will set it to `false`.

* Now that we have defined our variables for our contracts values we can create a function to set them.

Add a function called `updateTrade` to the contract:

```solidity
pragma solidity ^0.5.0;

contract LatestTrade {
    string coin = "BTC";
    uint price;
    bool is_buy_order;

    function updateTrade(string memory newCoin, uint newPrice, bool is_buy) public {
        coin = newCoin;
        price = newPrice;
        is_buy_order = is_buy; /// is this a buy or a sell order?
    }
}
```

* Remember, we have to specify the data type of the parameters as well. We can't get away with ambiguity here like we can in Python!

* Pay close attention to the keyword `memory` in front of the `newCoin` variable.

* The reason we specify that the string is stored in `memory` is because strings are a more complex,
  and thus more expensive data type than integers and addresses and the EVM requires you to specify where it is stored.

* While we operate on the string (like passing it in from a parameter), we can store it in `memory` and use less gas than storing a string normally.

* Since we defined `string coin` at the top of the contract without specifying `memory`,
  any variable stored in `coin` is permanently written to the blockchain.

Now it's time to add a function to fetch all of these variables in one shot:

```solidity
function getLatestTrade() public returns (string memory, uint, bool) {
    return (coin, price, is_buy_order);
}
```

* Notice that we add the `public` to the function definition, and we also need to specify the return types!

* Even though functions are `public` by default, Solidity requires us to specify that anyway.
  What this means, is that the function can be called from outside of the contract, either by users or other contracts.
  If we set this to `private`, the function would only be callable from other functions in the contract.

* As you might expect, Solidity requires us to specify what types of data this function returns.
  In this case, we are returning a `string` that will be stored only in `memory` (since we are just fetching the variable), a `uint` and a `bool`.

* Since we are just fetching data, calling this function is free! It only costs money to write data to the blockchain or perform calculations on things in `memory`!

* You can "get" the data all you want, since it's already stored on the blockchain node.
