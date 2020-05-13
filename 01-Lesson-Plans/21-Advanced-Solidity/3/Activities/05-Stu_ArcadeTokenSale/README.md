# Creating an ArcadeTokenSale with OpenZeppelin

In this activity, you will be creating a crowdsale contract using the OpenZeppelin library that will automatically manage the sale and minting of your ArcadeTokens. Then, after deploying to your local blockchain, you will make a test purchase from the ArcadeTokenSale contract and watch your ArcadeToken balance increase.

## Instructions

* Open up [Remix](https://remix.ethereum.org) and create a new file called `ArcadeTokenSale.sol`. Populate the contents with the [starter code](Unsolved/ArcadeTokenSale.sol).

* First, at the top of the contract, you will need to import `ArcadeTokenMintable.sol`.

* Inside of the `ArcadeTokenSale` contract, you will need to create a constructor that fulfills the parameters that OpenZeppelin's `Crowdsale` contract. According to the [documentation](https://docs.openzeppelin.com/contracts/2.x/api/crowdsale#Crowdsale-constructor-uint256-address-payable-contract-IERC20-), `Crowdsale` accepts three parameters:

  ![Crowdsale Constructor](Images/oz-crowdsale-constructor.png)

  * In our case, we can use `constructor(uint rate, address payable wallet, ArcadeToken token)` since `ArcadeToken` is compatible with the ERC20 interface (IERC20) that the crowdsale contract requires.

  * You will need to pass in the parameters from the main constructor to the secondary `Crowdsale` constructor using the same methodology in `ArcadeTokenMintable.sol`.

  * The body of the constructor can stay empty since all of the logic is inherited from `Crowdsale` and `MintedCrowdsale`.

* Now, below `ArcadeTokenSale`, at the top of the `ArcadeTokenSaleDeployer` contract, add the following variables to store the addresses of the `ArcadeToken` and `ArcadeTokenSale` contracts that this contract will be deploying:

  * An `address public` called `arcade_sale_address`, which will store `ArcadeTokenSale`'s address once deployed.

  * An `address public` called `token_address`, which will store `ArcadeToken`'s address once deployed.

* Inside of the constructor, perform the following:

  * Create the `ArcadeToken` by defining a variable like `ArcadeToken token` and setting it to equal `new ArcadeToken()`. Inside of the parameters of `new ArcadeToken`, pass in the `name` and `symbol` variables. For the `initial_supply` variable that `ArcadeToken` expects, pass in `0`.

    * For example:

    ```solidity
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
    ```

  * Then, store the address of the token by using `token_address = address(token)`. This will allow us to easily fetch the token's address for later from the deploying contract.

  * Next, create the `ArcadeTokenSale` contract instance using the same logic used when creating `ArcadeToken`. Store the variable in `ArcadeTokenSale arcade_sale` and set the parameters:

    * `rate` should be hard-coded to `1` in order to maintain the same units as Ether.

    * `wallet` should be passed in from the main constructor, this is the wallet that will get paid all Ether raised by the `ArcadeTokenSale`.

    * `token` should be the actual `token` variable where `ArcadeToken` is stored.

  * Once again, store the address of the `ArcadeTokenSale` in the `arcade_sale_address` variable for easy access later.

  * Finally, we need to set the `ArcadeTokenSale` contract as a `minter`, then renounce "mintership" from the `ArcadeTokenSaleDeployer` contract, like so:

    ```solidity
    token.addMinter(arcade_sale_address);
    token.renounceMinter();
    ```

    * Remember, we need to do this because when we set our token as `ERC20Mintable`, the `msg.sender` (the person/contract deploying) is automatically set as the default minter. Since `ArcadeTokenSaleDeployer` is actually `msg.sender` in this case, this step will ensure that the `ArcadeTokenSale` is the actual minter, as expected.

* Open up your `ArcadeTokenMintable.sol` contract. It should match what is in this [starter code](Unsolved/ArcadeTokenMintable.sol).

* Remove the `mint` call that is inside of the body of the constructor. The constructor must now be empty since we will be delegating all minting logic to the ArcadeTokenSale contract. Otherwise, since `msg.sender` would be the `ArcadeTokenSaleDeployer` contract, these tokens would be locked up with no function to withdraw, and it is cheaper gas-wise to prevent this from occurring in the first place.

* Deploy and test your contract. You will need to load the `ArcadeTokenSale` and `ArcadeToken` contracts via their deployed address using the `At Address` feature in the `Deploy` tab of Remix:

  ![Deployment](Images/deployment.gif)

* Make a test purchase by setting the `value` field to some Ether value and calling the `buyTokens` function on the `ArcadeTokenSale` contract, then check your balance on the `ArcadeToken` contract:

  ![Purchase](Images/purchase.gif)

## Hints

* If you would like to see the parameters you need to pass to `Crowdsale` on-hand, visit the [OpenZeppelin API documentation](https://docs.openzeppelin.com/contracts/2.x/api/crowdsale#_core) for the details.

* The [Crowdsales Overview](https://docs.openzeppelin.com/contracts/2.x/crowdsales) page on OpenZeppelin's documentation also serves as a good resource for how crowdsales work in detail, and the nuances of different implementations provided.
