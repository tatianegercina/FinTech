# 21.3 Lesson Plan: Writing Secure Contracts with OpenZeppelin

### Overview

In the last class, students were introduced to several of the popular ERC token standards (20, 721, 777, 1155) and implemented an ERC20 compliant token using the OpenZeppelin libraries. Today students will be introduced to the concept of crowdsales, a popular method for distributing tokens; they will explore popular historic crowdsales and implement their own crowdsale using the OpenZeppelin libraries.

---

### Class Objectives

By the end of the class, students will be able to:

* Articulate different types of crowdsales and how Ethereum/blockchain makes them much easier and auditable.

* Prepare an ERC20Mintable token for Crowdsale

* Build a crowdsale that distributes an ERC20Mintable token.

* Design contracts to avoid common security pitfalls, such as a re-entrancy attack.

* Analyze contracts to identify and fix simple security vulnerabilities.

---

### Instructor Notes

* Today's class will be heavily focused on crowdsales. While this method of fundraising has been used legitimately for many successful companies and projects in the space, there are many scams. Try to limit the discussion of scams and keep the class focused on legitimate implementations, but acknowledge that there is risk involved when investing in crowdfunded projects, just as there are risks in any other investment.

* Ethereum itself was crowdfunded by the people with Bitcoin, but certainly has not been the largest crowdsale, and has been used to launch other platforms that raised even more funds. It is recommended to familiarize yourself with popular crowdsales such as Basic Attention Token, Filecoin, EOS, Qtum, and others from the [most funded ICO list.](https://icowatchlist.com/finished/most-funded)

* While Initial Coin Offerings (ICOs) have been the most popular type of crowdsale, the industry is moving toward Security Token Offerings (STOs) and more regulated systems.
* OpenZeppelin provides many different configurations for crowdsales. Encourage students to perform their due diligence with legal compliance and technical requirements of a crowdsale if they show interest in leveraging one themselves in the future.

* When discussing security, drive home the importance of due diligence in software development. Encourage the students to get excited about security research, as they will have to think about security inherently in their future.

* Encourage students not just to seek out and scan for low-level bugs and exploits in their code, but to thoroughly analyze the logical implementation of their code as to not create a vulnerability by improperly implementing the business logic. A secure specification can still be implemented insecurely, so it is important to build their ability to "think like a hacker."

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1q661f6W6QL-u-24G6W_Hu5GOBzJfoU1s3XxkS91o4YA/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome to Class (10 min)

Refresh the students on ERC standards and set the stage for today's class by briefly discussing the topic of token distribution.

Review the following recall questions with the class.

* What are some examples of ERC standards?

  * **Answer** Fungible tokens

  * **Answer** Non-fungible tokens

  * **Answer** Token exchange standards

  * **Answer** Ethereum Domain Name Service

  * **Answer** Multi Token Standard

* What are some benefits of ERC standards?

  * **Answer** Provides a way to submit new standards within the community.

  * **Answer** Allows the community to agree on a current standard for a feature.

  * **Answer** Helps prevent bugs and security vulnerabilities by creating a specification for implementing certain types of smart contracts.

* What are some of the stages that an ERC goes through before being accepted by the community.

  * **Answer**  WIP

  * **Answer**  DRAFT

  * **Answer** LAST CALL

  * **Answer** FINAL

* What are some differences between `fungible` and `non-fungible` tokens?

  * **Answer** Non-fungible tokens are unique, fungible tokens are not unique.

  * **Answer** Fungible tokens are interchangeable with one another whereas non-fungible are not.

  * **Answer** non-fungible tokens use ERC 721, fungible tokens use ERC 777.

Now that the students are familiar with tokens and the various ERC token standards, briefly introduce the concept of token distributions by discussing the following question with the class.

* We understand basic tokenomics and how to implement our own ERC compliant token, but now how do we distribute that token to users and create a market for it?

  * This is where a `crowdsale` comes in.

Inform the class that we will be discussing the concept and application of crowdsales in the next activity.

### 2. Instructor Do: Crowdsales in Ethereum (10 min)

In this activity, you will explain how crowdsales have become a popular method for distributing tokens.

* For companies and startups, it's cheap to have new ideas, but executing those ideas can be very expensive.

* Over the last decade, `crowdfunding` has become a popularized way for projects to receive funding that enables them to bring their product or service to production successfully.

* `Crowdfunding` is the process of raising funds by asking a large number of people each for a small amount of money. Crowdfunding is often done through a `crowdfunding platform` where users are promised a product or service and can then donate money to a project in a streamlined manner.

* Blockchain technologies and the rise of tokenomics has enabled a new form of `crowdfunding` known as a `crowdsale`.

* Unlike in traditional crowdfunding backers funding the project are not promised a particular product or service. They are instead promised a given number of tokens at a set price.

* The tokens sold during the `crowdsale` then serve as a way for users to take part in whatever product or service the company is planning to launch.

Pose the class the following question:

* What are some things that crowdsale funds could be used for?

  * Marketing funds

  * To pay developers

  * Product development

  * Product production

  * Any other initial operating costs

Explain to the class that tokenomics still play a huge rule in `crowdsales`. Investors backing the project aren't always just buying the token because they believe the future project will be successful but also because they believe the perceived market value of the token will increase.

* Important factors of a crowdsale:

  * Price & Rate Configuration

  * Will your crowdsale offer tokens at a fixed price?

  * Emission

  * Is there a cap on the total number of tokens released?

  * Is there a cap on the total number of tokens a single person can buy?

  * How is your token sent to people participating in the crowdsale?

  * Start/Endtime/Timeframe

  * Are the funds distributed during the crowdsale or after.

  * Is there a refund policy if the goal was not successful.

* When implementing a crowdsale, you have first to decide how you are going to release tokens to the participants of the sale. This is known as `token emission` and is normally done in one of three ways:

  * The crowdsale contract owns a given number of tokens and transfers ownership of them as users purchase them.

  * The crowdsale contract dynamically mints new tokens as they are purchased.

  * The crowdsale contract has access to a multi-sig wallet from which it can transfer ownership of tokens as they are purchased.

### 3. Students Do: Crowdsale Exploration and Discussion (10 min)

Students will be provided a list of crowdsales from which they will explore and research some of the most popular crowdsales in history.

**Instructions:**

* [README.md](Activities/01-Stu_Crowdsale_Exploration_and_Discussion/README.md)

### 4. Instructor Do: Crowdsales Review (5 min)

Discuss the following review questions with the class.

* What were some of the factors or interesting things about the explored historical crowdsales?

* **Example Answer** The price of ether during its initial sale was 2000 ETH per BTC.

* **Example Answer** According to the Ethereum blog post, "Ether is a product, NOT a security or investment offering. Ether is simply a token useful for paying transaction fees or building or purchasing decentralized application services on the Ethereum platform; it does not give you voting rights over anything, and we make no guarantees of its future value."

* **Example Answer** Basic Attention Token raised 36 million in 30 seconds, hitting the hard cap on their token supply.

* **Example Answer** FileCoin was capped at 200 million FileCoins

* What are some costs that a company may create a crowdsale to raise funds for?

  * **Answer** Production costs for a product

  * **Answer** Employee/Developer costs

  * **Answer** Marketing costs

  * **Answer** Initial startup costs

* What benefits might a crowdsale have over traditional crowdfunding?

  * **Answer** Potential access to a global marketplace.

  * **Answer** Benefits of an open blockchain.

  * **Answer** Increased control over a crowdfunding platform; you essentially become the crowdfunding platform.

### 5. Instructor Do: Preparing a token for a Crowdsale (10 min)

In this activity, students will be introduced to the ERC20Mintable contract from OpenZeppelin, and how they can use it to prepare a token that can work in a crowdsale.

**Files:**

[ArcadeTokenMintable.sol](Activities/02-Ins_Preparing_a_token_for_a_Crowdsale/Solved/ArcadeTokenMintable.sol)

Open [Remix](https://remix.ethereum.org) and create a new file called `ArcadeTokenMintable.sol`, and start with the following boilerplate:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
}
```

Explain to the students:

* As previously discussed, OpenZeppelin provides contracts that are implementations of common standards.

* Here, just like before, we are importing the ERC20 contracts from the OpenZeppelin library, now, however, we are also going to import and implement a new contract called `ERC20Mintable`.

Add the ERC20Mintable reference to the contract definition:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
}
```

* We have inherited the structures from `ERC20`, `ERC20Detailed`, and `ERC20Mintable`.

* By saying that `ArcadeToken is ERC20`, we are inheriting all of the properties and functions of `ERC20Mintable` into our new contract, including the `mint` function. As you have seen, we can inherit from multiple contracts.

Once again, expand upon the concept of inheritance by opening up the `ERC20Mintable.sol` in Remix from the sidebar (you will need to save `ArcadeTokenMintable.sol` to get Remix to load the library):

![ERC20MintableFile](Images/ERC20MintableFile.png)

Take a moment to point out the code in the file, particularly the comments.

![ERC20MintableCode](Images/ERC20MintableCode.png)

* `ERC20Mintable` extends `ERC20` to add a set of accounts with the MinterRole, who have permission to mint (create) new tokens as they see fit.

* At construction, the deployer of the contract is the only minter.

* The `onlyMinter` modifier restricts the mint function so that only accounts with the MinterRole can call the mint function.

Close OpenZeppelin's `ERC20Mintable` and navigate back to `ArcadeTokenMintable.sol`.

Now that `ERC20Mintable`'s functionality has been imported into our new contract, it's time to add our constructors.

First, add the constructor for the ArcadeToken contract itself. This constructor will accept a string `name`, a string `symbol`, and a uint `initial_supply`.

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
}
```

* Our contracts constructor accepts three values a string `name`, a string `symbol`, and a uint `initial_supply`.

Next, define the constructor for the `ERC20Detailed` contract that we are importing.

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
}
```

