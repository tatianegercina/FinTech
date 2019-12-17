## 21.1 Lesson Plan: Advanced Solidity

### Overview

In today's class, students will be introduced to the concept of tokens on the Ethereum blockchain.

Students will learn more advanced Solidity data structures, what tokens are, and how to use them.

---

### Class Objectives

By the end of the unit, students will be able to:

* Explain what gives tokens (digital assets) value, and the different mechanisms in which tokens may be collateralized.

* Distinguish the general difference between a `coin` and a `token` in the context of crypto.

* Use the mapping data structure to associate customer addresses with their individual information.

* Build a simple token on the ETH blockchain.

* Import 3rd party OpenZeppelin libraries from Github within Solidity.

* Use the SafeMath library to perform secure math operations.

* Build a simple tokenized reward system in Solidity that distributes tokens to users based on their actions.

* Design smart contracts that can replace traditional business mechanisms.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1devzesQ1UKT2weYAz43Ei9YBIM863dYDtw9IFIMfLis/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).


---

### Instructor Notes

* Today's class will be a challenging one as student start to dig deeper into advanced Solidity concepts. Take plenty of time to cover and review the new concepts in today's class.

* Reassure students that as they practice Solidity, they will begin to see common patterns in the code. Many of the examples show this week can be reused in other smart contract applications.

