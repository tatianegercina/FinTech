# Writing an Auction Contract

You are a smart contract engineer on a team of elite developers hired by the Martian Land Foundation to build a system that will crowdfund the development of a new colony on Mars. To accomplish this goal and help humanity thrive on Mars you have communicated with your project manager, gathered the necessary business requirements and have decided to leverage an `Open Auction Smart Contract`. In this activity, you will take a SimpleAuction contract basd off of the Solidity documentation and modify it to suit the needs of the `Martian Land Foundation`.

## Instructions

* Begin by opening the [simple auction boilerplate contract](Unsolved/MartianAuction.sol). This has been given to you based on the auction contract interface from the Solidity docs.

* Inside the `MartianAuction` contract above the contract's constructor define some initial variables that will be used to track the state of the auction.

  * An `address payable public beneficiary` will be used to track the beneficiary of the contract.

  * An `address public highestBidder` will be used to keep track of the address of the current highest bidder.

  * A `uint public highestBid` will be used to track the current highest bid amount of the highest bidder.

  * A mapping of `addresses` to `uints` named `pendingReturns` will be used to track the pending returns of those that were outbid.

  * A pubic `bool` named `ended` to track when the bidding period has closed and the auction has ended.

* Next define two events that will be used to log data for the frontend dApp.

  *  `event HighestBidIncreased(address bidder, uint amount);`

  *  `event AuctionEnded(address winner, uint amount);`

* Inside the `bid` function:

  * Add a `require` check for if a sent bid is less than the current `highest bid`. If it is less, then have the require return the text "There already is a higher bid."

  * Add a second `require` check inside the `bid` function that will check the `ended` variable to see if the auction has ended. remember to use the `!` operator.

  * Add an `if statement` to check if there has been a previous bidder. Inside the body of the `if statement` add the current `highestBidder` to the `pendingReturns` mapping and map the current value of `highestBid` to that bidder's address.

  * Set the new `highestBidder` to the `address` passed from the `bid` function's `sender` parameter. Also set the new `highestBid` value to the `msg.value` sent to the bid function.

  * On the last line inside the `bid` function `emit` the `HighestBidIncreased` and pass it `sender` and the current `msg.value`

* Inside the `withdraw` function:

  * Define a new `uint` named `amount` and set the value equal to that of the `mapped` value of `msg.sender` in the `pendingReturns` map.

  * Next, define a new `if statement` that checks if the `amount` variable is greater than 0, then after the `if statement` return `true`.

  * Inside the `if stament` set the current `msg.sender's` mapped `uint` value from `pendingReturns` to 0.

    * Now define a nested `if statement` inside the first, in the condition statement call `msg.sender.send` and send the previously defined `amount` to them. Add a `not` operator in front of the statement to `negate` the value from `true` to `false`.

    * Inside the nested `if statement` set the current `msg.sender`'s mapped `uint` value back to the value of `amount` and return `false`.

* Inside the `pendingReturn` function, return the passed `sender`'s corresponding `pendingReturn amount` via the `pendingReturns` mapping.

* Inside the body of the `auctionEnd` contract:

  *  Define a `require` statement that will check if the auction has ended by negating the `ended` variable with the `!` operator.

  * Below that define a second `require` statement that checks to see if `msg.sender` is equal to `beneficiary`.

  * Then set the `ended` variable equal to `true`.

  * `Emit` the `AuctionEnded` event passing it the `highestBidder` and the `highestBid` variables.

  * Transfer the `highestBid` amount to the `beneficiary` using the `.transfer` address method.

## Challenge

* If time remains, brainstorm additional functionality that could be implemented in your auction contract, such as a blind auction mechanism that doesn't reveal to bidders what others have bid until the end of the bidding period.

## Hints

* In case you need some help with this contract, visit the [Solidity documentation on auction contracts](https://solidity.readthedocs.io/en/v0.5.3/solidity-by-example.html#simple-open-auction) to gain additional insight.