* Here we are defining the constructor for the `ERC20Detailed` contract that we previously imported.

* `ERC20Detailed`'s constructor accepts the variables `name` and `symbol` that we defined in the main ArcadeToken contract.

* Here we are also hardcoding the number `18` as our third parameter. This parameter defines the number of decimals that our token will have. In this case, the number `18` denotes that the smallest increment of our token is `.000000000000000001`. We are sticking with `18` since it's Ethereum's default.

Finally, it's time to define the contract's body. Inside the body of the contract, call the `mint` function, passing `msg.sender` and the `inital_supply` variable that is defined in our constructor.

Your complete code should now look something like this:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        mint(msg.sender, initial_supply);
    }
}
```

* Now when our `ArcadeToken` contract is deployed it will call the mint function passing it the current `msg.sender` as well as our defined `inital_supply`.

Compile and deploy the completed contract for the class.

![Deploy ERC20Mintable](Images/DeployArcadeTokenMintable.gif)

In the next activity, the students will now be implementing their own `ERC20Mintable` token for crowdsale.

### 6. Students Do: ERC20 Mintable Token Design (10 min)

In this activity, students will build a mintable ERC20 token and prepare it for a crowdsale.

**Instructions:**

* [README.md](Activities/03-Stu_ERC20Mintable_Token_Design/README.md)

**File:**

* [ArcadeTokenMintable.sol](Activities/03-Stu_ERC20Mintable_Token_Design/Unsolved/ArcadeTokenMintable.sol)

### 7. Instructor Do: Review ERC20 Mintable Token Design (10 min)

**File:**

* [ArcadeTokenMintable.sol](Activities/03-Stu_ERC20Mintable_Token_Design/Solved/ArcadeTokenMintable.sol)

Review the previous activity with the class by discussing the following recall questions.

* What are some benefits of using the OpenZeppelin libraries?

  * **Answer** OpenZeppelin follows the community standards defined for various ERCS.

  * **Answer** Saves development time by providing a boilerplate for common tasks.

  * **Answer** OpenZeppelin smart contracts are secure.

* Why might we restrict who can mint tokens?

  * **Answer** If anyone could mint tokens using our contract, it would essentially make them worthless.

* What are we doing when we say `ArcadeToken is ERC20` in our contract definition.

  * **Answer** We are inheriting the functions and properties from ERC20 to ArcadeToken.

* What are some things a function modifier may be used for in solidity?

  * **Answer** To restrict access to a function.

  * **Answer** To expose a function.

  * **Answer** To add dependencies to a function.

### 8. Instructor Do: OpenZeppelin Crowdsales (15 min) (Critical)

In this activity, you will demonstrate OpenZeppelin's Crowdsale contract library by creating an `ArcadeTokenSale` and an `ArcadeTokenSaleDeployer` contract that will mint tokens automatically when users send Ether to the `ArcadeTokenSale`.

**Files:**

* [ArcadeTokenMintable.sol](Activities/04-Ins_Crowdsales/Solved/ArcadeTokenMintable.sol)

* [ArcadeTokenSale.sol](Activities/04-Ins_Crowdsales/Solved/ArcadeTokenSale.sol)

Explain to the students:

* In this activity, we will be exploring the Crowdsale contracts that OpenZeppelin provides. Since our token is now `ERC20Mintable`, we will create a `MintedCrowdsale` that will automatically manage our token sale securely.

* OpenZeppelin Crowdsale contracts allow us to do a variety of things, including the ability to configure (among many others):

  * Token Price and Exchange Rates.

  * Setting a maximum cap on the sale.

  * Whitelisted addresses to restrict who can purchase from the crowdsale to comply with KYC/AML regulations.

  * When or how the distribution of funds occurs.

  * Time limits for the sale.

Briefly open (**max** 2 minutes) the [Crowdsale Constructor API doc](https://docs.openzeppelin.com/contracts/2.x/api/crowdsale#Crowdsale-constructor-uint256-address-payable-contract-IERC20-) and point out the constructor parameters for the `Crowdsale` contract (`uint256 rate, address payable wallet, contract IERC20 token`).

![Crowdsale Constructor](Images/oz-crowdsale-constructor.png)

* The crowdsale requires three parameters in the constructor. The first, `rate` is the conversion between our token and wei. Since we are using the default decimal value of `18` in our `ArcadeTokenMintable`, and we want to keep compatible with Ether units, this `rate` will just be set to `1`.

* The `wallet` parameter is the address that all of the Ether raised in the crowdsale will go. Since this is for our Arcade, we will set this parameter to our main wallet address.

* The last parameter the crowdsale needs is the token itself. This will allow the crowdsale to interact with and mint the `ArcadeToken` once on-chain.

Open up [Remix](https://remix.ethereum.org) and create a new file called `ArcadeTokenSale.sol`.

First, populate the imports and create the contract definition:

```solidity
pragma solidity ^0.5.0;

