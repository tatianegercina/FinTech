### 2. Building to a Smart Contract Specification : (15 min)

Instructor will discuss the process of breaking down the elements of a smart contract specification, such as it's interface, and how to turn it into functioning code.

**Files:**

* [Solved - CryptoRight.sol](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Solved/CryptoRight.sol)

* [Unsolved - CryptoRight.sol](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Unsolved/CryptoRightSpec.sol)

* [Example CryptoRight EIP](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md)

Begin by opening the [Example CryptoRight EIP](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md) and displaying it for the class.

* In earlier classes we took a look at a variety of the EIP specifications located on [https://eips.ethereum.org/EIPS](https://eips.ethereum.org/EIPS)

* Today we will be taking a new example EIP, and are going to be breaking it down and translating it into functioning code.

* Let's begin by identifying the goal of the current contract This will allow us to gain scope on the logic that we will be implementing.

* A good way to identify the goal of a given contract specification is by reading the `Simple Summary`, `Abstract` and `Motivation`.

Together with the class read the `Simple Summary`, `Abstract` and `Motivation` sections of the EIP.

Open [Remix](https:://remix.ethereum.org/) in your web browser and create a new contact named `CryptoRight.sol`. Define  a new contract named `CryptoRight` that extends the `ICryptoRight` interface.

```Solidity
contract CryptoRight is ICryptoRight {
}
```

Next go through each method definition inside the specification section of the EIP document and scaffold out each function with the class.

* Now that we've familiarized ourselves with the goal of the example ERC333 copyright contract lets define the structure of our contract and scaffold out each functions business logic.

* When writing code to a particular specification it can be very helpful to write comments for each step that must be performed inside a functions body. In this activity we will take the contract specification and break down each methods business logic and backing data structures into descriptive comments.

Walk through the copyright_uri interface defintion.

* copyright_uri

  * Accepts a given `copyright_id` as a `uint` and returns a `mapped string` for the copyright's `reference_uri`.

  * The ERC333 spec defines the following interface for this method.

  ```Solidity
  function copyright_uri(uint copyright_id) public returns(string memory reference_uri);
  ```

  Now demonstrate what this looks like implemented inside the smart contract

  ```Solidity
  mapping(uint => string) public copyright_uri;
  ```

  * This translates to a function defintion that looks like this.

  * The details of the method were "Accepts a given `copyright_id` as a `uint` and returns a `mapped string`".

  * Pay particular attention to the wording  "as a `uint` and returns a `mapped string`, this can be translated to "a `uint` mapped to a `string`", eg, a mapping.

  * Remember that a variable defined with the public modifier automatically generates a getter function with defined parameters. In this case our publically defined mapping `copyright_uri` generates a getter function that accepts a `uint` and retruns a `string`.

  * This is a great example of how a specifications defined interface may not always exactly match what the actual code will look like but rather the interface that will be generated.

Walk through the `copyright_owner` interface defintion.

* copyright_owner

  * Accepts a given `copyright_id` as a `uint`and returns a `mapped address` for the `copyright_owner`.

  * The ERC333 spec defines this interface for the `copyright_id` method.

  ```solidity
  function copyright_owner(uint copyright_id) public returns(address copyright_owner);
  ```

  Now demonstrate what this looks like implemented inside the smart contract

  ```Solidity
  mapping(uint => address) public copyright_owner;
  ```

  * This translates to code that looks like this inside the smart contract.

  * Once again pay particular attention to the wording  "as a `uint` and returns a `mapped address`, this can be translated to "a `uint` mapped to an `address`", eg, a public mapping.

Walk through the `openSourceWork` interface defintion.

* openSourceWork

  ```Solidity
  function openSourceWork(string memory reference_uri) public
  ```

  * The ERC333 spec defines this interface for the `openSourceWork`  method.

  ```Solidity
    function openSourceWork(string memory reference_uri) public {
    }
  ```

  * This translates to code that looks  like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

* Generates a new `copyright_id` of type `uint` and maps it to a given `reference_uri` by calling `copyright_uri`.

```Solidity
    function openSourceWork(string memory reference_uri) public {
      // Increment the copyright_ids counter with .increment() method.

     // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    // Map the copyright_id to the given reference uri using the copyright_uri mapping.

    // no need to set address(0) in the copyright_owner mapping as this is already the default for empty address types
    }
  ```

* The `openSourceWork` method description can be broken down into the following steps.

  * Increment the copyright_ids counter with .increment() method.

  * Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

  * Map the copyright_id to the given reference uri using the copyright_uri mapping.

  * Also make the observation that since this type of copyright is `open source` there is no need to set `address(0)` because in the copyright_owner mapping this is already the default for empty address types.

Next add the code implementation for each commented step inside the `openSourceWork` method.

```Solidity
    function openSourceWork(string memory reference_uri) public {
     // Increment the copyright_ids counter with .increment() method.

     copyright_ids.increment();

     // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    uint id = copyright_ids.current();

    // Map the copyright_id to the given reference uri using the copyright_uri mapping.

    copyright_uri[id] = reference_uri;

    // no need to set address(0) in the copyright_owner mapping as this is already the default for empty address types

    }
  ```
