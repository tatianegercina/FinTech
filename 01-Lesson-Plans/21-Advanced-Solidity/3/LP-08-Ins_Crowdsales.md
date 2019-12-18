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

Briefly open (**max** 2 minutes) the [OpenZeppelin Crowdsale Documentation](https://docs.openzeppelin.com/contracts/2.x/crowdsales) and explore the different features they discuss. Make a stop at the [Crowdsale Constructor API doc](https://docs.openzeppelin.com/contracts/2.x/api/crowdsale#Crowdsale-constructor-uint256-address-payable-contract-IERC20-) and point out the constructor parameters for the `Crowdsale` contract (`uint256 rate, address payable wallet, contract IERC20 token`).

![OpenZeppelin Crowdsale Documentation](Images/oz-crowdsale-docs.png)

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