import "./ArcadeTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract ArcadeTokenSale is Crowdsale, MintedCrowdsale {

}
```

* Here, we are importing our `ArcadeTokenMintable` that we created in the last activity. We will be controlling the token with our new `ArcadeTokenSale` contract.

* We are also importing the `Crowdsale` and `MintedCrowdsale` contracts from the OpenZeppelin library. Then, we are inheriting the properties of these contracts in our `ArcadeTokenSale`.

Next, add a constructor that accepts the same parameters that the `Crowdsale` contract listed in the API docs:

```solidity
contract ArcadeTokenSale is Crowdsale, MintedCrowdsale {

    constructor(
        uint rate,
        address payable wallet,
        ArcadeToken token
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor can stay empty
    }
}
```

* Here we are simply accepting the same parameters that the OpenZeppelin documentation listed for the `Crowdsale` contract from our main constructor, and passing them into the `Crowdsale` constructor.

* This will allow `ArcadeTokenSale` to initialize all of the variables that `Crowdsale` requires. The body of the constructor can stay empty since all of the logic is already in the `Crowdsale` and `MintedCrowdsale` contracts.

Now, we will need to create one more contract in this file, below the `ArcadeTokenSale`, called `ArcadeTokenSaleDeployer`:

```solidity
contract ArcadeTokenSale {
  // ...
}

