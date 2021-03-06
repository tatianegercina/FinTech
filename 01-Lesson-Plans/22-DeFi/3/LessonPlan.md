# 22.3 Lesson Plan

### Overview

In today's class, students will be introduced to auction contracts. Students will create an ERC721 token that leverages their created auction contracts in an internal mapping structure to facilitate the sale of `Auctionable Non-Fungible Martian Land Tokens`.

### Class Objectives

By the end of the class, students will be able to:

* Modify and Deploy an Auction contract written in Solidity.

* Use the .value function to pass Ether from one function to another in Solidity, and explain the difference between `.value`, `.call.value`, `.send`, and `.transfer`.

* Create an ERC721 token that leverages the Auction contracts in an internal mapping structure to create "Auctionable Non-Fungible Martian Land Tokens.

* Create a landing page that points to the Martian Land ERC721 dApp.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/12aqogAhj3QhOZfcmXCFAcOetHV2R27odqlCnAjqj2GY).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/presentation/d/1_BDSSZoS2qRvOOAZJvW0dtQVaJfvhtqYzjunIsDO02o).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

### Instructor Notes

* Refer to the [Solidity documentation for open auctions](https://solidity.readthedocs.io/en/v0.5.11/solidity-by-example.html#simple-open-auction).

* Have your TAs keep track of the [Time Tracker](TimeTracker.xlsx).

### 1. Instructor Do: Welcome to Class (10 min)

During the previous lecture, students were introduced to the thought process and techniques that go into taking a formalized contract spec and implementing it into solidity code.  Students learned to take a simple yet formalized smart contract specification and implement it to fit the interface of an already established frontend dApp. Students then deployed the configured dApp to a centralized production environment, Github pages.

Today students will once again be leveraging the Github Pages service to host their static dApp bundle.

Review the following recall questions with the class.

* What are some benefits of using Github pages?

  **Answer:** Quick and Easy Deployments.

  **Answer:** Free Static Web Hosting

  **Answer:** Free-SSL

  **Answer:** Integrated Version Control (Git)

* Why is having a documented/formalized API for your applications and libraries important?

  **Answer:** Improves clarity of what the application can do and how it works on a granular level.

  **Answer:** Helps set forth standards from and for your given implementation. (like `EIPS` and `ERCS`)

  **Answer:** Facilitates code hand-offs between team members and increases collaboration.

* Having written many smart contracts, and now deployed a dApp, what are some contracts that you believe could be leveraged within a dApp?

  **Potential Answer:** A contract that tracks the immutable locations of historical landmarks.

  **Potential Answer:** A contract that transfers tokens between two users within a decentralized product swapping website.

  **Potential Answer:** Maintain an immutable achievement list of users' achievements within an online course dApp.

  **Potential Answer:** Any other dApp or smart contract that you can think of—the Ethereum blockchain is a globally distributed data store and supports Turing-complete programming languages.

### 2. Instructor Do: Auction Contracts in Solidity (10 min)

**Corresponding Activity:** [01-Ins_Auction_Contracts_in_Solidity](Activities/01-Ins_Auction_Contracts_in_Solidity)

In this activity, the Instructor will demonstrate the various Auction contracts available from the Solidity example documentation, and modify it to fit our needs. Students will be introduced to the story of the "Martian Land Foundation" and how we will be "tokenizing" martian land and auctioning it to the public, raising funds for the Martian Land Foundation's terraforming projects, and allowing every-day citizens to claim their spot on humanity's next frontier.

**Files:**

* [MartianAuction.sol](Activities/01-Ins_Auction_Contracts_in_Solidity/Solved/MartianAuction.sol)

Begin the activity by introducing the class to the backstory of the `Martian Land Foundation`.

* You are a smart contract engineer on a team of elite developers hired by the martian land foundation to build a system that will crowdfund the development of a new colony on Mars. To accomplish this goal and help humanity thrive on Mars, you have communicated with your project manager, gathered the necessary business requirements, and have decided to leverage an `Open Auction Smart Contract`.

Next open the [Solidity open auction contract documentation](https://solidity.readthedocs.io/en/v0.5.3/solidity-by-example.html#simple-open-auction)

* To implement our open auction smart contract, let's take a look at how the solidity community recommends we do it based on the current version of solidity.

Begin by reading the description for the `Simple Open Auction`.

* "The general idea of the following simple auction contract is that everyone can send their bids during a bidding period. The bids already include sending money/ether in order to bind the bidders to their bid. If the highest bid is raised, the previously highest bidder gets her money back. After the end of the bidding period, the contract has to be called manually for the beneficiary to receive their money - contracts cannot activate themselves".

* We will take this contract and simplify it for our needs.

Now open [Remix](https://remix.ethereum.org/) and create a new contract named `MartianAuction.sol`. Begin by adding the pragma and contract declarations.

```solidity
pragma solidity >=0.4.22 <0.6.0;

contract MartianAuction {
}
```

Next, define the variables that the contract will need to track its internal state.

```solidity
pragma solidity >=0.4.22 <0.6.0;

contract MartianAuction {

    address deployer;

    // Current state of the auction.
    address payable public beneficiary;
    address public highestBidder;
    uint public highestBid;
}
```

* Inside our contract, we are going to start by defining some initial variables that will track the state of our auction.

* This consists of:

  * An `address deployer` that will be used to track the address of the contract that deploys the `MartianAuction`.

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

* We need a way to set when an auction's bidding period has closed, and the auction has ended. We are going to track this with a pubic `bool` named ended.

Define the two events that we are going to use to log data for our frontend dApp.

```solidity
    // Events that will be emitted on changes.
    event HighestBidIncreased(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);

```

* This contract will serve as a backend store of information for an auction to easily communicate with our frontend, we have to define some events.

* Whenever the highest bid amount increases, we are going to call the `HighestBidIncreased` event and log the `address` of the bidder and the `amount`.

* Whenever an auction has ended, we are going to call `AuctionEnded` and log the `winner` and the `winning bid amount`.

Define the contracts `constructor` and set the public `beneficiary` variable to the value of a `_beneficiary` parameter passed to the constructor.

```solidity
    constructor(
        address payable _beneficiary
    ) public {
        deployer = msg.sender;
        beneficiary = _beneficiary;
    }
```

* Upon deployment of a new instance of the `MartianAuction` contract, a beneficiary, or the person hosting the auction, must be set. Here we are defining a constructor that will set the beneficiary.

* We also set the `deployer` address to the `msg.sender` in order to track the address of the contract that will be deploying this one. This is so we can make sure that certain privileged functions (like ending the auction) can only be called from the parent contract that created this one.

Add a new `public` function definition named `bid` for users to bid on the auction.

```solidity
function bid(address payable sender) public payable {
}
```

* An auction requires a method of bidding on an item within the auction.

* Here we are defining a `public payable` function named `bid` that accepts an `address` of the designated bidder the bidder can send funds to.

* Bidders will bid on the auction with the value sent, and the value will only be refunded if the auction is not won.

Inside the `bid` function, add the `require` check for if a sent bid is less than the current `highest bid`. If it is less, then we are going to send it back and not execute any further.

```solidity
        require(
            msg.value > highestBid,
            "There already is a higher bid."
        );
```

* Inside the `bid` function, we are going to add a `require` to check if a sent bid is less than the current `highest bid`. If it is less, then we are going to send it back.

Add a second `require` check inside the `bid` function that will check the ended variable to see if the auction has ended.

```solidity
        require(!ended, "auctionEnd has already been called.");
```

* Remember the `ended` variable that we defined at the top of our contract? We are going to add a second check inside our bid function that will check that `bool` value to see if the auction has ended.

* Remember that we can use the logical operator `!` or `not` to check if something is not the condition.

* In this case, we are checking if our `ended` variable, which is set to `false` by default is `not false` or `true`.

Add an `if statement` to check if there has been a previous bidder. Inside the body of the `if statement`, add the current `highestBidder` to the `pendingReturns` mapping and map the current value of `highestBid` to that bidder's address.

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

* Thus far, our bid function checks if an `incoming bid` is `higher` than the `current bid` and whether the `auction` has `ended`. If the `bid` is `higher` than the `current bid` and the `auction` has `not ended` then the next line of code will continue to execute.

* Now we need to save the previous bidders info so that they can withdraw their funds from the contract since they've been outbid.

* Before we can do this, we need to check that there has first been a previous bidder. This is done by checking if the `highestBid` is `not equal to 0`.

Set the new `highestBidder` to the `address` passed from the `bid` function's `sender` parameter. Also set the new `highestBid` value to the `msg.value` sent to the bid function.

On the last line inside the `bid` function `emit` the `HighestBidIncreased` and pass it `sender` and the current `msg.value`

```solidity
        highestBidder = sender;
        highestBid = msg.value;
        emit HighestBidIncreased(sender, msg.value);
```

* To complete our bid function, we need to set the new `highestBidder` equal to the `sender` parameter that was passed and the `highestBidder` equal to the amount sent to the bid function, e.g., `msg.value`.

* Finally we `emit` the `HighestBidIncreased` event and pass it those two values as well.

Define a `pubic` function named `withdraw` that returns a `bool`.

```solidity
function withdraw() public returns (bool) {
}
```

* Currently, we have a way to bid and even outbid other bidders. As you may remember, when a bidder is outbid, the amount that they originally bid is stored in `pendingReturns`. Now we need to create a way for them to return that amount to their account.

Inside the `withdraw` function, start by defining a new `uint` named `amount` and set the value equal to that of the `mapped` value of `msg.sender` in the `pendingReturns` map.

Next, define a new `if statement` that checks if the amount variable is greater than 0. After the `if statement` return `true`.

```solidity
      uint amount = pendingReturns[msg.sender];
        if (amount > 0) {
        }
        return true;
```

* Inside the `withdraw` function, we are first going to check the current amount that the person who is calling the withdraw function, e.g., `msg.sender` has deposited into the contract. If the amount is not greater than 0, then there is nothing to withdraw, and we return `true`.

Inside the `if stament` set the current `msg.sender's` mapped `uint` value from `pendingReturns` to 0.

```solidity
            pendingReturns[msg.sender] = 0;
```

*  It is important to set this to zero because the recipient can call this function again as part of the receiving call before `send` returns.

Now define a nested `if statement` inside the first, in the condition statement call `msg.sender.send` and send the previously defined `amount` to them. Add a `not` operator in front of the statement to `negate` the value from `true` to `false`.

```solidity
if (!msg.sender.send(amount)) {
}
```

* We are now going to `send` our defined `amount` to the `address` of the `bidder` attempting to `withdraw`. To check whether or not the transaction errored out, we are going to `negate` the output with a `!` operator. This will allow the `if statement` to check if `msg.sender.send` returns `false`.

Inside the nested `if statement` set the current `ms.sender`'s mapped `uint` value back to the value of `amount` and return `false`.

```solidity
         pendingReturns[msg.sender] = amount;
         return false;
```

* If the `msg.sender.send` fails and returns `false`, we have to revert our change of zeroing out the current bidders owed balance and return the owed value to the previous amount.

Define a new `public` function named `pendingReturn`, this function will accept a `sender`'s `address` and returns that `sender`'s corresponding `pendingReturn amount` via the `pendingReturns` mapping.

```solidity
    function pendingReturn(address sender) public view returns (uint) {
        return pendingReturns[sender];
    }
```

* For ease of use, let's define a new function named `pendingReturn`, this function will accept a `sender`'s `address` and returns that `sender`'s corresponding `pendingReturn amount` via the `pendingReturns` mapping.

Define a new `public` function named `auctionEnd`.

```solidity
    function auctionEnd() public {
    }
```

* Lastly, we need some way to end the auction. Let's define a new function named `auctionEnd`.

* This function will end the auction and send the highest bid to the beneficiary.

Inside the body of the `auctionEnd` contract:

  * Define a `require` statement that will check if the auction has ended by negating the `ended` variable with the `!` operator.

  * Below that, define a second `require` statement that checks to see if `msg.sender` is equal to `deployer`. This will ensure that only the deploying contract can call this function.

  * Then set the `ended` variable equal to `true`.

  * `Emit` the `AuctionEnded` event passing it the `highestBidder` and the `highestBid` variables.

  * Transfer the `highestBid` amount to the `beneficiary` using the `.transfer` address method.

```solidity
        // 1. Conditions
        require(!ended, "auctionEnd has already been called.");
        require(msg.sender == deployer, "You are not the auction deployer!");

        // 2. Effects
        ended = true;
        emit AuctionEnded(highestBidder, highestBid);

        // 3. Interaction
        beneficiary.transfer(highestBid);
```

* It is a good guideline to structure functions that interact with other contracts (i.e., they call functions or send Ether) into three phases:

  1. Checking conditions

  2. Performing actions (potentially changing conditions)

  3. Interacting with other contracts

  * If these phases are mixed up, the other contract could callback into the current contract and modify the state or cause effects (ether payout) to be performed multiple times.

  * If functions called internally include interaction with external contracts, they also have to be considered interaction with external contracts.

* Inside the body of the `auctionEnd` contract:

  * We are going to first check for the condition of whether or not the auction has ended by negating the `ended` variable with the `!` operator.

  * A second require is defined to check if the `msg.sender` attempting to end the auction is equal to the `deployer` running the auction.

  * Next, we are going to set `ended` equal to true to end the auction if it hasn't already.

  * Finally, we are going to transfer the `highestBid` amount to the `beneficiary` using the `.transfer` address method.

Congratulations, we have just built a `MartianAuction` contract; you may have very well just secured mankind's future.

### 3. Students Do: Writing an Auction Contract (15 min)

**Corresponding Activity:** [02-Stu_Writing_an_Auction_Contract](Activities/02-Stu_Writing_an_Auction_Contract)

In this activity, students will take a SimpleAuction contract from the Solidity documentation, modify it for their own needs (remove the time-related features), and prepare it for use within another contract.

**Instructions:**

* [README.md](Activities/02-Stu_Writing_an_Auction_Contract/README.md)

**Files:**

* [MartianAuction.sol](Activities/02-Stu_Writing_an_Auction_Contract/Unsolved/MartianAuction.sol)

### 4. Instructor Do: Writing an Auction Contract Review (15 min)

**Files:**

* [MartianAuction.sol](Activities/02-Stu_Writing_an_Auction_Contract/Solved/MartianAuction.sol)

Review the code from the previous activity with the class.

Now discuss the following recall questions:

* What are some additional features that you believe could add useful functionality to this contract?

  **Potential Answer:** The ability to re-open bids.

  **Potential Answer:** The ability to rebid at a higher price without additional transactions.

  **Potential Answer:** The ability to set a minimum bid price.

  **Potential Answer:** The ability to set a max bid price.

  **Potential Answer:** A buy now at market price feature.

* Are there any other events that you think this contract could benefit from having?

  **Answer:** An event that is emitted when the auction opens.

  **Answer:** An event that is emitted when funds are withdrawn.

### 5. Instructor Do: The MartianMarket (ERC721 + Auctions) (15 min) (Critical)

**Corresponding Activity:** [03-Ins_Martian_Market](Activities/03-Ins_Martian_Market)

In this activity, you will be demonstrating combining the ERC721 standard with the modified `MartianAuction` contract that was built in the previous activity.

**Files:**

* [MartianAuction.sol](Activities/03-Ins_Martian_Market/Resources/MartianAuction.sol)

* [MartianMarket.sol](Activities/03-Ins_Martian_Market/Solved/MartianMarket.sol)

First, explain to the students:

* We are going to be creating an ERC721 token with the ticker `MARS`. Only one entity will be allowed to create the tokens, and that entity in this example is called the "Martian Land Foundation." Assume this foundation is a global initiative from the governments of the world and is responsible for the terraforming and fundraising of Martian Land Development.

* For every token that the Martian Land Foundation mints, an `Auction` contract will be created. This auction contract will become the new owner of the token and will allow the public to bid on that piece of land. In the spirit of humanity, some landmarks will be marked as "sovereign" and will become permanently owner-less.

* The Martian Land Foundation can end the auctions at any time.

Open up [Remix](https://remix.ethereum.org) and create a new file called `MartianMarket.sol` and populate it with the contents of the [starter code](Activities/03-Ins_Martian_Market/Unsolved/MartianMarket.sol).

The beginning of the contract should look something like:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/ownership/Ownable.sol";
import "./MartianAuction.sol";

contract MartianMarket is ERC721Full, Ownable {

    constructor() ERC721Full("MartianMarket", "MARS") public {}
}
```

* In this contract, we are simply defining an ERC721 token contract called `MartianMarket` with the ticker of `MARS`. Each `MARS` token will represent a plot of land/landmark on Mars.

* We are importing the `MartianAuction` code as well since we will want to create a new auction for every new token.

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

* This is done by calling the `_exists` function that is built into OpenZeppelin's ERC721 library and returning the message `Land not registered!` if it doesn't. We can attach this modifier to any function that we expect a token to exist with, like bidding on an auction, or transferring ownership of land.

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

* All three of these functions are simply "forwarding" value from the `MartianAuction` to the `MartianMarket` interface. We can use them to introspect any activity happening to the auctions we have going for any token.

Finally, we need to create our last function, `bid`:

```solidity
    function bid(uint token_id) public payable landRegistered(token_id) {
        MartianAuction auction = auctions[token_id];
        auction.bid.value(msg.value)(msg.sender);
    }
```

* While this function starts out the same as the others, it is doing something a bit special. The first thing to notice is that it is set to `payable`. Meaning, we are going to expose this function to allow users to bid on specific `MARS` land tokens by sending Ether to this function, and forwarding it to the `MartianAuction`'s `bid` function.

* In order to forward the Ether sent from one function to another, we have to use a special `.value()` syntax. All we need to do is add `.value()` *before* the parameters of any function.

* For example, `auction.bid(msg.sender)` is the normal syntax. However, this only passes in the `sender` address parameter that the `MartianAuction` expects. The actual Ether attached to the transaction would be left behind. By adding `.value(msg.value)` right before the normal parenthesis that includes our parameters, we are sending the entire `msg.value` to the `auction.bid` function!

* We must be careful about this syntax, as it only forwards `2300` gas. Since that's enough to complete our function, we're okay. Otherwise, we'd have to add `.call` right before `.value()`, but that syntax doesn't protect against reentrancy attacks, so we'd need to be very careful about modifying the state of our contract in that case.

Make sure your contract compiles and matches the [solution](Activities/03-Ins_Martian_Market/Solved/MartianMarket.sol). The next activity includes a frontend that expects the same ABI.

Voila! Now it's time for the students to build out the same system.

### 6. Students Do: Building the MartianMarket (20 min)

**Corresponding Activity:** [04-Stu_Building_Martian_Market](Activities/04-Stu_Building_Martian_Market)

In this activity, students will be building the ERC721 + Auction based `MartianMarket`.

Have TAs circulate the room and ensure students can complete the activity.

**Instructions:**

* [README.md](Activities/04-Stu_Building_Martian_Market/README.md)

**Files:**

* [MartianMarket.sol](Activities/04-Stu_Building_Martian_Market/Unsolved/MartianMarket.sol)

* [MartianAuction.sol](Activities/04-Stu_Building_Martian_Market/Resources/MartianAuction.sol)

### 7. Instructor Do: MartianMarket Review (10 min)

**Files:**

* [MartianMarket.sol](Activities/04-Stu_Building_Martian_Market/Solved/MartianMarket.sol)

* [MartianAuction.sol](Activities/04-Stu_Building_Martian_Market/Resources/MartianAuction.sol)

Open the solution and review the `MartianMarket` code. Make sure to explain the following:

* In the `bid` function, we are using the `.value` syntax.

  * We must be careful about this syntax, as it only forwards `2300` gas. Since that's enough to complete our function, we're okay. Otherwise, we'd have to add `.call` right before `.value()`. That forwards the remaining gas, but that syntax doesn't protect against reentrancy attacks, so we'd need to be very careful about modifying the state of our contract in that case.

Ask the students:

* If we needed to drop down to the lower level `.call.value` syntax, how could we prevent a reentrancy attack?

  **Answer:** We'd need to set any state that limits an Ether withdrawal before calling the external function. Like in the `MartianAuction` contract, we set the `pendingReturns` for the address that is calling the `withdraw` function *before* calling `.send`. If we're able to get our function to `re-enter`, the check would know they already withdrew and stop the function from sending more Ether.

* What are some ways we can improve the logic of the `MartianMarket`? Can we make it more decentralized? How?

  **Answer:** We could implement a voting system to manage the `Martian Land Foundation` in a decentralized way, like a `DAO`.

  **Answer:** We could use a voting system to decentralize the process of land registration.

  **Answer:** We could re-introduce the time limit factor to the auction and tweak it to our preferences.

Ask for any remaining questions before moving on.

### 8. Students Do: Deploying the MartianMarket (20 min)

**Corresponding Activity:** [05-Stu_Deploying_Martian_Market](Activities/05-Stu_Deploying_Martian_Market)

In this challenge activity, students will create a landing page and deploy the MartianMarket dApp to Github Pages. The frontend will be provided in a similar fashion to `CryptoRight`. Students will leverage their skills to put together their dApp, create a detailed landing page, and deploy to GitHub Pages.

Send the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/05-Stu_Deploying_Martian_Market/README.md)

**Files:**

* [index.html](Activities/05-Stu_Deploying_Martian_Market/Resources/martian_market/frontend/index.html)

* [dapp.js](Activities/05-Stu_Deploying_Martian_Market/Resources/martian_market/frontend/dapp.js)

* [MartianMarket.json](Activities/05-Stu_Deploying_Martian_Market/Resources/martian_market/frontend/MartianMarket.json)

* [MartianAuction.json](Activities/05-Stu_Deploying_Martian_Market/Resources/martian_market/frontend/MartianAuction.json)

Ensure the following:

* Students have built their `MartianMarket` contracts exactly like the provided examples.

* The ABI `JSON` files, `dapp.js`, `index.html` are all within the `frontend` folder.

* The `README.md` is one directory above the `frontend` folder. The directory that contains the `README.md` should be the folder used to initialize and push the Git repo.

* Students are working with a **freshly** deployed `MartianMarket` contract.

* Students have a link from their `README.md` to the `frontend/index.html` of their dApp.

* Students are putting effort into the summary and presentation of their landing page.

### 9. Instructor Do: dApp Review (10 min)

Walkthrough the following recall questions with the class to review the various technologies/levels of the stack and their purpose:

* What is the purpose of having a Github Pages website for our dApp?

  **Answer:** It allows us to demonstrate our expertise in a context that we can control.

  **Answer:** It allows us to write documentation websites, explain the purpose of our project, gain developer and user traction, and much more.

* What are some benefits of Solidity Events?

  **Answer:** They have a lower gas cost.

  **Answer:** They allow you to keep a log of information on-chain.

  **Answer:** Events are MUCH cheaper than contract storage.

  **Answer:** Events are Solidity's built-in way to interact with something external, such as a user interface.

* What are some potential issues that IPFS seeks to solve?

  **Answer:** Inefficiencies in the web, such as duplicate files.

  **Answer:** Inefficiencies on the web, such as having to route to a faraway server to get the file you need when it might be right next door.

  **Answer:** Problems with security and file integrity, such as not knowing whether or not files you have accessed over the web have changed.

  **Answer:** Problems with the security of centralized servers providing a centralized attack vector.

---

### 10. BREAK (40 min)

---

### 11. Student Do: Project Work Session (50 mins)

Welcome the students back to class, and allow them to use this activity time to work on their projects.


### 12. Instructor Do: Career Services (35 min)

**Note:** If you are teaching this lesson on a weeknight, save this section for the next Saturday class.

* In this Career Services section, you will discuss with the students the importance of writing a high-quality and effective `README` for each project.

* There's no universal standard in what to include in a `README`, but we do know from speaking to employers the kinds of things they're looking for, and the sort of `READMEs` that are effective.

#### Instructor Do: Introduction to READMEs (5 min)

* Ask the class the following questions (☝️) and call on students for the answers (🙋):

  * ☝️What is a `README` file?

  * 🙋A text file written using Markdown that describes the repository, what it does, how to use it, who built it etc.

  * ☝️ Why are they important when job-seeking?

  * 🙋 It is the first impression recruiters and prospective employers will have of our projects.

  * ☝️And what should we include in order to make it a good, high-quality `README` that we would want employers to see?

  * 🙋A `README` should include a project title, technologies, installation guide, screen shots / examples, instructions on how to use it, contributors, and a license.

* Show students how to pin a repository in GitHub. Navigate to `www.github.com/<yourUsername>` and click `Customize your pins`:

![customize.png](Images/customize.png)

* Then select the pins you would like to show on the main page of your profile.

* Let students know this allows recruiters to more easily find the repositories you want them to look at!

#### Students Do: Compare and Review (10 min)

* In this activity, students will compare three `README` files and write down the differences they note between them.

* Using `06-Stu_Compare_README`, ask students to compare [SAMPLE_1.md](Activities/06-Stu_Compare_README/SAMPLE_1.md),
[SAMPLE_2.md](Activities/06-Stu_Compare_README/SAMPLE_2.md),
and [SAMPLE_3.md](Activities/06-Stu_Compare_README/SAMPLE_3.md) and note the differences they see.

* Slack out the instruction file for the activity and these three sample files.

#### Instructor Do: Review ReadMe (5 min)

* Ask the class the following questions (☝️) and call on students for the answers (🙋):

* Pull up `sample_1/README.md` to show to students.

  * ☝️ What did we think of this README?

  * 🙋 Terrible!
    * No creative title
    * No subsections containing relevant data
    * The developer refers to themself as "me"
    * No images

* Pull up `sample_2/README.md` and `sample_3/README.md` to compare.

  * ☝️ Which of the two do we prefer?

  * 🙋 Number 3!

  * ☝️ OK, and why?

  * 🙋 It's better because it has a unique app title and subsections but:
    * the images are broken
    * No installation guide
    * No license
    * No LinkedIn

#### Students Do: Create Readme (15 min)

* For the remaining 15 minutes, ask students update their Project #2 `README`. They should feel free to add other elements that they think will be useful for people to know about their project.

* If they finish early, or have already updated their Project #1 and Project #2 `README` files, ask students to move on to updating any homework `README` files that need additional details.



---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
