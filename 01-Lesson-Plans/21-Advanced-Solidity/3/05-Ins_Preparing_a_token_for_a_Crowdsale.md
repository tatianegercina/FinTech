### 5. Instructor Do: Preparing a token for a Crowdsale (10min)

In this activity, students will be introduced to the ERC20Mintable contract from OpenZeppelin, and how they can use it to prepare a token that can work in a crowdsale.

**Files:**

[ArcadeTokenMintable.sol](Activities/05-Ins_Preparing_a_token_for_a_Crowdsale/Solved/ArcadeTokenERC20.sol)

Open [Remix](https://remix.ethereum.org) and create a new file called `ArcadeTokenMintable.sol`, and start with the following boilerplate:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
}
```

Explain to the students:

* As previously discussed, OpenZeppelin provides contracts that are implementations of common standards.

* Here, just like before we are importing the ERC20 contracts from the OpenZeppelin library, now, however, we are also going to import and implement a new contract called `ERC20Mintable`

Add the ERC20MIntable reference to the contract definition.

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
}
```

Now that we have inherited the structures from `ERC20`, `ERC20Detailed`, and `ERC20Mintable`.

* By saying that `ArcadeToken is ERC20`, we are inheriting all of the properties and functions of ERC20Mintable into our new contract. As you have seen, we can inherit from multiple contracts; we are now going to inherit the defined functions and properties for ERC20, ERC20Detailed, and ERC20mintable.

Once again, expand upon the concept of inheritance by opening up the `ERC20Mintable.sol` in Remix from the sidebar (you will need to save `ArcadeTokenMintable.sol` to get Remix to load the library):

![ERC20MintableFile](Images/ERC20MintableFile.png)

Take a moment to point out the code in the file, particularly the comments.

![ERC20MintableCode](Images/ERC20MintableCode.png)

* `ERC20Mintable` extends `ERC20` to add a set of accounts with the MinterRole, who have permission to mint (create) new tokens as they see fit.

* At construction, the deployer of the contract is the only minter.

* The `onlyMinter` modifier restricts the mint function so that only accounts with the MinterRole can call the mint function.

Close OpenZeppelin's `ERC20Mintable` and navigate back to `ArcadeTokenMintable.sol`.

Now that `ERC20Mintable`'s functionality has been imported into our new contract it's time to add our constructors.

First add the constructor for the ArcadeToken contract itself. This constructor will accept a string `name`, a string `symbol`, and a uint `initial_supply`.

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
}
```

* Our contracts constructor accepts three values a string `name`, a string `symbol`, and a uint `initial_supply`.

Next define the constructor for the `ERC20Detailed` contract that we are importing.

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
}
```

* Here we are defining the constructor for the `ERC20Detailed` contract that we previously imported.

* `ERC20Detailed`'s constructor accpets the variable name, and symbol that we defined in the main ArcadeToken contract.

* Here we are also hardcoding the number `18` as our third parameter. This parameter defines the number of decimals that our token will have. In this case the number `18` denotes that the smallest increment of our token is `.000000000000000001`.

Finally it's time to define the contracts body. Inside the body of the contract call the `mint` function and pass it the current `msg.sender` and the `inital_supply` variable that is defined in our constructor.

Your complete code should now look something like this.

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        mint(msg.sender, initial_supply);
    }
}
```

* Now when our `ArcadeToken` contract is deployed it will call the mint function passing it the current `msg.sender` as well a our defined `inital_supply`.

Compile and deploy the completed contract for the class.

![Deploy ERC20Mintable](Images/DeployArcadeTokenMintable.gif)

In the next activity the students will now be implementing their own `ERC20Mintable` token for crowdsale.
