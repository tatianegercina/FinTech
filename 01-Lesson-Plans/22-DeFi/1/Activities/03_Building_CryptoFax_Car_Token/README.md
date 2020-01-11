# Building the CryptoFax Car Token

In this activity, you will implement a non-fungible car token containing an immutable vehicle history using the ERC721 OpenZeppelin contract. This contract will require you to apply your knowledge of safemath counters, structs, and events.

## Instructions

* Define your new contract's  `pragma` as ^0.5.11.

```solidity
pragma solidity ^0.5.11;
```

* Import the OpenZeppelin libraries for `ERC721Full` and `safemath counters`.

```solidity

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";

```

* Create a new contract named `CryptoFax` that inherits from ERC721Full and for ERC721Full's constructor function's definition, perform the following:

  * Pass in the variables that ERC721Full expects, which are `string name`, `string symbol` Use the following values:

    * `"CryptoFax"` for the first parameter.

    * `"CARS"` as the second.

* The contract with the constructor call should look something like this:

  ```solidity
  contract ContractName is ERC721Full {
    constructor() ERC721Full("TokenName", "TKN") public { }
  }
  ```

* Next, create a new counter to keep track of what current token_id we are on starting from 0. Apply the `using for` syntax to attach the safe math counter library to the counter type and create a new variable named `token_ids` that is of type `Counters.counter`.

```solidity
using Counters for Counters.Counter;
Counters.Counter token_ids;
```

* Each cryptofax car token will contain a `string` representing the vehicle's `vin` and a `uint` that tracks the number of accidents the vehicle has had. Represent this information as a `struct` named `Car ` containing two attributes `string vin` and `uint accidents`.

```solidity
    struct Car {
        string vin;
        uint accidents;
    }
```

* You now have to associate each instance of a car's information as defined in the struct with each car token. This is done by means of a mapping between the token_id and the given car. Define a new `mapping` named `cars` that maps a `uint` to our defined `Car` data structure.

```solidity
    mapping(uint => Car) public cars;
```

* The data that is stored on-chain for each car token is stored in the cars `mapping`, but accident reports are far too large to store on-chain.  Instead, it is a much gas price to store accident reports in a decentralized storage provider such as `IPFS` and then referenced on-chain by hash. Calling an event is an easy and cheap way to permanently log a `URI` or `Uniform Resource Identifier`. Define a new event called `Accident` that will accept a `uint` named `token_id`, and a `string` named  `report_uri`.

```solidity
    event Accident(uint token_id, string report_uri);
```

* Add a function named `registerVehicle`. This function will be responsible for registering a new vehicle on the chain; it accepts the following parameters

  * address owner,

  * string memory vin

  * string memory token_uri

and is a `public` function that `returns` a `uint`.

```solidity
function registerVehicle(address owner, string memory vin, string memory token_uri) public returns(uint) {}
```

* Inside the body of the `registerVehicle` function you must generate the next token_id; this is done by incrementing the `token_ids` counter with the `.increment()` method and then by fetching the current count with the `.current()` method; storing it as a `uint` named `token_id`.

```solidity
        token_ids.increment();
        uint token_id = token_ids.current();
```

* Next, inside the `registerVehicle` function call the internal `_mint` method from `ERC721Full`. Pass the `_mint` function the `owner` value that we defined and the new `token_id` that was generated.

```solidity
        _mint(owner, token_id);
```

## Challenge

* If time remains, try registering multiple vehicles by calling the registerVehicle function in your cryptofax contract.

## Hints

* In case you are struggling with any of the aspects of the OpenZeppelin ERC721 contract, take a look at the [OpenZeppelin ERC721 Documentation](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721).

* If you are still confused or would like additional clarification on solidity events checkout the [Solidity documentation on events](https://solidity.readthedocs.io/en/v0.5.3/contracts.html#events)
