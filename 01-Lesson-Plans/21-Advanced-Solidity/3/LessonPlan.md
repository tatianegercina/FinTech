# 21.3 Lesson Plan: Writing Secure Contracts with OpenZeppelin

### Overview

In the last class, students were introduced to several of the popular ERC token standards (20, 721, 777, 1155) and implemented an ERC20 compliant token using the OpenZeppelin libraries. Today students will be introduced to the concept of crowdsales, a popular method for distributing tokens; they will explore popular historic crowdsales and implement their own crowdsale using the OpenZeppelin libraries.

### Class Objectives

By the end of the unit, students will be able to:

* Articulate different types of crowdsales and how Ethereum/blockchain makes them much easier and auditable.

* Prepare an ERC777Mintable token for Crowdsale

* Build a crowdsale that distributes an ERC777Mintable token.

* Design contracts to avoid common security pitfalls, such as a re-entrancy attack.

* Perform a Mythril security scan on contracts to test for simple security vulnerabilities.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).


### Instructor Notes

* TBD

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

  * **Answer** Non-fungible tokens use ERC 721, fungible tokens use ERC 777.

Now that the students are familiar with tokens and the various ERC token standards, briefly introduce the concept of token distributions by discussing the following question with the class.

* Explain the following to students:

  * We understand basic tokenomics and how to implement our own ERC compliant token, but now how do we distribute that token to users and create a market for it?

  * This is where a `crowdsale` comes in.

Inform the class that we will be discussing the concept and application of crowdsales in the next activity.

### 2. Instructor Do: Crowdsales in Ethereum (10 min)

In this activity, you will explain how crowdsales have become a popular method for distributing tokens.

* For companies and startups, it's cheap to have new ideas, but executing those ideas can be very expensive.

* Over the last decade, `crowdfunding` has become a popularized way for projects to receive funding that enables them to successfully bring their product or service to production.

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

Explain to the class that tokenomics still plays a huge rule in `crowdsales`. Investors backing the project aren't always just buying the token because they believe the future project will be successful but also because they believe the perceived market value of the token will increase.

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

* When implementing a crowdsale, you have to first decide how you are going to release tokens to the participants of the sale. This is known as `token emission` and is normally done in one of three ways:

  * The crowdsale contract owns a given number of tokens and transfers ownership of them as users purchase them.

  * The crowdsale contract dynamically mints new tokens as they are purchased.

  * The crowdsale contract has access to a multi-sig wallet from which it can transfer ownership of tokens as they are purchased.

### 3. Students Do: Crowdsale Exploration and Discussion (10 min)

Students will be provided a list of crowdsales from which they will explore and research some of the most popular crowdsales in history.

**Instructions:**

* [README.md](Activities/03_Stu_Crowdsale_Exploration_and_Discussion/README.md)

### 4. Instructor Do: Crowdsales Review (5 min)

Discuss the following review questions with the class.

* What were some of the factors or interesting things about the explored historical crowdsales?

* **Example Answer** The price of ether during its initial sale was 2000 ETH per BTC.

* **Example Answer** According to the Ethereum blogpost "Ether is a product, NOT a security or investment offering. Ether is simply a token useful for paying transaction fees or building or purchasing decentralized application services on the Ethereum platform; it does not give you voting rights over anything, and we make no guarantees of its future value."

* **Example Answer** Basic Attention Token raised 36 million in 24 seconds hitting the hard cap on their token supply.

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

### 4. Students Do: ERC20Mintable Token Design

In this activity, students will build a mintable ERC20token and prepare it for a crowdsale.

### 8. Instructor Do: OpenZeppelin Crowdsales (15 min) (Critical)

In this activity, you will demonstrate OpenZeppelin's Crowdsale contract library by creating an `ArcadeTokenSale` and an `ArcadeTokenSaleDeployer` contract that will mint tokens automatically when users send Ether to the `ArcadeTokenSale`.

**Files:**

* [ArcadeTokenMintable.sol](Activities/08-Ins_Crowdsales/Solved/ArcadeTokenMintable.sol)

