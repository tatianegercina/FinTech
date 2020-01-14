### 3. Students Do: Building the CryptoFax Car Token (20 min)

In this activity, students will implement a non-fungible car token containing an immutable vehicle history using the ERC721 OpenZeppelin contract. This contract will require them to apply their knowledge of safemath counters, structs, and events.

**Instructions:**

* [README.md](Activities/03_Building_CryptoFax_Car_Token/README.md)

**Files:**

* [Solved](Activities/03_Building_CryptoFax_Car_Token/Solved/CryptoFax.sol)

* [Unsolved](Activities/03_Building_CryptoFax_Car_Token/Unsolved/CryptoFax.sol)

### 4. Instructor Do: ERC721 + Structs and Events Review (10 min)

Open and review the solved solution from the previous activity.

```solidity
contract CryptoFax is ERC721Full {

    constructor() ERC721Full("CryptoFax", "CARS") public { }
```

* First we inherited the properties of ERC721Full's contract in our new CryptoFax contract and called the ERC721Full's constructor passing it the name of the token  `CryptoFax` and the token symbol `Cars`.

```solidity
    using Counters for Counters.Counter;
    Counters.Counter token_ids;
```

* We used the `using for` syntax to attach the functions of the safemath library to the defined Counter type.

* To track the number of tokens that have been minted so that the next `token_id` can be generated, a custom Counter data structure from OpenZeppelin was used.

```solidity
  struct Car {
        string vin;
        uint accidents;
    }
```

* A struct was defined to hold each car's on-chain information, it's `vin` and it's number of `accidents`.

```solidity
    mapping(uint => Car) public cars;
```

* The CryptoFax contract tracks each new token that is minted by storing it's `token_id` and corresponding info for each car.

```solidity
    event Accident(uint token_id, string report_uri);
```

* Here we defined a new event called `Accident` that accepts a `uint` named `token_id`, and a `string` named  `report_uri`.

* As mentioned the data that is stored on-chain for each car token is stored in the cars `mapping`, however, accident reports are far too large to store on-chain.  Instead, it is much cheaper (in gass) to store accident reports in a decentralized storage provider such as [IPFS](https://ipfs.io/) and then reference them on-chain by hash.

* Calling an event is an easy and cheap way to permanently log a `URI` or `Uniform Resource Identifier`.

```solidity
    function registerVehicle(address owner, string memory vin, string memory token_uri) public returns(uint) {
        token_ids.increment();
        uint token_id = token_ids.current();

        _mint(owner, token_id);
        _setTokenURI(token_id, token_uri);

        cars[token_id] = Car(vin, 0);

        return token_id;
    }
```

* The `registerVehicle` function is responsible for registering a new vehicle on the chain.

* The `token_ids` counter is first incremented so that a new token can be minted; the new token id is stored as a uint named `token_id`.

* The mint function is then called passing it the owner's address from `registerVehicle` and the new `token_id`.

* The `_setTokenURI` function is then called to set the new token's `URI` based upon it's id.

* A newly defined car with a corresponsing `vin` and a given number of `accidents` is then added to the cars mapping with it's mapped `token_id` and the new token_id is returned.

```solidity
  function reportAccident(uint token_id, string memory report_uri) public returns(uint) {
        cars[token_id].accidents += 1;

        // Permanently associates the report_uri with the token_id on-chain via Events for a lower gas-cost than storing directly in the contract's storage.
        emit Accident(token_id, report_uri);

        return cars[token_id].accidents;
    }
```

* The `reportAccident`function is responsible for reporting a new accident by logging it's `report_uri`, it accepts two parameters a `uint` named `token_id` and a `string memory` represeting the `report_uri`.

* The `reportAccident` function does three things:

  * it increments the number of accidents for the given `token_id` inside the cars mapping,

  * it `emits` the `Accident` event passing it the given `token_id` and `report_uri`

  *  it returns the current number of accidents after the latest accident.

* Remember, you are `emitting` the  Accident function in order to trigger the logging of a new accident report.

* Congratulations, you've just built an `ERC721` compliant `non-fungible` token complete with on-chain custom attributes and several linked token `URI`s

Discuss the following review questions with the class:

* Why is a struct a useful data structure.

* **Answer** It allows you to create new dynamic data structures.

* **Answer** It allows you to create data structures that contain multiple types.

* **Answer** It allows you to create objects.

* What are some uses for solidity events.

* **Answer** Events are a cheap way of logging information on the blockchain.

* **Answer** Events alappsApps to update and monitor given values on the blockchain.

* What are some other examples of non-fungible tokens that could be created?

* **Answer** A token that represents a card in a cardgame.

* **Answer** A token that represents a persons debt.

* **Answer** A token that represents a certification that a person has earned.
