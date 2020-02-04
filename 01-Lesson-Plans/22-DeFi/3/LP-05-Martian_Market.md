### 5. Instructor Do: The Martian Market (ERC721 + Auctions) (15 min) (Critical)

In this activity, you will be demonstrating combining the ERC721 standard with the modified `MartianAuction` contract that was built in the previous activity.

**Files:**

* [MartianAuction.sol](Activities/05-Ins_Martian_Market/Resources/MartianAuction.sol)

* [MartianMarket.sol](Activities/05-Ins_Martian_Market/Solved/MartianMarket.sol)

First, explain to the students:

* We are going to be creating an ERC721 token with the ticker `MARS`. Only one entity will be allowed to create the tokens, and that entity in this example is called the "Martian Land Foundation." Assume this foundation is a global initiative from the governments of the world and is responsible for the terraforming and fundraising of Martian Land Development.

* For every token that the Martian Land Foundation mints, an `Auction` contract will be created. This auction contract will become the new owner of the token, and will allow the public to bid on that piece of land. In spirit of humanity, some landmarks will be marked as "sovereign" and will become permanently owner-less.

* The Martian Land Foundation can end the auctions at anytime.

Open up [Remix](https://remix.ethereum.org) and create a new file called `MartianMarket.sol` and populate it with the contents of the [starter code](Activities/05-Ins_Martian_Market/Unsolved/MartianMarket.sol).

The beginning of the contract should look something like:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/ownership/Ownable.sol";
import "./MartianAuction.sol";

contract MartianMarket is ERC721Full, Ownable {

    constructor() ERC721Full("MartianMarket", "MARS") public {}
}
```

* In this contract, we are simply defining an ERC721 token contract called `MartianMarket` with the ticker of `MARS`. Each `MARS` token will represent a plot of land/landmark on Mars.

* We are importing the `MartianAuction` code as well, since we will want to create a new auction for every new token.

* We are setting the ERC721 contract as `Ownable` using the OpenZeppelin library, as the Martian Land Foundation will be solely responsible for the management of the tokens, and we'll want to restrict some of our functions using the `onlyOwner` modifier that OpenZeppelin provides.

Next, you will need to add a counter to keep track of token IDs:

```solidity
    using Counters for Counters.Counter;

    Counters.Counter token_ids;
```

* Just like the last ERC721 implementations we did, we need to keep track of unique token IDs using the OpenZeppelin counter library. This will allow us to make sure that every ID we generate is unique, regardless if any tokens have been "burned" or removed from circulation.

Then, save the Martian Land Foundation's address as the contract deployer (`msg.sender`) and set it to `payable`:

```solidity
    address payable foundation_address = msg.sender;
```

* We're storing this address for later as `payable`, since we'll want to transfer the funds raised by all of the auctions to the `foundation_address`.

Now, create a new mapping that keeps track of all of the auction contracts relating to tokens:

```solidity
    mapping(uint => MartianAuction) public auctions;
```

* We are going to be creating a new `MartianAuction` contract for every `token_id` that we register into the system.

* During the minting process, we will create a `Martian Auction` contract in this mapping at the corresponding `token_id`. The `foundation_address` will be the initial owner of the token, but we will add functionality to transfer the ownership once the auction is ended.

Add a modifier that will check if a specific token exists:

```solidity
    modifier landRegistered(uint token_id) {
        require(_exists(token_id), "Land not registered!");
        _;
    }
```

* We need to add this `landRegistered` modifier in order to check whether or not a token exists before operating on it.

* This is done by calling the `_exists` function that is built into OpenZeppelin's ERC721 library, and returning the message `Land not registered!` if it doesn't. We can attach this modifier to any function that we expect a token to exist with, like bidding on an auction, or transfering ownership of land.

Add a function to create a new `MartianAuction` contract given a `token_id`:

```solidity
    function createAuction(uint token_id) public onlyOwner {
        auctions[token_id] = new MartianAuction(foundation_address);
    }
```

* This function is short and sweet, as it creates a new `MartianAuction` contract in the slot of the `auctions` mapping that belongs to the specified `token_id`. By passing in the `foundation_address`, we set the foundation as the beneficiary of the auction. In other words, the funds raised from this auction will go to the `foundation_address`.

* We can now reference this auction contract later as long as we know the `token_id` it relates to.

Now it's time to fill in the `registerLand` function:

```solidity
function registerLand(string memory uri) public onlyOwner {
        token_ids.increment();
        uint token_id = token_ids.current();
        _mint(foundation_address, token_id);
        _setTokenURI(token_id, uri);
        createAuction(token_id);
    }
```

* In this function, we are creating a new `token_id` by incrementing our counter and capturing the latest value.

* Then, we are calling the ERC721 `_mint` function, setting the `foundation_address` as the initial owner, and creating it at the `token_id` that we just generated.

* Like all ERC721 tokens, we pass in a token URI into the `_setTokenURI` function. We can set this to what we'd like later.

* Finally, we call the `createAuction` function to create a new `MartianAuction` auction contract for our new token. We will use the results of this to manage the initial public (not the foundation) ownership of the tokens.

Next, we need to create a function to end our auctions:

```solidity
    function endAuction(uint token_id) public onlyOwner landRegistered(token_id) {
        MartianAuction auction = auctions[token_id];
        auction.auctionEnd();
        safeTransferFrom(owner(), auction.highestBidder(), token_id);
    }
```

* In this function, we are using our `landRegistered` modifier to check if the token was minted yet.

* Then, we fetch the `MartianAuction` contract from the `auctions` mapping, and store it in a variable temporarily called `auction`.

* We then call the `auction.auctionEnd()` function against the auction we fetched.

* Once we end the auction, we then perform a `safeTransferFrom` that is built into the ERC721 library. This function accepts `from`, `to`, and `token_id` as the parameters. We are passing the token's owner by calling `owner()`. We can also use `foundation_address` here. Then, we send the token to the address that `auction.highestBidder()` returns.

Now we need to add a function to tell whether or not an auction has ended:

```solidity
    function auctionEnded(uint token_id) public view returns(bool) {
        MartianAuction auction = auctions[token_id];
        return auction.ended();
    }
```

* This function simply fetches the `MartianAuction` relating to a `token_id`, then returns the value of `auction.ended()`. This allows users and a frontend to quickly tell whether an auction is running for a specific land token.

Repeat the process with the `highestBid` and `pendingReturn` functions:

```solidity
    function highestBid(uint token_id) public view landRegistered(token_id) returns(uint) {
        MartianAuction auction = auctions[token_id];
        return auction.highestBid();
    }

    function pendingReturn(uint token_id, address sender) public view landRegistered(token_id) returns(uint) {
        MartianAuction auction = auctions[token_id];
        return auction.pendingReturn(sender);
    }
```

* All three of these functions are simply "forwarding" a value from the `MartianAuction` to the `MartianMarket` interface. We can use them to introspect any activity happening to the auctions we have going for any token.

Finally, we need to create our last function, `bid`:

```solidity
    function bid(uint token_id) public payable landRegistered(token_id) {
        MartianAuction auction = auctions[token_id];
        auction.bid.value(msg.value)(msg.sender);
    }
```

* While this function starts out the same as the others, it is doing something a bit special. First thing to notice, is that it is set to `payable`. Meaning, we are going to expose this function to allow users to bid on specific `MARS` land tokens by sending Ether to this function, and forwarding it to the `MartianAuction`'s `bid` function.

* In order to forward the Ether sent from one function to another, we have to use a special `.value()` syntax. All we need to do is add `.value()` *before* the parameters of any function.

* For example, `auction.bid(msg.sender)` is the normal syntax. However, this only passes in the `sender` address parameter that the `MartianAuction` expects. The actual Ether attached to the transaction would be left behind. By adding `.value(msg.value)` right before the normal parenthesis that include our parameters, we are sending the entire `msg.value` to the `auction.bid` function!

* We must be careful about this syntax, as it only forwards `2300` gas. Since that's enough to complete our function, we're okay. Otherwise, we'd have to add `.call` right before `.value()`, but that syntax doesn't protect against re-entrancy attacks, so we'd need to be very careful about modifying the state of our contract in that case.

Make sure your contract compiles and matches the [solution](Activities/05-Ins_Martian_Market/Solved/MartianMarket.sol). The next activity includes a frontend that expects the same ABI.

Voila! Now it's time for the students to build out the same system.