* [ArcadeTokenSale.sol](Activities/08-Ins_Crowdsales/Solved/ArcadeTokenSale.sol)

Explain to the students:

* In this activity, we will be exploring the Crowdsale contracts that OpenZeppelin provides. Since our token is now `ERC20Mintable`, we will create a `MintedCrowdsale` that will automatically manage our token sale securely.

* OpenZeppelin Crowdsale contracts allow us to do a variety of things, including the ability to configure (amont many others):

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
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/crowdsale/emission/MintedCrowdsale.sol";

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

* This will allow `ArcadeTokenSale` to initialize all of the variables that `Crowdsale` requires. The body of the constructor can stay empty, since all of the logic is already in the `Crowdsale` and `MintedCrowdsale` contracts.

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

* We are going to use a temporary contract, called `ArcadeTokenSaleDeployer` to help us deploy and configure our `ArcadeToken` and `ArcadeTokenSale` contracts with all of the correct information.

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

* Since `msg.sender` is the default minter when deploying `ERC20Mintable` tokens, and `ArcadeTokenSaleDeployer` is the `msg.sender` when creating the token, we need to set things straight by making the `ArcadeTokenSale` contract a minter, and having the `ArcadeTokenSaleDeployer` renounce its "mintership," since we only want the crowdsale contract to have control of minting.

Your contract should now match the [ArcadeTokenSale.sol](Activities/08-Ins_Crowdsales/Solved/ArcadeTokenSale.sol) solution linked above.

Navigate back to the `ArcadeTokenMintable.sol`.

Remove the `mint` call that was in the constructor. The contract should look like the solution linked above:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Mintable.sol";

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

* It is especially important to think twice about who exactly `msg.sender` is, and how `msg.sender` can be manipulated. Remember, other people can write smart contracts that could talk to yours, so `msg.sender` isn't always going to be a simple wallet.

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

* [README.md](Activities/09-Stu_ArcadeTokenSale/README.md)

**Files:**

* [ArcadeTokenMintable.sol](Activities/09-Stu_ArcadeTokenSale/Unsolved/ArcadeTokenMintable.sol)

* [ArcadeTokenSale.sol](Activities/09-Stu_ArcadeTokenSale/Unsolved/ArcadeTokenSale.sol)

Ensure that students are not modifying the constructor *parameters* of `ArcadeTokenMintable`, since it needs to match the ERC20 standard, which specifies `(string name, string symbol, uint initial_supply)`. We pass in `0` as the `initial_supply` when initializing the `ArcadeToken`.

### 10. Instructor Do: Crowdsales Review (10 min)

**Files:**

* [ArcadeTokenMintable.sol](Activities/09-Stu_ArcadeTokenSale/Solved/ArcadeTokenMintable.sol)

* [ArcadeTokenSale.sol](Activities/09-Stu_ArcadeTokenSale/Solved/ArcadeTokenSale.sol)

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

* Why must we be careful about using `msg.sender` as a check in our contracts?

  * **Answer:** `msg.sender` can also be another smart contract, so if the logic requires a human to be on the other end, it might not work.

* Why do `ArcadeToken` and `ArcadeTokenSale` have empty constructor bodies?

  * **Answer:** All of the logic for these contracts is handled in the contracts that they inherit, so no additional logic is needed.

Explain to the students that for the rest of the class, we will be examining the security of the crowdsale we just built, and learning about the common vulnerabilities that smart contract developers should avoid.

### 13. Instructor Do: Solidity Security / MythX Intro (15 min) (Critical)

In this activity, you will demonstrate the MythX security tool, and how it can identify some common security vulnerabilities in Solidity contracts.

**Files:**

* [ArcadeTokenVulnerable.sol](Activities/13-Ins_Security/Solved/ArcadeTokenVulnerable.sol)

Security is a fundamental topic regarding anything to do with technology, especially software that works directly with monetary value. Stress the importance of security:

* In our testnet and local development environments, we are able to "battle test" our code before we deploy it to the prime-time mainnet. It is especially important when programming smart contracts to avoid certain design patters that lead to vulnerabilities that could potentially be exploited.

