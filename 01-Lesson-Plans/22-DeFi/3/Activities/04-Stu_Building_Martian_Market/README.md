# Building the MartianMarket

In this activity, you will combine an ERC721 token contract with the `MartianAuction` contract to create the `Martian Land Market`. This market will be managed by the `Martian Land Foundation`, which, in this example, is a global human collaborative that oversees the terraforming of Mars. The foundation will be able to register (aka, mint) Martian landmarks as tokens. These tokens are immediately put out for a public auction.

## Instructions

* Open up [Remix](https://remix.ethereum.org) and create a new file called `MartianMarket.sol` and populate it with the contents of the [starter code](Unsolved/MartianMarket.sol).

  * In this contract, we are simply defining an ERC721 token contract called `MartianMarket` with the ticker of `MARS`. Each `MARS` token will represent a plot of land/landmark on Mars.

  * We are importing the `MartianAuction` code as well, since we will want to create a new auction for every new token.

* Add a counter to keep track of token IDs. Name the counter `token_ids`.

* Save the Martian Land Foundation's address as the contract deployer (`msg.sender`) and set it to `payable`. Name the variable `foundation_address`.

  * We're storing this address for later as `payable`, since we'll want to transfer the funds raised by all of the auctions to the `foundation_address`.

* Now, create a new mapping that keeps track of all of the auction contracts relating to tokens. The mapping should look like `uint => MartianAuction`. Name it `auctions`.

* Add a modifier that will check if a specific token exists called `landRegistered`. Check if the token exists using the ERC721 `_exists` function. If the token does not exist, return a message like `Land not registered!` using a `require` statement. Don't forget to put `_;` at the end of the modifier to return back to the original function!

* Add a function to create a `new MartianAuction` contract given a `token_id` in the `auctions` mapping. Name this function `createAuction`.

* Now it's time to fill in the `registerLand` function:

  * In this function, create a new `token_id` by incrementing the `token_ids` counter and capturing the latest value using `token_ids.current()`.

  * Then, call the ERC721 `_mint` function, setting the `foundation_address` as the initial owner, and passing in the `token_id` that was just generated.

  * Like all ERC721 tokens, pass in a token URI into the `_setTokenURI` function.

  * Finally, call the `createAuction` function to create a new `MartianAuction` auction contract for the new token.

* Next, create a function to end the auctions called `endAuction`. This should have the `landRegistered` and `onlyOwner` modifiers.

  * In this function, fetch the `MartianAuction` contract from the `auctions` mapping, and store it in a variable temporarily called `auction`.

  * Call the `auction.auctionEnd()` function against the auction that was fetched.

  * After ending the auction, perform a `safeTransferFrom` that is built into the ERC721 library. This function accepts `from`, `to`, and `token_id` as the parameters. Pass the token's owner by calling `owner()` or `foundation_address` here (in this case, they will be the same. Then, send the token to the address that `auction.highestBidder()` returns.

* Next, add a function to tell whether or not an auction has ended called `auctionEnded` that simply fetches the `MartianAuction` relating to a `token_id`, then returns the value of `auction.ended()`.

* Repeat the process with the `highestBid` and `pendingReturn` functions. Each of these functions should simply fetch the `MartianAuction` contract given a `token_id`, then return the `auction.highestBid()` and `auction.pendingReturn(sender)` variables. For `pendingReturn`, you will need to accept a `token_id` and `address sender` to lookup this value from `MartianAuction`.

  * All three of these functions are simply "forwarding" a value from the `MartianAuction` to the `MartianMarket` interface. This can be used to introspect any activity happening to the auctions we have going for any token easily from the `MartianMarket` contract, instead of having to manually find each `MartianAuction` in the blockchain (there's one per token!).

* Finally, create the last function, `bid`. Make sure it is `payable`, as this is what the public will use to send their Ether as bids for `MARS` tokens. In this function, you will need to fetch the `MartianAuction` given a `token_id` just like the other functions, but instead, you will need to forward the Ether value that was sent to the `MartianMarket` to the corresponding `MartianAuction` using the `.value` syntax.

  * All you need to do is add `.value()` *before* the parameters of any function to set the Ether value transferred to it.

  * For example, `auction.bid(msg.sender)` is the normal syntax. However, this only passes in the `sender` address parameter that the `MartianAuction` expects. The actual Ether attached to the transaction would be left behind. By adding `.value(msg.value)` right before the normal parenthesis that include our parameters, you can send the entire `msg.value` to the `auction.bid` function!

  * The function call will look something like:

  ```solidity
    auction.bid.value(msg.value)(msg.sender)
  ```

* Deploy the contract to your `Ganache` blockchain, and copy the address for later. Congratulate yourself on combining some very complex smart contracts to create a powerful market system!

## Challenge

* If time remains, copy your deployed contract's address over to a note file, and copy the `MartianMarket` and `MartianAuction` ABI's from Remix into separate `json` files. This will prepare you for the next activity, where you will be working with this contract's frontend!

## Hints

* For a reminder of the features that OpenZeppelin provides in their ERC721 implementation, check out the [API documentation for ERC721](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721).
