# "Looks like we've made First Contract!"

![contract](https://image.shutterstock.com/z/stock-photo-two-hands-handshake-polygonal-low-poly-hud-illustration-smart-contract-agreement-blockchain-and-1161295627.jpg)

## Background

Now that your company has its very own custom blockchain running, the team wants to begin opening the chain to
allow other businesses and individuals to participate and strengthen the network. But first, the team wants to create a system on-chain
built to allow these businesses to register a list of addresses that belong to that company.

Fortunately, you've been learning how to program smart contracts with Solidity! What you will be doing this assignment
is creating an `Identity` contract. This contract will be very simple, only storing the names, addresses, phone, location,
and other details about that entity.

## Dependencies

You will need to install the following tools, if you have not installed them in class already:

- [Truffle Suite](https://www.trufflesuite.com/)

- Either your own local blockchain built previously in class, or [Ganache](https://www.trufflesuite.com/ganache)

## Creating your project

Create a new project directory, then inside, run the following command:

`truffle init`

This will create a new project for you.

![truffle-success](Images/truffle.png)

Now you must modify the `truffle-config.js` to include the `development` network that is pointed to your local chain.

## Designing the Smart Contract

You will need to provide the following `public` variables:

- `name` -- The name of the individual/company

- `location` -- The physical location of the individual/company

- `phone` -- The phone number of the individual/company

- `email` -- The email address of the individual/company

- `addresses` -- A public list of `payable` addresses

Feel absolutely free to add more variables you see fit to attach to an Identity. Get creative!

You will need the following functions:

- The `constructor` must include the initial public variables that you'd like the contract to start with.

- `onlyBy(owner)` modifier -- This function should set a `require` check ensuring that only the owner can call the function.

- "Setter" functions -- These functions will be setting the above variables. These *MUST* be restricted to the owner
  of the contract by a `modifier` function.

- `getAddress` -- This function will be a `public view` that takes an integer index, and returns the designated address
  from the array. Anyone can call this function and does not need the `onlyBy(owner)` modifier.

You will also need to create an event that notifies clients that info has changed. You can make separate events for each,
or combine them into a generic event that passes the parameter that was changed as well as the value to the client.

## Setting up the deployment/migration script

This is the easy part! All you must do take a look inside of the `migrations` folder that `truffle` created for you.
You need to copy the `1_initial_migration.js` script into a file named something like `2_identity.js` (name is up to you).
Next, you simply need to find anywhere that `Migration` is listed as the contract name and replace it with `Identity`.
After that, `truffle` will recognize the new deployment job and will migrate the contract for you upon a `truffle migrate`!

However, we need to set the values we defined in the `constructor`. In order to do this, simply add the parameters to
the line in `2_identity.js` that says: `deployer.deploy(Identity);` like so: `deployer.deploy(Identity, param1, param2);`
Later in the course, you will do slightly more powerful migrations, but for now, this simple deploy script will work!

The completed migration script should look something like this (but with the complete parameter set):

![2_identity.js](Images/2_identity.png)

## Test the contract

You should be able to set and get values only using the account used to deploy the contract.
This account is likely `eth.accounts[0]` as that is the default used by Truffle.

You can test the contract by dropping into an interactive Python shell (or writing a script) that uses `web3.py`
to connect to the local chain that the `Identity` contract is deployed to, then using something like:
`identity_contract.functions.FUNCTION_NAME(param).transact(TX_PARAMS)` and setting the function name and building the
transaction parameters.

## Submission

For this submission, you may simply upload the entire Truffle project to Github and submit the repository URL.

You may write a `README.md` that explains the details of your contract and what the intended use case is.

## You can do it! If you get stuck...

Building the next financial revolution isn't easy, but we need your help, don't be intimidated by the semicolons!

There are lots of great resources to learn Solidity. Remember, you are helping push the very edge of this space forward,
so don't feel discouraged if you get stuck! In fact, you should be proud that you are taking on such a challenge!

For some simple and succinct code snips, check out [Solidity By Example](https://github.com/raineorshine/solidity-by-example)

For a larger list of awesome Solidity resources, checkout [Awesome Solidity](https://github.com/bkrem/awesome-solidity)

Another tutorial is available at [EthereumDev.io](https://ethereumdev.io/)

If you enjoy building games, here's a great tutorial called [CryptoZombies](https://cryptozombies.io/)
