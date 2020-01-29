# Matching a Contract Specification

In this activity, you will take a simple smart contract specification, in this particular case the ERC333 example contract specification and implement it.

## Instructions

* Throughout your reading attempt to identify the goal of the ERC333 copyright contract.

* Begin by opening the [Example CryptoRight EIP](Resources/ExampleEIP.md) and reading the `Simple Summary`, `Abstract` and `Motivation` sections of the EIP.

* Open [Remix](https:://remix.ethereum.org/) in your web browser and create two new contracts the first-named `ICryptoRight.sol` and the second named `CryptoRight.sol`.

* Inside `ICryptoRight.sol` paste the contents of [ICryptoRight.sol](Resources/ICryptoRight.sol) from the resources folder.

* Inside `CryptoRight.sol` define a new contract named `CryptoRight` that implements the `ICryptoRight` interface by using the `CryptoRight is ICryptoRight` syntax.

* Next, pull up Remix side by side with the [Example CryptoRight EIP](Resources/ExampleEIP.md). Go through each method definition/description inside the specification section of the EIP document, scaffolding out each function definition with comments and adding it's corresponding business logic.

## Challenge

* If time remains, deploy your contract in Remix and attempt to create a new open-source or copyrighted work.

## Hints

* Break each method description down into its core requirements. What values does it accept as input, what does it do with the input values, what values does it return as output.

* If you're struggling to write the business logic of a function remember that it can help to plan out each step with a comment.

* If stuck for an extended period raise your hand and review the contract specification with a TA.
