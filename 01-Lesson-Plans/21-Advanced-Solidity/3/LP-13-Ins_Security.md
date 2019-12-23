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