contract ArcadeTokenSaleDeployer {

    address public arcade_sale_address;
    address public token_address;

}
```

* We are going to use a temporary contract, called `ArcadeTokenSaleDeployer`, to help us deploy and configure our `ArcadeToken` and `ArcadeTokenSale` contracts with all of the correct information.

* First, we're going to create some public variables to store the addresses of the contracts we will be deploying from `ArcadeTokenSaleDeployer` to keep track of later.

Next, add the constructor that accepts `name`, `symbol`, and `wallet`, which will be the only non-hardcoded values, then create the new contracts from within the constructor:

```solidity
contract ArcadeTokenSaleDeployer {

    address public arcade_sale_address;
    address public token_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        // create the ArcadeToken and keep its address handy
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
        token_address = address(token);

        // create the ArcadeTokenSale and tell it about the token
        ArcadeTokenSale arcade_sale = new ArcadeTokenSale(1, wallet, token);
        arcade_sale_address = address(arcade_sale);
    }
}
```

* We accept the `name` and `symbol` for our token that we create here. We also accept the `wallet` that will receive all Ether raised by the crowdsale.

* We create the `ArcadeToken` within the constructor and store it in a variable called `token`, passing in the `name` and `symbol` parameters, and setting the `initial_supply` to `0`. Notice that we are still specifying the type, only the type is `ArcadeToken`. It has the same interface as an ERC20 token, so the crowdsale will accept it.

* We store the address of the token in the public variable we set earlier to keep handy.

* Then, we create the `ArcadeTokenSale` itself. We hardcoded the `rate` as `1` to maintain parity with Ether units. We pass in the `wallet` and the actual `ArcadeToken`. We also store the address of the crowdsale itself for easy access later.

Finally, we need to make the `ArcadeTokenSale` a `minter` and renounce the `minter` role from `ArcadeTokenSaleDeployer` at the end of the constructor:

```solidity
// make the ArcadeTokenSale contract a minter, then have the ArcadeTokenSaleDeployer renounce its minter role
token.addMinter(arcade_sale_address);
token.renounceMinter();
```

* Since `msg.sender` is the default minter when deploying `ERC20Mintable` tokens, and `ArcadeTokenSaleDeployer` is the `msg.sender` when creating the token, we need to set things straight by making the `ArcadeTokenSale` contract a minter, and to have the `ArcadeTokenSaleDeployer` renounce its "mintership," since we only want the crowdsale contract to have control of minting.

Your contract should now match the [ArcadeTokenSale.sol](Activities/04-Ins_Crowdsales/Solved/ArcadeTokenSale.sol) solution linked above.

Navigate back to the `ArcadeTokenMintable.sol`.

Remove the `mint` call that was in the constructor. The contract should look like the solution linked above:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        // constructor can stay empty
    }
}
```

