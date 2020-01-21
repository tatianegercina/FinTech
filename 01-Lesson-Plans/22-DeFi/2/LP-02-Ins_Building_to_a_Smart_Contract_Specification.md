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

Walk through the copyrights interface defintion.

* copyrights

  * Accepts a given `copyright_id` as a `uint` and returns a `mapped struct` containing the copyright's `owner` and `uri`.

  ```Solidity
  function copyright_uri(uint copyright_id) public returns(string memory reference_uri);
  ```

  * The ERC333 spec defines this interface for the copyrights method.

  Now demonstrate what this looks like implemented inside the smart contract

  ```Solidity
  mapping(uint => string) public copyright_uri;
  ```

  * This translates to a function defintion that looks like this.

  * The details of the method were "Accepts a given `copyright_id` as a `uint` and returns a `mapped string`".

  * Pay particular attention to the wording  "as a `uint` and returns a `mapped string`, this can be translated to "a `uint` mapped to a `string`", eg, a mapping.

  * Remember that a variable defined with the public modifier automatically generates a getter function with defined parameters. In this case our publically defined mapping `copyright_uri` generates a getter function that accepts a `uint` and retruns a `string`.

  * This is a great example of how a specification's defined interface may not always exactly match what the actual code will look like but rather the interface that will be generated.

Walk through the `copyrightWork` method interface defintion.

* copyrightWork

  ```Solidity
  function copyrightWork(string memory reference_uri) public
  ```

  * The ERC333 spec defines this interface for the `openSourceWork` method.

  ```Solidity
  function copyrightWork(string memory reference_uri) public {
  }
  ```

  * This translates to code that looks like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

* Generates a new `copyright_id` of type `uint` and maps it to a `Work struct` containing the given copyright `owner` and `uri`.

```Solidity
    function copyrightWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    // Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyright_uri mapping.

    }
  ```

* The `openSourceWork` method description can be broken down into the following steps.

  * Increment the copyright_ids counter with .increment() method.

  * Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

  * Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyright_uri mapping.

Next add the code implementation for each commented step inside the `copyrightWork` method.

```Solidity
    function copyrightWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.
    copyright_ids.increment();

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.
    uint id = copyright_ids.current();

    // Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyright_uri mapping.
    copyrights[id] = Work(msg.sender, reference_uri);

    }
```

Walk through the `openSourceWork`method  interface defintion.

* openSourceWork

  ```Solidity
  function openSourceWork(string memory reference_uri) public
  ```

  * The ERC333 spec defines this interface for the `openSourceWork` method.

  ```Solidity
  function openSourceWork(string memory reference_uri) public {
  }
  ```

  * This translates to code that looks  like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

* Generates a new `copyright_id` of type `uint` and maps it to a `Work struct` containing the `uri`.

```Solidity
    function openSourceWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    // Map the copyright_id to a Work struct containing the given uri using the copyright_uri mapping.

    // No need to set address(0) in the copyrights mapping as this is already the default for empty address types
    }
  ```

* The `openSourceWork` method description can be broken down into the following steps.

  * Increment the copyright_ids counter with .increment() method.

  * Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

  * Map the copyright_id to a Work struct containing the given uri using the copyright_uri mapping.

  * Also make the observation that since this type of copyright is `open source` there is no need to set `address(0)` because in the copyrights mapping this is already the default for empty address types.

Next add the code implementation for each commented step inside the `openSourceWork` method.

```Solidity
    function openSourceWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.
    copyright_ids.increment();

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.
    uint id = copyright_ids.current();

    // Map the copyright_id to the given reference uri using the copyright_uri mapping.
    copyright_uri[id] = reference_uri;

    // No need to set address(0) in the copyrights mapping as this is already the default for empty address types

    }
  ```

Walk through the `transferCopyrightOwnership` method interface defintion.

* transferCopyrightOwnership

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
```

  * The ERC333 spec defines this interface for the `transferCopyrightOwnership` method.

  ```Solidity
     function transferCopyrightOwnership(uint
    }
  ```

  * This translates to code that looks like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

* Re-maps a given copyright_id to a new copyright owner.

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        //Re-maps a given copyright_id to a new copyright owner.

    }
```

* As you can see the `transferCopyrightOwnership` method is relatively simple, the description can be copied into a single comment consisting of the exact description text.

Next add the code implementation for each commented step inside the `transferCopyrightOwnership` method.

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        //Re-maps a given copyright_id to a new copyright owner.
        copyrights[copyright_id].owner = new_owner;
    }
```

* Here we are passing our given `copyright_id` into our `copyrights mapping` in order to set the `owner` attribute to the `address` of the given `new_owner`

Walk through the `renounceCopyrightOwnership` method interface defintion.

* renounceCopyrightOwnership

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id)
```

  * The ERC333 spec defines this interface for the `renounceCopyrightOwnership` method.

  ```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
    }
  ```

* This translates to code that looks like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

* Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
    }
```

* Here the important part of the method descripton is "Re-maps a given copyright_id to the 0x0000000000000000000000000000000000000000".

* Remember we've already impelmented a function that is able to re-map a copyright to a new owner's address called `transferCopyrightOwnership`.

Next add the code implementation for each commented step inside the `renounceCopyrightOwnership` method.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
      transferCopyrightOwnership(copyright_id, address(0));

    }
```

* Here we call the previously `transferCopyrightOwnership` method passing it the given `copyright_id` and `address(0)`.

* Mapping something to `address(0)` in effect makes it so that nonone can ever control that copyright, eg, it becomes `open source`.