* Software security is not a new field, but it has recently exploded in demand and will continue to be a critical part of the software development lifecycle. Security is not just left to the security team in the software world; in reality, the security of a system is the sum of its technical and human aspects, and every person in an organization should be working towards the goal of higher security.

* Typically organizations will have dedicated security teams continuously vetting and testing the software and operations. This does not mean you are off the hook! As the engineers, you are the first, and often, only line of defense standing between a hacker and your trophies. When developing software, you should be taking security very seriously and integrate it from the ground up.

Briefly discuss the Ethereum DAO hack:

* Historically, we have seen instances of hacking in every industry. Since the blockchain space is still in adolescence and is rapidly growing, stumbles have occurred regarding smart contracts.

* A notable instance of this is the DAO hack. This was an organization built entirely from smart contracts that was exploited due to a low-level technical attack called a "re-entrancy" attack that allowed a hacker to drain the contract's funds, which we will learn more about soon. Since this attack, measures have been made to help prevent such attacks, and more security improvements are being made every day.

* Thus, it is important to learn how to spot these vulnerabilities. One way we can do that is to leverage security tools that analyze our code and test it for these low-level vulnerabilities.

Present the MythX/Mythril tool to the class by opening the [MythX](https://mythx.io/) website.

* MythX is a service that is based on an open source command line tool, [Mythril](https://github.com/ConsenSys/mythril), that allows Solidity developers to scan for common low-level vulnerabilities in their contracts. The tool has integrations with many IDEs, including Remix itself!

* This tool will help identify the low hanging fruit that you can take care of easily during development. **However**, no automated security tool will uncover **all** vulnerabilities. For instance, it can't uncover logical bugs, like if you are missing some `require`s or have a function that doesn't quite check all of the required access control permissions needed for the contract to work as expected. Essentially, it can detect the little things here and there that could potentially lead to big exploits, but it cannot tell if your contract fulfils its design requirements.

Open up [Remix](https://remix.ethereum.org) and enable the MythX plugin:

![MythX Remix Plugin](Images/mythx-remix.gif)

* This plugin will run in trial mode, but you can create an account at the MythX website, and configure the plugin credentials.

* Registration is easy (and free), it's simply providing an email and signing a message with MetaMask, but this is optional.

* We can use this tool for unlimited scans. We would only need to pay for this tool for increased analysis that uses other tools behind the scenes, besides the open source Mythril tool.

Now, time to use an old contract as an example for what a vulnerable contract could look like. Create a new file called `ArcadeTokenVulnerable.sol` and populate it with the [file linked above](Activities/13-Ins_Security/Solved/ArcadeTokenVulnerable.sol).

* Remember this contract we wrote back when we first learned how tokens worked?

* Remember how we had an integer underflow/overflow vulnerability that allowed us to hack our token balances?

For example:

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] -= value;
    balances[recipient] += value;
}
```

* This function would allow us to send tokens without having balance, and would actually cause the hacker's balance to increase to the maximum value that `uint` allowed.

* Let's see what MythX has to say about this contract!

Open up the MythX tab in Remix, ensuring that your contract has compiled, and click the `Analyze` button:

![MythX Analyze](Images/mythx-analyze.png)

This process can take up to 2 minutes, while you are waiting, ask the students:

* What is the solution we used to fix our underflow/overflow issues?

  **Answer:** OpenZeppelin's SafeMath library!

* Who is ultimately responsible for the cyber security of an organization?

  **Answer:** Everyone is responsible for carrying the burden of security!

* Why do we use tools like this? Why not just offload this stuff to the security team?

  **Answer:** The security team is already going to be overwhelmed with many other things to patch and is fighting a constant upward-hill battle.

  **Answer:** Every little bit off effort towards security helps.

  **Answer:** We can't be lazy when developing and leave security as an afterthought.

  **Answer:** Because that's how the technology industry became so vulnerable in the first place!

When the analysis finishes, point out the different vulnerabilities that MythX
identified by clicking on the red and yellow boxes in the sidebar:

![MythX Analysis](Images/mythx-done.png)

* Notice that we have nice and pretty highlighting of our errors!

* The errors in `red` are critical errors that we **must** fix that MythX has identified.

* As you can see, the tool uncovered the very same issues that we fixed with SafeMath!

* The issues highlighted in `yellow` are warnings. While they are not critical vulnerabilities that MythX knows can be directly exploited, they are flags to look out for. While a hacker might be able to hack your contract using one or two red/critical vulnerabilities as expected, they may also be able to combine several yellow/warning level vulnerabilities to craft an exploit that leverages multiple "less serious" vulnerabilities.

* It is best to get our contracts as close to fully-passing as possible. However, there are some instances where we simply can't, and there are instances where you might be adding safe-guards where the tool cannot recognize, and generate a warning anyway. These tools are not perfect, but they can help a long way.

Now it's time for the students to analyze some contracts of their own, starting with the crowdsale they just built!

### 14. Students Do: Scanning Contracts with MythX (15 min)

In this activity, students will spend the time scanning the contracts they have built so far in class, starting with the `ArcadeTokenSale` they just built.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/14-Stu_Scanning_with_MythX/README.md)

**Files:**

* [ArcadeTokenVulnerable.sol](Activities/14-Stu_Scanning_with_MythX/Solved/ArcadeTokenVulnerable.sol)

Ensure that students are scanning their contracts with MythX properly.

If the students are having difficulties, try the following:

* Remove and re-add the MythX plugin in Remix. Hard refresh or clear cookies to reset any cobbled state.

* If the trial does not work properly, register an account at [MythX.io](https://mythx.io) while MetaMask is pointing to the mainnet, then save the credentials in the MythX plugin while in mainnet. Then, MetaMask can be switched back over. This process should take about 2-3 minutes.

### 15. Instructor Do: Review MythX (5 min)

Now that students have scanned their contracts, ask them the following questions:

* What was the most common vulnerability that kept popping up?

  **Answer:** Floating pragma version, state variable visibility not being set, etc.

* After fixing our vulnerabilities, are our contracts "hack-proof?"

  **Answer:** We cannot guarantee that they are hack proof, but we still performed due diligence.

  **Answer:** There may be a bug in our logic that the tool cannot pick up, so we should still have a 3rd party security team test and audit these contracts before deploying to production/mainnet.

Now that students have scanned and fixed their contracts, it's time for them to dive a bit deeper into some common vulnerabilities.

### 15. Students Do: Exploring Common Smart Contract Vulnerabilities (SWCs) (10 min)

In this activity, students will use the remaining time to explore the most common smart contract vulnerabilities by checking out the [SWC Registry](https://swcregistry.io/) and the [SWC Coverage](https://mythx.io/swc-coverage/) that MythX supports.

**Instructions:**

* [README.md](Activities/15-Stu_SWC_Exploration/README.md)

Have TAs circulate the room and ensure that students are looking at example code and trying to understand the different vulnerabilities they are researching.

Some vulnerabilities may be very complex or low-level, encourage the students to dig deeper into a concept they uncover that they don't understand by researching more examples online.

If students get too confused, have them move onto other vulnerabilities and have them take a step back and slow down, or practice working with the example code in Remix.

### 16. Instructor Do: Review SWCs (5 min)

Ask the students the following questions:

* What was the most interesting vulnerability you found?

* Why might some vulnerabilities be suppported by the free version of MythX and some require Pro?

  **Answer:** Some analysis takes more computation and time, which costs MythX more.

  **Answer:** Other tools may be used besides the open source tools that MythX makes available.

* Why is it useful to be able to explore a registry of vulnerabilities like the SWC?

  **Answer:** The ability to identify vulnerabilities in code by recognizing a pattern is extremely useful when developing software.

  **Answer:** By having a list that contains example code and an identifiable SWC number, one can practice avoiding the vulnerabilities before having a tool identify them.

### 17. Instructor Do: Structured Review (35 mins)

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