* Since our Crowdsale contract is going to be minting and distributing tokens, we don't want to mint any tokens in the constructor. In fact, since we were minting to `msg.sender`, keeping the mint function here would cause us to **lose tokens**.

* This is because the `ArcadeTokenSaleDeployer` contract is the one that creates the `ArcadeToken` initially. Therefore, `msg.sender` would actually be the address of the `ArcadeTokenSaleDeployer` contract! Since we have no function to withdraw those tokens, they'd be effectively "burned" out of the usable supply. We could add a function to `ArcadeTokenSaleDeployer` to withdraw, but that is quite unnecessary and would ultimately be more expensive.

* It is especially important to think twice about who exactly `msg.sender` is, and how `msg.sender` can be manipulated. Remember, other people, can write smart contracts that could talk to yours, so `msg.sender` isn't always going to be a simple wallet.

That's all we need to get the crowdsale going. Navigate to the `Deploy` tab in Remix, and deploy the `ArcadeTokenSaleDeployer` contract, passing in the parameters.

You will then need to load the `ArcadeTokenSale` and `ArcadeToken` contracts from the `At Address` field using the addresses that `ArcadeTokenSaleDeployer` returns:

![Deployment](Images/deployment.gif)

Demonstrate purchasing some tokens from the `ArcadeTokenSale` and checking the balance in the `ArcadeToken`:

![Purchasing from the Crowdsale](Images/purchase.gif)

Now it's time for the students to make their own `ArcadeTokenSale`!

### 9. Students Do: Building an ArcadeTokenSale with OpenZeppelin (20 min)

In this activity, students will be creating and deploying an `ArcadeTokenSale` contract with an `ArcadeTokenSaleDeployer` contract.

Send the instructions to the students and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/05-Stu_ArcadeTokenSale/README.md)

