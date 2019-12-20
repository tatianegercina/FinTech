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
