# Unit 20 - "Looks like we've made our First Contract!"

![contract](https://image.shutterstock.com/z/stock-photo-two-hands-handshake-polygonal-low-poly-hud-illustration-smart-contract-agreement-blockchain-and-1161295627.jpg)

## Background

Now that your company has its very own custom blockchain running, the team wants to begin opening the chain to
allow other businesses and individuals to participate and strengthen the network. But first, the team wants to create a system on-chain built to allow these businesses to register a list of addresses that belong to that company.

Fortunately, you've been learning how to program smart contracts with Solidity! What you will be doing this assignment
is creating an `Identity` contract. This contract will be very simple, only storing info such as name, email, website,
GitHub, image URL, a short bio, and an array of payable addresses.

Your coworker has already built you a frontend that will work with the contract, so long as it implements the exact
public variables and functions specified below.

## Files

Truffle project [starter code](Starter-Code/identity.zip)

## Instructions

### Starting your project

Download and extract the starter code above. This contains a small frontend that will interact with your contract when
you successfully implement the proper functions and variables.

You will need to install the dependencies once you `cd` into the `identity` folder by running:

`npm install`

This will allow you to build and deploy the project to Github Pages later.

You can use the development server by running:

`npm run dev`

When you have finished your contract, you can navigate to `localhost:1234` and interact with the contract with MetaMask.

You can build the project for production by running:

`npm run build`

### Designing the Smart Contract

You will need to provide the following `public` variables:

- `name` -- The name of the individual/company as a `string`

- `email` -- The email address of the individual/company as a `string`

- `website` -- The website of the individual/company as a `string`

- `github` -- Github repository/account/project URL `string`

- `image` -- A profile image/logo URL `string`

- `bio` -- A short bio `string`

- `addresses` -- A `payable` `address` array

Feel absolutely free to add more variables you see fit to attach to an Identity. Get creative!

You will need the following functions:

- The `constructor` must include the initial public variables that you'd like the contract to start with.

- `onlyBy(owner)` modifier -- This function should set a `require` check ensuring that only the owner can call the function.

- "Setter" functions -- These functions will be setting the above variables. These *MUST* be restricted to the owner
 of the contract by the `onlyBy(owner)` modifier.

- `getAddress` -- This function will be a `public view` that takes a `uint256` integer index, and returns the designated address from the array. Anyone can call this function and does not need the `onlyBy(owner)` modifier.

- `getAddressCount` -- This `public view` function will return the length of the address array.
 This is necessary to keep track of the number of addresses stored in the contract.

- `delAddress` -- This function will take a `uint256` integer index and delete the designated address from the array.
 This function *MUST* be restricted to the owner of the contract by the `onlyBy(owner)` modifier.

You will also need to create an event that notifies clients that info has changed. You can make separate events for each,
or combine them into a generic event that passes the parameter that was changed as well as the value to the client.

### Setting up the deployment/migration script

We have provided the migration script for the `Identity` contract. This should run without error once the contract
is properly designed.

Take a look inside the `migrations` folder and edit the `2_identity.js` file according to the information you would
like to store on the contract.

The completed migration script should look something like this (but with the complete parameter set):

![2_identity.js](Images/2_identity.png)

### Deploy the contract

Run `truffle migrate` to build and deploy the contract to your local network.

### Connect MetaMask to your local node

Add a custom network to MetaMask if you have not already that points to your local Ganache, PoA, or PoW network.

You should also import the private key from your network that deployed the contract.
This is likely `web3.eth.accounts[0]`.

### Update the frontend

Once you have the contract's address, replace the `const contractAddress = ""` line with the
proper address. If you are running the dev server, the frontend will hot-reload. Make sure that the `identityJson`
path is also correct (it should be pointing to the contract's ABI).

### Test the contract locally

Once you have properly built the contract, the proper variables should appear in the frontend at `localhost:1234`.

This is an example of what the frontend will look like once the smart contract is successfully built:

![frontend-success](Images/frontend-success.png)

There are admin features that only appear when you are using the *same* account in MetaMask that you used to deploy
the contract. This will enable adding and deleting addresses.

The Github, website, and email links should all properly navigate to the correct places. If not, replace the values with
valid links. Use full URLs when setting the variables.

You should be able to set and get values only using the account used to deploy the contract.
This account is likely `web3.eth.accounts[0]` as that is the default used by Truffle.

You can also test the contract by dropping into an interactive Python shell (or writing a script) that uses `web3.py`
to connect to the local chain that the `Identity` contract is deployed to, then using something like:
`identity_contract.functions.FUNCTION_NAME(param).transact(TX_PARAMS)` and setting the function name and building the
transaction parameters.

### Deploy to a testnet

Request the testnet tokens from your preferred faucet, on your preferred testnet (not your local chain).

You may use either Ropsten, Kovan, Rinkeby, Goerli, or any networks that are bundled with MetaMask.

Configure your `truffle-config.js` to properly utilize your Infura account (or if you are running) and point to the
designated testnet.

Once you deploy the contract successfully, you will need to update the `contractAddress` variable in `dapp.js` again
before you deploy the frontend.

## Resources

Building the next financial revolution isn't easy, but we need your help, don't be intimidated by the semicolons!

There are lots of great resources to learn Solidity. Remember, you are helping push the very edge of this space forward,
so don't feel discouraged if you get stuck! In fact, you should be proud that you are taking on such a challenge!

For some simple and succinct code snips, check out [Solidity By Example](https://github.com/raineorshine/solidity-by-example)

For a larger list of awesome Solidity resources, checkout [Awesome Solidity](https://github.com/bkrem/awesome-solidity)

Another tutorial is available at [EthereumDev.io](https://ethereumdev.io/)

If you enjoy building games, here's a great tutorial called [CryptoZombies](https://cryptozombies.io/)

## Submission

Create a `README.md` that explains what testnet the contract is on, and how to connect MetaMask to it.

You will also deploy this dApp to Github Pages. Your coworker has provided a helper script to assist in deploying.

Create a Github repo, name it `identity-dapp`. If you would like to name it something else, you will need to change the
following line in the `package.json` file:

`"build": "parcel build -d build/frontend --public-url ./identity-dapp/ index.html",`

You must change the `./identity-dapp/` portion to `./your-repo-name/`. This is necessary to generate the URLs properly
on the page, since Github Pages defaults to the `https://username.github.io/your-repo-name/` format.

If you are deploying to a URL that is at the "root" domain (i.e., no `/your-repo-name/` prefix) such as
`https://identity-dapp.yourportfoliosite.com`, you can remove the `--public-url ./identity-dapp` flag entirely.

Once your Github Pages repo is configured, initialize your `identity` project folder with the instructions given and
push your code.

When ready, simply run `npm run deploy` -- this will build the frontend to a separate branch that will be hosted via
Github Pages.

Navigate to the deployed dApp, set MetaMask to the proper network, and make sure the frontend works!

Congratulate yourself for building a decentralized identity system!
