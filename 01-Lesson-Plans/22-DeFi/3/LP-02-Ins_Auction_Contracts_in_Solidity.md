### 2. Instructor Do: Auction Contracts in Solidity (10 min)

In this activity, the Instructor will demonstrate the various Auction contracts available from the Solidity example documentation, and modify it to fit our needs. Students will be introduced to the story of the "Martian Land Foundation" and how we will be "tokenizing" martian land and auctioning it to the public, raising funds for the Martian Land Foundation's terraforming projects, and allowing every-day citizens to claim their spot on humanity's next frontier.

**Files:**

* [AuctionContract.sol](Activities/02-Ins_Auction_Contracts_in_Solidity/Solved/SimpleAuction.sol)

Begin the activity by introducing the class to the backstory of the `Martian Land Foundation`.

* You are a smart contract engineer on a team of elite developers hired by the martian land foundation to build a system that will crowdfund the development of a new colony on Mars. To accomplish this goal and help humanity thrive on Mars you have communicated with your project manager, gathered the necessary business requirements and have decided to leverage an `Open Auction Smart Contract`.

Next open the [solidity open auction contract documentation](https://solidity.readthedocs.io/en/v0.5.3/solidity-by-example.html#simple-open-auction)

* To implement our open auction smart contract let's take a look at how the solidity community recommends we do it based on the current version of solidity.

Begin by reading the description for the `Simple Open Auction`.

* "The general idea of the following simple auction contract is that everyone can send their bids during a bidding period. The bids already include sending money / ether in order to bind the bidders to their bid. If the highest bid is raised, the previously highest bidder gets her money back. After the end of the bidding period, the contract has to be called manually for the beneficiary to receive their money - contracts cannot activate themselves".

* We will take this contract and simplify it for our needs.

Now open [Remix](https://remix.ethereum.org/) and create a new contract named `SimpleAuction.sol`. Begin by adding the pragma and contract declarations.

```solidity
pragma solidity >=0.4.22 <0.6.0;

contract MartianAuction {
}
```

Next, define the variables that the contract will need to track its internal state.

```solidity
pragma solidity >=0.4.22 <0.6.0;

contract MartianAuction {

    // Current state of the auction.
    address payable public beneficiary;
    address public highestBidder;
    uint public highestBid;
}
```

* Inside our contract, we are going to start by defining some initial variables that will track the state of our auction.

* This consists of an

  * An `address payable public beneficiary` will be used to track the beneficiary of the contract.

  * An `address public highestBidder` will be used to keep track of the address of the current highestBidder.

  * A `uint public highestBid` will be used to track the current highest bid amount of the highest bidder.

Add a mapping of `addressses` to `uints` to track the pending returns of those that were outbid.

```solidity
    // Allowed withdrawals of previous bids
    mapping(address => uint) pendingReturns;
```

* Auction funds are all stored together in the contract's wallet; we need an easy way to keep track of who paid what.

* We are going to track this with a `mapping` that maps a bidder's `address` to the amount that they bid.

Define a public `bool` named `ended`.

```solidity
    bool public ended;
```

* We need a way to set when an auction's bidding period has closed and the auction has ended. We are going to track this with a pubic `bool` named ended.

Define the two events that we are going to use to log data for our frontend dApp.

```solidity
    // Events that will be emitted on changes.
    event HighestBidIncreased(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);

```

* This contract will serve as a backend store of information for an auction to easily communicate this information with our frontend we have to define some events.

* Whenever the highest bid amount increases we are going to call the `HighestBidIncreased` event and log the `address` of the bidder and the `amount`.

* Whenever an auction has ended we are going to call `AuctionEnded` and log the `winner` and the `winning bid amount`.

Define the contracts `constructor` and set the public `beneficiary` variable to the value of a `_beneficiary` parameter passed to the constructor.

```solidity
    constructor(
        address payable _beneficiary
    ) public {
        beneficiary = _beneficiary;
    }
```

* Upon deployment of a new instance of the `MartianAuction` contract a beneficiary or the person hosting the auction must be set. here we are going to define a constructor that will set the beneficiary.

Add a new `public` function defintion named `bid` for users to bid on the auction.

```solidity
function bid(address payable sender) public payable {
}
```

* An auction requires a method of bidding on an item within the auction.

* Here we are defining a `public payable` function named `bid` that accepts an `address` of the designated bidder the bidder can send funds to.

* Bidders will bid on the auction with the value sent and the value will only be refunded if the auction is not won.

Inside the `bid` function add the `require` check for if a sent bid is less than the current `highest bid`. If it is less, then we are going to send it back and not execute any further.

```solidity
        require(
            msg.value > highestBid,
            "There already is a higher bid."
        );
```

* Inside the `bid` function we are going to add a `require` to check if a sent bid is less than the current `highest bid`. If it is less, then we are going to send it back.

Add a second `require` check inside the `bid` function that will check the ended variable to see if the auction has ended.

```solidity
        require(!ended, "auctionEnd has already been called.");
```

* Remember the `ended` variable that we defined at the top of our contract, well we are going to add a second check inside our bid function that will check that `bool` value to see if the auction has ended.

* Remember that we can use the logical operator `!` or `not` to check if something is not the condition.

*, In this case, we are checking if our `ended` variable which is set to `false` by default is `not false` or `true`.

Add an `if statement` to check if there has been a previous bidder. Inside the body of the `if statement` add the current `highestBidder` to the `pendingReturns` mapping and map the current value of `highestBid` to that bidder's address.

```solidity
        if (highestBid != 0) {
            // Sending back the money by simply using
            // highestBidder.send(highestBid) is a security risk
            // because it could execute an un-trusted contract.
            // It is always safer to let the recipients
            // withdraw their money themselves.
            pendingReturns[highestBidder] += highestBid;
        }
```

* Thus far our bid function checks if an `incoming bid` is `higher` than the `current bid` and whether the `auction` has `ended`. If the `bid` is `higher` than the `current bid` and the `auction` has `not ended` then the next line of code will continue to execute.

* Now we need to save the previous bidders info so that they can withdraw their funds from the contract since they've been outbid.

* Before we can do this we need to check that there has first been a previous bidder. This is done by checking if the `highestBid` is `not equal to 0`.

Set the new `highestBidder` to the `address` passed from the `bid` function's `sender` parameter. Also set the new `highestBid` value to the `msg.value` sent to the bid function.

On the last line inside the `bid` function `emit` the `HighestBidIncreased` and pass it `sender` and the current `msg.value`

```solidity
        highestBidder = sender;
        highestBid = msg.value;
        emit HighestBidIncreased(sender, msg.value);
```

* To complete our bid function we need to set the new `highestBidder` equal to the `sender` parameter that was passed and the `highestBidder` equal to the amount sent to the bid function, eg, `msg.value`.

* Finally we `emit` the `HighestBidIncreased` event and pass it those two values as well.

Define a `pubic` function named `withdraw` that returns a `bool`.

```solidity
function withdraw() public returns (bool) {
}
```

* Currently we have a way to bid and even outbid other bidders. As you may remember when a bidder is outbid the amount that they originally bid is stored in `pendingReturns`. Now we need to create a way for them to return that amount to their account.

Inside the `withdraw` function start by defining a new `uint` named `amount` and set the value equal to that of the `mapped` value of `msg.sender` in the `pendingReturns` map.

Next, define a new `if statement` that checks if the amount variable is greater than 0. After the `if statment` return `true`.

```solidity
      uint amount = pendingReturns[msg.sender];
        if (amount > 0) {
        }
        return true;
```

* Inside the `withdraw` function we are first going to check the current amount that the person who is calling the withdraw function, eg, `msg.sender` has deposited into the contract. If the amount is not greater than 0 then there is nothing to withdraw and we return `true`.

Set the current `msg.sender's` mapped `uint` value inside `pendingReturns` to 0.

```solidity
            pendingReturns[msg.sender] = 0;
```

*  It is important to set this to zero because the recipient can call this function again as part of the receiving call before `send` returns.

Now define a nested `if statement` inside the first, in the condition statement call `msg.sender.send` and send the previously defined `amount` to them. Add a `not` operator in front of the statement to `negate` the value from `true` to `false`.

```solidity
if (!msg.sender.send(amount)) {
}
```

* We are now going to `send` our defined `amount` to the `address` of the `bidder` attempting to `withdraw`. To check whether or not the transaction errored out we are going to `negate` the output with a `!` operator. This will allow the `if statement` to check if `msg.sender.send` returns `false`.

Inside the nested `if statement` set the current `ms.sender`'s mapped `uint` value back to the value of `amount` and return `false`.

```solidity
         pendingReturns[msg.sender] = amount;
         return false;
```

* If the `msg.sender.send` fails and returns `false` we have to revert our change of zeroing out the current bidders owed balance and return the owed value to the previous amount.

Define a new `public` function named `pendingReturn`, this function will accept a `sender`'s `address` and returns that `sender`'s corresponding `pendingReturn amount` via the `pendingReturns` mapping.

```solidity
    function pendingReturn(address sender) public view returns (uint) {
        return pendingReturns[sender];
    }
```

* For ease of use let's define a new function named `pendingReturn`, this function will accept a `sender`'s `address` and returns that `sender`'s corresponding `pendingReturn amount` via the `pendingReturns` mapping.

Define a new `public` function named `auctionEnd`.

```solidity
    function auctionEnd() public {
    }
```

* Lastly we need some way to end the auction. let's define a new function named `auctionEnd`.

* This function will end the auction and send the highest bid to the beneficiary.

Inside the body of the `auctionEnd` contract define a `require` statement that will check if the auction has ended by negating the `ended` variable with the `!` operator. Then set the `ended` variable equal to `true` and `emit` the `AuctionEnded` event passing it the `highestBidder` and the `highestBid` variables. Finally, transfer the `highestBid` amount to the `beneficiary` using the `.transfer` address method.

```solidity
        // 1. Conditions
        require(!ended, "auctionEnd has already been called.");

        // 2. Effects
        ended = true;
        emit AuctionEnded(highestBidder, highestBid);

        // 3. Interaction
        beneficiary.transfer(highestBid);
```

* It is a good guideline to structure functions that interact with other contracts (i.e. they call functions or send Ether) into three phases:

  1. Checking conditions

  2. Performing actions (potentially changing conditions)

  3. Interacting with other contracts

  * If these phases are mixed up, the other contract could callback into the current contract and modify the state or cause effects (ether payout) to be performed multiple times.

  * If functions called internally include interaction with external contracts, they also have to be considered interaction with external contracts.

* Inside the body of the `auctionEnd` contract:

  * We are going to first check for the condition of whether or not the auction has ended by negating the `ended` variable with the `!` operator.

  * Next we are going to set ended equal to true to end the auction if it hasn't already ended, eg our perform our effects.

  * Finally, we are going to transfer the `highestBid` amount to the `beneficiary` using the `.transfer` address method.

Congratulations we have just built a `MartianAuction` contract, you may have very well just secured mankind's future.