**Files:**

* [ArcadeTokenMintable.sol](Activities/05-Stu_ArcadeTokenSale/Unsolved/ArcadeTokenMintable.sol)

* [ArcadeTokenSale.sol](Activities/05-Stu_ArcadeTokenSale/Unsolved/ArcadeTokenSale.sol)

Ensure that students are not modifying the constructor *parameters* of `ArcadeTokenMintable`, since it needs to match the ERC20 standard, which specifies `(string name, string symbol, uint initial_supply)`. We pass in `0` as the `initial_supply` when initializing the `ArcadeToken`.

### 10. Instructor Do: Crowdsales Review (10 min)

**Files:**

* [ArcadeTokenMintable.sol](Activities/05-Stu_ArcadeTokenSale/Solved/ArcadeTokenMintable.sol)

* [ArcadeTokenSale.sol](Activities/05-Stu_ArcadeTokenSale/Solved/ArcadeTokenSale.sol)

Open the solution and explain the following:

* We maintain the same parameters in our `ArcadeTokenMintable` in order to keep the interface compatible with ERC20. However, we remove any minting logic from inside of the body of the constructor, since we are delegating minting logic to the crowdsale.

* In the `ArcadeTokenSale` contract, all we need to do is pass the parameters from the constructor into the inherited `Crowdsale` contract, by using `Crowdsale(rate, wallet, token)`.

* We can keep the constructor body empty, as all of the logic is within the `Crowdsale` and `MintedCrowdsale` contracts that we inherit.

* In our `ArcadeTokenSaleDeployer`, we set define the `arcade_sale_address` and the `token_address` as public variables to easily fetch later.

* Then, within the constructor, we create the `new ArcadeToken` and pass in the `name` and `symbol` parameters, and we set the `initial_supply` parameter as `0` to ensure that we are not minting tokens unnecessarily.

* After creating the `new ArcadeToken`, we store the token's address in the `token_address` variable for easy access later.

* Next, we create the `new ArcadeTokenSale` contract and set the `rate` to `1` to keep parity with Ether units, then pass in the `wallet` that will receive all raised funds, and the`token` contract itself.

* In the same fashion, we store the `ArcadeTokenSale` contract's address in the `arcade_sale_address` variable.

* Finally, we make the `arcade_sale_address` a minter of the `token`, then we renounce "mintership" from our `ArcadeTokenSaleDeployer` contract.

Ask for any remaining questions before moving on.

---

### 11. BREAK (40 min)

---

### 12. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to class and have them settle in from the break.

Ask the following recall questions:

* What is a crowdsale useful for?

  * **Answer:** Another avenue for fundraising.

  * **Answer:** A way of removing middlemen from the fundraising process.

  * **Answer:** Managing the general sale and creation of tokens automatically.

* Why must we be careful about using `msg.sender` as a check-in our contracts?

  * **Answer:** `msg.sender` can also be another smart contract, so if the logic requires a human to be on the other end, it might not work.

* Why do `ArcadeToken` and `ArcadeTokenSale` have empty constructor bodies?

  * **Answer:** All of the logic for these contracts are handled in the contracts that they inherit, so no additional logic is needed.

Explain to the students that for the rest of the class, we will be examining the security of the crowdsale we just built, and learning about the common vulnerabilities that smart contract developers should avoid.

### 13. Instructor Do: Solidity Security (15 min) (Critical)