* Refer to OpenZeppelin Safe Math documentation for further information about functions. [Safe Math Docs](https://docs.openzeppelin.com/contracts/2.x/api/math)

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Back (10 min)

Take a few minutes to discuss the following recall questions with the class.

* Before we move on to new and advanced concepts in Solidity, let's review some of the basics that we already know.

  * **Answer** Solidity is:

  * A high-level object-oriented programing language.

  * It is the language used to write smart contracts on the Ethereum blockchain.

  * Is strictly typed.

* What is a `uint`?

  * **Answer:** Unsigned Integer.

* What is the difference between an `int` and a `uint`?

  * **Answer:** `int` can be positive and negative, `uint` is positive only.

* Why is Solidity so strict with its typing?

  * **Answer:** It allows for better error handling in code.

  * **Answer:** Contracts should not leave room for ambiguity.

  * **Answer:** Being upfront about data types and the size to store them results in less computational overhead/gas costs.

* What is a `payable` address, and why is it different from a regular address?

  * **Answer:** A payable address is like a normal address type, except it allows the `.transfer` function to be called in order to send it Ether.

* What is a potential benefit of executing code in a virtual machine?

  * **Answer** The code executed in a virtual machine cannot affect the host machine directly.

  * **Answer** The code can run anywhere the virtual machine can run.

---

### 2. Instructor Do: Intro to Tokenomics (10 min)

This activity will introduce the idea of `Tokenomics,` the nature of tokens on the blockchain and what gives them value, the loose definitions of coins and tokens, as well as several examples.

Begin by giving the students some background on tokens and how they can be utilized within a blockchain platform to represent an asset, digital or physical.

* Tokens are used to represent an asset or utility on a blockchain platform.

* You can tokenize things like gold, silver, the USD, real-estate, your car, artwork, property, and virtually anything that holds some value.

* Since tokens are built using smart contracts they can be programmed to do many things besides just payments.

* By tokenizing things, we can make representing and trading value extremely easy and efficient. Since they are blockchain powered, these tokens can be traded globally without any additional infrastructure.

* Representing commodities as tokens allows for easy transportation of ownership. For example, transferring a metric ton of gold takes a lot of energy. Sending tokens representing that metric ton of gold is much easier, and allows for the same borderless nature given by the blockchain.

* Imagine opening up your cryptowallet to see all the various assets you own in a single place, digital and physical. You could manage your house ownership, car payments, artwork, investments, video game items, and more with cryptographically provable math.

* Business assets can easily be tracked and transferred, dramatically improving liquidity and auditability.

* Items you purchase at a grocery store can even be tokenized, allowing you to scan a code on your groceries to pull up the entire supply chain history of that item, allowing you to prove exactly where it came from.

* Stablecoins are tokens designed to have stable value; unlike traditional cryptocurrencies, they are not as volatile since they are backed by fiat (government) currencies.

* Stablecoins normally hold USD within bank accounts and then issue tokens backed by these dollars.

Clarify that `coins` are the cryptocurrencies native to the blockchain, coins like `BTC` and `ETH`, while `tokens` are generally built on top of existing blockchain platforms.

Additionally, clarify that the previous statement is a loose definition, and you may hear people using the terms coin and token interchangeably.

Now it's time for students to explore some tokens themselves!

---

### 3. Students Do: Token Exploration (10 min)

Students will take the given activity time to research their selected tokens.

Have the students open the following list of popular Ethereum blockchain tokens and select a few that interest them.

**Instructions:**

* [README.md](Activities/03_Stu_Token_Exploration/README.md)

---

### 4. Instructor Do: Review Questions (5 min)

Discuss the following review questions with the class.

* What are some potential differences between `coins` and `tokens`?

  * **Answer** Tokens are often built on top of a blockchain platform, whereas coins usually have their own blockchain.

  * **Answer** A token is programmed with a smart contract.

* What are some potential similarities between `coins` and `tokens`?

  * **Answer** Both coins and tokens can represent value.

  * **Answer** Both coins and tokens utilize a blockchain on some level.

  * **Answer** Both coins and tokens can have a fixed or infinite amount of supply, depending on the system.

  * **Answer** Both coins and tokens can be used to implement a stablecoin.

  What are some real-world use cases that you discovered while researching popular tokens?

  * **Potential Answers**

  * **BAT** - seeking to address fraud in advertising, basic attention is an open-source, decentralized ad platform that allows advertisers to pay website publishers for the attention of users.

  * **0x** - a protocol that allows the creation of decentralized crypto exchanges on the Ethereum blockchain using smart contracts for negotiation between users.

  * **Tether (USDT)** - is a controversial token that was one of the original stablecoins. Each `USDT` is backed by either a United States Dollar or a Loan and is managed by the Tether company.

  * **Hedge** - a platform that creates a market for knowledge on best trading practices, allows users to trade their current market analysis for an equivalent amount of value.

  * **Vechain** - "VeChain offers a Blockchain-as-a-Service (`BaaS`) platform called ToolChain. ToolChain offerers services like product lifecycle management, supply chain process control, data deposit, data certification, and process certification to enterprise companies like Walmart.

  * **Maker Dao (Dai)** - Dai is a token but also a `stablecoin`, this means 1 Dai = $1. Instead of having a central company back the fiat, the MakerDAO converts Ether to the Dai stablecoin. This creates a 1:1 parity with the USD, without a central authority, just smart contracts!

  * **Golem (GNT)** - is a token that you use to pay for rentable computing power on the Golem network. It allows you to pay for computations that occur outside of Ethereum, like GPU access or other hardcore number-crunching jobs.

---

### 5. Instructor Do: Mappings Data Structure in Solidity (15 min) (Critical)

This activity shows students how to build a simple token with Solidity.

**Files:**

* [ArcadeToken.sol](Activities/05-Ins_Mappings/Unsolved/ArcadeToken.sol)

Now that we are familiar with the concept of tokens, let's build one!

* In order to build a token with Solidity, we need to learn one more data structure, called a `mapping`.

* You can think of a mapping as a `mapping` between two variables. For instance, you can *map* an address to a balance.

* You can map a customer ID to an address, or vice versa. They can even be nested, but we won't need to do that.

Open up Remix and create a new contract called `ArcadeToken.sol`.

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

Note, this contract is currently vulnerable to something called an `integer underflow` attack and allows users to spend tokens they do not have. If students notice this, simply explain that we will add more security features later today to prevent spending with zero token balance.

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

---

### 6. Students Do: Building an Arcade Token with Mappings (20 min)

In this activity, students will practice using the `mapping` data structure by building an ArcadeToken.

Send out the instructions and the starter code below, and have the TAs circulate the class.

**Instructions:**

* [README.md](Activities/06-Stu_ArcadeToken/README.md)

**Files:**

* [ArcadeToken.sol](Activities/06-Stu_ArcadeToken/Unsolved/ArcadeToken.sol)

Ensure that students are using the mapping to map `address` to `uint` specifically.

If students are confused about how the `exchange_rate` works, remind them:

* By multiplying the `exchange_rate` with the `msg.value`, you are effectively multiplying the amount of `wei`, the smallest denomination of Ether, which is stored in a `uint`. We will learn how to calculate Ether values later this week, but operating on `wei` gives absolute precision.

For students that are confused about `mapping`:

* Mapping simply associates one data type to another. By pairing `address` to `uint`, we can track balances.

  * For example, `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333` is what the data might look like in contract storage.

---

### 7. Instructor Do: ArcadeToken Review (10 min)

**Files:**

* [ArcadeToken.sol](Activities/06-Stu_ArcadeToken/Solved/ArcadeToken.sol)

Open the solution and explain the following:

* By setting our mapping to `mapping(address => uint) balances` we are able to track address balances by setting the `uint` that is paired to any address.

* Since all types are set to `0` by default, we don't need to worry about initializing any balances. We can simply set them as people use the token.

* We can access our balance from the `balances` function by returning `balances[msg.sender]`. This is a very similar format to how we would access a dictionary in Python.

* In our `transfer` function, we simply subtract the value from the sender's balance in the `balances mapping` and add it to the recipient's.

* By setting an `exchange_rate`, we can reward/create tokens based on how much `wei` is sent to the `purchase` function, and then collect the Ether for ourselves, automatically!

* In our `mint` function, we restrict the function to only allow ourselves (the `owner`) to create new tokens when we need to.

Ask for any remaining questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to the class. Allow them to settle in while asking a few recall questions:

* What is a `mapping`?

  * **Answer:** A pair of types.

* Why do we use it in our token?

  * **Answer:** It allows us to map `address` to `uint`, so we can set balances associated with addresses.

* What is the limit for how much we can store in a `mapping`?

  * **Answer:** There is no set cap, but we are limited by gas prices and gas limits of the current state of the blockchain network.

Get the students excited about the next activity by explaining how we are now going to secure our tokens from a vulnerability that allows users to spend tokens they don't have!

---

### 10. Instructor Do: 3rd Parties Libraries in Solidity (SafeMath) (15 min) (Critical)

This demonstration shows students how to use the `SafeMath` from `OpenZeppelin` to secure their tokens.

**Files:**

* [ArcadeTokenSafeMath.sol](Activities/10-Ins_SafeMath/Unsolved/ArcadeTokenSafeMath.sol)

Now it's time to make our tokens more secure. Briefly explain to the class:

* The tokens that we have created so far are not actually secure.

* We can make these secure by using a library called `SafeMath` from OpenZeppelin.

First, show students how a contract is vulnerable to rewarding infinite tokens via an `integer underflow` exploit. Here's an example in-action:

![Hacked Balance GIF](Images/hacked_balance.gif)

Continue with the `ArcadeToken.sol` contract. It should match the unsolved file below at this point.

In the `Deploy` tab in Remix, deploy a new version of the contract to ensure that your account has an `ARCD` balance of `0`.

Then, expand the `transfer` function to expose the parameter inputs:

![Redeploy ArcadeToken](Images/redeploy.gif)

Fill in any address that is **different** from the current account in the `recipient` field, and a value of `1` in the `value` field:

![Vulnerable Transfer](Images/arcade_token_vulnerable_transfer.png)

Hit `Transact`, confirm the transaction in MetaMask, then click on the `balance` function in the contract.

You will notice that you have an extremely high balance of tokens, in fact, the maximum balance you could possibly have!

![Hacked Balance](Images/hacked_balance.png)

Ask the class:

* Can anyone spot the vulnerability in our code that allows this to happen?

Allow the students to give their answers, then confirm:

* We are subtracting the balance from the `msg.sender` without checking if there is enough first!

* When we subtract `1` from a `uint` that is set to `0`, we actually perform something called an "integer underflow."

* Imagine if you took a car's odometer (mileage tracker) and cranked it to the maximum value it could support. What would happen when you reached mile `999999999...`? It would reset back to `0`. That's an integer overflow.

* An underflow is the opposite, when we subtract `1` from `0`, we roll it back to the maximum value that can fit inside a `uint`. By default, most programming languages behave this way. It's up to us to make sure that does not happen.

Ensure the students understand the concept of an underflow/overflow and how it allows us to hack an insecure contract, then move on.

* Thankfully, there are libraries out there that allow us to write more secure smart contracts.

Introduce the OpenZeppelin project, and the SafeMath library:

* The OpenZeppelin project contains many standardized smart contracts and templates to help the community build off of. This allows developers to write more secure and efficient Solidity code.

* To fix our contract, we can leverage the SafeMath library provided by OpenZeppelin.

* The SafeMath library provides the guardrails we need to prevent integer underflows and overflows and similar vulnerabilities.

Navigate back to Remix and edit the `ArcadeToken` contract.

Import the SafeMath library at above the contract definition like so:

```solidity
pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/math/SafeMath.sol";

contract ArcadeToken {
    // ...
}
```

* Remix supports importing libraries straight from Github. It will automatically resolve the dependencies for us.

* Alternatively, we could paste the contents of the `SafeMath.sol` file directly where the import would be, above the `ArcadeToken` contract definition.

Next, in the first line of the contract, add `using SafeMath for uint;` to link the library to the `uint` type:

```solidity
pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/math/SafeMath.sol";

contract ArcadeToken {
    using SafeMath for uint;

    // ...
}
```

Explain to the class:

* We need to add this line at the beginning of our contract to link the library to the `uint` data type.

* This adds special functions to any object using the `uint` type, like `.add()`, `.sub()`, `.mul()`, and `.div()` that we can use instead of the `+`, `-`, `*`, and `/` operators.

Modify the `transfer` function to use the SafeMath assignments instead of the standard `-` and `+` operators:

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] = balances[msg.sender].sub(value); // prevents integer underflow
    balances[recipient] = balances[recipient].add(value);
}
```

* Notice now we can call `.sub()` and `.add()` on the `uint` values that come from the `balances` mapping.

* By performing math operations this way, we now prevent integer underflows! Let's try to perform the same hack on our contract again and see what happens.

Deploy a fresh version of this newly modified contract and fill in the `transfer` function with the same details as before:

![Secure Transfer](Images/arcade_token_secure_transfer.png)

Now, attempt to make the same transaction. You will need to ignore a `Gas estimation failed` error -- this is because even the EVM knows an error is likely to occur.

Sending the transaction anyway will result in an error like:

![MetaMask Failed](Images/metamask_failed.png)

The log in Remix will show something like:

```shell
transact to ArcadeToken.transfer pending ...
transact to ArcadeToken.transfer errored: Error: [ethjs-rpc] rpc error with payload {"id":559065790857,"jsonrpc":"2.0","params":["0xf8ab1a843b9aca00832dc6c094aa6b6a74aec9a4d05484c9841dd911b35838bb4180b844a9059cbb000000000000000000000000a29f7e79ecea4ce30dd78cfeb9605d9aff5143a50000000000000000000000000000000000000000000000000000000000000001822d45a0dc029786c5cb8efb0c75ed6d6c86db6f75e5e51af57e584f0df168e6d4fffbf0a069cabf26a54d320aaea8d68d98d02d296fbf80335200c6434b021f9324058ef7"],"method":"eth_sendRawTransaction"} [object Object]
```

* Voila! Now are contract is secured against integer under/overflows.

* Note, this will only work with `uint` currently, but we can declare it for `int` as well in the future.

* We'll need to make sure that we replace every instance of a normal operator like `+`, `-`, `*`, `/`, etc, with the SafeMath alternatives.

* It is good practice to leverage this library by default, and the majority of smart contract developers do the same as it has prevented many tokens from being compromised.

Now it's time for students to secure their tokens!

---

### 11. Students Do: Using SafeMath (15 min)

In this activity students will implement the SafeMath library and replace all math operations with the SafeMath alternatives.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/11-Stu_Using_SafeMath/README.md)

**Files:**

* [ArcadeTokenSafeMath.sol](Activities/11-Stu_Using_SafeMath/Unsolved/ArcadeTokenSafeMath.sol)

Ensure that students:

* Properly import SafeMath via the GitHub URL provided.

* Add the `using SafeMath...` line to the top of their contract.

* Replace the math operations with the SafeMath alternatives.

Take care that students are reassigning the variables with an `=` and not just running the SafeMath operations. SafeMath will not mutate the variable it is operating on, so you will need to ensure that the variables are reassigned.

---

### 12. Instructor Do: SafeMath Review (10 min)

**Files:**

* [ArcadeTokenSafeMath.sol](Activities/11-Stu_Using_SafeMath/Solved/ArcadeTokenSafeMath.sol)

Open the solution and explain the following:

* We import the SafeMath library directly from GitHub at the top of the file. This is only supported in Remix. We can also copy and paste the contract directly into our code above our own.

* We need the `using SafeMath for uint;` line to link the library to the `uint` type. That way, we can call the `.add()`, `.sub()`, etc functions on any `uint` later.

* By replacing all of the math operations with the SafeMath alternatives, we secure ourselves from potential balance hacks.

Ask for any remaining questions before moving on.

---

### 13. Students Do: Tokenized Reward System Challenge (20 min)

In this activity, students will take some time to work on a "tokenized reward system" challenge.

Students will modify their `ArcadeToken` to distribute tokens as a reward for spending Ether with the contract. The new `spend` function will collect a small transaction fee for the owner (say, `0.25%`) and reward points to the user in exchange (say, 3 tokens for every wei spent).

Send out the instructions to the students and have TAs circulate the class. Remind students to use SafeMath operations!

**Instructions:**

* [README.md](Activities/13-Stu_Tokenized_Rewards_Challenge/README.md)

**Files:**

* [ArcadeTokenRewards.sol](Activities/13-Stu_Tokenized_Rewards_Challenge/Unsolved/ArcadeTokenRewards.sol)

Clarify the activity a bit to the students:

* In this activity we will incentivize loyal Arcade to users to collect `ARCD` tokens passively during regular Ether transactions that can later be used in the Arcade.

* We will alter our contract to provide a system similar to credit card points that can be redeemed for cashback, in-store credits, etc. by adding a new function called `spend` that will collect a small transaction fee to the `owner` and forward the rest of the Ether to a `recipient`. Then, the contract will reward X amount of points for every wei spent.

* Say we actually ran an Arcade, or some other store or service. Loyal Arcade customers can spend their Ether with our contract and redeem the tokens back at the Arcade!

* The contract owner collects a small Ether fee passively in return for the rewarded tokens, so capital is generated to provide these benefits. You could configure the reward system however you'd see fit.

Note: since Solidity does not support floating point numbers (decimals), a formula is provided in the instructions to calculate percentages from "basis points."

`1` basis point = `0.01%`. You can calculate a percentage by using `basis_points * some_number / 10000`.

For example: `250 basis points * $100 / 10000` is equal to `$2.5` or 2.5%

Here's a handy chart for easy reference (also provided to the students):

Basis Points | Percentage
---------|----------
1 | 0.01%
5 | 0.05%
10 | 0.1%
50 | 0.5%
100 | 1%
1000 | 10%
10000 | 100%

Ensure students are applying this formula if they decide to use percentages in their rewards system.

---

### 14. Instructor Do: Challenge Review / Recap (10 min)

**Files:**

* [ArcadeTokenRewards.sol](Activities/13-Stu_Tokenized_Rewards_Challenge/Solved/ArcadeTokenRewards.sol)

Open the solution and explain the following:

* In our spend function, we calculate the fee by performing `uint fee = msg.value.mul(fee_rate).div(10000)`. This calculates a percentage of the `msg.value` by using the basis points formula.

* We calculate the token reward amount by multiplying the `msg.value` by the reward as so: `uint reward = msg.value.mul(reward_rate)`.

* We then add the rewards to the balance of the user by running `balances[msg.sender] = balances[msg.sender].add(reward)`.

* Next, we transfer the `msg.value` minus the fee to the `recipient` using `recipient.transfer(msg.value.sub(fee))`.

* Finally, we transfer the remaining `fee` value by running `owner.transfer(fee)`.

Ask the students the following questions:

* Why might we want to implement a reward system like this?

  * **Answer:** You could incentivize loyal users to return to your Arcade or business.

  * **Answer:** You generate capital from small fees that allow you to further develop your business.

  * **Answer:** This works much like an annual credit card fee would, but instead collects passively.

  * **Answer:** You only need to write the contract once, then you have the reward system in place. Less infrastructure cost for the business.

* What are some downsides to this system?

  * **Answer:** Some users won't be willing to pay an extra fee. In that case you may be able to remove it applicable for your business model.

  * **Answer:** Users have to pay extra gas to run the `spend` function vs paying Ether directly.

  * **Answer:** It may be difficult to come up with a viable rewards system that works for your business.

Ask for any remaining questions before moving on.

---

### 15. Instructor Do: Homework Demo (10 min)

This section is reserved for the homework demo. Take some time to review the homework with the class.

* [Unit 21 Homework Instructions](../../../02-Homework/21-Advanced-Solidity/Instructions/README.md)

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
