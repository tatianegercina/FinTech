# 21.2 Lesson Plan: Writing Secure Contracts with OpenZeppelin

### Overview

Previously students were introduced to the concept of tokens on the Ethereum blockchain. They learned what tokens are and how to use them. Today they will be introduced to the concept of `fungibility`, `fungible` vs. `non-fungible` goods, and how this relates to tokens and the various token standards.

### Class Objectives

By the end of the unit, students will be able to:

* Explain the difference between fungible and non-fungible tokens and their use-cases.

* Explain that ERC standards are official smart contract implementations for various use cases.

* Explain which ERC token standards correspond with fungible vs. non-fungible tokens

* Implement an ERC20 compatible fungible token using OpenZeppelin libraries

* Evaluate different ERC standards and determine which work for different use cases

* Leverage open, community-maintained libraries in Solidity to implement ERC standards

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1fANX-FqvBTBvz2iTsLZebKLO24zhMc2vSC0nhU-z9RU/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).


### Instructor Notes

* Focus on really conveying that ERC's are just standards that can be implemented in a number of ways.

* Refer to the [OpenZeppenlin Documentaion](https://docs.openzeppelin.com/contracts/2.x/tokens) for additional links and examples.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome to Class (10 min)

Review tokens, and the concept of tokenomics with the class.

* What are things that can be represented by a token?

  * **Answer** Property

  * **Answer** Currency

  * **Answer** Votes

  * **Answer** Potentially any other store of value

* What are some common aspects of a `token`.

  * **Answer** They have a supply which can be a fixed or infinite amount.

  * **Answer** They represent some store of value.

  * **Answer** They can be programmed with a smart contract.

* What are some generally accepted differences between `coins` and `tokens`?

  * **Answer** Tokens are commonly built on top of an existing blockchain platform. In contrast, coins are commonly a fundamental component of a blockchain platform.

  * **Answer** Coins are typically used as just a currency for buying and selling things. In contrast, tokens can have broader use cases.

  * **Answer**  Sometimes there's no difference at all; many people within the crypto communities use the terms interchangeably.

* What are some potential benefits of tokenizing an asset on an open blockchain?

  * **Answer** The asset can be traded globally without any additional infrastructure.

  * **Answer** Easy transfer of ownership with improvements in liquidity and audibility.

  * **Answer** Benefits of an open blockchain; open, public, borderless, censorship-resistant, and neutral.

### 2. Instructor Do: Fungible vs. Non-Fungible Tokens (10 min)

In this activity, students will be introduced to the concepts of fungible vs. non-fungible tokens and their differences.

You will be starting with real-world examples and move into digital examples. Refer to the following link for additional documentation [OpenZeppenlin Documentation: Tokens](https://docs.openzeppelin.com/contracts/2.x/tokens#_different_kinds_of_tokens)

* As previously discussed, tokens can be used to represent any potential store of value including, votes, currency, and property.

* Tokens and the idea of tokenomics is an extremely powerful concept. However, it goes a lot deeper than just representing the value of an asset.

Have the class consider the following question?

* What happens if two assets are not of the same value, how do you represent them both with tokens?

Expand on the previous question with the following points and introduce the concept of `fungibility`.

* Se we have things of equal value that are interchangeable with one another, and we have things that are not of equal value that are therefore not interchangeable with one another. This concept is referred to as `fungibility`.

* Examples of fungible goods include cryptocurrencies, fiat currencies, and voting rights.

  * A vote is a vote, if you have two people that both have voted, then their votes both have the same voting power. Just like if you have two people that both have a `nickel`, both nickels are worth the same 5 cents.

* Examples of non-fungible goods include pieces of land, diamonds, or collectibles.

  * A person could own a piece of land in San Diego, and a piece of land in Pennsylvania, these two pieces of land are different, they do not hold the same value and are therefore not interchangeable with one another. The same could be said for two different collectible figures like a Pop Vinyl or a Beanie Baby; each collectible is unique.

* Previously, we implemented our basic token standard. Today we will be discussing and using some of the community accepted standards for implementing both fungible and non-fungible tokens.

Now that the students have a basic understanding of `fungibility`, discuss some of the real-world implementations of `fungible` and `non-fungible` tokens on the blockchain.

In your web browser open the [CryptoKitties Website](https://www.cryptokitties.co/)

![CryptoKitties](Images/cryptokitties_website.png)

* `CryptoKitties` is a popular `non-fungible` token on the Ethereum blockchain.

* `CryptoKitties` is also a dApp that allows users to buy and sell, and breed virtual cats.

* At the crypto peak in 2017, some `crypto kitties` were valued at over 130 thousand US dollars.

Remind the students that we have already discussed many examples of `fungible` tokens yesterday. Examples include:

* Basic Attention Token (BAT)

* Golem (GNT)

* Maker Dao (Dai)

* Our Arcade Token (ARCD)

### 3. Students Do: Use Case Thought Experiment (15 min)

In this activity, students will break into groups of 3 - 5 people and brainstorm ways to leverage fungible and non-fungible tokens.

**Instructions:**

* [README.md](Activities/02_Stu_Use_Case_Thought_Experiment/README.md)

### 4. Instructor Do: Fungible vs. Non-Fungible Review (10 min)

Now that the students have collected their lists of fungible and non-fungible use cases. Go around the room and ask each group the following questions.

* What was your favorite `Fungible` use case?

* What was your favorite `Non-fungible` use case?

* Why do you think the benefits of scaling such a system on a blockchain would be?

* Why do you think some downsides of scaling such a system on a blockchain would be?

### 5. Instructor Do: ERC Standards (10 min)

In this activity, students will be introduced to various ERC standards. Students will gain the understanding that such specifications exist to standardize smart contract use cases to avoid bugs and security vulnerabilities.

* Ethereum is continuing to grow and rapidly evolve as the crypto community and the world continues to expand on the concepts of Web3 and blockchain.

* Throughout these periods of change, standards are formed to lead to best practices within the platform to prevent bugs and security vulnerabilities.

* Today we will be discussing several of these standards, also known as `EIP`s, we will specifically be talking about `ERC`s a type of `EIP` specifically related to application-level standards and conventions such as smart contracts.

* The ERCs we will be focusing on today are `20, 721, 777, 1155`.

  * EIP 20: ERC20 Fungible Token Standard

  * EIP 721: ERC721 Non-Fungible Token Standard

  * EIP 777: ERC777 Fungible Token Standard

  * EIP 1155: ERC1155 Multi-Token Standard

Click the following link to review the list of [Ethereum Improvement Proposals](https://eips.ethereum.org).

![List of EIPS](Images/eips.png)

* The following categories of `EIP`s exist.

  * Core

  * Networking

  * Interface

  * ERC

  * Meta

  * Information

* The Ethereum foundation officially refers to `EIP`s as `A design document providing information to the Ethereum community, or describing a new feature for Ethereum or its processes or environment`.

Core EIPs follow a slightly different process from the rest of the EIP categories. Since ERCs are not in the `Core` EIP category, it will follow the process below, just like the rest:

[ WIP ] -> [ DRAFT ] -> [ LAST CALL ] -> [ FINAL ]

* The stages of the process consist of the following.

  * WIP - During the `work in progress` phase, EIP creators formulate their EIP and may ask the community forums for input.

  * Draft - During the draft phase, the initial draft and any changes are merged in as a pull request. The EIP must be implemented to progress to the next phase.

  * Last Call - During the last call phase, the EIP is listed on the [https://eips.ethereum.org/](https://eips.ethereum.org/) website under the Last call section. If there are no unaddressed technical complaints will or changes to source material required, then the changes will become Final.

  * Final -  The EIP becomes final, reflecting the most state-of-the-art standard.

* Up to this point, we have discussed the concept of tokens, have implemented our basic token standard, and have learned that tokens can represent both fungible and non-fungible goods.

* There are ERC standards that the community has established to implement different use cases including `fungible` and `non-fungible` tokens. We have built our own `fungible` token using our logic. However, we should be able to find the latest community standards when we go to build our tokens and dApps in production.

* Assure students that by being able to follow the newest accepted `Ethereum Improvement Proposals`, that they will be able to stay up to date on the current Ethereum standards, practices, and technologies.

### 6. Students Do: ERC Standards Exploration (15 min)

In this activity, students will be exploring the various ERC standards that are currently being developed, and that have been accepted as final.

Send out the instructions and have TAs circulate the class.
**Instructions:**

* [README.md](Activities/03_Stu_ERC_Standards_Exploration/README.md)

Explain to the students:

* You will be exploring the ERC standards that are currently being developed or have been finalized by the community.

* The goal of this activity is to be able to learn how to leverage the current state of the community standards when developing ideas or implementing blockchain technologies. By getting comfortable exploring the standards, you will be able to keep up with the latest developments in the ecosystem and know that your implementations will be compatible with the community.

* Don't be intimidated by the fancy language; try to do some quick Googling!

### 7. Instructor Do: ERC Standards Review (10 min)

Ask the students the following review questions about the ERC standards activity.

* Which token standards were fungible?

  * **Answer** 20, 777, 1155

* Which token standards were fungible?

  * **Answer** 721, 1155

* What do you think some potential benefits of EIP's having to follow the acceptance process might be?

  * **Answer** Community support, better standards from peer review, open development.

* Why do you think `fungible` and `non-fungible` are implemented as separate contracts?

* **Answer** Keeping the standards focused on the use case and as simple as possible helps increase the adoption of the standard and makes them easier to work with.

* Why do you think ERC1155 combines the fungible and non-fungible concepts into one?

  * **Answer** For some use cases, like video games, you need a mix of fungible and non-fungible tokens available. For these edge cases, ERC1155 has your back.

* What ERC standards would you like to see?

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Welcome Back (5 min)

Before the break, we discussed various ERC token standards and what the students found interesting about them. Take a few minutes to go over the following ERC review questions with the class.

* Why might Ethereum improvement proposals such as ERCs be important?

  * **Answer** Provides a way to submit new standards within the community.

  * **Answer** Allows the community to agree on a current standard for a feature.

  * **Answer** Helps prevent bugs and security vulnerabilities by creating a specification for implementing certain types of smart contracts.

* What are some of the categories for EIP's?

  * **Answer** Core, Networking, Interface, ERC, Meta, Informational

* What are some of the ERC's that we've taken a look at so far?

  * **Answer** 20, 777, 721, 1155

### 10. Instructor Do: OpenZeppelin's ERC Library (15 min) (Critical)

In this activity, you will demonstrate the ERC20 contract provided by the OpenZeppelin library, and re-implement the ArcadeToken using the official ERC20 standard.

**Files:**

* [ArcadeTokenERC20.sol](Activities/04-Ins_OpenZeppelin_ERC20/Solved/ArcadeTokenERC20.sol)

Explain why we are starting with ERC20 to the students:

* We are going to implement ERC20 before ERC777 for several reasons.

  * It is a simpler standard to understand.

  * It has the widest adoption and support in blockchain explorers, wallets, and developer libraries.

  * ERC20 tokens are plentiful in the wild and are implemented by stablecoins like Coinbase's USDC and Gemini's GUSD, so it is important to understand how they are structured.

  * ERC777 depends on another contract defined in EIP1820 to be deployed onto our network, so we'll worry about that later.

Open [Remix](https://remix.ethereum.org) and create a new file called `ArcadeTokenERC20.sol`, and start with the following boilerplate:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {

}
```

Explain to the students:

* OpenZeppelin provides contracts that are implementations of common standards.

* Here, we are importing the ERC20 contracts from the OpenZeppelin library.

* By defining our contract like `ArcadeToken is ERC20, ERC20Detailed`, we are telling the compiler that our contract will *inherit* the functions and properties of `ERC20` and `ERC20Detailed` contracts.

Expand upon the concept of inheritance by opening up the `ERC20.sol` in Remix from the sidebar (you will need to save `ArcadeTokenERC20.sol` to get Remix to load the library):

![OpenZeppelin ERC20 File](Images/oz-erc20.png)

Point out the code in the file:

![OpenZeppelin ERC20 Code](Images/oz-erc20-code.png)

* This contract contains a `mapping` called `_balances` to keep track of balances in the same way we designed our tokens previously. The `balanceOf` function pulls the `uint` value from the `_balances` mapping corresponding to an `address` in the same way we made our balance functions before.

* The `transfer` function is also defined, just like the ERC20 standard specifies. It is formatted a bit differently from the way we defined it when we built our tokens from scratch. This is to make sure that certain security checks are performed. However, the same parameters and general logic are used to get the job done.

* By saying that `ArcadeToken is ERC20`, we are inheriting all of these variables, functions, and so on into our contract. We can inherit from multiple contracts as well!

* This means that we can call the `transfer` function and `balanceOf` functions, as well as the others like `_mint` in order to manage our token.

Next, open up OpenZeppelin's `ERC20Detailed` contract in the same folder and point out the code:

![ERC20Detailed](Images/oz-erc20-detailed.png)

* Since the ERC20 standard defines the `name`, `symbol` (the token's ticker), and other variables as *optional*, OpenZeppelin separates the optional parameters into `ERC20Detailed`.

* Notice that `ERC20Detailed` has its constructor as well to establish the `name`, `symbol`, and `decimals` parameter. The `name` is the human-friendly name of the token, the `symbol` is the ticker, and the `decimals` are the number of decimal points this token will use. We will stick to Ethereum's default, `18` in most of our cases.

* There are also "getter" functions that return these values.

Close OpenZeppelin's implementations and navigate back to `ArcadeTokenERC20.sol`.

First, define an `address payable owner` at the top of the contract:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;
}
```

Then, add the following constructor below the `owner`:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }
}
```

Explain to the students that this is a constructor that also passes parameters to the ERC20Detailed constructor:

* Notice that in our constructor, we call `ERC20Detailed`, and we pass in some parameters.

* Since we are inheriting from `ERC20Detailed`, and `ERC20Detailed` has a constructor, we need to pass the parameters it expects.

* Remember, the `ERC20Detailed` constructor had three parameters: `name`, `symbol`, and `decimals`. Here, we are passing in `ArcadeToken` as the name, `ARCD` as the symbol, and we are using Ethereum's default `18` decimal places for easier conversion.

* In our constructor, we are setting the `owner` as the `msg.sender`, and calling the `_mint` function that OpenZeppelin's `ERC20` provides to us. By passing in `initial_supply`, we can create an initial amount of tokens and send it to the owner upon deployment.

Now, add a `mint` function to the contract:

```solidity
function mint(address recipient, uint amount) public {
    _mint(recipient, amount);
}
```

* Since the `_mint` function is set to `internal` in the `ERC20` contract, we can only call it from within our `ArcadeToken` contract. This means we have to create a new `mint` function here to expose the function and enable us to use it later.

* However, we want to restrict this `mint` function using a `require`. Rather than using the same method we used before, let's create our own `modifier`!

Add the following `modifier` function to the contract:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }
}
```

* A `modifier` is a special function that will allow us to restrict our other functions in the same way that we set them to `public` or `payable`.

* Since we call this modifier `onlyOwner`, we can add `onlyOwner` to the functions that we want to restrict to ourselves.

* Inside the modifier, we add the same `require` that we would normally to ensure that `msg.sender` is the `owner` address.

* At the last line of the modifier, we need to add an underscore `_` to tell Solidity to return to the function that called the modifier.

Now, add the `onlyOwner` modifier after `public` on the `mint` function:

```solidity
function mint(address recipient, uint amount) public onlyOwner {
    _mint(recipient, amount);
}
```

The contract should look like the following up to this point:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
}
```

* That's it! Now, this token is a fully functioning ERC20 token, that has a `mint` function that we created an `onlyOwner` modifier for.

* We could potentially deploy this to the mainnet and get this listed on an exchange. It will also automatically be detected by many wallets and block explorers.

Now it's time for the students to implement their own ERC20 tokens!

### 11. Students Do: Building an ERC20 Token with OpenZeppelin (20 min)

In this activity, students will implement the ArcadeToken using the ERC20 standard, provided by the OpenZeppelin library.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/05-Stu_ERC20/README.md)

**Files:**

* [ArcadeTokenERC20.sol](Activities/05-Stu_ERC20/Unsolved/ArcadeTokenERC20.sol)

Ensure that students are properly passing parameters to the `ERC20Detailed` constructor and that they are properly using the `onlyOwner` modifier.

### 12. Instructor Do: ERC20 Review (10 min)

**Files:**

* [ArcadeTokenERC20.sol](Activities/05-Stu_ERC20/Solved/ArcadeTokenERC20.sol)

Open the solution and explain the following:

* The `onlyOwner` modifier allows us to add `onlyOwner` to the list of modifiers (usually after `public`) on any function we'd like to restrict.

* The constructor passes the `ERC20Detailed` parameters properly to set the token's name, symbol, and the number of decimal places.

* Within the constructor, we set the token's owner to `msg.sender`. Then we call `_mint` to add the `initial_supply` to the token owner's balance.

* Our new `mint` function we added will be restricted to `onlyOwner`, and will

Ask for any remaining questions before moving on.

### 13. Everyone Do: Deploying the token to a Testnet (10 min)

In this activity, you will lead a code along, where the entire class will deploy their tokens to the Kovan testnet.

**Files:**

* [ArcadeTokenERC20.sol](Activities/06-Evr_Deploying_ERC20/Resources/ArcadeTokenERC20.sol)

First, assign a number to every student in the class. This will be the number that they will append to their `symbol` as a way of quickly identifying which `ArcadeToken` was deployed by each student.

Have each student modify their token's `symbol` to append their number; for example, student 33 would modify their token symbol to be `ARCD33`; student 42 would use `ARCD42`, and so on.

Once each student has set their `symbol` properly, have everyone **save their contract** before moving forward. We will be switching to the Kovan network in MetaMask, and this will trigger a refresh in Remix.

Now, switch MetaMask's network to the Kovan network, like so:

![MetaMask Kovan](Images/metamask-kovan.png)

Allow Remix to refresh and navigate back to the `ArcadeTokenERC20.sol` contract.

Have students switch over to the Kovan network and pause until everyone has switched, refreshed Remix, and reopened their contract.

Navigate to the `Deploy` tab, and switch the `Environment` from `JavaScript VM` to `Injected Web3` to connect it to MetaMask. The environment should show `Kovan (42) Network`.

Next, type in an arbitrary amount, like `333333333333333333333` into the `initial_supply` constructor parameter, then click the orange `Deploy` button:

![ERC20 Deployment](Images/arcade-token-erc20-deploy.png)

Confirm the contract deployment in MetaMask:

![Deployment Confirmation](Images/deploy-confirm.png)

Point out the following before confirming the transaction:

* The estimated price can be used to check how much deploying this token to the mainnet would cost. In this case, deploying our ERC20-compliant ArcadeToken would cost about $0.34 total.

Confirm the transaction and have all of the students follow along and deploy their tokens to Kovan. It may take a couple of minutes for everyone's transactions to confirm. However, Kovan's blocktime is 5 seconds and should manage quickly.

Once everyone has deployed, point out that Remix will allow you to interact with this contract in the sidebar as usual:

![Deployed contract](Images/arcade-token-deployed.png)

Explain to the class:

* We should copy the contract's address and store it where convenient. We can always look it up on the blockchain by looking at our transaction history, but we want to have it handy.

Copy the contract's address, then refresh the page, clearing out the Remix session. Navigate back to the contract's code.

Switch the environment to `Injected Web3` again, then paste the contract's address in the `At Address` field below the orange `Deploy` button:

![Fetch contract at address](Images/arcade-token-at-address.png)

Click the `At Address` button to fetch the contract from the Kovan testnet. This will have the contract's interactive menu re-appear:

![The Arcade Token Returns](Images/arcade-token-reappear.png)

Explain to the students:

* As long as we have our contract's code, and the address, we can generate the information we need to interact with the contract.

* In fact, we don't need the code itself, just something called the ABI (Application Binary Interface), which is a compiled interface that is like an API, but in binary format. Since we have the code, we can generate the ABI. However, don't worry about that, Remix will handle that stuff behind the scenes.

* We can come back to this interactive menu at any time by pointing Remix in the right direction by setting the network and contract's address.

Now time for the exciting part, actually using our tokens!

### 14. Students Do: Sending and Receiving ERC20 tokens (15 min)

In this activity, students will pair up and exchange each other's tokens on the testnet. They will also explore the transactions and the contract on the Etherscan block explorer, which provides more detail for ERC20-compliant smart contracts.

**Instructions:**

* [README.md](Activities/07-Stu_Sending_Receiving_ERC20/README.md)

Have TAs circulate the room and ensure that students can call their contract functions properly, and mint and transfer tokens to each other.

### 15. Instructor Do: Recap (10 min)

Ask the students the following questions:

* What are some benefits of using standards when developing smart contracts?

  * **Answer:** We utilize the community-driven implementations to prevent bugs and security holes.

  * **Answer:** It makes it easier for us to develop our applications.

* What does OpenZeppelin provide as a library?

  * **Answer:** Security tools.

  * **Answer:** Standardized implementations of official ERCs to make developer lives easier.

* What is the difference between fungible and non-fungible?

  * **Answer:** Fungible refers to tokens where you ask "how many," whereas non-fungible refer to tokens where you ask "which one."

  * **Answer:** Fungible tokens are like-kinds, where each token can be exchanged with another of the same value without making a difference. Non-fungible tokens are unique per-token, meaning each token has its properties and value, like artwork or legal certificates.

* Why was MetaMask able to understand, send, and receive our ArcadeTokens?


  * **Answer:** MetaMask is compatible with the ERC20 standard so that it can recognize and utilize our tokens!


---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
