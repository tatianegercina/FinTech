# Unit 20 - "Looks like we've made First Contract!"

![contract](https://image.shutterstock.com/z/stock-photo-two-hands-handshake-polygonal-low-poly-hud-illustration-smart-contract-agreement-blockchain-and-1161295627.jpg)

## Background

Now that your company has its very own custom blockchain running, the team wants to build a smart contract that will allow the team to split the company profits 3 ways.

Fortunately, you've been learning how to program smart contracts with Solidity! What you will be doing this assignment is creating a `ProfitSplitter` contract. This contract will accept payment using a `deposit` function, and automatically divide the Ether among the beneficiaries.

You will deploy the contract to an Ethereum testnet, like Kovan, so the team can test it out before moving to production.

## Files

ProfitSplitter [starter code](Starter-Code/ProfitSplitter.sol)

## Instructions

### Starting your project

Navigate to the [Remix IDE](https://remix.ethereum.org) and create a new contract called `ProfitSplitter.sol` using the starter code above.

While developing and testing your contract, use the [Ganache](https://www.trufflesuite.com/ganache) development chain, and point MetaMask to `localhost:8545`, or replace the port with what you have set in your workspace.

### Designing the Smart Contract

At the top of your contract, you will need to define the following `public` variables:

* `beneficiary_one` -- The `address` of the first beneficiary. Make sure to set this to `payable`.

* `beneficiary_two` -- Another `address payable` that represents the second beneficiary.

* `beneficiary_three` -- The third `address payable` that represents the third beneficiary.

Create a constructor function that accepts:

* `address payable _one`

* `address payable _two`

* `address payable _three`

Within the constructor, set the beneficiary addresses to equal the parameter values. This will allow you to avoid hardcoding the beneficiary addresses.

Next, create the following functions:

* `balance` -- This function should be set to `public view returns(uint)`, and must return the contract's current balance. Since we should always be sending Ether to the beneficiaries, this function should always return `0`. If it does not, the `deposit` function is not handling remainders properly and should be fixed. This will serve as a test function of sorts.

* `deposit` -- This function should set to `public payable` check ensuring that only the owner can call the function.

  * In this function, perform the following steps:

    * Set a `uint amount` to equal `msg.value / 3;` in order to calculate the split value of the Ether.

    * Transfer the `amount` to `beneficiary_one`.

    * Repeat the steps for `beneficiary_two` and `beneficiary_three`.

    * Since `uint` only contains positive whole numbers, and Solidity does not fully support float/decimals, we must deal with a potential remainder at the end of this function, since `amount` will discard the remainder during division.

    * We may either have `1` or `2` wei leftover, so pick a beneficiary that gets the change and transfer them the `msg.value - amount * 3`. This will re-multiply the `amount` by 3, then subtract it from the `msg.value` to account for any leftover wei.

* Create a fallback function using `function() external payable`, and call the `deposit` function from within it. This will ensure that the logic in `deposit` executes if Ether is sent directly to the contract. This is important to prevent Ether from being locked in the contract, since we don't have a `withdraw` function in this use-case.

### Challenge

Create a rolling counter called `uint counter` at the top of the contract.

In the `deposit` function, you can create a counter that goes from `0` to `2` before resetting back to `0` using modulous. Create a some of `if` statements to check which beneficiary to send the leftover wei to by checking the counter, then increment it with `counter += counter % 2`.

This will make the way remainders are handled more fair to the each beneficiary.

### Test the contract

In the `Deploy` tab in Remix, deploy the contract to your local Ganache chain by connecting to `Injected Web3` and ensuring MetaMask is pointed to `localhost:8545`.

You will need to fill in the constructor parameters with your designated `beneficiary` addresses.

Test the `deposit` function by sending various values. Keep an eye on the `beneficiary` balances as you send different amounts of Ether to the contract and ensure the logic is executing properly.

![Remix Testing](Images/remix-test.png)

### Deploy to a live Testnet

Once you feel comfortable with your contract, point MetaMask at the Kovan or Ropsten network. Ensure you have test Ether on this network!

After switching MetaMask to Kovan, simply deploy the contract as before and keep note of the deployed address. The transaction will also be in your MetaMask history, and on the blockchain permanently to explore later.

![Remix Deploy](Images/remix-deploy.png)

## Resources

Building the next financial revolution isn't easy, but we need your help, don't be intimidated by the semicolons!

There are lots of great resources to learn Solidity. Remember, you are helping push the very edge of this space forward,
so don't feel discouraged if you get stuck! In fact, you should be proud that you are taking on such a challenge!

For some simple and succinct code snips, check out [Solidity By Example](https://github.com/raineorshine/solidity-by-example)

For a larger list of awesome Solidity resources, checkout [Awesome Solidity](https://github.com/bkrem/awesome-solidity)

Another tutorial is available at [EthereumDev.io](https://ethereumdev.io/)

If you enjoy building games, here's a great tutorial called [CryptoZombies](https://cryptozombies.io/)

## Submission

Create a `README.md` that explains what testnet the contract is on, the motivation for the contract.

Upload this to a Github repository that explains how the contract works, and provide the testnet address for others to be able to send to.
