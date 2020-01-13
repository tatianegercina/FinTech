### 2. Instructor Do: ERC721 Non-Fungible Tokens and Events (15 min)

In this activity, the class will be reintroduced to the ERC721 standard, review fungible vs non-fungible, and demonstrate implementing ERC721 using OpenZeppelin. You will explain the concept of events in solidity and demonstrate defining new events (appraisal, etc.) and associating them with unique ERC721 tokens.

**Files:**

* [Erc721ArtToken.sol](Activities/02_Ins_ERC721_Non-Fungible_Tokens_and_Events/Solved/Erc721ArtToken.sol)

Start by opening [Remix](https://remix.ethereum.org) in your web browser and creating a new contract named `ArtToken.sol`. Set the `pragma` and import the OpenZeppelin libraries for ERC721Full and safemath counters.

  ```solidity
  pragma solidity ^0.5.11;

  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";
  ```

* In this contract, we will be leveraging the contract for `ERC721Full` and the safemath counters data type.

Next, create a new contract named ArtToken that inherits from ERC721Full, for ERC721Full's constructor function's definition pass in the variables that ERC721Full expects, which are a `string` for the `token name` and a `string` for the token's `symbol`. Use `"ArtToken"` for the first parameter and `"ART"` for the second parameter.

  ```solidity
  contract ArtToken is ERC721Full {

      constructor() ERC721Full("ArtToken", "ART") public { }
  }
  ```

* We will be extending the `ERC721Full` contract for our ArtToken contract.

* The `ERC721Full` constructor accepts a `string` for the `token name` and a `string` for the token's `symbol`.

Now define a new counter to keep track of what current `token_id` we are on starting from 0. Apply the `using for` syntax to attach the safe math counter library to the counter type and create a new variable named `token_ids` that is of type Counters.counter.

  ```solidity
      using Counters for Counters.Counter;
      Counters.Counter token_ids;
  ```

* In order for us to track the number of tokes that have been minted and to genrate the next `token_id` we will be leveraging the custom Counter data structure from OpenZeppelin.

* Openzeppelin safemath counters allow us to increment and decrement a counter without worrying about overflows and other common types of errors.

Represent the artwork's information as a struct named `Artwork` containing these three attributes. A `string` named `name`, a `string` named artist and a `uint` named appraisal_value.

  ```solidity
      struct Artwork {
          string name;
          string artist;
          uint appraisal_value;
      }
  ```

* Each ArtToken will contain one `string` representing a piece of artworks `name`, a second `string` representing the `artist` that created the artwork, and a `uint` representing the last `appraisal_value` of the Artwork.

* In this activity, we will be using a new data structure called a `struct`.

* As you might be able to guess, struct is short for `structure`.

* Structs allow you to have `structured collections` of data within a user-defined datatype.

* As you can see, the struct that we are creating for this contract contains two `string`s and a `uint`.

* You can think of a struct kind of like a python dictionary in that they are both types of objects containing data, however, make no mistake a struct is a fundamentally different data type than a python dictionary.

Define a new `mapping` named `art_collection` that maps a `uint` to our defined Artwork data structure.

  ```solidity
      mapping(uint => Artwork) public art_collection;
  ```

* We now have to associate each instance of an artwork's information as defined in the `struct` with each art token. This is done by means of a mapping between the `token_id` and the given art tokens id.

Define a new event called `Appraisal` that will accept a `uint` named `token_id`, a second `uint` named `appraisal_value` and a string named `report_uri`.

  ```solidity
  event Appraisal(uint token_id, uint appraisal_value, string report_uri);
  ```

* The data that is stored on-chain for each art token is stored in the art_collection mapping, but appraisal reports are far too large to store on-chain.

* Instead, it is a much lower gas price to store appraisal reports in a decentralized storage provider such as IPFS and then referenced on-chain by hash. Calling an event is an easy and cheap way to permanently log a `URI` or `Uniform Resource Identifier`.

Define a function named `registerArtwork`; it accepts the following parameters:

  * address owner,

  * string memory vin

  * string memory artist

  * uint initial_value

  * string memory token_uri

  and is a `public` function that `returns` a `uint`.

  ```solidity
  function registerArtwork(address owner, string memory name, string memory artist, uint initial_value, string memory token_uri) public returns(uint) {

  }
  ```

* This function will be responsible for registering a new piece of artwork on the chain.

Add the lines of code inside the `registerArtwork` function for generating the token's id.

  ```solidity
          token_ids.increment();
          uint token_id = token_ids.current();
  ```

* Inside the body of the `registerArtwork` function you must generate the next `token_id`, this is done by incrementing the `token_ids` counter with the `.increment()` method and then by fetching the current count with the `.current()` method; storing it as a `uint` named `token_id`.

Next, inside the `registerArtwork` function call the internal `_mint` method from `ERC721Full`. Pass the `_mint` function the `owner` value that we defined and the new `token_id` that was generated.

  ```solidity
            _mint(owner, token_id);
  ```

* Now let's mint the new token.

On the next line inside of the `registerArtwork` function call the internal `_setTokenURI` method from `ERC721Full` and pass it the generated `token_id` as well as the `token_uri` that was passed to the registerArtwork function.

  ```solidity
  _setTokenURI(token_id, token_uri);
  ```

* A typical ERC721 token contains an attached `tokenURI`. Usually linking to some sort of json object.

On the next line of the `registerArtwork` function add the generated `token_id` and map it to a new artwork instace with the passed `name`, `artist`, `initial_value`. Then have the `registerArtwork` function return the generted `token_id`.

  ```solidity
          cars[token_id] = Car(vin, 0);
          return token_id;
  ```

* In order to register a piece of art it's `token_id` must be stored in the defined mapping of art tokens.

* When our `registerArtwork` function finishes creating a new artwork token it will then return the token's id.

Define a second function named `newAppraisal`, this function will be responsible for reporting a new artwork apprasialt by logging it's `report_uri`, it accepts three parameters a `uint` named `token_id`, a seocnd `uint` named `new_value` and a `string memory` represeting the `report_uri`. Make `newAppraisal` a public function that returns a `uint`.

  ```solidity
      function newAppraisal(uint token_id, uint new_value, string memory report_uri) public returns(uint) {
  ```

Inside the body of the `newAppraisal` function set the passed token_id's appraisal_value to the new_amount passed to the function. Then `emit` the `Appraisal` event passing it the given `token_id`, the `new_amount` for the last apparasial and the `report_uri`. Finally return the `new_amount` value.

  ```solidity
          art_collection[token_id].appraisal_value = new_value;

          emit Appraisal(token_id, new_value, report_uri);

          return art_collection[token_id].appraisal_value;
  ```

* This function will be responsible for reporting a new accident by logging it's `report_uri`.

* The `newAppraisal` function does three things:

  *  it increments the new appraisal amount for the given `token_id` inside the `art_collection` mapping,

  * it `emits` the `Appraisal` event passing it the given `token_id`, the `new_amount` for the last apparasial and the `report_uri`

  *  it returns the current artwork `appraisal_value` after the latest appraisal.

* We have now created a new ERC721 non-fungible token with custom attributes.
