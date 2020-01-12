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

* A typical ERC721 token contains an attached `tokenURI`, the car token's may resolve to something like this.

  ```json
      {
          "title": "Vehicle Metadata",
          "type": "object",
          "properties": {
              "make": {
                  "type": "string",
                  "description": "Ford"
              },
              "model": {
                  "type": "string",
                  "description": "Fusion"
              },
              "year": {
                  "type": "uint",
                  "description": "2014"
              }
          }
      }
  ```

* On the next line inside of the `registerVehicle` function call the internal `_setTokenURI` method from `ERC721Full`and pass it the gnereated `token_id`,and the `token_uri` passed to the registerVehicle function.

  ```solidity
  _setTokenURI(token_id, token_uri);
  ```

* In order to register a new vehicle it's `token_id` must be stored in the defined mapping of car_tokens. On the next line of the `registerVehicle` function add the generated `token_id` and map it to a new car instace with the passed vin and `0` for the default number of accidents. Then have the `registerVehicle` function return the generted `token_id`.

  ```solidity
          cars[token_id] = Car(vin, 0);
          return token_id;
  ```

* Define a second function named `reportAccident`, this function will be responsible for reporting a new accident by logging it's `report_uri`, it accepts two parameters a `uint` named `token_id` and a `string memory` represeting the `report_uri`. Make `reportAccident` a public function that returns a `uint`.

  ```solidity
      function reportAccident(uint token_id, string memory report_uri) public returns(uint) {}
  ```

* The `reportAccident` function does three things, it increments the number of accidents for the given `token_id` inside the cars mapping, it `emits` the `Accident` event passing it the given `token_id` and `report_uri` and it returns the current number of accidents after the latest accident.

```solidity
        cars[token_id].accidents += 1;

        // Permanently associates the report_uri with the token_id on-chain via Events for a lower gas-cost than storing directly in the contract's storage.
        emit Accident(token_id, report_uri);

        return cars[token_id].accidents;
```

## Challenge

* If time remains, try registering multiple vehicles by calling the registerVehicle function in your cryptofax contract.

## Hints

* If you are struggling with any of the aspects of the OpenZeppelin ERC721 contract, take a look at the [OpenZeppelin ERC721 Documentation](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721).

* If you are still confused or would like additional clarification on solidity events checkout the [Solidity documentation on events](https://solidity.readthedocs.io/en/v0.5.3/contracts.html#events)