In this activity, you will demonstrate how to analyze, identify and fix common security vulnerabilities in Solidity contracts. Download the example contract, open the [Remix IDE](https://remix.ethereum.org), and explain the following.

**Files:**

* [ArtTokenVulnerable.sol](Activities/06-Ins_Security/Unsolved/ArtTokenVulnerable.sol)

Security is a fundamental topic regarding anything to do with technology, especially software that works directly with monetary value. Stress the importance of security:

* In our testnet and local development environments, we can "battle test" our code before we deploy it to the prime-time mainnet. It is especially important when programming smart contracts to avoid certain design patterns that lead to vulnerabilities that could potentially be exploited.

* Software security is not a new field, but it has recently exploded in demand and will continue to be a critical part of the software development lifecycle. Security is not just left to the security team in the software world; in reality, the security of a system is the sum of its technical and human aspects, and every person in an organization should be working towards the goal of higher security.

* Typically, organizations will have dedicated security teams continuously vetting and testing the software and operations. This does not mean you are off the hook! As the engineers, you are the first, and often, the only line of defense standing between a hacker and your trophies. When developing software, you should be taking security very seriously and integrate it from the ground up.

Briefly discuss the Ethereum DAO hack:

* Historically, we have seen instances of hacking in every industry. Since the blockchain space is still in adolescence and is rapidly growing, stumbles have occurred regarding smart contracts.

* A notable instance of this is the DAO hack. This was an organization built entirely from smart contracts that was exploited due to a low-level technical attack called a "re-entrancy" attack that allowed a hacker to drain the contract's funds, which we will learn more about soon. Since this attack, measures have been made to help prevent such attacks, and more security improvements are being made every day.

* Thus, it is important to learn how to spot these vulnerabilities.

In remix create a new file called `ArtTokenVulnerable.sol` and populate it with the [file linked above](Activities/06-Ins_Security/Unsolved/ArtTokenVulnerable.sol).

* Now, it's time to look at an example of what a vulnerable contract could look like.

* This contract is similar to one we wrote back when we first learned how tokens worked.

* Remember how in the past we had an integer underflow/overflow vulnerability that allowed us to hack our token balances is that present in this contract as well?

  * The answer is yes, because we're not using SafeMath.

In remix highlight the `transfer` function.

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] -= value;
    balances[recipient] += value;
}
```

* This function would allow us to send tokens without having a balance and would cause the hacker's balance to increase to the maximum value that `uint` allowed.

At the top of the contract add the`SafeMath` import and use the safemath `uint` alias.

```solidity
import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract ArtTokenVulnerable {
    using SafeMath for uint;
```

Then redfine the inside of your `transfer` function to use the `add` and `sub` methods.

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] = balances[msg.sender].sub(value);
    balances[recipient] = balances[recipient].add(value);
}
```

* We can switch our `transfer` function to use the `add` and `sub` SafeMath methods to prevent integer overflow attacks.

* Let's see what else we can find in this contract!

Next highlight the `withdrawBalance()` function.

```solidity
function withdrawBalance() public{
    if( ! (msg.sender.call.value(userBalance[msg.sender])() ) ){
        revert();
    }
    userBalance[msg.sender] = 0;
}
```

* This function sends the amount of `userBalance[msg.sender]`s ether to `msg.sender`.

* With the current structure of this function if `msg.sender` is a contract, it will call its fallback function.

* Because of how state is poorly tracked in this function it allows users to syphon off funds and revert the state to say that the user still has a balance

* This is a prime example of a re-entrancy attack. Luckily theirs a simple fix for this.

Inside the `widthdrawBalance` function define a new `uint` named `amount` and use it to save the current `msg.sender`'s `userBalance`. Then set the `userBalance` to 0.

```solidity
function withdrawBalance(){
    uint amount = userBalance[msg.sender];
    userBalance[msg.sender] = 0;
    if( ! (msg.sender.call.value(amount)() ) ){
            revert();
    }
}
```

* To protect against re-entrancy the state variable has to be change before the call.

* We are going to define a new `uint` named `amount` and use it to save the current `msg.sender`'s `userBalance`.

* Then we are going to set the `userBalance` to 0.

 Now highlight the `mint` function and pose the following question to the class.

```solidity
function mint(address recipient, uint value) public {
    balances[recipient] += value;
}
```

* Do you see anything wrong with the the current state of the mint function?

* **Answer**: Currently our mint function does not check to see if you are the owner of the contract. This allows anyone to mint new tokens and increase their balance.

* This final vulnerability that we're going to fix isn't complicated but one that is extremely important to fix.

* We can fix this easily by adding a simple `require` statement.

Modify the mint function to add the following require statement that checks if the current `msg.sender` is the owner of the contract.

```solidity
function mint(address recipient, uint value) public {
    require(msg.sender == owner, "You do not have permission to mint tokens!");
    balances[recipient] += value;
}
```

* And just like that we've fixed a major vulnerability in our code.

* We should now have a much more secure contract!

End the activity with a few brief review questions.

* What is the solution we used to fix our underflow/overflow issues?

  * **Answer:** OpenZeppelin's SafeMath library!

* Who is ultimately responsible for the cybersecurity of an organization?

  * **Answer:** Everyone is responsible for carrying the burden of security!

* Why not just offload this stuff to the security team?

  * **Answer:** The security team is already going to be overwhelmed with many other things to patch and is fighting a constant upward-hill battle.

  * **Answer:** Every little bit of effort towards security helps.

  * **Answer:** We can't be lazy when developing and leave security as an afterthought.

  * **Answer:** Because that's how the technology industry became so vulnerable in the first place!

Now it's time for the students to analyze some contracts of their own. Let them know that this is an important step to not only becoming a knowledgeable smart contract engineer but in general a more security minded programmer.

### 14. Students Do: Bug Hunt - Identifying Common Vulnerabilities (15 min)

In this activity, students will spend the time looking through a vulnerable smart contract to identify various vulnerabilities.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/07-Stu_Identifying_Common_Vulnerabilities/README.md)

