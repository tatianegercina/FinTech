### 10. Instructor Do: OpenZeppelin's ERC Library (15 min) (Critical)

In this activity, you will demonstrate the ERC20 contract provided by the OpenZeppelin library, and re-implement the ArcadeToken using the official ERC20 standard.

**Files:**

* [ArcadeTokenERC20.sol](Activities/10-Ins_OpenZeppelin_ERC20/Solved/ArcadeTokenERC20.sol)

Explain why we are starting with ERC20 to the students:

* We are going to implement ERC20 before ERC777 for several reasons.

  * It is a simpler standard to understand.

  * It has the widest adoption and support in blockchain explorers, wallets and developer libraries.

  * ERC20 tokens are plentiful in the wild, and are implemented by stablecoins like Coinbase's USDC and Gemini's GUSD, so it is important to understand how they are structured.

  * ERC777 depends another contract defined in EIP1820 to be deployed onto our network, so we'll worry about that later.

Open [Remix](https://remix.ethereum.org) and create a new file called `ArcadeTokenERC20.sol`, and start with the following boilerplate:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {

}
```

Explain to the students:

* OpenZeppelin provides contracts that are implementations of common standards.

* Here, we are importing the ERC20 contracts from the OpenZeppelin library.

* By defining our contract like `ArcadeToken is ERC20, ERC20Detailed`, we are telling the compiler that our contract will *inherit* the functions and properties of `ERC20` and `ERC20Detailed` contracts.

Expand upon the concept of inheritance by opening up the `ERC20.sol` in Remix from the sidebar (you will need to save `ArcadeTokenERC20.sol` to get Remix to load the library):

![OpenZeppelin ERC20 File](Images/oz-erc20.png)

Point out the code in the file:

![OpenZeppelin ERC20 Code](Images/oz-erc20-code.png)

* This contract contains the a `mapping` called `_balances` to keep track of balances in the exact same way we designed our tokens previously. The `balanceOf` function pulls the `uint` value from the `_balances` mapping corresponding to an `address` in the same way we made our balance functions before.

* The `transfer` function is also defined, just like the ERC20 standard specifies. It is formatted a bit differently from the way we defined it when we built our tokens from scratch. This is to make sure that certain security checks are performed. However, the same parameters and general logic is used to get the job done.

* By saying that `ArcadeToken is ERC20`, we are inheriting all of these variables, functions, and so on into our contract. We can inherit from multiple contracts as well!

* This means that we can call the `transfer` function and `balanceOf` functions, as well as the others like `_mint` in order to manage our token.

Next, open up OpenZeppelin's `ERC20Detailed` contract in the same folder and point out the code:

![ERC20Detailed](Images/oz-erc20-detailed.png)

* Since the ERC20 standard defines the `name`, `symbol` (the token's ticker), and other variables as *optional*, OpenZeppelin separates the optional parameters into `ERC20Detailed`.

* Notice that `ERC20Detailed` has its own constructor as well to establish the `name`, `symbol`, and `decimals` parameter. The `name` is the human-friendly name of the token, the `symbol` is the ticker, and the `decimals` are the number of decimal points this token will use. We will stick to Ethereum's default, `18` in most of our cases.

* There are also "getter" functions that return these values.

Close OpenZeppelin's implementations and navigate back to `ArcadeTokenERC20.sol`.

First, define an `address payable owner` at the top of the contract:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;
}
```

Then, add the following constructor below the `owner`:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }
}
```

Explain to the students that this is a constructor that also passes parameters to the ERC20Detailed constructor:

* Notice that in our constructor, we call `ERC20Detailed` and we pass in some parameters.

* Since we are inheriting from `ERC20Detailed`, and `ERC20Detailed` has a constructor, we need to pass the parameters it expects.

* Remember, the `ERC20Detailed` constructor had three parameters: `name`, `symbol`, and `decimals`. Here, we are passing in `ArcadeToken` as the name, `ARCD` as the symbol, and we are using Ethereum's default `18` decimal places for easier conversion.

* In our constructor, we are setting the `owner` as the `msg.sender`, and calling the `_mint` function that OpenZeppelin's `ERC20` provides to us. By passing in `initial_supply`, we can create an initial amount of tokens and send it to the owner upon deployment.

Now, add a `mint` function to the contract:

```solidity
function mint(address recipient, uint amount) public {
    _mint(recipient, amount);
}
```

* Since the `_mint` function is set to `internal` in the `ERC20` contract, we can only call it from within our `ArcadeToken` contract. This means we have to create a new `mint` function here to expose the function and enable us to use it later.

* However, we want to restrict this `mint` function using a `require`. Rather than using the same method we used before, let's create our own `modifier`!

Add the following `modifier` function to the contract:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }
}
```

* A `modifier` is a special function that will allow us to restrict our other functions in the same way that we set them to `public` or `payable`.

* Since we call this modifier `onlyOwner`, we can add `onlyOwner` to the functions that we want to restrict to ourselves.

* Inside the modifier, we add the same `require` that we would normally to ensure that `msg.sender` is the `owner` address.

* At the last line of the modifier, we need to add an underscore `_` to tell Solidity to return to the function that called the modifier.

Now, add the `onlyOwner` modifier after `public` on the `mint` function:

```solidity
function mint(address recipient, uint amount) public onlyOwner {
    _mint(recipient, amount);
}
```

The contract should look like the following up to this point:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
}
```

* That's it! Now this token is a fully functioning ERC20 token, that has a `mint` function that we created an `onlyOwner` modifier for.

* We could potentially deploy this to the mainnet and get this listed on an exchange. It will also automatically be detected by many wallets and block explorers.

Now it's time for the students to implement their own ERC20 tokens!
