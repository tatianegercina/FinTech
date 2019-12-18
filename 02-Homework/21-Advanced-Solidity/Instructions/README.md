# Unit 21: You sure can attract a crowd!

![crowd](https://image.shutterstock.com/image-photo/group-people-holding-cigarette-lighters-600w-687342115.jpg)

## Background

Your company has decided to crowdsale their PupperCoin token in order to help fund the network development.
This network will be used to track the dog breeding activity across the globe in a decentralized way.

You will need to create an ERC20 token that will be minted through a `MintedCrowdsale` contract that you can leverage
from the OpenZeppelin Solidity library.

This crowdsale contract will manage the entire process, allowing users to send ETH and get back PPC (PupperCoin).
This contract will mint the tokens automatically and distribute them to buyers in one transaction.

It will need to inherit `CappedCrowdsale` (your choice as to the limit), `RefundableCrowdsale`, and `MintedCrowdsale`.

You will first conduct the crowdsale on the Kovan or Ropsten testnet in order to get a real-world pre-production test in.

## Instructions

### Creating your project

You will need to create a simple Truffle project, as well as create an npm package.

Simply run:

`npm init`
`truffle init`

Then, configure the `truffle-config.js` to connect to both your local development chain as well as the testnet.
You can connect to Kovan using Infura.

### Designing the contracts

#### ERC20 PupperCoin

You will need to import the ERC20 token contract, and you will need to customize the token to fit PupperCoin parameters.

This must also be included in your Crowdsale contract, as the crowdsale contract will need to mint tokens upon purchase.

#### PupperCoinCrowdsale

You will need to bootstrap the contract by inheriting the following OpenZeppelin contracts:

- `CappedCrowdsale`

- `RefundableCrowdsale`

- `MintedCrowdsale`

You will need to customize all of the features of your crowdsale, such as the cap, decimals of the token, duration, etc. Feel free to configure these parameters to your liking.

### Deploying the crowdsale

You will need to create the migration scripts for the ERC20 and the Crowdsale contracts.

You must ensure that you are passing the proper parameters into the contract constructors, or your crowdsale may not
function. You must also correctly import the contracts and link the two together using Truffles `link` feature.

First, deploy the crowdsale to your local blockchain. After you confirm that you can purchase the tokens with ETH,
you will need to request Kovan or Ropsten testnet tokens and deploy it to that network.

Make sure that you have your `truffle-config.js` properly configured in order to deploy to that network, and make sure
to specify the network via the `--network` flag when running `truffle migrate`.

### Testing the crowdsale

You will need to deploy the crowdsale successfully to Kovan or Ropsten.

Test the crowdsale once again using your testnet tokens, then once you confirm that the crowdsale works as expected,
try to add the token to MyCrypto and test a transaction.

You can add custom tokens from the `Add custom token` feature:

![add-custom-token](https://i.imgur.com/p1wwXQ9.png)

### Submission

Create a Github repo, and a `README.md` file explaining the process for purchasing PupperCoin (or whatever name you came up with).

Ensure that anyone can run the steps and add the token to MyCrypto, or a similar wallet.

Include information such as the token parameters, token name, crowdsale cap, etc.