**Files:**

* [ArcadeTokenVulnerable.sol](Activities/07-Stu_Identifying_Common_Vulnerabilities/Solved/ArcadeTokenVulnerable.sol)

Ensure that students are identifying the three mentioned vulnerabilities and are taking the proper steps to address each one.

### 15. Instructor Do: Review Smart Contract Security (5 min)

Now that students have scanned their contracts, ask them the following questions:

* Who is ultimately responsible for the cyber-security of an organization?

  **Answer:** Everyone is responsible for carrying the burden of security!

* After fixing our vulnerabilities, are our contracts "hack-proof?"

  **Answer:** We cannot guarantee that they are hack-proof, but we still performed due diligence.

  **Answer:** There may be a bug in our logic that the tool cannot pick up, so we should still have a 3rd party security team test and audit these contracts before deploying to production/mainnet.

Now that students have analyzed and fixed their contracts, it's time for them to dive a bit deeper into some common vulnerabilities. Present the MythX/Mythril tool to the class by opening the [MythX](https://mythx.io/) website.

* MythX is a service that is based on an open-source command-line tool, [Mythril](https://github.com/ConsenSys/mythril), that allows Solidity developers to scan for common low-level vulnerabilities in their contracts. The tool has integrations with many IDEs, including Remix itself!

* This tool will help identify the low hanging fruit that you can take care of easily during development. **However**, no automated security tool will uncover **all** vulnerabilities. For instance, it can't uncover logical bugs, like if you are missing some `require`s or have a function that doesn't quite check all of the required access control permissions needed for the contract to work as expected. Essentially, it can detect the little things here and there that could potentially lead to big exploits, but it cannot tell if your contract fulfills its design requirements.

In the next activity students will take a look at some of the registries containing common smart contract vulnerabilities where tools like MythX pull their data from.

### 16. Students Do: Exploring Common Smart Contract Vulnerabilities (SWCs) (10 min)

In this activity, students will use the remaining time to explore the most common smart contract vulnerabilities by checking out the [SWC Registry](https://swcregistry.io/) and the [SWC Coverage](https://mythx.io/swc-coverage/) that MythX supports.

**Instructions:**

* [README.md](Activities/08-Stu_SWC_Exploration/README.md)

Have TAs circulate the room and ensure that students are looking at example code and trying to understand the different vulnerabilities they are researching.

Some vulnerabilities may be very complex or low-level, encourage the students to dig deeper into a concept they uncover that they don't understand by researching more examples online.

If students get too confused, have them move onto other vulnerabilities and have them take a step back and slow down, or practice working with the example code in Remix.

### 17. Instructor Do: Review SWCs (5 min)

Ask the students the following questions:

* What was the most interesting vulnerability you found?

* Why is it useful to be able to explore a registry of vulnerabilities like the SWC?

  **Answer:** The ability to identify vulnerabilities in code by recognizing a pattern is extremely useful when developing software.

  **Answer:** By having a list that contains example code and an identifiable SWC number, one can practice avoiding the vulnerabilities before having a tool identify them.

### 18. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
