### 5. Instructor Do: Mappings Data Structure in Solidity (15 min) (Critical)

Now that we are familiar with the concept of tokens, let's build one!

* In order to build a token with Solidity, we need to learn one more data structure, called a `mapping`.

* You can think of a mapping as a `mapping` between two variables. For instance, you can *map* an address to a balance.
  You can map a customer ID to an address, or vice versa. They can even be nested, but we won't need to do that.

Open up Remix and create a new contract called `ArcadeToken.sol`.

**Files:**

* [ArcadeToken.sol](Activities/05-Ins_Mappings/Unsolved/ArcadeToken.sol)

Define the token contract like so:

```solidity
pragma solidity ^0.5.0;

contract ArcadeToken {

}
```

* Let's say we owned an Arcade; we're going to have customers exchange Ether for tokens that can be spent to play games, redeem prizes, etc., at the arcade.

First, define a few variables to get the contract started:

```solidity
pragma solidity ^0.5.0;

contract ArcadeToken {
    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;
}
```

* We are setting the owner of the ArcadeToken contract to the `msg.sender`. Since this is only called once during deployment, this will set ourselves us as the owner when we deploy later.

* We are setting a `string public` called `symbol` to our token's ticker. MetaMask, and many other wallets and explorers will recognize the symbol as long as it is a public string.

* Setting the `exchange_rate` to `100` represents the amount of tokens we will distribute per `wei` spent later.

Next, we need to add a way of tracking ArcadeToken user balances. To do this, we will add a `mapping`:

```solidity
pragma solidity ^0.5.0;

contract ArcadeToken {
    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;
}
```

Stop and explain the `mapping` data structure to the class:

* Here we are setting a `mapping` of the type `address` to `uint`. This means that we can use an `address` as a key, and set a `uint` value associated with it.

* It is conceptually similar to an unordered list of key-value pairs, or a Python dictionary (key-value store), or a hash-table, but not as flexible since we set the types up front. They do not have a set limit to the number of values you can store, and adding or changing values does not cost more gas as the mapping grows. In fact, we are only limited by gas in regards to how much we can store per transaction and per block.

* Since this `mapping` pairs `address`es to `uint`s, we can associate any `address` with a balance stored in a `uint`.

* Let's actually write a function that fetches a `uint` balance that is associated with an `address` by writing a balance function.

Demonstrate how to access the balance of an address by adding a new `balance` function:

```solidity
mapping(address => uint) balances;

function balance() public view returns(uint) {
    return balances[msg.sender];
}
```

* Notice how we are able to access the balance of the user by selecting via `balances[msg.sender]`.

* This is the same way we access values in dictionaries. The key is `msg.sender`, which is an `address`, and the value that this function outputs is the `uint` the address is mapped to.

* We could pass any `address` as the selector/index/key to the `mapping`, and it will return the `uint` associated with it.

  * For example, `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333` is what the data might look like in contract storage.

* Mappings are flexible data types that allow you to link data together efficiently. They are much cheaper than using an array, so we'll be using them quite often. They are one of the main data types used in tokens, because of this easy way of creating a balance system. We can map any type to any type, even `address` to `address`.

Now, let's demonstrate how customers could transfer ArcadeTokens between each other by adding another function called `transfer`:

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] -= value;
    balances[recipient] += value;
}
```

* We are adding a new function that called `transfer` that accepts a `recipient` and a `value`.

* This function subtracts the value from the token balance of the sender, then adds that same value to the token balance of the recipient address.

* As you can see, the logic here is actually just as simple as you would expect. Value moves from one address to another.

Note, this contract is currently vulnerable to something called an `integer underflow` attack and allows users to spend tokens they do not have.
If students notice this, simply explain that we will add more security features later today to prevent spending with zero token balance.

Now, we'll need some way to allow users to purchase tokens from the contract. Add a new `purchase` function, and set it to `payable`:

```solidity
function purchase() public payable {
    uint amount = msg.value * exchange_rate;
    balances[msg.sender] += amount;
    owner.transfer(msg.value);
}
```

* With this `purchase` function, we allow users to send Ether by setting the function to `payable`.

* We then multiply the `msg.value` by the `exchange_rate` we set earlier.

* Next, we add the amount of tokens being purchased to the token balance of the `msg.sender` by changing the value in the `balances mapping`.

* Finally, we transfer the Ether to ourselves via the `owner.transfer(msg.value)` call.

* Now, when users send Ether to this function, they will be given tokens based on the exchange rate, and the Ether will be sent to the ArcadeToken owner.

* Once the users have tokens, they can call the `transfer` function to send them back and forth, or to pay for Arcade games!

Explain to the class that we'll need some way to create tokens out of thin air when we absolutely need to. To do this, we'll add a `mint` function:

```solidity
function mint(address recipient, uint value) public {
    require(msg.sender == owner, "You do not have permission to mint tokens!");
    balances[recipient] += value;
}
```

* This function accepts the same parameters as `transfer`, however it can only be called by the `owner` due to the `require`.

* This way, whenever we need to mint new tokens as the owner, we can add value to any balance needed.

* This may be useful for customer support, rewards, or could even be connected to an automatic system of your design.

Time for the students to get their hands dirty with some token design!
